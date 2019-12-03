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
module: oci_nat_gateway
short_description: Manage NAT gateways in OCI
description:
    - This module allows the user to create, block or allow traffic to, delete and update a NAT gateway in OCI.
version_added: "2.5"
options:
    block_traffic:
        description: Whether the NAT gateway blocks traffic through it.
        required: false
        default: false
        type: bool
    compartment_id:
        description: The OCID of the compartment to contain the NAT gateway. Required when creating a NAT
                     gateway with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
        required: false
        aliases: [ 'name' ]
    state:
        description: Use I(state=present) to create or update a NAT gateway. Use I(state=absent) to delete a NAT
                     gateway.
        required: false
        default: present
        choices: ['present', 'absent']
    nat_gateway_id:
        description: The OCID of the NAT gateway. Required when deleting a NAT gateway with I(state=absent) or
                     updating a NAT gateway with I(state=present).
        required: false
        aliases: [ 'id' ]
    vcn_id:
        description: The OCID of the VCN the gateway belongs to. Required to create a NAT gateway with I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a NAT gateway
  oci_nat_gateway:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    vcn_id: 'ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx'
    display_name: my_nat_gateway

- name: Update NAT gateway display name
  oci_nat_gateway:
    id: ocid1.natgateway.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_nat_gateway

- name: Block all traffic through the NAT gateway
  oci_nat_gateway:
    id: ocid1.natgateway.oc1.phx.xxxxxEXAMPLExxxxx
    block_traffic: True

- name: Delete the specified NAT gateway
  oci_nat_gateway:
    id: ocid1.natgateway.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
nat_gateway:
    description: Information about the NAT gateway
    returned: On successful operation
    type: dict
    sample: {
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
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreateNatGatewayDetails, UpdateNatGatewayDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_nat_gateway(virtual_network_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="nat_gateway",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_nat_gateway,
        kwargs_get={"nat_gateway_id": module.params["nat_gateway_id"]},
        delete_fn=virtual_network_client.delete_nat_gateway,
        kwargs_delete={"nat_gateway_id": module.params["nat_gateway_id"]},
        module=module,
    )
    return result


def update_nat_gateway(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="nat_gateway",
        get_fn=virtual_network_client.get_nat_gateway,
        client=virtual_network_client,
        kwargs_get={"nat_gateway_id": module.params["nat_gateway_id"]},
        update_fn=virtual_network_client.update_nat_gateway,
        primitive_params_update=["nat_gateway_id"],
        kwargs_non_primitive_update={
            UpdateNatGatewayDetails: "update_nat_gateway_details"
        },
        module=module,
        update_attributes=UpdateNatGatewayDetails().attribute_map.keys(),
    )
    return result


def create_nat_gateway(virtual_network_client, module):
    create_nat_gateway_details = CreateNatGatewayDetails()
    for attribute in create_nat_gateway_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_nat_gateway_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(
        resource_type="nat_gateway",
        create_fn=virtual_network_client.create_nat_gateway,
        kwargs_create={"create_nat_gateway_details": create_nat_gateway_details},
        client=virtual_network_client,
        get_fn=virtual_network_client.get_nat_gateway,
        get_param="nat_gateway_id",
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            block_traffic=dict(type="bool", required=False, default=False),
            vcn_id=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            nat_gateway_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["nat_gateway_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    exclude_attributes = {"display_name": True}
    state = module.params["state"]

    if state == "absent":
        result = delete_nat_gateway(virtual_network_client, module)

    else:
        if module.params["nat_gateway_id"] is not None:
            result = update_nat_gateway(virtual_network_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="nat_gateway",
                create_fn=create_nat_gateway,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_nat_gateways,
                kwargs_list={
                    "compartment_id": module.params["compartment_id"],
                    "vcn_id": module.params["vcn_id"],
                },
                module=module,
                model=CreateNatGatewayDetails(),
                exclude_attributes=exclude_attributes,
            )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
