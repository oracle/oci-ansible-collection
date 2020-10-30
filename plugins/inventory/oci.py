# Copyright (c) 2020, Oracle and/or its affiliates.
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
            choices: ['oracle.oci.oci']
        config_file:
            description: The oci config path.
            env:
               - name: OCI_CONFIG_FILE
        config_profile:
             description: The config profile to use.
             env:
               - name: OCI_CONFIG_PROFILE
        api_user_key_file:
            description: Full path and filename of the private key (in PEM format). If the key is encrypted with
                         a pass-phrase, the pass_phrase option must also be provided.
                         Preference order is .oci.yml > OCI_USER_KEY_FILE environment variable > settings from config file
                         This option is required if the private key is not specified through a configuration
                         file (See config_file)
            type: str
            env:
                - name: OCI_USER_KEY_FILE
        api_user_key_pass_phrase:
            description: Passphrase used by the key referenced in api_user_key_file, if it is encrypted.
                         Preference order is .oci.yml > OCI_USER_KEY_PASS_PHRASE environment variable > settings from config file
                         This option is required if the passphrase is not specified through a configuration
                         file (See config_file)
            type: str
            env:
                - name: OCI_USER_KEY_PASS_PHRASE
        instance_principal_authentication:
             description: Use instance principal based authentication.
                 If not set, the API key in your config will be used.
             env:
               - name: OCI_ANSIBLE_AUTH_TYPE
        enable_parallel_processing:
              description: Use multiple threads to speedup lookup. Default is set to True
        regions:
             description: A list of regions to search. If not specified, the region is read from config file. Use 'all'
                          to generate inventory from all subscribed regions.
        hostnames:
             description: A list of hostnames to search for.
        hostname_format:
             description: Host naming format to use. Use 'fqdn' to list hosts using the instance's
                          Fully Qualified Domain Name (FQDN). These FQDNs are resolvable within the VCN using the VCN
                          resolver specified through the subnet's DHCP options. Please see
                          https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm for more details.
                          Use 'public_ip' to list hosts using public IP address. Use 'private_ip' to list hosts using
                          private IP address. By default, hosts are listed using public IP address.
             env:
               - name: OCI_HOSTNAME_FORMAT
        filters:
             description: A dictionary of filter value pairs. Available filters  are
                 display_name, lifecycle_state, availability_domain, defined_tags, freeform_tags.
        fetch_db_hosts:
             description: When set, the db nodes are also fetched.
        compartments:
            description: A dictionary of compartment identifier to obtain list of hosts. This config parameter is
                         optional. If compartment is not specified, the plugin fetches all compartments from
                         the tenancy
            type: list
            suboptions:
                compartment_ocid:
                    description: OCID of the compartment. If None, root compartment is assumed to be the default value.
                    type: str
                compartment_name:
                    description: Name of the compartment. If None and `compartment_ocid` is not set, all the
                                 compartments including the root compartment are returned.
                    type: str
                fetch_hosts_from_subcompartments:
                    description: Flag used to fetch hosts from subcompartments. Default value is set to True
                    type: boolean
                parent_compartment_ocid:
                    description: This option is not needed when the compartment_ocid option is used, it is needed when
                                 compartment_name is used. OCID of the parent compartment. If None, root compartment
                                 is assumed to be parent.
                    type: str
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
    fetch_hosts_from_subcompartments: false

  - compartment_name: "test_compartment"
    parent_compartment_ocid: ocid1.tenancy.oc1..xxxxxx

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

# DB Hosts
fetch_db_hosts: True
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
from collections import deque, defaultdict
from multiprocessing.pool import ThreadPool
from functools import partial
from contextlib import contextmanager

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_config_utils,
    oci_common_utils,
    oci_version,
)

try:
    import oci
    from oci.core.compute_client import ComputeClient
    from oci.identity.identity_client import IdentityClient
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.database import DatabaseClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError
except ImportError:
    raise AnsibleError("The oci dynamic inventory plugin requires oci python sdk.")


class InventoryModule(BaseInventoryPlugin, Constructable, Cacheable):
    NAME = "oracle.oci.oci"
    LIFECYCLE_ACTIVE_STATE = "ACTIVE"
    LIFECYCLE_RUNNING_STATE = "RUNNING"
    LIFECYCLE_ATTACHED_STATE = "ATTACHED"

    def __init__(self):
        super(InventoryModule, self).__init__()

        self.inventory = None
        self.config = {}
        self.compartments = None
        self._identity_client = None
        self._region_subscriptions = None
        self.regions = {}
        self.enable_parallel_processing = True
        self.compartments_info = None
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
            "fetch_hosts_from_subcompartments": True,
            "debug": False,
            "hostname_format": None,
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

    def _get_key_file(self):
        # preference order: .oci.yml > environment variable > settings from config file
        if self.get_option("api_user_key_file") is not None:
            self.params["key_file"] = os.path.expanduser(
                self.get_option("api_user_key_file")
            )
        elif "OCI_USER_KEY_FILE" in os.environ:
            self.params["key_file"] = os.path.expanduser(
                os.path.expandvars(os.environ.get("OCI_USER_KEY_FILE"))
            )

    def _get_pass_phrase(self):
        # preference order: .oci.yml > environment variable > settings from config file
        if self.get_option("api_user_key_pass_phrase") is not None:
            self.params["pass_phrase"] = self.get_option("api_user_key_pass_phrase")
        elif "OCI_USER_KEY_PASS_PHRASE" in os.environ:
            self.params["pass_phrase"] = os.path.expandvars(
                os.environ.get("OCI_USER_KEY_PASS_PHRASE")
            )

    def _get_hostname_format(self):
        # Preference order: .oci.yml > environment variable
        if self.get_option("hostname_format"):
            return self.get_option("hostname_format")
        if os.environ.get("OCI_HOSTNAME_FORMAT"):
            return os.environ.get("OCI_HOSTNAME_FORMAT")
        return "public_ip"

    def read_config(self):

        self._get_config_file()
        # Read values from config file
        if os.path.isfile(to_bytes(self.params["config_file"])):
            self.config = oci.config.from_file(
                file_location=self.params["config_file"],
                profile_name=self.params["profile"],
            )

        self.config["additional_user_agent"] = (
            oci_config_utils.inventory_agent_name + oci_version.__version__
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

    @property
    def region_subscriptions(self):
        if self._region_subscriptions:
            return self._region_subscriptions
        if not self.params["tenancy"]:
            raise Exception("Tenancy OCID required to get the region subscriptions.")
        self._region_subscriptions = oci_common_utils.call_with_backoff(
            self.identity_client.list_region_subscriptions,
            tenancy_id=self.params["tenancy"],
        ).data
        return self._region_subscriptions

    @property
    def identity_client(self):
        if self._identity_client:
            return self._identity_client
        self._identity_client = self.create_service_client(IdentityClient)
        return self._identity_client

    def log(self, *args, **kwargs):
        if self.params["debug"]:
            self.display.warning(*args, **kwargs)
        pass

    def setup_clients(self, regions):
        """
            :param regions: A list of regions to create  clients

        """
        self.regions = regions

        self._compute_clients = dict(
            (region, self.create_service_client(ComputeClient, region=region))
            for region in self.regions
        )

        self._virtual_nw_clients = dict(
            (region, self.create_service_client(VirtualNetworkClient, region=region))
            for region in self.regions
        )

        self._database_clients = dict(
            (region, self.create_service_client(DatabaseClient, region=region))
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

    def _fetch_db_hosts(self):
        # check if we should fetch db hosts
        return self.get_option("fetch_db_hosts")

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

        self.compartments = dict()

        if self.compartments_info:
            fetching_hosts_from_all_compartments = False
            for key, value in self.compartments_info.items():
                compartments = self.get_compartments(
                    compartment_ocid=value.get("compartment_ocid"),
                    parent_compartment_ocid=value.get("parent_compartment_ocid"),
                    compartment_name=value.get("compartment_name"),
                    fetch_hosts_from_subcompartments=value.get(
                        "fetch_hosts_from_subcompartments"
                    ),
                )

                for compartment in compartments:
                    if compartment.id in self.compartments:
                        self.display.warning(
                            "Obtained the the compartment {0} twice, picking up the later entry in the list".format(
                                compartment.id
                            )
                        )
                    if value.get("fetch_hosts_from_subcompartments") and (
                        "tenancy" in compartment.id
                    ):
                        fetching_hosts_from_all_compartments = True
                        self.display.warning(
                            "Config given to fetch hosts from all compartments, skipping reading the "
                            "compartments list further if there are any present"
                        )
                    self.compartments[compartment.id] = compartment
                if fetching_hosts_from_all_compartments:
                    break
        else:
            # fetch all compartments in tenancy
            compartments = self.get_compartments()
            for compartment in compartments:
                self.compartments[compartment.id] = compartment

        if not self.compartments:
            self.display.warning("No compartments matching the criteria.")
            return

        all_instances = self.get_instances(self.compartments)
        instance_inventories = [
            self.build_inventory_for_instance(instance, region)
            for region in all_instances
            for instance in all_instances[region]
        ]

        if self._fetch_db_hosts():
            all_db_hosts = self.get_db_hosts(self.compartments)

            instance_inventories += [
                self.build_inventory_for_db_host(db_host, region)
                for region in all_db_hosts
                for db_host in all_db_hosts[region]
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

    def get_db_hosts(self, compartment_ocids):
        """Get and return instances from all the specified compartments and regions.

        :param compartment_ocids: List of compartment ocid's to fetch the instances from
        :return: dict with region as key and list of db nodes of the region as value
        """
        db_hosts = defaultdict(list)

        if self.get_option("enable_parallel_processing"):
            for region in self.regions:
                num_threads = min(
                    len(compartment_ocids), self.params["max_thread_count"]
                )
                self.display.warning(
                    "Parallel processing enabled. Getting db hosts from {0} in {1} threads.".format(
                        region, num_threads
                    )
                )

                with self.pool(processes=num_threads) as pool:
                    get_filtered_db_hosts_for_region = partial(
                        self.get_filtered_db_hosts, region=region
                    )
                    lists_of_instances = pool.map(
                        get_filtered_db_hosts_for_region, compartment_ocids
                    )
                for sublist in lists_of_instances:
                    db_hosts[region].extend(sublist)

        else:
            for region in self.regions:
                for compartment_ocid in compartment_ocids:
                    db_hosts[region].extend(
                        self.get_filtered_db_hosts(compartment_ocid, region)
                    )

        return db_hosts

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
            Only applicable when compartment_name or compartment_ocid is specified. When set to true, the entire
            hierarchy of compartments of the given compartment is returned.
        :raises ServiceError: When the Service returned an Error response
        :raises MaximumWaitTimeExceededError: When maximum wait time is exceeded while invoking target_fn
        :return: list of :class:`~oci.identity.models.Compartment`
        """
        if compartment_ocid:
            try:
                compartment_with_ocid = oci_common_utils.call_with_backoff(
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
            tenancy = oci_common_utils.call_with_backoff(
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
            for compartment in oci_common_utils.list_all_resources(
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
                for compartment in oci_common_utils.list_all_resources(
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
            if hasattr(instance, "freeform_tags"):
                for key in instance.freeform_tags:
                    tag_group_name = self.sanitize(
                        "tag_" + key + "=" + instance.freeform_tags[key]
                    )
                    common_groups.add(tag_group_name)

            # Group by defined tags
            if hasattr(instance, "defined_tags"):
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
                for vnic_attachment in oci_common_utils.list_all_resources(
                    target_fn=compute_client.list_vnic_attachments,
                    compartment_id=compartment.id,
                    instance_id=instance.id,
                )
                if self.filter_resource(
                    vnic_attachment, lifecycle_state=self.LIFECYCLE_ATTACHED_STATE
                )
            ]

            for vnic_attachment in vnic_attachments:

                vnic = oci_common_utils.call_with_backoff(
                    virtual_nw_client.get_vnic, vnic_id=vnic_attachment.vnic_id
                ).data
                self.log(
                    "VNIC {0} is attached to instance {1}.".format(
                        vnic.id, vnic_attachment.instance_id
                    )
                )

                subnet = oci_common_utils.call_with_backoff(
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
            self.log(
                "Final inventory for {0}.".format(
                    str(self.get_resource_for_logging(instance_inventory))
                )
            )
            return instance_inventory

        except ServiceError as ex:
            if ex.status == 401:
                self.log(ex)
                raise
            self.log(ex)

    def build_inventory_for_db_host(self, db_host, region):
        """Build and return inventory for a database host"""
        try:
            db_host_inventory = {}
            virtual_nw_client = self.get_virtual_nw_client_for_region(region)
            compartment = self.compartments[db_host.compartment_id]

            db_host_vars = to_dict(db_host)

            common_groups = set(["all_hosts", "db_hosts"])
            # Group by availability domain
            ad = self.sanitize(db_host.availability_domain)
            common_groups.add(ad)

            # Group by compartments
            compartment_name = self.sanitize(compartment.name)
            common_groups.add(compartment_name)

            # Group by region
            region_grp = self.sanitize("region_" + region)
            common_groups.add(region_grp)

            # Group by freeform tags tag_key=value
            if hasattr(db_host, "freeform_tags"):
                for key in db_host.freeform_tags:
                    tag_group_name = self.sanitize(
                        "tag_" + key + "=" + db_host.freeform_tags[key]
                    )
                    common_groups.add(tag_group_name)

            # Group by defined tags
            if hasattr(db_host, "defined_tags"):
                for namespace in db_host.defined_tags:
                    for key in db_host.defined_tags[namespace]:
                        defined_tag_group_name = self.sanitize(
                            namespace
                            + "#"
                            + key
                            + "="
                            + db_host.defined_tags[namespace][key]
                        )
                        common_groups.add(defined_tag_group_name)

            if not db_host.vnic_id:
                return None

            vnic = oci_common_utils.call_with_backoff(
                virtual_nw_client.get_vnic, vnic_id=db_host.vnic_id
            ).data

            self.log("VNIC {0} is attached to db_host {1}.".format(vnic.id, db_host.id))

            subnet = oci_common_utils.call_with_backoff(
                virtual_nw_client.get_subnet, subnet_id=vnic.subnet_id
            ).data

            db_host_vars.update({"vcn_id": subnet.vcn_id})
            db_host_vars.update({"vnic_id": vnic.id})
            db_host_vars.update({"subnet_id": vnic.subnet_id})
            db_host_vars.update({"public_ip": vnic.public_ip})
            db_host_vars.update({"private_ip": vnic.private_ip})

            host_name = self.get_host_name(vnic, region=region)

            # Skip host which is not addressable using hostname_format
            if not host_name:
                if self.params["strict_hostname_checking"] == "yes":
                    raise Exception(
                        "Instance with OCID: {0} does not have a valid hostname.".format(
                            db_host.id
                        )
                    )
                self.log("Skipped instance with OCID:" + db_host.id)
                return None

            host_name = self.sanitize(host_name)

            groups = set(common_groups)

            self.display.warning("Creating inventory for host {0}.".format(host_name))
            self.create_instance_inventory_for_host(
                db_host_inventory, host_name, vars=db_host_vars, groups=groups
            )
            self.log("Final inventory for {0}.".format(str(db_host_inventory)))
            return db_host_inventory

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

    def get_filtered_resources(self, resources, compartment_ocid):

        self.log(
            "Resources before filtering from compartment {0}:{1}".format(
                compartment_ocid, self.get_resources_for_logging(resources)
            )
        )
        filters = ["display_name", "availability_domain", "lifecycle_state"]
        resources = [
            resource
            for resource in resources
            if all(
                True
                if not self.filters.get(filter)
                or getattr(resource, filter, None) == self.filters[filter]
                else False
                for filter in filters
            )
        ]

        if self.filters.get("freeform_tags"):
            resources = [
                resource
                for resource in resources
                if all(
                    hasattr(resource, "freeform_tags")
                    and resource.freeform_tags.get(key) == value
                    for key, value in six.iteritems(self.filters["freeform_tags"])
                )
            ]
            self.display.warning(
                "Resources in compartment {0} which match all the freeform tags: {1}".format(
                    compartment_ocid, self.get_resources_for_logging(resources)
                )
            )
        if self.filters.get("defined_tags"):
            resources = [
                resource
                for resource in resources
                if all(
                    (
                        hasattr(resource, "defined_tags")
                        and resource.defined_tags.get(namespace, {})
                    ).get(key)
                    == value
                    for namespace in self.filters["defined_tags"]
                    for key, value in six.iteritems(
                        self.filters["defined_tags"][namespace]
                    )
                )
            ]
            self.display.warning(
                "Resources in compartment {0} which match all the freeform & defined tags: {1}".format(
                    compartment_ocid, self.get_resources_for_logging(resources)
                )
            )
        self.log(
            "Resources after filtering from compartment {0}:{1}".format(
                compartment_ocid, self.get_resources_for_logging(resources)
            )
        )
        return resources

    def get_resource_for_logging(self, resource):
        """Return the resource with any sensitive data removed"""
        if not resource:
            return dict()
        NO_LOG_KEYS = ["metadata"]
        # this covers the case where we are logging instance inventory
        if isinstance(resource, dict):
            for v in six.itervalues(resource):
                if isinstance(v, dict) and v.get("vars"):
                    v["vars"] = dict(
                        (k, v)
                        for k, v in six.iteritems(v["vars"])
                        if k not in NO_LOG_KEYS
                    )
        return dict(
            (k, v) for k, v in six.iteritems(to_dict(resource)) if k not in NO_LOG_KEYS
        )

    def get_resources_for_logging(self, resources):
        """Return the resource with any sensitive data removed"""
        if not resources:
            return []
        return [self.get_resource_for_logging(resource) for resource in resources]

    def get_resource_with_attributes(self, resource, **kwargs):
        """Add the given kwargs as attributes to the resource"""
        if not kwargs:
            return resource
        for key, value in six.iteritems(kwargs):
            if hasattr(resource, key):
                continue
            # for now only string types are supported
            if not isinstance(value, six.string_types):
                continue
            setattr(resource, key, value)
            # also add attr to the swagger_types so that it is returned when converted to dict using to_dict
            if hasattr(resource, "swagger_types"):
                resource.swagger_types[key] = "str"
        return resource

    def get_filtered_db_hosts(self, compartment_ocid, region):
        try:
            database_client = self.get_database_client_for_region(region)

            db_hosts = self.get_filtered_resources(
                [
                    self.get_resource_with_attributes(
                        db_node,
                        availability_domain=db_system.availability_domain,
                        compartment_id=db_system.compartment_id,
                    )
                    for db_system in oci_common_utils.list_all_resources(
                        target_fn=database_client.list_db_systems,
                        compartment_id=compartment_ocid,
                    )
                    for db_node in oci_common_utils.list_all_resources(
                        database_client.list_db_nodes,
                        compartment_id=compartment_ocid,
                        db_system_id=db_system.id,
                    )
                    if db_node.lifecycle_state == "AVAILABLE"
                ],
                compartment_ocid,
            )
            return db_hosts

        except ServiceError as ex:
            if ex.status == 401:
                self.display.warning(ex)
                raise
            self.display.warning(ex)
            return []

    def get_filtered_instances(self, compartment_ocid, region):
        try:
            compute_client = self.get_compute_client_for_region(region)

            instances = self.get_filtered_resources(
                oci_common_utils.list_all_resources(
                    target_fn=compute_client.list_instances,
                    compartment_id=compartment_ocid,
                    lifecycle_state="RUNNING",
                ),
                compartment_ocid,
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
                "Could not fetch the virtual network client for region {0}.".format(
                    region
                )
            )
        return self._virtual_nw_clients[region]

    def get_database_client_for_region(self, region):
        if region not in self._database_clients:
            raise ValueError(
                "Could not fetch the database client for region {0}.".format(region)
            )
        return self._database_clients[region]

    def get_host_name(self, vnic, region):
        virtual_nw_client = self.get_virtual_nw_client_for_region(region)
        if self.params["hostname_format"] == "fqdn":
            subnet = oci_common_utils.call_with_backoff(
                virtual_nw_client.get_subnet, subnet_id=vnic.subnet_id
            ).data
            vcn = oci_common_utils.call_with_backoff(
                virtual_nw_client.get_vcn, vcn_id=subnet.vcn_id
            ).data

            oraclevcn_domain_name = ".oraclevcn.com"
            if not (vnic.hostname_label and subnet.dns_label and vcn.dns_label):
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
                            if host_inventory["vars"].get("display_name"):
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

        self.compartments_info = dict()
        it = 0
        for item in options["compartments"]["value"]:
            self.log(" compartments item: {0}".format(item))
            self.compartments_info[it] = dict()
            if "compartment_ocid" in item:
                self.compartments_info[it]["compartment_ocid"] = item[
                    "compartment_ocid"
                ]
            if "parent_compartment_ocid" in item:
                self.compartments_info[it]["parent_compartment_ocid"] = item[
                    "parent_compartment_ocid"
                ]
            if "compartment_name" in item:
                self.compartments_info[it]["compartment_name"] = item[
                    "compartment_name"
                ]
            if "fetch_hosts_from_subcompartments" in item:
                self.compartments_info[it]["fetch_hosts_from_subcompartments"] = item[
                    "fetch_hosts_from_subcompartments"
                ]
            it += 1

        regions = options["regions"]["value"]
        if "all" in regions:
            if len(regions) > 1:
                raise AnsibleError(
                    "Found conflicting values for regions. Cannot specify other regions when using 'all'"
                )
            self.log(
                "Inventory requested for all regions. Fetching all subsribed regions."
            )
            regions = [
                region_subscription.region_name
                for region_subscription in self.region_subscriptions
            ]
            self.log("Subscribed regions: {0}.".format(regions))
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

        # read the key_file and passphrase
        self._get_key_file()
        self._get_pass_phrase()

        regions, filters, hostnames = self._get_query_options(config_data)

        # hostname format
        self.params["hostname_format"] = self._get_hostname_format()
        self.log("Using hostname format {0}".format(self.params["hostname_format"]))

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
