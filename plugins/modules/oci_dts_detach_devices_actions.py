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
module: oci_dts_detach_devices_actions
short_description: Perform actions on a DetachDevices resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DetachDevices resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a TransferJob into a different compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    transfer_job_id:
        description:
            - ID of the Transfer Job
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID],https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resources should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the DetachDevices.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on detach_devices
  oci_dts_detach_devices_actions:
    # required
    transfer_job_id: "ocid1.transferjob.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    from oci.dts import TransferJobClient
    from oci.dts.models import ChangeTransferJobCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetachDevicesActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "transfer_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("transfer_job_id")

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeTransferJobCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_transfer_job_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                transfer_job_id=self.module.params.get("transfer_job_id"),
                change_transfer_job_compartment_details=action_details,
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


DetachDevicesActionsHelperCustom = get_custom_class("DetachDevicesActionsHelperCustom")


class ResourceHelper(DetachDevicesActionsHelperCustom, DetachDevicesActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            transfer_job_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="detach_devices",
        service_client_class=TransferJobClient,
        namespace="dts",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
