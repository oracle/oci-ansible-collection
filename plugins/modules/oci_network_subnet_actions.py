#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_network_subnet_actions
short_description: Perform actions on a Subnet resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Subnet resource in Oracle Cloud Infrastructure
    - For I(action=add_ipv6_subnet_cidr), add an IPv6 CIDR to a subnet.
    - For I(action=change_compartment), moves a subnet into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=remove_ipv6_subnet_cidr), remove an IPv6 CIDR from a subnet. At least one IPv6 CIDR should remain.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              subnet to.
            - Required for I(action=change_compartment).
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subnet.
        type: str
        aliases: ["id"]
        required: true
    ipv6_cidr_block:
        description:
            - This field is not required and should only be specified when adding an IPv6 CIDR
              to a subnet's IPv6 address space.
              SeeL(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
            - "Example: `2001:0db8:0123::/64`"
            - Required for I(action=add_ipv6_subnet_cidr), I(action=remove_ipv6_subnet_cidr).
        type: str
    action:
        description:
            - The action to perform on the Subnet.
        type: str
        required: true
        choices:
            - "add_ipv6_subnet_cidr"
            - "change_compartment"
            - "remove_ipv6_subnet_cidr"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_ipv6_subnet_cidr on subnet
  oci_network_subnet_actions:
    # required
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    ipv6_cidr_block: ipv6_cidr_block_example
    action: add_ipv6_subnet_cidr

- name: Perform action change_compartment on subnet
  oci_network_subnet_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_ipv6_subnet_cidr on subnet
  oci_network_subnet_actions:
    # required
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    ipv6_cidr_block: ipv6_cidr_block_example
    action: remove_ipv6_subnet_cidr

"""

RETURN = """
subnet:
    description:
        - Details of the Subnet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The subnet's availability domain. This attribute will be null if this is a regional subnet
                  instead of an AD-specific subnet. Oracle recommends creating regional subnets.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        cidr_block:
            description:
                - The subnet's CIDR block.
                - "Example: `10.0.1.0/24`"
            returned: on success
            type: str
            sample: cidr_block_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the subnet.
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
        dhcp_options_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the set of DHCP options that the subnet uses.
            returned: on success
            type: str
            sample: "ocid1.dhcpoptions.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        dns_label:
            description:
                - A DNS label for the subnet, used in conjunction with the VNIC's hostname and
                  VCN's DNS label to form a fully qualified domain name (FQDN) for each VNIC
                  within this subnet (for example, `bminstance1.subnet123.vcn1.oraclevcn.com`).
                  Must be an alphanumeric string that begins with a letter and is unique within the VCN.
                  The value cannot be changed.
                - The absence of this parameter means the Internet and VCN Resolver
                  will not resolve hostnames of instances in this subnet.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                - "Example: `subnet123`"
            returned: on success
            type: str
            sample: dns_label_example
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
                - The subnet's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ipv6_cidr_block:
            description:
                - For an IPv6-enabled subnet, this is the IPv6 CIDR block for the subnet's IP address space.
                  The subnet size is always /64. See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm).
                - "Example: `2001:0db8:0123:1111::/64`"
            returned: on success
            type: str
            sample: ipv6_cidr_block_example
        ipv6_cidr_blocks:
            description:
                - The list of all IPv6 CIDR blocks (Oracle allocated IPv6 GUA, ULA or private IPv6 CIDR blocks, BYOIPv6 CIDR blocks) for the subnet.
            returned: on success
            type: list
            sample: []
        ipv6_virtual_router_ip:
            description:
                - For an IPv6-enabled subnet, this is the IPv6 address of the virtual router.
                - "Example: `2001:0db8:0123:1111:89ab:cdef:1234:5678`"
            returned: on success
            type: str
            sample: ipv6_virtual_router_ip_example
        lifecycle_state:
            description:
                - The subnet's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        prohibit_internet_ingress:
            description:
                - Whether to disallow ingress internet traffic to VNICs within this subnet. Defaults to false.
                - For IPV4, `prohibitInternetIngress` behaves similarly to `prohibitPublicIpOnVnic`.
                  If it is set to false, VNICs created in this subnet will automatically be assigned public IP
                  addresses unless specified otherwise during instance launch or VNIC creation (with the `assignPublicIp`
                  flag in L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)).
                  If `prohibitInternetIngress` is set to true, VNICs created in this subnet cannot have public IP addresses
                  (that is, it's a privatesubnet).
                - For IPv6, if `prohibitInternetIngress` is set to `true`, internet access is not allowed for any
                  IPv6s assigned to VNICs in the subnet. Otherwise, ingress internet traffic is allowed by default.
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        prohibit_public_ip_on_vnic:
            description:
                - Whether VNICs within this subnet can have public IP addresses.
                  Defaults to false, which means VNICs created in this subnet will
                  automatically be assigned public IP addresses unless specified
                  otherwise during instance launch or VNIC creation (with the
                  `assignPublicIp` flag in
                  L(CreateVnicDetails,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/CreateVnicDetails/)).
                  If `prohibitPublicIpOnVnic` is set to true, VNICs created in this
                  subnet cannot have public IP addresses (that is, it's a private
                  subnet).
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        route_table_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table that the subnet uses.
            returned: on success
            type: str
            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        security_list_ids:
            description:
                - "The OCIDs of the security list or lists that the subnet uses. Remember
                  that security lists are associated *with the subnet*, but the
                  rules are applied to the individual VNICs in the subnet."
            returned: on success
            type: list
            sample: []
        subnet_domain_name:
            description:
                - The subnet's domain name, which consists of the subnet's DNS label,
                  the VCN's DNS label, and the `oraclevcn.com` domain.
                - For more information, see
                  L(DNS in Your Virtual Cloud Network,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/dns.htm).
                - "Example: `subnet123.vcn1.oraclevcn.com`"
            returned: on success
            type: str
            sample: subnet_domain_name_example
        time_created:
            description:
                - The date and time the subnet was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the subnet is in.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
        virtual_router_ip:
            description:
                - The IP address of the virtual router.
                - "Example: `10.0.14.1`"
            returned: on success
            type: str
            sample: virtual_router_ip_example
        virtual_router_mac:
            description:
                - The MAC address of the virtual router.
                - "Example: `00:00:00:00:00:01`"
            returned: on success
            type: str
            sample: virtual_router_mac_example
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "cidr_block": "cidr_block_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "dhcp_options_id": "ocid1.dhcpoptions.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "dns_label": "dns_label_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ipv6_cidr_block": "ipv6_cidr_block_example",
        "ipv6_cidr_blocks": [],
        "ipv6_virtual_router_ip": "ipv6_virtual_router_ip_example",
        "lifecycle_state": "PROVISIONING",
        "prohibit_internet_ingress": true,
        "prohibit_public_ip_on_vnic": true,
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "security_list_ids": [],
        "subnet_domain_name": "subnet_domain_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx",
        "virtual_router_ip": "virtual_router_ip_example",
        "virtual_router_mac": "virtual_router_mac_example"
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
    from oci.work_requests import WorkRequestClient
    from oci.core import VirtualNetworkClient
    from oci.core.models import AddSubnetIpv6CidrDetails
    from oci.core.models import ChangeSubnetCompartmentDetails
    from oci.core.models import RemoveSubnetIpv6CidrDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubnetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_ipv6_subnet_cidr
        change_compartment
        remove_ipv6_subnet_cidr
    """

    def __init__(self, *args, **kwargs):
        super(SubnetActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "subnet_id"

    def get_module_resource_id(self):
        return self.module.params.get("subnet_id")

    def get_get_fn(self):
        return self.client.get_subnet

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subnet, subnet_id=self.module.params.get("subnet_id"),
        )

    def add_ipv6_subnet_cidr(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddSubnetIpv6CidrDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_ipv6_subnet_cidr,
            call_fn_args=(),
            call_fn_kwargs=dict(
                subnet_id=self.module.params.get("subnet_id"),
                add_subnet_ipv6_cidr_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSubnetCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_subnet_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                subnet_id=self.module.params.get("subnet_id"),
                change_subnet_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_ipv6_subnet_cidr(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveSubnetIpv6CidrDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_ipv6_subnet_cidr,
            call_fn_args=(),
            call_fn_kwargs=dict(
                subnet_id=self.module.params.get("subnet_id"),
                remove_subnet_ipv6_cidr_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


SubnetActionsHelperCustom = get_custom_class("SubnetActionsHelperCustom")


class ResourceHelper(SubnetActionsHelperCustom, SubnetActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            subnet_id=dict(aliases=["id"], type="str", required=True),
            ipv6_cidr_block=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_ipv6_subnet_cidr",
                    "change_compartment",
                    "remove_ipv6_subnet_cidr",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="subnet",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
