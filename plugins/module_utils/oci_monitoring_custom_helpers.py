# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_config_utils,
)

try:
    from oci.monitoring.models.metric import Metric
    from oci.monitoring.models.metric_data import MetricData
    from oci.monitoring.models.suppression import Suppression
    from oci.monitoring import MonitoringClient

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class MetricActionsHelperCustom:
    # this resource does not have get method. The customisation for `get_resource` is only to make the other functions
    # work and to return some data to the user.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            resource=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, Metric
            )
        )


class MetricDataActionsHelperCustom:
    # this resource does not have get method. The customisation for `get_resource` is only to make the other functions
    # work and to return some data to the user.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            resource=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, MetricData
            )
        )


class SuppressionActionsHelperCustom:
    # this resource does not have get method. The customisation for `get_resource` is only to make the other functions
    # work and to return some data to the user.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            resource=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, Suppression
            )
        )


class MetricDataHelperCustom:
    # operation - PostMetricData uses the telemetry-ingestion endpoints; all other operations, use the telemetry
    # endpoints. Providing `service_endpoint` argument explicitly to specify service endpoint used by this client.
    def __init__(self, *args, **kwargs):
        super(MetricDataHelperCustom, self).__init__(*args, **kwargs)
        service_endpoint = str(self.client.base_client.endpoint)
        self.module.params["service_endpoint"] = service_endpoint.replace(
            "telemetry", "telemetry-ingestion"
        )

        self.client = oci_config_utils.create_service_client(
            self.module, MonitoringClient
        )


class AlarmActionsHelperCustom:
    REMOVE_ALARM_SUPPRESSION = "remove_alarm_suppression"

    # For idempotency we check if suppression already exists for an alarm.
    def is_action_necessary(self, action, resource=None):
        if action.lower() == self.REMOVE_ALARM_SUPPRESSION:
            return resource.suppression is not None
        return super(AlarmActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
