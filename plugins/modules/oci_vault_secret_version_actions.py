#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_vault_secret_version_actions
short_description: Perform actions on a SecretVersion resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SecretVersion resource in Oracle Cloud Infrastructure
    - For I(action=cancel_secret_version_deletion), cancels the scheduled deletion of a secret version.
    - For I(action=schedule_secret_version_deletion), schedules the deletion of the specified secret version. This deletes it after the specified retention
      period ends. You can only
      delete a secret version if the secret version rotation state is marked as `DEPRECATED`.
version_added: "2.9"
author: Oracle (@oracle)
options:
    secret_id:
        description:
            - The OCID of the secret.
        type: str
        required: true
    secret_version_number:
        description:
            - The version number of the secret.
        type: int
        required: true
    time_of_deletion:
        description:
            - "An optional property indicating when to delete the secret version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
              Example: `2019-04-03T21:10:29.600Z`"
            - Applicable only for I(action=schedule_secret_version_deletion).
        type: str
    action:
        description:
            - The action to perform on the SecretVersion.
        type: str
        required: true
        choices:
            - "cancel_secret_version_deletion"
            - "schedule_secret_version_deletion"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action cancel_secret_version_deletion on secret_version
  oci_vault_secret_version_actions:
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    secret_version_number: 789
    action: cancel_secret_version_deletion

- name: Perform action schedule_secret_version_deletion on secret_version
  oci_vault_secret_version_actions:
    time_of_deletion: "2018-04-03T21:10:29.600Z"
    secret_id: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
    secret_version_number: "789"
    action: "schedule_secret_version_deletion"

"""

RETURN = """
secret_version:
    description:
        - Details of the SecretVersion resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        content_type:
            description:
                - The content type of the secret version's secret contents.
            returned: on success
            type: string
            sample: BASE64
        name:
            description:
                - The name of the secret version. A name is unique across versions of a secret.
            returned: on success
            type: string
            sample: name_example
        secret_id:
            description:
                - The OCID of the secret.
            returned: on success
            type: string
            sample: "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx"
        stages:
            description:
                - A list of possible rotation states for the secret version. A secret version marked `CURRENT` is currently in use. A secret version
                  marked `PENDING` is staged and available for use, but has not been applied on the target system and, therefore, has not been rotated
                  into current, active use. The secret most recently uploaded to a vault is always marked `LATEST`. (The first version of a secret is
                  always marked as both `CURRENT` and `LATEST`.) A secret version marked `PREVIOUS` is the secret version that was most recently marked
                  `CURRENT`, before the last secret version rotation. A secret version marked `DEPRECATED` is neither current, pending, nor the previous
                  one in use. Only secret versions marked `DEPRECATED` can be scheduled for deletion.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - "A optional property indicating when the secret version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        time_of_deletion:
            description:
                - "An optional property indicating when to delete the secret version, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp
                  format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        time_of_current_version_expiry:
            description:
                - "An optional property indicating when the current secret version will expire, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                  Example: `2019-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-04-03T21:10:29.600Z
        version_number:
            description:
                - The version number of the secret.
            returned: on success
            type: int
            sample: 56
    sample: {
        "content_type": "BASE64",
        "name": "name_example",
        "secret_id": "ocid1.secret.oc1..xxxxxxEXAMPLExxxxxx",
        "stages": [],
        "time_created": "2019-04-03T21:10:29.600Z",
        "time_of_deletion": "2019-04-03T21:10:29.600Z",
        "time_of_current_version_expiry": "2019-04-03T21:10:29.600Z",
        "version_number": 56
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
    from oci.vault import VaultsClient
    from oci.vault.models import ScheduleSecretVersionDeletionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecretVersionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_secret_version_deletion
        schedule_secret_version_deletion
    """

    @staticmethod
    def get_module_resource_id_param():
        return "secret_version_number"

    def get_module_resource_id(self):
        return self.module.params.get("secret_version_number")

    def get_get_fn(self):
        return self.client.get_secret_version

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_secret_version,
            secret_id=self.module.params.get("secret_id"),
            secret_version_number=self.module.params.get("secret_version_number"),
        )

    def cancel_secret_version_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_secret_version_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                secret_id=self.module.params.get("secret_id"),
                secret_version_number=self.module.params.get("secret_version_number"),
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

    def schedule_secret_version_deletion(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ScheduleSecretVersionDeletionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_secret_version_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(
                secret_id=self.module.params.get("secret_id"),
                secret_version_number=self.module.params.get("secret_version_number"),
                schedule_secret_version_deletion_details=action_details,
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


SecretVersionActionsHelperCustom = get_custom_class("SecretVersionActionsHelperCustom")


class ResourceHelper(SecretVersionActionsHelperCustom, SecretVersionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            secret_id=dict(type="str", required=True),
            secret_version_number=dict(type="int", required=True),
            time_of_deletion=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_secret_version_deletion",
                    "schedule_secret_version_deletion",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="secret_version",
        service_client_class=VaultsClient,
        namespace="vault",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
