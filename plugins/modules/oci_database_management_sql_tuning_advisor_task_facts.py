#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_database_management_sql_tuning_advisor_task_facts
short_description: Fetches details about one or multiple SqlTuningAdvisorTask resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SqlTuningAdvisorTask resources in Oracle Cloud Infrastructure
    - Lists the SQL Tuning Advisor tasks for the specified Managed Database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    name:
        description:
            - The optional query parameter to filter the SQL Tuning Advisor task list by name.
        type: str
    status:
        description:
            - The optional query parameter to filter the SQL Tuning Advisor task list by status.
        type: str
        choices:
            - "INITIAL"
            - "EXECUTING"
            - "INTERRUPTED"
            - "COMPLETED"
            - "ERROR"
    time_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to query parameter to filter the timestamp.
        type: str
    time_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the timestamp.
        type: str
    sort_by:
        description:
            - The option to sort the SQL Tuning Advisor task summary data.
        type: str
        choices:
            - "NAME"
            - "START_TIME"
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
- name: List sql_tuning_advisor_tasks
  oci_database_management_sql_tuning_advisor_task_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    status: INITIAL
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    sort_by: NAME
    sort_order: ASC

"""

RETURN = """
sql_tuning_advisor_tasks:
    description:
        - List of SqlTuningAdvisorTask resources
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
        instance_id:
            description:
                - The instance ID of the SQL Tuning Advisor task. This is not the
                  L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
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
                - The description of the SQL Tuning Advisor task.
            returned: on success
            type: str
            sample: description_example
        owner:
            description:
                - The owner of the SQL Tuning Advisor task.
            returned: on success
            type: str
            sample: owner_example
        time_created:
            description:
                - The Creation date of the SQL Tuning Advisor task.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        task_status:
            description:
                - The status of the SQL Tuning Advisor task.
            returned: on success
            type: str
            sample: COMPLETED
        days_to_expire:
            description:
                - The number of days left before the task expires. If the value equals -1, then the task has no expiration time (UNLIMITED).
            returned: on success
            type: int
            sample: 56
        time_execution_started:
            description:
                - The start time of the task execution.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_execution_ended:
            description:
                - The end time of the task execution.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        total_sql_statements:
            description:
                - The total number of SQL statements related to the SQL Tuning Advisor task.
            returned: on success
            type: int
            sample: 56
        recommendation_count:
            description:
                - The number of recommendations provided for the SQL Tuning Advisor task.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "sql_tuning_advisor_task_id": 56,
        "instance_id": 56,
        "name": "name_example",
        "description": "description_example",
        "owner": "owner_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "task_status": "COMPLETED",
        "days_to_expire": 56,
        "time_execution_started": "2013-10-20T19:20:30+01:00",
        "time_execution_ended": "2013-10-20T19:20:30+01:00",
        "total_sql_statements": 56,
        "recommendation_count": 56
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


class SqlTuningAdvisorTaskFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "status",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sql_tuning_advisor_tasks,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


SqlTuningAdvisorTaskFactsHelperCustom = get_custom_class(
    "SqlTuningAdvisorTaskFactsHelperCustom"
)


class ResourceFactsHelper(
    SqlTuningAdvisorTaskFactsHelperCustom, SqlTuningAdvisorTaskFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            name=dict(type="str"),
            status=dict(
                type="str",
                choices=["INITIAL", "EXECUTING", "INTERRUPTED", "COMPLETED", "ERROR"],
            ),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            sort_by=dict(type="str", choices=["NAME", "START_TIME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_tuning_advisor_task",
        service_client_class=SqlTuningClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_tuning_advisor_tasks=result)


if __name__ == "__main__":
    main()
