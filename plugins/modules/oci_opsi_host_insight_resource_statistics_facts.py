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
module: oci_opsi_host_insight_resource_statistics_facts
short_description: Fetches details about a HostInsightResourceStatistics resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a HostInsightResourceStatistics resource in Oracle Cloud Infrastructure
    - Lists the resource statistics (usage, capacity, usage change percent, utilization percent, load) for each host filtered
      by utilization level.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    resource_metric:
        description:
            - Filter by host resource metric.
              Supported values are CPU, MEMORY, and LOGICAL_MEMORY.
        type: str
        required: true
    analysis_time_interval:
        description:
            - Specify time period in ISO 8601 format with respect to current time.
              Default is last 30 days represented by P30D.
              If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
              Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to
              current time (P25M).
        type: str
    time_interval_start:
        description:
            - Analysis start time in UTC in ISO 8601 format(inclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              The minimum allowed value is 2 years prior to the current day.
              timeIntervalStart and timeIntervalEnd parameters are used together.
              If analysisTimeInterval is specified, this parameter is ignored.
        type: str
    time_interval_end:
        description:
            - Analysis end time in UTC in ISO 8601 format(exclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              timeIntervalStart and timeIntervalEnd are used together.
              If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.
        type: str
    platform_type:
        description:
            - Filter by one or more platform types.
              Possible value is LINUX.
        type: list
        choices:
            - "LINUX"
    id:
        description:
            - Optional list of host insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
    percentile:
        description:
            - Percentile values of daily usage to be used for computing the aggregate resource usage.
        type: int
    insight_by:
        description:
            - Return data of a specific insight
              Possible values are High Utilization, Low Utilization, Any ,High Utilization Forecast,
              Low Utilization Forecast
        type: str
    forecast_days:
        description:
            - Number of days used for utilization forecast analysis.
        type: int
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The order in which resource statistics records are listed.
        type: str
        choices:
            - "utilizationPercent"
            - "usage"
            - "usageChangePercent"
            - "hostName"
            - "platformType"
    defined_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
    freeform_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
              The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
        type: list
    defined_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
              or \\"{namespace}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
    freeform_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
              The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for different tag names are interpreted as \\"AND\\"."
        type: list
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific host_insight_resource_statistics
  oci_opsi_host_insight_resource_statistics_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    resource_metric: resource_metric_example

"""

RETURN = """
host_insight_resource_statistics:
    description:
        - HostInsightResourceStatistics resource
    returned: on success
    type: complex
    contains:
        time_interval_start:
            description:
                - The start timestamp that was passed into the request.
            returned: on success
            type: string
            sample: 2020-12-06T00:00:00.000Z
        time_interval_end:
            description:
                - The end timestamp that was passed into the request.
            returned: on success
            type: string
            sample: 2020-12-06T00:00:00.000Z
        resource_metric:
            description:
                - Defines the type of resource metric (CPU, Physical Memory, Logical Memory)
            returned: on success
            type: string
            sample: CPU
        usage_unit:
            description:
                - Displays usage unit.
            returned: on success
            type: string
            sample: CORES
        items:
            description:
                - Collection of Resource Statistics items
            returned: on success
            type: complex
            contains:
                host_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host.
                            returned: on success
                            type: string
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        host_name:
                            description:
                                - The host name. The host name is unique amongst the hosts managed by the same management agent.
                            returned: on success
                            type: string
                            sample: host_name_example
                        host_display_name:
                            description:
                                - The user-friendly name for the host. The name does not have to be unique.
                            returned: on success
                            type: string
                            sample: host_display_name_example
                        platform_type:
                            description:
                                - Platform type.
                            returned: on success
                            type: string
                            sample: LINUX
                        agent_identifier:
                            description:
                                - The identifier of the agent.
                            returned: on success
                            type: string
                            sample: agent_identifier_example
                current_statistics:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        usage:
                            description:
                                - Total amount used of the resource metric type (CPU, STORAGE).
                            returned: on success
                            type: float
                            sample: 34.5
                        capacity:
                            description:
                                - The maximum allocated amount of the resource metric type  (CPU, STORAGE).
                            returned: on success
                            type: float
                            sample: 222.3
                        utilization_percent:
                            description:
                                - Resource utilization in percentage.
                            returned: on success
                            type: float
                            sample: 35.1
                        usage_change_percent:
                            description:
                                - Change in resource utilization in percentage
                            returned: on success
                            type: float
                            sample: 5.2
                        resource_name:
                            description:
                                - Name of resource for host
                            returned: on success
                            type: string
                            sample: HOST_CPU_STATISTICS
                        load:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                minimum:
                                    description:
                                        - The smallest number in the data set.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                maximum:
                                    description:
                                        - The largest number in the data set.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                average:
                                    description:
                                        - The average number in the data set.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                median:
                                    description:
                                        - The middle number in the data set.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                lower_quartile:
                                    description:
                                        - The middle number between the smallest number and the median of the data set. It's also known as the 25th quartile.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                upper_quartile:
                                    description:
                                        - The middle number between the median and the largest number of the data set. It's also known as the 75th quartile.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                        free_memory:
                            description:
                                - ""
                            returned: on success
                            type: float
                            sample: 1.2
                        available_memory:
                            description:
                                - ""
                            returned: on success
                            type: float
                            sample: 1.2
                        huge_pages_total:
                            description:
                                - Total number of huge pages.
                            returned: on success
                            type: int
                            sample: 56
                        huge_page_size_in_mb:
                            description:
                                - Size of huge pages in megabytes.
                            returned: on success
                            type: float
                            sample: 1.2
                        huge_pages_free:
                            description:
                                - Total number of available huge pages.
                            returned: on success
                            type: int
                            sample: 56
                        huge_pages_reserved:
                            description:
                                - Total number of huge pages which are used or reserved.
                            returned: on success
                            type: int
                            sample: 56
    sample: {
        "time_interval_start": "2020-12-06T00:00:00.000Z",
        "time_interval_end": "2020-12-06T00:00:00.000Z",
        "resource_metric": "CPU",
        "usage_unit": "CORES",
        "items": [{
            "host_details": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "host_name": "host_name_example",
                "host_display_name": "host_display_name_example",
                "platform_type": "LINUX",
                "agent_identifier": "agent_identifier_example"
            },
            "current_statistics": {
                "usage": 34.5,
                "capacity": 222.3,
                "utilization_percent": 35.1,
                "usage_change_percent": 5.2,
                "resource_name": "HOST_CPU_STATISTICS",
                "load": {
                    "minimum": 1.2,
                    "maximum": 1.2,
                    "average": 1.2,
                    "median": 1.2,
                    "lower_quartile": 1.2,
                    "upper_quartile": 1.2
                },
                "free_memory": 1.2,
                "available_memory": 1.2,
                "huge_pages_total": 56,
                "huge_page_size_in_mb": 1.2,
                "huge_pages_free": 56,
                "huge_pages_reserved": 56
            }
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HostInsightResourceStatisticsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
            "resource_metric",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "percentile",
            "insight_by",
            "forecast_days",
            "sort_order",
            "sort_by",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_host_insight_resource_statistics,
            compartment_id=self.module.params.get("compartment_id"),
            resource_metric=self.module.params.get("resource_metric"),
            **optional_kwargs
        )


HostInsightResourceStatisticsFactsHelperCustom = get_custom_class(
    "HostInsightResourceStatisticsFactsHelperCustom"
)


class ResourceFactsHelper(
    HostInsightResourceStatisticsFactsHelperCustom,
    HostInsightResourceStatisticsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            resource_metric=dict(type="str", required=True),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            platform_type=dict(type="list", choices=["LINUX"]),
            id=dict(type="list"),
            percentile=dict(type="int"),
            insight_by=dict(type="str"),
            forecast_days=dict(type="int"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "utilizationPercent",
                    "usage",
                    "usageChangePercent",
                    "hostName",
                    "platformType",
                ],
            ),
            defined_tag_equals=dict(type="list"),
            freeform_tag_equals=dict(type="list"),
            defined_tag_exists=dict(type="list"),
            freeform_tag_exists=dict(type="list"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="host_insight_resource_statistics",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(host_insight_resource_statistics=result)


if __name__ == "__main__":
    main()
