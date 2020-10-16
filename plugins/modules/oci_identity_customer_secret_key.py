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
module: oci_identity_customer_secret_key
short_description: Manage a CustomerSecretKey resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CustomerSecretKey resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new secret key for the specified user. Secret keys are used for authentication with the Object Storage Service's Amazon S3
      compatible API. For information, see
      L(Managing User Credentials,https://docs.cloud.oracle.com/Content/Identity/Tasks/managingcredentials.htm).
    - "You must specify a *description* for the secret key (although it can be an empty string). It does not
      have to be unique, and you can change it anytime with
      L(UpdateCustomerSecretKey,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/CustomerSecretKeySummary/UpdateCustomerSecretKey)."
    - "Every user has permission to create a secret key for *their own user ID*. An administrator in your organization
      does not need to write a policy to give users this ability. To compare, administrators who have permission to the
      tenancy can use this operation to create a secret key for any user, including themselves."
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The name you assign to the secret key during creation. Does not have to be unique, and it's changeable.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
    customer_secret_key_id:
        description:
            - The OCID of the secret key.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the CustomerSecretKey.
            - Use I(state=present) to create or update a CustomerSecretKey.
            - Use I(state=absent) to delete a CustomerSecretKey.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create customer_secret_key
  oci_identity_customer_secret_key:
    display_name: display_name_example
    user_id: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx

- name: Update customer_secret_key using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_customer_secret_key:
    display_name: display_name_example
    user_id: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx

- name: Update customer_secret_key
  oci_identity_customer_secret_key:
    display_name: display_name_example
    user_id: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx
    customer_secret_key_id: ocid1.customersecretkey.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete customer_secret_key
  oci_identity_customer_secret_key:
    user_id: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx
    customer_secret_key_id: ocid1.customersecretkey.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete customer_secret_key using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_identity_customer_secret_key:
    display_name: display_name_example
    user_id: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
customer_secret_key:
    description:
        - Details of the CustomerSecretKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the secret key.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        user_id:
            description:
                - The OCID of the user the password belongs to.
            returned: on success
            type: string
            sample: ocid1.user.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The displayName you assign to the secret key. Does not have to be unique, and it's changeable.
            returned: on success
            type: string
            sample: display_name_example
        time_created:
            description:
                - Date and time the `CustomerSecretKey` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_expires:
            description:
                - Date and time when this password will expire, in the format defined by RFC3339.
                  Null if it never expires.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description:
                - The secret key's current state. After creating a secret key, make sure its `lifecycleState` changes from
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_expires": "2016-08-25T21:10:29.600Z",
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
    from oci.identity.models import CreateCustomerSecretKeyDetails
    from oci.identity.models import UpdateCustomerSecretKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CustomerSecretKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, list and delete"""

    def get_module_resource_id_param(self):
        return "customer_secret_key_id"

    def get_module_resource_id(self):
        return self.module.params.get("customer_secret_key_id")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.id:
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
        return oci_common_utils.list_all_resources(
            self.client.list_customer_secret_keys, **kwargs
        )

    def get_create_model_class(self):
        return CreateCustomerSecretKeyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_customer_secret_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_customer_secret_key_details=create_details,
                user_id=self.module.params.get("user_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateCustomerSecretKeyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_customer_secret_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                customer_secret_key_id=self.module.params.get("customer_secret_key_id"),
                update_customer_secret_key_details=update_details,
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
            call_fn=self.client.delete_customer_secret_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                customer_secret_key_id=self.module.params.get("customer_secret_key_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


CustomerSecretKeyHelperCustom = get_custom_class("CustomerSecretKeyHelperCustom")


class ResourceHelper(CustomerSecretKeyHelperCustom, CustomerSecretKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            user_id=dict(type="str", required=True),
            customer_secret_key_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="customer_secret_key",
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
