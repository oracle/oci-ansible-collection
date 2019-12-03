#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
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
module: oci_cross_connect
short_description: Create,update and delete OCI cross-connects
description:
    - Create an OCI cross-connect
    - Update an OCI cross-connect, if present, with a new display name
    - Activate an OCI cross-connect
    - Delete an OCI cross-connect, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this cross-connect would be created. Mandatory for
                     create operation. Mutually exclusive with I(cross_connect_id).
        required: false
    cross_connect_group_id:
        description: The OCID of the cross-connect group to put this cross-connect in.
        required: false
    cross_connect_id:
        description: Identifier of the cross-connect. Mandatory for delete and update.
        required: false
        aliases: ['id']
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
                     Avoid entering confidential information.
        required: false
        aliases: ['name']
    far_cross_connect_or_cross_connect_group_id:
        description: If you already have an existing cross-connect or cross-connect group at this FastConnect location,
                     and you want this new cross-connect to be on a different router (for the purposes of redundancy),
                     provide the OCID of that existing cross-connect or cross-connect group.
        required: false
    near_cross_connect_or_cross_connect_group_id:
        description: If you already have an existing cross-connect or cross-connect group at this FastConnect location,
                     and you want this new cross-connect to be on the same router, provide the OCID of that existing
                     cross-connect or cross-connect group.
        required: false
    location_name:
        description: The name of the FastConnect location where this cross-connect will be installed.
        required: false
    port_speed_shape_name:
        description: The port speed for this cross-connect.
        required: false
    is_active:
        description: Set to true to activate the cross-connect. You activate it after the physical cabling is complete,
                     and you've confirmed the cross-connect's light levels are good and your side of the interface is up.
                     Activation indicates to Oracle that the physical connection is ready.
        required: false
    state:
        description: Create,update or delete cross-connect. For I(state=present), if it
                     does not exists, it gets created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options, oracle_creatable_resource ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create a new cross-connect
- name: Create a new cross-connect
  oci_cross_connect:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      display_name: 'ansible-cross-connect'
      cross_connect_group_id: 'ocid1.crossconnectgroup..xvdf'
      far_cross_connect_or_cross_connect_group_id: 'ocid1.crossconnect..xxxxxEXAMPLExxxxx'
      location_name: 'EXAMPLE LOCATION'
      port_speed_shape_name: '10 Gbps'
      state: 'present'

# Update an existing cross-connect's display Name
- name: Update an existing cross-connect's display Name
  oci_cross_connect:
      cross_connect_id: 'ocid1.crossconnect..xxxxxEXAMPLExxxxx'
      display_name: 'cross-connect-updated'
      state: 'present'

# Activate a cross-connect
- name: Update cross-connect Active state
  oci_cross_connect:
      cross_connect_id: 'ocid1.crossconnect..xxxxxEXAMPLExxxxx'
      is_active: True
      state: 'present'

# Delete a cross-connect
- name: Delete cross-connect
  oci_cross_connect:
      cross_connect_id: 'ocid1.crossconnect..xxxxxEXAMPLExxxxx'
      state: 'absent'
"""

RETURN = """
    cross_connect:
        description: Attributes of the cross-connect.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The OCID of the compartment containing the cross-connect group.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx
            cross_connect_group_id:
                description: The OCID of the cross-connect group this cross-connect belongs to (if any).
                returned: always
                type: string
                sample: ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx
            display_name:
                description: A user-friendly name. Does not have to be unique, and it's changeable.
                             Avoid entering confidential information.
                returned: always
                type: string
                sample: ansible-cross-connect
            id:
                description: Identifier of the cross-connect.
                returned: always
                type: string
                sample: ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the cross-connect was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            lifecycle_state:
                description: The current state of the cross-connect.
                returned: always
                type: string
                sample: PROVISIONED
            location_name:
                description: The name of the FastConnect location where this cross-connect is installed.
                returned: always
                type: string
                sample: EXAMPLE LOCATION
            port_name:
                description: A string identifying the meet-me room port for this cross-connect.
                returned: always
                type: string
                sample: EXAMPLE
            port_speed_shape_name:
                description: The port speed for this cross-connect.
                returned: always
                type: string
                sample: 10 Gbps
        sample: {
                    "compartment_id":"ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx",
                    "cross_connect_group_id":"ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"ansible-cross-connect",
                    "id":"ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"PROVISIONING",
                    "location_name":"EXAMPLE LOCATION",
                    "port_name":"EXAMPLE PORT",
                    "port_speed_shape_name":"10 Gbps",
                    "time_created":"2018-03-03T06:55:49.463000+00:00"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.core.models import CreateCrossConnectDetails, UpdateCrossConnectDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_cross_connect(virtual_network_client, module):
    result = dict(changed=False, cross_connect="")
    cross_connect_id = module.params.get("cross_connect_id")
    exclude_attributes = {"display_name": True}
    try:
        if cross_connect_id:
            existing_cross_connect = oci_utils.get_existing_resource(
                virtual_network_client.get_cross_connect,
                module,
                cross_connect_id=cross_connect_id,
            )
            result = update_cross_connect(
                virtual_network_client, existing_cross_connect, module
            )
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="cross_connect",
                create_fn=create_cross_connect,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_cross_connects,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module,
                exclude_attributes=exclude_attributes,
                model=CreateCrossConnectDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    return result


def create_cross_connect(virtual_network_client, module):
    create_cross_connect_details = CreateCrossConnectDetails()
    for attribute in create_cross_connect_details.attribute_map:
        create_cross_connect_details.__setattr__(
            attribute, module.params.get(attribute)
        )
    result = oci_utils.create_and_wait(
        resource_type="cross_connect",
        create_fn=virtual_network_client.create_cross_connect,
        kwargs_create={"create_cross_connect_details": create_cross_connect_details},
        client=virtual_network_client,
        get_fn=virtual_network_client.get_cross_connect,
        get_param="cross_connect_id",
        module=module,
        states=["PENDING_CUSTOMER", "PENDING_PROVIDER", "PROVISIONED"],
    )
    return result


def update_cross_connect(virtual_network_client, existing_cross_connect, module):
    result = oci_utils.check_and_update_resource(
        resource_type="cross_connect",
        get_fn=virtual_network_client.get_cross_connect,
        kwargs_get={"cross_connect_id": module.params["cross_connect_id"]},
        update_fn=virtual_network_client.update_cross_connect,
        primitive_params_update=["cross_connect_id"],
        kwargs_non_primitive_update={
            UpdateCrossConnectDetails: "update_cross_connect_details"
        },
        module=module,
        update_attributes=UpdateCrossConnectDetails().attribute_map.keys(),
        states=["PENDING_CUSTOMER", "PENDING_PROVIDER", "PROVISIONED"],
    )
    return result


def delete_cross_connect(virtual_network_client, module):
    return oci_utils.delete_and_wait(
        resource_type="cross_connect",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_cross_connect,
        kwargs_get={"cross_connect_id": module.params["cross_connect_id"]},
        delete_fn=virtual_network_client.delete_cross_connect,
        kwargs_delete={"cross_connect_id": module.params["cross_connect_id"]},
        module=module,
    )


def main():
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        compartment_id=dict(type="str", required=False),
        display_name=dict(type="str", required=False, aliases=["name"]),
        cross_connect_group_id=dict(type="str", required=False),
        cross_connect_id=dict(type="str", required=False, aliases=["id"]),
        state=dict(
            type="str", required=False, default="present", choices=["present", "absent"]
        ),
        far_cross_connect_or_cross_connect_group_id=dict(type="str", required=False),
        near_cross_connect_or_cross_connect_group_id=dict(type="str", required=False),
        location_name=dict(type="str", required=False),
        port_speed_shape_name=dict(type="str", required=False),
        is_active=dict(type=bool, required=False),
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    state = module.params["state"]

    if state == "present":
        result = create_or_update_cross_connect(virtual_network_client, module)
    elif state == "absent":
        result = delete_cross_connect(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
