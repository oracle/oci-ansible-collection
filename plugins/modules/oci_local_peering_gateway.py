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
module: oci_local_peering_gateway
short_description: Manage Local Peering Gateways(LPGs) in OCI
description:
    - This module allows the user to create, delete, update a local peering gateway(LPG) and connect LPGs in the same
      region in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment containing the local peering gateway (LPG). Required when creating a
                     LPG with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information.
        required: false
        aliases: [ 'name' ]
    state:
        description: Create or update a LPG with I(state=present). Use I(state=absent) to delete a LPG.
        required: false
        default: present
        choices: ['present', 'absent']
    local_peering_gateway_id:
        description: The OCID of the LPG. Required when deleting a LPG with I(state=absent) or updating a LPG with
                     I(state=present).
        required: false
        aliases: [ 'id' ]
    peer_id:
        description: The OCID of the LPG you want to peer with. Required to connect I(local_peering_gateway_id) to
                     another LPG in the same region.
        required: false
    route_table_id:
        description: The OCID of the route table the LPG will use. If you don't specify a route table here, the LPG is
                     created without an associated route table. The Networking service does NOT automatically associate
                     the attached VCN's default route table with the LPG.
        required: false
    skip_exhaustive_search_for_lpg_peerings:
        description: While connecting a LPG to another peer LPG with I(state=present), an exhaustive search
                     looks for all available LPG peerings within the tenancy and tries to detect if the desired LPG
                     peering already exists. This search may yield false positives and it is disabled by default.
                     If set to false, an exhaustive search is conducted and the connect operation fails if it detects
                     that there appears to exist a similar LPG peering in the tenancy.
        required: false
        default: True
    vcn_id:
        description: The OCID of the VCN the LPG belongs to. Required when creating a LPG with I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a LPG
  oci_local_peering_gateway:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: my_local_peering_gateway
    vcn_id: 'ocid1.vcn.oc1..xxxxxEXAMPLExxxxx'

- name: Update the specified LPG's display name
  oci_local_peering_gateway:
    local_peering_gateway_id: ocid1.localpeeringgateway.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_local_peering_gateway

- name: Connect a LPG to another LPG in the same region
  oci_local_peering_gateway:
    local_peering_gateway_id: ocid1.localpeeringgateway.oc1.phx.xxxxxEXAMPLExxxxx
    peer_id: ocid1.localpeeringgateway.oc1.phx.xxxxxEXAMPLExxxxx

- name: Delete the specified LPG
  oci_local_peering_gateway:
    id: ocid1.localpeeringgateway.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
local_peering_gateway:
    description: Information about the LPG
    returned: On successful operation
    type: dict
    sample: {
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
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.identity.identity_client import IdentityClient
    from oci.core.models import CreateLocalPeeringGatewayDetails
    from oci.core.models import UpdateLocalPeeringGatewayDetails
    from oci.core.models import ConnectLocalPeeringGatewaysDetails
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def delete_local_peering_gateway(virtual_network_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="local_peering_gateway",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_local_peering_gateway,
        kwargs_get={
            "local_peering_gateway_id": module.params["local_peering_gateway_id"]
        },
        delete_fn=virtual_network_client.delete_local_peering_gateway,
        kwargs_delete={
            "local_peering_gateway_id": module.params["local_peering_gateway_id"]
        },
        module=module,
    )
    return result


def update_local_peering_gateway(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="local_peering_gateway",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_local_peering_gateway,
        kwargs_get={
            "local_peering_gateway_id": module.params["local_peering_gateway_id"]
        },
        update_fn=virtual_network_client.update_local_peering_gateway,
        primitive_params_update=["local_peering_gateway_id"],
        kwargs_non_primitive_update={
            UpdateLocalPeeringGatewayDetails: "update_local_peering_gateway_details"
        },
        module=module,
        update_attributes=UpdateLocalPeeringGatewayDetails().attribute_map.keys(),
    )
    return result


def create_local_peering_gateway(virtual_network_client, module):
    create_local_peering_gateway_details = CreateLocalPeeringGatewayDetails()
    for attribute in create_local_peering_gateway_details.attribute_map.keys():
        if attribute in module.params:
            setattr(
                create_local_peering_gateway_details,
                attribute,
                module.params[attribute],
            )

    result = oci_utils.create_and_wait(
        resource_type="local_peering_gateway",
        create_fn=virtual_network_client.create_local_peering_gateway,
        kwargs_create={
            "create_local_peering_gateway_details": create_local_peering_gateway_details
        },
        client=virtual_network_client,
        get_fn=virtual_network_client.get_local_peering_gateway,
        get_param="local_peering_gateway_id",
        module=module,
    )
    return result


def get_similar_lpg(
    compartments, virtual_network_client, lpg_cidr_block, peer_lpg_cidr_block, peer_lpg
):
    for compartment in compartments:
        compartment_id = compartment.id
        vcns = []
        try:
            vcns = oci_utils.list_all_resources(
                virtual_network_client.list_vcns, compartment_id=compartment_id
            )
        except ServiceError as ex:
            if ex.status == 403:
                pass

        for vcn in vcns:
            if vcn.cidr_block == peer_lpg_cidr_block:
                debug(
                    "VCN {0} exists with CIDR {1}".format(vcn.id, peer_lpg_cidr_block)
                )
                similar_lpg = get_lpg_in_peered_state_in_vcn(
                    virtual_network_client,
                    compartments,
                    vcn.id,
                    lpg_cidr_block,
                    peer_lpg,
                )
                if similar_lpg:
                    return similar_lpg
    return None


def get_lpg_in_peered_state_in_vcn(
    virtual_network_client, compartments, vcn_id, cidr_block, peer_lpg
):
    for compartment in compartments:
        lpgs = []
        try:
            lpgs = oci_utils.list_all_resources(
                virtual_network_client.list_local_peering_gateways,
                compartment_id=compartment.id,
                vcn_id=vcn_id,
            )
        except ServiceError as ex:
            if ex.status == 403:
                pass
        for lpg in lpgs:
            if lpg.id != peer_lpg.id:
                if (
                    lpg.peering_status == "PEERED"
                    and lpg.peer_advertised_cidr == cidr_block
                ):
                    debug(
                        "Local peering gateway {0} exists in VCN {1} which is PEERED to a VCN with CIDR block {2}.".format(
                            lpg.id, vcn_id, cidr_block
                        )
                    )
                    return lpg
    return None


def matching_lpg_exists(
    virtual_network_client, module, lpg, peer_lpg, lpg_vcn, peer_vcn
):
    tenancy = oci_utils.get_oci_config(module)["tenancy"]
    identity_client = oci_utils.create_service_client(module, IdentityClient)
    compartments = []
    try:
        compartments = oci_utils.list_all_resources(
            identity_client.list_compartments,
            compartment_id=tenancy,
            compartment_id_in_subtree=True,
        )
    except ServiceError as ex:
        if ex.status == 403:
            pass
    similar_lpg = get_similar_lpg(
        compartments,
        virtual_network_client,
        lpg_vcn.cidr_block,
        peer_vcn.cidr_block,
        peer_lpg,
    )
    if similar_lpg:
        module.fail_json(
            msg="Local peering gateway {0} may be connected to local peering gateway {1}.".format(
                similar_lpg.id, lpg.id
            )
        )
    return False


def are_lpgs_connected(virtual_network_client, module, lpg, peer_lpg):
    # Return True if `lpg` & `peer_lpg` are connected.
    #
    # LPG's don't have an attribute which mentions about the ID of the other LPG to which it is connected.
    # To confirm if two LPGs are already connected:
    # 1. check if `peering_status` attribute of `lpg` is PEERED & `peer_advertised_cidr` attribute of `lpg` is same as
    #    the cidr_block of VCN to which the `peer_lpg` belongs.
    # 2. check if `peering_status` attribute of `peer_lpg` is PEERED & `peer_advertised_cidr` attribute of `peer_lpg` is
    #    same as the cidr_block of VCN to which the `lpg` belongs.
    # 3. Make sure there is no other VCN with cidr_block same as cidr_block of VCN to which `peer_lpg` belongs and which
    #    has a LPG which is in PEERED status with `peer_advertised_cidr` equal to cidr_block of VCN to which the `lpg`
    #    belongs.
    # If condition 3 is false, there is a possibility that `lpg` and `peer_lpg` are connected individually to some other
    # LPGs that are in different VCNs but having same CIDR as that of lpg's cidr block & peer_lpg's cidr_block. We
    # throw an error in this case, indicating this possibility. This heuristic may have false positives. So, if an user
    # wants to ignore this invalid failure, "skip_exhaustive_search_for_lpg_peerings" could be employed.

    lpg_vcn = oci_utils.call_with_backoff(
        virtual_network_client.get_vcn, vcn_id=lpg.vcn_id
    ).data
    peer_vcn = oci_utils.call_with_backoff(
        virtual_network_client.get_vcn, vcn_id=peer_lpg.vcn_id
    ).data

    if (
        lpg.peering_status == "PEERED"
        and lpg.peer_advertised_cidr == peer_vcn.cidr_block
    ) and (
        peer_lpg.peering_status == "PEERED"
        and peer_lpg.peer_advertised_cidr == lpg_vcn.cidr_block
    ):
        if module.params["skip_exhaustive_search_for_lpg_peerings"]:
            return True
        else:
            return not matching_lpg_exists(
                virtual_network_client, module, lpg, peer_lpg, lpg_vcn, peer_vcn
            )
    else:
        return False


def connect_lpgs_and_wait(virtual_network_client, module, lpg_id, peer_id):
    connect_details = ConnectLocalPeeringGatewaysDetails()
    connect_details.peer_id = peer_id
    oci_utils.call_with_backoff(
        virtual_network_client.connect_local_peering_gateways,
        local_peering_gateway_id=lpg_id,
        connect_local_peering_gateways_details=connect_details,
    )
    response = oci_utils.call_with_backoff(
        virtual_network_client.get_local_peering_gateway,
        local_peering_gateway_id=lpg_id,
    )
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


def connect_lpg(virtual_network_client, module):
    lpg_id = module.params["local_peering_gateway_id"]
    peer_id = module.params["peer_id"]
    try:
        lpg = oci_utils.call_with_backoff(
            virtual_network_client.get_local_peering_gateway,
            local_peering_gateway_id=lpg_id,
        ).data
        peer_lpg = oci_utils.call_with_backoff(
            virtual_network_client.get_local_peering_gateway,
            local_peering_gateway_id=peer_id,
        ).data
        connected = are_lpgs_connected(virtual_network_client, module, lpg, peer_lpg)
        if not connected:
            lpg = connect_lpgs_and_wait(virtual_network_client, module, lpg_id, peer_id)
            return dict(changed=True, local_peering_gateway=to_dict(lpg))
        else:
            return dict(changed=False, local_peering_gateway=to_dict(lpg))
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def set_logger(my_logger):
    global logger
    logger = my_logger


def get_logger():
    return logger


def debug(s):
    get_logger().debug(s)


def main():
    my_logger = oci_utils.get_logger("oci_local_peering_gateway")
    set_logger(my_logger)
    module_args = oci_utils.get_taggable_arg_spec(
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
            local_peering_gateway_id=dict(type="str", required=False, aliases=["id"]),
            peer_id=dict(type="str", required=False),
            vcn_id=dict(type="str", required=False),
            route_table_id=dict(type="str", required=False),
            skip_exhaustive_search_for_lpg_peerings=dict(
                type=bool, required=False, default=True
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ("state", "absent", ["local_peering_gateway_id"]),
            ("peer_id", not None, ["local_peering_gateway_id"]),
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    exclude_attributes = {"display_name": True}
    state = module.params["state"]

    if state == "absent":
        result = delete_local_peering_gateway(virtual_network_client, module)

    else:
        local_peering_gateway_id = module.params["local_peering_gateway_id"]
        if local_peering_gateway_id is not None:
            result = update_local_peering_gateway(virtual_network_client, module)
            # A LPG can be connected to another LPG. Perform this operation when peer_id is specified along with
            # local_peering_gateway_id.
            if module.params["peer_id"] is not None:
                result_of_connect_lpg = connect_lpg(virtual_network_client, module)
                result["changed"] = (
                    result["changed"] or result_of_connect_lpg["changed"]
                )
                result["local_peering_gateway"] = result_of_connect_lpg[
                    "local_peering_gateway"
                ]
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="local_peering_gateway",
                create_fn=create_local_peering_gateway,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_local_peering_gateways,
                kwargs_list={
                    "compartment_id": module.params["compartment_id"],
                    "vcn_id": module.params["vcn_id"],
                },
                module=module,
                model=CreateLocalPeeringGatewayDetails(),
                exclude_attributes=exclude_attributes,
                default_attribute_values={"route_table_id": None},
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
