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
module: oci_cross_connect_group
short_description: Create, update and delete OCI cross-connect groups
description:
    - Create an OCI cross-connect group to use with Oracle Cloud Infrastructure FastConnect
    - Update an OCI cross-connect group, if present, with a new display name
    - Delete an OCI cross-connect group, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this cross-connect group
                     would be created. Mandatory for create operation.
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
                     Avoid entering confidential information.
        required: false
        aliases: ['name']
    cross_connect_group_id:
        description: Identifier of the cross-connect group. Mandatory for update and delete.
        required: false
        aliases: ['id']
    state:
        description: Create,update or delete cross-connect group. For I(state=present), if it
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
# Create cross-connect group
- name: Create cross-connect group
  oci_cross_connect_group:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      display_name: 'ansible-cross-connect-group'
      state: 'present'

# Update cross-connect group's Display Name
- name: Update cross-connect group's Display Name
  oci_cross_connect_group:
      cross_connect_grou_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
      display_name: 'cross-connect-group-updated'
      state: 'present'

# Delete cross-connect
- name: Delete cross-connect group
  oci_cross_connect_group:
      cross_connect_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
      state: 'absent'
"""

RETURN = """
    oci_cross_connect_group:
        description: Attributes of the cross-connect group.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The OCID of the compartment containing the cross-connect group.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx
            display_name:
                description: A user-friendly name. Does not have to be unique, and it's changeable.
                             Avoid entering confidential information.
                returned: always
                type: string
                sample: ansible-cross-connect-group
            id:
                description: Identifier of the cross-connect group.
                returned: always
                type: string
                sample: ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the cross-connect group was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            lifecycle_state:
                description: The current state of the cross-connect group.
                returned: always
                type: string
                sample: PROVISIONED
        sample: {
                    "compartment_id":"ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"ansible-cross-connect-group",
                    "id":"ocid1.crossconnectgroup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"PROVISIONING",
                    "time_created":"2018-03-03T06:55:49.463000+00:00"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.core.models import (
        CreateCrossConnectGroupDetails,
        UpdateCrossConnectGroupDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_cross_connect_group(virtual_network_client, module):
    result = dict(changed=False, cross_connect_group="")
    cross_connect_group_id = module.params.get("cross_connect_group_id")
    exclude_attributes = {"display_name": True}
    try:
        if cross_connect_group_id:
            existing_cross_connect_group = oci_utils.get_existing_resource(
                virtual_network_client.get_cross_connect_group,
                module,
                cross_connect_group_id=cross_connect_group_id,
            )
            result = update_cross_connect_group(
                virtual_network_client, existing_cross_connect_group, module
            )
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="cross_connect_group",
                create_fn=create_cross_connect_group,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_cross_connect_groups,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module,
                exclude_attributes=exclude_attributes,
                model=CreateCrossConnectGroupDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    return result


def create_cross_connect_group(virtual_network_client, module):
    create_cross_connect_group_details = CreateCrossConnectGroupDetails()
    for attribute in create_cross_connect_group_details.attribute_map:
        create_cross_connect_group_details.__setattr__(
            attribute, module.params.get(attribute)
        )
    result = oci_utils.create_and_wait(
        resource_type="cross_connect_group",
        create_fn=virtual_network_client.create_cross_connect_group,
        kwargs_create={
            "create_cross_connect_group_details": create_cross_connect_group_details
        },
        client=virtual_network_client,
        get_fn=virtual_network_client.get_cross_connect_group,
        get_param="cross_connect_group_id",
        module=module,
        states=["INACTIVE", "PROVISIONED"],
    )
    return result


def update_cross_connect_group(
    virtual_network_client, existing_cross_connect_group, module
):
    result = oci_utils.check_and_update_resource(
        resource_type="cross_connect_group",
        get_fn=virtual_network_client.get_cross_connect_group,
        kwargs_get={"cross_connect_group_id": module.params["cross_connect_group_id"]},
        update_fn=virtual_network_client.update_cross_connect_group,
        primitive_params_update=["cross_connect_group_id"],
        kwargs_non_primitive_update={
            UpdateCrossConnectGroupDetails: "update_cross_connect_group_details"
        },
        module=module,
        client=virtual_network_client,
        update_attributes=UpdateCrossConnectGroupDetails().attribute_map.keys(),
        states=["INACTIVE", "PROVISIONED"],
    )
    return result


def delete_cross_connect_group(virtual_network_client, module):
    return oci_utils.delete_and_wait(
        resource_type="cross_connect_group",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_cross_connect_group,
        kwargs_get={"cross_connect_group_id": module.params["cross_connect_group_id"]},
        delete_fn=virtual_network_client.delete_cross_connect_group,
        kwargs_delete={
            "cross_connect_group_id": module.params["cross_connect_group_id"]
        },
        module=module,
    )


def main():
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        compartment_id=dict(type="str", required=False),
        cross_connect_group_id=dict(type="str", required=False, aliases=["id"]),
        display_name=dict(type="str", required=False, aliases=["name"]),
        state=dict(
            type="str", required=False, default="present", choices=["present", "absent"]
        ),
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    state = module.params["state"]

    if state == "present":
        result = create_or_update_cross_connect_group(virtual_network_client, module)
    elif state == "absent":
        result = delete_cross_connect_group(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
