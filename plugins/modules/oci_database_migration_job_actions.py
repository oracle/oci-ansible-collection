#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_database_migration_job_actions
short_description: Perform actions on a Job resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Job resource in Oracle Cloud Infrastructure
    - For I(action=abort), aborts a Migration Job (either Evaluation or Migration).
    - For I(action=resume), resume a migration Job.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The OCID of the job
        type: str
        aliases: ["id"]
        required: true
    wait_after:
        description:
            - Name of a migration phase. The Job will wait after executing this
              phase until Resume Job endpoint is called again.
            - Applicable only for I(action=resume).
        type: str
        choices:
            - "ODMS_VALIDATE_TGT"
            - "ODMS_VALIDATE_SRC"
            - "ODMS_VALIDATE_PREMIGRATION_ADVISOR"
            - "ODMS_VALIDATE_GG_HUB"
            - "ODMS_VALIDATE_DATAPUMP_SETTINGS"
            - "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC"
            - "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT"
            - "ODMS_VALIDATE_DATAPUMP_SRC"
            - "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC"
            - "ODMS_VALIDATE"
            - "ODMS_PREPARE"
            - "ODMS_INITIAL_LOAD_EXPORT"
            - "ODMS_DATA_UPLOAD"
            - "ODMS_INITIAL_LOAD_IMPORT"
            - "ODMS_POST_INITIAL_LOAD"
            - "ODMS_PREPARE_REPLICATION_TARGET"
            - "ODMS_MONITOR_REPLICATION_LAG"
            - "ODMS_SWITCHOVER"
            - "ODMS_CLEANUP"
    action:
        description:
            - The action to perform on the Job.
        type: str
        required: true
        choices:
            - "abort"
            - "resume"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action abort on job
  oci_database_migration_job_actions:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
    action: abort

- name: Perform action resume on job
  oci_database_migration_job_actions:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
    action: resume

    # optional
    wait_after: ODMS_VALIDATE_TGT

"""

RETURN = """
job:
    description:
        - Details of the Job resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        unsupported_objects:
            description:
                - Database objects not supported.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "migration_id": "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "EVALUATION",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "progress": {
            "current_status": "PENDING",
            "current_phase": "ODMS_VALIDATE_TGT",
            "phases": [{
                "name": "ODMS_VALIDATE_TGT",
                "status": "PENDING",
                "duration_in_ms": 56,
                "is_advisor_report_available": true,
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
            }]
        },
        "unsupported_objects": [{
            "type": "GOLDEN_GATE",
            "owner": "owner_example",
            "object_name": "object_name_example"
        }],
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.database_migration import DatabaseMigrationClient
    from oci.database_migration.models import ResumeJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        abort
        resume
    """

    @staticmethod
    def get_module_resource_id_param():
        return "job_id"

    def get_module_resource_id(self):
        return self.module.params.get("job_id")

    def get_get_fn(self):
        return self.client.get_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job, job_id=self.module.params.get("job_id"),
        )

    def abort(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.abort_job,
            call_fn_args=(),
            call_fn_kwargs=dict(job_id=self.module.params.get("job_id"),),
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

    def resume(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResumeJobDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resume_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                job_id=self.module.params.get("job_id"),
                resume_job_details=action_details,
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


JobActionsHelperCustom = get_custom_class("JobActionsHelperCustom")


class ResourceHelper(JobActionsHelperCustom, JobActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            job_id=dict(aliases=["id"], type="str", required=True),
            wait_after=dict(
                type="str",
                choices=[
                    "ODMS_VALIDATE_TGT",
                    "ODMS_VALIDATE_SRC",
                    "ODMS_VALIDATE_PREMIGRATION_ADVISOR",
                    "ODMS_VALIDATE_GG_HUB",
                    "ODMS_VALIDATE_DATAPUMP_SETTINGS",
                    "ODMS_VALIDATE_DATAPUMP_SETTINGS_SRC",
                    "ODMS_VALIDATE_DATAPUMP_SETTINGS_TGT",
                    "ODMS_VALIDATE_DATAPUMP_SRC",
                    "ODMS_VALIDATE_DATAPUMP_ESTIMATE_SRC",
                    "ODMS_VALIDATE",
                    "ODMS_PREPARE",
                    "ODMS_INITIAL_LOAD_EXPORT",
                    "ODMS_DATA_UPLOAD",
                    "ODMS_INITIAL_LOAD_IMPORT",
                    "ODMS_POST_INITIAL_LOAD",
                    "ODMS_PREPARE_REPLICATION_TARGET",
                    "ODMS_MONITOR_REPLICATION_LAG",
                    "ODMS_SWITCHOVER",
                    "ODMS_CLEANUP",
                ],
            ),
            action=dict(type="str", required=True, choices=["abort", "resume"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="job",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
