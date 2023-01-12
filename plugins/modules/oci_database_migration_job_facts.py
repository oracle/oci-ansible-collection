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
module: oci_database_migration_job_facts
short_description: Fetches details about one or multiple Job resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Job resources in Oracle Cloud Infrastructure
    - List all the names of the Migration jobs associated to the specified
      migration site.
    - If I(job_id) is specified, the details of a single Job will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The OCID of the job
            - Required to get a specific job.
        type: str
        aliases: ["id"]
    migration_id:
        description:
            - The ID of the migration in which to list resources.
            - Required to list multiple jobs.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.
              Default order for displayName is ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - The lifecycle state of the Migration Job.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "UNKNOWN"
            - "TERMINATED"
            - "FAILED"
            - "SUCCEEDED"
            - "WAITING"
            - "CANCELING"
            - "CANCELED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific job
  oci_database_migration_job_facts:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

- name: List jobs
  oci_database_migration_job_facts:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_by: timeCreated
    sort_order: ASC
    lifecycle_state: ACCEPTED

"""

RETURN = """
jobs:
    description:
        - List of Job resources
    returned: on success
    type: complex
    contains:
        unsupported_objects:
            description:
                - Database objects not supported.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - Type of unsupported object
                    returned: on success
                    type: str
                    sample: GOLDEN_GATE
                owner:
                    description:
                        - Owner of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: owner_example
                object_name:
                    description:
                        - Name of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: object_name_example
        id:
            description:
                - The OCID of the Migration Job.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Name of the job.
            returned: on success
            type: str
            sample: display_name_example
        migration_id:
            description:
                - The OCID of the Migration that this job belongs to.
            returned: on success
            type: str
            sample: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - The job type.
            returned: on success
            type: str
            sample: EVALUATION
        progress:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                current_status:
                    description:
                        - Current status of the job.
                    returned: on success
                    type: str
                    sample: PENDING
                current_phase:
                    description:
                        - Current phase of the job.
                    returned: on success
                    type: str
                    sample: ODMS_VALIDATE_TGT
                phases:
                    description:
                        - List of phase status for the job.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Phase name
                            returned: on success
                            type: str
                            sample: ODMS_VALIDATE_TGT
                        status:
                            description:
                                - Phase status
                            returned: on success
                            type: str
                            sample: PENDING
                        duration_in_ms:
                            description:
                                - Duration of the phase in milliseconds
                            returned: on success
                            type: int
                            sample: 56
                        is_advisor_report_available:
                            description:
                                - True if a Pre-Migration Advisor report is available for this phase. False or null if no report is available.
                            returned: on success
                            type: bool
                            sample: true
                        issue:
                            description:
                                - The text describing the root cause of the reported issue
                            returned: on success
                            type: str
                            sample: issue_example
                        action:
                            description:
                                - The text describing the action required to fix the issue
                            returned: on success
                            type: str
                            sample: action_example
                        extract:
                            description:
                                - Summary of phase status results.
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - Type of extract.
                                    returned: on success
                                    type: str
                                    sample: ERROR
                                message:
                                    description:
                                        - Message in entry.
                                    returned: on success
                                    type: str
                                    sample: message_example
                        log_location:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                bucket_name:
                                    description:
                                        - Name of the bucket containing the log file.
                                    returned: on success
                                    type: str
                                    sample: bucket_name_example
                                namespace:
                                    description:
                                        - Object Storage namespace.
                                    returned: on success
                                    type: str
                                    sample: namespace_example
                                object_name:
                                    description:
                                        - Log object name.
                                    returned: on success
                                    type: str
                                    sample: object_name_example
                        progress:
                            description:
                                - Percent progress of job phase.
                            returned: on success
                            type: int
                            sample: 56
                job_progress:
                    description:
                        - "Job progress percentage (0 - 100)"
                    returned: on success
                    type: int
                    sample: 56
        time_created:
            description:
                - The time the Migration Job was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Migration Job was last updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the migration job.
            returned: on success
            type: str
            sample: ACCEPTED
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information
                  for a resource in Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "unsupported_objects": [{
            "type": "GOLDEN_GATE",
            "owner": "owner_example",
            "object_name": "object_name_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "migration_id": "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "EVALUATION",
        "progress": {
            "current_status": "PENDING",
            "current_phase": "ODMS_VALIDATE_TGT",
            "phases": [{
                "name": "ODMS_VALIDATE_TGT",
                "status": "PENDING",
                "duration_in_ms": 56,
                "is_advisor_report_available": true,
                "issue": "issue_example",
                "action": "action_example",
                "extract": [{
                    "type": "ERROR",
                    "message": "message_example"
                }],
                "log_location": {
                    "bucket_name": "bucket_name_example",
                    "namespace": "namespace_example",
                    "object_name": "object_name_example"
                },
                "progress": 56
            }],
            "job_progress": 56
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_migration import DatabaseMigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "job_id",
        ]

    def get_required_params_for_list(self):
        return [
            "migration_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job, job_id=self.module.params.get("job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_jobs,
            migration_id=self.module.params.get("migration_id"),
            **optional_kwargs
        )


JobFactsHelperCustom = get_custom_class("JobFactsHelperCustom")


class ResourceFactsHelper(JobFactsHelperCustom, JobFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            job_id=dict(aliases=["id"], type="str"),
            migration_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "UNKNOWN",
                    "TERMINATED",
                    "FAILED",
                    "SUCCEEDED",
                    "WAITING",
                    "CANCELING",
                    "CANCELED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="job",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(jobs=result)


if __name__ == "__main__":
    main()
