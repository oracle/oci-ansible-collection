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
module: oci_autoscaling_auto_scaling_configuration_policy_facts
short_description: Fetches details about one or multiple AutoScalingConfigurationPolicy resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutoScalingConfigurationPolicy resources in Oracle Cloud Infrastructure
    - Lists the autoscaling policies in the specified autoscaling configuration.
    - If I(auto_scaling_policy_id) is specified, the details of a single AutoScalingConfigurationPolicy will be returned.
version_added: "2.9"
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
            - Required to get a specific auto_scaling_configuration_policy.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List auto_scaling_configuration_policies
  oci_autoscaling_auto_scaling_configuration_policy_facts:
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific auto_scaling_configuration_policy
  oci_autoscaling_auto_scaling_configuration_policy_facts:
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    auto_scaling_policy_id: "ocid1.autoscalingpolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
auto_scaling_configuration_policies:
    description:
        - List of AutoScalingConfigurationPolicy resources
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
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        policy_type:
            description:
                - The type of autoscaling policy.
            returned: on success
            type: string
            sample: policy_type_example
        time_created:
            description:
                - The date and time the autoscaling configuration was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
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
                    type: string
                    sample: cron
                timezone:
                    description:
                        - The time zone for the execution schedule.
                    returned: on success
                    type: string
                    sample: UTC
                expression:
                    description:
                        - A cron expression that represents the time at which to execute the autoscaling policy.
                        - "Cron expressions have this format: `<second> <minute> <hour> <day of month> <month> <day of week> <year>`"
                        - You can use special characters that are supported with the Quartz cron implementation.
                        - You must specify `0` as the value for seconds.
                        - "Example: `0 15 10 ? * *`"
                    returned: on success
                    type: string
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
                    type: string
                    sample: action_type_example
                action:
                    description:
                        - ""
                    returned: on success
                    type: string
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
                            type: string
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
                    type: string
                    sample: display_name_example
                id:
                    description:
                        - ID of the condition that is assigned after creation.
                    returned: on success
                    type: string
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
                            type: string
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
                                    type: string
                                    sample: GT
                                value:
                                    description:
                                        - ""
                                    returned: on success
                                    type: int
                                    sample: 56
    sample: [{
        "capacity": {
            "max": 56,
            "min": 56,
            "initial": 56
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "policy_type": "policy_type_example",
        "time_created": "2016-08-25T21:10:29.600Z",
        "is_enabled": true,
        "execution_schedule": {
            "type": "cron",
            "timezone": "UTC",
            "expression": "0 15 10 ? * *"
        },
        "resource_action": {
            "action_type": "action_type_example",
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.autoscaling import AutoScalingClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoScalingConfigurationPolicyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "auto_scaling_configuration_id",
            "auto_scaling_policy_id",
        ]

    def get_required_params_for_list(self):
        return [
            "auto_scaling_configuration_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_policy,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
            auto_scaling_policy_id=self.module.params.get("auto_scaling_policy_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_auto_scaling_policies,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
            **optional_kwargs
        )


AutoScalingConfigurationPolicyFactsHelperCustom = get_custom_class(
    "AutoScalingConfigurationPolicyFactsHelperCustom"
)


class ResourceFactsHelper(
    AutoScalingConfigurationPolicyFactsHelperCustom,
    AutoScalingConfigurationPolicyFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            auto_scaling_configuration_id=dict(type="str", required=True),
            auto_scaling_policy_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="auto_scaling_configuration_policy",
        service_client_class=AutoScalingClient,
        namespace="autoscaling",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(auto_scaling_configuration_policies=result)


if __name__ == "__main__":
    main()
