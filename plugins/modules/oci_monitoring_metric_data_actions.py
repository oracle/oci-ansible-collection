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
module: oci_monitoring_metric_data_actions
short_description: Perform actions on a MetricData resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MetricData resource in Oracle Cloud Infrastructure
    - "For I(action=summarize_metrics_data), returns aggregated data that match the criteria specified in the request. Compartment OCID required.
      For information on metric queries, see L(Building Metric Queries,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/buildingqueries.htm).
      For important limits information, see L(Limits on
      Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits).
      Transactions Per Second (TPS) per-tenancy limit for this operation: 10."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the
              resources monitored by the metric that you are searching for. Use tenancyId to search in
              the root compartment.
            - "Example: `ocid1.compartment.oc1..exampleuniqueID`"
        type: str
        required: true
    namespace:
        description:
            - The source service or application to use when searching for metric data points to aggregate.
            - "Example: `oci_computeagent`"
        type: str
        required: true
    resource_group:
        description:
            - Resource group that you want to use as a filter. The specified resource group must exist in the definition of the posted metric. Only one resource
              group can be applied per metric.
              A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_), hyphens
              (-), and dollar signs ($).
              Avoid entering confidential information.
            - "Example: `frontend-fleet`"
        type: str
    query:
        description:
            - "The Monitoring Query Language (MQL) expression to use when searching for metric data points to
              aggregate. The query must specify a metric, statistic, and interval. Supported values for
              interval: `1m`-`60m` (also `1h`). You can optionally specify dimensions and grouping functions.
              Supported grouping functions: `grouping()`, `groupBy()`."
            - Construct your query to avoid exceeding limits on returned data. See L(MetricData Reference,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/monitoring/20180401/MetricData).
            - For details about Monitoring Query Language (MQL), see
              L(Monitoring Query Language (MQL) Reference,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Reference/mql.htm).
              For available dimensions, review the metric definition for the supported service.
              See L(Supported Services,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#SupportedServices).
            - "Example: `CpuUtilization[1m].sum()`"
        type: str
        required: true
    start_time:
        description:
            - "The beginning of the time range to use when searching for metric data points.
              Format is defined by RFC3339. The response includes metric data points for the startTime.
              Default value: the timestamp 3 hours before the call was sent."
            - "Example: `2019-02-01T01:02:29.600Z`"
        type: str
    end_time:
        description:
            - "The end of the time range to use when searching for metric data points.
              Format is defined by RFC3339. The response excludes metric data points for the endTime.
              Default value: the timestamp representing when the call was sent."
            - "Example: `2019-02-01T02:02:29.600Z`"
        type: str
    resolution:
        description:
            - "The time between calculated aggregation windows. Use with the query interval to vary the
              frequency at which aggregated data points are returned. For example, use a query interval of
              5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute
              frequency. The resolution must be equal or less than the interval in the query. The default
              resolution is 1m (one minute). Supported values: `1m`-`60m` (also `1h`)."
            - "Example: `5m`"
        type: str
    compartment_id_in_subtree:
        description:
            - When true, returns resources from all compartments and subcompartments. The parameter can
              only be set to true when compartmentId is the tenancy OCID (the tenancy is the root compartment).
              A true value requires the user to have tenancy-level permissions. If this requirement is not met,
              then the call is rejected. When false, returns resources from only the compartment specified in
              compartmentId. Default is false.
        type: bool
    action:
        description:
            - The action to perform on the MetricData.
        type: str
        required: true
        choices:
            - "summarize_metrics_data"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action summarize_metrics_data on metric_data
  oci_monitoring_metric_data_actions:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    namespace: oci_computeagent
    query: CpuUtilization[1m]{resourceId:<instance_OCID>}.max()
    start_time: 2019-03-10T22:19:26.789Z
    end_time: 2019-03-10T22:28:26.789Z
    action: summarize_metrics_data

"""

RETURN = """
metric_data:
    description:
        - Details of the MetricData resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        namespace:
            description:
                - The reference provided in a metric definition to indicate the source service or
                  application that emitted the metric.
                - "Example: `oci_computeagent`"
            returned: on success
            type: string
            sample: oci_computeagent
        resource_group:
            description:
                - Resource group provided with the posted metric. A resource group is a custom string that can be used as a filter. Only one resource group can
                  be applied per metric.
                  A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_),
                  hyphens (-), and dollar signs ($).
                  Avoid entering confidential information.
                - "Example: `frontend-fleet`"
            returned: on success
            type: string
            sample: frontend-fleet
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the
                  resources from which the aggregated data was returned.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..exampleuniqueID
        name:
            description:
                - The name of the metric.
                - "Example: `CpuUtilization`"
            returned: on success
            type: string
            sample: CpuUtilization
        dimensions:
            description:
                - Qualifiers provided in the definition of the returned metric.
                  Available dimensions vary by metric namespace. Each dimension takes the form of a key-value pair.
                - "Example: `\\"resourceId\\": \\"ocid1.instance.region1.phx.exampleuniqueID\\"`"
            returned: on success
            type: dict
            sample: {}
        metadata:
            description:
                - The references provided in a metric definition to indicate extra information about the metric.
                - "Example: `\\"unit\\": \\"bytes\\"`"
            returned: on success
            type: dict
            sample: {}
        resolution:
            description:
                - "The time between calculated aggregation windows. Use with the query interval to vary the
                  frequency at which aggregated data points are returned. For example, use a query interval of
                  5 minutes with a resolution of 1 minute to retrieve five-minute aggregations at a one-minute
                  frequency. The resolution must be equal or less than the interval in the query. The default
                  resolution is 1m (one minute). Supported values: `1m`-`60m` (also `1h`)."
                - "Example: `5m`"
            returned: on success
            type: string
            sample: 5m
        aggregated_datapoints:
            description:
                - The list of timestamp-value pairs returned for the specified request. Metric values are rolled up to the start time specified in the request.
                  For important limits information related to data points, see MetricData Reference at the top of this page.
            returned: on success
            type: complex
            contains:
                timestamp:
                    description:
                        - The date and time associated with the value of this data point. Format defined by RFC3339.
                        - "Example: `2019-02-01T01:02:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2019-02-01T01:02:29.600Z
                value:
                    description:
                        - Numeric value of the metric.
                        - "Example: `10.4`"
                    returned: on success
                    type: float
                    sample: 10.4
    sample: {
        "namespace": "oci_computeagent",
        "resource_group": "frontend-fleet",
        "compartment_id": "ocid1.compartment.oc1..exampleuniqueID",
        "name": "CpuUtilization",
        "dimensions": {},
        "metadata": {},
        "resolution": "5m",
        "aggregated_datapoints": [{
            "timestamp": "2019-02-01T01:02:29.600Z",
            "value": 10.4
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.monitoring import MonitoringClient
    from oci.monitoring.models import SummarizeMetricsDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MetricDataActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        summarize_metrics_data
    """

    def summarize_metrics_data(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SummarizeMetricsDataDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.summarize_metrics_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                summarize_metrics_data_details=action_details,
                compartment_id_in_subtree=self.module.params.get(
                    "compartment_id_in_subtree"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


MetricDataActionsHelperCustom = get_custom_class("MetricDataActionsHelperCustom")


class ResourceHelper(MetricDataActionsHelperCustom, MetricDataActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            namespace=dict(type="str", required=True),
            resource_group=dict(type="str"),
            query=dict(type="str", required=True),
            start_time=dict(type="str"),
            end_time=dict(type="str"),
            resolution=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            action=dict(type="str", required=True, choices=["summarize_metrics_data"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="metric_data",
        service_client_class=MonitoringClient,
        namespace="monitoring",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
