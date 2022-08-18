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
module: oci_apm_traces_query_result_actions
short_description: Perform actions on a QueryResult resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a QueryResult resource in Oracle Cloud Infrastructure
    - For I(action=query), retrieves the results (selected attributes and aggregations) of a query constructed according to the Application Performance
      Monitoring Defined Query Syntax.
      Query results are filtered by the filter criteria specified in the where clause.
      Further query results are grouped by the attributes specified in the group by clause.  Finally,
      ordering (asc/desc) is done by the specified attributes in the order by clause.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM Domain ID the request is intended for.
        type: str
        required: true
    time_span_started_greater_than_or_equal_to:
        description:
            - Include spans that have a `spanStartTime` equal to or greater than this value.
        type: str
        required: true
    time_span_started_less_than:
        description:
            - Include spans that have a `spanStartTime`less than this value.
        type: str
        required: true
    query_text:
        description:
            - Application Performance Monitoring defined query string that filters and retrieves trace data results.
        type: str
    action:
        description:
            - The action to perform on the QueryResult.
        type: str
        required: true
        choices:
            - "query"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action query on query_result
  oci_apm_traces_query_result_actions:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    time_span_started_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_span_started_less_than: 2013-10-20T19:20:30+01:00
    action: query

    # optional
    query_text: query_text_example

"""

RETURN = """
query_result_response:
    description:
        - Details of the QueryResult resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        query_result_metadata_summary:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                query_result_row_type_summaries:
                    description:
                        - A collection of QueryResultRowTypeSummary objects that describe the type and properties of the individual row elements of the query
                          rows
                          being returned.  The i-th element in this list contains the QueryResultRowTypeSummary of the i-th key-value pair in the
                          QueryResultRowData map.
                    returned: on success
                    type: complex
                    contains:
                        data_type:
                            description:
                                - Datatype of the query result row element.
                            returned: on success
                            type: str
                            sample: data_type_example
                        unit:
                            description:
                                - Granular unit in which the query result row element's data is represented.
                            returned: on success
                            type: str
                            sample: unit_example
                        display_name:
                            description:
                                - Alias name if an alias is used for the query result row element or an assigned display name from the query language
                                  in some default cases.
                            returned: on success
                            type: str
                            sample: display_name_example
                        expression:
                            description:
                                - Actual show expression in the user typed query that produced this column.
                            returned: on success
                            type: str
                            sample: expression_example
                        query_result_row_type_summaries:
                            description:
                                - A query result row type summary object that represents a nested table structure.
                            returned: on success
                            type: complex
                            contains:
                                data_type:
                                    description:
                                        - Datatype of the query result row element.
                                    returned: on success
                                    type: str
                                    sample: data_type_example
                                unit:
                                    description:
                                        - Granular unit in which the query result row element's data is represented.
                                    returned: on success
                                    type: str
                                    sample: unit_example
                                display_name:
                                    description:
                                        - Alias name if an alias is used for the query result row element or an assigned display name from the query language
                                          in some default cases.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                expression:
                                    description:
                                        - Actual show expression in the user typed query that produced this column.
                                    returned: on success
                                    type: str
                                    sample: expression_example
                                query_result_row_type_summaries:
                                    description:
                                        - A query result row type summary object that represents a nested table structure.
                                    returned: on success
                                    type: list
                                    sample: []
                source_name:
                    description:
                        - Source of the query result set (traces, spans, and so on).
                    returned: on success
                    type: str
                    sample: source_name_example
                query_results_grouped_by:
                    description:
                        - Columns or attributes of the query rows  which are group by values.  This is a list of ResultsGroupedBy summary objects,
                          and the list will contain as many elements as the attributes and aggregate functions in the group by clause in the select query.
                    returned: on success
                    type: complex
                    contains:
                        query_results_grouped_by_column:
                            description:
                                - Column or attribute in the query result, which is a group by value.
                            returned: on success
                            type: str
                            sample: query_results_grouped_by_column_example
                query_results_ordered_by:
                    description:
                        - Order by which the query results are organized.  This is a list of queryResultsOrderedBy summary objects, and the list
                          will contain more than one OrderedBy summary object, if the sort was multidimensional.
                    returned: on success
                    type: complex
                    contains:
                        query_results_ordered_by:
                            description:
                                - Attribute by which the query results are sorted.
                            returned: on success
                            type: str
                            sample: query_results_ordered_by_example
                        query_results_sort_order:
                            description:
                                - The sort order for the attribute, either 'ASC' or 'DESC'.
                            returned: on success
                            type: str
                            sample: query_results_sort_order_example
                time_series_interval_in_mins:
                    description:
                        - Interval for the time series function in minutes.
                    returned: on success
                    type: int
                    sample: 56
        query_result_rows:
            description:
                - A collection of objects with each object representing an individual row of the query result set.  The total number of objects
                  returned in this collection correspond to the total number of rows returned by the actual query that is run against
                  the queried entity.
            returned: on success
            type: complex
            contains:
                query_result_row_data:
                    description:
                        - "A map containing the actual data represented by a single row of the query result.
                          The key is the column name or attribute specified in the show clause, or an aggregate function in the show clause.
                          The value is the actual value of that attribute or aggregate function of the corresponding single row of the query result set.
                          If an alias name is specified for an attribute or an aggregate function, then the key will be the alias name specified in the show
                          clause.  If an alias name is not specified for the group by aggregate function in the show clause, then the corresponding key
                          will be the appropriate aggregate_function_name_column_name (For example: count(traces) will be keyed as count_traces).  The datatype
                          of the value
                          is presented in the queryResultRowTypeSummaries list in the queryResultMetadata structure, where the i-th queryResultRowTypeSummary
                          object
                          represents the datatype of the i-th value when this map is iterated in order."
                    returned: on success
                    type: dict
                    sample: {}
                query_result_row_metadata:
                    description:
                        - A map containing metadata or add-on data for the data presented in the queryResultRowData map.  Data required to present drill down
                          information from the queryResultRowData is presented as key-value pairs.
                    returned: on success
                    type: dict
                    sample: {}
    sample: {
        "query_result_metadata_summary": {
            "query_result_row_type_summaries": [{
                "data_type": "data_type_example",
                "unit": "unit_example",
                "display_name": "display_name_example",
                "expression": "expression_example",
                "query_result_row_type_summaries": [{
                    "data_type": "data_type_example",
                    "unit": "unit_example",
                    "display_name": "display_name_example",
                    "expression": "expression_example",
                    "query_result_row_type_summaries": []
                }]
            }],
            "source_name": "source_name_example",
            "query_results_grouped_by": [{
                "query_results_grouped_by_column": "query_results_grouped_by_column_example"
            }],
            "query_results_ordered_by": [{
                "query_results_ordered_by": "query_results_ordered_by_example",
                "query_results_sort_order": "query_results_sort_order_example"
            }],
            "time_series_interval_in_mins": 56
        },
        "query_result_rows": [{
            "query_result_row_data": {},
            "query_result_row_metadata": {}
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.apm_traces import QueryClient
    from oci.apm_traces.models import QueryDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueryResultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        query
    """

    def query(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, QueryDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.query,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                time_span_started_greater_than_or_equal_to=self.module.params.get(
                    "time_span_started_greater_than_or_equal_to"
                ),
                time_span_started_less_than=self.module.params.get(
                    "time_span_started_less_than"
                ),
                query_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


QueryResultActionsHelperCustom = get_custom_class("QueryResultActionsHelperCustom")


class ResourceHelper(QueryResultActionsHelperCustom, QueryResultActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            time_span_started_greater_than_or_equal_to=dict(type="str", required=True),
            time_span_started_less_than=dict(type="str", required=True),
            query_text=dict(type="str"),
            action=dict(type="str", required=True, choices=["query"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="query_result",
        service_client_class=QueryClient,
        namespace="apm_traces",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
