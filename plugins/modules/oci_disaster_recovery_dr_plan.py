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
module: oci_disaster_recovery_dr_plan
short_description: Manage a DrPlan resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DrPlan resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new DR Plan of the specified DR Plan type.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    type:
        description:
            - The type of DR Plan to be created.
            - Required for create using I(state=present).
        type: str
        choices:
            - "SWITCHOVER"
            - "FAILOVER"
    dr_protection_group_id:
        description:
            - The OCID of the DR Protection Group to which this DR Plan belongs.
            - "Example: `ocid1.drprotectiongroup.oc1.iad.&lt;unique_id&gt;`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The display name of the DR Plan being created.
            - "Example: `EBS Switchover PHX to IAD`"
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    plan_groups:
        description:
            - An ordered list of plan groups in a DR Plan.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            id:
                description:
                    - The unique id of this group. Must not be modified by user.
                    - "Example: `sgid1.group..&lt;unique_id&gt;`"
                    - This parameter is updatable.
                type: str
            display_name:
                description:
                    - The display name of this group.
                    - "Example: `My_GROUP_3 - EBS Start`"
                    - This parameter is updatable.
                type: str
                aliases: ["name"]
            type:
                description:
                    - The group type.
                    - This parameter is updatable.
                type: str
                choices:
                    - "USER_DEFINED"
                    - "BUILT_IN"
                    - "BUILT_IN_PRECHECK"
            steps:
                description:
                    - The list of steps in this group.
                type: list
                elements: dict
                suboptions:
                    id:
                        description:
                            - The unique id of this step.
                            - "Example: `sgid1.step..&lt;unique_id&gt;`"
                            - This parameter is updatable.
                        type: str
                    display_name:
                        description:
                            - The display name of this step in a group.
                            - "Example: `My_STEP_3A - EBS Start - STAGE A`"
                            - This parameter is updatable.
                        type: str
                        aliases: ["name"]
                    error_mode:
                        description:
                            - The error mode for this step.
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "STOP_ON_ERROR"
                            - "CONTINUE_ON_ERROR"
                    timeout:
                        description:
                            - The timeout in seconds for executing this step.
                            - "Example: `600`"
                            - This parameter is updatable.
                        type: int
                    is_enabled:
                        description:
                            - A flag indicating whether this step should be enabled for execution.
                            - "Example: `true`"
                            - This parameter is updatable.
                        type: bool
                    user_defined_step:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            function_id:
                                description:
                                    - The OCID of function to be invoked.
                                    - "Example: `ocid1.fnfunc.oc1.iad.&lt;unique_id&gt;`"
                                    - This parameter is updatable.
                                    - Required when step_type is 'INVOKE_FUNCTION'
                                type: str
                            request_body:
                                description:
                                    - The request body for the function.
                                    - "Example: `{ \\"FnParam1\\", \\"FnParam2\\" }`"
                                    - This parameter is updatable.
                                    - Applicable when step_type is 'INVOKE_FUNCTION'
                                type: str
                            object_storage_script_location:
                                description:
                                    - ""
                                    - Required when step_type is 'RUN_OBJECTSTORE_SCRIPT'
                                type: dict
                                suboptions:
                                    namespace:
                                        description:
                                            - "The namespace in Object Storage (Note - this is usually the tenancy name)."
                                            - "Example: `myocitenancy`"
                                            - This parameter is updatable.
                                            - Required when step_type is 'RUN_OBJECTSTORE_SCRIPT'
                                        type: str
                                        required: true
                                    bucket:
                                        description:
                                            - The bucket name inside the Object Storage namespace.
                                            - "Example: `custom_dr_scripts`"
                                            - This parameter is updatable.
                                            - Required when step_type is 'RUN_OBJECTSTORE_SCRIPT'
                                        type: str
                                        required: true
                                    object:
                                        description:
                                            - The object name inside the Object Storage bucket.
                                            - "Example: `validate_app_start.sh`"
                                            - This parameter is updatable.
                                            - Required when step_type is 'RUN_OBJECTSTORE_SCRIPT'
                                        type: str
                                        required: true
                            step_type:
                                description:
                                    - The type of the user-defined step.
                                    - "RUN_OBJECTSTORE_SCRIPT - A step which runs a script stored in Oracle Object Storage Service."
                                    - "RUN_LOCAL_SCRIPT - A step which runs a script that resides locally on a compute instance."
                                    - "INVOKE_FUNCTION - A step which invokes an Oracle Function.
                                        See https://docs.oracle.com/en-us/iaas/Content/Functions/home.htm."
                                    - This parameter is updatable.
                                type: str
                                choices:
                                    - "RUN_LOCAL_SCRIPT_PRECHECK"
                                    - "INVOKE_FUNCTION_PRECHECK"
                                    - "INVOKE_FUNCTION"
                                    - "RUN_OBJECTSTORE_SCRIPT"
                                    - "RUN_OBJECTSTORE_SCRIPT_PRECHECK"
                                    - "RUN_LOCAL_SCRIPT"
                                required: true
                            run_on_instance_id:
                                description:
                                    - The OCID of the instance where this script or command should be executed.
                                    - This parameter is updatable.
                                    - Required when step_type is one of ['RUN_LOCAL_SCRIPT', 'RUN_OBJECTSTORE_SCRIPT']
                                type: str
                            script_command:
                                description:
                                    - The script name and arguments.
                                    - "Example: `/usr/bin/python3 /home/opc/scripts/my_app_script.py arg1 arg2 arg3`"
                                    - This parameter is updatable.
                                    - Required when step_type is 'RUN_LOCAL_SCRIPT'
                                type: str
                            run_as_user:
                                description:
                                    - The userid on the instance to be used for executing the script or command.
                                    - "Example: `opc`"
                                    - This parameter is updatable.
                                    - Applicable when step_type is 'RUN_LOCAL_SCRIPT'
                                type: str
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
    dr_plan_id:
        description:
            - The OCID of the DR Plan.
            - "Example: `ocid1.drplan.oc1.iad.exampleocid`"
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DrPlan.
            - Use I(state=present) to create or update a DrPlan.
            - Use I(state=absent) to delete a DrPlan.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create dr_plan
  oci_disaster_recovery_dr_plan:
    # required
    type: SWITCHOVER
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dr_plan
  oci_disaster_recovery_dr_plan:
    # required
    dr_plan_id: "ocid1.drplan.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    plan_groups:
    - # optional
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
      type: USER_DEFINED
      steps:
      - # optional
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        error_mode: STOP_ON_ERROR
        timeout: 56
        is_enabled: true
        user_defined_step:
          # required
          step_type: RUN_LOCAL_SCRIPT_PRECHECK
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update dr_plan using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_disaster_recovery_dr_plan:
    # required
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    plan_groups:
    - # optional
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      display_name: display_name_example
      type: USER_DEFINED
      steps:
      - # optional
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        error_mode: STOP_ON_ERROR
        timeout: 56
        is_enabled: true
        user_defined_step:
          # required
          step_type: RUN_LOCAL_SCRIPT_PRECHECK
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete dr_plan
  oci_disaster_recovery_dr_plan:
    # required
    dr_plan_id: "ocid1.drplan.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete dr_plan using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_disaster_recovery_dr_plan:
    # required
    dr_protection_group_id: "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
dr_plan:
    description:
        - Details of the DrPlan resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of this DR Plan.
                - "Example: `ocid1.drplan.oc1.iad.&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of this DR Plan.
                - "Example: `EBS Switchover PHX to IAD`"
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment containing the DR Plan.
                - "Example: `ocid1.compartment.oc1..&lt;unique_id&gt;`"
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - The type of this DR Plan.
            returned: on success
            type: str
            sample: SWITCHOVER
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
        plan_groups:
            description:
                - The list of groups in this DR Plan.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "SWITCHOVER",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "dr_protection_group_id": "ocid1.drprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_dr_protection_group_id": "ocid1.peerdrprotectiongroup.oc1..xxxxxxEXAMPLExxxxxx",
        "peer_region": "us-phoenix-1",
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
        "lifecycle_state": "CREATING",
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
    from oci.disaster_recovery.models import CreateDrPlanDetails
    from oci.disaster_recovery.models import UpdateDrPlanDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrPlanHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DrPlanHelperGen, self).get_possible_entity_types() + [
            "drplan",
            "drplans",
            "disasterRecoverydrplan",
            "disasterRecoverydrplans",
            "drplanresource",
            "drplansresource",
            "disasterrecovery",
        ]

    def get_module_resource_id_param(self):
        return "dr_plan_id"

    def get_module_resource_id(self):
        return self.module.params.get("dr_plan_id")

    def get_get_fn(self):
        return self.client.get_dr_plan

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan, dr_plan_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dr_plan, dr_plan_id=self.module.params.get("dr_plan_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "dr_protection_group_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["dr_plan_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_dr_plans, **kwargs)

    def get_create_model_class(self):
        return CreateDrPlanDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_dr_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(create_dr_plan_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDrPlanDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_dr_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_dr_plan_details=update_details,
                dr_plan_id=self.module.params.get("dr_plan_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_dr_plan,
            call_fn_args=(),
            call_fn_kwargs=dict(dr_plan_id=self.module.params.get("dr_plan_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DrPlanHelperCustom = get_custom_class("DrPlanHelperCustom")


class ResourceHelper(DrPlanHelperCustom, DrPlanHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            type=dict(type="str", choices=["SWITCHOVER", "FAILOVER"]),
            dr_protection_group_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            plan_groups=dict(
                type="list",
                elements="dict",
                options=dict(
                    id=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    type=dict(
                        type="str",
                        choices=["USER_DEFINED", "BUILT_IN", "BUILT_IN_PRECHECK"],
                    ),
                    steps=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            id=dict(type="str"),
                            display_name=dict(aliases=["name"], type="str"),
                            error_mode=dict(
                                type="str",
                                choices=["STOP_ON_ERROR", "CONTINUE_ON_ERROR"],
                            ),
                            timeout=dict(type="int"),
                            is_enabled=dict(type="bool"),
                            user_defined_step=dict(
                                type="dict",
                                options=dict(
                                    function_id=dict(type="str"),
                                    request_body=dict(type="str"),
                                    object_storage_script_location=dict(
                                        type="dict",
                                        options=dict(
                                            namespace=dict(type="str", required=True),
                                            bucket=dict(type="str", required=True),
                                            object=dict(type="str", required=True),
                                        ),
                                    ),
                                    step_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "RUN_LOCAL_SCRIPT_PRECHECK",
                                            "INVOKE_FUNCTION_PRECHECK",
                                            "INVOKE_FUNCTION",
                                            "RUN_OBJECTSTORE_SCRIPT",
                                            "RUN_OBJECTSTORE_SCRIPT_PRECHECK",
                                            "RUN_LOCAL_SCRIPT",
                                        ],
                                    ),
                                    run_on_instance_id=dict(type="str"),
                                    script_command=dict(type="str"),
                                    run_as_user=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            dr_plan_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dr_plan",
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
