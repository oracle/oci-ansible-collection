#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_local_peering_gateway_facts
short_description: Retrieve facts of Local Peering Gateways(LPGs)
description:
    - This module retrieves information of the specified local peering gateway(LPG) or lists the local peering gateways
      (LPGs) for the specified VCN and compartment (the LPG's compartment).
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to get all the LPGs in the specified VCN
                     and compartment (the LPG's compartment).
        required: false
    vcn_id:
        description: The OCID of the VCN. I(vcn_id) is required to get all the LPGs in the specified VCN and
                     compartment (the LPG's compartment).
        required: false
    local_peering_gateway_id:
        description: The OCID of the LPG. I(local_peering_gateway_id) is required to get a specific LPG's information.
        required: false
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the LPGs in a compartment
  oci_local_peering_gateway_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    vcn_id: 'ocid1.vcn.oc1..xxxxxEXAMPLExxxxx'

- name: Get a specific LPG using its OCID
  oci_local_peering_gateway_facts:
    local_peering_gateway_id: ocid1.localpeeringgateway.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
local_peering_gateways:
    description: List of LPG details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the LPG.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: Name of the LPG.
            returned: always
            type: string
            sample: ansible_local_peering_gateway
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: OCID of the LPG.
            returned: always
            type: string
            sample: ocid1.localpeeringgateway.oc1.phx.xxxxxEXAMPLExxxxx
        is_cross_tenancy_peering:
            description: Whether the VCN at the other end of the peering is in a different tenancy.
            returned: always
            type: bool
            sample: false
        lifecycle_state:
            description: Current state of the LPG.
            returned: always
            type: string
            sample: AVAILABLE
        peer_advertised_cidr:
            description: The range of IP addresses available on the VCN at the other end of the peering from this LPG.
                         The value is null if the LPG is not peered. You can use this as the destination CIDR for a
                         route rule to route a subnet's traffic to this LPG.
            returned: always
            type: string
            sample: "172.16.1.0/30"
        peering_status:
            description: Whether the LPG is peered with another LPG. NEW means the LPG has not yet been peered.
                         PENDING means the peering is being established. REVOKED means the LPG at the other end of the
                         peering has been deleted.
            returned: always
            type: string
            sample: PEERED
        peering_status_details:
            description: Additional information regarding the peering status, if applicable.
            returned: always
            type: string
            sample: "Connected to a peer."
        time_created:
            description: The date and time the LPG was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
        vcn_id:
            description: The OCID of the VCN the LPG belongs to.
            returned: always
            type: string
            sample: "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_local_peering_gateway",
            "freeform_tags": {},
            "id": "ocid1.localpeeringgateway.oc1.phx.xxxxxEXAMPLExxxxx",
            "is_cross_tenancy_peering": false,
            "lifecycle_state": "AVAILABLE",
            "peer_advertised_cidr":  "172.16.1.0/30",
            "peering_status": "PEERED",
            "peering_status_details": "Connected to a peer.",
            "time_created": "2018-09-24T06:51:59.491000+00:00",
            "vcn_id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
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
            vcn_id=dict(type="str", required=False),
            local_peering_gateway_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[["local_peering_gateway_id", None, ["vcn_id", "compartment_id"]]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    local_peering_gateway_id = module.params["local_peering_gateway_id"]
    result = []

    try:
        if local_peering_gateway_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_local_peering_gateway,
                        local_peering_gateway_id=local_peering_gateway_id,
                    ).data
                )
            ]
        else:
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_local_peering_gateways,
                    display_name=module.params["display_name"],
                    vcn_id=module.params["vcn_id"],
                    compartment_id=module.params["compartment_id"],
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(local_peering_gateways=result)


if __name__ == "__main__":
    main()
