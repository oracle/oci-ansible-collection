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
module: oci_opsi_summarize_exadata_insight_resource_forecast_trend_facts
short_description: Fetches details about one or multiple SummarizeExadataInsightResourceForecastTrend resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SummarizeExadataInsightResourceForecastTrend resources in Oracle Cloud Infrastructure
    - Get historical usage and forecast predictions for an exadata system with breakdown by databases, hosts or storage servers.
      Additionally resources can be filtered using databaseInsightId, hostInsightId or storageServerName query parameters.
      Top five resources are returned if total exceeds the limit specified.
      Valid values for ResourceType DATABASE are CPU,MEMORY,IO and STORAGE. Database name is returned in name field. DatabaseInsightId , cdbName and hostName
      query parameter applies to ResourceType DATABASE.
      Valid values for ResourceType HOST are CPU and MEMORY. HostName s returned in name field. HostInsightId and hostName query parameter applies to
      ResourceType HOST.
      Valid values for ResourceType STORAGE_SERVER are STORAGE, IOPS and THROUGHPUT. Storage server name is returned in name field for resourceMetric IOPS and
      THROUGHPUT
      and asmName is returned in name field for resourceMetric STORAGE. StorageServerName query parameter applies to ResourceType STORAGE_SERVER.
      Valid value for ResourceType DISKGROUP is STORAGE. Comma delimited (asmName,diskgroupName) is returned in name field.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
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
    exadata_insight_id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of exadata insight resource.
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
    database_insight_id:
        description:
            - Optional list of database insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    host_insight_id:
        description:
            - Optional list of host insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    storage_server_name:
        description:
            - Optional storage server name on an exadata system.
        type: list
        elements: str
    exadata_type:
        description:
            - Filter by one or more Exadata types.
              Possible value are DBMACHINE, EXACS, and EXACC.
        type: list
        elements: str
    statistic:
        description:
            - Choose the type of statistic metric data to be used for forecasting.
        type: str
        choices:
            - "AVG"
            - "MAX"
    forecast_start_day:
        description:
            - Number of days used for utilization forecast analysis.
        type: int
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
    confidence:
        description:
            - This parameter is used to change data's confidence level, this data is ingested by the
              forecast algorithm.
              Confidence is the probability of an interval to contain the expected population parameter.
              Manipulation of this value will lead to different results.
              If not set, default confidence value is 95%.
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
            - The order in which resource Forecast trend records are listed
        type: str
        choices:
            - "id"
            - "name"
            - "daysToReachCapacity"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List summarize_exadata_insight_resource_forecast_trends
  oci_opsi_summarize_exadata_insight_resource_forecast_trend_facts:
    # required
    resource_type: resource_type_example
    resource_metric: resource_metric_example
    exadata_insight_id: "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    database_insight_id: [ "ocid1.databaseinsight.oc1..xxxxxxEXAMPLExxxxxx" ]
    host_insight_id: [ "ocid1.hostinsight.oc1..xxxxxxEXAMPLExxxxxx" ]
    storage_server_name: [ "storage_server_name_example" ]
    exadata_type: [ "exadata_type_example" ]
    statistic: AVG
    forecast_start_day: 0
    forecast_days: 0
    forecast_model: LINEAR
    cdb_name: [ "cdb_name_example" ]
    host_name: [ "host_name_example" ]
    confidence: 1
    sort_order: ASC
    sort_by: id

"""

RETURN = """
summarize_exadata_insight_resource_forecast_trends:
    description:
        - List of SummarizeExadataInsightResourceForecastTrend resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database insight resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the resource.
            returned: on success
            type: str
            sample: name_example
        days_to_reach_capacity:
            description:
                - Days to reach capacity for a storage server
            returned: on success
            type: int
            sample: 56
        pattern:
            description:
                - Time series patterns used in the forecasting.
            returned: on success
            type: str
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "days_to_reach_capacity": 56,
        "pattern": "LINEAR",
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
    }]
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


class SummarizeExadataInsightResourceForecastTrendFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "resource_type",
            "resource_metric",
            "exadata_insight_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_insight_id",
            "host_insight_id",
            "storage_server_name",
            "exadata_type",
            "statistic",
            "forecast_start_day",
            "forecast_days",
            "forecast_model",
            "cdb_name",
            "host_name",
            "confidence",
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_exadata_insight_resource_forecast_trend,
            resource_type=self.module.params.get("resource_type"),
            resource_metric=self.module.params.get("resource_metric"),
            exadata_insight_id=self.module.params.get("exadata_insight_id"),
            **optional_kwargs
        )


SummarizeExadataInsightResourceForecastTrendFactsHelperCustom = get_custom_class(
    "SummarizeExadataInsightResourceForecastTrendFactsHelperCustom"
)


class ResourceFactsHelper(
    SummarizeExadataInsightResourceForecastTrendFactsHelperCustom,
    SummarizeExadataInsightResourceForecastTrendFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            resource_type=dict(type="str", required=True),
            resource_metric=dict(type="str", required=True),
            exadata_insight_id=dict(type="str", required=True),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            database_insight_id=dict(type="list", elements="str"),
            host_insight_id=dict(type="list", elements="str"),
            storage_server_name=dict(type="list", elements="str"),
            exadata_type=dict(type="list", elements="str"),
            statistic=dict(type="str", choices=["AVG", "MAX"]),
            forecast_start_day=dict(type="int"),
            forecast_days=dict(type="int"),
            forecast_model=dict(
                type="str", choices=["LINEAR", "ML_AUTO", "ML_NO_AUTO"]
            ),
            cdb_name=dict(type="list", elements="str"),
            host_name=dict(type="list", elements="str"),
            confidence=dict(type="int"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["id", "name", "daysToReachCapacity"]),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="summarize_exadata_insight_resource_forecast_trend",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(summarize_exadata_insight_resource_forecast_trends=result)


if __name__ == "__main__":
    main()
