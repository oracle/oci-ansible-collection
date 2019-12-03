#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_nat_gateway_facts
short_description: Retrieve facts of NAT gateways
description:
    - This module retrieves information of the specified NAT gateway or lists all the NAT gateways in the specified
      compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to get all the NAT gateways in the
                     compartment.
        required: false
    vcn_id:
        description: The OCID of the VCN. Use I(vcn_id) with I(compartment_id) to filter the results by VCN.
        required: false
    nat_gateway_id:
        description: The OCID of the NAT gateway. I(nat_gateway_id) is required to get a specific NAT
                     gateway's information.
        required: false
        aliases: [ 'id' ]
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive. Allowed values are "PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"
        required: false
        choices: ["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the NAT gateways in a compartment
  oci_nat_gateway_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get a specific NAT gateway using its OCID
  oci_nat_gateway_facts:
    nat_gateway_id: ocid1.natgateway.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
nat_gateways:
    description: List of NAT gateway details
    returned: always
    type: complex
    contains:
        block_traffic:
            description: Whether the NAT gateway blocks all traffic through it. The default is false.
            returned: always
            type: bool
            sample: true
        compartment_id:
            description: The OCID of the compartment containing the NAT gateway.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: Name of the NAT gateway.
            returned: always
            type: string
            sample: ansible_nat_gateway
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: OCID of the NAT gateway.
            returned: always
            type: string
            sample: ocid1.natgateway.oc1.phx.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: Current state of the NAT gateway.
            returned: always
            type: string
            sample: AVAILABLE
        nat_ip:
            description: The IP address associated with the NAT gateway.
            returned: always
            type: string
            sample: "129.213.64.168"
        time_created:
            description: The date and time the NAT gateway was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
        vcn_id:
            description: The OCID of the VCN the NAT gateway belongs to.
            returned: always
            type: string
            sample: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
    sample: [{
            "block_traffic": false,
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_nat_gateway",
            "freeform_tags": {},
            "id": "ocid1.natgateway.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "nat_ip": "129.213.64.168",
            "time_created": "2017-11-13T20:22:40.626000+00:00",
            "vcn_id": ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
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
            nat_gateway_id=dict(type="str", required=False, aliases=["id"]),
            vcn_id=dict(type="str", required=False),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=["PROVISIONING", "AVAILABLE", "TERMINATING", "TERMINATED"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "nat_gateway_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    nat_gateway_id = module.params["nat_gateway_id"]
    compartment_id = module.params["compartment_id"]
    result = []

    try:
        if nat_gateway_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_nat_gateway,
                        nat_gateway_id=nat_gateway_id,
                    ).data
                )
            ]
        else:
            optional_list_method_params = ["display_name", "lifecycle_state", "vcn_id"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_nat_gateways,
                    compartment_id=compartment_id,
                    **optional_kwargs
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(nat_gateways=result)


if __name__ == "__main__":
    main()
