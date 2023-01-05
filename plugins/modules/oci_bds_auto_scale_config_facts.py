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
module: oci_bds_auto_scale_config_facts
short_description: Fetches details about one or multiple BdsAutoScaleConfig resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BdsAutoScaleConfig resources in Oracle Cloud Infrastructure
    - Returns information about the autoscaling configurations for a cluster.
    - If I(auto_scaling_configuration_id) is specified, the details of a single BdsAutoScaleConfig will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    auto_scaling_configuration_id:
        description:
            - Unique Oracle-assigned identifier of the autoscale configuration.
            - Required to get a specific bds_auto_scale_config.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple bds_auto_scale_configs.
        type: str
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - The state of the autoscale configuration.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific bds_auto_scale_config
  oci_bds_auto_scale_config_facts:
    # required
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List bds_auto_scale_configs
  oci_bds_auto_scale_config_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: timeCreated
    sort_order: ASC
    display_name: display_name_example
    lifecycle_state: CREATING

"""

RETURN = """
bds_auto_scale_configs:
    description:
        - List of BdsAutoScaleConfig resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier for the autoscale configuration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The state of the autoscale configuration.
            returned: on success
            type: str
            sample: CREATING
        node_type:
            description:
                - A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.
            returned: on success
            type: str
            sample: node_type_example
        time_created:
            description:
                - The time the cluster was created, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the autoscale configuration was updated, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                policy_type:
                    description:
                        - Types of autoscale policies. Options are SCHEDULE-BASED or THRESHOLD-BASED. (Only THRESHOLD-BASED is supported in this release.)
                    returned: on success
                    type: str
                    sample: THRESHOLD_BASED
                rules:
                    description:
                        - The list of rules for autoscaling. If an action has multiple rules, the last rule in the array will be applied.
                    returned: on success
                    type: complex
                    contains:
                        action:
                            description:
                                - The valid value are CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN.
                            returned: on success
                            type: str
                            sample: CHANGE_SHAPE_SCALE_UP
                        metric:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                metric_type:
                                    description:
                                        - Allowed value is CPU_UTILIZATION.
                                    returned: on success
                                    type: str
                                    sample: CPU_UTILIZATION
                                threshold:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        duration_in_minutes:
                                            description:
                                                - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                                  triggered. The value is in minutes.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        operator:
                                            description:
                                                - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            returned: on success
                                            type: str
                                            sample: GT
                                        value:
                                            description:
                                                - Integer non-negative value. 0 < value < 100
                                            returned: on success
                                            type: int
                                            sample: 56
        policy_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                scale_out_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        metric:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                metric_type:
                                    description:
                                        - Allowed value is CPU_UTILIZATION.
                                    returned: on success
                                    type: str
                                    sample: CPU_UTILIZATION
                                threshold:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        duration_in_minutes:
                                            description:
                                                - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                                  triggered. The value is in minutes.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        operator:
                                            description:
                                                - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            returned: on success
                                            type: str
                                            sample: GT
                                        value:
                                            description:
                                                - Integer non-negative value. 0 < value < 100
                                            returned: on success
                                            type: int
                                            sample: 56
                        max_node_count:
                            description:
                                - This value is the maximum number of nodes the cluster can be scaled-out to.
                            returned: on success
                            type: int
                            sample: 56
                        step_size:
                            description:
                                - This value is the number of nodes to add during a scale-out event.
                            returned: on success
                            type: int
                            sample: 56
                scale_in_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        metric:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                metric_type:
                                    description:
                                        - Allowed value is CPU_UTILIZATION.
                                    returned: on success
                                    type: str
                                    sample: CPU_UTILIZATION
                                threshold:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        duration_in_minutes:
                                            description:
                                                - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                                  triggered. The value is in minutes.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        operator:
                                            description:
                                                - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            returned: on success
                                            type: str
                                            sample: GT
                                        value:
                                            description:
                                                - Integer non-negative value. 0 < value < 100
                                            returned: on success
                                            type: int
                                            sample: 56
                        min_node_count:
                            description:
                                - This value is the minimum number of nodes the cluster can be scaled-in to.
                            returned: on success
                            type: int
                            sample: 56
                        step_size:
                            description:
                                - This value is the number of nodes to remove during a scale-in event.
                            returned: on success
                            type: int
                            sample: 56
                scale_up_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        metric:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                metric_type:
                                    description:
                                        - Allowed value is CPU_UTILIZATION.
                                    returned: on success
                                    type: str
                                    sample: CPU_UTILIZATION
                                threshold:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        duration_in_minutes:
                                            description:
                                                - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                                  triggered. The value is in minutes.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        operator:
                                            description:
                                                - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            returned: on success
                                            type: str
                                            sample: GT
                                        value:
                                            description:
                                                - Integer non-negative value. 0 < value < 100
                                            returned: on success
                                            type: int
                                            sample: 56
                        max_ocpus_per_node:
                            description:
                                - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                  shape), this value is the maximum number of OCPUs each node can be scaled-up to. This value is not used for nodes with fixed
                                  compute shapes.
                            returned: on success
                            type: int
                            sample: 56
                        max_memory_per_node:
                            description:
                                - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                  shape), this value is the maximum memory in GBs each node can be scaled-up to. This value is not used for nodes with fixed
                                  compute shapes.
                            returned: on success
                            type: int
                            sample: 56
                        ocpu_step_size:
                            description:
                                - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                  shape), this value is the number of OCPUs to add to each node during a scale-up event. This value is not used for nodes with
                                  fixed compute shapes.
                            returned: on success
                            type: int
                            sample: 56
                        memory_step_size:
                            description:
                                - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                  shape), this value is the size of memory in GBs to add to each node during a scale-up event. This value is not used for nodes
                                  with fixed compute shapes.
                            returned: on success
                            type: int
                            sample: 56
                scale_down_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        metric:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                metric_type:
                                    description:
                                        - Allowed value is CPU_UTILIZATION.
                                    returned: on success
                                    type: str
                                    sample: CPU_UTILIZATION
                                threshold:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        duration_in_minutes:
                                            description:
                                                - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                                  triggered. The value is in minutes.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        operator:
                                            description:
                                                - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            returned: on success
                                            type: str
                                            sample: GT
                                        value:
                                            description:
                                                - Integer non-negative value. 0 < value < 100
                                            returned: on success
                                            type: int
                                            sample: 56
                        min_ocpus_per_node:
                            description:
                                - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                  shape), this value is the minimum number of OCPUs each node can be scaled-down to. This value is not used for nodes with fixed
                                  compute shapes.
                            returned: on success
                            type: int
                            sample: 56
                        min_memory_per_node:
                            description:
                                - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                  shape), this value is the minimum memory in GBs each node can be scaled-down to. This value is not used for nodes with fixed
                                  compute shapes.
                            returned: on success
                            type: int
                            sample: 56
                        ocpu_step_size:
                            description:
                                - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                  shape), this value is the number of OCPUs to remove from each node during a scale-down event. This value is not used for nodes
                                  with fixed compute shapes.
                            returned: on success
                            type: int
                            sample: 56
                        memory_step_size:
                            description:
                                - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                  shape), this value is the size of memory in GBs to remove from each node during a scale-down event. This value is not used for
                                  nodes with fixed compute shapes.
                            returned: on success
                            type: int
                            sample: 56
                policy_type:
                    description:
                        - Type of autoscaling policy.
                    returned: on success
                    type: str
                    sample: METRIC_BASED_VERTICAL_SCALING_POLICY
                trigger_type:
                    description:
                        - The type of autoscaling trigger.
                    returned: on success
                    type: str
                    sample: METRIC_BASED
                action_type:
                    description:
                        - The type of autoscaling action to take.
                    returned: on success
                    type: str
                    sample: VERTICAL_SCALING
                timezone:
                    description:
                        - The time zone of the execution schedule, in IANA time zone database name format
                    returned: on success
                    type: str
                    sample: timezone_example
                schedule_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        schedule_type:
                            description:
                                - The type of schedule.
                            returned: on success
                            type: str
                            sample: DAY_BASED
                        time_and_horizontal_scaling_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                time_recurrence:
                                    description:
                                        - Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY
                                          frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR
                                          and BYMINUTE fields. Other fields are not supported.
                                    returned: on success
                                    type: str
                                    sample: time_recurrence_example
                                target_node_count:
                                    description:
                                        - This value is the desired number of nodes in the cluster.
                                    returned: on success
                                    type: int
                                    sample: 56
                        time_and_vertical_scaling_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                time_recurrence:
                                    description:
                                        - Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY
                                          frequency is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR
                                          and BYMINUTE fields. Other fields are not supported.
                                    returned: on success
                                    type: str
                                    sample: time_recurrence_example
                                target_shape:
                                    description:
                                        - For nodes with L(fixed compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-
                                          plan-shape), this value is the desired shape of each node. This value is not used for nodes with flexible compute
                                          shapes.
                                    returned: on success
                                    type: str
                                    sample: target_shape_example
                                target_ocpus_per_node:
                                    description:
                                        - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-
                                          cluster.htm#cluster-plan-shape), this value is the desired OCPUs count on each node. This value is not used for nodes
                                          with fixed compute shapes.
                                    returned: on success
                                    type: int
                                    sample: 56
                                target_memory_per_node:
                                    description:
                                        - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-
                                          cluster.htm#cluster-plan-shape), this value is the desired memory in GBs on each node. This value is not used for
                                          nodes with fixed compute shapes.
                                    returned: on success
                                    type: int
                                    sample: 56
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "node_type": "node_type_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "policy": {
            "policy_type": "THRESHOLD_BASED",
            "rules": [{
                "action": "CHANGE_SHAPE_SCALE_UP",
                "metric": {
                    "metric_type": "CPU_UTILIZATION",
                    "threshold": {
                        "duration_in_minutes": 56,
                        "operator": "GT",
                        "value": 56
                    }
                }
            }]
        },
        "policy_details": {
            "scale_out_config": {
                "metric": {
                    "metric_type": "CPU_UTILIZATION",
                    "threshold": {
                        "duration_in_minutes": 56,
                        "operator": "GT",
                        "value": 56
                    }
                },
                "max_node_count": 56,
                "step_size": 56
            },
            "scale_in_config": {
                "metric": {
                    "metric_type": "CPU_UTILIZATION",
                    "threshold": {
                        "duration_in_minutes": 56,
                        "operator": "GT",
                        "value": 56
                    }
                },
                "min_node_count": 56,
                "step_size": 56
            },
            "scale_up_config": {
                "metric": {
                    "metric_type": "CPU_UTILIZATION",
                    "threshold": {
                        "duration_in_minutes": 56,
                        "operator": "GT",
                        "value": 56
                    }
                },
                "max_ocpus_per_node": 56,
                "max_memory_per_node": 56,
                "ocpu_step_size": 56,
                "memory_step_size": 56
            },
            "scale_down_config": {
                "metric": {
                    "metric_type": "CPU_UTILIZATION",
                    "threshold": {
                        "duration_in_minutes": 56,
                        "operator": "GT",
                        "value": 56
                    }
                },
                "min_ocpus_per_node": 56,
                "min_memory_per_node": 56,
                "ocpu_step_size": 56,
                "memory_step_size": 56
            },
            "policy_type": "METRIC_BASED_VERTICAL_SCALING_POLICY",
            "trigger_type": "METRIC_BASED",
            "action_type": "VERTICAL_SCALING",
            "timezone": "timezone_example",
            "schedule_details": [{
                "schedule_type": "DAY_BASED",
                "time_and_horizontal_scaling_config": [{
                    "time_recurrence": "time_recurrence_example",
                    "target_node_count": 56
                }],
                "time_and_vertical_scaling_config": [{
                    "time_recurrence": "time_recurrence_example",
                    "target_shape": "target_shape_example",
                    "target_ocpus_per_node": 56,
                    "target_memory_per_node": 56
                }]
            }]
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.bds import BdsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsAutoScaleConfigFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "bds_instance_id",
            "auto_scaling_configuration_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "bds_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_auto_scaling_configurations,
            compartment_id=self.module.params.get("compartment_id"),
            bds_instance_id=self.module.params.get("bds_instance_id"),
            **optional_kwargs
        )


BdsAutoScaleConfigFactsHelperCustom = get_custom_class(
    "BdsAutoScaleConfigFactsHelperCustom"
)


class ResourceFactsHelper(
    BdsAutoScaleConfigFactsHelperCustom, BdsAutoScaleConfigFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            auto_scaling_configuration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            bds_instance_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bds_auto_scale_config",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(bds_auto_scale_configs=result)


if __name__ == "__main__":
    main()
