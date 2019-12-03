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
module: oci_remote_peering_connection_facts
short_description: Retrieve facts of Remote Peering Connections(RPCs)
description:
    - This module retrieves information of the specified remote peering connection(RPC) or lists the RPCs for the
      specified DRG and compartment (the RPC's compartment).
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to get all the RPCs in the specified
                     compartment (the RPC's compartment).
        required: false
    drg_id:
        description: The OCID of the DRG. I(drg_id) is required to get all the RPCs for the specified DRG and
                     compartment (the RPC's compartment).
        required: false
    remote_peering_connection_id:
        description: The OCID of the RPC. I(remote_peering_connection_id) is required to get a specific RPC's
                     information.
        required: false
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the RPCs in a compartment
  oci_remote_peering_connection_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get a specific RPC using its OCID
  oci_remote_peering_connection_facts:
    remote_peering_connection_id: ocid1.remotepeeringconnection.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
remote_peering_connections:
    description: List of RPC details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the RPC.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: Name of the RPC.
            returned: always
            type: string
            sample: ansible_remote_peering_connection
        drg_id:
            description: The OCID of the DRG that this RPC belongs to.
            returned: always
            type: string
            sample: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx
        id:
            description: OCID of the RPC.
            returned: always
            type: string
            sample: ocid1.remotepeeringconnection.oc1.phx.xxxxxEXAMPLExxxxx
        is_cross_tenancy_peering:
            description: Whether the VCN at the other end of the peering is in a different tenancy.
            returned: always
            type: bool
            sample: false
        lifecycle_state:
            description: Current state of the RPC.
            returned: always
            type: string
            sample: AVAILABLE
        peer_id:
            description: If this RPC is peered, this value is the OCID of the other RPC.
            returned: always
            type: string
            sample: ocid1.remotepeeringconnection.oc1.iad.xxxxxEXAMPLExxxxx
        peering_status:
            description: Whether the RPC is peered with another RPC. NEW means the RPC has not yet been peered. PENDING
                         means the peering is being established. REVOKED means the RPC at the other end of the peering
                         has been deleted.
            returned: always
            type: string
            sample: PEERED
        peering_region_name:
            description: If this RPC is peered, this value is the region that contains the other RPC.
            returned: always
            type: string
            sample: us-ashburn-1
        time_created:
            description: The date and time the RPC was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
        peer_tenancy_id:
            description: If this RPC is peered, this value is the OCID of the other RPC's tenancy.
            returned: always
            type: string
            sample: "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx"
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible_remote_peering_connection",
            "drg_id": "ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx",
            "id": "ocid1.remotepeeringconnection.oc1.phx.xxxxxEXAMPLExxxxx",
            "is_cross_tenancy_peering": false,
            "lifecycle_state": "AVAILABLE",
            "peer_id":  "ocid1.remotepeeringconnection.oc1.iad.xxxxxEXAMPLExxxxx",
            "peer_region_name": "us-ashburn-1",
            "peer_tenancy_id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx",
            "peering_status": "PEERED",
            "time_created": "2018-09-24T06:51:59.491000+00:00"
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
            drg_id=dict(type="str", required=False),
            remote_peering_connection_id=dict(
                type="str", required=False, aliases=["id"]
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["remote_peering_connection_id", "compartment_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    remote_peering_connection_id = module.params["remote_peering_connection_id"]
    result = []

    try:
        if remote_peering_connection_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_remote_peering_connection,
                        remote_peering_connection_id=remote_peering_connection_id,
                    ).data
                )
            ]
        else:
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_remote_peering_connections,
                    display_name=module.params["display_name"],
                    drg_id=module.params["drg_id"],
                    compartment_id=module.params["compartment_id"],
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(remote_peering_connections=result)


if __name__ == "__main__":
    main()
