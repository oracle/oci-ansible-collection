#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_identity_user_state
short_description: Manage an UserState resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an UserState resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
        type: str
        aliases: ["id"]
        required: true
    blocked:
        description:
            - "Update state to blocked or unblocked. Only \\"false\\" is supported (for changing the state to unblocked)."
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the UserState.
            - Use I(state=present) to update an existing an UserState.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update user_state
  oci_identity_user_state:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    blocked: true

"""

RETURN = """
user:
    description:
        - Details of the UserState resource acted upon by the current operation
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
        db_user_name:
            description:
                - DB username of the DB credential. Has to be unique across the tenancy.
            returned: on success
            type: str
            sample: db_user_name_example
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
            sample: "2013-10-20T19:20:30+01:00"
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
                    sample: true
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
                can_use_db_credentials:
                    description:
                        - Indicates if the user can use DB passwords.
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
        "db_user_name": "db_user_name_example",
        "identity_provider_id": "ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx",
        "external_identifier": "external_identifier_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "capabilities": {
            "can_use_console_password": true,
            "can_use_api_keys": true,
            "can_use_auth_tokens": true,
            "can_use_smtp_credentials": true,
            "can_use_db_credentials": true,
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
    from oci.identity.models import UpdateStateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UserStateHelperGen(OCIResourceHelperBase):
    """Supported operations: update"""

    def get_possible_entity_types(self):
        return super(UserStateHelperGen, self).get_possible_entity_types() + [
            "userstate",
            "userstates",
            "identityuserstate",
            "identityuserstates",
            "userstateresource",
            "userstatesresource",
            "state",
            "states",
            "identitystate",
            "identitystates",
            "stateresource",
            "statesresource",
            "identity",
        ]

    def get_module_resource_id_param(self):
        return "user_id"

    def get_module_resource_id(self):
        return self.module.params.get("user_id")

    def get_response_field_name(self):
        return "user"

    def get_update_model_class(self):
        return UpdateStateDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_user_state,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                update_state_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


UserStateHelperCustom = get_custom_class("UserStateHelperCustom")


class ResourceHelper(UserStateHelperCustom, UserStateHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            user_id=dict(aliases=["id"], type="str", required=True),
            blocked=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="user_state",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
