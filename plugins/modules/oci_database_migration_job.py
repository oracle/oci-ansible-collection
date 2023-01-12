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
module: oci_database_migration_job
short_description: Manage a Job resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a Job resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_database_migration_job_actions) module: abort, resume."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Name of the job.
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    job_id:
        description:
            - The OCID of the job
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    migration_id:
        description:
            - The ID of the migration in which to list resources.
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the Job.
            - Use I(state=present) to update an existing a Job.
            - Use I(state=absent) to delete a Job.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update job
  oci_database_migration_job:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_migration_job:
    # required
    display_name: display_name_example
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete job
  oci_database_migration_job:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_migration_job:
    # required
    display_name: display_name_example
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
    from oci.database_migration import DatabaseMigrationClient
    from oci.database_migration.models import UpdateJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(JobHelperGen, self).get_possible_entity_types() + [
            "job",
            "jobs",
            "databaseMigrationjob",
            "databaseMigrationjobs",
            "jobresource",
            "jobsresource",
            "databasemigration",
        ]

    def get_module_resource_id_param(self):
        return "job_id"

    def get_module_resource_id(self):
        return self.module.params.get("job_id")

    def get_get_fn(self):
        return self.client.get_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_job, job_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job, job_id=self.module.params.get("job_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "migration_id",
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
        return oci_common_utils.list_all_resources(self.client.list_jobs, **kwargs)

    def get_update_model_class(self):
        return UpdateJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                job_id=self.module.params.get("job_id"),
                update_job_details=update_details,
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
            call_fn=self.client.delete_job,
            call_fn_args=(),
            call_fn_kwargs=dict(job_id=self.module.params.get("job_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


JobHelperCustom = get_custom_class("JobHelperCustom")


class ResourceHelper(JobHelperCustom, JobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            job_id=dict(aliases=["id"], type="str"),
            migration_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="job",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
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

    module.exit_json(**result)


if __name__ == "__main__":
    main()
