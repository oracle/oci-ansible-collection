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
module: oci_remote_peering_connection
short_description: Manage remote peering connections in OCI
description:
    - This module allows the user to create, delete, update a remote peering connection(RPC) and connect one RPC to
      another one in a different region in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment containing the RPC. Required when creating a RPC with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information.
        required: false
        aliases: [ 'name' ]
    state:
        description: Create or update a RPC with I(state=present). Use I(state=absent) to delete a RPC.
        required: false
        default: present
        choices: ['present', 'absent']
    remote_peering_connection_id:
        description: The OCID of the remote peering connection (RPC). Required when deleting a RPC with I(state=absent)
                     or updating a RPC with I(state=present) or for connecting RPCs.
        required: false
        aliases: [ 'id' ]
    peer_id:
        description: The OCID of the RPC you want to peer with. Required to connect I(remote_peering_connection_id) to
                     another RPC in different region.
        required: false
    peer_region_name:
        description: The name of the region that contains the RPC you want to peer with. Required to connect
                     I(remote_peering_connection_id) to another RPC in different region.
        required: false
    drg_id:
        description: The OCID of the DRG the RPC belongs to. Required when creating a RPC with I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Create a RPC
  oci_remote_peering_connection:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: my_remote_peering_connection
    drg_id: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx

- name: Update the specified RPC's display name
  oci_remote_peering_connection:
    remote_peering_connection_id: ocid1.remotepeeringconnection.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_remote_peering_connection

- name: Connect a RPC to another RPC in different region
  oci_remote_peering_connection:
    remote_peering_connection_id: ocid1.remotepeeringconnection.oc1.phx.xxxxxEXAMPLExxxxx
    peer_id: ocid1.remotepeeringconnection.oc1.iad.xxxxxEXAMPLExxxxx
    peer_region_name: us-ashburn-1

- name: Delete the specified RPC
  oci_remote_peering_connection:
    id: ocid1.remotepeeringconnection.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
remote_peering_connection:
    description: Information about the RPC
    returned: On successful operation
    type: dict
    sample: {
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
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreateRemotePeeringConnectionDetails
    from oci.core.models import UpdateRemotePeeringConnectionDetails
    from oci.core.models import ConnectRemotePeeringConnectionsDetails
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_remote_peering_connection(virtual_network_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="remote_peering_connection",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_remote_peering_connection,
        kwargs_get={
            "remote_peering_connection_id": module.params[
                "remote_peering_connection_id"
            ]
        },
        delete_fn=virtual_network_client.delete_remote_peering_connection,
        kwargs_delete={
            "remote_peering_connection_id": module.params[
                "remote_peering_connection_id"
            ]
        },
        module=module,
    )
    return result


def update_remote_peering_connection(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="remote_peering_connection",
        get_fn=virtual_network_client.get_remote_peering_connection,
        client=virtual_network_client,
        kwargs_get={
            "remote_peering_connection_id": module.params[
                "remote_peering_connection_id"
            ]
        },
        update_fn=virtual_network_client.update_remote_peering_connection,
        primitive_params_update=["remote_peering_connection_id"],
        kwargs_non_primitive_update={
            UpdateRemotePeeringConnectionDetails: "update_remote_peering_connection_details"
        },
        module=module,
        update_attributes=UpdateRemotePeeringConnectionDetails().attribute_map.keys(),
    )
    return result


def create_remote_peering_connection(virtual_network_client, module):
    create_remote_peering_connection_details = CreateRemotePeeringConnectionDetails()
    for attribute in create_remote_peering_connection_details.attribute_map.keys():
        if attribute in module.params:
            setattr(
                create_remote_peering_connection_details,
                attribute,
                module.params[attribute],
            )

    result = oci_utils.create_and_wait(
        resource_type="remote_peering_connection",
        create_fn=virtual_network_client.create_remote_peering_connection,
        kwargs_create={
            "create_remote_peering_connection_details": create_remote_peering_connection_details
        },
        client=virtual_network_client,
        get_fn=virtual_network_client.get_remote_peering_connection,
        get_param="remote_peering_connection_id",
        module=module,
    )
    return result


def are_rpcs_connected(virtual_network_client, rpc, peer_id):
    # Return True if `rpc` & `peer_rpc` are connected.
    return rpc.peer_id == peer_id


def connect_rpcs_and_wait(virtual_network_client, module):
    connect_details = ConnectRemotePeeringConnectionsDetails()

    for attribute in connect_details.attribute_map.keys():
        if attribute in module.params:
            setattr(connect_details, attribute, module.params[attribute])

    rpc_id = module.params["remote_peering_connection_id"]

    virtual_network_client.connect_remote_peering_connections(rpc_id, connect_details)
    response = virtual_network_client.get_remote_peering_connection(rpc_id)
    if module.params["wait"]:
        states_to_wait_for = module.params["wait_until"] or "PEERED"
        response = oci.wait_until(
            virtual_network_client,
            response,
            evaluate_response=lambda r: r.data.peering_status in states_to_wait_for,
            max_wait_seconds=module.params.get(
                "wait_timeout", oci_utils.MAX_WAIT_TIMEOUT_IN_SECONDS
            ),
        )
    return response.data


def connect_rpc(virtual_network_client, module):
    rpc_id = module.params["remote_peering_connection_id"]
    peer_id = module.params["peer_id"]
    try:
        rpc = virtual_network_client.get_remote_peering_connection(rpc_id).data

        if not are_rpcs_connected(virtual_network_client, rpc, peer_id):
            rpc = connect_rpcs_and_wait(virtual_network_client, module)
            return dict(changed=True, remote_peering_connection=to_dict(rpc))
        else:
            return dict(changed=False, remote_peering_connection=to_dict(rpc))
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            remote_peering_connection_id=dict(
                type="str", required=False, aliases=["id"]
            ),
            peer_region_name=dict(type="str", required=False),
            peer_id=dict(type="str", required=False),
            drg_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["remote_peering_connection_id"])],
        required_together=[["peer_id", "peer_region_name"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    exclude_attributes = {"display_name": True}
    state = module.params["state"]

    if state == "absent":
        result = delete_remote_peering_connection(virtual_network_client, module)

    else:
        remote_peering_connection_id = module.params["remote_peering_connection_id"]
        if remote_peering_connection_id is not None:
            result = update_remote_peering_connection(virtual_network_client, module)
            # A RPC can be connected to another RPC. Perform this operation when peer_id is specified along with
            # remote_peering_connection_id.
            if module.params["peer_id"] is not None:
                result_of_connect_rpc = connect_rpc(virtual_network_client, module)
                result["changed"] = (
                    result["changed"] or result_of_connect_rpc["changed"]
                )
                result["remote_peering_connection"] = result_of_connect_rpc[
                    "remote_peering_connection"
                ]
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="remote_peering_connection",
                create_fn=create_remote_peering_connection,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_remote_peering_connections,
                kwargs_list={
                    "compartment_id": module.params["compartment_id"],
                    "drg_id": module.params["drg_id"],
                },
                module=module,
                model=CreateRemotePeeringConnectionDetails(),
                exclude_attributes=exclude_attributes,
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
