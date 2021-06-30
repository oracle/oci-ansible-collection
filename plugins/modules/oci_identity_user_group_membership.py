#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_identity_user_group_membership
short_description: Manage an UserGroupMembership resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an UserGroupMembership resource in Oracle Cloud Infrastructure
    - For I(state=present), adds the specified user to the specified group and returns a `UserGroupMembership` object with its own OCID.
    - After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using the
      object, first make sure its `lifecycleState` has changed to ACTIVE.
version_added: "2.9"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
            - Required for create using I(state=present).
        type: str
    group_id:
        description:
            - The OCID of the group.
            - Required for create using I(state=present).
        type: str
    user_group_membership_id:
        description:
            - The OCID of the userGroupMembership.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the UserGroupMembership.
            - Use I(state=present) to create an UserGroupMembership.
            - Use I(state=absent) to delete an UserGroupMembership.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create user_group_membership
  oci_identity_user_group_membership:
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    group_id: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete user_group_membership
  oci_identity_user_group_membership:
    user_group_membership_id: "ocid1.usergroupmembership.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
user_group_membership:
    description:
        - Details of the UserGroupMembership resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the membership.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the user, group, and membership object.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        group_id:
            description:
                - The OCID of the group.
            returned: on success
            type: string
            sample: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The OCID of the user.
            returned: on success
            type: string
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the membership was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The membership's current state.  After creating a membership object, make sure its `lifecycleState` changes
                  from CREATING to ACTIVE before using it.
            returned: on success
            type: string
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "group_id": "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56
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
    from oci.identity.models import AddUserToGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UserGroupMembershipHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "user_group_membership_id"

    def get_module_resource_id(self):
        return self.module.params.get("user_group_membership_id")

    def get_get_fn(self):
        return self.client.get_user_group_membership

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user_group_membership,
            user_group_membership_id=self.module.params.get("user_group_membership_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["user_id", "group_id"]

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
        return oci_common_utils.list_all_resources(
            self.client.list_user_group_memberships, **kwargs
        )

    def get_create_model_class(self):
        return AddUserToGroupDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_user_to_group,
            call_fn_args=(),
            call_fn_kwargs=dict(add_user_to_group_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_user_from_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_group_membership_id=self.module.params.get(
                    "user_group_membership_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


UserGroupMembershipHelperCustom = get_custom_class("UserGroupMembershipHelperCustom")


class ResourceHelper(UserGroupMembershipHelperCustom, UserGroupMembershipHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            user_id=dict(type="str"),
            group_id=dict(type="str"),
            user_group_membership_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="user_group_membership",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
