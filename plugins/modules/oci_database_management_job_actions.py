#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_database_management_job_actions
short_description: Perform actions on a Job resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Job resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a job.
version_added: "2.9"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The identifier of the job.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
              compartment to which the job should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Job.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on job
  oci_database_management_job_actions:
    compartment_id: "compartmentId"
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
    action: "change_compartment"

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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the job.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the job resides.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The display name of the job.
            returned: on success
            type: string
            sample: name_example
        description:
            description:
                - The description of the job.
            returned: on success
            type: string
            sample: description_example
        managed_database_group_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group where the job has to be
                  executed.
            returned: on success
            type: string
            sample: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"
        managed_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database where the job has to be executed.
            returned: on success
            type: string
            sample: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
        managed_databases_details:
            description:
                - The details of the Managed Databases where the job has to be executed.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
                    returned: on success
                    type: string
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the Managed Database.
                    returned: on success
                    type: string
                    sample: name_example
        database_sub_type:
            description:
                - The subtype of the Oracle Database where the job has to be executed. Applicable only when managedDatabaseGroupId is provided.
            returned: on success
            type: string
            sample: CDB
        schedule_type:
            description:
                - The schedule type of the job.
            returned: on success
            type: string
            sample: IMMEDIATE
        job_type:
            description:
                - The type of job.
            returned: on success
            type: string
            sample: SQL
        lifecycle_state:
            description:
                - The lifecycle state of the job.
            returned: on success
            type: string
            sample: ACTIVE
        timeout:
            description:
                - "The job timeout duration, which is expressed like \\"1h 10m 15s\\"."
            returned: on success
            type: string
            sample: timeout_example
        result_location:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of the job execution result location.
                    returned: on success
                    type: string
                    sample: OBJECT_STORAGE
                namespace_name:
                    description:
                        - The Object Storage namespace used for job execution result storage.
                    returned: on success
                    type: string
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The name of the bucket used for job execution result storage.
                    returned: on success
                    type: string
                    sample: bucket_name_example
        submission_error_message:
            description:
                - The error message that is returned if the job submission fails. Null is returned in all other scenarios.
            returned: on success
            type: string
            sample: submission_error_message_example
        time_created:
            description:
                - The date and time when the job was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The date and time when the job was last updated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        sql_type:
            description:
                - The type of SQL. This is a mandatory field for the EXECUTE_SQL operationType.
            returned: on success
            type: string
            sample: QUERY
        sql_text:
            description:
                - The SQL text to be executed in the job. This is a mandatory field for the EXECUTE_SQL operationType.
            returned: on success
            type: string
            sample: sql_text_example
        operation_type:
            description:
                - The SQL operation type.
            returned: on success
            type: string
            sample: EXECUTE_SQL
        user_name:
            description:
                - The database user name used to execute the SQL job. If the job is being executed on a Managed Database Group,
                  then the user name should exist on all the databases in the group with the same password.
            returned: on success
            type: string
            sample: user_name_example
        role:
            description:
                - The role of the database user. Indicates whether the database user is a normal user or sysdba.
            returned: on success
            type: string
            sample: NORMAL
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "managed_database_group_id": "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_database_id": "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_databases_details": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example"
        }],
        "database_sub_type": "CDB",
        "schedule_type": "IMMEDIATE",
        "job_type": "SQL",
        "lifecycle_state": "ACTIVE",
        "timeout": "timeout_example",
        "result_location": {
            "type": "OBJECT_STORAGE",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example"
        },
        "submission_error_message": "submission_error_message_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "sql_type": "QUERY",
        "sql_text": "sql_text_example",
        "operation_type": "EXECUTE_SQL",
        "user_name": "user_name_example",
        "role": "NORMAL"
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
    from oci.database_management import DbManagementClient
    from oci.database_management.models import ChangeJobCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeJobCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_job_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                job_id=self.module.params.get("job_id"),
                change_job_compartment_details=action_details,
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


JobActionsHelperCustom = get_custom_class("JobActionsHelperCustom")


class ResourceHelper(JobActionsHelperCustom, JobActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            job_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="job",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
