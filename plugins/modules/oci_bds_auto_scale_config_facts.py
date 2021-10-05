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
module: oci_bds_auto_scale_config_facts
short_description: Fetches details about one or multiple BdsAutoScaleConfig resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BdsAutoScaleConfig resources in Oracle Cloud Infrastructure
    - Returns information about the autoscaling configurations for a cluster.
    - If I(auto_scaling_configuration_id) is specified, the details of a single BdsAutoScaleConfig will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
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
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List bds_auto_scale_configs
  oci_bds_auto_scale_config_facts:
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific bds_auto_scale_config
  oci_bds_auto_scale_config_facts:
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

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
        node_type:
            description:
                - A node type that is managed by an autoscale configuration. The only supported type is WORKER.
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
            sample: "2020-03-29T09:36:42.000+0000"
        time_updated:
            description:
                - The time the autoscale configuration was updated, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2020-04-29T09:36:42.000+0000"
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
                                                - This value is the minimum period of time the metric value meets or exceeds the threshold value before the
                                                  action is triggered. The value is in minutes.
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "node_type": "node_type_example",
        "lifecycle_state": "CREATING",
        "time_created": "2020-03-29T09:36:42.000+0000",
        "time_updated": "2020-04-29T09:36:42.000+0000",
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
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
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
            bds_instance_id=dict(type="str", required=True),
            auto_scaling_configuration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

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
