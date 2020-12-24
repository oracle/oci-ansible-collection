#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
            - Filter by resource metric.
              Supported values are CPU and STORAGE.
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
              Possible values are ADW-S, ATP-S, ADW-D, ATP-D
        type: list
        choices:
            - "ADW-S"
            - "ATP-S"
            - "ADW-D"
            - "ATP-D"
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific resource_forecast_trend
  oci_opsi_resource_forecast_trend_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    resource_metric: resource_metric_example

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
                - Defines the type of resource metric (CPU, STORAGE)
            returned: on success
            type: string
            sample: STORAGE
        usage_unit:
            description:
                - Displays usage unit ( CORES, GB)
            returned: on success
            type: string
            sample: CORES
        pattern:
            description:
                - Time series patterns used in the forecasting.
            returned: on success
            type: string
            sample: LINEAR
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
                    type: string
                    sample: 2020-05-01T00:00:00.000Z
                usage:
                    description:
                        - Total amount used of the resource metric type (CPU, STORAGE).
                    returned: on success
                    type: float
                    sample: 34.5
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
                    type: string
                    sample: 2020-05-01T00:00:00.000Z
                usage:
                    description:
                        - Total amount used of the resource metric type (CPU, STORAGE).
                    returned: on success
                    type: float
                    sample: 34.5
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
        "time_interval_start": "2020-12-06T00:00:00.000Z",
        "time_interval_end": "2020-12-06T00:00:00.000Z",
        "resource_metric": "STORAGE",
        "usage_unit": "CORES",
        "pattern": "LINEAR",
        "historical_data": [{
            "end_timestamp": "2020-05-01T00:00:00.000Z",
            "usage": 34.5
        }],
        "projected_data": [{
            "end_timestamp": "2020-05-01T00:00:00.000Z",
            "usage": 34.5,
            "high_value": 1.2,
            "low_value": 1.2
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
            "statistic",
            "forecast_days",
            "forecast_model",
            "utilization_level",
            "confidence",
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
                type="list", choices=["ADW-S", "ATP-S", "ADW-D", "ATP-D"]
            ),
            database_id=dict(type="list"),
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
        )
    )

    module = AnsibleModule(argument_spec=module_args)

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
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_forecast_trend=result)


if __name__ == "__main__":
    main()
