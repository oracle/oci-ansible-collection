#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_subnet_facts
short_description: Retrieve facts of subnets
description:
    - This module allows the user to retrieve information of the specified subnet or all the subnets in the specified
      VCN and the specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to retrieve all the subnets in the
                     specified VCN and the specified compartment.
        required: false
    subnet_id:
        description: The OCID of the subnet. I(subnet_id) is required to get a particular subnet's information.
                     Whenever a I(subnet_id) is specified with any other options, information of only the subnet
                     pointed by I(subnet_id) is retrieved.
        required: false
    vcn_id:
        description: The OCID of the VCN. I(vcn_id) is required to retrieve all the subnets in the specified VCN and
                     the specified compartment.
        required: false
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive. Allowed values are "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"
        required: false
        choices: ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the subnets in the specified VCN and the specified compartment
  oci_subnet_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx

- name: Get a specific subnet
  oci_subnet_facts:
    subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
subnets:
    description: List of subnet details
    returned: always
    type: complex
    contains:
        availability_domain:
            description: The subnet's Availability Domain.
            returned: always
            type: string
            sample: BnQb:PHX-AD-1
        cidr_block:
            description: The subnet's CIDR block.
            returned: always
            type: string
            sample: 10.0.1.0/24
        compartment_id:
            description: The OCID of the compartment containing the subnet.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        dhcp_options_id:
            description: The OCID of the set of DHCP options associated with the subnet.
            returned: always
            type: string
            sample: ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx
        display_name:
            description: Name of the subnet.
            returned: always
            type: string
            sample: ansible_subnet
        dns_label:
            description: A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS
                         label to form a fully qualified domain name (FQDN) for each VNIC within this subnet.
            returned: always
            type: string
            sample: ansiblesubnet
        id:
            description: OCID of the subnet.
            returned: always
            type: string
            sample: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The subnet's current state.
            returned: always
            type: string
            sample: AVAILABLE
        prohibit_public_ip_on_vnic:
            description: Whether VNICs within this subnet can have public IP addresses. Defaults to false, which means
                         VNICs created in this subnet will automatically be assigned public IP addresses unless
                         specified otherwise during instance launch or VNIC creation (with the assignPublicIp flag in
                         CreateVnicDetails). If prohibitPublicIpOnVnic is set to true, VNICs created in this subnet
                         cannot have public IP addresses (that is, it's a private subnet).
            returned: always
            type: boolean
            sample: true
        route_table_id:
            description: The OCID of the route table the subnet is using.
            returned: always
            type: string
            sample: ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx
        security_list_ids:
            description: OCIDs for the security lists to use for VNICs in this subnet.
            returned: always
            type: list of strings
            sample: [
                    "ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx"
                ]
        subnet_domain_name:
            description: The subnet's domain name, which consists of the subnet's DNS label, the VCN's DNS label, and
                         the oraclevcn.com domain.
            returned: always
            type: string
            sample: ansiblesubnet.ansiblevcn.oraclevcn.com
        time_created:
            description: The date and time the subnet was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
        vcn_id:
            description: The OCID of the VCN the subnet is in.
            returned: always
            type: string
            sample: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
        virtual_router_ip:
            description: The IP address of the virtual router.
            returned: always
            type: string
            sample: 10.0.1.1
        virtual_router_mac:
            description: The MAC address of the virtual router.
            returned: always
            type: string
            sample: 00:00:17:D1:27:79
    sample: [{
            "availability_domain": "BnQb:PHX-AD-1",
            "cidr_block": "10.0.1.0/24",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "dhcp_options_id": "ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx",
            "display_name": "ansible_subnet",
            "dns_label": ansiblesubnet,
            "id": "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "prohibit_public_ip_on_vnic": true,
            "route_table_id": "ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx",
            "security_list_ids": [
                "ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx"
            ],
            "subnet_domain_name": ansiblesubnet.ansiblevcn.oraclevcn.com,
            "time_created": "2017-11-16T07:25:47.234000+00:00",
            "vcn_id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx",
            "virtual_router_ip": "10.0.2.1",
            "virtual_router_mac": "00:00:17:D1:27:79"
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            subnet_id=dict(type="str", required=False),
            vcn_id=dict(type="str", required=False),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    subnet_id = module.params["subnet_id"]
    vcn_id = module.params["vcn_id"]
    compartment_id = module.params["compartment_id"]
    result = []

    if subnet_id is not None:
        try:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_subnet, subnet_id=subnet_id
                    ).data
                )
            ]
        except ServiceError as ex:
            module.fail_json(msg=ex.message)
    elif compartment_id is not None and vcn_id is not None:
        try:
            optional_list_method_params = ["display_name", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_subnets,
                    compartment_id=compartment_id,
                    vcn_id=vcn_id,
                    **optional_kwargs
                )
            )
        except ServiceError as ex:
            module.fail_json(msg=ex.message)
    else:
        module.fail_json(
            msg="Specify a compartment_id and a vcn_id to get all the subnets in the compartment and the \
                            VCN or a subnet_id to retrieve a specific subnet"
        )

    module.exit_json(subnets=result)


if __name__ == "__main__":
    main()
