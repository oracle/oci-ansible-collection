#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_identity_user
short_description: Manage an User resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an User resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new user in your tenancy. For conceptual information about users, your tenancy, and other
      IAM Service components, see L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
    - You must specify your tenancy's OCID as the compartment ID in the request object (remember that the
      tenancy is simply the root compartment). Notice that IAM resources (users, groups, compartments, and
      some policies) reside within the tenancy itself, unlike cloud resources such as compute instances,
      which typically reside within compartments inside the tenancy. For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "You must also specify a *name* for the user, which must be unique across all users in your tenancy
      and cannot be changed. Allowed characters: No spaces. Only letters, numerals, hyphens, periods,
      underscores, +, and @. If you specify a name that's already in use, you'll get a 409 error.
      This name will be the user's login to the Console. You might want to pick a
      name that your company's own identity system (e.g., Active Directory, LDAP, etc.) already uses.
      If you delete a user and then create a new user with the same name, they'll be considered different
      users because they have different OCIDs."
    - "You must also specify a *description* for the user (although it can be an empty string).
      It does not have to be unique, and you can change it anytime with
      L(UpdateUser,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/User/UpdateUser). You can use the field to provide the user's
      full name, a description, a nickname, or other information to generally identify the user."
    - After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before
      using the object, first make sure its `lifecycleState` has changed to ACTIVE.
    - A new user has no permissions until you place the user in one or more groups (see
      L(AddUserToGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/UserGroupMembership/AddUserToGroup)). If the user needs to
      access the Console, you need to provide the user a password (see
      L(CreateOrResetUIPassword,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/UIPassword/CreateOrResetUIPassword)).
      If the user needs to access the Oracle Cloud Infrastructure REST API, you need to upload a
      public API signing key for that user (see
      L(Required Keys and OCIDs,https://docs.cloud.oracle.com/Content/API/Concepts/apisigningkey.htm) and also
      L(UploadApiKey,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/ApiKey/UploadApiKey)).
    - "**Important:** Make sure to inform the new user which compartment(s) they have access to."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy containing the user.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    name:
        description:
            - The name you assign to the user during creation. This is the user's login for the Console.
              The name must be unique across all users in the tenancy and cannot be changed.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The description you assign to the user during creation. Does not have to be unique, and it's changeable.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    email:
        description:
            - The email you assign to the user. Has to be unique across the tenancy.
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
    user_id:
        description:
            - The OCID of the user.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the User.
            - Use I(state=present) to create or update an User.
            - Use I(state=absent) to delete an User.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create user
  oci_identity_user:
    # required
    compartment_id: "ocid1.tenancy.oc1..aaaaaaaaba3pv6exampleuniqueID"
    name: JohnSmith@example.com
    description: John Smith

    # optional
    email: email_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update user
  oci_identity_user:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: John Smith
    email: email_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update user using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_user:
    # required
    compartment_id: "ocid1.tenancy.oc1..aaaaaaaaba3pv6exampleuniqueID"
    name: JohnSmith@example.com

    # optional
    description: John Smith
    email: email_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete user
  oci_identity_user:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete user using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_user:
    # required
    compartment_id: "ocid1.tenancy.oc1..aaaaaaaaba3pv6exampleuniqueID"
    name: JohnSmith@example.com
    state: absent

"""

RETURN = """
user:
    description:
        - Details of the User resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the user.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the tenancy containing the user.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name you assign to the user during creation. This is the user's login for the Console.
                  The name must be unique across all users in the tenancy and cannot be changed.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The description you assign to the user. Does not have to be unique, and it's changeable.
            returned: on success
            type: str
            sample: description_example
        email:
            description:
                - The email address you assign to the user.
                  The email address must be unique across all users in the tenancy.
            returned: on success
            type: str
            sample: email_example
        email_verified:
            description:
                - Whether the email address has been validated.
            returned: on success
            type: bool
            sample: true
        identity_provider_id:
            description:
                - The OCID of the `IdentityProvider` this user belongs to.
            returned: on success
            type: str
            sample: "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx"
        external_identifier:
            description:
                - Identifier of the user in the identity provider
            returned: on success
            type: str
            sample: external_identifier_example
        time_created:
            description:
                - Date and time the user was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        lifecycle_state:
            description:
                - The user's current state. After creating a user, make sure its `lifecycleState` changes from CREATING to
                  ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - "Returned only if the user's `lifecycleState` is INACTIVE. A 16-bit value showing the reason why the user
                  is inactive:"
                - "- bit 0: SUSPENDED (reserved for future use)
                  - bit 1: DISABLED (reserved for future use)
                  - bit 2: BLOCKED (the user has exceeded the maximum number of failed login attempts for the Console)"
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
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
        capabilities:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                can_use_console_password:
                    description:
                        - Indicates if the user can log in to the console.
                    returned: on success
                    type: bool
                    sample: example-password
                can_use_api_keys:
                    description:
                        - Indicates if the user can use API keys.
                    returned: on success
                    type: bool
                    sample: true
                can_use_auth_tokens:
                    description:
                        - Indicates if the user can use SWIFT passwords / auth tokens.
                    returned: on success
                    type: bool
                    sample: true
                can_use_smtp_credentials:
                    description:
                        - Indicates if the user can use SMTP passwords.
                    returned: on success
                    type: bool
                    sample: true
                can_use_customer_secret_keys:
                    description:
                        - Indicates if the user can use SigV4 symmetric keys.
                    returned: on success
                    type: bool
                    sample: true
        is_mfa_activated:
            description:
                - Flag indicates if MFA has been activated for the user.
            returned: on success
            type: bool
            sample: true
        last_successful_login_time:
            description:
                - The date and time of when the user most recently logged in the
                  format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`).
                  If there is no login history, this field is null.
                - For illustrative purposes, suppose we have a user who has logged in
                  at July 1st, 2020 at 1200 PST and logged out 30 minutes later.
                  They then login again on July 2nd, 2020 at 1500 PST.
                - Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`.
                - Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        previous_successful_login_time:
            description:
                - The date and time of when the user most recently logged in the
                  format defined by RFC3339 (ex. `2016-08-25T21:10:29.600Z`).
                  If there is no login history, this field is null.
                - For illustrative purposes, suppose we have a user who has logged in
                  at July 1st, 2020 at 1200 PST and logged out 30 minutes later.
                  They then login again on July 2nd, 2020 at 1500 PST.
                - Their previousSuccessfulLoginTime would be `2020-07-01:19:00.000Z`.
                - Their lastSuccessfulLoginTime would be `2020-07-02:22:00.000Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "email": "email_example",
        "email_verified": true,
        "identity_provider_id": "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx",
        "external_identifier": "external_identifier_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "capabilities": {
            "can_use_console_password": example-password,
            "can_use_api_keys": true,
            "can_use_auth_tokens": true,
            "can_use_smtp_credentials": true,
            "can_use_customer_secret_keys": true
        },
        "is_mfa_activated": true,
        "last_successful_login_time": "2013-10-20T19:20:30+01:00",
        "previous_successful_login_time": "2013-10-20T19:20:30+01:00"
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
    from oci.identity.models import CreateUserDetails
    from oci.identity.models import UpdateUserDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UserHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "user_id"

    def get_module_resource_id(self):
        return self.module.params.get("user_id")

    def get_get_fn(self):
        return self.client.get_user

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user, user_id=self.module.params.get("user_id"),
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
        return oci_common_utils.list_all_resources(self.client.list_users, **kwargs)

    def get_create_model_class(self):
        return CreateUserDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_user,
            call_fn_args=(),
            call_fn_kwargs=dict(create_user_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateUserDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_user,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                update_user_details=update_details,
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
            call_fn=self.client.delete_user,
            call_fn_args=(),
            call_fn_kwargs=dict(user_id=self.module.params.get("user_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


UserHelperCustom = get_custom_class("UserHelperCustom")


class ResourceHelper(UserHelperCustom, UserHelperGen):
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
            email=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            user_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="user",
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
