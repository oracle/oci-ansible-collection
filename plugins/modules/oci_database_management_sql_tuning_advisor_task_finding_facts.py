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
module: oci_database_management_sql_tuning_advisor_task_finding_facts
short_description: Fetches details about one or multiple SqlTuningAdvisorTaskFinding resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SqlTuningAdvisorTaskFinding resources in Oracle Cloud Infrastructure
    - Gets an array of the details of the findings that match specific filters.
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
        required: true
    begin_exec_id:
        description:
            - The optional greater than or equal to filter on the execution ID related to a specific SQL Tuning Advisor task.
        type: int
    end_exec_id:
        description:
            - The optional less than or equal to query parameter to filter on the execution ID related to a specific SQL Tuning Advisor task.
        type: int
    search_period:
        description:
            - The search period during which the API will search for begin and end exec id, if not supplied.
              Unused if beginExecId and endExecId optional query params are both supplied.
        type: str
        choices:
            - "LAST_24HR"
            - "LAST_7DAY"
            - "LAST_31DAY"
            - "SINCE_LAST"
            - "ALL"
    finding_filter:
        description:
            - The filter used to display specific findings in the report.
        type: str
        choices:
            - "none"
            - "FINDINGS"
            - "NOFINDINGS"
            - "ERRORS"
            - "PROFILES"
            - "INDICES"
            - "STATS"
            - "RESTRUCTURE"
            - "ALTERNATIVE"
            - "AUTO_PROFILES"
            - "OTHER_PROFILES"
    stats_hash_filter:
        description:
            - The hash value of the object for the statistic finding search.
        type: str
    index_hash_filter:
        description:
            - The hash value of the index table name.
        type: str
    sort_by:
        description:
            - The possible sortBy values of an object's recommendations.
        type: str
        choices:
            - "DBTIME_BENEFIT"
            - "PARSING_SCHEMA"
            - "SQL_ID"
            - "STATS"
            - "PROFILES"
            - "SQL_BENEFIT"
            - "DATE"
            - "INDICES"
            - "RESTRUCTURE"
            - "ALTERNATIVE"
            - "MISC"
            - "ERROR"
            - "TIMEOUTS"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Descending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List sql_tuning_advisor_task_findings
  oci_database_management_sql_tuning_advisor_task_finding_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    sql_tuning_advisor_task_id: 56

    # optional
    begin_exec_id: 56
    end_exec_id: 56
    search_period: LAST_24HR
    finding_filter: none
    stats_hash_filter: stats_hash_filter_example
    index_hash_filter: index_hash_filter_example
    sort_by: DBTIME_BENEFIT
    sort_order: ASC

"""

RETURN = """
sql_tuning_advisor_task_findings:
    description:
        - List of SqlTuningAdvisorTaskFinding resources
    returned: on success
    type: complex
    contains:
        sql_tuning_advisor_task_id:
            description:
                - The unique identifier of the SQL Tuning Advisor task. This is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: int
            sample: 56
        sql_tuning_advisor_task_object_id:
            description:
                - The key of the object to which these recommendations apply.
                  This is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: int
            sample: 56
        sql_tuning_advisor_task_object_execution_id:
            description:
                - The execution id of the analyzed SQL object. This is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: int
            sample: 56
        sql_text:
            description:
                - The text of the SQL statement.
            returned: on success
            type: str
            sample: sql_text_example
        parsing_schema:
            description:
                - The parsing schema of the object.
            returned: on success
            type: str
            sample: parsing_schema_example
        sql_key:
            description:
                - The unique key of this SQL statement.
            returned: on success
            type: str
            sample: sql_key_example
        db_time_benefit:
            description:
                - The time benefit (in seconds) for the highest-rated finding for this object.
            returned: on success
            type: float
            sample: 3.4
        per_execution_percentage:
            description:
                - The per-execution percentage benefit.
            returned: on success
            type: int
            sample: 56
        is_stats_finding_present:
            description:
                - Indicates whether a statistics recommendation was reported for this SQL statement.
            returned: on success
            type: bool
            sample: true
        is_sql_profile_finding_present:
            description:
                - Indicates whether a SQL Profile recommendation was reported for this SQL statement.
            returned: on success
            type: bool
            sample: true
        is_sql_profile_finding_implemented:
            description:
                - Indicates whether a SQL Profile recommendation has been implemented for this SQL statement.
            returned: on success
            type: bool
            sample: true
        is_index_finding_present:
            description:
                - Indicates whether an index recommendation was reported for this SQL statement.
            returned: on success
            type: bool
            sample: true
        is_restructure_sql_finding_present:
            description:
                - Indicates whether a restructure SQL recommendation was reported for this SQL statement.
            returned: on success
            type: bool
            sample: true
        is_alternative_plan_finding_present:
            description:
                - Indicates whether an alternative execution plan was reported for this SQL statement.
            returned: on success
            type: bool
            sample: true
        is_miscellaneous_finding_present:
            description:
                - Indicates whether a miscellaneous finding was reported for this SQL statement.
            returned: on success
            type: bool
            sample: true
        is_error_finding_present:
            description:
                - Indicates whether there is an error in this SQL statement.
            returned: on success
            type: bool
            sample: true
        is_timeout_finding_present:
            description:
                - Indicates whether the task timed out.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "sql_tuning_advisor_task_id": 56,
        "sql_tuning_advisor_task_object_id": 56,
        "sql_tuning_advisor_task_object_execution_id": 56,
        "sql_text": "sql_text_example",
        "parsing_schema": "parsing_schema_example",
        "sql_key": "sql_key_example",
        "db_time_benefit": 3.4,
        "per_execution_percentage": 56,
        "is_stats_finding_present": true,
        "is_sql_profile_finding_present": true,
        "is_sql_profile_finding_implemented": true,
        "is_index_finding_present": true,
        "is_restructure_sql_finding_present": true,
        "is_alternative_plan_finding_present": true,
        "is_miscellaneous_finding_present": true,
        "is_error_finding_present": true,
        "is_timeout_finding_present": true
    }]
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


class SqlTuningAdvisorTaskFindingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
            "sql_tuning_advisor_task_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "begin_exec_id",
            "end_exec_id",
            "search_period",
            "finding_filter",
            "stats_hash_filter",
            "index_hash_filter",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sql_tuning_advisor_task_findings,
            managed_database_id=self.module.params.get("managed_database_id"),
            sql_tuning_advisor_task_id=self.module.params.get(
                "sql_tuning_advisor_task_id"
            ),
            **optional_kwargs
        )


SqlTuningAdvisorTaskFindingFactsHelperCustom = get_custom_class(
    "SqlTuningAdvisorTaskFindingFactsHelperCustom"
)


class ResourceFactsHelper(
    SqlTuningAdvisorTaskFindingFactsHelperCustom,
    SqlTuningAdvisorTaskFindingFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            sql_tuning_advisor_task_id=dict(type="int", required=True),
            begin_exec_id=dict(type="int"),
            end_exec_id=dict(type="int"),
            search_period=dict(
                type="str",
                choices=["LAST_24HR", "LAST_7DAY", "LAST_31DAY", "SINCE_LAST", "ALL"],
            ),
            finding_filter=dict(
                type="str",
                choices=[
                    "none",
                    "FINDINGS",
                    "NOFINDINGS",
                    "ERRORS",
                    "PROFILES",
                    "INDICES",
                    "STATS",
                    "RESTRUCTURE",
                    "ALTERNATIVE",
                    "AUTO_PROFILES",
                    "OTHER_PROFILES",
                ],
            ),
            stats_hash_filter=dict(type="str"),
            index_hash_filter=dict(type="str"),
            sort_by=dict(
                type="str",
                choices=[
                    "DBTIME_BENEFIT",
                    "PARSING_SCHEMA",
                    "SQL_ID",
                    "STATS",
                    "PROFILES",
                    "SQL_BENEFIT",
                    "DATE",
                    "INDICES",
                    "RESTRUCTURE",
                    "ALTERNATIVE",
                    "MISC",
                    "ERROR",
                    "TIMEOUTS",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_tuning_advisor_task_finding",
        service_client_class=SqlTuningClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_tuning_advisor_task_findings=result)


if __name__ == "__main__":
    main()
