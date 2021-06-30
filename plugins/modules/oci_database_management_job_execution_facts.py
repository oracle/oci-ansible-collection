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
module: oci_database_management_job_execution_facts
short_description: Fetches details about one or multiple JobExecution resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple JobExecution resources in Oracle Cloud Infrastructure
    - Gets the job execution for a specific ID or the list of job executions for a job, Managed Database or Managed Database Group
      in a specific compartment. Only one of the parameters, ID, jobId, managedDatabaseId or managedDatabaseGroupId should be provided.
      If none of these parameters is provided, all the job executions in the compartment are listed. Job executions can also be filtered
      based on the name and status parameters.
    - If I(job_execution_id) is specified, the details of a single JobExecution will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    job_execution_id:
        description:
            - The identifier of the job execution.
            - Required to get a specific job_execution.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple job_executions.
        type: str
    job_id:
        description:
            - The identifier of the job.
        type: str
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
    managed_database_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group.
        type: str
    status:
        description:
            - The status of the job execution.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire name.
        type: str
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
- name: List job_executions
  oci_database_management_job_execution_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific job_execution
  oci_database_management_job_execution_facts:
    job_execution_id: "ocid1.jobexecution.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
job_executions:
    description:
        - List of JobExecution resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The identifier of the job execution.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the job execution.
            returned: on success
            type: string
            sample: name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the parent job resides.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        managed_database_group_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database Group where the parent job has to
                  be executed.
            returned: on success
            type: string
            sample: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"
        managed_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database associated with the job execution.
            returned: on success
            type: string
            sample: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
        managed_database_name:
            description:
                - The name of the Managed Database associated with the job execution.
            returned: on success
            type: string
            sample: managed_database_name_example
        job_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the parent job.
            returned: on success
            type: string
            sample: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
        job_name:
            description:
                - The name of the parent job.
            returned: on success
            type: string
            sample: job_name_example
        job_run_id:
            description:
                - The identifier of the associated job run.
            returned: on success
            type: string
            sample: "ocid1.jobrun.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The status of the job execution.
            returned: on success
            type: string
            sample: SUCCEEDED
        error_message:
            description:
                - The error message that is returned if the job execution fails. Null is returned if the job is
                  still running or if the job execution is successful.
            returned: on success
            type: string
            sample: error_message_example
        result_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of job execution result.
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
                object_name:
                    description:
                        - The name of the object containing the job execution result.
                    returned: on success
                    type: string
                    sample: object_name_example
                row_count:
                    description:
                        - The number of rows returned in the result. Only applicable for QUERY SqlType.
                    returned: on success
                    type: int
                    sample: 56
        time_created:
            description:
                - The date and time when the job execution was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_completed:
            description:
                - The date and time when the job execution completed.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_database_group_id": "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_database_id": "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_database_name": "managed_database_name_example",
        "job_id": "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx",
        "job_name": "job_name_example",
        "job_run_id": "ocid1.jobrun.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "SUCCEEDED",
        "error_message": "error_message_example",
        "result_details": {
            "type": "OBJECT_STORAGE",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example",
            "row_count": 56
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_completed": "2013-10-20T19:20:30+01:00"
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


class JobExecutionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "job_execution_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_job_execution,
            job_execution_id=self.module.params.get("job_execution_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "job_id",
            "managed_database_id",
            "managed_database_group_id",
            "status",
            "name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_job_executions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


JobExecutionFactsHelperCustom = get_custom_class("JobExecutionFactsHelperCustom")


class ResourceFactsHelper(JobExecutionFactsHelperCustom, JobExecutionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            job_execution_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            job_id=dict(type="str"),
            managed_database_id=dict(type="str"),
            managed_database_group_id=dict(type="str"),
            status=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="job_execution",
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

    module.exit_json(job_executions=result)


if __name__ == "__main__":
    main()
