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
module: oci_disaster_recovery_dr_plan_execution
short_description: Manage a DrPlanExecution resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DrPlanExecution resource in Oracle Cloud Infrastructure
    - For I(state=present), execute a DR Plan for a DR Protection Group.
    - "This resource has the following action operations in the M(oracle.oci.oci_disaster_recovery_dr_plan_execution_actions) module: cancel, ignore, pause,
      resume, retry."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    plan_id:
        description:
            - The OCID of the DR Plan.
            - "Example: `ocid1.drplan.oc1.iad.&lt;unique_id&gt;`"
            - Required for create using I(state=present).
        type: str
    execution_options:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            plan_execution_type:
                description:
                    - The type of the plan execution.
                type: str
                choices:
                    - "SWITCHOVER_PRECHECK"
                    - "FAILOVER_PRECHECK"
                    - "SWITCHOVER"
                    - "FAILOVER"
                required: true
            are_prechecks_enabled:
                description:
                    - A flag indicating whether prechecks should be executed before the plan execution.
                    - "Example: `false`"
                    - Applicable when plan_execution_type is one of ['SWITCHOVER', 'FAILOVER']
                type: bool
            are_warnings_ignored:
                description:
                    - A flag indicating whether warnings should be ignored during the switchover precheck.
                    - "Example: `true`"
                type: bool
    display_name:
        description:
            - The display name of the DR Plan Execution.
            - "Example: `Execution - EBS Switchover PHX to IAD`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    dr_plan_execution_id:
        description:
            - The OCID of the DR Plan Execution.
            - "Example: `ocid1.drplanexecution.oc1.iad.exampleocid`"
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    dr_protection_group_id:
        description:
            - The OCID of the DR Protection Group. Mandatory query param.
            - "Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the DrPlanExecution.
            - Use I(state=present) to create or update a DrPlanExecution.
            - Use I(state=absent) to delete a DrPlanExecution.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create dr_plan_execution
  oci_disaster_recovery_dr_plan_execution:
    # required
    plan_id: "ocid1.plan.oc1..xxxxxxEXAMPLExxxxxx"
    execution_options:
      # required
      plan_execution_type: SWITCHOVER_PRECHECK

      # optional
      are_warnings_ignored: true

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dr_plan_execution
  oci_disaster_recovery_dr_plan_execution:
    # required
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dr_plan_execution using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_disaster_recovery_dr_plan_execution:
    # required
    display_name: display_name_example
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete dr_plan_execution
  oci_disaster_recovery_dr_plan_execution:
    # required
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete dr_plan_execution using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_disaster_recovery_dr_plan_execution:
    # required
    display_name: display_name_example
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
dr_plan_execution:
    description:
        - Details of the DrPlanExecution resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the DR Plan Execution.
                - "Example: `ocid1.drplanexecution.oc1.iad.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing this DR Plan Execution.
                - "Example: `ocid1.compartment.oc1..&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of this DR Plan Execution.
                - "Example: `Execution - EBS Switchover PHX to IAD`"
            returned: on success
            type: str
            sample: display_name_example
        plan_id:
            description:
                - The OCID of the DR Plan.
                - "Example: `ocid1.drplan.oc1.iad.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.plan.oc1..xxxxxxEXAMPLExxxxxx"
        plan_execution_type:
            description:
                - The type of the DR Plan executed.
            returned: on success
            type: str
            sample: SWITCHOVER
        execution_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                are_prechecks_enabled:
                    description:
                        - A flag indicating whether prechecks should be executed before the plan execution.
                        - "Example: `true`"
                    returned: on success
                    type: bool
                    sample: true
                plan_execution_type:
                    description:
                        - The type of the plan execution.
                    returned: on success
                    type: str
                    sample: SWITCHOVER
                are_warnings_ignored:
                    description:
                        - A flag indicating whether warnings should be ignored during the plan execution.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: true
        dr_protection_group_id:
            description:
                - The OCID of the DR Protection Group to which this DR Plan Execution belongs.
                - "Example: `ocid1.drprotectiongroup.oc1.iad.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
        peer_dr_protection_group_id:
            description:
                - The OCID of peer (remote) DR Protection Group associated with this plan's
                  DR Protection Group.
                - "Example: `ocid1.drprotectiongroup.oc1.phx.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.peerdrprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
        peer_region:
            description:
                - The region of the peer (remote) DR Protection Group.
                - "Example: `us-ashburn-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        log_location:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                namespace:
                    description:
                        - "The namespace in Object Storage (Note - this is usually the tenancy name)."
                        - "Example: `myocitenancy`"
                    returned: on success
                    type: str
                    sample: namespace_example
                bucket:
                    description:
                        - The bucket name inside the Object Storage namespace.
                        - "Example: `operation_logs`"
                    returned: on success
                    type: str
                    sample: bucket_example
                object:
                    description:
                        - The object name inside the Object Storage bucket.
                        - "Example: `switchover_plan_executions`"
                    returned: on success
                    type: str
                    sample: object_example
        time_created:
            description:
                - The date and time at which DR Plan Execution was created. An RFC3339 formatted datetime string.
                - "Example: `2019-03-29T09:36:42Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - The date and time at which DR Plan Execution began. An RFC3339 formatted datetime string.
                - "Example: `2019-03-29T09:36:42Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time at which DR Plan Execution was last updated. An RFC3339 formatted datetime string.
                - "Example: `2019-03-29T09:36:42Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The date and time at which DR Plan Execution succeeded, failed, was paused, or was canceled.
                  An RFC3339 formatted datetime string.
                - "Example: `2019-03-29T09:36:42Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        execution_duration_in_sec:
            description:
                - The total duration in seconds taken to complete the DR Plan Execution.
                - "Example: `750`"
            returned: on success
            type: int
            sample: 56
        group_executions:
            description:
                - A list of groups executed in this DR Plan Execution.
            returned: on success
            type: complex
            contains:
                group_id:
                    description:
                        - The unique id of the group. Must not be modified by user.
                        - "Example: `sgid1.group..&lt;unique_id&gt;`"
                    returned: on success
                    type: str
                    sample: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The plan group type.
                    returned: on success
                    type: str
                    sample: USER_DEFINED
                display_name:
                    description:
                        - The display name of group that was executed.
                        - "Example: `DATABASE_SWITCHOVER`"
                    returned: on success
                    type: str
                    sample: display_name_example
                status:
                    description:
                        - The status of the group execution.
                    returned: on success
                    type: str
                    sample: QUEUED
                status_details:
                    description:
                        - Additional details about the group execution status.
                        - "Example: `A total of three steps failed in the group`"
                    returned: on success
                    type: str
                    sample: status_details_example
                time_started:
                    description:
                        - The time at which group execution began. An RFC3339 formatted datetime string.
                        - "Example: `2019-03-29T09:36:42Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_ended:
                    description:
                        - The time at which group execution ended. An RFC3339 formatted datetime string.
                        - "Example: `2019-03-29T09:36:42Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                execution_duration_in_sec:
                    description:
                        - The total duration in seconds taken to complete group execution.
                        - "Example: `120`"
                    returned: on success
                    type: int
                    sample: 56
                step_executions:
                    description:
                        - A list of details of each step executed in this group.
                    returned: on success
                    type: complex
                    contains:
                        step_id:
                            description:
                                - The unique id of this step. Must not be modified by user.
                                - "Example: `sgid1.step..&lt;unique_id&gt;`"
                            returned: on success
                            type: str
                            sample: "ocid1.step.oc1..xxxxxxEXAMPLExxxxxx"
                        type:
                            description:
                                - The plan step type.
                            returned: on success
                            type: str
                            sample: COMPUTE_INSTANCE_STOP_PRECHECK
                        group_id:
                            description:
                                - The unique id of the group to which this step belongs. Must not be modified by user.
                                - "Example: `sgid1.group..&lt;unique_id&gt;`"
                            returned: on success
                            type: str
                            sample: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - The display name of the step.
                                - "Example: `DATABASE_SWITCHOVER`"
                            returned: on success
                            type: str
                            sample: display_name_example
                        log_location:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                namespace:
                                    description:
                                        - "The namespace in Object Storage (Note - this is usually the tenancy name)."
                                        - "Example: `myocitenancy`"
                                    returned: on success
                                    type: str
                                    sample: namespace_example
                                bucket:
                                    description:
                                        - The bucket name inside the Object Storage namespace.
                                        - "Example: `operation_logs`"
                                    returned: on success
                                    type: str
                                    sample: bucket_example
                                object:
                                    description:
                                        - The object name inside the Object Storage bucket.
                                        - "Example: `switchover_plan_executions`"
                                    returned: on success
                                    type: str
                                    sample: object_example
                        status:
                            description:
                                - The status of the step execution.
                            returned: on success
                            type: str
                            sample: QUEUED
                        status_details:
                            description:
                                - Additional details about the step execution status.
                                - "Example: `This step failed to complete due to a timeout`"
                            returned: on success
                            type: str
                            sample: status_details_example
                        time_started:
                            description:
                                - The time at which step execution began. An RFC3339 formatted datetime string.
                                - "Example: `2019-03-29T09:36:42Z`"
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_ended:
                            description:
                                - The time at which step execution ended. An RFC3339 formatted datetime string.
                                - "Example: `2019-03-29T09:36:42Z`"
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        execution_duration_in_sec:
                            description:
                                - The total duration in seconds taken to complete step execution.
                                - "Example: `35`"
                            returned: on success
                            type: int
                            sample: 56
        lifecycle_state:
            description:
                - The current state of the DR Plan Execution.
            returned: on success
            type: str
            sample: ACCEPTED
        life_cycle_details:
            description:
                - A message describing the DR Plan Execution's current state in more detail.
                - "Example: `The DR Plan Execution [Execution - EBS Switchover PHX to IAD] is currently in progress`"
            returned: on success
            type: str
            sample: life_cycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "plan_id": "ocid1.plan.oc1..xxxxxxEXAMPLExxxxxx",
        "plan_execution_type": "SWITCHOVER",
        "execution_options": {
            "are_prechecks_enabled": true,
            "plan_execution_type": "SWITCHOVER",
            "are_warnings_ignored": true
        },
        "dr_protection_group_id": "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_dr_protection_group_id": "ocid1.peerdrprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_region": "us-phoenix-1",
        "log_location": {
            "namespace": "namespace_example",
            "bucket": "bucket_example",
            "object": "object_example"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "execution_duration_in_sec": 56,
        "group_executions": [{
            "group_id": "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "USER_DEFINED",
            "display_name": "display_name_example",
            "status": "QUEUED",
            "status_details": "status_details_example",
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_ended": "2013-10-20T19:20:30+01:00",
            "execution_duration_in_sec": 56,
            "step_executions": [{
                "step_id": "ocid1.step.oc1..xxxxxxEXAMPLExxxxxx",
                "type": "COMPUTE_INSTANCE_STOP_PRECHECK",
                "group_id": "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "log_location": {
                    "namespace": "namespace_example",
                    "bucket": "bucket_example",
                    "object": "object_example"
                },
                "status": "QUEUED",
                "status_details": "status_details_example",
                "time_started": "2013-10-20T19:20:30+01:00",
                "time_ended": "2013-10-20T19:20:30+01:00",
                "execution_duration_in_sec": 56
            }]
        }],
        "lifecycle_state": "ACCEPTED",
        "life_cycle_details": "life_cycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.disaster_recovery import DisasterRecoveryClient
    from oci.disaster_recovery.models import CreateDrPlanExecutionDetails
    from oci.disaster_recovery.models import UpdateDrPlanExecutionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrPlanExecutionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DrPlanExecutionHelperGen, self).get_possible_entity_types() + [
            "drplanexecution",
            "drplanexecutions",
            "disasterRecoverydrplanexecution",
            "disasterRecoverydrplanexecutions",
            "drplanexecutionresource",
            "drplanexecutionsresource",
            "disasterrecovery",
        ]

    def get_module_resource_id_param(self):
        return "dr_plan_execution_id"

    def get_module_resource_id(self):
        return self.module.params.get("dr_plan_execution_id")

    def get_get_fn(self):
        return self.client.get_dr_plan_execution

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan_execution, dr_plan_execution_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan_execution,
            dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "dr_protection_group_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["dr_plan_execution_id", "display_name"]

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
            self.client.list_dr_plan_executions, **kwargs
        )

    def get_create_model_class(self):
        return CreateDrPlanExecutionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(create_dr_plan_execution_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDrPlanExecutionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_dr_plan_execution_details=update_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DrPlanExecutionHelperCustom = get_custom_class("DrPlanExecutionHelperCustom")


class ResourceHelper(DrPlanExecutionHelperCustom, DrPlanExecutionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            plan_id=dict(type="str"),
            execution_options=dict(
                type="dict",
                options=dict(
                    plan_execution_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "SWITCHOVER_PRECHECK",
                            "FAILOVER_PRECHECK",
                            "SWITCHOVER",
                            "FAILOVER",
                        ],
                    ),
                    are_prechecks_enabled=dict(type="bool"),
                    are_warnings_ignored=dict(type="bool"),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            dr_plan_execution_id=dict(aliases=["id"], type="str"),
            dr_protection_group_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dr_plan_execution",
        service_client_class=DisasterRecoveryClient,
        namespace="disaster_recovery",
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
