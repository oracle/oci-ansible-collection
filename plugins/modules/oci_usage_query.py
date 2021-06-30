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
module: oci_usage_query
short_description: Manage a Query resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Query resource in Oracle Cloud Infrastructure
    - For I(state=present), returns the created query.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment OCID.
            - Required for create using I(state=present).
        type: str
    query_definition:
        description:
            - ""
            - Required for create using I(state=present), update using I(state=present) with query_id present.
        type: dict
        suboptions:
            display_name:
                description:
                    - The query display name. Avoid entering confidential information.
                type: str
                aliases: ["name"]
                required: true
            report_query:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    tenant_id:
                        description:
                            - Tenant ID
                        type: str
                        required: true
                    time_usage_started:
                        description:
                            - The usage start time.
                        type: str
                    time_usage_ended:
                        description:
                            - The usage end time.
                        type: str
                    granularity:
                        description:
                            - "The usage granularity.
                              HOURLY - Hourly data aggregation.
                              DAILY - Daily data aggregation.
                              MONTHLY - Monthly data aggregation.
                              TOTAL - Not yet supported."
                        type: str
                        choices:
                            - "HOURLY"
                            - "DAILY"
                            - "MONTHLY"
                            - "TOTAL"
                        required: true
                    is_aggregate_by_time:
                        description:
                            - is aggregated by time. true isAggregateByTime will add up all usage/cost over query time period
                        type: bool
                    forecast:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            forecast_type:
                                description:
                                    - BASIC uses ETS to project future usage/cost based on history data. The basis for projections will be a rolling set of
                                      equivalent historical days for which projection is being made.
                                type: str
                                choices:
                                    - "BASIC"
                            time_forecast_started:
                                description:
                                    - forecast start time. Will default to UTC-1 if not specified
                                type: str
                            time_forecast_ended:
                                description:
                                    - forecast end time.
                                type: str
                                required: true
                    query_type:
                        description:
                            - "The query usage type. COST by default if it is missing
                              Usage - Query the usage data.
                              Cost - Query the cost/billing data."
                        type: str
                        choices:
                            - "USAGE"
                            - "COST"
                    group_by:
                        description:
                            - "Aggregate the result by.
                              example:
                                `[\\"tagNamespace\\", \\"tagKey\\", \\"tagValue\\", \\"service\\", \\"skuName\\", \\"skuPartNumber\\", \\"unit\\",
                                  \\"compartmentName\\", \\"compartmentPath\\", \\"compartmentId\\", \\"platform\\", \\"region\\", \\"logicalAd\\",
                                  \\"resourceId\\", \\"tenantId\\", \\"tenantName\\"]`"
                        type: list
                    group_by_tag:
                        description:
                            - "GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list.
                              For example:
                                `[{\\"namespace\\":\\"oracle\\", \\"key\\":\\"createdBy\\"]`"
                        type: list
                        suboptions:
                            namespace:
                                description:
                                    - The tag namespace.
                                type: str
                            key:
                                description:
                                    - The tag key.
                                type: str
                            value:
                                description:
                                    - The tag value.
                                type: str
                    compartment_depth:
                        description:
                            - The compartment depth level.
                        type: float
                    filter:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            operator:
                                description:
                                    - "The filter operator. Example: 'AND', 'OR', 'NOT'."
                                type: str
                                choices:
                                    - "AND"
                                    - "NOT"
                                    - "OR"
                            dimensions:
                                description:
                                    - The dimensions to filter on.
                                type: list
                                suboptions:
                                    key:
                                        description:
                                            - The dimension key.
                                        type: str
                                        required: true
                                    value:
                                        description:
                                            - The dimension value.
                                        type: str
                                        required: true
                            tags:
                                description:
                                    - The tags to filter on.
                                type: list
                                suboptions:
                                    namespace:
                                        description:
                                            - The tag namespace.
                                        type: str
                                    key:
                                        description:
                                            - The tag key.
                                        type: str
                                    value:
                                        description:
                                            - The tag value.
                                        type: str
                            filters:
                                description:
                                    - The nested filter object.
                                type: list
                                suboptions:
                                    operator:
                                        description:
                                            - "The filter operator. Example: 'AND', 'OR', 'NOT'."
                                        type: str
                                        choices:
                                            - "AND"
                                            - "NOT"
                                            - "OR"
                                    dimensions:
                                        description:
                                            - The dimensions to filter on.
                                        type: list
                                    tags:
                                        description:
                                            - The tags to filter on.
                                        type: list
                                    filters:
                                        description:
                                            - The nested filter object.
                                        type: list
                    date_range_name:
                        description:
                            - the date range for ui, eg LAST_THREE_MONTHS. It is conflict with timeUsageStarted and timeUsageEnded
                        type: str
                        choices:
                            - "LAST_SEVEN_DAYS"
                            - "LAST_TEN_DAYS"
                            - "MTD"
                            - "LAST_TWO_MONTHS"
                            - "LAST_THREE_MONTHS"
                            - "ALL"
                            - "LAST_SIX_MONTHS"
                            - "LAST_ONE_YEAR"
                            - "YTD"
                            - "CUSTOM"
            cost_analysis_ui:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    graph:
                        description:
                            - the type of graph mode.
                        type: str
                        choices:
                            - "BARS"
                            - "LINES"
                            - "STACKED_LINES"
                    is_cumulative_graph:
                        description:
                            - is cumulative graph.
                        type: bool
            version:
                description:
                    - the version of saved query.
                type: float
                required: true
    query_id:
        description:
            - The query unique OCID.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Query.
            - Use I(state=present) to create or update a Query.
            - Use I(state=absent) to delete a Query.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create query
  oci_usage_query:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    query_definition:
      display_name: display_name_example
      report_query:
        tenant_id: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        granularity: HOURLY
      version: 10

- name: Update query
  oci_usage_query:
    query_definition:
      display_name: display_name_example
      report_query:
        tenant_id: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
        granularity: HOURLY
      version: 10
    query_id: "ocid1.query.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete query
  oci_usage_query:
    query_id: "ocid1.query.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
query:
    description:
        - Details of the Query resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The query OCID.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment OCID.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        query_definition:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - The query display name. Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                report_query:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        tenant_id:
                            description:
                                - Tenant ID
                            returned: on success
                            type: string
                            sample: "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx"
                        time_usage_started:
                            description:
                                - The usage start time.
                            returned: on success
                            type: string
                            sample: 2013-10-20T19:20:30+01:00
                        time_usage_ended:
                            description:
                                - The usage end time.
                            returned: on success
                            type: string
                            sample: 2013-10-20T19:20:30+01:00
                        granularity:
                            description:
                                - "The usage granularity.
                                  HOURLY - Hourly data aggregation.
                                  DAILY - Daily data aggregation.
                                  MONTHLY - Monthly data aggregation.
                                  TOTAL - Not yet supported."
                            returned: on success
                            type: string
                            sample: HOURLY
                        is_aggregate_by_time:
                            description:
                                - is aggregated by time. true isAggregateByTime will add up all usage/cost over query time period
                            returned: on success
                            type: bool
                            sample: true
                        forecast:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                forecast_type:
                                    description:
                                        - BASIC uses ETS to project future usage/cost based on history data. The basis for projections will be a rolling set of
                                          equivalent historical days for which projection is being made.
                                    returned: on success
                                    type: string
                                    sample: BASIC
                                time_forecast_started:
                                    description:
                                        - forecast start time. Will default to UTC-1 if not specified
                                    returned: on success
                                    type: string
                                    sample: 2013-10-20T19:20:30+01:00
                                time_forecast_ended:
                                    description:
                                        - forecast end time.
                                    returned: on success
                                    type: string
                                    sample: 2013-10-20T19:20:30+01:00
                        query_type:
                            description:
                                - "The query usage type. COST by default if it is missing
                                  Usage - Query the usage data.
                                  Cost - Query the cost/billing data."
                            returned: on success
                            type: string
                            sample: USAGE
                        group_by:
                            description:
                                - "Aggregate the result by.
                                  example:
                                    `[\\"tagNamespace\\", \\"tagKey\\", \\"tagValue\\", \\"service\\", \\"skuName\\", \\"skuPartNumber\\", \\"unit\\",
                                      \\"compartmentName\\", \\"compartmentPath\\", \\"compartmentId\\", \\"platform\\", \\"region\\", \\"logicalAd\\",
                                      \\"resourceId\\", \\"tenantId\\", \\"tenantName\\"]`"
                            returned: on success
                            type: list
                            sample: []
                        group_by_tag:
                            description:
                                - "GroupBy a specific tagKey. Provide the tagNamespace and tagKey in the tag object. Only supports one tag in the list.
                                  For example:
                                    `[{\\"namespace\\":\\"oracle\\", \\"key\\":\\"createdBy\\"]`"
                            returned: on success
                            type: complex
                            contains:
                                namespace:
                                    description:
                                        - The tag namespace.
                                    returned: on success
                                    type: string
                                    sample: namespace_example
                                key:
                                    description:
                                        - The tag key.
                                    returned: on success
                                    type: string
                                    sample: key_example
                                value:
                                    description:
                                        - The tag value.
                                    returned: on success
                                    type: string
                                    sample: value_example
                        compartment_depth:
                            description:
                                - The compartment depth level.
                            returned: on success
                            type: float
                            sample: 10
                        filter:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                operator:
                                    description:
                                        - "The filter operator. Example: 'AND', 'OR', 'NOT'."
                                    returned: on success
                                    type: string
                                    sample: AND
                                dimensions:
                                    description:
                                        - The dimensions to filter on.
                                    returned: on success
                                    type: complex
                                    contains:
                                        key:
                                            description:
                                                - The dimension key.
                                            returned: on success
                                            type: string
                                            sample: key_example
                                        value:
                                            description:
                                                - The dimension value.
                                            returned: on success
                                            type: string
                                            sample: value_example
                                tags:
                                    description:
                                        - The tags to filter on.
                                    returned: on success
                                    type: complex
                                    contains:
                                        namespace:
                                            description:
                                                - The tag namespace.
                                            returned: on success
                                            type: string
                                            sample: namespace_example
                                        key:
                                            description:
                                                - The tag key.
                                            returned: on success
                                            type: string
                                            sample: key_example
                                        value:
                                            description:
                                                - The tag value.
                                            returned: on success
                                            type: string
                                            sample: value_example
                                filters:
                                    description:
                                        - The nested filter object.
                                    returned: on success
                                    type: complex
                                    contains:
                                        operator:
                                            description:
                                                - "The filter operator. Example: 'AND', 'OR', 'NOT'."
                                            returned: on success
                                            type: string
                                            sample: AND
                                        dimensions:
                                            description:
                                                - The dimensions to filter on.
                                            returned: on success
                                            type: list
                                            sample: []
                                        tags:
                                            description:
                                                - The tags to filter on.
                                            returned: on success
                                            type: list
                                            sample: []
                                        filters:
                                            description:
                                                - The nested filter object.
                                            returned: on success
                                            type: list
                                            sample: []
                        date_range_name:
                            description:
                                - the date range for ui, eg LAST_THREE_MONTHS. It is conflict with timeUsageStarted and timeUsageEnded
                            returned: on success
                            type: string
                            sample: LAST_SEVEN_DAYS
                cost_analysis_ui:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        graph:
                            description:
                                - the type of graph mode.
                            returned: on success
                            type: string
                            sample: BARS
                        is_cumulative_graph:
                            description:
                                - is cumulative graph.
                            returned: on success
                            type: bool
                            sample: true
                version:
                    description:
                        - the version of saved query.
                    returned: on success
                    type: float
                    sample: 10
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "query_definition": {
            "display_name": "display_name_example",
            "report_query": {
                "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
                "time_usage_started": "2013-10-20T19:20:30+01:00",
                "time_usage_ended": "2013-10-20T19:20:30+01:00",
                "granularity": "HOURLY",
                "is_aggregate_by_time": true,
                "forecast": {
                    "forecast_type": "BASIC",
                    "time_forecast_started": "2013-10-20T19:20:30+01:00",
                    "time_forecast_ended": "2013-10-20T19:20:30+01:00"
                },
                "query_type": "USAGE",
                "group_by": [],
                "group_by_tag": [{
                    "namespace": "namespace_example",
                    "key": "key_example",
                    "value": "value_example"
                }],
                "compartment_depth": 10,
                "filter": {
                    "operator": "AND",
                    "dimensions": [{
                        "key": "key_example",
                        "value": "value_example"
                    }],
                    "tags": [{
                        "namespace": "namespace_example",
                        "key": "key_example",
                        "value": "value_example"
                    }],
                    "filters": [{
                        "operator": "AND",
                        "dimensions": [],
                        "tags": [],
                        "filters": []
                    }]
                },
                "date_range_name": "LAST_SEVEN_DAYS"
            },
            "cost_analysis_ui": {
                "graph": "BARS",
                "is_cumulative_graph": true
            },
            "version": 10
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.usage_api import UsageapiClient
    from oci.usage_api.models import CreateQueryDetails
    from oci.usage_api.models import UpdateQueryDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueryHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "query_id"

    def get_module_resource_id(self):
        return self.module.params.get("query_id")

    def get_get_fn(self):
        return self.client.get_query

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_query, query_id=self.module.params.get("query_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_queries, **kwargs)

    def get_create_model_class(self):
        return CreateQueryDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_query,
            call_fn_args=(),
            call_fn_kwargs=dict(create_query_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateQueryDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_query,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_query_details=update_details,
                query_id=self.module.params.get("query_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_query,
            call_fn_args=(),
            call_fn_kwargs=dict(query_id=self.module.params.get("query_id"),),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


QueryHelperCustom = get_custom_class("QueryHelperCustom")


class ResourceHelper(QueryHelperCustom, QueryHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            query_definition=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str", required=True),
                    report_query=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            tenant_id=dict(type="str", required=True),
                            time_usage_started=dict(type="str"),
                            time_usage_ended=dict(type="str"),
                            granularity=dict(
                                type="str",
                                required=True,
                                choices=["HOURLY", "DAILY", "MONTHLY", "TOTAL"],
                            ),
                            is_aggregate_by_time=dict(type="bool"),
                            forecast=dict(
                                type="dict",
                                options=dict(
                                    forecast_type=dict(type="str", choices=["BASIC"]),
                                    time_forecast_started=dict(type="str"),
                                    time_forecast_ended=dict(type="str", required=True),
                                ),
                            ),
                            query_type=dict(type="str", choices=["USAGE", "COST"]),
                            group_by=dict(type="list"),
                            group_by_tag=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    namespace=dict(type="str"),
                                    key=dict(type="str"),
                                    value=dict(type="str"),
                                ),
                            ),
                            compartment_depth=dict(type="float"),
                            filter=dict(
                                type="dict",
                                options=dict(
                                    operator=dict(
                                        type="str", choices=["AND", "NOT", "OR"]
                                    ),
                                    dimensions=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(type="str", required=True),
                                            value=dict(type="str", required=True),
                                        ),
                                    ),
                                    tags=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            namespace=dict(type="str"),
                                            key=dict(type="str"),
                                            value=dict(type="str"),
                                        ),
                                    ),
                                    filters=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            operator=dict(
                                                type="str", choices=["AND", "NOT", "OR"]
                                            ),
                                            dimensions=dict(type="list"),
                                            tags=dict(type="list"),
                                            filters=dict(type="list"),
                                        ),
                                    ),
                                ),
                            ),
                            date_range_name=dict(
                                type="str",
                                choices=[
                                    "LAST_SEVEN_DAYS",
                                    "LAST_TEN_DAYS",
                                    "MTD",
                                    "LAST_TWO_MONTHS",
                                    "LAST_THREE_MONTHS",
                                    "ALL",
                                    "LAST_SIX_MONTHS",
                                    "LAST_ONE_YEAR",
                                    "YTD",
                                    "CUSTOM",
                                ],
                            ),
                        ),
                    ),
                    cost_analysis_ui=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            graph=dict(
                                type="str", choices=["BARS", "LINES", "STACKED_LINES"]
                            ),
                            is_cumulative_graph=dict(type="bool"),
                        ),
                    ),
                    version=dict(type="float", required=True),
                ),
            ),
            query_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="query",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
