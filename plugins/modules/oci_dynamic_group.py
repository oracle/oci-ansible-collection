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
module: oci_dynamic_group
short_description: Manage dynamic groups in OCI
description:
    - This module allows the user to create, delete and update dynamic groups in Oracle Cloud Infrastructure.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the tenancy containing the group. Required to create a dynamic group.
        required: false
    description:
        description: The description you assign to the group during creation. Does not have to be unique, and it's
                     changeable. Required to create a dynamic group.
        required: false
    dynamic_group_id:
        description: The OCID of the dynamic group. Required to delete or update a dynamic group.
        required: false
        aliases: [ 'id' ]
    matching_rule:
        description: The matching rule to dynamically match an instance certificate to this dynamic group. For rule
                     syntax, see
                     U(https://docs.us-phoenix-1.oraclecloud.com/Content/Identity/Tasks/managingdynamicgroups.htm).
                     Required to create a dynamic group.
        required: false
    name:
        description: The name you assign to the group during creation. The name must be unique across all groups in the
                     tenancy and cannot be changed. Required to create a dynamic group.
        required: false
    state:
        description: Create or update a dynamic group with I(state=present). Use I(state=absent) to delete a dynamic
                     group.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a dynamic group
  oci_dynamic_group:
    compartment_id: ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx
    description: Group for all instances that are in a specific compartment
    matching_rule: "instance.compartment.id = 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'"
    name: Sample dynamic group

- name: Update matching rule and description of a dynamic group
  oci_dynamic_group:
    id: ocid1.dynamicgroup.oc1..xxxxxEXAMPLExxxxx
    description: Group for all instances with the tag namespace and tag key operations.department
    matching_rule: "tag.operations.department.value"

- name: Delete a dynamic group
  oci_dynamic_group:
    id: ocid1.dynamicgroup.oc1..xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
dynamic_group:
    description: Information about the dynamic group
    returned: On successful create, delete & update operation
    type: dict
    sample: {
            "compartment_id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx",
            "description": "Group for all instances with the tag namespace and tag key operations.department",
            "id": "ocid1.dynamicgroup.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status": null,
            "lifecycle_state": "ACTIVE",
            "matching_rule": "tag.operations.department.value",
            "name": "Sample dynamic group",
            "time_created": "2018-07-05T09:38:27.176000+00:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import CreateDynamicGroupDetails
    from oci.identity.models import UpdateDynamicGroupDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_dynamic_group(identity_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="dynamic_group",
        client=identity_client,
        get_fn=identity_client.get_dynamic_group,
        kwargs_get={"dynamic_group_id": module.params["dynamic_group_id"]},
        delete_fn=identity_client.delete_dynamic_group,
        kwargs_delete={"dynamic_group_id": module.params["dynamic_group_id"]},
        module=module,
    )
    return result


def update_dynamic_group(identity_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="dynamic_group",
        client=identity_client,
        get_fn=identity_client.get_dynamic_group,
        kwargs_get={"dynamic_group_id": module.params["dynamic_group_id"]},
        update_fn=identity_client.update_dynamic_group,
        primitive_params_update=["dynamic_group_id"],
        kwargs_non_primitive_update={
            UpdateDynamicGroupDetails: "update_dynamic_group_details"
        },
        module=module,
        update_attributes=UpdateDynamicGroupDetails().attribute_map.keys(),
    )

    return result


def create_dynamic_group(identity_client, module):
    create_dynamic_group_details = CreateDynamicGroupDetails()
    for attribute in create_dynamic_group_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_dynamic_group_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(
        resource_type="dynamic_group",
        create_fn=identity_client.create_dynamic_group,
        kwargs_create={"create_dynamic_group_details": create_dynamic_group_details},
        client=identity_client,
        get_fn=identity_client.get_dynamic_group,
        get_param="dynamic_group_id",
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            description=dict(type="str", required=False),
            matching_rule=dict(type="str", required=False),
            name=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            dynamic_group_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["dynamic_group_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    state = module.params["state"]
    dynamic_group_id = module.params["dynamic_group_id"]

    if state == "absent":
        result = delete_dynamic_group(identity_client, module)

    else:
        if dynamic_group_id is not None:
            result = update_dynamic_group(identity_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="dynamic_group",
                create_fn=create_dynamic_group,
                kwargs_create={"identity_client": identity_client, "module": module},
                list_fn=identity_client.list_dynamic_groups,
                kwargs_list={"compartment_id": module.params["compartment_id"]},
                module=module,
                model=CreateDynamicGroupDetails(),
            )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
