#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_database_oneoff_patch_actions
short_description: Perform actions on an OneoffPatch resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OneoffPatch resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), move the one-off patch to the specified compartment.
    - For I(action=download), download one-off patch.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the resource to.
            - Required for I(action=change_compartment).
        type: str
    oneoff_patch_id:
        description:
            - The one-off patch L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the OneoffPatch.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "download"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on oneoff_patch
  oci_database_oneoff_patch_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    oneoff_patch_id: "ocid1.oneoffpatch.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action download on oneoff_patch
  oci_database_oneoff_patch_actions:
    # required
    oneoff_patch_id: "ocid1.oneoffpatch.oc1..xxxxxxEXAMPLExxxxxx"
    action: download

"""

RETURN = """
oneoff_patch:
    description:
        - Details of the OneoffPatch resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the one-off patch.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - One-off patch name.
            returned: on success
            type: str
            sample: display_name_example
        db_version:
            description:
                - A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable,
                  dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: str
            sample: db_version_example
        release_update:
            description:
                - The PSU or PBP or Release Updates. To get a list of supported versions, use the L(ListDbVersions,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
            returned: on success
            type: str
            sample: release_update_example
        one_off_patches:
            description:
                - List of one-off patches for Database Homes.
            returned: on success
            type: list
            sample: []
        size_in_kbs:
            description:
                - The size of one-off patch in kilobytes.
            returned: on success
            type: float
            sample: 3.4
        lifecycle_state:
            description:
                - The current state of the one-off patch.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Detailed message for the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        sha256_sum:
            description:
                - SHA-256 checksum of the one-off patch.
            returned: on success
            type: str
            sample: sha256_sum_example
        time_updated:
            description:
                - The date and time one-off patch was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - The date and time one-off patch was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_expiration:
            description:
                - The date and time until which the one-off patch will be available for download.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "db_version": "db_version_example",
        "release_update": "release_update_example",
        "one_off_patches": [],
        "size_in_kbs": 3.4,
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "sha256_sum": "sha256_sum_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_of_expiration": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ChangeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OneoffPatchActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        download
    """

    def __init__(self, *args, **kwargs):
        super(OneoffPatchActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    @staticmethod
    def get_module_resource_id_param():
        return "oneoff_patch_id"

    def get_module_resource_id(self):
        return self.module.params.get("oneoff_patch_id")

    def get_get_fn(self):
        return self.client.get_oneoff_patch

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_oneoff_patch,
            oneoff_patch_id=self.module.params.get("oneoff_patch_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_oneoff_patch_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_compartment_details=action_details,
                oneoff_patch_id=self.module.params.get("oneoff_patch_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def download(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.download_oneoff_patch,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oneoff_patch_id=self.module.params.get("oneoff_patch_id"),
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


OneoffPatchActionsHelperCustom = get_custom_class("OneoffPatchActionsHelperCustom")


class ResourceHelper(OneoffPatchActionsHelperCustom, OneoffPatchActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            oneoff_patch_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str", required=True, choices=["change_compartment", "download"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="oneoff_patch",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
