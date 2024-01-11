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
module: oci_disaster_recovery_dr_plan_execution_actions
short_description: Perform actions on a DrPlanExecution resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DrPlanExecution resource in Oracle Cloud Infrastructure
    - "For I(action=cancel), cancel the DR Plan Execution indentified by *drPlanExecutionId*."
    - "For I(action=ignore), ignore failed group or step in DR Plan Execution identified by *drPlanExecutionId* and resume execution."
    - "For I(action=pause), pause the DR Plan Execution identified by *drPlanExecutionId*."
    - "For I(action=resume), resume the DR Plan Execution identified by *drPlanExecutionId*."
    - "For I(action=retry), retry failed group or step in DR Plan Execution identified by *drPlanExecutionId* and resume execution."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    action_type:
        description:
            - The type of control action.
            - Required for I(action=cancel), I(action=pause), I(action=resume).
        type: str
        choices:
            - "CANCEL"
            - "PAUSE"
            - "RESUME"
    group_id:
        description:
            - The unique id of the group to ignore as a whole, or the group containing the step to ignore.
            - "Example: `sgid1.group..&lt;unique_id&gt;`"
            - Required for I(action=ignore), I(action=retry).
        type: str
    step_id:
        description:
            - The unique id of the step to ignore (optional). Only needed when ignoring a step.
            - "Example: `sgid1.step..&lt;unique_id&gt;`"
            - Applicable only for I(action=ignore)I(action=retry).
        type: str
    dr_plan_execution_id:
        description:
            - The OCID of the DR Plan Execution.
            - "Example: `ocid1.drplanexecution.oc1.iad.exampleocid`"
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the DrPlanExecution.
        type: str
        required: true
        choices:
            - "cancel"
            - "ignore"
            - "pause"
            - "resume"
            - "retry"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cancel on dr_plan_execution
  oci_disaster_recovery_dr_plan_execution_actions:
    # required
    action_type: CANCEL
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel

- name: Perform action ignore on dr_plan_execution
  oci_disaster_recovery_dr_plan_execution_actions:
    # required
    group_id: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"
    action: ignore

    # optional
    step_id: "ocid1.step.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action pause on dr_plan_execution
  oci_disaster_recovery_dr_plan_execution_actions:
    # required
    action_type: CANCEL
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"
    action: pause

- name: Perform action resume on dr_plan_execution
  oci_disaster_recovery_dr_plan_execution_actions:
    # required
    action_type: CANCEL
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"
    action: resume

- name: Perform action retry on dr_plan_execution
  oci_disaster_recovery_dr_plan_execution_actions:
    # required
    group_id: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"
    action: retry

    # optional
    step_id: "ocid1.step.oc1..xxxxxxEXAMPLExxxxxx"

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.disaster_recovery import DisasterRecoveryClient
    from oci.disaster_recovery.models import CancelDrPlanExecutionDetails
    from oci.disaster_recovery.models import IgnoreDrPlanExecutionDetails
    from oci.disaster_recovery.models import PauseDrPlanExecutionDetails
    from oci.disaster_recovery.models import ResumeDrPlanExecutionDetails
    from oci.disaster_recovery.models import RetryDrPlanExecutionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrPlanExecutionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
        ignore
        pause
        resume
        retry
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dr_plan_execution_id"

    def get_module_resource_id(self):
        return self.module.params.get("dr_plan_execution_id")

    def get_get_fn(self):
        return self.client.get_dr_plan_execution

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan_execution,
            dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
        )

    def cancel(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CancelDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cancel_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def ignore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IgnoreDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ignore_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ignore_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def pause(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, PauseDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.pause_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pause_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def resume(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ResumeDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resume_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                resume_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def retry(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RetryDrPlanExecutionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.retry_dr_plan_execution,
            call_fn_args=(),
            call_fn_kwargs=dict(
                retry_dr_plan_execution_details=action_details,
                dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DrPlanExecutionActionsHelperCustom = get_custom_class(
    "DrPlanExecutionActionsHelperCustom"
)


class ResourceHelper(
    DrPlanExecutionActionsHelperCustom, DrPlanExecutionActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            action_type=dict(type="str", choices=["CANCEL", "PAUSE", "RESUME"]),
            group_id=dict(type="str"),
            step_id=dict(type="str"),
            dr_plan_execution_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["cancel", "ignore", "pause", "resume", "retry"],
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
