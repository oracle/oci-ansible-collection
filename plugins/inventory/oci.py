# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
             description:
                - This parameter is DEPRECATED. Please use auth_type instead.
                - Use instance principal based authentication.
                  If not set, the API key in your config will be used.
        auth_type:
            description:
                - The type of authentication to use for making API requests. By default C(auth_type="api_key") based
                  authentication is performed and the API key (see I(api_user_key_file)) in your config file will be
                  used. If this 'auth_type' module option is not specified, the value of the OCI_ANSIBLE_AUTH_TYPE,
                  if any, is used. Use C(auth_type="instance_principal") to use instance principal based authentication
                  when running ansible playbooks within an OCI compute instance.
            choices: ['api_key', 'instance_principal', 'instance_obo_user', 'resource_principal']
            default: 'api_key'
            type: str
            env:
               - name: OCI_ANSIBLE_AUTH_TYPE
        delegation_token_file:
            description:
                - Path to delegation_token file. If not set then the value of the OCI_DELEGATION_TOKEN_FILE environment variable,
                  if any, is used. Otherwise, defaults to config_file.
                - This parameter is only applicable when C(auth_type=instance_obo_user) is set.
            type: str
            env:
                - name: OCI_DELEGATION_TOKEN_FILE
        enable_parallel_processing:
              description: Use multiple threads to speedup lookup. Default is set to True
        regions:
             description: A list of regions to search. If not specified, the region is read from config file. Use 'all'
                          to generate inventory from all subscribed regions.
             type: list
        hostnames:
             description: A list of hostnames to search for.
             type: list
        hostname_format_preferences:
            description: A list of Jinja2 expressions in order of precedence to compose inventory_hostname.
                         Ignores expression if result is an empty string or None value.
                         hostname_format_preferences and hostname_format cannot be used together.
                         The instance is ignored if none of the hostname_format_preferences resulted in a non-empty value
            type: list
        hostname_format:
             description: Host naming format to use. Use 'fqdn' to list hosts using the instance's
                          Fully Qualified Domain Name (FQDN). These FQDNs are resolvable within the VCN using the VCN
                          resolver specified through the subnet's DHCP options. Please see
                          https://docs.us-phoenix-1.oraclecloud.com/Content/Network/Concepts/dns.htm for more details.
                          Use 'public_ip' to list hosts using public IP address. Use 'private_ip' to list hosts using
                          private IP address. Use 'display_name' to list hosts using display_name of the Instances.
                          'display_name' cannot be used when fetch_db_hosts is True. By default, hosts are listed using public IP address.
                          hostname_format_preferences and hostname_format cannot be used together
             env:
               - name: OCI_HOSTNAME_FORMAT
        filters:
             description:
               - A dictionary of filter value pairs.
               - Available filters are display_name, lifecycle_state, availability_domain, defined_tags, freeform_tags.
               - "Note: defined_tags and freeform_tags filters are not supported for db hosts. The db hosts will not
                 be returned when you use either of these filters."
             type: list
        exclude_host_filters:
             description: A list of Jinja2 conditional expressions. Each expression in the list is evaluated for each host;
                          when any of the expressions is evaluated to Truthy value, the host is excluded from the inventory.
                          exclude_host_filters take priority over the include_host_filters and filters.
             type: list
        include_host_filters:
             description: A list of Jinja2 conditional expressions. Each expression in the list is evaluated for each host;
                          when any of the expressions is evaluated to Truthy value, the host is included in the inventory.
                          include_host_filters and filters options cannot be used together.
             type: list
        fetch_db_hosts:
             description: When set, the db nodes are also fetched. Default value set to False.
             type: bool
        fetch_compute_hosts:
             description: When set, the compute nodes are fetched. Default value set to True.
             type: bool
        primary_vnic_only:
            description: The default behavior of the plugin is to process all VNIC's attached to a compute instance.
                         This might result in instance having multiple entries. When this parameter is set to True,
                         the plugin will only process the primary VNIC and thus having only a single entry for
                         each compute instance.
            type: bool
            env:
                - name: OCI_PRIMARY_VNIC_ONLY
        debug:
            description: Parameter to enable logs while running the inventory plugin. Default value is set to False
            type: boolean
        compartments:
            description: A dictionary of compartment identifier to obtain list of hosts. This config parameter is optional.
                         If compartment is not specified, the plugin fetches all compartments from the tenancy.
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
        exclude_compartments:
            description: A dictionary of compartment identifier to filter the compartments from which  hosts should be listed from.
                         This config parameter is optional.
                         Suboption is not considered when both compartment_ocid, compartment_name are None
            type: list
            suboptions:
                compartment_ocid:
                    description: OCID of the compartment.
                    type: str
                compartment_name:
                    description: Name of the compartment. If None and `compartment_ocid` is not set,
                                 this option is not considered for filtering the compartments.
                                 If both compartment_ocid and compartment_name are passed, compartment_ocid is considered
                    type: str
                skip_subcompartments:
                    description: Flag used to skip the sub-compartments. Default value is set to True
                    type: boolean
                parent_compartment_ocid:
                    description: This option is not needed when the compartment_ocid option is used, it is needed when
                                 compartment_name is used. OCID of the parent compartment. If None, root compartment
                                 is assumed to be parent.
                    type: str
        default_groups:
            description:  OCI Inventory plugin creates some groups by default based on these properties
                          ["availability_domain", "compartment_name", "region", "freeform_tags", "defined_tags"].
                          If you don't want OCI inventory plugin to create these default groups,
                          you can use this option to configure which of these default groups should be created.
                          This option takes a list of properties of inventory hosts based on which the groups will be created.
                          The supported properties are
                          - "availability_domain"
                          - "compartment_name"
                          - "region"
                          - "freeform_tags"
                          - "defined_tags"
                          if empty list is passed to this option, none of the default groups are created.
            type: list
"""

EXAMPLES = """
# Please check https://docs.oracle.com/en-us/iaas/Content/API/SDKDocs/ansibleinventoryintro.htm
# for more scenario based examples.

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

# Sets the inventory_hostname to either "display_name+'.oci.com'" or id
# "'display_name+'.oci.com'" has more preference than id
hostname_format_preferences:
  - "display_name+'.oci.com'"
  - "id"

# Excludes host that is not in the region 'iad' from the inventory
exclude_host_filters:
  - "region not in ['iad']"

# Includes only the hosts that has display_name ending with '.oci.com' in the inventory
include_host_filters:
  - "display_name is match('.*.oci.com')"

# Example group results by key
keyed_groups:
  - key: availability_domain

# Example to create and modify a host variable
compose:
  ansible_host: display_name+'.oracle.com'

# Example flag to turn on debug mode
debug: true

# Enable Cache
cache: yes
cache_plugin: jsonfile
cache_timeout: 7200
cache_connection: /tmp/oci-cache
cache_prefix: oci_

# DB Hosts
fetch_db_hosts: True

# Compute Hosts (bool type)
fetch_compute_hosts: True

# Process only the primary vnic of a compute instance
primary_vnic_only: True

# Select compartment by ocid or name
exclude_compartments:
  - compartment_ocid: ocid1.compartment.oc1..xxxxxx
    skip_subcompartments: false

  - compartment_name: "test_skip_compartment"
    parent_compartment_ocid: ocid1.tenancy.oc1..xxxxxx

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
    from oci.auth.signers.resource_principals_signer import (
        get_resource_principals_signer,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


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
        self.exclude_compartments_info = None
        self.exclude_compartments = dict()
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
            "filters": None,
            "primary_vnic_only": False,
            "auth_type": "api_key",
            "delegation_token_file": None,
            "default_groups": []
        }

        self.group_prefix = "oci_"
        self.display = Display()
        self.supported_default_groups = ["availability_domain", "compartment_name", "region", "freeform_tags", "defined_tags"]

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
        # preference order: .oci.yml > environment variable > settings from config file.
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

    def _get_hostname_from_preference(self, host_vars):
        hostname_format_preferences = (
            self.get_option("hostname_format_preferences") or []
        )
        host_vars = host_vars or {}
        hostname = None
        for preference in hostname_format_preferences:
            try:
                hostname = self._compose(preference, host_vars)
            except Exception as e:
                self.debug(
                    "Error occurred while composing hostname_format_preferences - {0} to hostname -  {1}".format(
                        preference, str(e)
                    )
                )
                if self.get_option("strict"):
                    raise AnsibleError(
                        "Error occurred while composing hostname_format_preferences - {0} to hostname -  {1}".format(
                            preference, str(e)
                        )
                    )
            if hostname:
                return hostname
        return None

    def _validate_config(self):
        self._validate_hostname_format()
        self._validate_filters()
        self._validate_default_groups()

    def _validate_hostname_format(self):
        hostname_format = self.params.get("hostname_format")
        hostname_format_preferences = self.get_option("hostname_format_preferences")
        if hostname_format_preferences and self.get_option("hostname_format"):
            raise AnsibleError(
                "hostname_format and hostname_format_preferences cannot be used together"
            )
        if hostname_format == "display_name" and self._fetch_db_hosts():
            raise AnsibleError(
                "The hostname_format %s is not supported for db_hosts"
                % (hostname_format)
            )

    def _validate_default_groups(self):
        for group in self.params.get("default_groups"):
            if group not in self.supported_default_groups:
                raise AnsibleError("The default_group %s is not supported" % group)

    def _validate_filters(self):
        static_filter = self.get_option("filters")
        include_filter = self.get_option("include_host_filters")
        if static_filter and include_filter:
            raise AnsibleError(
                "The options filters and include_host_filters cannot be used together"
            )

    def _get_primary_vnic_only(self):
        # Preference order: .oci.yml > environment variable
        if self.get_option("primary_vnic_only"):
            return self.get_option("primary_vnic_only")
        if os.environ.get("OCI_PRIMARY_VNIC_ONLY"):
            return os.environ.get("OCI_PRIMARY_VNIC_ONLY")
        return False

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
        self.debug(self.config["additional_user_agent"])

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

    def debug(self, *args, **kwargs):
        if self.params["debug"]:
            self.display.display(*args, **kwargs)
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
        """
        Creates a service client using the common module options provided by the user.
        :param module: An AnsibleModule that represents user provided options for a Task
        :param service_client_class: A class that represents a client to an OCI Service
        :param client_kwargs: kwargs that would be passed to the client class
        :return: A fully configured client
        """
        if not region:
            region = self.params["region"]
        params = dict(self.params, region=region)
        kwargs = {}
        if self._is_instance_principal_auth():
            self.params["auth_type"] = "instance_principal"
            kwargs["signer"] = self.create_instance_principal_signer()

        elif self._is_delegation_token_auth():
            self.params["auth_type"] = "instance_obo_user"
            delegation_token_location = self._get_delegation_token_file()
            kwargs["signer"] = self.create_instance_principal_signer(
                delegation_token_location=delegation_token_location
            )

        elif self._is_resource_principal_auth():
            self.params["auth_type"] = "resource_principal"
            kwargs["signer"] = get_resource_principals_signer()
        self.debug("auth_type : {0}".format(self.params["auth_type"]))
        # Create service client class with the signer.
        client = service_client_class(params, **kwargs)

        return client

    def _is_instance_principal_auth(self):
        # check if auth is set to `instance_principal`. Support for backward compatibility.
        if self.get_option("instance_principal_authentication") == "instance_principal":
            self.debug(
                "instance_principal_authentication parameter is DEPRECATED. Please use auth_type parameter instead."
            )
            return True
        # check if auth type is overridden via module params
        if self.get_option("auth_type") == "instance_principal":
            return True
        elif (
            self.get_option("auth_type") is None
            and os.environ.get("OCI_ANSIBLE_AUTH_TYPE") == "instance_principal"
        ):
            return True
        return False

    def _is_delegation_token_auth(self):
        # check if auth type is overridden via module params
        if self.get_option("auth_type") == "instance_obo_user":
            return True
        elif (
            self.get_option("auth_type") is None
            and os.environ.get("OCI_ANSIBLE_AUTH_TYPE") == "instance_obo_user"
        ):
            return True
        return False

    def _is_resource_principal_auth(self):
        if self.get_option("auth_type") == "resource_principal":
            return True
        elif (
            self.get_option("auth_type") is None
            and os.environ.get("OCI_ANSIBLE_AUTH_TYPE") == "resource_principal"
        ):
            return True
        return False

    def _get_delegation_token_file(self):
        if self.get_option("delegation_token_file") is not None:
            self.params["delegation_token_file"] = os.path.expanduser(
                self.get_option("delegation_token_file")
            )
        elif "OCI_DELEGATION_TOKEN_FILE" in os.environ:
            self.params["delegation_token_file"] = os.environ.get(
                "OCI_DELEGATION_TOKEN_FILE"
            )
        return self.params.get("delegation_token_file")

    def _fetch_db_hosts(self):
        # check if we should fetch db hosts
        if self.get_option("fetch_db_hosts") is None:
            return False
        return self.get_option("fetch_db_hosts")

    def _fetch_compute_hosts(self):
        # check if we should fetch compute hosts
        if self.get_option("fetch_compute_hosts") is None:
            return True
        return self.get_option("fetch_compute_hosts")

    @staticmethod
    def create_instance_principal_signer(delegation_token_location=None):
        """
        Creates a signer for API authentication.
        :param delegation_token_location: path for delegation_token file. If None, Instance_Principal signer will be created.
        :return: A signer for authentication
        """
        signer = None
        try:
            if delegation_token_location:  # instance_obo_user
                signer_kwargs = {}
                delegation_token = None
                # expand file location
                expanded_location = os.path.expanduser(delegation_token_location)
                if not os.path.exists(expanded_location):
                    raise IOError(
                        "ERROR: delegation_token_file not found at {0}".format(
                            expanded_location
                        )
                    )
                # read from file
                with open(expanded_location, "r") as delegation_token_file:
                    delegation_token = delegation_token_file.read().strip()
                # check if token is there
                if not delegation_token:
                    raise ValueError(
                        "ERROR: delegation_token not found in file {0}".format(
                            expanded_location
                        )
                    )
                # fill up kwarg
                signer_kwargs["delegation_token"] = delegation_token
                # create instance_principal_delegation_auth signer
                signer = oci.auth.signers.InstancePrincipalsDelegationTokenSigner(
                    **signer_kwargs
                )
            else:
                signer = oci.auth.signers.InstancePrincipalsSecurityTokenSigner()
        except (ValueError, IOError):
            raise
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

    def get_compartments_from_compartment_info(self, compartments_info_items):
        """
        gets the compartments from compartments_info which is passed in the option compartments
        """
        compartments_result = dict()
        fetching_hosts_from_all_compartments = False
        for key, value in compartments_info_items:
            compartments = self.get_compartments(
                compartment_ocid=value.get("compartment_ocid"),
                parent_compartment_ocid=value.get("parent_compartment_ocid"),
                compartment_name=value.get("compartment_name"),
                fetch_hosts_from_subcompartments=value.get(
                    "fetch_hosts_from_subcompartments"
                ),
            )

            for compartment in compartments:
                if compartment.id in compartments_result:
                    self.debug(
                        "Obtained the the compartment {0} twice, picking up the later entry in the list".format(
                            compartment.id
                        )
                    )
                if value.get("fetch_hosts_from_subcompartments") and (
                    "tenancy" in compartment.id
                ):
                    fetching_hosts_from_all_compartments = True
                    self.debug(
                        "Config given to fetch hosts from all compartments, skipping reading the "
                        "compartments list further if there are any present"
                    )
                compartments_result[compartment.id] = compartment
            if fetching_hosts_from_all_compartments:
                break
        return compartments_result

    def get_compartments_from_exclude_compartment_info(self):
        """
        gets the compartments with compartment_ocids from exclude_compartments
        """
        exclude_compartments = dict()
        for key, value in self.exclude_compartments_info.items():
            if value.get("compartment_ocid", None):
                exclude_compartments.update({value.get("compartment_ocid"): value})
            elif value.get("compartment_name", None):
                compartment = self.get_compartment_from_compartment_name(
                    parent_compartment_ocid=value.get("parent_compartment_ocid", None),
                    compartment_name=value.get("compartment_name", None),
                    fetch_hosts_from_subcompartments=False,
                    exclude_compartments={},
                )
                exclude_compartments.update({compartment[0].id: value})
        return exclude_compartments

    def get_all_compartments(self):
        """
        gets all the compartments excluding the compartments configured in exclude_compartments
        """
        compartments_result = dict()
        if self.exclude_compartments_info:
            self.exclude_compartments = (
                self.get_compartments_from_exclude_compartment_info()
            )

        if self.compartments_info:
            compartments_result = self.get_compartments_from_compartment_info(
                self.compartments_info.items()
            )
        else:
            # fetch all compartments in tenancy
            compartments = self.get_compartments()
            for compartment in compartments:
                compartments_result[compartment.id] = compartment
        return compartments_result

    def _get_instances_by_region(self, regions):
        """
        :param regions: a list of regions in which to describe instances
        :return A list of instance dictionaries
        """
        self.setup_clients(regions)

        self.debug("Building inventory.")

        self.compartments = self.get_all_compartments()

        if not self.compartments:
            self.debug("No compartments matching the criteria.")
            return

        instance_inventories = []
        self.debug(
            "Fetch compute hosts:{0}".format(self.get_option("fetch_compute_hosts"))
        )
        self.debug("Fetch db hosts:{0}".format(self.get_option("fetch_db_hosts")))

        if self._fetch_compute_hosts():
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
                self.debug(
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
                self.debug(
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

    def get_compartment_from_compartment_name(
        self,
        compartment_name,
        parent_compartment_ocid=None,
        fetch_hosts_from_subcompartments=True,
        exclude_compartments=None,
    ):
        """
        Gets the compartments based on the compartment_name.

        the compartment with that name and its hierarchy of compartments are returned
        if fetch_hosts_from_subcompartments is true.

        The tenancy is returned when compartment_name is the tenancy name.
        """
        if not self.params["tenancy"]:
            raise Exception(
                "Tenancy OCID required to get the compartments in the tenancy."
            )
        if not compartment_name:
            raise Exception("compartment_name is required")

        tenancy_compartments = self.get_compartment_including_sub_compartments(
            compartment_id=self.params["tenancy"],
            exclude_compartments=exclude_compartments,
            fetch_child_compartments=False,
        )

        tenancy_name = (
            tenancy_compartments[0].name if len(tenancy_compartments) > 0 else None
        )
        if compartment_name == tenancy_name:
            # return all the compartments when fetch_hosts_from_subcompartments is true
            if fetch_hosts_from_subcompartments:
                return self.get_compartment_including_sub_compartments(
                    compartment_id=self.params["tenancy"],
                    exclude_compartments=exclude_compartments,
                    fetch_child_compartments=True,
                )
            else:
                return tenancy_compartments

        if not parent_compartment_ocid:
            parent_compartment_ocid = (
                tenancy_compartments[0].id if len(tenancy_compartments) > 0 else None
            )

        all_compartments = self.get_compartment_including_sub_compartments(
            compartment_id=self.params["tenancy"],
            exclude_compartments=exclude_compartments,
            fetch_child_compartments=True,
        )
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
        return self.get_compartment_including_sub_compartments(
            compartment_id=compartment_with_name.id,
            exclude_compartments=self.exclude_compartments,
            fetch_child_compartments=True,
        )

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

        When both compartment_ocid and compartment_name are not passed, all the compartments are returned.

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
            return self.get_compartment_including_sub_compartments(
                compartment_id=compartment_ocid,
                exclude_compartments=self.exclude_compartments,
                fetch_child_compartments=fetch_hosts_from_subcompartments,
            )
        if compartment_name:
            return self.get_compartment_from_compartment_name(
                compartment_name=compartment_name,
                parent_compartment_ocid=parent_compartment_ocid,
                fetch_hosts_from_subcompartments=fetch_hosts_from_subcompartments,
                exclude_compartments=self.exclude_compartments,
            )
        # return all the compartments if compartment_name is not passed
        if not self.params["tenancy"]:
            raise Exception(
                "Tenancy OCID required to get the compartments in the tenancy."
            )

        all_compartments = self.get_compartment_including_sub_compartments(
            compartment_id=self.params["tenancy"],
            exclude_compartments=self.exclude_compartments,
            fetch_child_compartments=True,
        )
        return all_compartments

    @staticmethod
    def filter_resource(resource, **kwargs):
        for key, val in six.iteritems(kwargs):
            if getattr(resource, key, None) != val:
                return False
        return True

    def get_compartment_including_sub_compartments(
        self, compartment_id, exclude_compartments=None, fetch_child_compartments=True
    ):
        # OCI SDK does not support fetching sub-compartments for non root compartments
        # So traverse the compartment tree to fetch all the sub compartments
        compartments = []
        queue = deque()
        try:
            exclude_compartments = (
                exclude_compartments if exclude_compartments else dict()
            )
            # we should get the sub compartments when the compartment_id is not in exclude_compartments or
            # when the compartment_id is in exclude_compartments and skip_subcompartments is False
            if (compartment_id not in exclude_compartments) or (
                compartment_id in exclude_compartments
                and not exclude_compartments[compartment_id].get("skip_subcompartments")
            ):
                root_compartment = oci_common_utils.call_with_backoff(
                    self.identity_client.get_compartment, compartment_id=compartment_id,
                ).data
                queue.append(root_compartment)
            while len(queue) > 0:
                parent_compartment = queue.popleft()

                if parent_compartment.id not in exclude_compartments:
                    compartments.append(parent_compartment)

                if (
                    parent_compartment.id not in exclude_compartments
                    or (
                        parent_compartment.id in exclude_compartments
                        and not exclude_compartments[parent_compartment.id].get(
                            "skip_subcompartments"
                        )
                    )
                ) and fetch_child_compartments:
                    child_compartments = [
                        compartment
                        for compartment in oci_common_utils.list_all_resources(
                            target_fn=self.identity_client.list_compartments,
                            compartment_id=parent_compartment.id,
                            access_level="ACCESSIBLE",
                        )
                        if self.filter_resource(
                            compartment, lifecycle_state=self.LIFECYCLE_ACTIVE_STATE
                        )
                    ]
                    for child_compartment in child_compartments:
                        queue.append(child_compartment)
        except ServiceError as se:
            if se.status == 404:
                raise Exception(
                    "Compartment either does not exist or you don't have permission to access it. complete error : {0}".format(
                        str(se)
                    )
                )
            raise
        return compartments

    def get_common_groups(self, instance, region):
        """
        returns the enabled groups that are common between compute_instance and db_host.
        A group is enable when it is configured in the default_groups
        """
        common_groups = set(["all_hosts"])

        if "availability_domain" in self.params.get("default_groups"):
            # Group by availability domain
            ad = self.sanitize(instance.availability_domain)
            common_groups.add(ad)

        if "compartment_name" in self.params.get("default_groups"):
            # Group by compartments
            compartment = self.compartments[instance.compartment_id]
            compartment_name = self.sanitize(compartment.name)
            common_groups.add(compartment_name)

        if "region" in self.params.get("default_groups"):
            # Group by region
            region_grp = self.sanitize("region_" + region)
            common_groups.add(region_grp)

        if "freeform_tags" in self.params.get("default_groups"):
            # Group by freeform tags tag_key=value
            if hasattr(instance, "freeform_tags") and instance.freeform_tags:
                for key in instance.freeform_tags:
                    tag_group_name = self.sanitize(
                        "tag_" + key + "=" + instance.freeform_tags[key]
                    )
                    common_groups.add(tag_group_name)

        if "defined_tags" in self.params.get("default_groups"):
            # Group by defined tags
            if hasattr(instance, "defined_tags") and instance.defined_tags:
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
        return common_groups

    def build_inventory_for_instance(self, instance, region):
        """Build and return inventory for an instance"""
        try:
            instance_inventory = {}
            compute_client = self.get_compute_client_for_region(region)
            virtual_nw_client = self.get_virtual_nw_client_for_region(region)
            compartment = self.compartments[instance.compartment_id]

            instance_common_vars = to_dict(instance)
            compartment_name = self.sanitize(compartment.name)
            instance_common_vars.update({"compartment_name": compartment_name})

            common_groups = self.get_common_groups(instance=instance, region=region)

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
                instance_vars = instance_common_vars.copy()
                vnic = oci_common_utils.call_with_backoff(
                    virtual_nw_client.get_vnic, vnic_id=vnic_attachment.vnic_id
                ).data
                self.debug(
                    "VNIC {0} is attached to instance {1}.".format(
                        vnic.id, vnic_attachment.instance_id
                    )
                )

                # create inventory for instance for all vnics if primary_vnic_only option set to false
                # else create inventory only if the vnic is primary vnic for the instance
                if not self._get_primary_vnic_only() or vnic.is_primary:

                    subnet = vlan = None
                    if getattr(vnic, "subnet_id", None):
                        subnet = oci_common_utils.call_with_backoff(
                            virtual_nw_client.get_subnet, subnet_id=vnic.subnet_id
                        ).data
                    elif getattr(vnic, "vlan_id", None):
                        vlan = oci_common_utils.call_with_backoff(
                            virtual_nw_client.get_vlan, vlan_id=vnic.vlan_id
                        ).data
                    else:
                        self.debug(
                            "VNIC {} attached to instance {} doesn't have subnet_id or vlan_id associated. Skipping it".format(
                                vnic_attachment.vnic_id, vnic_attachment.instance_id
                            )
                        )
                        continue

                    if instance_vars.get("id") == vnic_attachment.instance_id:
                        instance_vars.update({"vnic_id": vnic.id})
                        if getattr(vnic, "subnet_id", None):
                            instance_vars.update({"subnet_id": vnic.subnet_id})
                            instance_vars.update({"vcn_id": subnet.vcn_id})
                        elif getattr(vnic, "vlan_id", None):
                            instance_vars.update({"vlan_id": vnic.vlan_id})
                            instance_vars.update({"vcn_id": vlan.vcn_id})
                        instance_vars.update({"public_ip": vnic.public_ip})
                        instance_vars.update({"private_ip": vnic.private_ip})

                    host_name = self.get_hostname(instance_vars, vnic, region)
                    self.debug(
                        "hostname : {0} built for instance {1}".format(
                            host_name, instance_vars.get("id")
                        )
                    )
                    if not host_name:
                        if self.get_option("strict"):
                            raise AnsibleError(
                                "Instance with OCID: {0} does not have a valid hostname.".format(
                                    instance.id
                                )
                            )
                        self.debug(
                            "hostname is {0}. Skipped instance with OCID: {1} ".format(
                                host_name, instance.id
                            )
                        )
                        continue
                    host_name = self.sanitize(host_name)

                    groups = set(common_groups)

                    self.debug("Creating inventory for host {0}.".format(host_name))
                    self.create_instance_inventory_for_host(
                        instance_inventory, host_name, vars=instance_vars, groups=groups
                    )
            self.debug(
                "Final inventory for {0}.".format(
                    str(self.get_resource_for_logging(instance_inventory))
                )
            )
            return instance_inventory

        except ServiceError as ex:
            if ex.status == 401:
                self.debug(str(ex))
                raise
            self.debug(str(ex))

    def build_inventory_for_db_host(self, db_host, region):
        """Build and return inventory for a database host"""
        try:
            db_host_inventory = {}
            virtual_nw_client = self.get_virtual_nw_client_for_region(region)
            compartment = self.compartments[db_host.compartment_id]

            db_host_vars = to_dict(db_host)

            compartment_name = self.sanitize(compartment.name)
            db_host_vars.update({"compartment_name": compartment_name})

            common_groups = self.get_common_groups(instance=db_host, region=region)

            common_groups.add("db_hosts")

            if not db_host.vnic_id:
                return None

            vnic = oci_common_utils.call_with_backoff(
                virtual_nw_client.get_vnic, vnic_id=db_host.vnic_id
            ).data

            self.debug(
                "VNIC {0} is attached to db_host {1}.".format(vnic.id, db_host.id)
            )

            subnet = oci_common_utils.call_with_backoff(
                virtual_nw_client.get_subnet, subnet_id=vnic.subnet_id
            ).data

            db_host_vars.update({"vcn_id": subnet.vcn_id})
            db_host_vars.update({"vnic_id": vnic.id})
            db_host_vars.update({"subnet_id": vnic.subnet_id})
            db_host_vars.update({"public_ip": vnic.public_ip})
            db_host_vars.update({"private_ip": vnic.private_ip})
            host_name = self.get_hostname(db_host_vars, vnic, region)
            if not host_name:
                if self.get_option("strict"):
                    raise AnsibleError(
                        "DB Instance with OCID: {0} does not have a valid hostname.".format(
                            db_host_vars.get("id")
                        )
                    )
                self.debug(
                    "hostname is {0}. Skipped DB instance with OCID: {1}".format(
                        host_name, db_host_vars.get(id)
                    )
                )
                return None

            host_name = self.sanitize(host_name)

            groups = set(common_groups)

            self.debug("Creating inventory for host {0}.".format(host_name))
            self.create_instance_inventory_for_host(
                db_host_inventory, host_name, vars=db_host_vars, groups=groups
            )
            self.debug("Final inventory for {0}.".format(str(db_host_inventory)))
            return db_host_inventory

        except ServiceError as ex:
            if ex.status == 401:
                self.debug(str(ex))
                raise
            self.debug(str(ex))

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

    def _filter_hosts(self, filter_template_list, hostvars):
        self.templar.available_variables = hostvars
        for condition_template in filter_template_list:
            try:
                jinja_condition = "%s%s%s" % ("{{", condition_template, "}}")
                if self.templar.template(jinja_condition):
                    return True
            except Exception as ex:
                self.debug(
                    "parsing template {0} failed with exception {1}".format(
                        condition_template, str(ex)
                    )
                )
                if self.get_option("strict"):
                    raise AnsibleParserError(
                        "failed parsing filter_template {0} for instance {1} with exception {2}".format(
                            condition_template, hostvars.get("id"), str(ex)
                        )
                    )
                continue
        return False

    def get_filtered_resources(self, resources, compartment_ocid):

        self.debug(
            "Resources before filtering from compartment {0}:{1}".format(
                compartment_ocid, self.get_resources_for_logging(resources)
            )
        )
        filters = ["display_name", "availability_domain", "lifecycle_state"]

        resources_filtered = []
        for resource in resources:
            resource_dict = to_dict(resource)
            if self.get_option("exclude_host_filters") and self._filter_hosts(
                self.get_option("exclude_host_filters"), resource_dict
            ):
                continue
            if self.get_option("include_host_filters"):
                if self._filter_hosts(
                    self.get_option("include_host_filters"), resource_dict
                ):
                    resources_filtered.append(resource)
                continue
            if all(
                True
                if not self.filters.get(filter)
                or getattr(resource, filter, None) == self.filters[filter]
                else False
                for filter in filters
            ):
                resources_filtered.append(resource)

        resources = resources_filtered
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
            self.debug(
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
                        and resource.defined_tags.get(namespace, {}).get(key) == value
                    )
                    for namespace in self.filters["defined_tags"]
                    for key, value in six.iteritems(
                        self.filters["defined_tags"][namespace]
                    )
                )
            ]
            self.debug(
                "Resources in compartment {0} which match all the freeform & defined tags: {1}".format(
                    compartment_ocid, self.get_resources_for_logging(resources)
                )
            )
        self.debug(
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
                        db_system_display_name=db_system.display_name,
                        region=region,
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
                self.debug(str(ex))
                raise
            self.debug(str(ex))
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
                self.debug(str(ex))
                raise
            self.debug(str(ex))
            return []

    def get_compute_client_for_region(self, region):
        if region not in self._compute_clients:
            raise ValueError(
                "Could not fetch the compute client for region {0}.".format(region)
            )
        return self._compute_clients[region]

    def get_virtual_nw_client_for_region(self, region):
        if region not in self._virtual_nw_clients:
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

    def get_hostname(self, host_vars, vnic, region):
        if self.get_option("hostname_format_preferences"):
            return self._get_hostname_from_preference(host_vars)
        return self.get_host_from_hostname_format(host_vars, vnic, region)

    def get_host_from_hostname_format(self, host_vars, vnic, region):
        # This method should return public_ip by default
        hostname_format = self.params.get("hostname_format", "public_ip")
        if hostname_format == "fqdn":
            virtual_nw_client = self.get_virtual_nw_client_for_region(region)
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
            self.debug("FQDN for VNIC: {0} is {1}.".format(vnic.id, fqdn))
            return fqdn

        elif hostname_format == "private_ip":
            self.debug(
                "Private IP for VNIC: {0} is {1}.".format(vnic.id, vnic.private_ip)
            )
            return vnic.private_ip
        elif hostname_format == "display_name":
            if self._fetch_db_hosts():
                if self.get_option("strict"):
                    raise AnsibleError(
                        "The hostname_format %s is not supported for db_hosts"
                        % (self.params["hostname_format"])
                    )
                return None
            self.debug(
                "Display_name of instance : {0} is {1}.".format(
                    host_vars.get("id"), host_vars.get("display_name")
                )
            )
            return host_vars.get("display_name")
        self.debug(
            "public_ip of the instance : {0} is {1}".format(
                host_vars.get("id"), vnic.public_ip
            )
        )
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
                            for host_variable in host_inventory["vars"]:
                                self.inventory.set_variable(
                                    host_name,
                                    host_variable,
                                    host_inventory["vars"][host_variable],
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

    def _process_query_options(self, config_data):
        """
            :param config_data: contents of the inventory config file
            :return A list of regions to query
                    a list of filters
                    a list of possible hostnames
        """
        options = {
            "regions": {"type_to_be": list, "value": config_data.get("regions", [])},
            "compartments": {
                "type_to_be": list,
                "value": config_data.get("compartments", []),
            },
            "exclude_compartments": {
                "type_to_be": list,
                "value": config_data.get("exclude_compartments", []),
            },
            "filters": {"type_to_be": list, "value": config_data.get("filters", [])},
            "hostnames": {
                "type_to_be": list,
                "value": config_data.get("hostnames", []),
            },
            "default_groups": {
                "type_to_be": list,
                "value": config_data.get("default_groups", [])
            }
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
            self.debug(" compartments item: {0}".format(item))
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

        self.exclude_compartments_info = dict()
        it = 0
        for item in options["exclude_compartments"]["value"]:
            self.debug("exclude_compartments item: {0}".format(item))
            self.exclude_compartments_info[it] = dict()
            if "compartment_ocid" in item:
                self.exclude_compartments_info[it]["compartment_ocid"] = item[
                    "compartment_ocid"
                ]
            if "parent_compartment_ocid" in item:
                self.exclude_compartments_info[it]["parent_compartment_ocid"] = item[
                    "parent_compartment_ocid"
                ]
            if "compartment_name" in item:
                self.exclude_compartments_info[it]["compartment_name"] = item[
                    "compartment_name"
                ]
            if "skip_subcompartments" in item:
                self.exclude_compartments_info[it]["skip_subcompartments"] = item[
                    "skip_subcompartments"
                ]
            else:
                self.exclude_compartments_info[it]["skip_subcompartments"] = True
            it += 1

        regions = options["regions"]["value"]
        if "all" in regions:
            if len(regions) > 1:
                raise AnsibleError(
                    "Found conflicting values for regions. Cannot specify other regions when using 'all'"
                )
            self.debug(
                "Inventory requested for all regions. Fetching all subsribed regions."
            )
            regions = [
                region_subscription.region_name
                for region_subscription in self.region_subscriptions
            ]
            self.debug("Subscribed regions: {0}.".format(regions))
        hostnames = options["hostnames"]["value"]

        # setting the default_groups to lower case values to avoid case insensitive comparison
        if self.get_option("default_groups") is None:
            self.params.update({"default_groups": self.supported_default_groups})
        else:
            default_groups = config_data.get("default_groups", [])
            for group in default_groups:
                self.params.get("default_groups").append(group.lower())

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
        if not HAS_OCI_PY_SDK:
            raise AnsibleError(
                "The oci dynamic inventory plugin requires oci python sdk."
            )
        super(InventoryModule, self).parse(inventory, loader, path)

        config_data = self._read_config_data(path)

        # debug flag
        if self.get_option("debug") is not None:
            self.params["debug"] = self.get_option("debug")
        self.debug("The debug flag is set to {0}".format(self.params["debug"]))

        # read oci config
        self.read_config()

        # read the key_file and passphrase
        self._get_key_file()
        self._get_pass_phrase()

        regions, filters, hostnames = self._process_query_options(config_data)

        self._validate_config()
        if self.get_option("hostname_format_preferences"):
            self.debug(
                "Using hostname_format_preferences: {0} and can be changed via the option 'hostname_format_preferences'".format(
                    self.get_option("hostname_format_preferences")
                )
            )
        else:
            self.params["hostname_format"] = self._get_hostname_format()
            self.debug(
                "Using hostname format: {0} and can be changed via the option 'hostname_format'".format(
                    self.params["hostname_format"]
                )
            )
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
                self.debug("Using cached results")
                self._populate(cached_results, hostnames)

        results = None
        if not cache or cache_needs_update:
            results = self._query(regions)
            self._populate(results, hostnames)

        # update the cached inventory
        if cache_needs_update or (not cache and self.get_option("cache")):
            self._cache[cache_key] = results
