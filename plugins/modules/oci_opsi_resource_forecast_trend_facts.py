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
module: oci_opsi_resource_forecast_trend_facts
short_description: Fetches details about a ResourceForecastTrend resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ResourceForecastTrend resource in Oracle Cloud Infrastructure
    - Get Forecast predictions for CPU and Storage resources since a time in the past.
      If compartmentIdInSubtree is specified, aggregates resources in a compartment and in all sub-compartments.
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
            - Filter by resource metric.
              Supported values are CPU , STORAGE, MEMORY and IO.
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
    database_type:
        description:
            - Filter by one or more database type.
              Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.
        type: list
        elements: str
        choices:
            - "ADW-S"
            - "ATP-S"
            - "ADW-D"
            - "ATP-D"
            - "EXTERNAL-PDB"
            - "EXTERNAL-NONCDB"
            - "COMANAGED-VM-CDB"
            - "COMANAGED-VM-PDB"
            - "COMANAGED-VM-NONCDB"
            - "COMANAGED-BM-CDB"
            - "COMANAGED-BM-PDB"
            - "COMANAGED-BM-NONCDB"
            - "COMANAGED-EXACS-CDB"
            - "COMANAGED-EXACS-PDB"
            - "COMANAGED-EXACS-NONCDB"
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
        type: list
        elements: str
    id:
        description:
            - Optional list of database insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    exadata_insight_id:
        description:
            - Optional list of exadata insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    cdb_name:
        description:
            - Filter by one or more cdb name.
        type: list
        elements: str
    statistic:
        description:
            - Choose the type of statistic metric data to be used for forecasting.
        type: str
        choices:
            - "AVG"
            - "MAX"
    forecast_days:
        description:
            - Number of days used for utilization forecast analysis.
        type: int
    forecast_model:
        description:
            - "Choose algorithm model for the forecasting.
              Possible values:
                - LINEAR: Uses linear regression algorithm for forecasting.
                - ML_AUTO: Automatically detects best algorithm to use for forecasting.
                - ML_NO_AUTO: Automatically detects seasonality of the data for forecasting using linear or seasonal algorithm."
        type: str
        choices:
            - "LINEAR"
            - "ML_AUTO"
            - "ML_NO_AUTO"
    utilization_level:
        description:
            - "Filter by utilization level by the following buckets:
                - HIGH_UTILIZATION: DBs with utilization greater or equal than 75.
                - LOW_UTILIZATION: DBs with utilization lower than 25.
                - MEDIUM_HIGH_UTILIZATION: DBs with utilization greater or equal than 50 but lower than 75.
                - MEDIUM_LOW_UTILIZATION: DBs with utilization greater or equal than 25 but lower than 50."
        type: str
        choices:
            - "HIGH_UTILIZATION"
            - "LOW_UTILIZATION"
            - "MEDIUM_HIGH_UTILIZATION"
            - "MEDIUM_LOW_UTILIZATION"
    confidence:
        description:
            - This parameter is used to change data's confidence level, this data is ingested by the
              forecast algorithm.
              Confidence is the probability of an interval to contain the expected population parameter.
              Manipulation of this value will lead to different results.
              If not set, default confidence value is 95%.
        type: int
    host_name:
        description:
            - Filter by one or more hostname.
        type: list
        elements: str
    tablespace_name:
        description:
            - Tablespace name for a database
        type: str
    is_database_instance_level_metrics:
        description:
            - Flag to indicate if database instance level metrics should be returned. The flag is ignored when a host name filter is not applied.
              When a hostname filter is applied this flag will determine whether to return metrics for the instances located on the specified host or for the
              whole database which contains an instance on this host.
        type: bool
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
    vmcluster_name:
        description:
            - Optional list of Exadata Insight VM cluster name.
        type: list
        elements: str
    high_utilization_threshold:
        description:
            - Percent value in which a resource metric is considered highly utilized.
        type: int
    low_utilization_threshold:
        description:
            - Percent value in which a resource metric is considered low utilized.
        type: int
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific resource_forecast_trend
  oci_opsi_resource_forecast_trend_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    resource_metric: resource_metric_example

    # optional
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    database_type: [ "ADW-S" ]
    database_id: [ "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx" ]
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    exadata_insight_id: [ "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx" ]
    cdb_name: [ "cdb_name_example" ]
    statistic: AVG
    forecast_days: 30
    forecast_model: LINEAR
    utilization_level: HIGH_UTILIZATION
    confidence: 1
    host_name: [ "host_name_example" ]
    tablespace_name: tablespace_name_example
    is_database_instance_level_metrics: true
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true
    vmcluster_name: [ "vmcluster_name_example" ]
    high_utilization_threshold: 1
    low_utilization_threshold: 0

"""

RETURN = """
resource_forecast_trend:
    description:
        - ResourceForecastTrend resource
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
        high_utilization_threshold:
            description:
                - Percent value in which a resource metric is considered highly utilized.
            returned: on success
            type: int
            sample: 56
        low_utilization_threshold:
            description:
                - Percent value in which a resource metric is considered lowly utilized.
            returned: on success
            type: int
            sample: 56
        resource_metric:
            description:
                - "Defines the type of resource metric (example: CPU, STORAGE)"
            returned: on success
            type: str
            sample: CPU
        usage_unit:
            description:
                - Displays usage unit ( CORES, GB , PERCENT, MBPS)
            returned: on success
            type: str
            sample: CORES
        selected_forecast_algorithm:
            description:
                - Auto-ML algorithm leveraged for the forecast. Only applicable for Auto-ML forecast.
            returned: on success
            type: str
            sample: selected_forecast_algorithm_example
        pattern:
            description:
                - Time series patterns used in the forecasting.
            returned: on success
            type: str
            sample: LINEAR
        tablespace_name:
            description:
                - The name of tablespace.
            returned: on success
            type: str
            sample: tablespace_name_example
        historical_data:
            description:
                - Time series data used for the forecast analysis.
            returned: on success
            type: complex
            contains:
                end_timestamp:
                    description:
                        - The timestamp in which the current sampling period ends in RFC 3339 format.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                usage:
                    description:
                        - Total amount used of the resource metric type (CPU, STORAGE).
                    returned: on success
                    type: float
                    sample: 1.2
        projected_data:
            description:
                - Time series data result of the forecasting analysis.
            returned: on success
            type: complex
            contains:
                end_timestamp:
                    description:
                        - The timestamp in which the current sampling period ends in RFC 3339 format.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                usage:
                    description:
                        - Total amount used of the resource metric type (CPU, STORAGE).
                    returned: on success
                    type: float
                    sample: 1.2
                high_value:
                    description:
                        - Upper uncertainty bound of the current usage value.
                    returned: on success
                    type: float
                    sample: 1.2
                low_value:
                    description:
                        - Lower uncertainty bound of the current usage value.
                    returned: on success
                    type: float
                    sample: 1.2
    sample: {
        "time_interval_start": "2013-10-20T19:20:30+01:00",
        "time_interval_end": "2013-10-20T19:20:30+01:00",
        "high_utilization_threshold": 56,
        "low_utilization_threshold": 56,
        "resource_metric": "CPU",
        "usage_unit": "CORES",
        "selected_forecast_algorithm": "selected_forecast_algorithm_example",
        "pattern": "LINEAR",
        "tablespace_name": "tablespace_name_example",
        "historical_data": [{
            "end_timestamp": "2013-10-20T19:20:30+01:00",
            "usage": 1.2
        }],
        "projected_data": [{
            "end_timestamp": "2013-10-20T19:20:30+01:00",
            "usage": 1.2,
            "high_value": 1.2,
            "low_value": 1.2
        }]
    }
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


class ResourceForecastTrendFactsHelperGen(OCIResourceFactsHelperBase):
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
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "statistic",
            "forecast_days",
            "forecast_model",
            "utilization_level",
            "confidence",
            "host_name",
            "tablespace_name",
            "is_database_instance_level_metrics",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
            "vmcluster_name",
            "high_utilization_threshold",
            "low_utilization_threshold",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_database_insight_resource_forecast_trend,
            compartment_id=self.module.params.get("compartment_id"),
            resource_metric=self.module.params.get("resource_metric"),
            **optional_kwargs
        )


ResourceForecastTrendFactsHelperCustom = get_custom_class(
    "ResourceForecastTrendFactsHelperCustom"
)


class ResourceFactsHelper(
    ResourceForecastTrendFactsHelperCustom, ResourceForecastTrendFactsHelperGen
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
            database_type=dict(
                type="list",
                elements="str",
                choices=[
                    "ADW-S",
                    "ATP-S",
                    "ADW-D",
                    "ATP-D",
                    "EXTERNAL-PDB",
                    "EXTERNAL-NONCDB",
                    "COMANAGED-VM-CDB",
                    "COMANAGED-VM-PDB",
                    "COMANAGED-VM-NONCDB",
                    "COMANAGED-BM-CDB",
                    "COMANAGED-BM-PDB",
                    "COMANAGED-BM-NONCDB",
                    "COMANAGED-EXACS-CDB",
                    "COMANAGED-EXACS-PDB",
                    "COMANAGED-EXACS-NONCDB",
                ],
            ),
            database_id=dict(type="list", elements="str"),
            id=dict(type="list", elements="str"),
            exadata_insight_id=dict(type="list", elements="str"),
            cdb_name=dict(type="list", elements="str"),
            statistic=dict(type="str", choices=["AVG", "MAX"]),
            forecast_days=dict(type="int"),
            forecast_model=dict(
                type="str", choices=["LINEAR", "ML_AUTO", "ML_NO_AUTO"]
            ),
            utilization_level=dict(
                type="str",
                choices=[
                    "HIGH_UTILIZATION",
                    "LOW_UTILIZATION",
                    "MEDIUM_HIGH_UTILIZATION",
                    "MEDIUM_LOW_UTILIZATION",
                ],
            ),
            confidence=dict(type="int"),
            host_name=dict(type="list", elements="str"),
            tablespace_name=dict(type="str"),
            is_database_instance_level_metrics=dict(type="bool"),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
            vmcluster_name=dict(type="list", elements="str"),
            high_utilization_threshold=dict(type="int"),
            low_utilization_threshold=dict(type="int"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_forecast_trend",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_forecast_trend=result)


if __name__ == "__main__":
    main()
