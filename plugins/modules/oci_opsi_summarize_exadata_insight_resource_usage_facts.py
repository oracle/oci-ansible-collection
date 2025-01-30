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
module: oci_opsi_summarize_exadata_insight_resource_usage_facts
short_description: Fetches details about one or multiple SummarizeExadataInsightResourceUsage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SummarizeExadataInsightResourceUsage resources in Oracle Cloud Infrastructure
    - A cumulative distribution function is used to rank the usage data points per resource within the specified time period.
      For each resource, the minimum data point with a ranking > the percentile value is included in the summation.
      Linear regression functions are used to calculate the usage change percentage.
      Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE.
      Valid values for ResourceType HOST are CPU and MEMORY.
      Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    resource_type:
        description:
            - Filter by resource.
              Supported values are HOST , STORAGE_SERVER and DATABASE
        type: str
        required: true
    resource_metric:
        description:
            - Filter by resource metric.
              Supported values are CPU , STORAGE, MEMORY, IO, IOPS, THROUGHPUT
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
    exadata_insight_id:
        description:
            - Optional list of exadata insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    exadata_type:
        description:
            - Filter by one or more Exadata types.
              Possible value are DBMACHINE, EXACS, and EXACC.
        type: list
        elements: str
    cdb_name:
        description:
            - Filter by one or more cdb name.
        type: list
        elements: str
    host_name:
        description:
            - Filter by hostname.
        type: list
        elements: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The order in which resource usage summary records are listed
        type: str
        choices:
            - "utilizationPercent"
            - "usage"
            - "capacity"
            - "usageChangePercent"
    percentile:
        description:
            - Percentile values of daily usage to be used for computing the aggregate resource usage.
        type: int
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List summarize_exadata_insight_resource_usages
  oci_opsi_summarize_exadata_insight_resource_usage_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    resource_type: resource_type_example
    resource_metric: resource_metric_example

    # optional
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    exadata_insight_id: [ "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx" ]
    exadata_type: [ "exadata_type_example" ]
    cdb_name: [ "cdb_name_example" ]
    host_name: [ "host_name_example" ]
    sort_order: ASC
    sort_by: utilizationPercent
    percentile: 1
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]

"""

RETURN = """
summarize_exadata_insight_resource_usages:
    description:
        - List of SummarizeExadataInsightResourceUsage resources
    returned: on success
    type: complex
    contains:
        exadata_insight_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Exadata insight.
            returned: on success
            type: str
            sample: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"
        exadata_display_name:
            description:
                - The user-friendly name for the Exadata system. The name does not have to be unique.
            returned: on success
            type: str
            sample: exadata_display_name_example
        usage:
            description:
                - Total amount used of the resource metric type (CPU, STORAGE).
            returned: on success
            type: float
            sample: 1.2
        capacity:
            description:
                - The maximum allocated amount of the resource metric type  (CPU, STORAGE) for a set of databases.
            returned: on success
            type: float
            sample: 1.2
        utilization_percent:
            description:
                - Resource utilization in percentage
            returned: on success
            type: float
            sample: 1.2
        usage_change_percent:
            description:
                - Change in resource utilization in percentage
            returned: on success
            type: float
            sample: 1.2
        total_host_capacity:
            description:
                - The maximum host CPUs (cores x threads/core) on the underlying infrastructure. This only applies to CPU and does not not apply for Autonomous
                  Databases.
            returned: on success
            type: float
            sample: 1.2
    sample: [{
        "exadata_insight_id": "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx",
        "exadata_display_name": "exadata_display_name_example",
        "usage": 1.2,
        "capacity": 1.2,
        "utilization_percent": 1.2,
        "usage_change_percent": 1.2,
        "total_host_capacity": 1.2
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


class SummarizeExadataInsightResourceUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "resource_type",
            "resource_metric",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "exadata_insight_id",
            "exadata_type",
            "cdb_name",
            "host_name",
            "sort_order",
            "sort_by",
            "percentile",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_exadata_insight_resource_usage,
            compartment_id=self.module.params.get("compartment_id"),
            resource_type=self.module.params.get("resource_type"),
            resource_metric=self.module.params.get("resource_metric"),
            **optional_kwargs
        )


SummarizeExadataInsightResourceUsageFactsHelperCustom = get_custom_class(
    "SummarizeExadataInsightResourceUsageFactsHelperCustom"
)


class ResourceFactsHelper(
    SummarizeExadataInsightResourceUsageFactsHelperCustom,
    SummarizeExadataInsightResourceUsageFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            resource_type=dict(type="str", required=True),
            resource_metric=dict(type="str", required=True),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            exadata_insight_id=dict(type="list", elements="str"),
            exadata_type=dict(type="list", elements="str"),
            cdb_name=dict(type="list", elements="str"),
            host_name=dict(type="list", elements="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "utilizationPercent",
                    "usage",
                    "capacity",
                    "usageChangePercent",
                ],
            ),
            percentile=dict(type="int"),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="summarize_exadata_insight_resource_usage",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(summarize_exadata_insight_resource_usages=result)


if __name__ == "__main__":
    main()
