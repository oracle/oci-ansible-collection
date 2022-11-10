#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_autoscaling_auto_scaling_configuration_actions
short_description: Perform actions on an AutoScalingConfiguration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AutoScalingConfiguration resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an autoscaling configuration into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      When you move an autoscaling configuration to a different compartment, associated resources such as instance
      pools are not moved.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    auto_scaling_configuration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the autoscaling configuration.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the autoscaling configuration
              to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the AutoScalingConfiguration.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on auto_scaling_configuration
  oci_autoscaling_auto_scaling_configuration_actions:
    # required
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
        time_created:
            description:
                - The date and time the autoscaling configuration was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "max_resource_count": 56,
        "min_resource_count": 56
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
    from oci.autoscaling import AutoScalingClient
    from oci.autoscaling.models import ChangeAutoScalingCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoScalingConfigurationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAutoScalingCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_auto_scaling_configuration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                change_compartment_details=action_details,
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


AutoScalingConfigurationActionsHelperCustom = get_custom_class(
    "AutoScalingConfigurationActionsHelperCustom"
)


class ResourceHelper(
    AutoScalingConfigurationActionsHelperCustom,
    AutoScalingConfigurationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            auto_scaling_configuration_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="auto_scaling_configuration",
        service_client_class=AutoScalingClient,
        namespace="autoscaling",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
