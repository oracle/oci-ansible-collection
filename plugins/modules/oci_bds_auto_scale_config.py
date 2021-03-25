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
module: oci_bds_auto_scale_config
short_description: Manage a BdsAutoScaleConfig resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BdsAutoScaleConfig resource in Oracle Cloud Infrastructure
    - For I(state=present), add autoscaling configuration.
version_added: "2.9"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the BDS instance
        type: str
        required: true
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    node_type:
        description:
            - A node type that is managed by an autoscaling configuration. The only supported type is WORKER.
            - Required for create using I(state=present).
        type: str
    is_enabled:
        description:
            - Whether the autoscaling configuration is enabled.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    cluster_admin_password:
        description:
            - Base-64 encoded password for Cloudera Manager admin user
            - Required for create using I(state=present).
            - Required for delete using I(state=absent).
            - This parameter is updatable.
        type: str
    policy:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            policy_type:
                description:
                    - Types of autoscaling policies. SCHEDULE-BASED or  THRESHOLD-BASED, current only supported THRESHOLD-BASED.
                type: str
                choices:
                    - "THRESHOLD_BASED"
                    - "SCHEDULE_BASED"
                required: true
            rules:
                description:
                    - The list of rules for autoscaling. If an action have multiple rules, last rule in the array will be applied.
                type: list
                required: true
                suboptions:
                    action:
                        description:
                            - "The valid value are - CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN"
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
                                    - Allowed value is CPU_UTILIZATION currently
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
                                            - This value is the minimum period of time metric value meets or exceeds threshold value before action is trigger.
                                              The value is in minutes.
                                        type: int
                                        required: true
                                    operator:
                                        description:
                                            - The comparison operator to use. Options are greater than (GT), less than (LT).
                                        type: str
                                        choices:
                                            - "GT"
                                            - "LT"
                                        required: true
                                    value:
                                        description:
                                            - integer non negative value. 0 < value < 100
                                        type: int
                                        required: true
    auto_scaling_configuration_id:
        description:
            - Unique Oracle-assigned identifier of the autoscaling configuration.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
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
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    node_type: node_type_example
    is_enabled: true
    cluster_admin_password: cluster_admin_password_example
    policy:
      policy_type: THRESHOLD_BASED
      rules:
      - action: CHANGE_SHAPE_SCALE_UP
        metric:
          metric_type: CPU_UTILIZATION
          threshold:
            duration_in_minutes: 56
            operator: GT
            value: 56
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update bds_auto_scale_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bds_auto_scale_config:
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    is_enabled: true
    cluster_admin_password: cluster_admin_password_example
    policy:
      policy_type: THRESHOLD_BASED
      rules:
      - action: CHANGE_SHAPE_SCALE_UP
        metric:
          metric_type: CPU_UTILIZATION
          threshold:
            duration_in_minutes: 56
            operator: GT
            value: 56
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update bds_auto_scale_config
  oci_bds_auto_scale_config:
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete bds_auto_scale_config
  oci_bds_auto_scale_config:
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: cluster_admin_password_example
    auto_scaling_configuration_id: "ocid1.autoscalingconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete bds_auto_scale_config using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bds_auto_scale_config:
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                - The unique identifier for autoscaling configuration.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        node_type:
            description:
                - A node type that is managed by an autoscaling configuration. The only supported type is WORKER.
            returned: on success
            type: string
            sample: node_type_example
        lifecycle_state:
            description:
                - The state of the autoscaling configuration
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - The time the BDS instance was created. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2020-03-29T09:36:42.000+0000
        time_updated:
            description:
                - The time the autoscale configuration was updated.
                  An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2020-04-29T09:36:42.000+0000
        policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                policy_type:
                    description:
                        - Types of autoscaling policies. SCHEDULE-BASED or  THRESHOLD-BASED, current only supported THRESHOLD-BASED.
                    returned: on success
                    type: string
                    sample: THRESHOLD_BASED
                rules:
                    description:
                        - The list of rules for autoscaling. If an action have multiple rules, last rule in the array will be applied.
                    returned: on success
                    type: complex
                    contains:
                        action:
                            description:
                                - "The valid value are - CHANGE_SHAPE_SCALE_UP or CHANGE_SHAPE_SCALE_DOWN"
                            returned: on success
                            type: string
                            sample: CHANGE_SHAPE_SCALE_UP
                        metric:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                metric_type:
                                    description:
                                        - Allowed value is CPU_UTILIZATION currently
                                    returned: on success
                                    type: string
                                    sample: CPU_UTILIZATION
                                threshold:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        duration_in_minutes:
                                            description:
                                                - This value is the minimum period of time metric value meets or exceeds threshold value before action is
                                                  trigger. The value is in minutes.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        operator:
                                            description:
                                                - The comparison operator to use. Options are greater than (GT), less than (LT).
                                            returned: on success
                                            type: string
                                            sample: GT
                                        value:
                                            description:
                                                - integer non negative value. 0 < value < 100
                                            returned: on success
                                            type: int
                                            sample: 56
    sample: {
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
    from oci.bds import BdsClient
    from oci.bds.models import AddAutoScalingConfigurationDetails
    from oci.bds.models import UpdateAutoScalingConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsAutoScaleConfigHelperGen(OCIResourceHelperBase):
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
            bds_instance_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            node_type=dict(type="str"),
            is_enabled=dict(type="bool"),
            cluster_admin_password=dict(type="str", no_log=True),
            policy=dict(
                type="dict",
                options=dict(
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=["THRESHOLD_BASED", "SCHEDULE_BASED"],
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
            auto_scaling_configuration_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
