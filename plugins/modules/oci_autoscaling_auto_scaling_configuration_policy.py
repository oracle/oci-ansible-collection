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
module: oci_autoscaling_auto_scaling_configuration_policy
short_description: Manage an AutoScalingConfigurationPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an AutoScalingConfigurationPolicy resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    auto_scaling_configuration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the autoscaling configuration.
        type: str
        required: true
    auto_scaling_policy_id:
        description:
            - The ID of the autoscaling policy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    rules:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when policy_type is 'threshold'
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
                            - This parameter is updatable.
                            - Required when policy_type is 'threshold'
                        type: str
                        choices:
                            - "CHANGE_COUNT_BY"
                        required: true
                    value:
                        description:
                            - To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of
                              instances), provide a negative value.
                            - This parameter is updatable.
                            - Required when policy_type is 'threshold'
                        type: int
                        required: true
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                    - This parameter is updatable.
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
                            - This parameter is updatable.
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
                                    - This parameter is updatable.
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
                                    - This parameter is updatable.
                                    - Required when policy_type is 'threshold'
                                type: int
                                required: true
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    capacity:
        description:
            - The capacity requirements of the autoscaling policy.
            - This parameter is updatable.
        type: dict
        suboptions:
            max:
                description:
                    - For a threshold-based autoscaling policy, this value is the maximum number of instances the instance pool is allowed
                      to increase to (scale out).
                    - For a schedule-based autoscaling policy, this value is not used.
                    - This parameter is updatable.
                    - Applicable when policy_type is 'threshold'
                type: int
            min:
                description:
                    - For a threshold-based autoscaling policy, this value is the minimum number of instances the instance pool is allowed
                      to decrease to (scale in).
                    - For a schedule-based autoscaling policy, this value is not used.
                    - This parameter is updatable.
                    - Applicable when policy_type is 'threshold'
                type: int
            initial:
                description:
                    - For a threshold-based autoscaling policy, this value is the initial number of instances to launch in the instance pool
                      immediately after autoscaling is enabled. After autoscaling retrieves performance metrics, the number of
                      instances is automatically adjusted from this initial number to a number that is based on the limits that
                      you set.
                    - For a schedule-based autoscaling policy, this value is the target pool size to scale to when executing the schedule
                      that's defined in the autoscaling policy.
                    - This parameter is updatable.
                    - Applicable when policy_type is 'threshold'
                type: int
    policy_type:
        description:
            - Indicates the type of autoscaling policy.
        type: str
        choices:
            - "threshold"
            - "scheduled"
        required: true
    is_enabled:
        description:
            - Whether the autoscaling policy is enabled.
            - This parameter is updatable.
        type: bool
    execution_schedule:
        description:
            - The schedule for executing the autoscaling policy.
            - This parameter is updatable.
            - Applicable when policy_type is 'scheduled'
        type: dict
        suboptions:
            type:
                description:
                    - The type of execution schedule.
                    - This parameter is updatable.
                type: str
                choices:
                    - "cron"
                required: true
            timezone:
                description:
                    - The time zone for the execution schedule.
                    - This parameter is updatable.
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
                    - This parameter is updatable.
                type: str
                required: true
    resource_action:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when policy_type is 'scheduled'
        type: dict
        suboptions:
            action_type:
                description:
                    - The type of resource action.
                    - This parameter is updatable.
                type: str
                choices:
                    - "power"
                required: true
            action:
                description:
                    - ""
                    - This parameter is updatable.
                type: str
                choices:
                    - "STOP"
                    - "START"
                    - "SOFTRESET"
                    - "RESET"
                required: true
    state:
        description:
            - The state of the AutoScalingConfigurationPolicy.
            - Use I(state=present) to update an existing an AutoScalingConfigurationPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update auto_scaling_configuration_policy with policy_type = threshold
  oci_autoscaling_auto_scaling_configuration_policy:
    # required
    policy_type: threshold

    # optional
    rules:
    - # required
      action:
        # required
        type: CHANGE_COUNT_BY
        value: 56
      metric:
        # required
        metric_type: CPU_UTILIZATION
        threshold:
          # required
          operator: GT
          value: 56

      # optional
      display_name: display_name_example
    display_name: display_name_example
    capacity:
      # optional
      max: 56
      min: 56
      initial: 56
    is_enabled: true

- name: Update auto_scaling_configuration_policy with policy_type = scheduled
  oci_autoscaling_auto_scaling_configuration_policy:
    # required
    policy_type: scheduled

    # optional
    display_name: display_name_example
    capacity:
      # optional
      max: 56
      min: 56
      initial: 56
    is_enabled: true
    execution_schedule:
      # required
      type: cron
      timezone: UTC
      expression: expression_example
    resource_action:
      # required
      action_type: power
      action: STOP

- name: Update auto_scaling_configuration_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with policy_type = threshold
  oci_autoscaling_auto_scaling_configuration_policy:
    # required
    policy_type: threshold

    # optional
    rules:
    - # required
      action:
        # required
        type: CHANGE_COUNT_BY
        value: 56
      metric:
        # required
        metric_type: CPU_UTILIZATION
        threshold:
          # required
          operator: GT
          value: 56

      # optional
      display_name: display_name_example
    display_name: display_name_example
    capacity:
      # optional
      max: 56
      min: 56
      initial: 56
    is_enabled: true

- name: Update auto_scaling_configuration_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with policy_type = scheduled
  oci_autoscaling_auto_scaling_configuration_policy:
    # required
    policy_type: scheduled

    # optional
    display_name: display_name_example
    capacity:
      # optional
      max: 56
      min: 56
      initial: 56
    is_enabled: true
    execution_schedule:
      # required
      type: cron
      timezone: UTC
      expression: expression_example
    resource_action:
      # required
      action_type: power
      action: STOP

"""

RETURN = """
auto_scaling_configuration_policy:
    description:
        - Details of the AutoScalingConfigurationPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
                    sample: expression_example
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
            sample: "2013-10-20T19:20:30+01:00"
        is_enabled:
            description:
                - Whether the autoscaling policy is enabled.
            returned: on success
            type: bool
            sample: true
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
    sample: {
        "execution_schedule": {
            "type": "cron",
            "timezone": "UTC",
            "expression": "expression_example"
        },
        "resource_action": {
            "action_type": "power",
            "action": "STOP"
        },
        "capacity": {
            "max": 56,
            "min": 56,
            "initial": 56
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "policy_type": "scheduled",
        "time_created": "2013-10-20T19:20:30+01:00",
        "is_enabled": true,
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
    from oci.autoscaling import AutoScalingClient
    from oci.autoscaling.models import UpdateAutoScalingPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoScalingConfigurationPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(
            AutoScalingConfigurationPolicyHelperGen, self
        ).get_possible_entity_types() + [
            "autoscalingconfigurationpolicy",
            "autoscalingconfigurationpolicies",
            "autoscalingautoscalingconfigurationpolicy",
            "autoscalingautoscalingconfigurationpolicies",
            "autoscalingconfigurationpolicyresource",
            "autoscalingconfigurationpoliciesresource",
            "policy",
            "policies",
            "autoscalingpolicy",
            "autoscalingpolicies",
            "policyresource",
            "policiesresource",
            "autoscaling",
        ]

    def get_module_resource_id_param(self):
        return "auto_scaling_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("auto_scaling_policy_id")

    def get_get_fn(self):
        return self.client.get_auto_scaling_policy

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_policy,
            auto_scaling_policy_id=summary_model.id,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_policy,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
            auto_scaling_policy_id=self.module.params.get("auto_scaling_policy_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "auto_scaling_configuration_id",
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
            self.client.list_auto_scaling_policies, **kwargs
        )

    def get_update_model_class(self):
        return UpdateAutoScalingPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_auto_scaling_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                auto_scaling_policy_id=self.module.params.get("auto_scaling_policy_id"),
                update_auto_scaling_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


AutoScalingConfigurationPolicyHelperCustom = get_custom_class(
    "AutoScalingConfigurationPolicyHelperCustom"
)


class ResourceHelper(
    AutoScalingConfigurationPolicyHelperCustom, AutoScalingConfigurationPolicyHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            auto_scaling_configuration_id=dict(type="str", required=True),
            auto_scaling_policy_id=dict(aliases=["id"], type="str"),
            rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    action=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            type=dict(
                                type="str", required=True, choices=["CHANGE_COUNT_BY"]
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
                                choices=["CPU_UTILIZATION", "MEMORY_UTILIZATION"],
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
            display_name=dict(aliases=["name"], type="str"),
            capacity=dict(
                type="dict",
                options=dict(
                    max=dict(type="int"), min=dict(type="int"), initial=dict(type="int")
                ),
            ),
            policy_type=dict(
                type="str", required=True, choices=["threshold", "scheduled"]
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
                    action_type=dict(type="str", required=True, choices=["power"]),
                    action=dict(
                        type="str",
                        required=True,
                        choices=["STOP", "START", "SOFTRESET", "RESET"],
                    ),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="auto_scaling_configuration_policy",
        service_client_class=AutoScalingClient,
        namespace="autoscaling",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
