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
module: oci_bds_auto_scale_config
short_description: Manage a BdsAutoScaleConfig resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BdsAutoScaleConfig resource in Oracle Cloud Infrastructure
    - For I(state=present), add an autoscale configuration to the cluster.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    node_type:
        description:
            - A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name. The name does not have to be unique, and it may be changed. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    is_enabled:
        description:
            - Whether the autoscale configuration is enabled.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    policy:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            policy_type:
                description:
                    - Types of autoscale policies. Options are SCHEDULE-BASED or THRESHOLD-BASED. (Only THRESHOLD-BASED is supported in this release.)
                type: str
                choices:
                    - "THRESHOLD_BASED"
                    - "SCHEDULE_BASED"
                    - "NONE"
                required: true
            rules:
                description:
                    - The list of rules for autoscaling. If an action has multiple rules, the last rule in the array will be applied.
                type: list
                elements: dict
                required: true
                suboptions:
                    action:
                        description:
                            - The valid value are CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN.
                        type: str
                        choices:
                            - "CHANGE_SHAPE_SCALE_UP"
                            - "CHANGE_SHAPE_SCALE_DOWN"
                        required: true
                    metric:
                        description:
                            - ""
                        type: dict
                        required: true
                        suboptions:
                            metric_type:
                                description:
                                    - Allowed value is CPU_UTILIZATION.
                                type: str
                                choices:
                                    - "CPU_UTILIZATION"
                                required: true
                            threshold:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    duration_in_minutes:
                                        description:
                                            - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                              triggered. The value is in minutes.
                                        type: int
                                        required: true
                                    operator:
                                        description:
                                            - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                        type: str
                                        choices:
                                            - "GT"
                                            - "LT"
                                        required: true
                                    value:
                                        description:
                                            - Integer non-negative value. 0 < value < 100
                                        type: int
                                        required: true
    policy_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            scale_up_config:
                description:
                    - ""
                    - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                type: dict
                suboptions:
                    metric:
                        description:
                            - ""
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: dict
                        suboptions:
                            metric_type:
                                description:
                                    - Allowed value is CPU_UTILIZATION.
                                    - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                type: str
                                choices:
                                    - "CPU_UTILIZATION"
                                required: true
                            threshold:
                                description:
                                    - ""
                                    - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                type: dict
                                required: true
                                suboptions:
                                    duration_in_minutes:
                                        description:
                                            - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                              triggered. The value is in minutes.
                                            - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                        type: int
                                        required: true
                                    operator:
                                        description:
                                            - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                        type: str
                                        choices:
                                            - "GT"
                                            - "LT"
                                        required: true
                                    value:
                                        description:
                                            - Integer non-negative value. 0 < value < 100
                                            - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                        type: int
                                        required: true
                    max_ocpus_per_node:
                        description:
                            - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                              shape), this value is the maximum number of OCPUs each node can be scaled-up to. This value is not used for nodes with fixed
                              compute shapes.
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: int
                    max_memory_per_node:
                        description:
                            - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                              shape), this value is the maximum memory in GBs each node can be scaled-up to. This value is not used for nodes with fixed compute
                              shapes.
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: int
                    ocpu_step_size:
                        description:
                            - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                              shape), this value is the number of OCPUs to add to each node during a scale-up event. This value is not used for nodes with fixed
                              compute shapes.
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: int
                    memory_step_size:
                        description:
                            - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                              shape), this value is the size of memory in GBs to add to each node during a scale-up event. This value is not used for nodes with
                              fixed compute shapes.
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: int
            scale_down_config:
                description:
                    - ""
                    - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                type: dict
                suboptions:
                    metric:
                        description:
                            - ""
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: dict
                        suboptions:
                            metric_type:
                                description:
                                    - Allowed value is CPU_UTILIZATION.
                                    - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                type: str
                                choices:
                                    - "CPU_UTILIZATION"
                                required: true
                            threshold:
                                description:
                                    - ""
                                    - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                type: dict
                                required: true
                                suboptions:
                                    duration_in_minutes:
                                        description:
                                            - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                              triggered. The value is in minutes.
                                            - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                        type: int
                                        required: true
                                    operator:
                                        description:
                                            - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                        type: str
                                        choices:
                                            - "GT"
                                            - "LT"
                                        required: true
                                    value:
                                        description:
                                            - Integer non-negative value. 0 < value < 100
                                            - Required when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                                        type: int
                                        required: true
                    min_ocpus_per_node:
                        description:
                            - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                              shape), this value is the minimum number of OCPUs each node can be scaled-down to. This value is not used for nodes with fixed
                              compute shapes.
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: int
                    min_memory_per_node:
                        description:
                            - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                              shape), this value is the minimum memory in GBs each node can be scaled-down to. This value is not used for nodes with fixed
                              compute shapes.
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: int
                    ocpu_step_size:
                        description:
                            - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                              shape), this value is the number of OCPUs to remove from each node during a scale-down event. This value is not used for nodes
                              with fixed compute shapes.
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: int
                    memory_step_size:
                        description:
                            - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                              shape), this value is the size of memory in GBs to remove from each node during a scale-down event. This value is not used for
                              nodes with fixed compute shapes.
                            - Applicable when policy_type is 'METRIC_BASED_VERTICAL_SCALING_POLICY'
                        type: int
            scale_out_config:
                description:
                    - ""
                    - Applicable when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                type: dict
                suboptions:
                    metric:
                        description:
                            - ""
                            - Applicable when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                        type: dict
                        suboptions:
                            metric_type:
                                description:
                                    - Allowed value is CPU_UTILIZATION.
                                    - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                type: str
                                choices:
                                    - "CPU_UTILIZATION"
                                required: true
                            threshold:
                                description:
                                    - ""
                                    - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                type: dict
                                required: true
                                suboptions:
                                    duration_in_minutes:
                                        description:
                                            - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                              triggered. The value is in minutes.
                                            - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                        type: int
                                        required: true
                                    operator:
                                        description:
                                            - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                        type: str
                                        choices:
                                            - "GT"
                                            - "LT"
                                        required: true
                                    value:
                                        description:
                                            - Integer non-negative value. 0 < value < 100
                                            - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                        type: int
                                        required: true
                    max_node_count:
                        description:
                            - This value is the maximum number of nodes the cluster can be scaled-out to.
                            - Applicable when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                        type: int
                    step_size:
                        description:
                            - This value is the number of nodes to add during a scale-out event.
                            - Applicable when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                        type: int
            scale_in_config:
                description:
                    - ""
                    - Applicable when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                type: dict
                suboptions:
                    metric:
                        description:
                            - ""
                            - Applicable when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                        type: dict
                        suboptions:
                            metric_type:
                                description:
                                    - Allowed value is CPU_UTILIZATION.
                                    - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                type: str
                                choices:
                                    - "CPU_UTILIZATION"
                                required: true
                            threshold:
                                description:
                                    - ""
                                    - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                type: dict
                                required: true
                                suboptions:
                                    duration_in_minutes:
                                        description:
                                            - This value is the minimum period of time the metric value exceeds the threshold value before the action is
                                              triggered. The value is in minutes.
                                            - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                        type: int
                                        required: true
                                    operator:
                                        description:
                                            - The comparison operator to use. Options are greater than (GT) or less than (LT).
                                            - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                        type: str
                                        choices:
                                            - "GT"
                                            - "LT"
                                        required: true
                                    value:
                                        description:
                                            - Integer non-negative value. 0 < value < 100
                                            - Required when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                                        type: int
                                        required: true
                    min_node_count:
                        description:
                            - This value is the minimum number of nodes the cluster can be scaled-in to.
                            - Applicable when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                        type: int
                    step_size:
                        description:
                            - This value is the number of nodes to remove during a scale-in event.
                            - Applicable when policy_type is 'METRIC_BASED_HORIZONTAL_SCALING_POLICY'
                        type: int
            policy_type:
                description:
                    - Type of autoscaling policy.
                    - This parameter is updatable.
                type: str
                choices:
                    - "METRIC_BASED_HORIZONTAL_SCALING_POLICY"
                    - "SCHEDULE_BASED_VERTICAL_SCALING_POLICY"
                    - "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY"
                    - "METRIC_BASED_VERTICAL_SCALING_POLICY"
                required: true
            timezone:
                description:
                    - The time zone of the execution schedule, in IANA time zone database name format
                    - This parameter is updatable.
                    - Applicable when policy_type is one of ['SCHEDULE_BASED_VERTICAL_SCALING_POLICY', 'SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY']
                type: str
            schedule_details:
                description:
                    - Details of a vertical scaling schedule.
                    - Applicable when policy_type is one of ['SCHEDULE_BASED_VERTICAL_SCALING_POLICY', 'SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY']
                type: list
                elements: dict
                suboptions:
                    time_and_horizontal_scaling_config:
                        description:
                            - Time of day and horizontal scaling configuration.
                        type: list
                        elements: dict
                        suboptions:
                            time_recurrence:
                                description:
                                    - Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency
                                      is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE
                                      fields. Other fields are not supported.
                                type: str
                            target_node_count:
                                description:
                                    - This value is the desired number of nodes in the cluster.
                                type: int
                    schedule_type:
                        description:
                            - The type of schedule.
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "DAY_BASED"
                        required: true
                    time_and_vertical_scaling_config:
                        description:
                            - Time of day and vertical scaling configuration
                        type: list
                        elements: dict
                        suboptions:
                            time_recurrence:
                                description:
                                    - Day/time recurrence (specified following RFC 5545) at which to trigger autoscaling action. Currently only WEEKLY frequency
                                      is supported. Days of the week are specified using BYDAY field. Time of the day is specified using BYHOUR and BYMINUTE
                                      fields. Other fields are not supported.
                                type: str
                            target_shape:
                                description:
                                    - For nodes with L(fixed compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-plan-
                                      shape), this value is the desired shape of each node. This value is not used for nodes with flexible compute shapes.
                                type: str
                            target_ocpus_per_node:
                                description:
                                    - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-
                                      plan-shape), this value is the desired OCPUs count on each node. This value is not used for nodes with fixed compute
                                      shapes.
                                type: int
                            target_memory_per_node:
                                description:
                                    - For nodes with L(flexible compute shapes,https://docs.cloud.oracle.com/iaas/Content/bigdata/create-cluster.htm#cluster-
                                      plan-shape), this value is the desired memory in GBs on each node. This value is not used for nodes with fixed compute
                                      shapes.
                                type: int
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    auto_scaling_configuration_id:
        description:
            - Unique Oracle-assigned identifier of the autoscale configuration.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    cluster_admin_password:
        description:
            - Base-64 encoded password for the cluster (and Cloudera Manager) admin user.
            - Required for create using I(state=present).
            - Required for delete using I(state=absent).
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the BdsAutoScaleConfig.
            - Use I(state=present) to create or update a BdsAutoScaleConfig.
            - Use I(state=absent) to delete a BdsAutoScaleConfig.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create bds_auto_scale_config
  oci_bds_auto_scale_config:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    node_type: node_type_example
    is_enabled: true
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password

    # optional
    display_name: display_name_example
    policy:
      # required
      policy_type: THRESHOLD_BASED
      rules:
      - # required
        action: CHANGE_SHAPE_SCALE_UP
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
    policy_details:
      # required
      policy_type: METRIC_BASED_HORIZONTAL_SCALING_POLICY

      # optional
      scale_out_config:
        # optional
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
        max_node_count: 56
        step_size: 56
      scale_in_config:
        # optional
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
        min_node_count: 56
        step_size: 56

- name: Update bds_auto_scale_config
  oci_bds_auto_scale_config:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    is_enabled: true
    policy:
      # required
      policy_type: THRESHOLD_BASED
      rules:
      - # required
        action: CHANGE_SHAPE_SCALE_UP
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
    policy_details:
      # required
      policy_type: METRIC_BASED_HORIZONTAL_SCALING_POLICY

      # optional
      scale_out_config:
        # optional
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
        max_node_count: 56
        step_size: 56
      scale_in_config:
        # optional
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
        min_node_count: 56
        step_size: 56
    cluster_admin_password: example-password

- name: Update bds_auto_scale_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bds_auto_scale_config:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_enabled: true
    policy:
      # required
      policy_type: THRESHOLD_BASED
      rules:
      - # required
        action: CHANGE_SHAPE_SCALE_UP
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
    policy_details:
      # required
      policy_type: METRIC_BASED_HORIZONTAL_SCALING_POLICY

      # optional
      scale_out_config:
        # optional
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
        max_node_count: 56
        step_size: 56
      scale_in_config:
        # optional
        metric:
          # required
          metric_type: CPU_UTILIZATION
          threshold:
            # required
            duration_in_minutes: 56
            operator: GT
            value: 56
        min_node_count: 56
        step_size: 56
    cluster_admin_password: example-password

- name: Delete bds_auto_scale_config
  oci_bds_auto_scale_config:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    state: absent

- name: Delete bds_auto_scale_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bds_auto_scale_config:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
bds_auto_scale_config:
    description:
        - Details of the BdsAutoScaleConfig resource acted upon by the current operation
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
        node_type:
            description:
                - A node type that is managed by an autoscale configuration. The only supported types are WORKER and COMPUTE_ONLY_WORKER.
            returned: on success
            type: str
            sample: node_type_example
        lifecycle_state:
            description:
                - The state of the autoscale configuration.
            returned: on success
            type: str
            sample: CREATING
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
                        - Details of a horizontal scaling schedule.
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
                                - Time of day and horizontal scaling configuration.
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
                                - Time of day and vertical scaling configuration
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "node_type": "node_type_example",
        "lifecycle_state": "CREATING",
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
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.bds import BdsClient
    from oci.bds.models import AddAutoScalingConfigurationDetails
    from oci.bds.models import UpdateAutoScalingConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsAutoScaleConfigHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(BdsAutoScaleConfigHelperGen, self).get_possible_entity_types() + [
            "bdsautoscaleconfig",
            "bdsautoscaleconfigs",
            "bdsbdsautoscaleconfig",
            "bdsbdsautoscaleconfigs",
            "bdsautoscaleconfigresource",
            "bdsautoscaleconfigsresource",
            "autoscalingconfiguration",
            "autoscalingconfigurations",
            "bdsautoscalingconfiguration",
            "bdsautoscalingconfigurations",
            "autoscalingconfigurationresource",
            "autoscalingconfigurationsresource",
            "bds",
        ]

    def get_module_resource_id_param(self):
        return "auto_scaling_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("auto_scaling_configuration_id")

    def get_get_fn(self):
        return self.client.get_auto_scaling_configuration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            auto_scaling_configuration_id=summary_model.id,
            bds_instance_id=self.module.params.get("bds_instance_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "bds_instance_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_auto_scaling_configurations, **kwargs
        )

    def get_create_model_class(self):
        return AddAutoScalingConfigurationDetails

    def get_exclude_attributes(self):
        return ["is_enabled", "cluster_admin_password"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_auto_scaling_configuration_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAutoScalingConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                update_auto_scaling_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                remove_auto_scaling_configuration_details=self.module.params.get(
                    "remove_auto_scaling_configuration_details"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BdsAutoScaleConfigHelperCustom = get_custom_class("BdsAutoScaleConfigHelperCustom")


class ResourceHelper(BdsAutoScaleConfigHelperCustom, BdsAutoScaleConfigHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            node_type=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_enabled=dict(type="bool"),
            policy=dict(
                type="dict",
                options=dict(
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=["THRESHOLD_BASED", "SCHEDULE_BASED", "NONE"],
                    ),
                    rules=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            action=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "CHANGE_SHAPE_SCALE_UP",
                                    "CHANGE_SHAPE_SCALE_DOWN",
                                ],
                            ),
                            metric=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            policy_details=dict(
                type="dict",
                options=dict(
                    scale_up_config=dict(
                        type="dict",
                        options=dict(
                            metric=dict(
                                type="dict",
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            max_ocpus_per_node=dict(type="int"),
                            max_memory_per_node=dict(type="int"),
                            ocpu_step_size=dict(type="int"),
                            memory_step_size=dict(type="int"),
                        ),
                    ),
                    scale_down_config=dict(
                        type="dict",
                        options=dict(
                            metric=dict(
                                type="dict",
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            min_ocpus_per_node=dict(type="int"),
                            min_memory_per_node=dict(type="int"),
                            ocpu_step_size=dict(type="int"),
                            memory_step_size=dict(type="int"),
                        ),
                    ),
                    scale_out_config=dict(
                        type="dict",
                        options=dict(
                            metric=dict(
                                type="dict",
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            max_node_count=dict(type="int"),
                            step_size=dict(type="int"),
                        ),
                    ),
                    scale_in_config=dict(
                        type="dict",
                        options=dict(
                            metric=dict(
                                type="dict",
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CPU_UTILIZATION"],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            duration_in_minutes=dict(
                                                type="int", required=True
                                            ),
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "LT"],
                                            ),
                                            value=dict(type="int", required=True),
                                        ),
                                    ),
                                ),
                            ),
                            min_node_count=dict(type="int"),
                            step_size=dict(type="int"),
                        ),
                    ),
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "METRIC_BASED_HORIZONTAL_SCALING_POLICY",
                            "SCHEDULE_BASED_VERTICAL_SCALING_POLICY",
                            "SCHEDULE_BASED_HORIZONTAL_SCALING_POLICY",
                            "METRIC_BASED_VERTICAL_SCALING_POLICY",
                        ],
                    ),
                    timezone=dict(type="str"),
                    schedule_details=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            time_and_horizontal_scaling_config=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    time_recurrence=dict(type="str"),
                                    target_node_count=dict(type="int"),
                                ),
                            ),
                            schedule_type=dict(
                                type="str", required=True, choices=["DAY_BASED"]
                            ),
                            time_and_vertical_scaling_config=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    time_recurrence=dict(type="str"),
                                    target_shape=dict(type="str"),
                                    target_ocpus_per_node=dict(type="int"),
                                    target_memory_per_node=dict(type="int"),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            bds_instance_id=dict(type="str", required=True),
            auto_scaling_configuration_id=dict(aliases=["id"], type="str"),
            cluster_admin_password=dict(type="str", no_log=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_auto_scale_config",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
