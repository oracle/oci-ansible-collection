#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_data_flow_pool
short_description: Manage a Pool resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Pool resource in Oracle Cloud Infrastructure
    - For I(state=present), create a pool to be used by dataflow runs or applications.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_flow_pool_actions) module: change_compartment, start, stop."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of a compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A user-friendly description. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    configurations:
        description:
            - List of PoolConfig items.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            shape:
                description:
                    - The compute shape of the resources you would like to provision.
                type: str
            shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs used for the driver or executors.
                              See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                        type: float
                    memory_in_gbs:
                        description:
                            - The amount of memory used for the driver or executors.
                        type: float
            min:
                description:
                    - Minimum number of compute instances in the pool for a given compute shape.
                type: int
            max:
                description:
                    - Maximum number of compute instances in the pool for a given compute shape.
                type: int
    schedules:
        description:
            - A list of schedules for pool to auto start and stop.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            day_of_week:
                description:
                    - Day of the week SUN-SAT
                type: str
                choices:
                    - "SUNDAY"
                    - "MONDAY"
                    - "TUESDAY"
                    - "WEDNESDAY"
                    - "THURSDAY"
                    - "FRIDAY"
                    - "SATURDAY"
            start_time:
                description:
                    - Hour of the day to start or stop pool.
                type: int
            stop_time:
                description:
                    - Hour of the day to stop the pool.
                type: int
    idle_timeout_in_minutes:
        description:
            - Optional timeout value in minutes used to auto stop Pools. A Pool will be auto stopped after inactivity for this amount of time period.
              If value not set, pool will not be auto stopped auto.
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    pool_id:
        description:
            - The unique ID for a pool.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Pool.
            - Use I(state=present) to create or update a Pool.
            - Use I(state=absent) to delete a Pool.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create pool
  oci_data_flow_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    configurations:
    - # optional
      shape: shape_example
      shape_config:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
      min: 56
      max: 56

    # optional
    description: description_example
    schedules:
    - # optional
      day_of_week: SUNDAY
      start_time: 56
      stop_time: 56
    idle_timeout_in_minutes: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update pool
  oci_data_flow_pool:
    # required
    pool_id: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    configurations:
    - # optional
      shape: shape_example
      shape_config:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
      min: 56
      max: 56
    schedules:
    - # optional
      day_of_week: SUNDAY
      start_time: 56
      stop_time: 56
    idle_timeout_in_minutes: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_flow_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    configurations:
    - # optional
      shape: shape_example
      shape_config:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
      min: 56
      max: 56
    schedules:
    - # optional
      day_of_week: SUNDAY
      start_time: 56
      stop_time: 56
    idle_timeout_in_minutes: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete pool
  oci_data_flow_pool:
    # required
    pool_id: "ocid1.pool.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_flow_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
pool:
    description:
        - Details of the Pool resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        description:
            description:
                - A user-friendly description. Avoid entering confidential information.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - A user-friendly name. It does not have to be unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The OCID of a pool. Unique Id to indentify a dataflow pool resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_details:
            description:
                - The detailed messages about the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of this pool.
            returned: on success
            type: str
            sample: ACCEPTED
        owner_principal_id:
            description:
                - The OCID of the user who created the resource.
            returned: on success
            type: str
            sample: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        owner_user_name:
            description:
                - The username of the user who created the resource.  If the username of the owner does not exist,
                  `null` will be returned and the caller should refer to the ownerPrincipalId value instead.
            returned: on success
            type: str
            sample: owner_user_name_example
        pool_metrics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_last_started:
                    description:
                        - The last time this pool was started.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_stopped:
                    description:
                        - The last time this pool was stopped.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_used:
                    description:
                        - The last time a run used this pool.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_last_metrics_updated:
                    description:
                        - The last time the mertics were updated for this.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                active_runs_count:
                    description:
                        - The number of runs that are currently running that are using this pool.
                    returned: on success
                    type: int
                    sample: 56
                actively_used_node_count:
                    description:
                        - A count of the nodes that are currently being used for each shape in this pool.
                    returned: on success
                    type: complex
                    contains:
                        logical_shape:
                            description:
                                - The compute shape of the nodes that the count is for.
                            returned: on success
                            type: str
                            sample: logical_shape_example
                        count:
                            description:
                                - The node count of this compute shape.
                            returned: on success
                            type: int
                            sample: 56
        configurations:
            description:
                - List of PoolConfig items.
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - The compute shape of the resources you would like to provision.
                    returned: on success
                    type: str
                    sample: shape_example
                shape_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - The total number of OCPUs used for the driver or executors.
                                  See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                            returned: on success
                            type: float
                            sample: 10
                        memory_in_gbs:
                            description:
                                - The amount of memory used for the driver or executors.
                            returned: on success
                            type: float
                            sample: 10
                min:
                    description:
                        - Minimum number of compute instances in the pool for a given compute shape.
                    returned: on success
                    type: int
                    sample: 56
                max:
                    description:
                        - Maximum number of compute instances in the pool for a given compute shape.
                    returned: on success
                    type: int
                    sample: 56
        schedules:
            description:
                - A list of schedules for pool to auto start and stop.
            returned: on success
            type: complex
            contains:
                day_of_week:
                    description:
                        - Day of the week SUN-SAT
                    returned: on success
                    type: str
                    sample: SUNDAY
                start_time:
                    description:
                        - Hour of the day to start or stop pool.
                    returned: on success
                    type: int
                    sample: 56
                stop_time:
                    description:
                        - Hour of the day to stop the pool.
                    returned: on success
                    type: int
                    sample: 56
        idle_timeout_in_minutes:
            description:
                - Optional timeout value in minutes used to auto stop Pools. A Pool will be auto stopped after inactivity for this amount of time period.
                  If value not set, pool will not be auto stopped auto.
            returned: on success
            type: int
            sample: 56
        time_created:
            description:
                - "The date and time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time the resource was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACCEPTED",
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_user_name": "owner_user_name_example",
        "pool_metrics": {
            "time_last_started": "2013-10-20T19:20:30+01:00",
            "time_last_stopped": "2013-10-20T19:20:30+01:00",
            "time_last_used": "2013-10-20T19:20:30+01:00",
            "time_last_metrics_updated": "2013-10-20T19:20:30+01:00",
            "active_runs_count": 56,
            "actively_used_node_count": [{
                "logical_shape": "logical_shape_example",
                "count": 56
            }]
        },
        "configurations": [{
            "shape": "shape_example",
            "shape_config": {
                "ocpus": 10,
                "memory_in_gbs": 10
            },
            "min": 56,
            "max": 56
        }],
        "schedules": [{
            "day_of_week": "SUNDAY",
            "start_time": 56,
            "stop_time": 56
        }],
        "idle_timeout_in_minutes": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import CreatePoolDetails
    from oci.data_flow.models import UpdatePoolDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowPoolHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DataFlowPoolHelperGen, self).get_possible_entity_types() + [
            "dataflowpool",
            "dataflowpools",
            "dataFlowdataflowpool",
            "dataFlowdataflowpools",
            "dataflowpoolresource",
            "dataflowpoolsresource",
            "pool",
            "pools",
            "dataFlowpool",
            "dataFlowpools",
            "poolresource",
            "poolsresource",
            "dataflow",
        ]

    def get_module_resource_id_param(self):
        return "pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("pool_id")

    def get_get_fn(self):
        return self.client.get_pool

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_pool, pool_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pool, pool_id=self.module.params.get("pool_id"),
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
        return oci_common_utils.list_all_resources(self.client.list_pools, **kwargs)

    def get_create_model_class(self):
        return CreatePoolDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(create_pool_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdatePoolDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_pool_details=update_details,
                pool_id=self.module.params.get("pool_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(pool_id=self.module.params.get("pool_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataFlowPoolHelperCustom = get_custom_class("DataFlowPoolHelperCustom")


class ResourceHelper(DataFlowPoolHelperCustom, DataFlowPoolHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            configurations=dict(
                type="list",
                elements="dict",
                options=dict(
                    shape=dict(type="str"),
                    shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                        ),
                    ),
                    min=dict(type="int"),
                    max=dict(type="int"),
                ),
            ),
            schedules=dict(
                type="list",
                elements="dict",
                options=dict(
                    day_of_week=dict(
                        type="str",
                        choices=[
                            "SUNDAY",
                            "MONDAY",
                            "TUESDAY",
                            "WEDNESDAY",
                            "THURSDAY",
                            "FRIDAY",
                            "SATURDAY",
                        ],
                    ),
                    start_time=dict(type="int"),
                    stop_time=dict(type="int"),
                ),
            ),
            idle_timeout_in_minutes=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            pool_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="pool",
        service_client_class=DataFlowClient,
        namespace="data_flow",
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
