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
module: oci_key_management_vault_actions
short_description: Perform actions on a Vault resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Vault resource in Oracle Cloud Infrastructure
    - For I(action=cancel_vault_deletion), cancels the scheduled deletion of the specified vault. Canceling a scheduled deletion
      restores the vault and all keys in it to their respective states from before their
      scheduled deletion. All keys that were scheduled for deletion prior to vault
      deletion retain their lifecycle state and time of deletion.
      As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning write operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      write operations exceeds 10 requests per second for a given tenancy.
    - For I(action=schedule_vault_deletion), schedules the deletion of the specified vault. This sets the lifecycle state of the vault and all keys in it
      that are not already scheduled for deletion to `PENDING_DELETION` and then deletes them after the
      retention period ends. The lifecycle state and time of deletion for keys already scheduled for deletion won't
      change. If any keys in the vault are scheduled to be deleted after the specified time of
      deletion for the vault, the call is rejected with the error code 409.
      As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning write operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      write operations exceeds 10 requests per second for a given tenancy.
version_added: "2.9"
author: Oracle (@oracle)
options:
    vault_id:
        description:
            - The OCID of the vault.
        type: str
        aliases: ["id"]
        required: true
    time_of_deletion:
        description:
            - An optional property indicating when to delete the vault, expressed in
              L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format. The specified
              time must be between 7 and 30 days from the time when the request is received.
              If this property is missing, it will be set to 30 days from the time of the request
              by default.
            - Applicable only for I(action=schedule_vault_deletion).
        type: str
    action:
        description:
            - The action to perform on the Vault.
        type: str
        required: true
        choices:
            - "cancel_vault_deletion"
            - "schedule_vault_deletion"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cancel_vault_deletion on vault
  oci_key_management_vault_actions:
    vault_id: ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx
    action: cancel_vault_deletion

- name: Perform action schedule_vault_deletion on vault
  oci_key_management_vault_actions:
    time_of_deletion: 2018-04-03T21:10:29.600Z
    vault_id: ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx
    action: schedule_vault_deletion

"""

RETURN = """
vault:
    description:
        - Details of the Vault resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains this vault.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        crypto_endpoint:
            description:
                - The service endpoint to perform cryptographic operations against. Cryptographic operations include
                  L(Encrypt,https://docs.cloud.oracle.com/api/#/en/key/latest/EncryptedData/Encrypt),
                  L(Decrypt,https://docs.cloud.oracle.com/api/#/en/key/latest/DecryptedData/Decrypt),
                  and L(GenerateDataEncryptionKey,https://docs.cloud.oracle.com/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey) operations.
            returned: on success
            type: string
            sample: crypto_endpoint_example
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
                - A user-friendly name for the vault. It does not have to be unique, and it is changeable.
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
                - The OCID of the vault.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The vault's current lifecycle state.
                - "Example: `DELETED`"
            returned: on success
            type: string
            sample: DELETED
        management_endpoint:
            description:
                - "The service endpoint to perform management operations against. Management operations include \\"Create,\\" \\"Update,\\" \\"List,\\"
                  \\"Get,\\" and \\"Delete\\" operations."
            returned: on success
            type: string
            sample: management_endpoint_example
        time_created:
            description:
                - The date and time this vault was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                - "Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2018-04-03T21:10:29.600Z
        time_of_deletion:
            description:
                - "An optional property to indicate when to delete the vault, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2018-04-03T21:10:29.600Z
        vault_type:
            description:
                - The type of vault. Each type of vault stores the key with different
                  degrees of isolation and has different options and pricing.
            returned: on success
            type: string
            sample: VIRTUAL_PRIVATE
        wrappingkey_id:
            description:
                - The OCID of the vault's wrapping key.
            returned: on success
            type: string
            sample: ocid1.wrappingkey.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "crypto_endpoint": "crypto_endpoint_example",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "DELETED",
        "management_endpoint": "management_endpoint_example",
        "time_created": "2018-04-03T21:10:29.600Z",
        "time_of_deletion": "2018-04-03T21:10:29.600Z",
        "vault_type": "VIRTUAL_PRIVATE",
        "wrappingkey_id": "ocid1.wrappingkey.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.key_management import KmsVaultClient
    from oci.key_management.models import ScheduleVaultDeletionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VaultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_vault_deletion
        schedule_vault_deletion
    """

    @staticmethod
    def get_module_resource_id_param():
        return "vault_id"

    def get_module_resource_id(self):
        return self.module.params.get("vault_id")

    def get_get_fn(self):
        return self.client.get_vault

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vault, vault_id=self.module.params.get("vault_id"),
        )

    def cancel_vault_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_vault_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(vault_id=self.module.params.get("vault_id"),),
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

    def schedule_vault_deletion(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScheduleVaultDeletionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_vault_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                vault_id=self.module.params.get("vault_id"),
                schedule_vault_deletion_details=action_details,
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


VaultActionsHelperCustom = get_custom_class("VaultActionsHelperCustom")


class ResourceHelper(VaultActionsHelperCustom, VaultActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            vault_id=dict(aliases=["id"], type="str", required=True),
            time_of_deletion=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["cancel_vault_deletion", "schedule_vault_deletion"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="vault",
        service_client_class=KmsVaultClient,
        namespace="key_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
