#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_file_storage_filesystem_snapshot_policy_actions
short_description: Perform actions on a FilesystemSnapshotPolicy resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a FilesystemSnapshotPolicy resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a file system snapshot policy into a different compartment within the same tenancy. For information about moving
      resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - For I(action=pause), this operation pauses the scheduled snapshot creation and snapshot deletion of the policy and updates the lifecycle state of the file
      system
      snapshot policy from ACTIVE to INACTIVE. When a file system snapshot policy is paused, file systems that are associated with the
      policy will not have scheduled snapshots created or deleted.
      If the policy is already paused, or in the INACTIVE state, you cannot pause it again. You can't pause a policy
      that is in a DELETING, DELETED, FAILED, CREATING or INACTIVE state; attempts to pause a policy in these states result in a 409 conflict error.
    - For I(action=unpause), this operation unpauses a paused file system snapshot policy and updates the lifecycle state of the file system snapshot policy
      from
      INACTIVE to ACTIVE. By default, file system snapshot policies are in the ACTIVE state. When a file system snapshot policy is not paused, or in the ACTIVE
      state, file systems that are associated with the
      policy will have snapshots created and deleted according to the schedules defined in the policy.
      If the policy is already in the ACTIVE state, you cannot unpause it. You can't unpause a policy that is in a DELETING, DELETED, FAILED, CREATING, or
      ACTIVE state; attempts to unpause a policy in these states result in a 409 conflict error.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to move the file system snapshot policy to.
            - Required for I(action=change_compartment).
        type: str
    filesystem_snapshot_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system snapshot policy.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the FilesystemSnapshotPolicy.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "pause"
            - "unpause"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on filesystem_snapshot_policy
  oci_file_storage_filesystem_snapshot_policy_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action pause on filesystem_snapshot_policy
  oci_file_storage_filesystem_snapshot_policy_actions:
    # required
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    action: pause

- name: Perform action unpause on filesystem_snapshot_policy
  oci_file_storage_filesystem_snapshot_policy_actions:
    # required
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    action: unpause

"""

RETURN = """
filesystem_snapshot_policy:
    description:
        - Details of the FilesystemSnapshotPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the file system snapshot
                  policy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - The availability domain that the file system snapshot policy is in. May be unset using a blank or NULL value.
                - "Example: `Uocm:PHX-AD-2`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system snapshot policy.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the file system snapshot policy.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the file system snapshot policy was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `policy1`"
            returned: on success
            type: str
            sample: display_name_example
        policy_prefix:
            description:
                - The prefix to apply to all snapshots created by this policy.
                - "Example: `acme`"
            returned: on success
            type: str
            sample: policy_prefix_example
        schedules:
            description:
                - The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy.
            returned: on success
            type: complex
            contains:
                schedule_prefix:
                    description:
                        - A name prefix to be applied to snapshots created by this schedule.
                        - "Example: `compliance1`"
                    returned: on success
                    type: str
                    sample: schedule_prefix_example
                time_schedule_start:
                    description:
                        - The starting point used to begin the scheduling of the snapshots based upon recurrence string
                          in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                          If no `timeScheduleStart` is provided, the value will be set to the time when the schedule was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                period:
                    description:
                        - The frequency of scheduled snapshots.
                    returned: on success
                    type: str
                    sample: HOURLY
                retention_duration_in_seconds:
                    description:
                        - The number of seconds to retain snapshots created with this schedule.
                          Snapshot expiration time will not be set if this value is empty.
                    returned: on success
                    type: int
                    sample: 56
                time_zone:
                    description:
                        - Time zone used for scheduling the snapshot.
                    returned: on success
                    type: str
                    sample: UTC
                hour_of_day:
                    description:
                        - The hour of the day to create a DAILY, WEEKLY, MONTHLY, or YEARLY snapshot.
                          If not set, a value will be chosen at creation time.
                    returned: on success
                    type: int
                    sample: 56
                day_of_week:
                    description:
                        - The day of the week to create a scheduled snapshot.
                          Used for WEEKLY snapshot schedules.
                    returned: on success
                    type: str
                    sample: MONDAY
                day_of_month:
                    description:
                        - The day of the month to create a scheduled snapshot.
                          If the day does not exist for the month, snapshot creation will be skipped.
                          Used for MONTHLY and YEARLY snapshot schedules.
                    returned: on success
                    type: int
                    sample: 56
                month:
                    description:
                        - The month to create a scheduled snapshot.
                          Used only for YEARLY snapshot schedules.
                    returned: on success
                    type: str
                    sample: JANUARY
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "policy_prefix": "policy_prefix_example",
        "schedules": [{
            "schedule_prefix": "schedule_prefix_example",
            "time_schedule_start": "2013-10-20T19:20:30+01:00",
            "period": "HOURLY",
            "retention_duration_in_seconds": 56,
            "time_zone": "UTC",
            "hour_of_day": 56,
            "day_of_week": "MONDAY",
            "day_of_month": 56,
            "month": "JANUARY"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import ChangeFilesystemSnapshotPolicyCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FilesystemSnapshotPolicyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        pause
        unpause
    """

    @staticmethod
    def get_module_resource_id_param():
        return "filesystem_snapshot_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("filesystem_snapshot_policy_id")

    def get_get_fn(self):
        return self.client.get_filesystem_snapshot_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_filesystem_snapshot_policy,
            filesystem_snapshot_policy_id=self.module.params.get(
                "filesystem_snapshot_policy_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeFilesystemSnapshotPolicyCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_filesystem_snapshot_policy_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                filesystem_snapshot_policy_id=self.module.params.get(
                    "filesystem_snapshot_policy_id"
                ),
                change_filesystem_snapshot_policy_compartment_details=action_details,
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

    def pause(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.pause_filesystem_snapshot_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                filesystem_snapshot_policy_id=self.module.params.get(
                    "filesystem_snapshot_policy_id"
                ),
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

    def unpause(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.unpause_filesystem_snapshot_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                filesystem_snapshot_policy_id=self.module.params.get(
                    "filesystem_snapshot_policy_id"
                ),
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


FilesystemSnapshotPolicyActionsHelperCustom = get_custom_class(
    "FilesystemSnapshotPolicyActionsHelperCustom"
)


class ResourceHelper(
    FilesystemSnapshotPolicyActionsHelperCustom,
    FilesystemSnapshotPolicyActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            filesystem_snapshot_policy_id=dict(
                aliases=["id"], type="str", required=True
            ),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "pause", "unpause"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="filesystem_snapshot_policy",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
