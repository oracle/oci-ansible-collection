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
module: oci_file_storage_filesystem_snapshot_policy
short_description: Manage a FilesystemSnapshotPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a FilesystemSnapshotPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new file system snapshot policy in the specified compartment and
      availability domain.
    - After you create a file system snapshot policy, you can associate it with
      file systems.
    - "This resource has the following action operations in the M(oracle.oci.oci_file_storage_filesystem_snapshot_policy_actions) module: change_compartment,
      pause, unpause."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain that the file system snapshot policy is in.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the file system snapshot
              policy.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - "Example: `policy1`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    policy_prefix:
        description:
            - The prefix to apply to all snapshots created by this policy.
            - "Example: `acme`"
            - This parameter is updatable.
        type: str
    schedules:
        description:
            - The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy.
            - "If using the CLI, provide the schedule as a list of JSON strings, with the list wrapped in
              quotation marks, i.e.
              ```
                --schedules '[{\\"timeZone\\":\\"UTC\\",\\"period\\":\\"DAILY\\",\\"hourOfDay\\":18},{\\"timeZone\\":\\"UTC\\",\\"period\\":\\"HOURLY\\"}]'
              ```"
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            schedule_prefix:
                description:
                    - A name prefix to be applied to snapshots created by this schedule.
                    - "Example: `compliance1`"
                type: str
            time_schedule_start:
                description:
                    - The starting point used to begin the scheduling of the snapshots based upon recurrence string
                      in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                      If no `timeScheduleStart` is provided, the value will be set to the time when the schedule was created.
                type: str
            period:
                description:
                    - The frequency of scheduled snapshots.
                type: str
                choices:
                    - "HOURLY"
                    - "DAILY"
                    - "WEEKLY"
                    - "MONTHLY"
                    - "YEARLY"
                required: true
            retention_duration_in_seconds:
                description:
                    - The number of seconds to retain snapshots created with this schedule.
                      Snapshot expiration time will not be set if this value is empty.
                type: int
            time_zone:
                description:
                    - Time zone used for scheduling the snapshot.
                type: str
                choices:
                    - "UTC"
                    - "REGIONAL_DATA_CENTER_TIME"
                required: true
            hour_of_day:
                description:
                    - The hour of the day to create a DAILY, WEEKLY, MONTHLY, or YEARLY snapshot.
                      If not set, a value will be chosen at creation time.
                type: int
            day_of_week:
                description:
                    - The day of the week to create a scheduled snapshot.
                      Used for WEEKLY snapshot schedules.
                type: str
                choices:
                    - "MONDAY"
                    - "TUESDAY"
                    - "WEDNESDAY"
                    - "THURSDAY"
                    - "FRIDAY"
                    - "SATURDAY"
                    - "SUNDAY"
            day_of_month:
                description:
                    - The day of the month to create a scheduled snapshot.
                      If the day does not exist for the month, snapshot creation will be skipped.
                      Used for MONTHLY and YEARLY snapshot schedules.
                type: int
            month:
                description:
                    - The month to create a scheduled snapshot.
                      Used only for YEARLY snapshot schedules.
                type: str
                choices:
                    - "JANUARY"
                    - "FEBRUARY"
                    - "MARCH"
                    - "APRIL"
                    - "MAY"
                    - "JUNE"
                    - "JULY"
                    - "AUGUST"
                    - "SEPTEMBER"
                    - "OCTOBER"
                    - "NOVEMBER"
                    - "DECEMBER"
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair
               with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    filesystem_snapshot_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system snapshot policy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the FilesystemSnapshotPolicy.
            - Use I(state=present) to create or update a FilesystemSnapshotPolicy.
            - Use I(state=absent) to delete a FilesystemSnapshotPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create filesystem_snapshot_policy
  oci_file_storage_filesystem_snapshot_policy:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    policy_prefix: policy_prefix_example
    schedules:
    - # required
      period: HOURLY
      time_zone: UTC

      # optional
      schedule_prefix: schedule_prefix_example
      time_schedule_start: time_schedule_start_example
      retention_duration_in_seconds: 56
      hour_of_day: 56
      day_of_week: MONDAY
      day_of_month: 56
      month: JANUARY
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update filesystem_snapshot_policy
  oci_file_storage_filesystem_snapshot_policy:
    # required
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    policy_prefix: policy_prefix_example
    schedules:
    - # required
      period: HOURLY
      time_zone: UTC

      # optional
      schedule_prefix: schedule_prefix_example
      time_schedule_start: time_schedule_start_example
      retention_duration_in_seconds: 56
      hour_of_day: 56
      day_of_week: MONDAY
      day_of_month: 56
      month: JANUARY
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update filesystem_snapshot_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_filesystem_snapshot_policy:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    policy_prefix: policy_prefix_example
    schedules:
    - # required
      period: HOURLY
      time_zone: UTC

      # optional
      schedule_prefix: schedule_prefix_example
      time_schedule_start: time_schedule_start_example
      retention_duration_in_seconds: 56
      hour_of_day: 56
      day_of_week: MONDAY
      day_of_month: 56
      month: JANUARY
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete filesystem_snapshot_policy
  oci_file_storage_filesystem_snapshot_policy:
    # required
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete filesystem_snapshot_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_filesystem_snapshot_policy:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import CreateFilesystemSnapshotPolicyDetails
    from oci.file_storage.models import UpdateFilesystemSnapshotPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FilesystemSnapshotPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            FilesystemSnapshotPolicyHelperGen, self
        ).get_possible_entity_types() + [
            "filesystemsnapshotpolicy",
            "filesystemsnapshotpolicies",
            "fileStoragefilesystemsnapshotpolicy",
            "fileStoragefilesystemsnapshotpolicies",
            "filesystemsnapshotpolicyresource",
            "filesystemsnapshotpoliciesresource",
            "filestorage",
        ]

    def get_module_resource_id_param(self):
        return "filesystem_snapshot_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("filesystem_snapshot_policy_id")

    def get_get_fn(self):
        return self.client.get_filesystem_snapshot_policy

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_filesystem_snapshot_policy,
            filesystem_snapshot_policy_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_filesystem_snapshot_policy,
            filesystem_snapshot_policy_id=self.module.params.get(
                "filesystem_snapshot_policy_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "availability_domain",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_filesystem_snapshot_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateFilesystemSnapshotPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_filesystem_snapshot_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_filesystem_snapshot_policy_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateFilesystemSnapshotPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_filesystem_snapshot_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                filesystem_snapshot_policy_id=self.module.params.get(
                    "filesystem_snapshot_policy_id"
                ),
                update_filesystem_snapshot_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_filesystem_snapshot_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                filesystem_snapshot_policy_id=self.module.params.get(
                    "filesystem_snapshot_policy_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


FilesystemSnapshotPolicyHelperCustom = get_custom_class(
    "FilesystemSnapshotPolicyHelperCustom"
)


class ResourceHelper(
    FilesystemSnapshotPolicyHelperCustom, FilesystemSnapshotPolicyHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            policy_prefix=dict(type="str"),
            schedules=dict(
                type="list",
                elements="dict",
                options=dict(
                    schedule_prefix=dict(type="str"),
                    time_schedule_start=dict(type="str"),
                    period=dict(
                        type="str",
                        required=True,
                        choices=["HOURLY", "DAILY", "WEEKLY", "MONTHLY", "YEARLY"],
                    ),
                    retention_duration_in_seconds=dict(type="int"),
                    time_zone=dict(
                        type="str",
                        required=True,
                        choices=["UTC", "REGIONAL_DATA_CENTER_TIME"],
                    ),
                    hour_of_day=dict(type="int"),
                    day_of_week=dict(
                        type="str",
                        choices=[
                            "MONDAY",
                            "TUESDAY",
                            "WEDNESDAY",
                            "THURSDAY",
                            "FRIDAY",
                            "SATURDAY",
                            "SUNDAY",
                        ],
                    ),
                    day_of_month=dict(type="int"),
                    month=dict(
                        type="str",
                        choices=[
                            "JANUARY",
                            "FEBRUARY",
                            "MARCH",
                            "APRIL",
                            "MAY",
                            "JUNE",
                            "JULY",
                            "AUGUST",
                            "SEPTEMBER",
                            "OCTOBER",
                            "NOVEMBER",
                            "DECEMBER",
                        ],
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            filesystem_snapshot_policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
