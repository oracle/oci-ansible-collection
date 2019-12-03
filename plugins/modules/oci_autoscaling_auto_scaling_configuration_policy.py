#!/usr/bin/python
# Copyright (c) 2017, 2019 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


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
version_added: "2.5"
options:
    auto_scaling_configuration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the autoscaling configuration.
        required: true
    auto_scaling_policy_id:
        description:
            - The ID of the autoscaling policy.
        aliases: ["id"]
        required: true
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
        aliases: ["name"]
    capacity:
        description:
            - The capacity requirements of the autoscaling policy.
        type: dict
        suboptions:
            max:
                description:
                    - The maximum number of instances the instance pool is allowed to increase to (scale out).
                type: int
                required: true
            min:
                description:
                    - The minimum number of instances the instance pool is allowed to decrease to (scale in).
                type: int
                required: true
            initial:
                description:
                    - The initial number of instances to launch in the instance pool immediately after autoscaling is
                      enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this
                      initial number to a number that is based on the limits that you set.
                type: int
                required: true
    policy_type:
        description:
            - Indicates the type of autoscaling policy.
        choices:
            - "threshold"
        required: true
    rules:
        description:
            - ""
        type: list
        suboptions:
            action:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    type:
                        description:
                            - The type of action to take.
                        choices:
                            - "CHANGE_COUNT_BY"
                        required: true
                    value:
                        description:
                            - To scale out (increase the number of instances), provide a positive value. To scale in (decrease the number of
                              instances), provide a negative value.
                        type: int
                        required: true
            display_name:
                description:
                    - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
                aliases: ["name"]
            metric:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    metric_type:
                        description:
                            - ""
                        choices:
                            - "CPU_UTILIZATION"
                            - "MEMORY_UTILIZATION"
                        required: true
                    threshold:
                        description:
                            - ""
                        type: dict
                        required: true
                        suboptions:
                            operator:
                                description:
                                    - The comparison operator to use. Options are greater than (`GT`), greater than or equal to
                                      (`GTE`), less than (`LT`), and less than or equal to (`LTE`).
                                choices:
                                    - "GT"
                                    - "GTE"
                                    - "LT"
                                    - "LTE"
                                required: true
                            value:
                                description:
                                    - ""
                                type: int
                                required: true
    state:
        description:
            - The state of the AutoScalingConfigurationPolicy.
            - Use I(state=present) to update an existing an AutoScalingConfigurationPolicy.
        required: false
        default: 'present'
        choices: ["present"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Update auto_scaling_configuration_policy
  oci_autoscaling_auto_scaling_configuration_policy:
    display_name: example_autoscaling_policy
    capacity:
      max: 50
      min: 10
      initial: 15
    policy_type: threshold
    rules:
    - action:
        type: CHANGE_COUNT_BY
        value: 5
      display_name: example_scale_out_condition
      metric:
        metric_type: CPU_UTILIZATION
        threshold:
          operator: GTE
          value: 90
    - action:
        type: CHANGE_COUNT_BY
        value: -5
      display_name: example_scale_in_condition
      metric:
        metric_type: CPU_UTILIZATION
        threshold:
          operator: LTE
          value: 25
    auto_scaling_configuration_id: ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx
    auto_scaling_policy_id: ocid1.autoscalingpolicy.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
auto_scaling_configuration_policy:
    description:
        - Details of the AutoScalingConfigurationPolicy resource acted upon by the current operation
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
                        - The maximum number of instances the instance pool is allowed to increase to (scale out).
                    returned: on success
                    type: int
                    sample: 56
                min:
                    description:
                        - The minimum number of instances the instance pool is allowed to decrease to (scale in).
                    returned: on success
                    type: int
                    sample: 56
                initial:
                    description:
                        - The initial number of instances to launch in the instance pool immediately after autoscaling is
                          enabled. After autoscaling retrieves performance metrics, the number of instances is automatically adjusted from this
                          initial number to a number that is based on the limits that you set.
                    returned: on success
                    type: int
                    sample: 56
        id:
            description:
                - The ID of the autoscaling policy that is assigned after creation.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
    sample: {
        "capacity": {
            "max": 56,
            "min": 56,
            "initial": 56
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "policy_type": "policy_type_example",
        "time_created": "2016-08-25T21:10:29.600Z",
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

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.autoscaling import AutoScalingClient
    from oci.autoscaling.models import UpdateAutoScalingPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoScalingConfigurationPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    @staticmethod
    def get_module_resource_id_param():
        return "auto_scaling_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("auto_scaling_policy_id")

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_policy,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
            auto_scaling_policy_id=self.module.params.get("auto_scaling_policy_id"),
        )

    def list_resources(self):
        required_list_method_params = ["auto_scaling_configuration_id"]

        optional_list_method_params = ["display_name"]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_auto_scaling_policies, **kwargs
        )

    def get_update_model_class(self):
        return UpdateAutoScalingPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_common_utils.call_with_backoff(
            self.client.update_auto_scaling_policy,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
            auto_scaling_policy_id=self.module.params.get("auto_scaling_policy_id"),
            update_auto_scaling_policy_details=update_details,
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
            auto_scaling_policy_id=dict(aliases=["id"], type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            capacity=dict(
                type="dict",
                options=dict(
                    max=dict(type="int", required=True),
                    min=dict(type="int", required=True),
                    initial=dict(type="int", required=True),
                ),
            ),
            policy_type=dict(type="str", required=True, choices=["threshold"]),
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
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="auto_scaling_configuration_policy",
        service_client_class=AutoScalingClient,
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
