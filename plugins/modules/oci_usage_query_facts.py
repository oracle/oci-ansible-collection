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
module: oci_usage_query_facts
short_description: Fetches details about one or multiple Query resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Query resources in Oracle Cloud Infrastructure
    - Returns the saved query list.
    - If I(query_id) is specified, the details of a single Query will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    query_id:
        description:
            - The query unique OCID.
            - Required to get a specific query.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment ID in which to list resources.
            - Required to list multiple queries.
        type: str
    sort_by:
        description:
            - The field to sort by. If not specified, the default is displayName.
        type: str
        choices:
            - "displayName"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List queries
  oci_usage_query_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific query
  oci_usage_query_facts:
    query_id: "ocid1.query.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
queries:
    description:
        - List of Query resources
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.usage_api import UsageapiClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "query_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_query, query_id=self.module.params.get("query_id"),
        )

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
            self.client.list_queries,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


QueryFactsHelperCustom = get_custom_class("QueryFactsHelperCustom")


class ResourceFactsHelper(QueryFactsHelperCustom, QueryFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            query_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="query",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(queries=result)


if __name__ == "__main__":
    main()
