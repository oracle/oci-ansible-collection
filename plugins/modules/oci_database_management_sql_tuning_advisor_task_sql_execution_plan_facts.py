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
module: oci_database_management_sql_tuning_advisor_task_sql_execution_plan_facts
short_description: Fetches details about a SqlTuningAdvisorTaskSqlExecutionPlan resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SqlTuningAdvisorTaskSqlExecutionPlan resource in Oracle Cloud Infrastructure
    - Retrieves a SQL execution plan for the SQL being tuned.
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
    sql_object_id:
        description:
            - The SQL object ID for the SQL tuning task. This is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: int
        required: true
    attribute:
        description:
            - The attribute of the SQL execution plan.
        type: str
        choices:
            - "ORIGINAL"
            - "ORIGINAL_WITH_ADJUSTED_COST"
            - "USING_SQL_PROFILE"
            - "USING_NEW_INDICES"
            - "USING_PARALLEL_EXECUTION"
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific sql_tuning_advisor_task_sql_execution_plan
  oci_database_management_sql_tuning_advisor_task_sql_execution_plan_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    sql_tuning_advisor_task_id: 56
    sql_object_id: 56
    attribute: ORIGINAL

"""

RETURN = """
sql_tuning_advisor_task_sql_execution_plan:
    description:
        - SqlTuningAdvisorTaskSqlExecutionPlan resource
    returned: on success
    type: complex
    contains:
        plan:
            description:
                - A SQL execution plan as a list of steps.
            returned: on success
            type: complex
            contains:
                plan_hash_value:
                    description:
                        - The numerical representation of the SQL execution plan.
                    returned: on success
                    type: int
                    sample: 56
                step_id:
                    description:
                        - The identification number of a step in the SQL execution plan. This is unique within the SQL execution plan.
                          This is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    returned: on success
                    type: int
                    sample: 56
                parent_step_id:
                    description:
                        - The ID of the next step that operates on the results of this step.
                          This is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    returned: on success
                    type: int
                    sample: 56
                position:
                    description:
                        - The order of processing for steps with the same parent ID.
                    returned: on success
                    type: int
                    sample: 56
                operation:
                    description:
                        - The name of the operation performed at this step.
                    returned: on success
                    type: str
                    sample: operation_example
                options:
                    description:
                        - The options used for the operation performed at this step.
                    returned: on success
                    type: str
                    sample: options_example
                optimizer_mode:
                    description:
                        - The current mode of the optimizer, such as all_rows, first_rows_n (where n = 1, 10, 100, 1000, and so on).
                    returned: on success
                    type: str
                    sample: optimizer_mode_example
                cost:
                    description:
                        - The cost of the current operation estimated by the cost-based optimizer (CBO).
                    returned: on success
                    type: float
                    sample: 1.2
                cardinality:
                    description:
                        - The number of rows returned by the current operation (estimated by the CBO).
                    returned: on success
                    type: int
                    sample: 56
                bytes:
                    description:
                        - The number of bytes returned by the current operation.
                    returned: on success
                    type: int
                    sample: 56
                cpu_cost:
                    description:
                        - The CPU cost of the current operation.
                    returned: on success
                    type: float
                    sample: 1.2
                io_cost:
                    description:
                        - The I/O cost of the current operation.
                    returned: on success
                    type: float
                    sample: 1.2
                temp_space:
                    description:
                        - The temporary space usage (in bytes) of the operation (sort or hash-join) as estimated by the CBO.
                    returned: on success
                    type: int
                    sample: 56
                time:
                    description:
                        - The elapsed time (in seconds) of the operation as estimated by the CBO.
                    returned: on success
                    type: int
                    sample: 56
                object_node:
                    description:
                        - The name of the database link used to reference the object.
                    returned: on success
                    type: str
                    sample: object_node_example
                object_owner:
                    description:
                        - The owner of the object.
                    returned: on success
                    type: str
                    sample: object_owner_example
                object_name:
                    description:
                        - The name of the object.
                    returned: on success
                    type: str
                    sample: object_name_example
                object_position:
                    description:
                        - The numbered position of the object name in the original SQL statement.
                    returned: on success
                    type: int
                    sample: 56
                object_type:
                    description:
                        - The descriptive modifier that further describes the type of object.
                    returned: on success
                    type: str
                    sample: object_type_example
                partition_start:
                    description:
                        - A step may get data from a range of partitions of a partitioned object, such as table or index,
                          based on predicates and sorting order. The partionStart is the starting partition of the range.
                          The partitionStop is the ending partition of the range.
                    returned: on success
                    type: str
                    sample: partition_start_example
                partition_stop:
                    description:
                        - A step may get data from a range of partitions of a partitioned object, such as table or index,
                          based on predicates and sorting order. The partionStart is the starting partition of the range.
                          The partitionStop is the ending partition of the range.
                    returned: on success
                    type: str
                    sample: partition_stop_example
                partition_id:
                    description:
                        - The ID of the step in the execution plan that has computed the pair of values of partitionStart and partitionStop.
                    returned: on success
                    type: int
                    sample: 56
                remarks:
                    description:
                        - The place for comments that can be added to the steps of the execution plan.
                    returned: on success
                    type: str
                    sample: remarks_example
                number_of_search_column:
                    description:
                        - Number of index columns with start and stop keys (that is, the number of columns with matching predicates).
                    returned: on success
                    type: int
                    sample: 56
                other:
                    description:
                        - Information about parallel execution servers and parallel queries
                    returned: on success
                    type: str
                    sample: other_example
                other_tag:
                    description:
                        - Describes the function of the SQL text in the OTHER column.
                    returned: on success
                    type: str
                    sample: other_tag_example
                attribute:
                    description:
                        - The text string identifying the type of execution plan.
                    returned: on success
                    type: str
                    sample: attribute_example
                access_predicates:
                    description:
                        - The predicates used to locate rows in an access structure. For example,
                          start or stop predicates for an index range scan.
                    returned: on success
                    type: str
                    sample: access_predicates_example
                filter_predicates:
                    description:
                        - The predicates used to filter rows before producing them.
                    returned: on success
                    type: str
                    sample: filter_predicates_example
    sample: {
        "plan": [{
            "plan_hash_value": 56,
            "step_id": 56,
            "parent_step_id": 56,
            "position": 56,
            "operation": "operation_example",
            "options": "options_example",
            "optimizer_mode": "optimizer_mode_example",
            "cost": 1.2,
            "cardinality": 56,
            "bytes": 56,
            "cpu_cost": 1.2,
            "io_cost": 1.2,
            "temp_space": 56,
            "time": 56,
            "object_node": "object_node_example",
            "object_owner": "object_owner_example",
            "object_name": "object_name_example",
            "object_position": 56,
            "object_type": "object_type_example",
            "partition_start": "partition_start_example",
            "partition_stop": "partition_stop_example",
            "partition_id": 56,
            "remarks": "remarks_example",
            "number_of_search_column": 56,
            "other": "other_example",
            "other_tag": "other_tag_example",
            "attribute": "attribute_example",
            "access_predicates": "access_predicates_example",
            "filter_predicates": "filter_predicates_example"
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


class SqlTuningAdvisorTaskSqlExecutionPlanFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "sql_tuning_advisor_task_id",
            "sql_object_id",
            "attribute",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sql_execution_plan,
            managed_database_id=self.module.params.get("managed_database_id"),
            sql_tuning_advisor_task_id=self.module.params.get(
                "sql_tuning_advisor_task_id"
            ),
            sql_object_id=self.module.params.get("sql_object_id"),
            attribute=self.module.params.get("attribute"),
        )


SqlTuningAdvisorTaskSqlExecutionPlanFactsHelperCustom = get_custom_class(
    "SqlTuningAdvisorTaskSqlExecutionPlanFactsHelperCustom"
)


class ResourceFactsHelper(
    SqlTuningAdvisorTaskSqlExecutionPlanFactsHelperCustom,
    SqlTuningAdvisorTaskSqlExecutionPlanFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            sql_tuning_advisor_task_id=dict(aliases=["id"], type="int", required=True),
            sql_object_id=dict(type="int", required=True),
            attribute=dict(
                type="str",
                required=True,
                choices=[
                    "ORIGINAL",
                    "ORIGINAL_WITH_ADJUSTED_COST",
                    "USING_SQL_PROFILE",
                    "USING_NEW_INDICES",
                    "USING_PARALLEL_EXECUTION",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_tuning_advisor_task_sql_execution_plan",
        service_client_class=SqlTuningClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_tuning_advisor_task_sql_execution_plan=result)


if __name__ == "__main__":
    main()
