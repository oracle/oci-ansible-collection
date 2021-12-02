#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_identity_mfa_totp_device_actions
short_description: Perform actions on a MfaTotpDevice resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MfaTotpDevice resource in Oracle Cloud Infrastructure
    - For I(action=activate), activates the specified MFA TOTP device for the user. Activation requires manual interaction with the Console.
    - For I(action=generate_totp_seed), generate seed for the MFA TOTP device.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
    mfa_totp_device_id:
        description:
            - The OCID of the MFA TOTP device.
        type: str
        aliases: ["id"]
        required: true
    totp_token:
        description:
            - The Totp token for MFA.
            - Applicable only for I(action=activate).
        type: str
    action:
        description:
            - The action to perform on the MfaTotpDevice.
        type: str
        required: true
        choices:
            - "activate"
            - "generate_totp_seed"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on mfa_totp_device
  oci_identity_mfa_totp_device_actions:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    mfa_totp_device_id: "ocid1.mfatotpdevice.oc1..xxxxxxEXAMPLExxxxxx"
    action: activate

    # optional
    totp_token: totp_token_example

- name: Perform action generate_totp_seed on mfa_totp_device
  oci_identity_mfa_totp_device_actions:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    mfa_totp_device_id: "ocid1.mfatotpdevice.oc1..xxxxxxEXAMPLExxxxxx"
    action: generate_totp_seed

"""

RETURN = """
mfa_totp_device:
    description:
        - Details of the MfaTotpDevice resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the MFA TOTP Device.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The OCID of the user the MFA TOTP device belongs to.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Date and time the `MfaTotpDevice` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        time_expires:
            description:
                - Date and time when this MFA TOTP device will expire, in the format defined by RFC3339.
                  Null if it never expires.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        lifecycle_state:
            description:
                - The MFA TOTP device's current state.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - "The detailed status of INACTIVE lifecycleState.
                  Allowed values are:
                   - 1 - SUSPENDED
                   - 2 - DISABLED
                   - 4 - BLOCKED
                   - 8 - LOCKED"
            returned: on success
            type: int
            sample: 56
        is_activated:
            description:
                - Flag to indicate if the MFA TOTP device has been activated
            returned: on success
            type: bool
            sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_expires": "2016-08-25T21:10:29.600Z",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "is_activated": true
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
    from oci.identity import IdentityClient
    from oci.identity.models import MfaTotpToken

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MfaTotpDeviceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
        generate_totp_seed
    """

    @staticmethod
    def get_module_resource_id_param():
        return "mfa_totp_device_id"

    def get_module_resource_id(self):
        return self.module.params.get("mfa_totp_device_id")

    def get_get_fn(self):
        return self.client.get_mfa_totp_device

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_mfa_totp_device,
            user_id=self.module.params.get("user_id"),
            mfa_totp_device_id=self.module.params.get("mfa_totp_device_id"),
        )

    def activate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, MfaTotpToken
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_mfa_totp_device,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                mfa_totp_device_id=self.module.params.get("mfa_totp_device_id"),
                mfa_totp_token=action_details,
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

    def generate_totp_seed(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_totp_seed,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                mfa_totp_device_id=self.module.params.get("mfa_totp_device_id"),
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


MfaTotpDeviceActionsHelperCustom = get_custom_class("MfaTotpDeviceActionsHelperCustom")


class ResourceHelper(MfaTotpDeviceActionsHelperCustom, MfaTotpDeviceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            mfa_totp_device_id=dict(aliases=["id"], type="str", required=True),
            totp_token=dict(type="str", no_log=True),
            action=dict(
                type="str", required=True, choices=["activate", "generate_totp_seed"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="mfa_totp_device",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
