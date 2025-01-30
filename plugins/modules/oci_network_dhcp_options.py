#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_network_dhcp_options
short_description: Manage a DhcpOptions resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DhcpOptions resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new set of DHCP options for the specified VCN. For more information, see
      L(DhcpOptions,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/DhcpOptions/).
    - For the purposes of access control, you must provide the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the
      compartment where you want the set of
      DHCP options to reside. Notice that the set of options doesn't have to be in the same compartment as the VCN,
      subnets, or other Networking Service components. If you're not sure which compartment to use, put the set
      of DHCP options in the same compartment as the VCN. For more information about compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm). For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the set of DHCP options, otherwise a default is provided.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - "This resource has the following action operations in the M(oracle.oci.oci_network_dhcp_options_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to contain the set of DHCP options.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the set of DHCP options belongs to.
            - Required for create using I(state=present).
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    options:
        description:
            - A set of DHCP options.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            custom_dns_servers:
                description:
                    - If you set `serverType` to `CustomDnsServer`, specify the
                      IP address of at least one DNS server of your choice (three maximum).
                    - Applicable when type is 'DomainNameServer'
                type: list
                elements: str
            server_type:
                description:
                    - "* **VcnLocal:** Reserved for future use."
                    - "* **VcnLocalPlusInternet:** Also referred to as \\"Internet and VCN Resolver\\".
                      Instances can resolve internet hostnames (no internet gateway is required),
                      and can resolve hostnames of instances in the VCN. This is the default
                      value in the default set of DHCP options in the VCN. For the Internet and
                      VCN Resolver to work across the VCN, there must also be a DNS label set for
                      the VCN, a DNS label set for each subnet, and a hostname for each instance.
                      The Internet and VCN Resolver also enables reverse DNS lookup, which lets
                      you determine the hostname corresponding to the private IP address. For more
                      information, see
                      L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm)."
                    - "* **CustomDnsServer:** Instances use a DNS server of your choice (three
                      maximum)."
                    - Required when type is 'DomainNameServer'
                type: str
                choices:
                    - "VcnLocal"
                    - "VcnLocalPlusInternet"
                    - "CustomDnsServer"
            type:
                description:
                    - The specific DHCP option. Either `DomainNameServer`
                      (for L(DhcpDnsOption,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/DhcpDnsOption/)) or
                      `SearchDomain` (for L(DhcpSearchDomainOption,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/DhcpSearchDomainOption/)).
                type: str
                choices:
                    - "DomainNameServer"
                    - "SearchDomain"
                required: true
            search_domain_names:
                description:
                    - A single search domain name according to L(RFC 952,https://tools.ietf.org/html/rfc952)
                      and L(RFC 1123,https://tools.ietf.org/html/rfc1123). During a DNS query,
                      the OS will append this search domain name to the value being queried.
                    - If you set L(DhcpDnsOption,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/DhcpDnsOption/) to `VcnLocalPlusInternet`,
                      and you assign a DNS label to the VCN during creation, the search domain name in the
                      VCN's default set of DHCP options is automatically set to the VCN domain
                      (for example, `vcn1.oraclevcn.com`).
                    - If you don't want to use a search domain name, omit this option from the
                      set of DHCP options. Do not include this option with an empty list
                      of search domain names, or with an empty string as the value for any search
                      domain name.
                    - Required when type is 'SearchDomain'
                type: list
                elements: str
    domain_name_type:
        description:
            - The search domain name type of DHCP options
            - This parameter is updatable.
        type: str
        choices:
            - "SUBNET_DOMAIN"
            - "VCN_DOMAIN"
            - "CUSTOM_DOMAIN"
    dhcp_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the set of DHCP options.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DhcpOptions.
            - Use I(state=present) to create or update a DhcpOptions.
            - Use I(state=absent) to delete a DhcpOptions.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create dhcp_options
  oci_network_dhcp_options:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    vcn_id: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    options:
    - # required
      server_type: VcnLocal
      type: DomainNameServer

      # optional
      custom_dns_servers: [ "custom_dns_servers_example" ]

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    domain_name_type: SUBNET_DOMAIN

- name: Update dhcp_options
  oci_network_dhcp_options:
    # required
    dhcp_id: "ocid1.dhcp.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    options:
    - # required
      server_type: VcnLocal
      type: DomainNameServer

      # optional
      custom_dns_servers: [ "custom_dns_servers_example" ]
    domain_name_type: SUBNET_DOMAIN

- name: Update dhcp_options using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_dhcp_options:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}
    options:
    - # required
      server_type: VcnLocal
      type: DomainNameServer

      # optional
      custom_dns_servers: [ "custom_dns_servers_example" ]
    domain_name_type: SUBNET_DOMAIN

- name: Delete dhcp_options
  oci_network_dhcp_options:
    # required
    dhcp_id: "ocid1.dhcp.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete dhcp_options using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_dhcp_options:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
dhcp_options:
    description:
        - Details of the DhcpOptions resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the set of DHCP options.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)) for the set of DHCP options.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the set of DHCP options.
            returned: on success
            type: str
            sample: PROVISIONING
        options:
            description:
                - The collection of individual DHCP options.
            returned: on success
            type: complex
            contains:
                custom_dns_servers:
                    description:
                        - If you set `serverType` to `CustomDnsServer`, specify the
                          IP address of at least one DNS server of your choice (three maximum).
                    returned: on success
                    type: list
                    sample: []
                server_type:
                    description:
                        - "* **VcnLocal:** Reserved for future use."
                        - "* **VcnLocalPlusInternet:** Also referred to as \\"Internet and VCN Resolver\\".
                          Instances can resolve internet hostnames (no internet gateway is required),
                          and can resolve hostnames of instances in the VCN. This is the default
                          value in the default set of DHCP options in the VCN. For the Internet and
                          VCN Resolver to work across the VCN, there must also be a DNS label set for
                          the VCN, a DNS label set for each subnet, and a hostname for each instance.
                          The Internet and VCN Resolver also enables reverse DNS lookup, which lets
                          you determine the hostname corresponding to the private IP address. For more
                          information, see
                          L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm)."
                        - "* **CustomDnsServer:** Instances use a DNS server of your choice (three
                          maximum)."
                    returned: on success
                    type: str
                    sample: VcnLocal
                type:
                    description:
                        - The specific DHCP option. Either `DomainNameServer`
                          (for L(DhcpDnsOption,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/DhcpDnsOption/)) or
                          `SearchDomain` (for L(DhcpSearchDomainOption,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/DhcpSearchDomainOption/)).
                    returned: on success
                    type: str
                    sample: DomainNameServer
                search_domain_names:
                    description:
                        - A single search domain name according to L(RFC 952,https://tools.ietf.org/html/rfc952)
                          and L(RFC 1123,https://tools.ietf.org/html/rfc1123). During a DNS query,
                          the OS will append this search domain name to the value being queried.
                        - If you set L(DhcpDnsOption,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/DhcpDnsOption/) to `VcnLocalPlusInternet`,
                          and you assign a DNS label to the VCN during creation, the search domain name in the
                          VCN's default set of DHCP options is automatically set to the VCN domain
                          (for example, `vcn1.oraclevcn.com`).
                        - If you don't want to use a search domain name, omit this option from the
                          set of DHCP options. Do not include this option with an empty list
                          of search domain names, or with an empty string as the value for any search
                          domain name.
                    returned: on success
                    type: list
                    sample: []
        time_created:
            description:
                - Date and time the set of DHCP options was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the set of DHCP options belongs to.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        domain_name_type:
            description:
                - The search domain name type of DHCP options
            returned: on success
            type: str
            sample: SUBNET_DOMAIN
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "options": [{
            "custom_dns_servers": [],
            "server_type": "VcnLocal",
            "type": "DomainNameServer",
            "search_domain_names": []
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "domain_name_type": "SUBNET_DOMAIN"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateDhcpDetails
    from oci.core.models import UpdateDhcpDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DhcpOptionsHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DhcpOptionsHelperGen, self).get_possible_entity_types() + [
            "dhcpoptions",
            "dhcpoption",
            "coredhcpoptions",
            "coredhcpoption",
            "dhcpoptionsresource",
            "dhcpoptionresource",
            "dhcp",
            "dhcps",
            "coredhcp",
            "coredhcps",
            "dhcpresource",
            "dhcpsresource",
            "core",
        ]

    def get_module_resource_id_param(self):
        return "dhcp_id"

    def get_module_resource_id(self):
        return self.module.params.get("dhcp_id")

    def get_get_fn(self):
        return self.client.get_dhcp_options

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dhcp_options, dhcp_id=self.module.params.get("dhcp_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["vcn_id", "display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_dhcp_options, **kwargs
        )

    def get_create_model_class(self):
        return CreateDhcpDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dhcp_options,
            call_fn_args=(),
            call_fn_kwargs=dict(create_dhcp_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDhcpDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dhcp_options,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dhcp_id=self.module.params.get("dhcp_id"),
                update_dhcp_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dhcp_options,
            call_fn_args=(),
            call_fn_kwargs=dict(dhcp_id=self.module.params.get("dhcp_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DhcpOptionsHelperCustom = get_custom_class("DhcpOptionsHelperCustom")


class ResourceHelper(DhcpOptionsHelperCustom, DhcpOptionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            options=dict(
                type="list",
                elements="dict",
                options=dict(
                    custom_dns_servers=dict(type="list", elements="str"),
                    server_type=dict(
                        type="str",
                        choices=["VcnLocal", "VcnLocalPlusInternet", "CustomDnsServer"],
                    ),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["DomainNameServer", "SearchDomain"],
                    ),
                    search_domain_names=dict(type="list", elements="str"),
                ),
            ),
            domain_name_type=dict(
                type="str", choices=["SUBNET_DOMAIN", "VCN_DOMAIN", "CUSTOM_DOMAIN"]
            ),
            dhcp_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dhcp_options",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
