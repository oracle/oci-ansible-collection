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
module: oci_identity_authentication_policy
short_description: Manage an AuthenticationPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an AuthenticationPolicy resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        aliases: ["id"]
        required: true
    password_policy:
        description:
            - Password policy.
        type: dict
        suboptions:
            minimum_password_length:
                description:
                    - Minimum password length required.
                type: int
            is_uppercase_characters_required:
                description:
                    - At least one uppercase character required.
                type: bool
            is_lowercase_characters_required:
                description:
                    - At least one lower case character required.
                type: bool
            is_numeric_characters_required:
                description:
                    - At least one numeric character required.
                type: bool
            is_special_characters_required:
                description:
                    - At least one special character required.
                type: bool
            is_username_containment_allowed:
                description:
                    - User name is allowed to be part of the password.
                type: bool
    state:
        description:
            - The state of the AuthenticationPolicy.
            - Use I(state=present) to update an existing an AuthenticationPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update authentication_policy
  oci_identity_authentication_policy:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
authentication_policy:
    description:
        - Details of the AuthenticationPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        password_policy:
            description:
                - Password policy.
            returned: on success
            type: complex
            contains:
                minimum_password_length:
                    description:
                        - Minimum password length required.
                    returned: on success
                    type: int
                    sample: 56
                is_uppercase_characters_required:
                    description:
                        - At least one uppercase character required.
                    returned: on success
                    type: bool
                    sample: true
                is_lowercase_characters_required:
                    description:
                        - At least one lower case character required.
                    returned: on success
                    type: bool
                    sample: true
                is_numeric_characters_required:
                    description:
                        - At least one numeric character required.
                    returned: on success
                    type: bool
                    sample: true
                is_special_characters_required:
                    description:
                        - At least one special character required.
                    returned: on success
                    type: bool
                    sample: true
                is_username_containment_allowed:
                    description:
                        - User name is allowed to be part of the password.
                    returned: on success
                    type: bool
                    sample: true
        compartment_id:
            description:
                - Compartment OCID.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "password_policy": {
            "minimum_password_length": 56,
            "is_uppercase_characters_required": true,
            "is_lowercase_characters_required": true,
            "is_numeric_characters_required": true,
            "is_special_characters_required": true,
            "is_username_containment_allowed": true
        },
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.identity.models import UpdateAuthenticationPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AuthenticationPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def get_module_resource_id_param(self):
        return "compartment_id"

    def get_module_resource_id(self):
        return self.module.params.get("compartment_id")

    def get_get_fn(self):
        return self.client.get_authentication_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_authentication_policy,
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_update_model_class(self):
        return UpdateAuthenticationPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_authentication_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                update_authentication_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )


AuthenticationPolicyHelperCustom = get_custom_class("AuthenticationPolicyHelperCustom")


class ResourceHelper(AuthenticationPolicyHelperCustom, AuthenticationPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(aliases=["id"], type="str", required=True),
            password_policy=dict(
                type="dict",
                options=dict(
                    minimum_password_length=dict(type="int"),
                    is_uppercase_characters_required=dict(type="bool"),
                    is_lowercase_characters_required=dict(type="bool"),
                    is_numeric_characters_required=dict(type="bool"),
                    is_special_characters_required=dict(type="bool"),
                    is_username_containment_allowed=dict(type="bool"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="authentication_policy",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
