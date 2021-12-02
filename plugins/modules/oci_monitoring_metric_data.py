#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_monitoring_metric_data
short_description: Manage a MetricData resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a MetricData resource in Oracle Cloud Infrastructure
    - For I(state=present), publishes raw metric data points to the Monitoring service.
      For more information about publishing metrics, see L(Publishing Custom
      Metrics,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Tasks/publishingcustommetrics.htm).
      For important limits information, see L(Limits on
      Monitoring,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#Limits).
    - Per-call limits information follows.
    - "* Dimensions per metric group*. Maximum: 20. Minimum: 1.
      * Unique metric streams*. Maximum: 50.
      * Transactions Per Second (TPS) per-tenancy limit for this operation: 50."
    - "*A metric group is the combination of a given metric, metric namespace, and tenancy for the purpose of determining limits.
      A dimension is a qualifier provided in a metric definition.
      A metric stream is an individual set of aggregated data for a metric, typically specific to a resource.
      For more information about metric-related concepts, see L(Monitoring
      Concepts,https://docs.cloud.oracle.com/iaas/Content/Monitoring/Concepts/monitoringoverview.htm#concepts)."
    - "The endpoints for this operation differ from other Monitoring operations. Replace the string `telemetry` with `telemetry-ingestion` in the endpoint, as
      in the following example:"
    - https://telemetry-ingestion.eu-frankfurt-1.oraclecloud.com
    - "This resource has the following action operations in the M(oracle.oci.oci_monitoring_metric_data_actions) module: summarize_metrics_data."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    metric_data:
        description:
            - A metric object containing raw metric data points to be posted to the Monitoring service.
        type: list
        elements: dict
        required: true
        suboptions:
            namespace:
                description:
                    - The source service or application emitting the metric.
                    - "A valid namespace value starts with an alphabetical character and includes only alphanumeric characters and underscores. The \\"oci_\\"
                      prefix is reserved.
                      Avoid entering confidential information."
                    - "Example: `my_namespace`"
                type: str
                required: true
            resource_group:
                description:
                    - Resource group to assign to the metric. A resource group is a custom string that you can match when retrieving custom metrics. Only one
                      resource group can be applied per metric.
                      A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.), underscores (_),
                      hyphens (-), and dollar signs ($).
                      Avoid entering confidential information.
                    - "Example: `frontend-fleet`"
                type: str
            compartment_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to use for metrics.
                type: str
                required: true
            name:
                description:
                    - The name of the metric.
                    - A valid name value starts with an alphabetical character and includes only alphanumeric characters, dots, underscores, hyphens, and dollar
                      signs. The `oci_` prefix is reserved.
                      Avoid entering confidential information.
                    - "Example: `my_app.success_rate`"
                type: str
                required: true
            dimensions:
                description:
                    - Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.
                      Each dimension takes the form of a key-value pair.
                      A valid dimension key includes only printable ASCII, excluding periods (.) and spaces. The character limit for a dimension key is 256.
                      A valid dimension value includes only Unicode characters. The character limit for a dimension value is 256.
                      Empty strings are not allowed for keys or values. Avoid entering confidential information.
                    - "Example: `\\"resourceId\\": \\"ocid1.instance.region1.phx.exampleuniqueID\\"`"
                type: dict
                required: true
            metadata:
                description:
                    - Properties describing metrics. These are not part of the unique fields identifying the metric.
                      Each metadata item takes the form of a key-value pair. The character limit for a metadata key is 256. The character limit for a metadata
                      value is 256.
                    - "Example: `\\"unit\\": \\"bytes\\"`"
                type: dict
            datapoints:
                description:
                    - A list of metric values with timestamps. At least one data point is required per call.
                type: list
                elements: dict
                required: true
                suboptions:
                    timestamp:
                        description:
                            - Timestamp for this metric value. Format defined by RFC3339.
                            - "Example: `2019-02-01T01:02:29.600Z`"
                        type: str
                        required: true
                    value:
                        description:
                            - Numeric value of the metric.
                            - "Example: `10.23`"
                        type: float
                        required: true
                    count:
                        description:
                            - The number of occurrences of the associated value in the set of data.
                            - Default is 1. Value must be greater than zero.
                        type: int
    batch_atomicity:
        description:
            - "Batch atomicity behavior. Requires either partial or full pass of input validation for
              metric objects in PostMetricData requests. The default value of NON_ATOMIC requires a
              partial pass: at least one metric object in the request must pass input validation, and
              any objects that failed validation are identified in the returned summary, along with
              their error messages. A value of ATOMIC requires a full pass: all metric objects in
              the request must pass input validation."
            - "Example: `NON_ATOMIC`"
        type: str
        choices:
            - "ATOMIC"
            - "NON_ATOMIC"
    state:
        description:
            - The state of the MetricData.
            - Use I(state=present) to create a MetricData.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create metric_data
  oci_monitoring_metric_data:
    # required
    metric_data:
    - # required
      namespace: my_namespace
      compartment_id: "ocid1.compartment.oc1..exampleuniqueID"
      name: my_app.success_rate
      dimensions: null
      datapoints:
      - # required
        timestamp: 2019-02-01T01:02:29.600Z
        value: 10.23

        # optional
        count: 56

      # optional
      resource_group: frontend-fleet
      metadata: null

    # optional
    batch_atomicity: NON_ATOMIC

"""

RETURN = """
metric_data:
    description:
        - Details of the MetricData resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        failed_metrics_count:
            description:
                - The number of metric objects that failed input validation.
            returned: on success
            type: int
            sample: 56
        failed_metrics:
            description:
                - A list of records identifying metric objects that failed input validation
                  and the reasons for the failures.
            returned: on success
            type: complex
            contains:
                message:
                    description:
                        - An error message indicating the reason that the indicated metric object failed input validation.
                    returned: on success
                    type: str
                    sample: message_example
                metric_data:
                    description:
                        - Identifier of a metric object that failed input validation.
                    returned: on success
                    type: complex
                    contains:
                        namespace:
                            description:
                                - The source service or application emitting the metric.
                                - "A valid namespace value starts with an alphabetical character and includes only alphanumeric characters and underscores. The
                                  \\"oci_\\" prefix is reserved.
                                  Avoid entering confidential information."
                                - "Example: `my_namespace`"
                            returned: on success
                            type: str
                            sample: my_namespace
                        resource_group:
                            description:
                                - Resource group to assign to the metric. A resource group is a custom string that you can match when retrieving custom metrics.
                                  Only one resource group can be applied per metric.
                                  A valid resourceGroup value starts with an alphabetical character and includes only alphanumeric characters, periods (.),
                                  underscores (_), hyphens (-), and dollar signs ($).
                                  Avoid entering confidential information.
                                - "Example: `frontend-fleet`"
                            returned: on success
                            type: str
                            sample: frontend-fleet
                        compartment_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to use for metrics.
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..exampleuniqueID"
                        name:
                            description:
                                - The name of the metric.
                                - A valid name value starts with an alphabetical character and includes only alphanumeric characters, dots, underscores,
                                  hyphens, and dollar signs. The `oci_` prefix is reserved.
                                  Avoid entering confidential information.
                                - "Example: `my_app.success_rate`"
                            returned: on success
                            type: str
                            sample: my_app.success_rate
                        dimensions:
                            description:
                                - Qualifiers provided in a metric definition. Available dimensions vary by metric namespace.
                                  Each dimension takes the form of a key-value pair.
                                  A valid dimension key includes only printable ASCII, excluding periods (.) and spaces. The character limit for a dimension key
                                  is 256.
                                  A valid dimension value includes only Unicode characters. The character limit for a dimension value is 256.
                                  Empty strings are not allowed for keys or values. Avoid entering confidential information.
                                - "Example: `\\"resourceId\\": \\"ocid1.instance.region1.phx.exampleuniqueID\\"`"
                            returned: on success
                            type: dict
                            sample: {}
                        metadata:
                            description:
                                - Properties describing metrics. These are not part of the unique fields identifying the metric.
                                  Each metadata item takes the form of a key-value pair. The character limit for a metadata key is 256. The character limit for
                                  a metadata value is 256.
                                - "Example: `\\"unit\\": \\"bytes\\"`"
                            returned: on success
                            type: dict
                            sample: {}
                        datapoints:
                            description:
                                - A list of metric values with timestamps. At least one data point is required per call.
                            returned: on success
                            type: complex
                            contains:
                                timestamp:
                                    description:
                                        - Timestamp for this metric value. Format defined by RFC3339.
                                        - "Example: `2019-02-01T01:02:29.600Z`"
                                    returned: on success
                                    type: str
                                    sample: "2019-02-01T01:02:29.600Z"
                                value:
                                    description:
                                        - Numeric value of the metric.
                                        - "Example: `10.23`"
                                    returned: on success
                                    type: float
                                    sample: 10.23
                                count:
                                    description:
                                        - The number of occurrences of the associated value in the set of data.
                                        - Default is 1. Value must be greater than zero.
                                    returned: on success
                                    type: int
                                    sample: 56
    sample: {
        "failed_metrics_count": 56,
        "failed_metrics": [{
            "message": "message_example",
            "metric_data": {
                "namespace": "my_namespace",
                "resource_group": "frontend-fleet",
                "compartment_id": "ocid1.compartment.oc1..exampleuniqueID",
                "name": "my_app.success_rate",
                "dimensions": {},
                "metadata": {},
                "datapoints": [{
                    "timestamp": "2019-02-01T01:02:29.600Z",
                    "value": 10.23,
                    "count": 56
                }]
            }
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.monitoring import MonitoringClient
    from oci.monitoring.models import PostMetricDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MetricDataHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return PostMetricDataDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.post_metric_data,
            call_fn_args=(),
            call_fn_kwargs=dict(post_metric_data_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


MetricDataHelperCustom = get_custom_class("MetricDataHelperCustom")


class ResourceHelper(MetricDataHelperCustom, MetricDataHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            metric_data=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    namespace=dict(type="str", required=True),
                    resource_group=dict(type="str"),
                    compartment_id=dict(type="str", required=True),
                    name=dict(type="str", required=True),
                    dimensions=dict(type="dict", required=True),
                    metadata=dict(type="dict"),
                    datapoints=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            timestamp=dict(type="str", required=True),
                            value=dict(type="float", required=True),
                            count=dict(type="int"),
                        ),
                    ),
                ),
            ),
            batch_atomicity=dict(type="str", choices=["ATOMIC", "NON_ATOMIC"]),
            state=dict(type="str", default="present", choices=["present"]),
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

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
