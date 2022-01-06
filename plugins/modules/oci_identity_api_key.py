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
module: oci_identity_api_key
short_description: Manage an ApiKey resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an ApiKey resource in Oracle Cloud Infrastructure
    - For I(state=present), uploads an API signing key for the specified user.
    - "Every user has permission to use this operation to upload a key for *their own user ID*. An
      administrator in your organization does not need to write a policy to give users this ability.
      To compare, administrators who have permission to the tenancy can use this operation to upload a
      key for any user, including themselves."
    - "**Important:** Even though you have permission to upload an API key, you might not yet
      have permission to do much else. If you try calling an operation unrelated to your own credential
      management (e.g., `ListUsers`, `LaunchInstance`) and receive an \\"unauthorized\\" error,
      check with an administrator to confirm which IAM Service group(s) you're in and what access
      you have. Also confirm you're working in the correct compartment."
    - After you send your request, the new object's `lifecycleState` will temporarily be CREATING. Before using
      the object, first make sure its `lifecycleState` has changed to ACTIVE.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
    key:
        description:
            - The public key.  Must be an RSA key in PEM format.
            - Required for create using I(state=present).
        type: str
    fingerprint:
        description:
            - The key's fingerprint.
            - Required for delete using I(state=absent).
        type: str
    state:
        description:
            - The state of the ApiKey.
            - Use I(state=present) to create an ApiKey.
            - Use I(state=absent) to delete an ApiKey.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create api_key
  oci_identity_api_key:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    key: key_example

- name: Delete api_key
  oci_identity_api_key:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    fingerprint: fingerprint_example
    state: absent

"""

RETURN = """
api_key:
    description:
        - Details of the ApiKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key_id:
            description:
                - "An Oracle-assigned identifier for the key, in this format:
                  TENANCY_OCID/USER_OCID/KEY_FINGERPRINT."
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        key_value:
            description:
                - The key's value.
            returned: on success
            type: str
            sample: key_value_example
        fingerprint:
            description:
                - The key's fingerprint (e.g., 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef).
            returned: on success
            type: str
            sample: fingerprint_example
        user_id:
            description:
                - The OCID of the user the key belongs to.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the `ApiKey` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The API key's current state. After creating an `ApiKey` object, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
    sample: {
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "key_value": "key_value_example",
        "fingerprint": "fingerprint_example",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
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
    from oci.identity.models import CreateApiKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApiKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, list and delete"""

    def get_module_resource_id_param(self):
        return "fingerprint"

    def get_module_resource_id(self):
        return self.module.params.get("fingerprint")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.fingerprint:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "user_id",
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
        return oci_common_utils.list_all_resources(self.client.list_api_keys, **kwargs)

    def get_create_model_class(self):
        return CreateApiKeyDetails

    def get_exclude_attributes(self):
        return ["key"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.upload_api_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                create_api_key_details=create_details,
            ),
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
            call_fn=self.client.delete_api_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                fingerprint=self.module.params.get("fingerprint"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ApiKeyHelperCustom = get_custom_class("ApiKeyHelperCustom")


class ResourceHelper(ApiKeyHelperCustom, ApiKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            key=dict(type="str", no_log=True),
            fingerprint=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="api_key",
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
