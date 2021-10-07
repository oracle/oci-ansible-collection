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
module: oci_autoscaling_auto_scaling_configuration
short_description: Manage an AutoScalingConfiguration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AutoScalingConfiguration resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an autoscaling configuration.
    - "This resource has the following action operations in the M(oci_auto_scaling_configuration_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the autoscaling configuration.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    cool_down_in_seconds:
        description:
            - For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions.
              The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which
              is also the default. The cooldown period starts when the instance pool reaches the running state.
            - For schedule-based autoscaling policies, this value is not used.
            - This parameter is updatable.
        type: int
    is_enabled:
        description:
            - Whether the autoscaling configuration is enabled.
            - This parameter is updatable.
        type: bool
    policies:
        description:
            - ""
            - Required for create using I(state=present).
        type: list
        elements: dict
        suboptions:
            capacity:
                description:
                    - The capacity requirements of the autoscaling policy.
                type: dict
                suboptions:
                    max:
                        description:
                            - For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed
                              to increase to (scale out).
                            - For a schedule-based autoscaling policy, this value is not used.
                            - Applicable when policy_type is 'scheduled'
                        type: int
                    min:
                        description:
                            - For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed
                              to decrease to (scale in).
                            - For a schedule-based autoscaling policy, this value is not used.
                            - Applicable when policy_type is 'scheduled'
                        type: int
                    initial:
                        description:
                            - For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool
                              immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of
                              instances is automatically adjusted from this initial number to a number that is based on the limits that
                              you set.
                            - For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule
                              that's defined in the autoscaling policy.
                            - Applicable when policy_type is 'scheduled'
                        type: int
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                type: str
                aliases: ["name"]
            policy_type:
                description:
                    - The type of autoscaling policy.
                type: str
                choices:
                    - "scheduled"
                    - "threshold"
                required: true
            is_enabled:
                description:
                    - Whether the autoscaling policy is enabled.
                type: bool
            execution_schedule:
                description:
                    - ""
                    - Required when policy_type is 'scheduled'
                type: dict
                suboptions:
                    type:
                        description:
                            - The type of execution schedule.
                        type: str
                        choices:
                            - "cron"
                        required: true
                    timezone:
                        description:
                            - The time zone for the execution schedule.
                        type: str
                        choices:
                            - "UTC"
                        required: true
                    expression:
                        description:
                            - A cron expression that represents the time at which to execute the autoscaling policy.
                            - "Cron expressions have this format: `<second> <minute> <hour> <day of month> <month> <day of week> <year>`"
                            - You can use special characters that are supported with the Quartz cron implementation.
                            - You must specify `0` as the value for seconds.
                            - "Example: `0 15 10 ? * *`"
                        type: str
                        required: true
            resource_action:
                description:
                    - ""
                    - Applicable when policy_type is 'scheduled'
                type: dict
                suboptions:
                    action_type:
                        description:
                            - The type of resource action.
                        type: str
                        choices:
                            - "power"
                        required: true
                    action:
                        description:
                            - ""
                        type: str
                        choices:
                            - "STOP"
                            - "START"
                            - "SOFTRESET"
                            - "RESET"
                        required: true
            rules:
                description:
                    - ""
                    - Required when policy_type is 'threshold'
                type: list
                elements: dict
                suboptions:
                    action:
                        description:
                            - ""
                            - Required when policy_type is 'threshold'
                        type: dict
                        required: true
                        suboptions:
                            type:
                                description:
                                    - The type of action to take.
                                    - Required when policy_type is 'threshold'
                                type: str
                                choices:
                                    - "CHANGE_COUNT_BY"
                                required: true
                            value:
                                description:
                                    - To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of
                                      instances), provide a negative value.
                                    - Required when policy_type is 'threshold'
                                type: int
                                required: true
                    display_name:
                        description:
                            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                            - Applicable when policy_type is 'threshold'
                        type: str
                        aliases: ["name"]
                    metric:
                        description:
                            - ""
                            - Required when policy_type is 'threshold'
                        type: dict
                        required: true
                        suboptions:
                            metric_type:
                                description:
                                    - ""
                                    - Required when policy_type is 'threshold'
                                type: str
                                choices:
                                    - "CPU_UTILIZATION"
                                    - "MEMORY_UTILIZATION"
                                required: true
                            threshold:
                                description:
                                    - ""
                                    - Required when policy_type is 'threshold'
                                type: dict
                                required: true
                                suboptions:
                                    operator:
                                        description:
                                            - The comparison operator to use. Options are greater than (`GT`), greater than or equal to
                                              (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
                                            - Required when policy_type is 'threshold'
                                        type: str
                                        choices:
                                            - "GT"
                                            - "GTE"
                                            - "LT"
                                            - "LTE"
                                        required: true
                                    value:
                                        description:
                                            - ""
                                            - Required when policy_type is 'threshold'
                                        type: int
                                        required: true
    resource:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            type:
                description:
                    - The type of resource.
                type: str
                choices:
                    - "instancePool"
                required: true
            id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling
                      configuration.
                type: str
                required: true
    auto_scaling_configuration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the autoscaling configuration.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AutoScalingConfiguration.
            - Use I(state=present) to create or update an AutoScalingConfiguration.
            - Use I(state=absent) to delete an AutoScalingConfiguration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create auto_scaling_configuration
  oci_autoscaling_auto_scaling_configuration:
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    display_name: "example_autoscaling_configuration"
    cool_down_in_seconds: 300
    is_enabled: true
    policies:
    - capacity:
        max: 50
        min: 10
        initial: 15
      display_name: "example_autoscaling_policy"
      policy_type: "threshold"
      rules:
      - action:
          type: "CHANGE_COUNT_BY"
          value: 5
        display_name: "example_scale_out_condition"
        metric:
          metric_type: "CPU_UTILIZATION"
          threshold:
            operator: "GTE"
            value: 90
      - action:
          type: "CHANGE_COUNT_BY"
          value: -5
        display_name: "example_scale_in_condition"
        metric:
          metric_type: "CPU_UTILIZATION"
          threshold:
            operator: "LTE"
            value: 25
    resource:
      type: "instancePool"
      id: "ocid1.instancepool.oc1..unique_ID"

- name: Update auto_scaling_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_autoscaling_auto_scaling_configuration:
    display_name: "example_autoscaling_configuration"
    is_enabled: false
    cool_down_in_seconds: 600

- name: Update auto_scaling_configuration
  oci_autoscaling_auto_scaling_configuration:
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete auto_scaling_configuration
  oci_autoscaling_auto_scaling_configuration:
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete auto_scaling_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_autoscaling_auto_scaling_configuration:
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    display_name: example_autoscaling_configuration
    state: absent

"""

RETURN = """
auto_scaling_configuration:
    description:
        - Details of the AutoScalingConfiguration resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the autoscaling
                  configuration.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the autoscaling configuration.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        cool_down_in_seconds:
            description:
                - For threshold-based autoscaling policies, this value is the minimum period of time to wait between scaling actions.
                  The cooldown period gives the system time to stabilize before rescaling. The minimum value is 300 seconds, which
                  is also the default. The cooldown period starts when the instance pool reaches the running state.
                - For schedule-based autoscaling policies, this value is not used.
            returned: on success
            type: int
            sample: 56
        is_enabled:
            description:
                - Whether the autoscaling configuration is enabled.
            returned: on success
            type: bool
            sample: true
        resource:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of resource.
                    returned: on success
                    type: str
                    sample: instancePool
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling
                          configuration.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        policies:
            description:
                - Autoscaling policy definitions for the autoscaling configuration. An autoscaling policy defines the criteria that
                  trigger autoscaling actions and the actions to take.
            returned: on success
            type: complex
            contains:
                capacity:
                    description:
                        - The capacity requirements of the autoscaling policy.
                    returned: on success
                    type: complex
                    contains:
                        max:
                            description:
                                - For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed
                                  to increase to (scale out).
                                - For a schedule-based autoscaling policy, this value is not used.
                            returned: on success
                            type: int
                            sample: 56
                        min:
                            description:
                                - For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed
                                  to decrease to (scale in).
                                - For a schedule-based autoscaling policy, this value is not used.
                            returned: on success
                            type: int
                            sample: 56
                        initial:
                            description:
                                - For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool
                                  immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of
                                  instances is automatically adjusted from this initial number to a number that is based on the limits that
                                  you set.
                                - For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule
                                  that's defined in the autoscaling policy.
                            returned: on success
                            type: int
                            sample: 56
                id:
                    description:
                        - The ID of the autoscaling policy that is assigned after creation.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                policy_type:
                    description:
                        - The type of autoscaling policy.
                    returned: on success
                    type: str
                    sample: scheduled
                time_created:
                    description:
                        - The date and time the autoscaling configuration was created, in the format defined by RFC3339.
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2016-08-25T21:10:29.600Z"
                is_enabled:
                    description:
                        - Whether the autoscaling policy is enabled.
                    returned: on success
                    type: bool
                    sample: true
                execution_schedule:
                    description:
                        - The schedule for executing the autoscaling policy.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of execution schedule.
                            returned: on success
                            type: str
                            sample: cron
                        timezone:
                            description:
                                - The time zone for the execution schedule.
                            returned: on success
                            type: str
                            sample: UTC
                        expression:
                            description:
                                - A cron expression that represents the time at which to execute the autoscaling policy.
                                - "Cron expressions have this format: `<second> <minute> <hour> <day of month> <month> <day of week> <year>`"
                                - You can use special characters that are supported with the Quartz cron implementation.
                                - You must specify `0` as the value for seconds.
                                - "Example: `0 15 10 ? * *`"
                            returned: on success
                            type: str
                            sample: "0 15 10 ? * *"
                resource_action:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        action_type:
                            description:
                                - The type of resource action.
                            returned: on success
                            type: str
                            sample: power
                        action:
                            description:
                                - ""
                            returned: on success
                            type: str
                            sample: STOP
                rules:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        action:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - The type of action to take.
                                    returned: on success
                                    type: str
                                    sample: CHANGE_COUNT_BY
                                value:
                                    description:
                                        - To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of
                                          instances), provide a negative value.
                                    returned: on success
                                    type: int
                                    sample: 56
                        display_name:
                            description:
                                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
                        id:
                            description:
                                - ID of the condition that is assigned after creation.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        metric:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                metric_type:
                                    description:
                                        - ""
                                    returned: on success
                                    type: str
                                    sample: CPU_UTILIZATION
                                threshold:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        operator:
                                            description:
                                                - The comparison operator to use. Options are greater than (`GT`), greater than or equal to
                                                  (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
                                            returned: on success
                                            type: str
                                            sample: GT
                                        value:
                                            description:
                                                - ""
                                            returned: on success
                                            type: int
                                            sample: 56
        time_created:
            description:
                - The date and time the autoscaling configuration was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        max_resource_count:
            description:
                - The maximum number of resources to scale out to.
            returned: on success
            type: int
            sample: 56
        min_resource_count:
            description:
                - The minimum number of resources to scale in to.
            returned: on success
            type: int
            sample: 56
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "cool_down_in_seconds": 56,
        "is_enabled": true,
        "resource": {
            "type": "instancePool",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "policies": [{
            "capacity": {
                "max": 56,
                "min": 56,
                "initial": 56
            },
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "policy_type": "scheduled",
            "time_created": "2016-08-25T21:10:29.600Z",
            "is_enabled": true,
            "execution_schedule": {
                "type": "cron",
                "timezone": "UTC",
                "expression": "0 15 10 ? * *"
            },
            "resource_action": {
                "action_type": "power",
                "action": "STOP"
            },
            "rules": [{
                "action": {
                    "type": "CHANGE_COUNT_BY",
                    "value": 56
                },
                "display_name": "display_name_example",
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "metric": {
                    "metric_type": "CPU_UTILIZATION",
                    "threshold": {
                        "operator": "GT",
                        "value": 56
                    }
                }
            }]
        }],
        "time_created": "2016-08-25T21:10:29.600Z",
        "max_resource_count": 56,
        "min_resource_count": 56
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
    from oci.autoscaling import AutoScalingClient
    from oci.autoscaling.models import CreateAutoScalingConfigurationDetails
    from oci.autoscaling.models import UpdateAutoScalingConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoScalingConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "auto_scaling_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("auto_scaling_configuration_id")

    def get_get_fn(self):
        return self.client.get_auto_scaling_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
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
        return CreateAutoScalingConfigurationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_auto_scaling_configuration_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAutoScalingConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                update_auto_scaling_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AutoScalingConfigurationHelperCustom = get_custom_class(
    "AutoScalingConfigurationHelperCustom"
)


class ResourceHelper(
    AutoScalingConfigurationHelperCustom, AutoScalingConfigurationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            cool_down_in_seconds=dict(type="int"),
            is_enabled=dict(type="bool"),
            policies=dict(
                type="list",
                elements="dict",
                options=dict(
                    capacity=dict(
                        type="dict",
                        options=dict(
                            max=dict(type="int"),
                            min=dict(type="int"),
                            initial=dict(type="int"),
                        ),
                    ),
                    display_name=dict(aliases=["name"], type="str"),
                    policy_type=dict(
                        type="str", required=True, choices=["scheduled", "threshold"]
                    ),
                    is_enabled=dict(type="bool"),
                    execution_schedule=dict(
                        type="dict",
                        options=dict(
                            type=dict(type="str", required=True, choices=["cron"]),
                            timezone=dict(type="str", required=True, choices=["UTC"]),
                            expression=dict(type="str", required=True),
                        ),
                    ),
                    resource_action=dict(
                        type="dict",
                        options=dict(
                            action_type=dict(
                                type="str", required=True, choices=["power"]
                            ),
                            action=dict(
                                type="str",
                                required=True,
                                choices=["STOP", "START", "SOFTRESET", "RESET"],
                            ),
                        ),
                    ),
                    rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            action=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=["CHANGE_COUNT_BY"],
                                    ),
                                    value=dict(type="int", required=True),
                                ),
                            ),
                            display_name=dict(aliases=["name"], type="str"),
                            metric=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    metric_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "CPU_UTILIZATION",
                                            "MEMORY_UTILIZATION",
                                        ],
                                    ),
                                    threshold=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            operator=dict(
                                                type="str",
                                                required=True,
                                                choices=["GT", "GTE", "LT", "LTE"],
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
            resource=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["instancePool"]),
                    id=dict(type="str", required=True),
                ),
            ),
            auto_scaling_configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="auto_scaling_configuration",
        service_client_class=AutoScalingClient,
        namespace="autoscaling",
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
