#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_data_safe_user_assessment_actions
short_description: Perform actions on an UserAssessment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an UserAssessment resource in Oracle Cloud Infrastructure
    - "For I(action=change_compartment), moves the specified saved user assessment or future scheduled assessments into a different compartment.
      To start storing scheduled user assessments on a different compartment, first call the operation ListUserAssessments with
      the filters \\"type = save_schedule\\". That call returns the scheduleAssessmentId. Then call
      ChangeUserAssessmentCompartment with the scheduleAssessmentId. The existing saved user assessments created per the schedule
      are not be moved. However, all new saves will be associated with the new compartment."
    - For I(action=set_user_assessment_baseline), sets the saved user assessment as the baseline in the compartment where the specified assessment resides. The
      user assessment needs to be of type 'SAVED'.
    - For I(action=unset_user_assessment_baseline), removes the baseline setting for the saved user assessment. The saved user assessment is no longer
      considered a baseline.
      Sets the if-match parameter to the value of the etag from a previous GET or POST response for that resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where you want to move the user assessment.
            - Required for I(action=change_compartment).
        type: str
    assessment_ids:
        description:
            - The list of user assessment OCIDs that need to be updated while setting the baseline.
            - Applicable only for I(action=set_user_assessment_baseline).
        type: list
        elements: str
    user_assessment_id:
        description:
            - The OCID of the user assessment.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the UserAssessment.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "set_user_assessment_baseline"
            - "unset_user_assessment_baseline"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on user_assessment
  oci_data_safe_user_assessment_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    user_assessment_id: "ocid1.userassessment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action set_user_assessment_baseline on user_assessment
  oci_data_safe_user_assessment_actions:
    # required
    user_assessment_id: "ocid1.userassessment.oc1..xxxxxxEXAMPLExxxxxx"
    action: set_user_assessment_baseline

    # optional
    assessment_ids: [ "assessment_ids_example" ]

- name: Perform action unset_user_assessment_baseline on user_assessment
  oci_data_safe_user_assessment_actions:
    # required
    user_assessment_id: "ocid1.userassessment.oc1..xxxxxxEXAMPLExxxxxx"
    action: unset_user_assessment_baseline

"""

RETURN = """
user_assessment:
    description:
        - Details of the UserAssessment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment that contains the user assessment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The description of the user assessment.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - The display name of the user assessment.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The OCID of the user assessment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        ignored_targets:
            description:
                - "List containing maps as values.
                  Example: `{\\"Operations\\": [ {\\"CostCenter\\": \\"42\\"} ] }`"
            returned: on success
            type: list
            sample: []
        ignored_assessment_ids:
            description:
                - "List containing maps as values.
                  Example: `{\\"Operations\\": [ {\\"CostCenter\\": \\"42\\"} ] }`"
            returned: on success
            type: list
            sample: []
        is_baseline:
            description:
                - Indicates if the user assessment is set as a baseline. This is applicable only to saved user assessments.
            returned: on success
            type: bool
            sample: true
        is_deviated_from_baseline:
            description:
                - Indicates if the user assessment deviates from the baseline.
            returned: on success
            type: bool
            sample: true
        last_compared_baseline_id:
            description:
                - The OCID of the last user assessment baseline against which the latest assessment was compared.
            returned: on success
            type: str
            sample: "ocid1.lastcomparedbaseline.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the user assessment.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current state of the user assessment.
            returned: on success
            type: str
            sample: lifecycle_details_example
        schedule_assessment_id:
            description:
                - The OCID of the user assessment that is responsible for creating this scheduled save assessment.
            returned: on success
            type: str
            sample: "ocid1.scheduleassessment.oc1..xxxxxxEXAMPLExxxxxx"
        schedule:
            description:
                - "Schedule of the assessment that runs periodically in this specified format:
                    <version-string>;<version-specific-schedule>"
                - " Allowed version strings - \\"v1\\"
                    v1's version specific schedule -<ss> <mm> <hh> <day-of-week> <day-of-month>
                    Each of the above fields potentially introduce constraints. A workrequest is created only
                    when clock time satisfies all the constraints. Constraints introduced:
                    1. seconds = <ss> (So, the allowed range for <ss> is [0, 59])
                    2. minutes = <mm> (So, the allowed range for <mm> is [0, 59])
                    3. hours = <hh> (So, the allowed range for <hh> is [0, 23])
                    <day-of-week> can be either '*' (without quotes or a number between 1(Monday) and 7(Sunday))
                    4. No constraint introduced when it is '*'. When not, day of week must equal the given value
                    <day-of-month> can be either '*' (without quotes or a number between 1 and 28)
                    5. No constraint introduced when it is '*'. When not, day of month must equal the given value"
            returned: on success
            type: str
            sample: schedule_example
        statistics:
            description:
                - "Map that contains maps of values.
                   Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {}
        target_ids:
            description:
                - Array of database target OCIDs.
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the user assessment was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the user assessment was last updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        triggered_by:
            description:
                - Indicates whether the user assessment was created by system or user.
            returned: on success
            type: str
            sample: USER
        type:
            description:
                - "Type of user assessment. Type can be:"
                - "LATEST: The most up-to-date assessment that is running automatically for a target. It is system generated.
                  SAVED: A saved user assessment. LATEST assessments will always be saved to maintain the history of runs. A SAVED assessment is also generated
                  by a 'refresh' action (triggered by the user).
                  SAVE_SCHEDULE: A schedule to periodically save LATEST assessments.
                  COMPARTMENT: An automatic managed assessment type that stores all details of targets in one compartment. This will keep an up-to-date status
                  of all potential risks identified in the compartment.
                         It is automatically updated once the latest assessment or refresh action is executed, as well as when a target is deleted or moved to a
                         different compartment."
            returned: on success
            type: str
            sample: LATEST
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "ignored_targets": [],
        "ignored_assessment_ids": [],
        "is_baseline": true,
        "is_deviated_from_baseline": true,
        "last_compared_baseline_id": "ocid1.lastcomparedbaseline.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "schedule_assessment_id": "ocid1.scheduleassessment.oc1..xxxxxxEXAMPLExxxxxx",
        "schedule": "schedule_example",
        "statistics": {},
        "target_ids": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "triggered_by": "USER",
        "type": "LATEST",
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
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import ChangeUserAssessmentCompartmentDetails
    from oci.data_safe.models import UserAssessmentBaseLineDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeUserAssessmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        set_user_assessment_baseline
        unset_user_assessment_baseline
    """

    @staticmethod
    def get_module_resource_id_param():
        return "user_assessment_id"

    def get_module_resource_id(self):
        return self.module.params.get("user_assessment_id")

    def get_get_fn(self):
        return self.client.get_user_assessment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user_assessment,
            user_assessment_id=self.module.params.get("user_assessment_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeUserAssessmentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_user_assessment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_assessment_id=self.module.params.get("user_assessment_id"),
                change_user_assessment_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def set_user_assessment_baseline(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UserAssessmentBaseLineDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.set_user_assessment_baseline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_assessment_id=self.module.params.get("user_assessment_id"),
                base_line_details=action_details,
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

    def unset_user_assessment_baseline(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.unset_user_assessment_baseline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_assessment_id=self.module.params.get("user_assessment_id"),
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


DataSafeUserAssessmentActionsHelperCustom = get_custom_class(
    "DataSafeUserAssessmentActionsHelperCustom"
)


class ResourceHelper(
    DataSafeUserAssessmentActionsHelperCustom, DataSafeUserAssessmentActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            assessment_ids=dict(type="list", elements="str"),
            user_assessment_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "set_user_assessment_baseline",
                    "unset_user_assessment_baseline",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="user_assessment",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
