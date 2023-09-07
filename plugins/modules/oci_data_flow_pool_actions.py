#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_data_flow_pool_actions
short_description: Perform actions on a Pool resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Pool resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a pool into a different compartment. When provided, If-Match is checked against ETag
      values of the resource. Associated resources, like historical metrics, will not be
      automatically moved. The pool must be in a terminal state (STOPPED, FAILED) in
      order for it to be moved to a different compartment
    - For I(action=start), starts the dataflow pool for a given `poolId`. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=stop), stops the dataflow pool for a given `poolId`. When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of a compartment.
            - Required for I(action=change_compartment).
        type: str
    pool_id:
        description:
            - The unique ID for a pool.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Pool.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on pool
  oci_data_flow_pool_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    pool_id: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action start on pool
  oci_data_flow_pool_actions:
    # required
    pool_id: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"
    action: start

- name: Perform action stop on pool
  oci_data_flow_pool_actions:
    # required
    pool_id: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"
    action: stop

"""

RETURN = """
pool:
    description:
        - Details of the Pool resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        description:
            description:
                - A user-friendly description. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - A user-friendly name. It does not have to be unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of a pool. Unique Id to indentify a dataflow pool resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_details:
            description:
                - The detailed messages about the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of this pool.
            returned: on success
            type: str
            sample: ACCEPTED
        owner_principal_id:
            description:
                - The OCID of the user who created the resource.
            returned: on success
            type: str
            sample: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        owner_user_name:
            description:
                - The username of the user who created the resource.  If the username of the owner does not exist,
                  `null` will be returned and the caller should refer to the ownerPrincipalId value instead.
            returned: on success
            type: str
            sample: owner_user_name_example
        pool_metrics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_last_started:
                    description:
                        - The last time this pool was started.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_stopped:
                    description:
                        - The last time this pool was stopped.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_used:
                    description:
                        - The last time a run used this pool.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_metrics_updated:
                    description:
                        - The last time the mertics were updated for this.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                active_runs_count:
                    description:
                        - The number of runs that are currently running that are using this pool.
                    returned: on success
                    type: int
                    sample: 56
                actively_used_node_count:
                    description:
                        - A count of the nodes that are currently being used for each shape in this pool.
                    returned: on success
                    type: complex
                    contains:
                        logical_shape:
                            description:
                                - The compute shape of the nodes that the count is for.
                            returned: on success
                            type: str
                            sample: logical_shape_example
                        count:
                            description:
                                - The node count of this compute shape.
                            returned: on success
                            type: int
                            sample: 56
        configurations:
            description:
                - List of PoolConfig items.
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - The compute shape of the resources you would like to provision.
                    returned: on success
                    type: str
                    sample: shape_example
                shape_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - The total number of OCPUs used for the driver or executors.
                                  See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                            returned: on success
                            type: float
                            sample: 10
                        memory_in_gbs:
                            description:
                                - The amount of memory used for the driver or executors.
                            returned: on success
                            type: float
                            sample: 10
                min:
                    description:
                        - Minimum number of compute instances in the pool for a given compute shape.
                    returned: on success
                    type: int
                    sample: 56
                max:
                    description:
                        - Maximum number of compute instances in the pool for a given compute shape.
                    returned: on success
                    type: int
                    sample: 56
        schedules:
            description:
                - A list of schedules for pool to auto start and stop.
            returned: on success
            type: complex
            contains:
                day_of_week:
                    description:
                        - Day of the week SUN-SAT
                    returned: on success
                    type: str
                    sample: SUNDAY
                start_time:
                    description:
                        - Hour of the day to start or stop pool.
                    returned: on success
                    type: int
                    sample: 56
                stop_time:
                    description:
                        - Hour of the day to stop the pool.
                    returned: on success
                    type: int
                    sample: 56
        idle_timeout_in_minutes:
            description:
                - Optional timeout value in minutes used to auto stop Pools. A Pool will be auto stopped after inactivity for this amount of time period.
                  If value not set, pool will not be auto stopped auto.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - "The date and time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACCEPTED",
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_user_name": "owner_user_name_example",
        "pool_metrics": {
            "time_last_started": "2013-10-20T19:20:30+01:00",
            "time_last_stopped": "2013-10-20T19:20:30+01:00",
            "time_last_used": "2013-10-20T19:20:30+01:00",
            "time_last_metrics_updated": "2013-10-20T19:20:30+01:00",
            "active_runs_count": 56,
            "actively_used_node_count": [{
                "logical_shape": "logical_shape_example",
                "count": 56
            }]
        },
        "configurations": [{
            "shape": "shape_example",
            "shape_config": {
                "ocpus": 10,
                "memory_in_gbs": 10
            },
            "min": 56,
            "max": 56
        }],
        "schedules": [{
            "day_of_week": "SUNDAY",
            "start_time": 56,
            "stop_time": 56
        }],
        "idle_timeout_in_minutes": 56,
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
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import ChangePoolCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowPoolActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("pool_id")

    def get_get_fn(self):
        return self.client.get_pool

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pool, pool_id=self.module.params.get("pool_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePoolCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_pool_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pool_id=self.module.params.get("pool_id"),
                change_pool_compartment_details=action_details,
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

    def start(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(pool_id=self.module.params.get("pool_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def stop(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(pool_id=self.module.params.get("pool_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataFlowPoolActionsHelperCustom = get_custom_class("DataFlowPoolActionsHelperCustom")


class ResourceHelper(DataFlowPoolActionsHelperCustom, DataFlowPoolActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            pool_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["change_compartment", "start", "stop"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="pool",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
