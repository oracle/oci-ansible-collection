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
module: oci_blockstorage_volume_backup_policy_facts
short_description: Fetches details about one or multiple VolumeBackupPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VolumeBackupPolicy resources in Oracle Cloud Infrastructure
    - Lists all the volume backup policies available in the specified compartment.
    - For more information about Oracle defined backup policies and user defined backup policies,
      see L(Policy-Based Backups,https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm).
    - If I(policy_id) is specified, the details of a single VolumeBackupPolicy will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    policy_id:
        description:
            - The OCID of the volume backup policy.
            - Required to get a specific volume_backup_policy.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
              If no compartment is specified, the Oracle defined backup policies are listed.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific volume_backup_policy
  oci_blockstorage_volume_backup_policy_facts:
    # required
    policy_id: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"

- name: List volume_backup_policies
  oci_blockstorage_volume_backup_policy_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
volume_backup_policies:
    description:
        - List of VolumeBackupPolicy resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The OCID of the volume backup policy.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
                    type: str
                    sample: FULL
                offset_seconds:
                    description:
                        - The number of seconds that the volume backup start
                          time should be shifted from the default interval boundaries specified by
                          the period. The volume backup start time is the frequency start time plus the offset.
                    returned: on success
                    type: int
                    sample: 56
                period:
                    description:
                        - The volume backup frequency.
                    returned: on success
                    type: str
                    sample: ONE_HOUR
                offset_type:
                    description:
                        - Indicates how the offset is defined. If value is `STRUCTURED`,
                          then `hourOfDay`, `dayOfWeek`, `dayOfMonth`, and `month` fields are used
                          and `offsetSeconds` will be ignored in requests and users should ignore its
                          value from the responses.
                        - "`hourOfDay` is applicable for periods `ONE_DAY`,
                          `ONE_WEEK`, `ONE_MONTH` and `ONE_YEAR`."
                        - "`dayOfWeek` is applicable for period
                          `ONE_WEEK`."
                        - "`dayOfMonth` is applicable for periods `ONE_MONTH` and `ONE_YEAR`."
                        - "'month' is applicable for period 'ONE_YEAR'."
                        - They will be ignored in the requests for inapplicable periods.
                        - If value is `NUMERIC_SECONDS`, then `offsetSeconds`
                          will be used for both requests and responses and the structured fields will be
                          ignored in the requests and users should ignore their values from the responses.
                        - For clients using older versions of Apis and not sending `offsetType` in their
                          requests, the behaviour is just like `NUMERIC_SECONDS`.
                    returned: on success
                    type: str
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
                    type: str
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
                    type: str
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
                    type: str
                    sample: UTC
        destination_region:
            description:
                - The paired destination region for copying scheduled backups to. Example `us-ashburn-1`.
                  See L(Region Pairs,https://docs.cloud.oracle.com/iaas/Content/Block/Tasks/schedulingvolumebackups.htm#RegionPairs) for details about paired
                  regions.
            returned: on success
            type: str
            sample: us-phoenix-1
        time_created:
            description:
                - The date and time the volume backup policy was created. Format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        compartment_id:
            description:
                - The OCID of the compartment that contains the volume backup.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: [{
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
        "destination_region": "us-phoenix-1",
        "time_created": "2013-10-20T19:20:30+01:00",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import BlockstorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeBackupPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "policy_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_backup_policy,
            policy_id=self.module.params.get("policy_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_volume_backup_policies, **optional_kwargs
        )


VolumeBackupPolicyFactsHelperCustom = get_custom_class(
    "VolumeBackupPolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    VolumeBackupPolicyFactsHelperCustom, VolumeBackupPolicyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            policy_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="volume_backup_policy",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(volume_backup_policies=result)


if __name__ == "__main__":
    main()
