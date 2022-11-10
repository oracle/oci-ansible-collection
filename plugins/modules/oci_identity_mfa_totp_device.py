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
module: oci_identity_mfa_totp_device
short_description: Manage a MfaTotpDevice resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a MfaTotpDevice resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new MFA TOTP device for the user. A user can have one MFA TOTP device.
    - "This resource has the following action operations in the M(oracle.oci.oci_identity_mfa_totp_device_actions) module: activate, generate_totp_seed."
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
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the MfaTotpDevice.
            - Use I(state=present) to create a MfaTotpDevice.
            - Use I(state=absent) to delete a MfaTotpDevice.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create mfa_totp_device
  oci_identity_mfa_totp_device:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete mfa_totp_device
  oci_identity_mfa_totp_device:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    mfa_totp_device_id: "ocid1.mfatotpdevice.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
            sample: "2013-10-20T19:20:30+01:00"
        time_expires:
            description:
                - Date and time when this MFA TOTP device will expire, in the format defined by RFC3339.
                  Null if it never expires.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "inactive_status": 56,
        "is_activated": true
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
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MfaTotpDeviceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MfaTotpDeviceHelperGen, self).get_possible_entity_types() + [
            "mfatotpdevice",
            "mfatotpdevices",
            "identitymfatotpdevice",
            "identitymfatotpdevices",
            "mfatotpdeviceresource",
            "mfatotpdevicesresource",
            "identity",
        ]

    def get_module_resource_id_param(self):
        return "mfa_totp_device_id"

    def get_module_resource_id(self):
        return self.module.params.get("mfa_totp_device_id")

    def get_get_fn(self):
        return self.client.get_mfa_totp_device

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_mfa_totp_device,
            mfa_totp_device_id=summary_model.id,
            user_id=self.module.params.get("user_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_mfa_totp_device,
            user_id=self.module.params.get("user_id"),
            mfa_totp_device_id=self.module.params.get("mfa_totp_device_id"),
        )

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
            self.client.list_mfa_totp_devices, **kwargs
        )

    def create_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_mfa_totp_device,
            call_fn_args=(),
            call_fn_kwargs=dict(user_id=self.module.params.get("user_id"),),
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
            call_fn=self.client.delete_mfa_totp_device,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                mfa_totp_device_id=self.module.params.get("mfa_totp_device_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MfaTotpDeviceHelperCustom = get_custom_class("MfaTotpDeviceHelperCustom")


class ResourceHelper(MfaTotpDeviceHelperCustom, MfaTotpDeviceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            mfa_totp_device_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="mfa_totp_device",
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
