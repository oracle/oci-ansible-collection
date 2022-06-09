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
module: oci_database_management_sql_tuning_advisor_task_recommendation_facts
short_description: Fetches details about one or multiple SqlTuningAdvisorTaskRecommendation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SqlTuningAdvisorTaskRecommendation resources in Oracle Cloud Infrastructure
    - Gets the findings and possible actions for a given object in a SQL tuning task.
      The task ID and object ID are used to retrieve the findings and recommendations.
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
    sort_by:
        description:
            - The possible sortBy values of an object's recommendations.
        type: str
        choices:
            - "RECOMMENDATION_TYPE"
            - "BENEFIT"
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
- name: List sql_tuning_advisor_task_recommendations
  oci_database_management_sql_tuning_advisor_task_recommendation_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    sql_tuning_advisor_task_id: 56
    sql_object_id: 56
    execution_id: 56

    # optional
    sort_by: RECOMMENDATION_TYPE
    sort_order: ASC

"""

RETURN = """
sql_tuning_advisor_task_recommendations:
    description:
        - List of SqlTuningAdvisorTaskRecommendation resources
    returned: on success
    type: complex
    contains:
        sql_tuning_advisor_task_id:
            description:
                - The unique identifier of the task. This is not the L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: int
            sample: 56
        sql_tuning_advisor_task_object_id:
            description:
                - The key of the object to which these recommendations apply. This is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: int
            sample: 56
        recommendation_key:
            description:
                - The unique identifier of the recommendation in the scope of the task.
            returned: on success
            type: int
            sample: 56
        recommendation_type:
            description:
                - Type of recommendation.
            returned: on success
            type: str
            sample: STATISTICS
        finding:
            description:
                - Summary of the issue found in the SQL statement.
            returned: on success
            type: str
            sample: finding_example
        recommendation:
            description:
                - The recommendation for a specific finding.
            returned: on success
            type: str
            sample: recommendation_example
        rationale:
            description:
                - Describes the reasoning behind the recommendation and how it relates to the finding.
            returned: on success
            type: str
            sample: rationale_example
        benefit:
            description:
                - The percentage benefit of this implementation.
            returned: on success
            type: float
            sample: 3.4
        implement_action_sql:
            description:
                - Action sql to be implemented based on the recommendation result.
            returned: on success
            type: str
            sample: implement_action_sql_example
        is_parallel_execution:
            description:
                - Indicates whether a SQL Profile recommendation uses parallel execution.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "sql_tuning_advisor_task_id": 56,
        "sql_tuning_advisor_task_object_id": 56,
        "recommendation_key": 56,
        "recommendation_type": "STATISTICS",
        "finding": "finding_example",
        "recommendation": "recommendation_example",
        "rationale": "rationale_example",
        "benefit": 3.4,
        "implement_action_sql": "implement_action_sql_example",
        "is_parallel_execution": true
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import SqlTuningClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SqlTuningAdvisorTaskRecommendationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
            "sql_tuning_advisor_task_id",
            "sql_object_id",
            "execution_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sql_tuning_advisor_task_recommendations,
            managed_database_id=self.module.params.get("managed_database_id"),
            sql_tuning_advisor_task_id=self.module.params.get(
                "sql_tuning_advisor_task_id"
            ),
            sql_object_id=self.module.params.get("sql_object_id"),
            execution_id=self.module.params.get("execution_id"),
            **optional_kwargs
        )


SqlTuningAdvisorTaskRecommendationFactsHelperCustom = get_custom_class(
    "SqlTuningAdvisorTaskRecommendationFactsHelperCustom"
)


class ResourceFactsHelper(
    SqlTuningAdvisorTaskRecommendationFactsHelperCustom,
    SqlTuningAdvisorTaskRecommendationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            sql_tuning_advisor_task_id=dict(type="int", required=True),
            sql_object_id=dict(type="int", required=True),
            execution_id=dict(type="int", required=True),
            sort_by=dict(type="str", choices=["RECOMMENDATION_TYPE", "BENEFIT"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_tuning_advisor_task_recommendation",
        service_client_class=SqlTuningClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_tuning_advisor_task_recommendations=result)


if __name__ == "__main__":
    main()
