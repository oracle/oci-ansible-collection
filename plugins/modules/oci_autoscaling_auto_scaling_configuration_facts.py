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
module: oci_autoscaling_auto_scaling_configuration_facts
short_description: Fetches details about one or multiple AutoScalingConfiguration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AutoScalingConfiguration resources in Oracle Cloud Infrastructure
    - Lists autoscaling configurations in the specifed compartment.
    - If I(auto_scaling_configuration_id) is specified, the details of a single AutoScalingConfiguration will be returned.
version_added: "2.5"
options:
    auto_scaling_configuration_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the autoscaling configuration.
            - Required to get a specific auto_scaling_configuration.
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the
              resources monitored by the metric that you are searching for. Use tenancyId to search in
              the root compartment.
            - Required to list multiple auto_scaling_configurations.
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        aliases: ["name"]
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        choices:
            - "ASC"
            - "DESC"
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: List auto_scaling_configurations
  oci_autoscaling_auto_scaling_configuration_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific auto_scaling_configuration
  oci_autoscaling_auto_scaling_configuration_facts:
    auto_scaling_configuration_id: ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
auto_scaling_configurations:
    description:
        - List of AutoScalingConfiguration resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the autoscaling
                  configuration.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
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
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        cool_down_in_seconds:
            description:
                - The minimum period of time to wait between scaling actions. The cooldown period gives the system time to stabilize
                  before rescaling. The minimum value is 300 seconds, which is also the default.
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
                    type: string
                    sample: instancePool
                id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource that is managed by the autoscaling
                          configuration.
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        policies:
            description:
                - Autoscaling policy definitions for the autoscaling configuration. An autoscaling policy defines the criteria that
                  trigger autoscaling actions and the actions to take.
                - Each autoscaling configuration can have one autoscaling policy.
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
        time_created:
            description:
                - The date and time the AutoScalingConfiguration was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: [{
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
        }],
        "time_created": "2016-08-25T21:10:29.600Z"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.autoscaling import AutoScalingClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoScalingConfigurationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return ["auto_scaling_configuration_id"]

    def get_required_params_for_list(self):
        return ["compartment_id"]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            auto_scaling_configuration_id=self.module.params.get(
                "auto_scaling_configuration_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = ["display_name", "sort_by", "sort_order"]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_auto_scaling_configurations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AutoScalingConfigurationFactsHelperCustom = get_custom_class(
    "AutoScalingConfigurationFactsHelperCustom"
)


class ResourceFactsHelper(
    AutoScalingConfigurationFactsHelperCustom, AutoScalingConfigurationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            auto_scaling_configuration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
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
        resource_type="auto_scaling_configuration",
        service_client_class=AutoScalingClient,
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(auto_scaling_configurations=result)


if __name__ == "__main__":
    main()
