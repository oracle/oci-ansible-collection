# Copyright (c) 2019, Oracle and/or its affiliates.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
    name: oci
    plugin_type: inventory
    short_description: Oracle Cloud Infrastructure (OCI) inventory plugin
    extends_documentation_fragment:
        - inventory_cache
        - constructed
    description:
        - Get inventory hosts from oci.
        - Uses a <name>.oci.yaml (or <name>.oci.yml) YAML configuration file.
    options:
        plugin:
            description: token that ensures this is a source file for the 'oci' plugin.
            required: True
            choices: ['oci']
        config_file:
            description: The oci config path.
            env:
               - name: OCI_CONFIG_FILE
        config_profile:
             description: The config profile to use.
             env:
               - name: OCI_CONFIG_PROFILE
        instance_principal_authentication:
             description: Use instance principal based authentication.
                 If not set, the API key in your config will be used.
             env:
               - name: OCI_ANSIBLE_AUTH_TYPE
        enable_parallel_processing:
              description: Use multiple threads to speedup lookup.
        regions:
             description: A list of regions to search. If not specified, the region is read from config file.
        hostnames:
             description: A list of hostnames to search for.
        filters:
             description: A dictionary of filter value pairs. Available filters  are
                 display_name, lifecycle_state, availability_domain, defined_tags, freeform_tags.
"""

EXAMPLES = """
# Fetch all hosts
plugin: oci

# Optional fields:
config_file: ~/.oci/config
config_profile: DEFAULT

# Example select regions
regions:
  - us-ashburn-1
  - us-phoenix-1

# Enable threads to speedup lookup
enable_parallel_processing: yes

# Select compartment by ocid or name
compartments:
  - compartment_ocid: ocid1.compartment.oc1..xxxxxx
  - compartment_name: "test"

# Example filtering using hostname IP
hostnames:
  - "11.145.214.11"

# Example group results by key
keyed_groups:
  - key: availability_domain

# Example using filters
filters:
  - availability_domain: "IwGV:US-ASHBURN-AD-3"
  - display_name: "instance20190506231645"
  - lifecycle_state: "RUNNING"
  - defined_tags: {
     "ansible_tag_2": {
       "ansibletag448": "test_value"
      }
    }
  - freeform_tags: {
     "oci:compute:instanceconfiguration": "ocid1.instanceconfiguration.oc1.phx.xxxx",
     "oci:compute:instancepool": "ocid1.instancepool.oc1.phx.xxxx"
    }

# Enable Cache
cache: yes
cache_plugin: jsonfile
cache_timeout: 7200
cache_connection: /tmp/oci-cache
cache_prefix: oci_
"""
import os
import re
import json


from ansible.errors import AnsibleError, AnsibleParserError
from ansible.module_utils._text import to_bytes
from ansible.module_utils.six import string_types
from ansible.plugins.inventory import BaseInventoryPlugin, Constructable, Cacheable
from ansible.utils.display import Display

from ansible.module_utils import six
from ansible.module_utils.oracle import oci_utils, oci_config_utils, oci_common_utils
from collections import deque, defaultdict
from multiprocessing.pool import ThreadPool
from functools import partial
from contextlib import contextmanager

try:
    import oci
    from oci.retry import RetryStrategyBuilder
    from oci.constants import HEADER_NEXT_PAGE
    from oci.core.compute_client import ComputeClient
    from oci.identity.identity_client import IdentityClient
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError
except ImportError:
    raise AnsibleError("The oci dynamic inventory plugin requires oci python sdk.")


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):

    NAME = "oci"
    LIFECYCLE_ACTIVE_STATE = "ACTIVE"
    LIFECYCLE_RUNNING_STATE = "RUNNING"
    LIFECYCLE_ATTACHED_STATE = "ATTACHED"

    def __init__(self):
        super(InventoryModule, self).__init__()

        self.inventory = None
        self.config = {}
        self.compartments = None
        self._region_subscriptions = None
        self.regions = {}
        self.params = {
            "config_file": os.path.join(os.path.expanduser("~"), ".oci", "config"),
            "profile": "DEFAULT",
            "user": None,
            "fingerprint": None,
            "key_file": None,
            "tenancy": None,
            "region": None,
            "pass_phrase": None,
            # other options
            "compartment_ocid": None,
            "compartment_name": None,
            "parent_compartment_ocid": None,
            "fetch_hosts_from_subcompartments": False,
            "debug": False,
            "hostname_format": "public_ip",
            "sanitize_names": True,
            "replace_dash_in_names": False,
            "max_thread_count": 50,
            "freeform_tags": None,
            "defined_tags": None,
            "regions": None,
            "strict_hostname_checking": "no",
            "filters": None,
        }

        self.group_prefix = "oci_"
        self.display = Display()

    def _get_config_file(self):
        """
            :param config_data: contents of the inventory config file
        """
        # Preference order: .oci.yml > environment variable > settings from config file.
        if self.get_option("config_file") is not None:
            self.params["config_file"] = os.path.expanduser(
                self.get_option("config_file")
            )
        elif "OCI_CONFIG_FILE" in os.environ:
            self.params["config_file"] = os.path.expanduser(
                os.path.expandvars(os.environ.get("OCI_CONFIG_FILE"))
            )

        if self.get_option("config_profile") is not None:
            self.params["profile"] = self.get_option("config_profile")
        elif "OCI_CONFIG_PROFILE" in os.environ:
            self.params["profile"] = os.environ.get("OCI_CONFIG_PROFILE")

    def read_config(self):

        self._get_config_file()
        # Read values from config file
        if os.path.isfile(to_bytes(self.params["config_file"])):
            self.config = oci.config.from_file(
                file_location=self.params["config_file"],
                profile_name=self.params["profile"],
            )

        self.config["additional_user_agent"] = (
            oci_config_utils.inventory_agent_name + oci_common_utils.__version__
        )
        self.log(self.config["additional_user_agent"])

        for setting in self.config:
            self.params[setting] = self.config[setting]

    def read_settings_config(self, boolean_options, dict_options):
        if self.settings_config.has_section("oci"):
            for option in self.settings_config.options("oci"):
                if option in boolean_options:
                    self.params[option] = self.settings_config.getboolean("oci", option)
                elif option in dict_options:
                    self.params[option] = json.loads(
                        self.settings_config.get("oci", option)
                    )
                else:
                    self.params[option] = self.settings_config.get("oci", option)

    def log(self, *args, **kwargs):
        if self.params["debug"]:
            self.display.warning(*args, **kwargs)
        pass

    def setup_clients(self, regions):
        """
            :param regions: A list of regions to create  clients

        """
        self.regions = regions

        self.identity_client = self.create_service_client(IdentityClient)

        self._compute_clients = dict(
            (region, self.create_service_client(ComputeClient, region=region))
            for region in self.regions
        )

        self._virtual_nw_clients = dict(
            (region, self.create_service_client(VirtualNetworkClient, region=region))
            for region in self.regions
        )

    def create_service_client(self, service_client_class, region=None):
        if not region:
            region = self.params["region"]
        params = dict(self.params, region=region)
        kwargs = {}
        if self._is_instance_principal_auth():
            kwargs["signer"] = self.create_instance_principal_signer()

        # Create service client class with the signer.
        client = service_client_class(params, **kwargs)

        return client

    def _is_instance_principal_auth(self):
        # check if auth is set to `instance_principal`.
        return self.get_option("instance_principal_authentication")

    @staticmethod
    def create_instance_principal_signer():
        try:
            signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
        except Exception as ex:
            raise Exception(
                "Failed retrieving certificates from localhost. Instance principal based authentication is only"
                "possible from within OCI compute instances. Exception: {0}".format(
                    str(ex)
                )
            )
        return signer

    @contextmanager
    def pool(self, **kwargs):
        pool = ThreadPool(**kwargs)
        try:
            yield pool
        finally:
            pool.close()
            # wait for all the instances to be processed
            pool.join()
            # terminate the pool
            pool.terminate()

    def _get_instances_by_region(self, regions):
        """
           :param regions: a list of regions in which to describe instances
           :return A list of instance dictionaries
        """
        self.setup_clients(regions)

        self.display.warning("Building inventory.")

        # Compartments(including the root compartment) from which the instances are to be retrieved.
        self.compartments = dict(
            (compartment.id, compartment)
            for compartment in self.get_compartments(
                compartment_ocid=self.params["compartment_ocid"],
                parent_compartment_ocid=self.params["parent_compartment_ocid"],
                compartment_name=self.params["compartment_name"],
            )
        )

        if not self.compartments:
            self.display.warning("No compartments matching the criteria.")
            return

        all_instances = self.get_instances(self.compartments)

        instance_inventories = [
            self.build_inventory_for_instance(instance, region)
            for region in all_instances
            for instance in all_instances[region]
        ]

        return instance_inventories

    def get_instances(self, compartment_ocids):
        """Get and return instances from all the specified compartments and regions.

        :param compartment_ocids: List of compartment ocid's to fetch the instances from
        :return: dict with region as key and list of instances of the region as value
        """
        instances = defaultdict(list)

        if self.get_option("enable_parallel_processing"):
            for region in self.regions:
                num_threads = min(
                    len(compartment_ocids), self.params["max_thread_count"]
                )
                self.display.warning(
                    "Parallel processing enabled. Getting instances from {0} in {1} threads.".format(
                        region, num_threads
                    )
                )

                with self.pool(processes=num_threads) as pool:
                    get_filtered_instances_for_region = partial(
                        self.get_filtered_instances, region=region
                    )
                    lists_of_instances = pool.map(
                        get_filtered_instances_for_region, compartment_ocids
                    )
                for sublist in lists_of_instances:
                    instances[region].extend(sublist)

        else:
            for region in self.regions:
                for compartment_ocid in compartment_ocids:
                    instances[region].extend(
                        self.get_filtered_instances(compartment_ocid, region)
                    )

        return instances

    def get_compartments(
        self,
        compartment_ocid=None,
        parent_compartment_ocid=None,
        compartment_name=None,
        fetch_hosts_from_subcompartments=True,
    ):
        """
        Get the compartments based on the parameters passed. When compartment_name is None, all the compartments
        including the root compartment is returned.

        When compartment_name is passed, the compartment with that name and its hierarchy of compartments are returned
        if fetch_hosts_from_subcompartments is true.

        The tenancy is returned when compartment_name is the tenancy name.

        :param str compartment_ocid: (optional)
            OCID of the compartment. If None, root compartment is assumed to be parent.
        :param str parent_compartment_ocid: (optional)
            OCID of the parent compartment. If None, root compartment is assumed to be parent.
        :param str compartment_name: (optional)
            Name of the compartment. If None and :attr:`compartment_ocid` is not set, all the compartments including
            the root compartment are returned.
        :param str fetch_hosts_from_subcompartments: (optional)
            Only applicable when compartment_name is specified. When set to true, the entire hierarchy of compartments
            of the given compartment is returned.
        :raises ServiceError: When the Service returned an Error response
        :raises MaximumWaitTimeExceededError: When maximum wait time is exceeded while invoking target_fn
        :return: list of :class:`~oci.identity.models.Compartment`
        """
        if compartment_ocid:
            try:
                compartment_with_ocid = oci_utils.call_with_backoff(
                    self.identity_client.get_compartment,
                    compartment_id=compartment_ocid,
                ).data
            except ServiceError as se:
                if se.status == 404:
                    raise Exception(
                        "Compartment with OCID {0} either does not exist or "
                        "you do not have permission to access it.".format(
                            compartment_ocid
                        )
                    )
            else:
                if not fetch_hosts_from_subcompartments:
                    return [compartment_with_ocid]
                return self.get_sub_compartments(compartment_with_ocid)

        if not self.params["tenancy"]:
            raise Exception(
                "Tenancy OCID required to get the compartments in the tenancy."
            )

        try:
            tenancy = oci_utils.call_with_backoff(
                self.identity_client.get_compartment,
                compartment_id=self.params["tenancy"],
            ).data
        except ServiceError as se:
            if se.status == 404:
                raise Exception(
                    "Either tenancy ocid is invalid or need inspect permission on root compartment to get the "
                    "compartments in the tenancy."
                )

        all_compartments = [tenancy] + [
            compartment
            for compartment in oci_utils.list_all_resources(
                target_fn=self.identity_client.list_compartments,
                compartment_id=self.params["tenancy"],
                compartment_id_in_subtree=True,
            )
            if self.filter_resource(
                compartment, lifecycle_state=self.LIFECYCLE_ACTIVE_STATE
            )
        ]

        # return all the compartments if compartment_name is not passed
        if not compartment_name:
            return all_compartments

        if compartment_name == tenancy.name:
            # return all the compartments when fetch_hosts_from_subcompartments is true
            if fetch_hosts_from_subcompartments:
                return all_compartments
            else:
                return [tenancy]

        if not parent_compartment_ocid:
            parent_compartment_ocid = tenancy.id

        compartment_with_name = None
        for compartment in all_compartments:
            if (
                compartment.name == compartment_name
                and compartment.compartment_id == parent_compartment_ocid
            ):
                compartment_with_name = compartment
                break

        if not compartment_with_name:
            raise Exception(
                "Compartment with name {0} not found.".format(compartment_name)
            )

        if not fetch_hosts_from_subcompartments:
            return [compartment_with_name]

        return self.get_sub_compartments(compartment_with_name)

    @staticmethod
    def filter_resource(resource, **kwargs):
        for key, val in six.iteritems(kwargs):
            if getattr(resource, key, None) != val:
                return False
        return True

    def get_sub_compartments(self, root):
        # OCI SDK does not support fetching sub-compartments for non root compartments
        # So traverse the compartment tree to fetch all the sub compartments
        compartments = []
        queue = deque()
        queue.append(root)
        while len(queue) > 0:
            parent_compartment = queue.popleft()
            compartments.append(parent_compartment)
            child_compartments = [
                compartment
                for compartment in oci_utils.list_all_resources(
                    target_fn=self.identity_client.list_compartments,
                    compartment_id=parent_compartment.id,
                )
                if self.filter_resource(
                    compartment, lifecycle_state=self.LIFECYCLE_ACTIVE_STATE
                )
            ]
            for child_compartment in child_compartments:
                queue.append(child_compartment)
        return compartments

    def build_inventory_for_instance(self, instance, region):
        """Build and return inventory for an instance"""
        try:
            instance_inventory = {}
            compute_client = self.get_compute_client_for_region(region)
            virtual_nw_client = self.get_virtual_nw_client_for_region(region)
            compartment = self.compartments[instance.compartment_id]

            instance_vars = to_dict(instance)

            common_groups = set(["all_hosts"])
            # Group by availability domain
            ad = self.sanitize(instance.availability_domain)
            common_groups.add(ad)

            # Group by compartments
            compartment_name = self.sanitize(compartment.name)
            common_groups.add(compartment_name)

            # Group by region
            region_grp = self.sanitize("region_" + region)
            common_groups.add(region_grp)

            # Group by freeform tags tag_key=value
            for key in instance.freeform_tags:
                tag_group_name = self.sanitize(
                    "tag_" + key + "=" + instance.freeform_tags[key]
                )
                common_groups.add(tag_group_name)

            # Group by defined tags
            for namespace in instance.defined_tags:
                for key in instance.defined_tags[namespace]:
                    defined_tag_group_name = self.sanitize(
                        namespace
                        + "#"
                        + key
                        + "="
                        + instance.defined_tags[namespace][key]
                    )
                    common_groups.add(defined_tag_group_name)

            vnic_attachments = [
                vnic_attachment
                for vnic_attachment in oci_utils.list_all_resources(
                    target_fn=compute_client.list_vnic_attachments,
                    compartment_id=compartment.id,
                    instance_id=instance.id,
                )
                if self.filter_resource(
                    vnic_attachment, lifecycle_state=self.LIFECYCLE_ATTACHED_STATE
                )
            ]

            for vnic_attachment in vnic_attachments:

                vnic = oci_utils.call_with_backoff(
                    virtual_nw_client.get_vnic, vnic_id=vnic_attachment.vnic_id
                ).data
                self.log(
                    "VNIC {0} is attached to instance {1}.".format(
                        vnic.id, vnic_attachment.instance_id
                    )
                )

                subnet = oci_utils.call_with_backoff(
                    virtual_nw_client.get_subnet, subnet_id=vnic.subnet_id
                ).data

                if instance_vars.get("id") == vnic_attachment.instance_id:
                    instance_vars.update({"vcn_id": subnet.vcn_id})
                    instance_vars.update({"vnic_id": vnic.id})
                    instance_vars.update({"subnet_id": vnic.subnet_id})
                    instance_vars.update({"public_ip": vnic.public_ip})
                    instance_vars.update({"private_ip": vnic.private_ip})

                host_name = self.get_host_name(vnic, region=region)

                # Skip host which is not addressable using hostname_format
                if not host_name:
                    if self.params["strict_hostname_checking"] == "yes":
                        raise Exception(
                            "Instance with OCID: {0} does not have a valid hostname.".format(
                                vnic_attachment.instance_id
                            )
                        )
                    self.log(
                        "Skipped instance with OCID:" + vnic_attachment.instance_id
                    )
                    return None

                host_name = self.sanitize(host_name)

                groups = set(common_groups)

                self.display.warning(
                    "Creating inventory for host {0}.".format(host_name)
                )
                self.create_instance_inventory_for_host(
                    instance_inventory, host_name, vars=instance_vars, groups=groups
                )
            self.log("Final inventory for {0}.".format(str(instance_inventory)))
            return instance_inventory

        except ServiceError as ex:
            if ex.status == 401:
                self.log(ex)
                raise
            self.log(ex)

    def create_instance_inventory_for_host(
        self, instance_inventory, host_name, vars, groups
    ):
        instance_inventory.setdefault(host_name, {"groups": {}, "vars": {}})
        instance_inventory[host_name]["vars"] = vars
        for group in groups:
            instance_inventory[host_name]["groups"].setdefault(group, {"children": []})

        return instance_inventory

    def sanitize(self, word):
        # regex represents an invalid non-alphanumeric character except UNDERSCORE, HASH, EQUALS and DOT
        regex = r"[^A-Za-z0-9_#=."
        if self.params["sanitize_names"]:
            if not self.params["replace_dash_in_names"]:
                # Add DASH as a valid character in regex.
                regex += r"-"

            # Replace all invalid characters with UNDERSCORE
            return re.sub(regex + "]", "_", word)
        return word

    def get_filtered_instances(self, compartment_ocid, region):
        try:
            compute_client = self.get_compute_client_for_region(region)

            instances = oci_utils.list_all_resources(
                target_fn=compute_client.list_instances,
                compartment_id=compartment_ocid,
                lifecycle_state="RUNNING",
            )
            self.log(
                "All RUNNING instances from compartment {0}:{1}".format(
                    compartment_ocid, instances
                )
            )

            # Data is cached so filter using all of the data not using the API
            if "display_name" in self.filters and self.filters["display_name"]:
                instances = [
                    instance
                    for instance in instances
                    if (instance.display_name == self.filters["display_name"])
                ]

            if (
                "availability_domain" in self.filters
                and self.filters["availability_domain"]
            ):
                instances = [
                    instance
                    for instance in instances
                    if (
                        instance.availability_domain
                        == self.filters["availability_domain"]
                    )
                ]

            if "lifecycle_state" in self.filters and self.filters["lifecycle_state"]:
                instances = [
                    instance
                    for instance in instances
                    if (instance.lifecycle_state == self.filters["lifecycle_state"])
                ]

            if "freeform_tags" in self.filters and self.filters["freeform_tags"]:
                instances = [
                    instance
                    for instance in instances
                    if all(
                        instance.freeform_tags.get(key) == value
                        for key, value in six.iteritems(self.filters["freeform_tags"])
                    )
                ]
                self.display.warning(
                    "Instances in compartment {0} which match all the freeform tags: {1}".format(
                        compartment_ocid, instances
                    )
                )
            if "defined_tags" in self.filters and self.filters["defined_tags"]:
                instances = [
                    instance
                    for instance in instances
                    if all(
                        (instance.defined_tags.get(namespace, {})).get(key) == value
                        for namespace in self.filters["defined_tags"]
                        for key, value in six.iteritems(
                            self.filters["defined_tags"][namespace]
                        )
                    )
                ]
                self.display.warning(
                    "Instances in compartment {0} which match all the freeform & defined tags: {1}".format(
                        compartment_ocid, instances
                    )
                )
            return instances
        except ServiceError as ex:
            if ex.status == 401:
                self.display.warning(ex)
                raise
            self.display.warning(ex)
            return []

    def get_compute_client_for_region(self, region):
        if region not in self._compute_clients:
            raise ValueError(
                "Could not fetch the compute client for region {0}.".format(region)
            )
        return self._compute_clients[region]

    def get_virtual_nw_client_for_region(self, region):
        if region not in self._compute_clients:
            raise ValueError(
                "Could not fetch the virtual network for region {0}.".format(region)
            )
        return self._virtual_nw_clients[region]

    def get_host_name(self, vnic, region):
        virtual_nw_client = self.get_virtual_nw_client_for_region(region)
        if self.params["hostname_format"] == "fqdn":
            subnet = oci_utils.call_with_backoff(
                virtual_nw_client.get_subnet, subnet_id=vnic.subnet_id
            ).data
            vcn = oci_utils.call_with_backoff(
                virtual_nw_client.get_vcn, vcn_id=subnet.vcn_id
            ).data

            oraclevcn_domain_name = ".oraclevcn.com"
            if not (vnic.hostname_label or subnet.dns_label or vcn.dns_label):
                return None
            fqdn = (
                vnic.hostname_label
                + "."
                + subnet.dns_label
                + "."
                + vcn.dns_label
                + oraclevcn_domain_name
            )
            self.display.warning("FQDN for VNIC: {0} is {1}.".format(vnic.id, fqdn))
            return fqdn

        elif self.params["hostname_format"] == "private_ip":
            self.display.warning(
                "Private IP for VNIC: {0} is {1}.".format(vnic.id, vnic.private_ip)
            )
            return vnic.private_ip

        return vnic.public_ip

    def _query(self, regions):
        """
            :param regions: a list of regions to query
        """
        return self._get_instances_by_region(regions)

    def _populate(self, instance_inventories, hostnames):
        for instance_inventory in instance_inventories:
            if instance_inventory:
                for host_name, host_inventory in six.iteritems(instance_inventory):
                    if not hostnames or host_name in hostnames:
                        for group in host_inventory["groups"]:
                            self.inventory.add_group(group)
                            self.inventory.add_host(host_name, group=group)
                            self.inventory.set_variable(
                                host_name,
                                host_inventory["vars"]["display_name"],
                                host_inventory["vars"],
                            )
                            self.inventory.add_child("all", host_name)
                            self._set_composite_vars(
                                self.get_option("compose"),
                                host_inventory["vars"],
                                host_name,
                            )
                            self._add_host_to_composed_groups(
                                self.get_option("groups"),
                                host_inventory["vars"],
                                host_name,
                            )
                            self._add_host_to_keyed_groups(
                                self.get_option("keyed_groups"),
                                host_inventory["vars"],
                                host_name,
                            )

    def verify_file(self, path):
        """
            :param loader: an ansible.parsing.dataloader.DataLoader object
            :param path: the path to the inventory config file
            :return the contents of the config file
        """
        if super(InventoryModule, self).verify_file(path):
            if path.endswith(".oci.yml") or path.endswith(".oci.yaml"):
                return True

    def _get_query_options(self, config_data):
        """
            :param config_data: contents of the inventory config file
            :return A list of regions to query
                    a list of possible hostnames
        """
        options = {
            "regions": {"type_to_be": list, "value": config_data.get("regions", [])},
            "compartments": {
                "type_to_be": list,
                "value": config_data.get("compartments", []),
            },
            "filters": {"type_to_be": list, "value": config_data.get("filters", [])},
            "hostnames": {
                "type_to_be": list,
                "value": config_data.get("hostnames", []),
            },
        }

        # validate the options
        for name in options:
            options[name]["value"] = self._validate_option(
                name, options[name]["type_to_be"], options[name]["value"]
            )

        filters = dict((key, d[key]) for d in options["filters"]["value"] for key in d)
        self.filters = filters

        for item in options["compartments"]["value"]:
            self.display.warning(" --- compartments item: {0}   ".format(item))
            if "compartment_ocid" in item:
                self.params["compartment_ocid"] = item["compartment_ocid"]
            if "parent_compartment_ocid" in item:
                self.params["parent_compartment_ocid"] = item["parent_compartment_ocid"]
            if "compartment_name" in item:
                self.params["compartment_name"] = item["compartment_name"]

        regions = options["regions"]["value"]
        hostnames = options["hostnames"]["value"]

        return regions, filters, hostnames

    def _validate_option(self, name, desired_type, option_value):
        """
            :param name: the option name
            :param desired_type: the class the option needs to be
            :param option: the value the user has provided
            :return The option of the correct class
        """

        if isinstance(option_value, string_types) and desired_type == list:
            option_value = [option_value]

        if option_value is None:
            option_value = desired_type()

        if not isinstance(option_value, desired_type):
            raise AnsibleParserError(
                "The option %s (%s) must be a %s" % (name, option_value, desired_type)
            )

        return option_value

    def parse(self, inventory, loader, path, cache=True):
        super(InventoryModule, self).parse(inventory, loader, path)

        config_data = self._read_config_data(path)
        # read oci config
        self.read_config()

        regions, filters, hostnames = self._get_query_options(config_data)

        cache_key = self.get_cache_key(path)

        if not regions:
            regions = [self.params["region"]]

        # false when refresh_cache
        if cache:
            cache = self.get_option("cache")

        # Generate inventory
        cache_needs_update = False
        if cache:
            try:
                cached_results = self._cache[cache_key]
            except Exception:
                # cache expired or cache file doesn't exist
                cache_needs_update = True
            else:
                self.display.warning("Using cached results")
                self._populate(cached_results, hostnames)

        results = None
        if not cache or cache_needs_update:
            results = self._query(regions)
            self._populate(results, hostnames)

        # update the cached inventory
        if cache_needs_update or (not cache and self.get_option("cache")):
            self._cache[cache_key] = results
