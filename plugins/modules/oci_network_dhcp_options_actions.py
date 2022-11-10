#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_network_dhcp_options_actions
short_description: Perform actions on a DhcpOptions resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DhcpOptions resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a set of DHCP options into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dhcp_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the set of DHCP options.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              set of DHCP options to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DhcpOptions.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on dhcp_options
  oci_network_dhcp_options_actions:
    # required
    dhcp_id: "ocid1.dhcp.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import ChangeDhcpOptionsCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DhcpOptionsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dhcp_id"

    def get_module_resource_id(self):
        return self.module.params.get("dhcp_id")

    def get_get_fn(self):
        return self.client.get_dhcp_options

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dhcp_options, dhcp_id=self.module.params.get("dhcp_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDhcpOptionsCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_dhcp_options_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dhcp_id=self.module.params.get("dhcp_id"),
                change_dhcp_options_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


DhcpOptionsActionsHelperCustom = get_custom_class("DhcpOptionsActionsHelperCustom")


class ResourceHelper(DhcpOptionsActionsHelperCustom, DhcpOptionsActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            dhcp_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
