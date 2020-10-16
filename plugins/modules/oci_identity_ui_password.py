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
module: oci_identity_ui_password
short_description: Manage an UiPassword resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create an UiPassword resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Console one-time password for the specified user. For more information about user
      credentials, see L(User Credentials,https://docs.cloud.oracle.com/Content/Identity/Concepts/usercredentials.htm).
    - Use this operation after creating a new user, or if a user forgets their password. The new one-time
      password is returned to you in the response, and you must securely deliver it to the user. They'll
      be prompted to change this password the next time they sign in to the Console. If they don't change
      it within 7 days, the password will expire and you'll need to create a new one-time password for the
      user.
    - "**Note:** The user's Console login is the unique name you specified when you created the user
      (see L(CreateUser,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/User/CreateUser))."
version_added: "2.9"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
    state:
        description:
            - The state of the UiPassword.
            - Use I(state=present) to create an UiPassword.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create ui_password
  oci_identity_ui_password:
    user_id: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
ui_password:
    description:
        - Details of the UiPassword resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        password:
            description:
                - The user's password for the Console.
            returned: on success
            type: string
            sample: password_example
        user_id:
            description:
                - The OCID of the user.
            returned: on success
            type: string
            sample: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - Date and time the password was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The password's current state. After creating a password, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
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
        "password": "password_example",
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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UiPasswordHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def create_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_or_reset_ui_password,
            call_fn_args=(),
            call_fn_kwargs=dict(user_id=self.module.params.get("user_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


UiPasswordHelperCustom = get_custom_class("UiPasswordHelperCustom")


class ResourceHelper(UiPasswordHelperCustom, UiPasswordHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ui_password",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
