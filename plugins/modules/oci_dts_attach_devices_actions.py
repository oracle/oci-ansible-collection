#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_dts_attach_devices_actions
short_description: Perform actions on an AttachDevices resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AttachDevices resource in Oracle Cloud Infrastructure
    - For I(action=attach_devices_to_transfer_package), attaches Devices to a Transfer Package
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    id:
        description:
            - ID of the Transfer Job
        type: str
        required: true
    transfer_package_label:
        description:
            - Label of the Transfer Package
        type: str
        required: true
    device_labels:
        description:
            - List of TransferDeviceLabel's
        type: list
        elements: str
    action:
        description:
            - The action to perform on the AttachDevices.
        type: str
        required: true
        choices:
            - "attach_devices_to_transfer_package"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action attach_devices_to_transfer_package on attach_devices
  oci_dts_attach_devices_actions:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    transfer_package_label: transfer_package_label_example
    action: attach_devices_to_transfer_package

    # optional
    device_labels: [ "device_labels_example" ]

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
    from oci.dts import TransferPackageClient
    from oci.dts.models import AttachDevicesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AttachDevicesActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        attach_devices_to_transfer_package
    """

    @staticmethod
    def get_module_resource_id_param():
        return "transfer_package_label"

    def get_module_resource_id(self):
        return self.module.params.get("transfer_package_label")

    def attach_devices_to_transfer_package(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AttachDevicesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.attach_devices_to_transfer_package,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                transfer_package_label=self.module.params.get("transfer_package_label"),
                attach_devices_details=action_details,
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


AttachDevicesActionsHelperCustom = get_custom_class("AttachDevicesActionsHelperCustom")


class ResourceHelper(AttachDevicesActionsHelperCustom, AttachDevicesActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            id=dict(type="str", required=True),
            transfer_package_label=dict(type="str", required=True),
            device_labels=dict(type="list", elements="str"),
            action=dict(
                type="str",
                required=True,
                choices=["attach_devices_to_transfer_package"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="attach_devices",
        service_client_class=TransferPackageClient,
        namespace="dts",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
