#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_internet_gateway
short_description: Create,update and delete OCI Internet Gateway
description:
    - Creates OCI Internet Gateway
    - Update OCI Internet Gateway, if present, with a new display name
    - Update OCI Internet Gateway, if present, with enable/disable state
    - Delete OCI Internet Gateway, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this Internet Gateway would be created. Mandatory for
                     create operation.Optional for delete and update. Mutually exclusive with I(ig_id).
        required: false
    vcn_id:
        description: Identifier of the Virtual Cloud Network to which the Internet Gateway should be attached. Mandatory
                     for create operation. Optional for delete and update. Mutually exclusive with I(ig_id).
        required: false
    ig_id:
        description: Identifier of the Internet Gateway. Mandatory for delete and update.
        required: false
        aliases: ['id']
    display_name:
        description: Name of the Internet Gateway. A user friendly name. Does not have to be unique, and could be
                     changed. If not specified, a default name would be provided.
        required: false
        aliases: ['name']
    state:
        description: Create,update or delete Internet Gateway. For I(state=present), if it
                     does not exists, it gets created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
    is_enabled:
        description: This option is mandatory for create operation.If I(is_enabled=yes), the gateway would be enabled.
                     If I(is_enabled=no), traffic is not routed to/from the Internet, regardless of route rules.
        required: false
        aliases: ['enabled']
        type: bool
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
#Note: These examples do not set authentication details.
#Create/update Internet Gateway
- name : Create new Internet Gateway in OCI
  oci_internet_gateway:
            compartment_id: 'ocid1.compartment..xdsc'
            vcn_id: 'ocid1.vcn..dsxc'
            name: 'ansible_ig'
            enabled: 'yes'
            freeform_tags:
                  region: 'east'
            defined_tags:
                features:
                   capacity: 'medium'
            state: 'present'
#Update Internet Gateway with ig_id
- name : Update Internet Gateway in OCI
  oci_internet_gateway:
            ig_id: 'ocid1.internetgateway..dsxc'
            display_name: 'ansible_ig'
            is_enabled: 'no'
            state: 'present'

#Delete Internet Gateway
- name : Delete Internet Gateway
  oci_internet_gateway:
            compartment_id: 'ocid1.compartment..xdsc'
            vcn_id: 'ocid1.vcn..dsxc'
            state: 'absent'

#Delete Internet Gateway
- name : Delete Internet Gateway
  oci_internet_gateway:
            id: 'ocid1.internetgateway..xdsc'
            state: 'absent'


"""

RETURN = """
    internet_gateway:
        description: Attributes of the created/updated Internet Gateway.
                    For delete, deleted Internet Gateway description will
                    be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Internet Gateway
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Internet Gateway during creation
                returned: always
                type: string
                sample: ansible_ig
            id:
                description: Identifier of the Internet Gateway
                returned: always
                type: string
                sample: ocid1.internetgateway.oc1.axdf
            vcn_id:
                description: Identifier of the Virtual Cloud Network to which the
                             Internet Gateway is attached.
                returned: always
                type: string
                sample: ocid1.vcn..ixcd
            lifecycle_state:
                description: The current state of the Internet Gateway
                returned: always
                type: string
                sample: ACTIVE
            time_created:
                description: Date and time when the Internet Gateway was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
        sample: {
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "freeform_tags":{"region":"east"},
                    "defined_tags":{"features":{"capacity":"medium"}},
                    "display_name":"ansible_ig",
                    "id":"ocid1.internetgateway.oc1.phx.xxxxxEXAMPLExxxxx",
                    "is_enabled":false,
                    "lifecycle_state":"AVAILABLE",
                    "time_created":"2017-11-12T13:17:36.564000+00:00",
                    "vcn_id":"ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
                }

"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.core.models import (
        CreateInternetGatewayDetails,
        UpdateInternetGatewayDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_internet_gateway(virtual_network_client, module):
    result = dict(changed=False, internet_gateway="")
    ig_id = module.params.get("ig_id")
    exclude_attributes = {"display_name": True}
    try:
        if ig_id:
            result = update_internet_gateway(virtual_network_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="internet_gateway",
                create_fn=create_internet_gateway,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_internet_gateways,
                kwargs_list={
                    "compartment_id": module.params.get("compartment_id"),
                    "vcn_id": module.params.get("vcn_id"),
                },
                module=module,
                exclude_attributes=exclude_attributes,
                model=CreateInternetGatewayDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    return result


def create_internet_gateway(virtual_network_client, module):
    create_internet_gateway_details = CreateInternetGatewayDetails()
    for attribute in create_internet_gateway_details.attribute_map:
        attribute_value = module.params.get(attribute)
        create_internet_gateway_details.__setattr__(attribute, attribute_value)
    result = oci_utils.create_and_wait(
        resource_type="internet_gateway",
        create_fn=virtual_network_client.create_internet_gateway,
        kwargs_create={
            "create_internet_gateway_details": create_internet_gateway_details
        },
        client=virtual_network_client,
        get_fn=virtual_network_client.get_internet_gateway,
        get_param="ig_id",
        module=module,
    )
    return result


def update_internet_gateway(virtual_network_client, module):
    return oci_utils.check_and_update_resource(
        resource_type="internet_gateway",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_internet_gateway,
        kwargs_get={"ig_id": module.params["ig_id"]},
        update_fn=virtual_network_client.update_internet_gateway,
        primitive_params_update=["ig_id"],
        kwargs_non_primitive_update={
            UpdateInternetGatewayDetails: "update_internet_gateway_details"
        },
        module=module,
        update_attributes=UpdateInternetGatewayDetails().attribute_map.keys(),
    )


def delete_internet_gateway(virtual_network_client, module):
    return oci_utils.delete_and_wait(
        resource_type="internet_gateway",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_internet_gateway,
        kwargs_get={"ig_id": module.params["ig_id"]},
        delete_fn=virtual_network_client.delete_internet_gateway,
        kwargs_delete={"ig_id": module.params["ig_id"]},
        module=module,
    )


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            vcn_id=dict(type="str", required=False),
            ig_id=dict(type="str", required=False, aliases=["id"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
            is_enabled=dict(type="bool", required=False, aliases=["enabled"]),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )
    state = module.params["state"]

    if state == "present":
        result = create_or_update_internet_gateway(virtual_network_client, module)
    elif state == "absent":
        result = delete_internet_gateway(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
