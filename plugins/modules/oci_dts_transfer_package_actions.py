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
module: oci_dts_transfer_package_actions
short_description: Perform actions on a TransferPackage resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a TransferPackage resource in Oracle Cloud Infrastructure
    - For I(action=detach_devices), detaches Devices from a Transfer Package
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
            - The action to perform on the TransferPackage.
        type: str
        required: true
        choices:
            - "detach_devices"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action detach_devices on transfer_package
  oci_dts_transfer_package_actions:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    transfer_package_label: transfer_package_label_example
    action: detach_devices

    # optional
    device_labels: [ "device_labels_example" ]

"""

RETURN = """
transfer_package:
    description:
        - Details of the TransferPackage resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        label:
            description:
                - ""
            returned: on success
            type: str
            sample: label_example
        lifecycle_state:
            description:
                - ""
            returned: on success
            type: str
            sample: PREPARING
        transfer_job_id:
            description:
                - ""
            returned: on success
            type: str
            sample: "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx"
        creation_time:
            description:
                - ""
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        original_package_delivery_tracking_number:
            description:
                - ""
            returned: on success
            type: str
            sample: original_package_delivery_tracking_number_example
        return_package_delivery_tracking_number:
            description:
                - ""
            returned: on success
            type: str
            sample: return_package_delivery_tracking_number_example
        package_delivery_vendor:
            description:
                - ""
            returned: on success
            type: str
            sample: package_delivery_vendor_example
        transfer_site_shipping_address:
            description:
                - ""
            returned: on success
            type: str
            sample: transfer_site_shipping_address_example
        attached_transfer_device_labels:
            description:
                - Transfer Devices attached to this Transfer Package
            returned: on success
            type: list
            sample: []
    sample: {
        "label": "label_example",
        "lifecycle_state": "PREPARING",
        "transfer_job_id": "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx",
        "creation_time": "2013-10-20T19:20:30+01:00",
        "original_package_delivery_tracking_number": "original_package_delivery_tracking_number_example",
        "return_package_delivery_tracking_number": "return_package_delivery_tracking_number_example",
        "package_delivery_vendor": "package_delivery_vendor_example",
        "transfer_site_shipping_address": "transfer_site_shipping_address_example",
        "attached_transfer_device_labels": []
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
    from oci.dts import TransferPackageClient
    from oci.dts.models import DetachDevicesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TransferPackageActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        detach_devices
    """

    @staticmethod
    def get_module_resource_id_param():
        return "transfer_package_label"

    def get_module_resource_id(self):
        return self.module.params.get("transfer_package_label")

    def get_get_fn(self):
        return self.client.get_transfer_package

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_transfer_package,
            id=self.module.params.get("id"),
            transfer_package_label=self.module.params.get("transfer_package_label"),
        )

    def detach_devices(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DetachDevicesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.detach_devices_from_transfer_package,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                transfer_package_label=self.module.params.get("transfer_package_label"),
                detach_devices_details=action_details,
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


TransferPackageActionsHelperCustom = get_custom_class(
    "TransferPackageActionsHelperCustom"
)


class ResourceHelper(
    TransferPackageActionsHelperCustom, TransferPackageActionsHelperGen
):
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
            action=dict(type="str", required=True, choices=["detach_devices"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="transfer_package",
        service_client_class=TransferPackageClient,
        namespace="dts",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
