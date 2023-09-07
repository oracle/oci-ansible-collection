#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_disaster_recovery_dr_plan_execution_facts
short_description: Fetches details about one or multiple DrPlanExecution resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DrPlanExecution resources in Oracle Cloud Infrastructure
    - Get a summary list of all DR Plan Executions for a DR Protection Group.
    - If I(dr_plan_execution_id) is specified, the details of a single DrPlanExecution will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dr_protection_group_id:
        description:
            - The OCID of the DR Protection Group. Mandatory query param.
            - "Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`"
            - Required to list multiple dr_plan_executions.
        type: str
    lifecycle_state:
        description:
            - A filter to return only DR Plan Executions that match the given lifecycleState.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "WAITING"
            - "CANCELING"
            - "CANCELED"
            - "SUCCEEDED"
            - "FAILED"
            - "DELETING"
            - "DELETED"
            - "PAUSING"
            - "PAUSED"
            - "RESUMING"
    dr_plan_execution_id:
        description:
            - The OCID of the DR Plan Execution.
            - "Example: `ocid1.drplanexecution.oc1.iad.exampleocid`"
            - Required to get a specific dr_plan_execution.
        type: str
        aliases: ["id"]
    dr_plan_execution_type:
        description:
            - The DR Plan Execution type.
        type: str
        choices:
            - "SWITCHOVER"
            - "SWITCHOVER_PRECHECK"
            - "FAILOVER"
            - "FAILOVER_PRECHECK"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
            - "Example: `MY UNIQUE DISPLAY NAME`"
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.
              Default order for displayName is ascending. If no value is specified timeCreated is default.
            - "Example: `displayName`"
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific dr_plan_execution
  oci_disaster_recovery_dr_plan_execution_facts:
    # required
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"

- name: List dr_plan_executions
  oci_disaster_recovery_dr_plan_execution_facts:
    # required
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACCEPTED
    dr_plan_execution_id: "ocid1.drplanexecution.oc1..xxxxxxEXAMPLExxxxxx"
    dr_plan_execution_type: SWITCHOVER
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
dr_plan_executions:
    description:
        - List of DrPlanExecution resources
    returned: on success
    type: complex
    contains:
        execution_options:
            description:
                - ""
                - Returned for get operation
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
        group_executions:
            description:
                - A list of groups executed in this DR Plan Execution.
                - Returned for get operation
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
    sample: [{
        "execution_options": {
            "are_prechecks_enabled": true,
            "plan_execution_type": "SWITCHOVER",
            "are_warnings_ignored": true
        },
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "plan_id": "ocid1.plan.oc1..xxxxxxEXAMPLExxxxxx",
        "plan_execution_type": "SWITCHOVER",
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
        "lifecycle_state": "ACCEPTED",
        "life_cycle_details": "life_cycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.disaster_recovery import DisasterRecoveryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrPlanExecutionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dr_plan_execution_id",
        ]

    def get_required_params_for_list(self):
        return [
            "dr_protection_group_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan_execution,
            dr_plan_execution_id=self.module.params.get("dr_plan_execution_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "dr_plan_execution_id",
            "dr_plan_execution_type",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_dr_plan_executions,
            dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
            **optional_kwargs
        )


DrPlanExecutionFactsHelperCustom = get_custom_class("DrPlanExecutionFactsHelperCustom")


class ResourceFactsHelper(
    DrPlanExecutionFactsHelperCustom, DrPlanExecutionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dr_protection_group_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "WAITING",
                    "CANCELING",
                    "CANCELED",
                    "SUCCEEDED",
                    "FAILED",
                    "DELETING",
                    "DELETED",
                    "PAUSING",
                    "PAUSED",
                    "RESUMING",
                ],
            ),
            dr_plan_execution_id=dict(aliases=["id"], type="str"),
            dr_plan_execution_type=dict(
                type="str",
                choices=[
                    "SWITCHOVER",
                    "SWITCHOVER_PRECHECK",
                    "FAILOVER",
                    "FAILOVER_PRECHECK",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="dr_plan_execution",
        service_client_class=DisasterRecoveryClient,
        namespace="disaster_recovery",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(dr_plan_executions=result)


if __name__ == "__main__":
    main()
