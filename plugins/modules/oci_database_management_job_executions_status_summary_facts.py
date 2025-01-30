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
module: oci_database_management_job_executions_status_summary_facts
short_description: Fetches details about one or multiple JobExecutionsStatusSummary resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple JobExecutionsStatusSummary resources in Oracle Cloud Infrastructure
    - Gets the number of job executions grouped by status for a job, Managed Database, or Database Group in a specific compartment. Only one of the parameters,
      jobId, managedDatabaseId, or managedDatabaseGroupId should be provided.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    start_time:
        description:
            - "The start time of the time range to retrieve the status summary of job executions
              in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
        type: str
        required: true
    end_time:
        description:
            - "The end time of the time range to retrieve the status summary of job executions
              in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
        type: str
        required: true
    id:
        description:
            - The identifier of the resource.
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
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List job_executions_status_summaries
  oci_database_management_job_executions_status_summary_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    start_time: start_time_example
    end_time: end_time_example

    # optional
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    managed_database_group_id: "ocid1.manageddatabasegroup.oc1..xxxxxxEXAMPLExxxxxx"
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
job_executions_status_summaries:
    description:
        - List of JobExecutionsStatusSummary resources
    returned: on success
    type: complex
    contains:
        status:
            description:
                - The status of the job execution.
            returned: on success
            type: str
            sample: SUCCEEDED
        count:
            description:
                - The number of job executions of a particular status.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "status": "SUCCEEDED",
        "count": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class JobExecutionsStatusSummaryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "start_time",
            "end_time",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "id",
            "managed_database_group_id",
            "managed_database_id",
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
            self.client.summarize_job_executions_statuses,
            compartment_id=self.module.params.get("compartment_id"),
            start_time=self.module.params.get("start_time"),
            end_time=self.module.params.get("end_time"),
            **optional_kwargs
        )


JobExecutionsStatusSummaryFactsHelperCustom = get_custom_class(
    "JobExecutionsStatusSummaryFactsHelperCustom"
)


class ResourceFactsHelper(
    JobExecutionsStatusSummaryFactsHelperCustom,
    JobExecutionsStatusSummaryFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            start_time=dict(type="str", required=True),
            end_time=dict(type="str", required=True),
            id=dict(type="str"),
            managed_database_group_id=dict(type="str"),
            managed_database_id=dict(type="str"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="job_executions_status_summary",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(job_executions_status_summaries=result)


if __name__ == "__main__":
    main()
