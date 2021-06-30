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
module: oci_database_management_job_facts
short_description: Fetches details about one or multiple Job resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Job resources in Oracle Cloud Infrastructure
    - Gets the job for a specific ID or the list of jobs for a Managed Database or Managed Database Group
      in a specific compartment. Only one of the parameters, ID, managedDatabaseId or managedDatabaseGroupId,
      should be provided. If none of these parameters is provided, all the jobs in the compartment are listed.
      Jobs can also be filtered based on the name and lifecycleState parameters.
    - If I(job_id) is specified, the details of a single Job will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The identifier of the job.
            - Required to get a specific job.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple jobs.
        type: str
    managed_database_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
        type: str
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire name.
        type: str
    lifecycle_state:
        description:
            - The lifecycle state of the job.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
    sort_by:
        description:
            - The field to sort information by. Only one sortOrder can be used. The default sort order
              for 'TIMECREATED' is descending and the default sort order for 'NAME' is ascending.
              The 'NAME' sort order is case-sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List jobs
  oci_database_management_job_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific job
  oci_database_management_job_facts:
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
jobs:
    description:
        - List of Job resources
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

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
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job, job_id=self.module.params.get("job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "managed_database_group_id",
            "managed_database_id",
            "name",
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
            self.client.list_jobs,
            compartment_id=self.module.params.get("compartment_id"),
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
            compartment_id=dict(type="str"),
            managed_database_group_id=dict(type="str"),
            managed_database_id=dict(type="str"),
            name=dict(type="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="job",
        service_client_class=DbManagementClient,
        namespace="database_management",
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
