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
module: oci_key_management_key
short_description: Manage a Key resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a Key resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new master encryption key.
    - As a management operation, this call is subject to a Key Management limit that applies to the total
      number of requests across all management write operations. Key Management might throttle this call
      to reject an otherwise valid request when the total rate of management write operations exceeds 10
      requests per second for a given tenancy.
    - "This resource has the following action operations in the M(oci_key_actions) module: cancel_key_deletion, disable, enable, schedule_key_deletion."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where you want to create the master encryption key.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name for the key. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    key_shape:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            algorithm:
                description:
                    - The algorithm used by a key's key versions to encrypt or decrypt.
                type: str
                choices:
                    - "AES"
                    - "RSA"
                required: true
            length:
                description:
                    - The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.
                type: int
                required: true
    protection_mode:
        description:
            - The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
              A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed inside
              the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
              on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
              a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.
        type: str
        choices:
            - "HSM"
            - "SOFTWARE"
    key_id:
        description:
            - The OCID of the key.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
    state:
        description:
            - The state of the Key.
            - Use I(state=present) to create or update a Key.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create key
  oci_key_management_key:
    compartment_id: ocid1.tenancy.oc1..exampleati4wjo6cvbxq4iusld5lsdneskcfy7lr4a6wfauxuwrwed5b3xea
    display_name: Key C
    key_shape:
      algorithm: AES
      length: 16
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

- name: Update key using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_key_management_key:
    display_name: Key CC
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

- name: Update key
  oci_key_management_key:
    key_id: ocid1.key.oc1..xxxxxxEXAMPLExxxxxx
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
key:
    description:
        - Details of the Key resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains this master encryption key.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        current_key_version:
            description:
                - The OCID of the key version used in cryptographic operations. During key rotation, the service might be
                  in a transitional state where this or a newer key version are used intermittently. The `currentKeyVersion`
                  property is updated when the service is guaranteed to use the new key version for all subsequent encryption operations.
            returned: on success
            type: string
            sample: current_key_version_example
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name for the key. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of the key.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        key_shape:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                algorithm:
                    description:
                        - The algorithm used by a key's key versions to encrypt or decrypt.
                    returned: on success
                    type: string
                    sample: AES
                length:
                    description:
                        - The length of the key, expressed as an integer. Values of 16, 24, or 32 are supported.
                    returned: on success
                    type: int
                    sample: 56
        protection_mode:
            description:
                - The key's protection mode indicates how the key persists and where cryptographic operations that use the key are performed.
                  A protection mode of `HSM` means that the key persists on a hardware security module (HSM) and all cryptographic operations are performed
                  inside
                  the HSM. A protection mode of `SOFTWARE` means that the key persists on the server, protected by the vault's RSA wrapping key which persists
                  on the HSM. All cryptographic operations that use a key with a protection mode of `SOFTWARE` are performed on the server. By default,
                  a key's protection mode is set to `HSM`. You can't change a key's protection mode after the key is created or imported.
            returned: on success
            type: string
            sample: HSM
        lifecycle_state:
            description:
                - The key's current lifecycle state.
                - "Example: `ENABLED`"
            returned: on success
            type: string
            sample: ENABLED
        time_created:
            description:
                - The date and time the key was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                - "Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2018-04-03T21:10:29.600Z
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the key, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        vault_id:
            description:
                - The OCID of the vault that contains this key.
            returned: on success
            type: string
            sample: ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "current_key_version": "current_key_version_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "key_shape": {
            "algorithm": "AES",
            "length": 56
        },
        "protection_mode": "HSM",
        "lifecycle_state": "ENABLED",
        "time_created": "2018-04-03T21:10:29.600Z",
        "time_of_deletion": "2019-04-03T21:10:29.600Z",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.key_management import KmsManagementClient
    from oci.key_management.models import CreateKeyDetails
    from oci.key_management.models import UpdateKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KeyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_module_resource_id_param(self):
        return "key_id"

    def get_module_resource_id(self):
        return self.module.params.get("key_id")

    def get_get_fn(self):
        return self.client.get_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_key, key_id=self.module.params.get("key_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["protection_mode"]

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
        return oci_common_utils.list_all_resources(self.client.list_keys, **kwargs)

    def get_create_model_class(self):
        return CreateKeyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_key,
            call_fn_args=(),
            call_fn_kwargs=dict(create_key_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateKeyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_key,
            call_fn_args=(),
            call_fn_kwargs=dict(
                key_id=self.module.params.get("key_id"),
                update_key_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


KeyHelperCustom = get_custom_class("KeyHelperCustom")


class ResourceHelper(KeyHelperCustom, KeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            key_shape=dict(
                type="dict",
                options=dict(
                    algorithm=dict(type="str", required=True, choices=["AES", "RSA"]),
                    length=dict(type="int", required=True),
                ),
            ),
            protection_mode=dict(type="str", choices=["HSM", "SOFTWARE"]),
            key_id=dict(aliases=["id"], type="str"),
            service_endpoint=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="key",
        service_client_class=KmsManagementClient,
        namespace="key_management",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
