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
module: oci_service_gateway
short_description: Manage service gateways in OCI
description:
    - This module allows the user to create, block or allow traffic to, delete and update a service gateway in OCI.
version_added: "2.5"
options:
    block_traffic:
        description: Whether the service gateway blocks all traffic through it. The default is false. When this is true,
                     traffic is not routed to any services, regardless of route rules.
        required: false
        default: false
        type: bool
    compartment_id:
        description: The OCID of the compartment to contain the service gateway. Required when creating a service
                     gateway with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
        required: false
        aliases: [ 'name' ]
    state:
        description: Use I(state=present) to create or update a service gateway or enable a service on a gateway. Use
                     I(state=absent) to delete a service gateway or disable a service on a  gateway.
        required: false
        default: present
        choices: ['present', 'absent']
    service_gateway_id:
        description: The OCID of the service gateway. Required when deleting a service gateway with I(state=absent) or
                     updating a service gateway with I(state=present) or to enable a service on a gateway using
                     I(state=present) or to disable a service on a gateway.
        required: false
        aliases: [ 'id' ]
    service_id:
        description: The OCID of the service. Required to enable a service on a gateway using I(state=present) or
                     disable a service on a gateway using I(state=absent).
        required: false
    services:
        description: List of the service OCIDs. These are the services that will be enabled on the service gateway. This
                     list can be empty. Required to create a service gateway with I(state=present) or update services
                     enabled on a service gateway.
        required: false
    vcn_id:
        description: The OCID of the VCN. Required to create a service gateway with I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a service gateway
  oci_service_gateway:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    services:
        - service_id: ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx
        - service_id: ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx
    vcn_id: 'ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx'
    display_name: my_service_gateway

- name: Update list of all the services to be enabled on a service gateway
  oci_service_gateway:
    id: ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx
    services:
        - service_id: ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx

- name: Update service gateway to disable all services by using an empty list
  oci_service_gateway:
    id: ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx
    services: []

- name: Block all traffic through the service gateway
  oci_service_gateway:
    id: ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx
    block_traffic: True

- name: Allow traffic through the service gateway
  oci_service_gateway:
    id: ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx
    block_traffic: False

- name: Update the specified service gateway's display name
  oci_service_gateway:
    service_gateway_id: ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_service_gateway

- name: Enable/attach a service on a service gateway
  oci_service_gateway:
    service_gateway_id: ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx
    service_id: ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx

- name: Disable/detach a service from a service gateway
  oci_service_gateway:
    service_gateway_id: ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx
    service_id: ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent

- name: Delete the specified service gateway
  oci_service_gateway:
    id: ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
service_gateway:
    description: Information about the service gateway
    returned: On successful operation
    type: dict
    sample: {
            "block_traffic": false,
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_service_gateway",
            "freeform_tags": {},
            "id": "ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "services": [{
                        "service_id": "ocid1.service.oc1.phx.xxxxxEXAMPLExxxxx",
                        "service_name": "OCI IAD Object Storage"
                        }],
            "time_created": "2017-11-13T20:22:40.626000+00:00",
            "vcn_id": ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import (
        CreateServiceGatewayDetails,
        UpdateServiceGatewayDetails,
        ServiceIdRequestDetails,
    )
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_service_gateway(virtual_network_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="service_gateway",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_service_gateway,
        kwargs_get={"service_gateway_id": module.params["service_gateway_id"]},
        delete_fn=virtual_network_client.delete_service_gateway,
        kwargs_delete={"service_gateway_id": module.params["service_gateway_id"]},
        module=module,
    )
    return result


def update_service_gateway(virtual_network_client, module):
    serviceid_requests = None
    if module.params["services"] is not None:
        serviceid_requests = []
        for service in module.params["services"]:
            req = ServiceIdRequestDetails()
            req.service_id = service["service_id"]
            serviceid_requests.append(req)
    result = oci_utils.check_and_update_resource(
        resource_type="service_gateway",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_service_gateway,
        kwargs_get={"service_gateway_id": module.params["service_gateway_id"]},
        update_fn=virtual_network_client.update_service_gateway,
        primitive_params_update=["service_gateway_id"],
        kwargs_non_primitive_update={
            UpdateServiceGatewayDetails: "update_service_gateway_details"
        },
        module=module,
        update_attributes=UpdateServiceGatewayDetails().attribute_map.keys(),
        sub_attributes_of_update_model={"services": serviceid_requests},
    )
    return result


def create_service_gateway(virtual_network_client, module):
    create_service_gateway_details = CreateServiceGatewayDetails()
    for attribute in create_service_gateway_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_service_gateway_details, attribute, module.params[attribute])

    list_of_request_details = []
    if module.params["services"] is not None:
        for req in module.params["services"]:
            req_details = ServiceIdRequestDetails()
            req_details.service_id = req["service_id"]
            list_of_request_details.append(req_details)
    create_service_gateway_details.services = list_of_request_details
    result = oci_utils.create_and_wait(
        resource_type="service_gateway",
        create_fn=virtual_network_client.create_service_gateway,
        kwargs_create={
            "create_service_gateway_details": create_service_gateway_details
        },
        client=virtual_network_client,
        get_fn=virtual_network_client.get_service_gateway,
        get_param="service_gateway_id",
        module=module,
    )
    return result


def is_service_attached_to_gateway(service_gateway, svc_id):
    for service in service_gateway.services:
        if service.service_id == svc_id:
            return True
    return False


def handle_service_id_request(virtual_network_client, module, attach):
    service_gateway_id = module.params["service_gateway_id"]
    try:
        service_gateway = oci_utils.call_with_backoff(
            virtual_network_client.get_service_gateway,
            service_gateway_id=service_gateway_id,
        ).data

        # Check if the service is in desired state stated by `attach` boolean variable.
        if (
            is_service_attached_to_gateway(service_gateway, module.params["service_id"])
            == attach
        ):
            return {"service_gateway": to_dict(service_gateway), "changed": False}
        else:
            # Enable service on the service gateway.
            service_details = ServiceIdRequestDetails()
            for attribute in service_details.attribute_map.keys():
                if attribute in module.params:
                    setattr(service_details, attribute, module.params[attribute])
            if attach:
                service_gateway = oci_utils.call_with_backoff(
                    virtual_network_client.attach_service_id,
                    service_gateway_id=service_gateway_id,
                    attach_service_details=service_details,
                ).data
            else:
                service_gateway = oci_utils.call_with_backoff(
                    virtual_network_client.detach_service_id,
                    service_gateway_id=service_gateway_id,
                    detach_service_details=service_details,
                ).data
            return {"service_gateway": to_dict(service_gateway), "changed": True}
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            block_traffic=dict(type="bool", required=False, default=False),
            service_id=dict(type="str", required=False),
            vcn_id=dict(type="str", required=False),
            services=dict(type="list", required=False),
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            service_gateway_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["service_gateway_id"])],
        mutually_exclusive=[["service_id", "services"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    exclude_attributes = {"display_name": True}
    state = module.params["state"]

    if state == "absent":
        if module.params["service_id"]:
            # Detach service from service gateway.
            result = handle_service_id_request(virtual_network_client, module, False)
        else:
            # Delete service gateway.
            result = delete_service_gateway(virtual_network_client, module)

    else:
        service_gateway_id = module.params["service_gateway_id"]
        if service_gateway_id is not None:
            # Update service gateway details.
            result = update_service_gateway(virtual_network_client, module)
            if module.params["service_id"]:
                # Attach/detach service to service gateway.
                serviceid_request_result = handle_service_id_request(
                    virtual_network_client, module, True
                )
                result["changed"] = (
                    serviceid_request_result["changed"] or result["changed"]
                )
                result["service_gateway"] = serviceid_request_result["service_gateway"]
        else:
            # Create service gateway.
            result = oci_utils.check_and_create_resource(
                resource_type="service_gateway",
                create_fn=create_service_gateway,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_service_gateways,
                kwargs_list={
                    "compartment_id": module.params["compartment_id"],
                    "vcn_id": module.params["vcn_id"],
                },
                module=module,
                model=CreateServiceGatewayDetails(),
                exclude_attributes=exclude_attributes,
            )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
