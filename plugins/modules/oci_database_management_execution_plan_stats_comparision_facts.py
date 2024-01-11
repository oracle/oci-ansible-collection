#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_management_execution_plan_stats_comparision_facts
short_description: Fetches details about a ExecutionPlanStatsComparision resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ExecutionPlanStatsComparision resource in Oracle Cloud Infrastructure
    - Retrieves a comparison of the existing SQL execution plan and a new plan.
      A SQL tuning task may suggest a new execution plan for a SQL,
      and this API retrieves the comparison report of the statistics of the two plans.
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
    execution_id:
        description:
            - The execution ID for an execution of a SQL tuning task. This is not the
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: int
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific execution_plan_stats_comparision
  oci_database_management_execution_plan_stats_comparision_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    sql_tuning_advisor_task_id: 56
    sql_object_id: 56
    execution_id: 56

"""

RETURN = """
execution_plan_stats_comparision:
    description:
        - ExecutionPlanStatsComparision resource
    returned: on success
    type: complex
    contains:
        original:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                plan_type:
                    description:
                        - The type of the original or modified plan with profile, index, and so on.
                    returned: on success
                    type: str
                    sample: plan_type_example
                plan_stats:
                    description:
                        - A map contains the statistics for the SQL execution using the plan.
                          The key of the map is the metric's name. The value of the map is the metric's value.
                    returned: on success
                    type: dict
                    sample: {}
                plan_status:
                    description:
                        - The status of the execution using the plan.
                    returned: on success
                    type: str
                    sample: COMPLETE
        modified:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                plan_type:
                    description:
                        - The type of the original or modified plan with profile, index, and so on.
                    returned: on success
                    type: str
                    sample: plan_type_example
                plan_stats:
                    description:
                        - A map contains the statistics for the SQL execution using the plan.
                          The key of the map is the metric's name. The value of the map is the metric's value.
                    returned: on success
                    type: dict
                    sample: {}
                plan_status:
                    description:
                        - The status of the execution using the plan.
                    returned: on success
                    type: str
                    sample: COMPLETE
    sample: {
        "original": {
            "plan_type": "plan_type_example",
            "plan_stats": {},
            "plan_status": "COMPLETE"
        },
        "modified": {
            "plan_type": "plan_type_example",
            "plan_stats": {},
            "plan_status": "COMPLETE"
        }
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


class ExecutionPlanStatsComparisionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "sql_tuning_advisor_task_id",
            "sql_object_id",
            "execution_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_execution_plan_stats_comparision,
            managed_database_id=self.module.params.get("managed_database_id"),
            sql_tuning_advisor_task_id=self.module.params.get(
                "sql_tuning_advisor_task_id"
            ),
            sql_object_id=self.module.params.get("sql_object_id"),
            execution_id=self.module.params.get("execution_id"),
        )


ExecutionPlanStatsComparisionFactsHelperCustom = get_custom_class(
    "ExecutionPlanStatsComparisionFactsHelperCustom"
)


class ResourceFactsHelper(
    ExecutionPlanStatsComparisionFactsHelperCustom,
    ExecutionPlanStatsComparisionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            sql_tuning_advisor_task_id=dict(aliases=["id"], type="int", required=True),
            sql_object_id=dict(type="int", required=True),
            execution_id=dict(type="int", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="execution_plan_stats_comparision",
        service_client_class=SqlTuningClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(execution_plan_stats_comparision=result)


if __name__ == "__main__":
    main()
