#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_apm_synthetics_aggregated_network_data_result_actions
short_description: Perform actions on an AggregatedNetworkDataResult resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AggregatedNetworkDataResult resource in Oracle Cloud Infrastructure
    - For I(action=aggregate_network_data), gets aggregated network data for given executions.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    monitor_id:
        description:
            - The OCID of the monitor.
        type: str
        aliases: ["id"]
        required: true
    vantage_point_execution_times:
        description:
            - List of VantagePointExecution items.
        type: list
        elements: dict
        required: true
        suboptions:
            name:
                description:
                    - Name of the vantage point.
                type: str
            executions:
                description:
                    - List of execution times in milliseconds.
                type: list
                elements: long
    action:
        description:
            - The action to perform on the AggregatedNetworkDataResult.
        type: str
        required: true
        choices:
            - "aggregate_network_data"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action aggregate_network_data on aggregated_network_data_result
  oci_apm_synthetics_aggregated_network_data_result_actions:
    # required
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"
    monitor_id: "ocid1.monitor.oc1..xxxxxxEXAMPLExxxxxx"
    vantage_point_execution_times:
    - # optional
      name: name_example
      executions: [ "executions_example" ]
    action: aggregate_network_data

"""

RETURN = """
aggregated_network_data_result:
    description:
        - Details of the AggregatedNetworkDataResult resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        aggregated_network_data:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                result_state:
                    description:
                        - Status of the aggregated network data result.
                    returned: on success
                    type: str
                    sample: SUCCESS
                vantage_point_nodes:
                    description:
                        - List of vantage point nodes.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - ID of the vantage point node.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        name:
                            description:
                                - Name of the vantage point node.
                            returned: on success
                            type: str
                            sample: name_example
                        display_name:
                            description:
                                - Display name of the vantage point node.
                            returned: on success
                            type: str
                            sample: display_name_example
                        geo_info:
                            description:
                                - Geographical information of the vantage point node.
                            returned: on success
                            type: str
                            sample: geo_info_example
                        outgoing_links:
                            description:
                                - Outgoing links from the vantage point node.
                            returned: on success
                            type: list
                            sample: []
                nodes_by_level:
                    description:
                        - An array of node arrays where each internal array corresponds to nodes at one level.
                    returned: on success
                    type: list
                    sample: []
                links:
                    description:
                        - Map of link objects.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - ID of the link.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        source:
                            description:
                                - ID of the source node.
                            returned: on success
                            type: str
                            sample: source_example
                        destination:
                            description:
                                - ID of the destination node.
                            returned: on success
                            type: str
                            sample: destination_example
                        repeat_count:
                            description:
                                - Number of times the link is repeated.
                            returned: on success
                            type: int
                            sample: 56
                        forwarding_loss:
                            description:
                                - Average packet loss.
                            returned: on success
                            type: float
                            sample: 1.2
                        delay_in_milliseconds:
                            description:
                                - Difference of the packet response time between source and destination nodes, in milliseconds.
                            returned: on success
                            type: float
                            sample: 1.2
                        min_delay_in_milliseconds:
                            description:
                                - Minimum delay in milliseconds.
                            returned: on success
                            type: float
                            sample: 1.2
                        max_delay_in_milliseconds:
                            description:
                                - Maximum delay in milliseconds.
                            returned: on success
                            type: float
                            sample: 1.2
                        paths:
                            description:
                                - List of all path IDs of which this link is part of.
                            returned: on success
                            type: list
                            sample: []
                error_details:
                    description:
                        - String containing error details.
                    returned: on success
                    type: str
                    sample: error_details_example
    sample: {
        "aggregated_network_data": {
            "result_state": "SUCCESS",
            "vantage_point_nodes": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "name": "name_example",
                "display_name": "display_name_example",
                "geo_info": "geo_info_example",
                "outgoing_links": []
            }],
            "nodes_by_level": [],
            "links": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "source": "source_example",
                "destination": "destination_example",
                "repeat_count": 56,
                "forwarding_loss": 1.2,
                "delay_in_milliseconds": 1.2,
                "min_delay_in_milliseconds": 1.2,
                "max_delay_in_milliseconds": 1.2,
                "paths": []
            },
            "error_details": "error_details_example"
        }
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
    from oci.apm_synthetics import ApmSyntheticClient
    from oci.apm_synthetics.models import AggregateNetworkDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AggregatedNetworkDataResultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        aggregate_network_data
    """

    @staticmethod
    def get_module_resource_id_param():
        return "monitor_id"

    def get_module_resource_id(self):
        return self.module.params.get("monitor_id")

    def aggregate_network_data(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AggregateNetworkDataDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.aggregate_network_data,
            call_fn_args=(),
            call_fn_kwargs=dict(
                apm_domain_id=self.module.params.get("apm_domain_id"),
                monitor_id=self.module.params.get("monitor_id"),
                aggregate_network_data_details=action_details,
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


AggregatedNetworkDataResultActionsHelperCustom = get_custom_class(
    "AggregatedNetworkDataResultActionsHelperCustom"
)


class ResourceHelper(
    AggregatedNetworkDataResultActionsHelperCustom,
    AggregatedNetworkDataResultActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            monitor_id=dict(aliases=["id"], type="str", required=True),
            vantage_point_execution_times=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    name=dict(type="str"), executions=dict(type="list", elements="long")
                ),
            ),
            action=dict(type="str", required=True, choices=["aggregate_network_data"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="aggregated_network_data_result",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
