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
module: oci_key_management_key_actions
short_description: Perform actions on a Key resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Key resource in Oracle Cloud Infrastructure
    - For I(action=cancel_key_deletion), cancels the scheduled deletion of the specified key. Canceling
      a scheduled deletion restores the key's lifecycle state to what
      it was before its scheduled deletion.
      As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning write operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      write operations exceeds 10 requests per second for a given tenancy.
    - For I(action=disable), disables a master encryption key so it can no longer be used for encryption, decryption, or
      generating new data encryption keys.
      As a management operation, this call is subject to a Key Management limit that applies to the total number
      of requests across all management write operations. Key Management might throttle this call to reject an
      otherwise valid request when the total rate of management write operations exceeds 10 requests per second
      for a given tenancy.
    - For I(action=enable), enables a master encryption key so it can be used for encryption, decryption, or
      generating new data encryption keys.
      As a management operation, this call is subject to a Key Management limit that applies to the total number
      of requests across all management write operations. Key Management might throttle this call to reject an
      otherwise valid request when the total rate of management write operations exceeds 10 requests per second
      for a given tenancy.
    - For I(action=schedule_key_deletion), schedules the deletion of the specified key. This sets the lifecycle state of the key
      to `PENDING_DELETION` and then deletes it after the specified retention period ends.
      As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning write operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      write operations exceeds 10 requests per second for a given tenancy.
version_added: "2.9"
author: Oracle (@oracle)
options:
    key_id:
        description:
            - The OCID of the key.
        type: str
        aliases: ["id"]
        required: true
    time_of_deletion:
        description:
            - An optional property to indicate when to delete the vault, expressed in
              L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format. The specified
              time must be between 7 and 30 days from when the request is received.
              If this property is missing, it will be set to 30 days from the time of the request
              by default.
            - Applicable only for I(action=schedule_key_deletion).
        type: str
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Key.
        type: str
        required: true
        choices:
            - "cancel_key_deletion"
            - "disable"
            - "enable"
            - "schedule_key_deletion"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cancel_key_deletion on key
  oci_key_management_key_actions:
    key_id: ocid1.key.oc1..xxxxxxEXAMPLExxxxxx
    action: cancel_key_deletion
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

- name: Perform action disable on key
  oci_key_management_key_actions:
    key_id: ocid1.key.oc1..xxxxxxEXAMPLExxxxxx
    action: disable
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

- name: Perform action enable on key
  oci_key_management_key_actions:
    key_id: ocid1.key.oc1..xxxxxxEXAMPLExxxxxx
    action: enable
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

- name: Perform action schedule_key_deletion on key
  oci_key_management_key_actions:
    time_of_deletion: 2018-04-03T21:10:29.600Z
    key_id: ocid1.key.oc1..xxxxxxEXAMPLExxxxxx
    action: schedule_key_deletion
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
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.key_management import KmsManagementClient
    from oci.key_management.models import ScheduleKeyDeletionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KeyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_key_deletion
        disable
        enable
        schedule_key_deletion
    """

    @staticmethod
    def get_module_resource_id_param():
        return "key_id"

    def get_module_resource_id(self):
        return self.module.params.get("key_id")

    def get_get_fn(self):
        return self.client.get_key

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_key, key_id=self.module.params.get("key_id"),
        )

    def cancel_key_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_key_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(key_id=self.module.params.get("key_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def disable(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_key,
            call_fn_args=(),
            call_fn_kwargs=dict(key_id=self.module.params.get("key_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def enable(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_key,
            call_fn_args=(),
            call_fn_kwargs=dict(key_id=self.module.params.get("key_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def schedule_key_deletion(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScheduleKeyDeletionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_key_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                key_id=self.module.params.get("key_id"),
                schedule_key_deletion_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


KeyActionsHelperCustom = get_custom_class("KeyActionsHelperCustom")


class ResourceHelper(KeyActionsHelperCustom, KeyActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            key_id=dict(aliases=["id"], type="str", required=True),
            time_of_deletion=dict(type="str"),
            service_endpoint=dict(type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_key_deletion",
                    "disable",
                    "enable",
                    "schedule_key_deletion",
                ],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
