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
module: oci_database_management_job
short_description: Manage a Job resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a Job resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a job to be executed on a Managed Database or Managed Database Group. Only one
      of the parameters, managedDatabaseId or managedDatabaseGroupId should be provided as
      input in CreateJobDetails resource in request body.
    - "This resource has the following action operations in the M(oci_job_actions) module: change_compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    name:
        description:
            - "The name of the job. Valid characters are uppercase or lowercase letters,
              numbers, and \\"_\\". The name of the job cannot be modified. It must be unique
              in the compartment and must begin with an alphabetic character."
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The description of the job.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the job resides.
            - Required for create using I(state=present).
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    managed_database_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group where the job has to be executed.
        type: str
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database where the job has to be executed.
        type: str
    database_sub_type:
        description:
            - The subtype of the Oracle Database where the job has to be executed. Only applicable when managedDatabaseGroupId is provided.
        type: str
        choices:
            - "CDB"
            - "PDB"
            - "NON_CDB"
    schedule_type:
        description:
            - The schedule type of the job.
            - Required for create using I(state=present).
        type: str
    job_type:
        description:
            - The type of job.
            - Required for create using I(state=present).
        type: str
        choices:
            - "SQL"
    timeout:
        description:
            - "The job timeout duration, which is expressed like \\"1h 10m 15s\\"."
        type: str
    result_location:
        description:
            - ""
        type: dict
        suboptions:
            type:
                description:
                    - The type of the job execution result location.
                type: str
                choices:
                    - "OBJECT_STORAGE"
                required: true
            namespace_name:
                description:
                    - The Object Storage namespace used for job execution result storage.
                type: str
            bucket_name:
                description:
                    - The name of the bucket used for job execution result storage.
                type: str
    sql_text:
        description:
            - The SQL text to be executed as part of the job.
        type: str
    sql_type:
        description:
            - ""
        type: str
    operation_type:
        description:
            - The SQL operation type.
            - Required for create using I(state=present).
        type: str
    user_name:
        description:
            - The database user name used to execute the SQL job. If the job is being executed on a
              Managed Database Group, then the user name should exist on all the databases in the
              group with the same password.
        type: str
    password:
        description:
            - The password for the database user name used to execute the SQL job.
        type: str
    role:
        description:
            - The role of the database user. Indicates whether the database user is a normal user or sysdba.
        type: str
    job_id:
        description:
            - The identifier of the job.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Job.
            - Use I(state=present) to create a Job.
            - Use I(state=absent) to delete a Job.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create job
  oci_database_management_job:
    name: TestJob
    compartment_id: "ocid1.tenancy.oc1..unique_ID"
    schedule_type: IMMEDIATE
    job_type: SQL
    operation_type: EXECUTE_SQL

- name: Delete job
  oci_database_management_job:
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_management_job:
    name: TestJob
    compartment_id: "ocid1.tenancy.oc1..unique_ID"
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import CreateJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "job_id"

    def get_module_resource_id(self):
        return self.module.params.get("job_id")

    def get_get_fn(self):
        return self.client.get_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job, job_id=self.module.params.get("job_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "managed_database_group_id",
            "managed_database_id",
            "name",
        ]

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

    def get_create_model_class(self):
        return CreateJobDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
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
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            name=dict(type="str"),
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            managed_database_group_id=dict(type="str"),
            managed_database_id=dict(type="str"),
            database_sub_type=dict(type="str", choices=["CDB", "PDB", "NON_CDB"]),
            schedule_type=dict(type="str"),
            job_type=dict(type="str", choices=["SQL"]),
            timeout=dict(type="str"),
            result_location=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["OBJECT_STORAGE"]),
                    namespace_name=dict(type="str"),
                    bucket_name=dict(type="str"),
                ),
            ),
            sql_text=dict(type="str"),
            sql_type=dict(type="str"),
            operation_type=dict(type="str"),
            user_name=dict(type="str"),
            password=dict(type="str", no_log=True),
            role=dict(type="str"),
            job_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
