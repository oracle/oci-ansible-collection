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
module: oci_opsi_host_insight_resource_statistics_facts
short_description: Fetches details about one or multiple HostInsightResourceStatistics resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HostInsightResourceStatistics resources in Oracle Cloud Infrastructure
    - Lists the resource statistics (usage, capacity, usage change percent, utilization percent, load) for each host filtered
      by utilization level in a compartment and in all sub-compartments if specified.
version_added: "2.9.0"
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
            - "Filter by one or more platform types.
              Supported platformType(s) for MACS-managed external host insight: [LINUX].
              Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX]."
        type: list
        elements: str
        choices:
            - "LINUX"
            - "SOLARIS"
            - "SUNOS"
            - "ZLINUX"
    id:
        description:
            - Optional list of host insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    exadata_insight_id:
        description:
            - Optional list of exadata insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
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
        elements: str
    freeform_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
              The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    defined_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
              or \\"{namespace}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
              The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    compartment_id_in_subtree:
        description:
            - A flag to search all resources within a given compartment and all sub-compartments.
        type: bool
    host_type:
        description:
            - Filter by one or more host types.
              Possible values are CLOUD-HOST, EXTERNAL-HOST
        type: list
        elements: str
    host_id:
        description:
            - Optional L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host (Compute Id)
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List host_insight_resource_statistics
  oci_opsi_host_insight_resource_statistics_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    resource_metric: resource_metric_example

    # optional
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    platform_type: [ "LINUX" ]
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    exadata_insight_id: [ "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx" ]
    percentile: 1
    insight_by: insight_by_example
    forecast_days: 30
    sort_order: ASC
    sort_by: utilizationPercent
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true
    host_type: [ "host_type_example" ]
    host_id: "ocid1.host.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
host_insight_resource_statistics:
    description:
        - List of HostInsightResourceStatistics resources
    returned: on success
    type: complex
    contains:
        time_interval_start:
            description:
                - The start timestamp that was passed into the request.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_interval_end:
            description:
                - The end timestamp that was passed into the request.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        resource_metric:
            description:
                - Defines the type of resource metric (CPU, Physical Memory, Logical Memory)
            returned: on success
            type: str
            sample: CPU
        usage_unit:
            description:
                - Displays usage unit ( CORES, GB , PERCENT, MBPS)
            returned: on success
            type: str
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
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        compartment_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        host_name:
                            description:
                                - The host name. The host name is unique amongst the hosts managed by the same management agent.
                            returned: on success
                            type: str
                            sample: host_name_example
                        host_display_name:
                            description:
                                - The user-friendly name for the host. The name does not have to be unique.
                            returned: on success
                            type: str
                            sample: host_display_name_example
                        platform_type:
                            description:
                                - "Platform type.
                                  Supported platformType(s) for MACS-managed external host insight: [LINUX].
                                  Supported platformType(s) for EM-managed external host insight: [LINUX, SOLARIS, SUNOS, ZLINUX]."
                            returned: on success
                            type: str
                            sample: LINUX
                        agent_identifier:
                            description:
                                - The identifier of the agent.
                            returned: on success
                            type: str
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
                            sample: 1.2
                        capacity:
                            description:
                                - The maximum allocated amount of the resource metric type  (CPU, STORAGE).
                            returned: on success
                            type: float
                            sample: 1.2
                        utilization_percent:
                            description:
                                - Resource utilization in percentage.
                            returned: on success
                            type: float
                            sample: 1.2
                        usage_change_percent:
                            description:
                                - Change in resource utilization in percentage
                            returned: on success
                            type: float
                            sample: 1.2
                        resource_name:
                            description:
                                - Name of resource for host
                            returned: on success
                            type: str
                            sample: HOST_CPU_STATISTICS
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
    sample: [{
        "time_interval_start": "2013-10-20T19:20:30+01:00",
        "time_interval_end": "2013-10-20T19:20:30+01:00",
        "resource_metric": "CPU",
        "usage_unit": "CORES",
        "items": [{
            "host_details": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "host_name": "host_name_example",
                "host_display_name": "host_display_name_example",
                "platform_type": "LINUX",
                "agent_identifier": "agent_identifier_example"
            },
            "current_statistics": {
                "usage": 1.2,
                "capacity": 1.2,
                "utilization_percent": 1.2,
                "usage_change_percent": 1.2,
                "resource_name": "HOST_CPU_STATISTICS",
                "free_memory": 1.2,
                "available_memory": 1.2,
                "huge_pages_total": 56,
                "huge_page_size_in_mb": 1.2,
                "huge_pages_free": 56,
                "huge_pages_reserved": 56,
                "load": {
                    "minimum": 1.2,
                    "maximum": 1.2,
                    "average": 1.2,
                    "median": 1.2,
                    "lower_quartile": 1.2,
                    "upper_quartile": 1.2
                }
            }
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HostInsightResourceStatisticsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "resource_metric",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "platform_type",
            "id",
            "exadata_insight_id",
            "percentile",
            "insight_by",
            "forecast_days",
            "sort_order",
            "sort_by",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
            "host_type",
            "host_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
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
            platform_type=dict(
                type="list",
                elements="str",
                choices=["LINUX", "SOLARIS", "SUNOS", "ZLINUX"],
            ),
            id=dict(type="list", elements="str"),
            exadata_insight_id=dict(type="list", elements="str"),
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
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
            host_type=dict(type="list", elements="str"),
            host_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="host_insight_resource_statistics",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(host_insight_resource_statistics=result)


if __name__ == "__main__":
    main()
