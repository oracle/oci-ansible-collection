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
module: oci_database_management_optimizer_statistics_collection_aggregations_facts
short_description: Fetches details about one or multiple OptimizerStatisticsCollectionAggregations resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OptimizerStatisticsCollectionAggregations resources in Oracle Cloud Infrastructure
    - Gets a list of the optimizer statistics collection operations per hour, grouped by task or object status for the specified Managed Database.
      You must specify a value for GroupByQueryParam to determine whether the data should be grouped by task status or task object status.
      Optionally, you can specify a date-time range (of seven days) to obtain collection aggregations within the specified time range.
      If the date-time range is not specified, then the operations in the last seven days are listed.
      You can further filter the results by providing the optional type of TaskTypeQueryParam.
      If the task type not provided, then both Auto and Manual tasks are considered for aggregation.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    group_type:
        description:
            - The optimizer statistics tasks grouped by type.
        type: str
        choices:
            - "TASK_STATUS"
            - "TASK_OBJECTS_STATUS"
        required: true
    start_time_greater_than_or_equal_to:
        description:
            - "The start time of the time range to retrieve the optimizer statistics of a Managed Database
              in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
        type: str
    end_time_less_than_or_equal_to:
        description:
            - "The end time of the time range to retrieve the optimizer statistics of a Managed Database
              in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
        type: str
    task_type:
        description:
            - The filter types of the optimizer statistics tasks.
        type: str
        choices:
            - "ALL"
            - "MANUAL"
            - "AUTO"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List optimizer_statistics_collection_aggregations
  oci_database_management_optimizer_statistics_collection_aggregations_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    group_type: TASK_STATUS

    # optional
    start_time_greater_than_or_equal_to: start_time_greater_than_or_equal_to_example
    end_time_less_than_or_equal_to: end_time_less_than_or_equal_to_example
    task_type: ALL

"""

RETURN = """
optimizer_statistics_collection_aggregations:
    description:
        - List of OptimizerStatisticsCollectionAggregations resources
    returned: on success
    type: complex
    contains:
        group_by:
            description:
                - The optimizer statistics tasks grouped by type.
            returned: on success
            type: str
            sample: TASK_STATUS
        time_start:
            description:
                - Indicates the start of the hour as the statistics are aggregated per hour.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - Indicates the end of the hour as the statistics are aggregated per hour.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        pending:
            description:
                - The number of tasks or objects for which statistics are yet to be gathered.
            returned: on success
            type: int
            sample: 56
        in_progress:
            description:
                - The number of tasks or objects for which statistics gathering is in progress.
            returned: on success
            type: int
            sample: 56
        completed:
            description:
                - The number of tasks or objects for which statistics gathering is completed.
            returned: on success
            type: int
            sample: 56
        failed:
            description:
                - The number of tasks or objects for which statistics gathering failed.
            returned: on success
            type: int
            sample: 56
        skipped:
            description:
                - The number of tasks or objects for which statistics gathering was skipped.
            returned: on success
            type: int
            sample: 56
        timed_out:
            description:
                - The number of tasks or objects for which statistics gathering timed out.
            returned: on success
            type: int
            sample: 56
        unknown:
            description:
                - The number of tasks or objects for which the status of statistics gathering is unknown.
            returned: on success
            type: int
            sample: 56
        total:
            description:
                - "The total number of tasks or objects for which statistics collection is finished. This number is the
                  sum of all the tasks or objects with various statuses: pending, inProgress, completed, failed, skipped,
                  timedOut, and unknown."
            returned: on success
            type: int
            sample: 56
    sample: [{
        "group_by": "TASK_STATUS",
        "time_start": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "pending": 56,
        "in_progress": 56,
        "completed": 56,
        "failed": 56,
        "skipped": 56,
        "timed_out": 56,
        "unknown": 56,
        "total": 56
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


class OptimizerStatisticsCollectionAggregationsFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
            "group_type",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "start_time_greater_than_or_equal_to",
            "end_time_less_than_or_equal_to",
            "task_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_optimizer_statistics_collection_aggregations,
            managed_database_id=self.module.params.get("managed_database_id"),
            group_type=self.module.params.get("group_type"),
            **optional_kwargs
        )


OptimizerStatisticsCollectionAggregationsFactsHelperCustom = get_custom_class(
    "OptimizerStatisticsCollectionAggregationsFactsHelperCustom"
)


class ResourceFactsHelper(
    OptimizerStatisticsCollectionAggregationsFactsHelperCustom,
    OptimizerStatisticsCollectionAggregationsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            group_type=dict(
                type="str",
                required=True,
                choices=["TASK_STATUS", "TASK_OBJECTS_STATUS"],
            ),
            start_time_greater_than_or_equal_to=dict(type="str"),
            end_time_less_than_or_equal_to=dict(type="str"),
            task_type=dict(type="str", choices=["ALL", "MANUAL", "AUTO"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="optimizer_statistics_collection_aggregations",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(optimizer_statistics_collection_aggregations=result)


if __name__ == "__main__":
    main()
