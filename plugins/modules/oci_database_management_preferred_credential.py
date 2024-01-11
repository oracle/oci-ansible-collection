#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_management_preferred_credential
short_description: Manage a PreferredCredential resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a PreferredCredential resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_database_management_preferred_credential_actions) module: test."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    type:
        description:
            - The type of preferred credential.
            - Required for update using I(state=present) with credential_name present.
        type: str
        choices:
            - "BASIC"
    user_name:
        description:
            - The user name used to connect to the database.
            - This parameter is updatable.
        type: str
    role:
        description:
            - The role of the database user.
            - This parameter is updatable.
        type: str
        choices:
            - "NORMAL"
            - "SYSDBA"
    password_secret_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Vault service secret that contains the database user
              password.
            - This parameter is updatable.
        type: str
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
    state:
        description:
            - The state of the PreferredCredential.
            - Use I(state=present) to update an existing a PreferredCredential.
            - Use I(state=absent) to delete a PreferredCredential.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update preferred_credential with type = BASIC
  oci_database_management_preferred_credential:
    # required
    type: BASIC

    # optional
    user_name: user_name_example
    role: NORMAL
    password_secret_id: "ocid1.passwordsecret.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete preferred_credential
  oci_database_management_preferred_credential:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    credential_name: credential_name_example
    state: absent

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
                - The type of preferred credential. Only 'BASIC' is supported currently.
            returned: on success
            type: str
            sample: BASIC
        credential_name:
            description:
                - The name of the preferred credential.
            returned: on success
            type: str
            sample: credential_name_example
        status:
            description:
                - The status of the preferred credential.
            returned: on success
            type: str
            sample: SET
        is_accessible:
            description:
                - Indicates whether the preferred credential is accessible.
            returned: on success
            type: bool
            sample: true
        user_name:
            description:
                - The user name used to connect to the database.
            returned: on success
            type: str
            sample: user_name_example
        role:
            description:
                - The role of the database user.
            returned: on success
            type: str
            sample: NORMAL
        password_secret_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Vault service secret that contains the database user
                  password.
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

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import UpdatePreferredCredentialDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PreferredCredentialHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(PreferredCredentialHelperGen, self).get_possible_entity_types() + [
            "preferredcredential",
            "preferredcredentials",
            "databaseManagementpreferredcredential",
            "databaseManagementpreferredcredentials",
            "preferredcredentialresource",
            "preferredcredentialsresource",
            "databasemanagement",
        ]

    def get_module_resource_id_param(self):
        return "credential_name"

    def get_module_resource_id(self):
        return self.module.params.get("credential_name")

    def get_get_fn(self):
        return self.client.get_preferred_credential

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_preferred_credential,
            credential_name=summary_model.credential_name,
            managed_database_id=self.module.params.get("managed_database_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_preferred_credential,
            managed_database_id=self.module.params.get("managed_database_id"),
            credential_name=self.module.params.get("credential_name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "managed_database_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_preferred_credentials, **kwargs
        )

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def get_update_model_class(self):
        return UpdatePreferredCredentialDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_preferred_credential,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                credential_name=self.module.params.get("credential_name"),
                update_preferred_credential_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_preferred_credential,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                credential_name=self.module.params.get("credential_name"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


PreferredCredentialHelperCustom = get_custom_class("PreferredCredentialHelperCustom")


class ResourceHelper(PreferredCredentialHelperCustom, PreferredCredentialHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            type=dict(type="str", choices=["BASIC"]),
            user_name=dict(type="str"),
            role=dict(type="str", choices=["NORMAL", "SYSDBA"]),
            password_secret_id=dict(type="str"),
            managed_database_id=dict(type="str", required=True),
            credential_name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="preferred_credential",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
