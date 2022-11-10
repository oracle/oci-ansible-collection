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
module: oci_database_management_sql_tuning_advisor_task_summary_report_facts
short_description: Fetches details about a SqlTuningAdvisorTaskSummaryReport resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SqlTuningAdvisorTaskSummaryReport resource in Oracle Cloud Infrastructure
    - Gets the summary report for the specified SQL Tuning Advisor task.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    sql_tuning_advisor_task_id:
        description:
            - The SQL tuning task identifier. This is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: int
        aliases: ["id"]
        required: true
    search_period:
        description:
            - How far back the API will search for begin and end exec id. Unused if neither exec ids nor time filter query params are supplied. This is
              applicable only for Auto SQL Tuning tasks.
        type: str
        choices:
            - "LAST_24HR"
            - "LAST_7DAY"
            - "LAST_31DAY"
            - "SINCE_LAST"
            - "ALL"
    time_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to query parameter to filter the timestamp. This is applicable only for Auto SQL Tuning tasks.
        type: str
    time_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the timestamp. This is applicable only for Auto SQL Tuning tasks.
        type: str
    begin_exec_id_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task. This is applicable only for Auto
              SQL Tuning tasks.
        type: int
    end_exec_id_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task. This is applicable
              only for Auto SQL Tuning tasks.
        type: int
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific sql_tuning_advisor_task_summary_report
  oci_database_management_sql_tuning_advisor_task_summary_report_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    sql_tuning_advisor_task_id: 56

    # optional
    search_period: LAST_24HR
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    begin_exec_id_greater_than_or_equal_to: 56
    end_exec_id_less_than_or_equal_to: 56

"""

RETURN = """
sql_tuning_advisor_task_summary_report:
    description:
        - SqlTuningAdvisorTaskSummaryReport resource
    returned: on success
    type: complex
    contains:
        task_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The ID of the SQL Tuning Advisor task. This is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    returned: on success
                    type: int
                    sample: 56
                name:
                    description:
                        - The name of the SQL Tuning Advisor task.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - The description of the SQL Tuning Advisor task. This is not defined for Auto SQL Tuning tasks.
                    returned: on success
                    type: str
                    sample: description_example
                owner:
                    description:
                        - The owner of the SQL Tuning Advisor task.
                    returned: on success
                    type: str
                    sample: owner_example
                status:
                    description:
                        - The status of the SQL Tuning Advisor task. This is not defined for Auto SQL Tuning tasks.
                    returned: on success
                    type: str
                    sample: COMPLETED
                time_started:
                    description:
                        - The start time of the task execution.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_ended:
                    description:
                        - The end time of the task execution.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                running_time:
                    description:
                        - The total running time in seconds. This is not defined for Auto SQL Tuning tasks.
                    returned: on success
                    type: int
                    sample: 56
        statistics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                statement_counts:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        distinct_sql:
                            description:
                                - The number of distinct SQL statements.
                            returned: on success
                            type: int
                            sample: 56
                        total_sql:
                            description:
                                - The total number of SQL statements.
                            returned: on success
                            type: int
                            sample: 56
                        finding_count:
                            description:
                                - The number of distinct SQL statements with findings.
                            returned: on success
                            type: int
                            sample: 56
                        error_count:
                            description:
                                - The number of distinct SQL statements with errors.
                            returned: on success
                            type: int
                            sample: 56
                finding_counts:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        recommended_sql_profile:
                            description:
                                - The number of distinct SQL statements with recommended SQL profiles.
                            returned: on success
                            type: int
                            sample: 56
                        implemented_sql_profile:
                            description:
                                - The number of distinct SQL statements with implemented SQL profiles.
                            returned: on success
                            type: int
                            sample: 56
                        index:
                            description:
                                - The number of distinct SQL statements with index recommendations.
                            returned: on success
                            type: int
                            sample: 56
                        restructure:
                            description:
                                - The number of distinct SQL statements with restructured SQL recommendations.
                            returned: on success
                            type: int
                            sample: 56
                        statistics:
                            description:
                                - The number of distinct SQL statements with stale or missing optimizer statistics recommendations.
                            returned: on success
                            type: int
                            sample: 56
                        alternate_plan:
                            description:
                                - The number of distinct SQL statements with alternative plan recommendations.
                            returned: on success
                            type: int
                            sample: 56
                finding_benefits:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        db_time_before_recommended:
                            description:
                                - The actual database time of the SQL statements for which SQL Tuning Advisor recommendations are not implemented.
                            returned: on success
                            type: int
                            sample: 56
                        db_time_after_recommended:
                            description:
                                - The estimated database time of the above SQL statements, if SQL Tuning Advisor recommendations are implemented.
                            returned: on success
                            type: int
                            sample: 56
                        db_time_after_implemented:
                            description:
                                - The actual database time of the SQL statements for which SQL Tuning Advisor recommendations are implemented.
                            returned: on success
                            type: int
                            sample: 56
                        db_time_before_implemented:
                            description:
                                - The actual database time of the above SQL statements, before SQL Tuning Advisor recommendations are implemented.
                            returned: on success
                            type: int
                            sample: 56
        object_stat_findings:
            description:
                - The list of object findings related to statistics.
            returned: on success
            type: complex
            contains:
                object_hash_value:
                    description:
                        - Numerical representation of the object.
                    returned: on success
                    type: int
                    sample: 56
                object_name:
                    description:
                        - Name of the object.
                    returned: on success
                    type: str
                    sample: object_name_example
                object_type:
                    description:
                        - Type of the object.
                    returned: on success
                    type: str
                    sample: object_type_example
                schema:
                    description:
                        - Schema of the object.
                    returned: on success
                    type: str
                    sample: schema_example
                problem_type:
                    description:
                        - Type of statistics problem related to the object.
                    returned: on success
                    type: str
                    sample: MISSING
                reference_count:
                    description:
                        - The number of the times the object is referenced within the SQL Tuning advisor task findings.
                    returned: on success
                    type: int
                    sample: 56
        index_findings:
            description:
                - The list of object findings related to indexes.
            returned: on success
            type: complex
            contains:
                index_hash_value:
                    description:
                        - Numerical representation of the index.
                    returned: on success
                    type: int
                    sample: 56
                index_name:
                    description:
                        - Name of the index.
                    returned: on success
                    type: str
                    sample: index_name_example
                table_name:
                    description:
                        - Table's name related to the index.
                    returned: on success
                    type: str
                    sample: table_name_example
                schema:
                    description:
                        - Schema related to the index.
                    returned: on success
                    type: str
                    sample: schema_example
                reference_count:
                    description:
                        - The number of times the index is referenced within the SQL Tuning advisor task findings.
                    returned: on success
                    type: int
                    sample: 56
                index_columns:
                    description:
                        - Columns of the index.
                    returned: on success
                    type: list
                    sample: []
    sample: {
        "task_info": {
            "id": 56,
            "name": "name_example",
            "description": "description_example",
            "owner": "owner_example",
            "status": "COMPLETED",
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_ended": "2013-10-20T19:20:30+01:00",
            "running_time": 56
        },
        "statistics": {
            "statement_counts": {
                "distinct_sql": 56,
                "total_sql": 56,
                "finding_count": 56,
                "error_count": 56
            },
            "finding_counts": {
                "recommended_sql_profile": 56,
                "implemented_sql_profile": 56,
                "index": 56,
                "restructure": 56,
                "statistics": 56,
                "alternate_plan": 56
            },
            "finding_benefits": {
                "db_time_before_recommended": 56,
                "db_time_after_recommended": 56,
                "db_time_after_implemented": 56,
                "db_time_before_implemented": 56
            }
        },
        "object_stat_findings": [{
            "object_hash_value": 56,
            "object_name": "object_name_example",
            "object_type": "object_type_example",
            "schema": "schema_example",
            "problem_type": "MISSING",
            "reference_count": 56
        }],
        "index_findings": [{
            "index_hash_value": 56,
            "index_name": "index_name_example",
            "table_name": "table_name_example",
            "schema": "schema_example",
            "reference_count": 56,
            "index_columns": []
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import SqlTuningClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SqlTuningAdvisorTaskSummaryReportFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "sql_tuning_advisor_task_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "search_period",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "begin_exec_id_greater_than_or_equal_to",
            "end_exec_id_less_than_or_equal_to",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_sql_tuning_advisor_task_summary_report,
            managed_database_id=self.module.params.get("managed_database_id"),
            sql_tuning_advisor_task_id=self.module.params.get(
                "sql_tuning_advisor_task_id"
            ),
            **optional_kwargs
        )


SqlTuningAdvisorTaskSummaryReportFactsHelperCustom = get_custom_class(
    "SqlTuningAdvisorTaskSummaryReportFactsHelperCustom"
)


class ResourceFactsHelper(
    SqlTuningAdvisorTaskSummaryReportFactsHelperCustom,
    SqlTuningAdvisorTaskSummaryReportFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            sql_tuning_advisor_task_id=dict(aliases=["id"], type="int", required=True),
            search_period=dict(
                type="str",
                choices=["LAST_24HR", "LAST_7DAY", "LAST_31DAY", "SINCE_LAST", "ALL"],
            ),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            begin_exec_id_greater_than_or_equal_to=dict(type="int"),
            end_exec_id_less_than_or_equal_to=dict(type="int"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_tuning_advisor_task_summary_report",
        service_client_class=SqlTuningClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_tuning_advisor_task_summary_report=result)


if __name__ == "__main__":
    main()
