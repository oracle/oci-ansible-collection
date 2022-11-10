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
module: oci_key_management_key_version_actions
short_description: Perform actions on a KeyVersion resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a KeyVersion resource in Oracle Cloud Infrastructure
    - For I(action=cancel_key_version_deletion), cancels the scheduled deletion of the specified key version. Canceling
      a scheduled deletion restores the key version to its lifecycle state from
      before its scheduled deletion.
      As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning write operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      write operations exceeds 10 requests per second for a given tenancy.
    - For I(action=schedule_key_version_deletion), schedules the deletion of the specified key version. This sets the lifecycle state of the key version
      to `PENDING_DELETION` and then deletes it after the specified retention period ends.
      As a provisioning operation, this call is subject to a Key Management limit that applies to
      the total number of requests across all provisioning write operations. Key Management might
      throttle this call to reject an otherwise valid request when the total rate of provisioning
      write operations exceeds 10 requests per second for a given tenancy.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    key_id:
        description:
            - The OCID of the key.
        type: str
        required: true
    key_version_id:
        description:
            - The OCID of the key version.
        type: str
        aliases: ["id"]
        required: true
    time_of_deletion:
        description:
            - An optional property to indicate when to delete the key version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
              timestamp format. The specified time must be between 7 and 30 days from the time
              when the request is received. If this property is missing, it will be set to 30 days from the time of the request by default.
            - Applicable only for I(action=schedule_key_version_deletion).
        type: str
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
    action:
        description:
            - The action to perform on the KeyVersion.
        type: str
        required: true
        choices:
            - "cancel_key_version_deletion"
            - "schedule_key_version_deletion"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cancel_key_version_deletion on key_version
  oci_key_management_key_version_actions:
    # required
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    key_version_id: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel_key_version_deletion
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

- name: Perform action schedule_key_version_deletion on key_version
  oci_key_management_key_version_actions:
    # required
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    key_version_id: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
    action: schedule_key_version_deletion

    # optional
    time_of_deletion: time_of_deletion_example
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
key_version:
    description:
        - Details of the KeyVersion resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains this key version.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The OCID of the key version.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        key_id:
            description:
                - The OCID of the key associated with this key version.
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        public_key:
            description:
                - The public key in PEM format. (This value pertains only to RSA and ECDSA keys.)
            returned: on success
            type: str
            sample: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
        lifecycle_state:
            description:
                - The key version's current lifecycle state.
                - "Example: `ENABLED`"
            returned: on success
            type: str
            sample: CREATING
        origin:
            description:
                - The source of the key material. When this value is `INTERNAL`, Key Management
                  created the key material. When this value is `EXTERNAL`, the key material
                  was imported from an external source.
            returned: on success
            type: str
            sample: INTERNAL
        time_created:
            description:
                - The date and time this key version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                - "Example: \\"2018-04-03T21:10:29.600Z\\""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the key version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vault_id:
            description:
                - The OCID of the vault that contains this key version.
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        replica_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                replication_id:
                    description:
                        - ReplicationId associated with a key version operation
                    returned: on success
                    type: str
                    sample: "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        is_primary:
            description:
                - ""
            returned: on success
            type: bool
            sample: true
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz...",
        "lifecycle_state": "CREATING",
        "origin": "INTERNAL",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "replica_details": {
            "replication_id": "ocid1.replication.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_primary": true
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.key_management import KmsManagementClient
    from oci.key_management.models import ScheduleKeyVersionDeletionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class KeyVersionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_key_version_deletion
        schedule_key_version_deletion
    """

    @staticmethod
    def get_module_resource_id_param():
        return "key_version_id"

    def get_module_resource_id(self):
        return self.module.params.get("key_version_id")

    def get_get_fn(self):
        return self.client.get_key_version

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_key_version,
            key_id=self.module.params.get("key_id"),
            key_version_id=self.module.params.get("key_version_id"),
        )

    def cancel_key_version_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_key_version_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                key_id=self.module.params.get("key_id"),
                key_version_id=self.module.params.get("key_version_id"),
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

    def schedule_key_version_deletion(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScheduleKeyVersionDeletionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_key_version_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                key_id=self.module.params.get("key_id"),
                key_version_id=self.module.params.get("key_version_id"),
                schedule_key_version_deletion_details=action_details,
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


KeyVersionActionsHelperCustom = get_custom_class("KeyVersionActionsHelperCustom")


class ResourceHelper(KeyVersionActionsHelperCustom, KeyVersionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            key_id=dict(type="str", required=True),
            key_version_id=dict(aliases=["id"], type="str", required=True),
            time_of_deletion=dict(type="str"),
            service_endpoint=dict(type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_key_version_deletion",
                    "schedule_key_version_deletion",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="key_version",
        service_client_class=KmsManagementClient,
        namespace="key_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
