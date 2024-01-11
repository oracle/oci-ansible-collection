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
module: oci_disaster_recovery_dr_plan_facts
short_description: Fetches details about one or multiple DrPlan resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DrPlan resources in Oracle Cloud Infrastructure
    - Gets a summary list of all DR Plans for a DR Protection Group.
    - If I(dr_plan_id) is specified, the details of a single DrPlan will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dr_protection_group_id:
        description:
            - The OCID of the DR Protection Group. Mandatory query param.
            - "Example: `ocid1.drprotectiongroup.oc1.phx.exampleocid`"
            - Required to list multiple dr_plans.
        type: str
    lifecycle_state:
        description:
            - A filter to return only DR Plans that match the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "NEEDS_ATTENTION"
    dr_plan_id:
        description:
            - The OCID of the DR Plan.
            - "Example: `ocid1.drplan.oc1.iad.exampleocid`"
            - Required to get a specific dr_plan.
        type: str
        aliases: ["id"]
    dr_plan_type:
        description:
            - The DR Plan type.
        type: str
        choices:
            - "SWITCHOVER"
            - "FAILOVER"
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
- name: Get a specific dr_plan
  oci_disaster_recovery_dr_plan_facts:
    # required
    dr_plan_id: "ocid1.drplan.oc1..xxxxxxEXAMPLExxxxxx"

- name: List dr_plans
  oci_disaster_recovery_dr_plan_facts:
    # required
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    dr_plan_id: "ocid1.drplan.oc1..xxxxxxEXAMPLExxxxxx"
    dr_plan_type: SWITCHOVER
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
dr_plans:
    description:
        - List of DrPlan resources
    returned: on success
    type: complex
    contains:
        plan_groups:
            description:
                - The list of groups in this DR Plan.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The unique id of this group. Must not be modified by user.
                        - "Example: `sgid1.group..&lt;unique_id&gt;`"
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The plan group type.
                    returned: on success
                    type: str
                    sample: USER_DEFINED
                display_name:
                    description:
                        - The display name of this DR Plan Group.
                        - "Example: `DATABASE_SWITCHOVER`"
                    returned: on success
                    type: str
                    sample: display_name_example
                steps:
                    description:
                        - The list of steps in this plan group.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The unique id of this step. Must not be modified by the user.
                                - "Example: `sgid1.step..&lt;unique_id&gt;`"
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        group_id:
                            description:
                                - The unique id of the group to which this step belongs. Must not be modified by user.
                                - "Example: `sgid1.group..&lt;unique_id&gt;`"
                            returned: on success
                            type: str
                            sample: "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx"
                        member_id:
                            description:
                                - The OCID of the member associated with this step.
                                - "Example: `ocid1.database.oc1.phx.&lt;unique_id&gt;`"
                            returned: on success
                            type: str
                            sample: "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx"
                        type:
                            description:
                                - The plan step type.
                            returned: on success
                            type: str
                            sample: COMPUTE_INSTANCE_STOP_PRECHECK
                        display_name:
                            description:
                                - The display name of this DR Plan Group.
                                - "Example: `DATABASE_SWITCHOVER`"
                            returned: on success
                            type: str
                            sample: display_name_example
                        error_mode:
                            description:
                                - The error mode for this step.
                            returned: on success
                            type: str
                            sample: STOP_ON_ERROR
                        timeout:
                            description:
                                - The timeout in seconds for executing this step.
                                - "Example: `600`"
                            returned: on success
                            type: int
                            sample: 56
                        is_enabled:
                            description:
                                - A flag indicating whether this step should be enabled for execution.
                                - "Example: `true`"
                            returned: on success
                            type: bool
                            sample: true
                        user_defined_step:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                function_id:
                                    description:
                                        - The OCID of function to be invoked.
                                        - "Example: `ocid1.fnfunc.oc1.iad.&lt;unique_id&gt;`"
                                    returned: on success
                                    type: str
                                    sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                                function_region:
                                    description:
                                        - The region in which the function is deployed.
                                        - "Example: `us-ashburn-1`"
                                    returned: on success
                                    type: str
                                    sample: us-phoenix-1
                                request_body:
                                    description:
                                        - The request body for the function.
                                        - "Example: `{ \\"FnParam1\\", \\"FnParam2\\" }`"
                                    returned: on success
                                    type: str
                                    sample: request_body_example
                                script_command:
                                    description:
                                        - The script name and arguments.
                                        - "Example: `/usr/bin/python3 /home/opc/scripts/my_app_script.py arg1 arg2 arg3`"
                                    returned: on success
                                    type: str
                                    sample: script_command_example
                                run_as_user:
                                    description:
                                        - The userid on the instance to be used for executing the script or command.
                                        - "Example: `opc`"
                                    returned: on success
                                    type: str
                                    sample: run_as_user_example
                                run_on_instance_id:
                                    description:
                                        - The OCID of the instance where this script or command should be executed.
                                        - "Example: `ocid1.instance.oc1.phx.&lt;unique_id&gt;`"
                                    returned: on success
                                    type: str
                                    sample: "ocid1.runoninstance.oc1..xxxxxxEXAMPLExxxxxx"
                                run_on_instance_region:
                                    description:
                                        - The region in which the instance is present.
                                        - "Example: `us-phoenix-1`"
                                    returned: on success
                                    type: str
                                    sample: us-phoenix-1
                                object_storage_script_location:
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
                                                - "Example: `custom_dr_scripts`"
                                            returned: on success
                                            type: str
                                            sample: bucket_example
                                        object:
                                            description:
                                                - The object name inside the Object Storage bucket.
                                                - "Example: `validate_app_start.sh`"
                                            returned: on success
                                            type: str
                                            sample: object_example
                                step_type:
                                    description:
                                        - The type of the step.
                                        - " RUN_OBJECTSTORE_SCRIPT_PRECHECK - A step which performs a precheck on a script stored
                                              in Oracle Object Storage Service"
                                        - " RUN_LOCAL_SCRIPT_PRECHECK - A step which performs a precheck on a script which resides
                                              locally on a compute instance"
                                        - " INVOKE_FUNCTION_PRECHECK - A step which performs a precheck on an Oracle Function.
                                              See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm."
                                        - " RUN_OBJECTSTORE_SCRIPT - A step which runs a script stored in
                                              Oracle Object Storage Service"
                                        - " RUN_LOCAL_SCRIPT - A step which runs a script that resides locally
                                              on a compute instance"
                                        - " INVOKE_FUNCTION - A step which invokes an Oracle Function.
                                              See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm."
                                    returned: on success
                                    type: str
                                    sample: RUN_OBJECTSTORE_SCRIPT_PRECHECK
        id:
            description:
                - The OCID of this DR Plan.
                - "Example: `ocid1.drplan.oc1.iad.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the DR Plan.
                - "Example: `ocid1.compartment.oc1..&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of this DR Plan.
                - "Example: `EBS Switchover PHX to IAD`"
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - The type of this DR Plan.
            returned: on success
            type: str
            sample: SWITCHOVER
        dr_protection_group_id:
            description:
                - The OCID of the DR Protection Group with which this DR Plan is associated.
                - "Example: `ocid1.drplan.oc1.iad.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
        peer_dr_protection_group_id:
            description:
                - The OCID of the peer (remote) DR Protection Group associated with this plan's
                  DR Protection Group.
                - "Example: `ocid1.drprotectiongroup.oc1.phx.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.peerdrprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
        peer_region:
            description:
                - The region of the peer (remote) DR Protection Group associated with this plan's
                  DR Protection Group.
                - "Example: `us-phoenix-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        time_created:
            description:
                - The date and time the DR Plan was created. An RFC3339 formatted datetime string.
                - "Example: `2019-03-29T09:36:42Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the DR Plan was updated. An RFC3339 formatted datetime string.
                - "Example: `2019-03-29T09:36:42Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the DR Plan.
            returned: on success
            type: str
            sample: CREATING
        life_cycle_details:
            description:
                - A message describing the DR Plan's current state in more detail.
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
        "plan_groups": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "USER_DEFINED",
            "display_name": "display_name_example",
            "steps": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "group_id": "ocid1.group.oc1..xxxxxxEXAMPLExxxxxx",
                "member_id": "ocid1.member.oc1..xxxxxxEXAMPLExxxxxx",
                "type": "COMPUTE_INSTANCE_STOP_PRECHECK",
                "display_name": "display_name_example",
                "error_mode": "STOP_ON_ERROR",
                "timeout": 56,
                "is_enabled": true,
                "user_defined_step": {
                    "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
                    "function_region": "us-phoenix-1",
                    "request_body": "request_body_example",
                    "script_command": "script_command_example",
                    "run_as_user": "run_as_user_example",
                    "run_on_instance_id": "ocid1.runoninstance.oc1..xxxxxxEXAMPLExxxxxx",
                    "run_on_instance_region": "us-phoenix-1",
                    "object_storage_script_location": {
                        "namespace": "namespace_example",
                        "bucket": "bucket_example",
                        "object": "object_example"
                    },
                    "step_type": "RUN_OBJECTSTORE_SCRIPT_PRECHECK"
                }
            }]
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "type": "SWITCHOVER",
        "dr_protection_group_id": "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_dr_protection_group_id": "ocid1.peerdrprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_region": "us-phoenix-1",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
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


class DrPlanFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dr_plan_id",
        ]

    def get_required_params_for_list(self):
        return [
            "dr_protection_group_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan, dr_plan_id=self.module.params.get("dr_plan_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "dr_plan_id",
            "dr_plan_type",
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
            self.client.list_dr_plans,
            dr_protection_group_id=self.module.params.get("dr_protection_group_id"),
            **optional_kwargs
        )


DrPlanFactsHelperCustom = get_custom_class("DrPlanFactsHelperCustom")


class ResourceFactsHelper(DrPlanFactsHelperCustom, DrPlanFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dr_protection_group_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "NEEDS_ATTENTION",
                ],
            ),
            dr_plan_id=dict(aliases=["id"], type="str"),
            dr_plan_type=dict(type="str", choices=["SWITCHOVER", "FAILOVER"]),
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
        resource_type="dr_plan",
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

    module.exit_json(dr_plans=result)


if __name__ == "__main__":
    main()
