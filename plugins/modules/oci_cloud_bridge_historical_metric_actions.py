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
module: oci_cloud_bridge_historical_metric_actions
short_description: Perform actions on a HistoricalMetric resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a HistoricalMetric resource in Oracle Cloud Infrastructure
    - For I(action=submit), creates or updates all metrics related to the asset.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    historical_metrics:
        description:
            - List of asset historical metrics.
        type: list
        elements: dict
        required: true
        suboptions:
            name:
                description:
                    - Metric name.
                type: str
                required: true
            aggregation:
                description:
                    - Aggregation time interval.
                type: str
                required: true
            value:
                description:
                    - Aggregation value.
                type: float
                required: true
    asset_id:
        description:
            - Unique asset identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the HistoricalMetric.
        type: str
        required: true
        choices:
            - "submit"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action submit on historical_metric
  oci_cloud_bridge_historical_metric_actions:
    # required
    historical_metrics:
    - # required
      name: name_example
      aggregation: aggregation_example
      value: 3.4
    asset_id: "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx"
    action: submit

"""

RETURN = """
historical_metric_collection:
    description:
        - Details of the HistoricalMetric resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Metric name.
            returned: on success
            type: str
            sample: name_example
        aggregation:
            description:
                - Aggregation time interval.
            returned: on success
            type: str
            sample: aggregation_example
        value:
            description:
                - Aggregation value.
            returned: on success
            type: float
            sample: 3.4
        time_created:
            description:
                - The time the HistoricalMetric was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the HistoricalMetric was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "name": "name_example",
        "aggregation": "aggregation_example",
        "value": 3.4,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.cloud_bridge import InventoryClient
    from oci.cloud_bridge.models import SubmitHistoricalMetricsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HistoricalMetricActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        submit
    """

    @staticmethod
    def get_module_resource_id_param():
        return "asset_id"

    def get_module_resource_id(self):
        return self.module.params.get("asset_id")

    def submit(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SubmitHistoricalMetricsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.submit_historical_metrics,
            call_fn_args=(),
            call_fn_kwargs=dict(
                submit_historical_metrics_details=action_details,
                asset_id=self.module.params.get("asset_id"),
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


HistoricalMetricActionsHelperCustom = get_custom_class(
    "HistoricalMetricActionsHelperCustom"
)


class ResourceHelper(
    HistoricalMetricActionsHelperCustom, HistoricalMetricActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            historical_metrics=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    name=dict(type="str", required=True),
                    aggregation=dict(type="str", required=True),
                    value=dict(type="float", required=True),
                ),
            ),
            asset_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["submit"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="historical_metric",
        service_client_class=InventoryClient,
        namespace="cloud_bridge",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
