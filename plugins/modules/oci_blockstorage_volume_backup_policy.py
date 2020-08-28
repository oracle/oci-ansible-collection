#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_blockstorage_volume_backup_policy
short_description: Manage a VolumeBackupPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VolumeBackupPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new user defined backup policy.
    - For more information about Oracle defined backup policies and user defined backup policies,
      see L(Policy-Based Backups,https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
              Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    destination_region:
        description:
            - "The paired destination region for copying scheduled backups to. Example: `us-ashburn-1`.
              See L(Region Pairs,https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#RegionPairs) for details about paired
              regions."
        type: str
    schedules:
        description:
            - The collection of schedules for the volume backup policy. See
              see L(Schedules,https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#schedules) in
              L(Policy-Based Backups,https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm) for more information.
        type: list
        suboptions:
            backup_type:
                description:
                    - The type of volume backup to create.
                type: str
                choices:
                    - "FULL"
                    - "INCREMENTAL"
                required: true
            offset_seconds:
                description:
                    - The number of seconds that the volume backup start time should be shifted from the default interval boundaries specified by the period.
                      The volume backup start time is the frequency start time plus the offset.
                type: int
            period:
                description:
                    - The volume backup frequency.
                type: str
                choices:
                    - "ONE_HOUR"
                    - "ONE_DAY"
                    - "ONE_WEEK"
                    - "ONE_MONTH"
                    - "ONE_YEAR"
                required: true
            offset_type:
                description:
                    - Indicates how the offset is defined. If value is `STRUCTURED`, then `hourOfDay`, `dayOfWeek`, `dayOfMonth`, and `month` fields are used
                      and `offsetSeconds` will be ignored in requests and users should ignore its value from the responses.
                    - "`hourOfDay` is applicable for periods `ONE_DAY`, `ONE_WEEK`, `ONE_MONTH` and `ONE_YEAR`."
                    - "`dayOfWeek` is applicable for period `ONE_WEEK`."
                    - "`dayOfMonth` is applicable for periods `ONE_MONTH` and `ONE_YEAR`."
                    - "'month' is applicable for period 'ONE_YEAR'."
                    - They will be ignored in the requests for inapplicable periods.
                    - If value is `NUMERIC_SECONDS`, then `offsetSeconds` will be used for both requests and responses and the structured fields will be ignored
                      in the requests and users should ignore their values from the responses.
                    - For clients using older versions of Apis and not sending `offsetType` in their requests, the behaviour is just like `NUMERIC_SECONDS`.
                type: str
                choices:
                    - "STRUCTURED"
                    - "NUMERIC_SECONDS"
            hour_of_day:
                description:
                    - The hour of the day to schedule the volume backup.
                type: int
            day_of_week:
                description:
                    - The day of the week to schedule the volume backup.
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
                    - The day of the month to schedule the volume backup.
                type: int
            month:
                description:
                    - The month of the year to schedule the volume backup.
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
            retention_seconds:
                description:
                    - How long, in seconds, to keep the volume backups created by this schedule.
                type: int
                required: true
            time_zone:
                description:
                    - Specifies what time zone is the schedule in
                type: str
                choices:
                    - "UTC"
                    - "REGIONAL_DATA_CENTER_TIME"
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    policy_id:
        description:
            - The OCID of the volume backup policy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the VolumeBackupPolicy.
            - Use I(state=present) to create or update a VolumeBackupPolicy.
            - Use I(state=absent) to delete a VolumeBackupPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create volume_backup_policy
  oci_blockstorage_volume_backup_policy:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update volume_backup_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume_backup_policy:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    destination_region: us-ashburn-1
    schedules:
    - backup_type: FULL
      period: ONE_HOUR
      retention_seconds: 56
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    freeform_tags: {'Department': 'Finance'}

- name: Update volume_backup_policy
  oci_blockstorage_volume_backup_policy:
    display_name: display_name_example
    destination_region: us-ashburn-1
    policy_id: ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete volume_backup_policy
  oci_blockstorage_volume_backup_policy:
    policy_id: ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete volume_backup_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_blockstorage_volume_backup_policy:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    state: absent

"""

RETURN = """
volume_backup_policy:
    description:
        - Details of the VolumeBackupPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - A user-friendly name for the volume backup policy. Does not have to be unique and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        id:
            description:
                - The OCID of the volume backup policy.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        schedules:
            description:
                - The collection of schedules that this policy will apply.
            returned: on success
            type: complex
            contains:
                backup_type:
                    description:
                        - The type of volume backup to create.
                    returned: on success
                    type: string
                    sample: FULL
                offset_seconds:
                    description:
                        - The number of seconds that the volume backup start time should be shifted from the default interval boundaries specified by the
                          period. The volume backup start time is the frequency start time plus the offset.
                    returned: on success
                    type: int
                    sample: 56
                period:
                    description:
                        - The volume backup frequency.
                    returned: on success
                    type: string
                    sample: ONE_HOUR
                offset_type:
                    description:
                        - Indicates how the offset is defined. If value is `STRUCTURED`, then `hourOfDay`, `dayOfWeek`, `dayOfMonth`, and `month` fields are
                          used and `offsetSeconds` will be ignored in requests and users should ignore its value from the responses.
                        - "`hourOfDay` is applicable for periods `ONE_DAY`, `ONE_WEEK`, `ONE_MONTH` and `ONE_YEAR`."
                        - "`dayOfWeek` is applicable for period `ONE_WEEK`."
                        - "`dayOfMonth` is applicable for periods `ONE_MONTH` and `ONE_YEAR`."
                        - "'month' is applicable for period 'ONE_YEAR'."
                        - They will be ignored in the requests for inapplicable periods.
                        - If value is `NUMERIC_SECONDS`, then `offsetSeconds` will be used for both requests and responses and the structured fields will be
                          ignored in the requests and users should ignore their values from the responses.
                        - For clients using older versions of Apis and not sending `offsetType` in their requests, the behaviour is just like `NUMERIC_SECONDS`.
                    returned: on success
                    type: string
                    sample: STRUCTURED
                hour_of_day:
                    description:
                        - The hour of the day to schedule the volume backup.
                    returned: on success
                    type: int
                    sample: 56
                day_of_week:
                    description:
                        - The day of the week to schedule the volume backup.
                    returned: on success
                    type: string
                    sample: MONDAY
                day_of_month:
                    description:
                        - The day of the month to schedule the volume backup.
                    returned: on success
                    type: int
                    sample: 56
                month:
                    description:
                        - The month of the year to schedule the volume backup.
                    returned: on success
                    type: string
                    sample: JANUARY
                retention_seconds:
                    description:
                        - How long, in seconds, to keep the volume backups created by this schedule.
                    returned: on success
                    type: int
                    sample: 56
                time_zone:
                    description:
                        - Specifies what time zone is the schedule in
                    returned: on success
                    type: string
                    sample: UTC
        destination_region:
            description:
                - The paired destination region for copying scheduled backups to. Example `us-ashburn-1`.
                  See L(Region Pairs,https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#RegionPairs) for details about paired
                  regions.
            returned: on success
            type: string
            sample: destination_region_example
        time_created:
            description:
                - The date and time the volume backup policy was created. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume backup.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: {
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "schedules": [{
            "backup_type": "FULL",
            "offset_seconds": 56,
            "period": "ONE_HOUR",
            "offset_type": "STRUCTURED",
            "hour_of_day": 56,
            "day_of_week": "MONDAY",
            "day_of_month": 56,
            "month": "JANUARY",
            "retention_seconds": 56,
            "time_zone": "UTC"
        }],
        "destination_region": "destination_region_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import BlockstorageClient
    from oci.core.models import CreateVolumeBackupPolicyDetails
    from oci.core.models import UpdateVolumeBackupPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeBackupPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("policy_id")

    def get_get_fn(self):
        return self.client.get_volume_backup_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_backup_policy,
            policy_id=self.module.params.get("policy_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id"]

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
            self.client.list_volume_backup_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateVolumeBackupPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_volume_backup_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(create_volume_backup_policy_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateVolumeBackupPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_volume_backup_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                policy_id=self.module.params.get("policy_id"),
                update_volume_backup_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_volume_backup_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(policy_id=self.module.params.get("policy_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


VolumeBackupPolicyHelperCustom = get_custom_class("VolumeBackupPolicyHelperCustom")


class ResourceHelper(VolumeBackupPolicyHelperCustom, VolumeBackupPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            destination_region=dict(type="str"),
            schedules=dict(
                type="list",
                elements="dict",
                options=dict(
                    backup_type=dict(
                        type="str", required=True, choices=["FULL", "INCREMENTAL"]
                    ),
                    offset_seconds=dict(type="int"),
                    period=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ONE_HOUR",
                            "ONE_DAY",
                            "ONE_WEEK",
                            "ONE_MONTH",
                            "ONE_YEAR",
                        ],
                    ),
                    offset_type=dict(
                        type="str", choices=["STRUCTURED", "NUMERIC_SECONDS"]
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
                    retention_seconds=dict(type="int", required=True),
                    time_zone=dict(
                        type="str", choices=["UTC", "REGIONAL_DATA_CENTER_TIME"]
                    ),
                ),
            ),
            defined_tags=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="volume_backup_policy",
        service_client_class=BlockstorageClient,
        namespace="core",
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
