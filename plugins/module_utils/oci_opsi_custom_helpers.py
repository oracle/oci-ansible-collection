# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    import oci
    from oci.opsi.models import (
        SummarizeDatabaseInsightResourceStatisticsAggregationCollection,
    )
    from oci.opsi.models import SqlInsightAggregationCollection
    from oci.opsi.models import SqlPlanInsightAggregationCollection
    from oci.opsi.models import SqlStatisticsTimeSeriesByPlanAggregationCollection
    from oci.opsi.models import SqlStatisticsTimeSeriesAggregationCollection

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

logger = oci_common_utils.get_logger("oci_opsi_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class DatabaseInsightsActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        return True

    # action module performs operations on underlying databases and not database insight.
    # database insight is not infrastructure resource. Hence get_resource is not applicable here.
    # This is dummy implementation so that other method works.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)


class ResourceStatisticsFactsHelperCustom:
    # generated method `get_resource` uses pagination supported by Python SDK.
    # Python SDK strips off the attribute other than `items` from response.
    # this override fixes response returned from `SummarizeDatabaseInsightResourceStatistics` operation.
    def get_resource(self):
        optional_get_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_type",
            "database_id",
            "percentile",
            "insight_by",
            "forecast_days",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )

        resourceStatisticsAggregationCollection = (
            SummarizeDatabaseInsightResourceStatisticsAggregationCollection()
        )
        items = []
        for response in oci.pagination.list_call_get_all_results_generator(
            self.client.summarize_database_insight_resource_statistics,
            "response",
            compartment_id=self.module.params.get("compartment_id"),
            resource_metric=self.module.params.get("resource_metric"),
            **optional_kwargs
        ):
            _debug("Response is " + str(response.data))
            resourceStatisticsAggregationCollection.resource_metric = (
                response.data.resource_metric
            )
            resourceStatisticsAggregationCollection.usage_unit = (
                response.data.usage_unit
            )
            resourceStatisticsAggregationCollection.time_interval_start = (
                response.data.time_interval_start
            )
            resourceStatisticsAggregationCollection.time_interval_end = (
                response.data.time_interval_end
            )
            items.extend(response.data.items)

        resourceStatisticsAggregationCollection.items = items
        return oci_common_utils.get_default_response_from_resource(
            resourceStatisticsAggregationCollection
        )


class SqlInsightsFactsHelperCustom:
    # generated method `get_resource` uses pagination supported by Python SDK.
    # Python SDK strips off the attribute other than `items` from response.
    def get_resource(self):
        optional_get_method_params = [
            "database_type",
            "database_id",
            "database_time_pct_greater_than",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )

        sqlInsightAggregationCollection = SqlInsightAggregationCollection()
        items = []
        for response in oci.pagination.list_call_get_all_results_generator(
            self.client.summarize_sql_insights,
            "response",
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        ):
            sqlInsightAggregationCollection.inventory = response.data.inventory
            sqlInsightAggregationCollection.thresholds = response.data.thresholds
            sqlInsightAggregationCollection.time_interval_start = (
                response.data.time_interval_start
            )
            sqlInsightAggregationCollection.time_interval_end = (
                response.data.time_interval_end
            )
            items.extend(response.data.items)

        sqlInsightAggregationCollection.items = items
        return oci_common_utils.get_default_response_from_resource(
            sqlInsightAggregationCollection
        )


class SqlPlanInsightsFactsHelperCustom:
    # generated method `get_resource` uses pagination supported by Python SDK.
    # Python SDK strips off the attribute other than `items` from response.
    def get_resource(self):
        optional_get_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )

        sqlPlanInsightAggregationCollection = SqlPlanInsightAggregationCollection()
        items = []
        for response in oci.pagination.list_call_get_all_results_generator(
            self.client.summarize_sql_plan_insights,
            "response",
            compartment_id=self.module.params.get("compartment_id"),
            database_id=self.module.params.get("database_id"),
            sql_identifier=self.module.params.get("sql_identifier"),
            **optional_kwargs
        ):
            sqlPlanInsightAggregationCollection.database_id = response.data.database_id
            sqlPlanInsightAggregationCollection.insights = response.data.insights
            sqlPlanInsightAggregationCollection.sql_identifier = (
                response.data.sql_identifier
            )
            sqlPlanInsightAggregationCollection.time_interval_end = (
                response.data.time_interval_end
            )
            sqlPlanInsightAggregationCollection.time_interval_start = (
                response.data.time_interval_start
            )
            items.extend(response.data.items)

        sqlPlanInsightAggregationCollection.items = items
        return oci_common_utils.get_default_response_from_resource(
            sqlPlanInsightAggregationCollection
        )


class SqlStatisticsTimeSeriesByPlanFactsHelperCustom:
    # generated method `get_resource` uses pagination supported by Python SDK.
    # Python SDK strips off the attribute other than `items` from response.
    def get_resource(self):
        optional_get_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        sqlStatisticsTimeSeriesByPlanAggregationCollection = (
            SqlStatisticsTimeSeriesByPlanAggregationCollection()
        )
        items = []
        for response in oci.pagination.list_call_get_all_results_generator(
            self.client.summarize_sql_statistics_time_series_by_plan,
            "response",
            compartment_id=self.module.params.get("compartment_id"),
            database_id=self.module.params.get("database_id"),
            sql_identifier=self.module.params.get("sql_identifier"),
            **optional_kwargs
        ):
            sqlStatisticsTimeSeriesByPlanAggregationCollection.database_id = (
                response.data.database_id
            )
            sqlStatisticsTimeSeriesByPlanAggregationCollection.end_timestamps = (
                response.data.end_timestamps
            )
            sqlStatisticsTimeSeriesByPlanAggregationCollection.item_duration_in_ms = (
                response.data.item_duration_in_ms
            )
            sqlStatisticsTimeSeriesByPlanAggregationCollection.time_interval_start = (
                response.data.time_interval_start
            )
            sqlStatisticsTimeSeriesByPlanAggregationCollection.time_interval_end = (
                response.data.time_interval_end
            )
            sqlStatisticsTimeSeriesByPlanAggregationCollection.sql_identifier = (
                response.data.sql_identifier
            )
            items.extend(response.data.items)

        sqlStatisticsTimeSeriesByPlanAggregationCollection.items = items
        return oci_common_utils.get_default_response_from_resource(
            sqlStatisticsTimeSeriesByPlanAggregationCollection
        )


class SqlStatisticsTimeSeriesFactsHelperCustom:
    # generated method `get_resource` uses pagination supported by Python SDK.
    # Python SDK strips off the attribute other than `items` from response.
    def get_resource(self):
        optional_get_method_params = [
            "database_id",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )

        sqlStatisticsTimeSeriesAggregationCollection = (
            SqlStatisticsTimeSeriesAggregationCollection()
        )
        items = []
        for response in oci.pagination.list_call_get_all_results_generator(
            self.client.summarize_sql_statistics_time_series,
            "response",
            compartment_id=self.module.params.get("compartment_id"),
            sql_identifier=self.module.params.get("sql_identifier"),
            **optional_kwargs
        ):
            sqlStatisticsTimeSeriesAggregationCollection.end_timestamps = (
                response.data.end_timestamps
            )
            sqlStatisticsTimeSeriesAggregationCollection.item_duration_in_ms = (
                response.data.item_duration_in_ms
            )
            sqlStatisticsTimeSeriesAggregationCollection.time_interval_start = (
                response.data.time_interval_start
            )
            sqlStatisticsTimeSeriesAggregationCollection.time_interval_end = (
                response.data.time_interval_end
            )
            sqlStatisticsTimeSeriesAggregationCollection.sql_identifier = (
                response.data.sql_identifier
            )
            items.extend(response.data.items)

        sqlStatisticsTimeSeriesAggregationCollection.items = items
        return oci_common_utils.get_default_response_from_resource(
            sqlStatisticsTimeSeriesAggregationCollection
        )


class EnterpriseManagerBridgeHelperCustom:
    def get_entity_type(self):
        return "opsienterprisemanagerbridge"


class HostInsightHelperCustom:
    def get_entity_type(self):
        return "opsidatabaseinsight"


class HostInsightActionsHelperCustom:
    ENABLE_ACTION_KEY = "enable"
    DISABLE_ACTION_KEY = "disable"
    RESOURCE_OPERATION_INSIGHTS_STATUS_ATTR = "status"
    STATUS_ENABLED = "ENABLED"
    STATUS_DISABLED = "DISABLED"

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        if action == self.ENABLE_ACTION_KEY:
            if (
                getattr(resource, self.RESOURCE_OPERATION_INSIGHTS_STATUS_ATTR, None)
                == self.STATUS_ENABLED
            ):
                return False
            return True
        if action == self.DISABLE_ACTION_KEY:
            if (
                getattr(resource, self.RESOURCE_OPERATION_INSIGHTS_STATUS_ATTR, None)
                == self.STATUS_DISABLED
            ):
                return False
            return True
        return super(HostInsightActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
