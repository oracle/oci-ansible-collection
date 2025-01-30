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
module: oci_file_storage_filesystem_snapshot_policy_facts
short_description: Fetches details about one or multiple FilesystemSnapshotPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple FilesystemSnapshotPolicy resources in Oracle Cloud Infrastructure
    - Lists file system snapshot policies in the specified compartment.
    - If I(filesystem_snapshot_policy_id) is specified, the details of a single FilesystemSnapshotPolicy will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    filesystem_snapshot_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system snapshot policy.
            - Required to get a specific filesystem_snapshot_policy.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple filesystem_snapshot_policies.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required to list multiple filesystem_snapshot_policies.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
            - "Example: `My resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Filter results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "INACTIVE"
    sort_by:
        description:
            - The field to sort by. You can provide either value, but not both.
              By default, when you sort by time created, results are shown
              in descending order. When you sort by displayName, results are
              shown in ascending alphanumeric order.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc', where 'asc' is
              ascending and 'desc' is descending. The default order is 'desc'
              except for numeric values.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific filesystem_snapshot_policy
  oci_file_storage_filesystem_snapshot_policy_facts:
    # required
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"

- name: List filesystem_snapshot_policies
  oci_file_storage_filesystem_snapshot_policy_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
filesystem_snapshot_policies:
    description:
        - List of FilesystemSnapshotPolicy resources
    returned: on success
    type: complex
    contains:
        schedules:
            description:
                - The list of associated snapshot schedules. A maximum of 10 schedules can be associated with a policy.
                - Returned for get operation
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
        availability_domain:
            description:
                - The availability domain that the file system snapshot policy is in. May be unset using a blank or NULL value.
                - "Example: `Uocm:PHX-AD-2`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the file system snapshot
                  policy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `policy1`"
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time the file system snapshot policy was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        policy_prefix:
            description:
                - The prefix to apply to all snapshots created by this policy.
                - "Example: `acme`"
            returned: on success
            type: str
            sample: policy_prefix_example
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
    sample: [{
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
        "availability_domain": "Uocm:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "policy_prefix": "policy_prefix_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.file_storage import FileStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FilesystemSnapshotPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "filesystem_snapshot_policy_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "availability_domain",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_filesystem_snapshot_policy,
            filesystem_snapshot_policy_id=self.module.params.get(
                "filesystem_snapshot_policy_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_filesystem_snapshot_policies,
            compartment_id=self.module.params.get("compartment_id"),
            availability_domain=self.module.params.get("availability_domain"),
            **optional_kwargs
        )


FilesystemSnapshotPolicyFactsHelperCustom = get_custom_class(
    "FilesystemSnapshotPolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    FilesystemSnapshotPolicyFactsHelperCustom, FilesystemSnapshotPolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            filesystem_snapshot_policy_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "INACTIVE",
                ],
            ),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="filesystem_snapshot_policy",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(filesystem_snapshot_policies=result)


if __name__ == "__main__":
    main()
