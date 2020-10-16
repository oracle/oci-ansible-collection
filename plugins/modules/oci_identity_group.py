#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_identity_group
short_description: Manage a Group resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Group resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new group in your tenancy.
    - You must specify your tenancy's OCID as the compartment ID in the request object (remember that the tenancy
      is simply the root compartment). Notice that IAM resources (users, groups, compartments, and some policies)
      reside within the tenancy itself, unlike cloud resources such as compute instances, which typically
      reside within compartments inside the tenancy. For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "You must also specify a *name* for the group, which must be unique across all groups in your tenancy and
      cannot be changed. You can use this name or the OCID when writing policies that apply to the group. For more
      information about policies, see L(How Policies Work,https://docs.cloud.oracle.com/Content/Identity/Concepts/policies.htm)."
    - "You must also specify a *description* for the group (although it can be an empty string). It does not
      have to be unique, and you can change it anytime with L(UpdateGroup,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/20160918/Group/UpdateGroup)."
    - After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
      object, first make sure its `lifecycleState` has changed to ACTIVE.
    - After creating the group, you need to put users in it and write policies for it.
      See L(AddUserToGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/UserGroupMembership/AddUserToGroup) and
      L(CreatePolicy,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Policy/CreatePolicy).
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy containing the group.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - The name you assign to the group during creation. The name must be unique across all groups
              in the tenancy and cannot be changed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The description you assign to the group during creation. Does not have to be unique, and it's changeable.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    group_id:
        description:
            - The OCID of the group.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Group.
            - Use I(state=present) to create or update a Group.
            - Use I(state=absent) to delete a Group.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create group
  oci_identity_group:
    compartment_id: ocid1.tenancy.oc1..aaaaaaaaba3pvexampleuniqueID
    description: Group for network administrators
    name: NetworkAdmins

- name: Update group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_group:
    compartment_id: ocid1.tenancy.oc1..aaaaaaaaba3pvexampleuniqueID
    name: NetworkAdmins
    description: Group for network administrators
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update group
  oci_identity_group:
    description: Group for network administrators
    freeform_tags: {'Department': 'Finance'}
    group_id: ocid1.group.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete group
  oci_identity_group:
    group_id: ocid1.group.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete group using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_group:
    compartment_id: ocid1.tenancy.oc1..aaaaaaaaba3pvexampleuniqueID
    name: NetworkAdmins
    state: absent

"""

RETURN = """
group:
    description:
        - Details of the Group resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the group.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the tenancy containing the group.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        name:
            description:
                - The name you assign to the group during creation. The name must be unique across all groups in
                  the tenancy and cannot be changed.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description you assign to the group. Does not have to be unique, and it's changeable.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - Date and time the group was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The group's current state. After creating a group, make sure its `lifecycleState` changes from CREATING to
                  ACTIVE before using it.
            returned: on success
            type: string
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient
    from oci.identity.models import CreateGroupDetails
    from oci.identity.models import UpdateGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GroupHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "group_id"

    def get_module_resource_id(self):
        return self.module.params.get("group_id")

    def get_get_fn(self):
        return self.client.get_group

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_group, group_id=self.module.params.get("group_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_groups, **kwargs)

    def get_create_model_class(self):
        return CreateGroupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_group,
            call_fn_args=(),
            call_fn_kwargs=dict(create_group_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateGroupDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                group_id=self.module.params.get("group_id"),
                update_group_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_group,
            call_fn_args=(),
            call_fn_kwargs=dict(group_id=self.module.params.get("group_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


GroupHelperCustom = get_custom_class("GroupHelperCustom")


class ResourceHelper(GroupHelperCustom, GroupHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            group_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="group",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
