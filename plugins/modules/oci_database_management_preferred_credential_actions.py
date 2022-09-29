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
module: oci_database_management_preferred_credential_actions
short_description: Perform actions on a PreferredCredential resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a PreferredCredential resource in Oracle Cloud Infrastructure
    - For I(action=test), test the preferred credential.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    credential_name:
        description:
            - The name of the preferred credential.
        type: str
        required: true
    type:
        description:
            - The type of preferred credential.
        type: str
        choices:
            - "BASIC"
        required: true
    user_name:
        description:
            - The user to connect to the database.
        type: str
    role:
        description:
            - Role of the database user.
        type: str
        choices:
            - "NORMAL"
            - "SYSDBA"
    password_secret_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret.
        type: str
    action:
        description:
            - The action to perform on the PreferredCredential.
        type: str
        required: true
        choices:
            - "test"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action test on preferred_credential with type = BASIC
  oci_database_management_preferred_credential_actions:
    # required
    type: BASIC

    # optional
    user_name: user_name_example
    role: NORMAL
    password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
preferred_credential:
    description:
        - Details of the PreferredCredential resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        type:
            description:
                - Type of the preferred credential.
            returned: on success
            type: str
            sample: BASIC
        credential_name:
            description:
                - Name of the preferred credential.
            returned: on success
            type: str
            sample: credential_name_example
        status:
            description:
                - Status of the preferred credential.
            returned: on success
            type: str
            sample: SET
        is_accessible:
            description:
                - Is preferred credential accessible.
            returned: on success
            type: bool
            sample: true
        user_name:
            description:
                - The user to connect to the database.
            returned: on success
            type: str
            sample: user_name_example
        role:
            description:
                - Role of the database user.
            returned: on success
            type: str
            sample: NORMAL
        password_secret_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the secret.
            returned: on success
            type: str
            sample: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "type": "BASIC",
        "credential_name": "credential_name_example",
        "status": "SET",
        "is_accessible": true,
        "user_name": "user_name_example",
        "role": "NORMAL",
        "password_secret_id": "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import TestPreferredCredentialDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PreferredCredentialActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        test
    """

    @staticmethod
    def get_module_resource_id_param():
        return "credential_name"

    def get_module_resource_id(self):
        return self.module.params.get("credential_name")

    def get_get_fn(self):
        return self.client.get_preferred_credential

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_preferred_credential,
            managed_database_id=self.module.params.get("managed_database_id"),
            credential_name=self.module.params.get("credential_name"),
        )

    def test(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, TestPreferredCredentialDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.test_preferred_credential,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                credential_name=self.module.params.get("credential_name"),
                test_preferred_credential_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


PreferredCredentialActionsHelperCustom = get_custom_class(
    "PreferredCredentialActionsHelperCustom"
)


class ResourceHelper(
    PreferredCredentialActionsHelperCustom, PreferredCredentialActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            credential_name=dict(type="str", required=True),
            type=dict(type="str", required=True, choices=["BASIC"]),
            user_name=dict(type="str"),
            role=dict(type="str", choices=["NORMAL", "SYSDBA"]),
            password_secret_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["test"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="preferred_credential",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
