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
module: oci_data_safe_security_assessment_actions
short_description: Perform actions on a SecurityAssessment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SecurityAssessment resource in Oracle Cloud Infrastructure
    - "For I(action=change_compartment), moves the specified saved security assessment or future scheduled assessments into a different compartment.
      To start, call first the operation ListSecurityAssessments with filters \\"type = save_schedule\\". This returns the scheduleAssessmentId. Then, call this
      changeCompartment with the scheduleAssessmentId.
      The existing saved security assessments created due to the schedule are not moved. However, all new saves will be associated with the new compartment."
    - For I(action=set_security_assessment_baseline), sets the saved security assessment as the baseline in the compartment where the the specified assessment
      resides. The security assessment needs to be of type 'SAVED'.
    - For I(action=unset_security_assessment_baseline), removes the baseline setting for the saved security assessment. The saved security assessment is no
      longer considered a baseline.
      Sets the if-match parameter to the value of the etag from a previous GET or POST response for that resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment where you want to move the security assessment.
            - Required for I(action=change_compartment).
        type: str
    assessment_ids:
        description:
            - List of security assessment OCIDs that need to be updated while setting the baseline.
            - Applicable only for I(action=set_security_assessment_baseline).
        type: list
        elements: str
    security_assessment_id:
        description:
            - The OCID of the security assessment.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the SecurityAssessment.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "set_security_assessment_baseline"
            - "unset_security_assessment_baseline"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on security_assessment
  oci_data_safe_security_assessment_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    security_assessment_id: "ocid1.securityassessment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action set_security_assessment_baseline on security_assessment
  oci_data_safe_security_assessment_actions:
    # required
    security_assessment_id: "ocid1.securityassessment.oc1..xxxxxxEXAMPLExxxxxx"
    action: set_security_assessment_baseline

    # optional
    assessment_ids: [ "assessment_ids_example" ]

- name: Perform action unset_security_assessment_baseline on security_assessment
  oci_data_safe_security_assessment_actions:
    # required
    security_assessment_id: "ocid1.securityassessment.oc1..xxxxxxEXAMPLExxxxxx"
    action: unset_security_assessment_baseline

"""

RETURN = """
security_assessment:
    description:
        - Details of the SecurityAssessment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the security assessment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time when the security assessment was created. Conforms to the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time when the security assessment was last updated. Conforms to the format defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_assessed:
            description:
                - The date and time when the security assessment was last run. Conforms to the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        compartment_id:
            description:
                - The OCID of the compartment that contains the security assessment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the security assessment.
            returned: on success
            type: str
            sample: display_name_example
        target_ids:
            description:
                - Array of database target OCIDs.
            returned: on success
            type: list
            sample: []
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
        target_version:
            description:
                - The version of the target database.
            returned: on success
            type: str
            sample: target_version_example
        is_baseline:
            description:
                - Indicates whether or not the security assessment is set as a baseline. This is applicable only for saved security assessments.
            returned: on success
            type: bool
            sample: true
        is_deviated_from_baseline:
            description:
                - Indicates if the assessment has deviated from the baseline.
            returned: on success
            type: bool
            sample: true
        last_compared_baseline_id:
            description:
                - The OCID of the baseline against which the latest security assessment was compared.
            returned: on success
            type: str
            sample: "ocid1.lastcomparedbaseline.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the security assessment.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Details about the current state of the security assessment.
            returned: on success
            type: str
            sample: lifecycle_details_example
        schedule_security_assessment_id:
            description:
                - The OCID of the security assessment that is responsible for creating this scheduled save assessment.
            returned: on success
            type: str
            sample: "ocid1.schedulesecurityassessment.oc1..xxxxxxEXAMPLExxxxxx"
        triggered_by:
            description:
                - Indicates whether the security assessment was created by system or by a user.
            returned: on success
            type: str
            sample: USER
        description:
            description:
                - The description of the security assessment.
            returned: on success
            type: str
            sample: description_example
        schedule:
            description:
                - "Schedule to save the assessment periodically in the specified format:
                  <version-string>;<version-specific-schedule>"
                - "Allowed version strings - \\"v1\\"
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
        link:
            description:
                - The summary of findings for the security assessment
            returned: on success
            type: str
            sample: link_example
        type:
            description:
                - "The type of this security assessment. The possible types are:"
                - "LATEST: The most up-to-date assessment that is running automatically for a target. It is system generated.
                  SAVED: A saved security assessment. LATEST assessments are always saved in order to maintain the history of runs. A SAVED assessment is also
                  generated by a 'refresh' action (triggered by the user).
                  SAVE_SCHEDULE: The schedule for periodic saves of LATEST assessments.
                  COMPARTMENT: An automatically managed assessment type that stores all details of targets in one compartment.
                   This type keeps an up-to-date assessment of all database risks in one compartment. It is automatically updated when
                   the latest assessment or refresh action is executed. It is also automatically updated when a target is deleted or move to a different
                   compartment."
            returned: on success
            type: str
            sample: LATEST
        statistics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                targets_count:
                    description:
                        - The total number of targets in this security assessment.
                    returned: on success
                    type: int
                    sample: 56
                high_risk:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        targets_count:
                            description:
                                - The number of targets that contributed to the counts at this risk level.
                            returned: on success
                            type: int
                            sample: 56
                        auditing_findings_count:
                            description:
                                - The number of findings in the Auditing category.
                            returned: on success
                            type: int
                            sample: 56
                        authorization_control_findings_count:
                            description:
                                - The number of findings in the Authorization Control category.
                            returned: on success
                            type: int
                            sample: 56
                        data_encryption_findings_count:
                            description:
                                - The number of findings in the Data Encryption category.
                            returned: on success
                            type: int
                            sample: 56
                        db_configuration_findings_count:
                            description:
                                - The number of findings in the Database Configuration category.
                            returned: on success
                            type: int
                            sample: 56
                        fine_grained_access_control_findings_count:
                            description:
                                - The number of findings in the Fine-Grained Access Control category.
                            returned: on success
                            type: int
                            sample: 56
                        privileges_and_roles_findings_count:
                            description:
                                - The number of findings in the Privileges and Roles category.
                            returned: on success
                            type: int
                            sample: 56
                        user_accounts_findings_count:
                            description:
                                - The number of findings in the User Accounts category.
                            returned: on success
                            type: int
                            sample: 56
                medium_risk:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        targets_count:
                            description:
                                - The number of targets that contributed to the counts at this risk level.
                            returned: on success
                            type: int
                            sample: 56
                        auditing_findings_count:
                            description:
                                - The number of findings in the Auditing category.
                            returned: on success
                            type: int
                            sample: 56
                        authorization_control_findings_count:
                            description:
                                - The number of findings in the Authorization Control category.
                            returned: on success
                            type: int
                            sample: 56
                        data_encryption_findings_count:
                            description:
                                - The number of findings in the Data Encryption category.
                            returned: on success
                            type: int
                            sample: 56
                        db_configuration_findings_count:
                            description:
                                - The number of findings in the Database Configuration category.
                            returned: on success
                            type: int
                            sample: 56
                        fine_grained_access_control_findings_count:
                            description:
                                - The number of findings in the Fine-Grained Access Control category.
                            returned: on success
                            type: int
                            sample: 56
                        privileges_and_roles_findings_count:
                            description:
                                - The number of findings in the Privileges and Roles category.
                            returned: on success
                            type: int
                            sample: 56
                        user_accounts_findings_count:
                            description:
                                - The number of findings in the User Accounts category.
                            returned: on success
                            type: int
                            sample: 56
                low_risk:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        targets_count:
                            description:
                                - The number of targets that contributed to the counts at this risk level.
                            returned: on success
                            type: int
                            sample: 56
                        auditing_findings_count:
                            description:
                                - The number of findings in the Auditing category.
                            returned: on success
                            type: int
                            sample: 56
                        authorization_control_findings_count:
                            description:
                                - The number of findings in the Authorization Control category.
                            returned: on success
                            type: int
                            sample: 56
                        data_encryption_findings_count:
                            description:
                                - The number of findings in the Data Encryption category.
                            returned: on success
                            type: int
                            sample: 56
                        db_configuration_findings_count:
                            description:
                                - The number of findings in the Database Configuration category.
                            returned: on success
                            type: int
                            sample: 56
                        fine_grained_access_control_findings_count:
                            description:
                                - The number of findings in the Fine-Grained Access Control category.
                            returned: on success
                            type: int
                            sample: 56
                        privileges_and_roles_findings_count:
                            description:
                                - The number of findings in the Privileges and Roles category.
                            returned: on success
                            type: int
                            sample: 56
                        user_accounts_findings_count:
                            description:
                                - The number of findings in the User Accounts category.
                            returned: on success
                            type: int
                            sample: 56
                advisory:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        targets_count:
                            description:
                                - The number of targets that contributed to the counts at this risk level.
                            returned: on success
                            type: int
                            sample: 56
                        auditing_findings_count:
                            description:
                                - The number of findings in the Auditing category.
                            returned: on success
                            type: int
                            sample: 56
                        authorization_control_findings_count:
                            description:
                                - The number of findings in the Authorization Control category.
                            returned: on success
                            type: int
                            sample: 56
                        data_encryption_findings_count:
                            description:
                                - The number of findings in the Data Encryption category.
                            returned: on success
                            type: int
                            sample: 56
                        db_configuration_findings_count:
                            description:
                                - The number of findings in the Database Configuration category.
                            returned: on success
                            type: int
                            sample: 56
                        fine_grained_access_control_findings_count:
                            description:
                                - The number of findings in the Fine-Grained Access Control category.
                            returned: on success
                            type: int
                            sample: 56
                        privileges_and_roles_findings_count:
                            description:
                                - The number of findings in the Privileges and Roles category.
                            returned: on success
                            type: int
                            sample: 56
                        user_accounts_findings_count:
                            description:
                                - The number of findings in the User Accounts category.
                            returned: on success
                            type: int
                            sample: 56
                evaluate:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        targets_count:
                            description:
                                - The number of targets that contributed to the counts at this risk level.
                            returned: on success
                            type: int
                            sample: 56
                        auditing_findings_count:
                            description:
                                - The number of findings in the Auditing category.
                            returned: on success
                            type: int
                            sample: 56
                        authorization_control_findings_count:
                            description:
                                - The number of findings in the Authorization Control category.
                            returned: on success
                            type: int
                            sample: 56
                        data_encryption_findings_count:
                            description:
                                - The number of findings in the Data Encryption category.
                            returned: on success
                            type: int
                            sample: 56
                        db_configuration_findings_count:
                            description:
                                - The number of findings in the Database Configuration category.
                            returned: on success
                            type: int
                            sample: 56
                        fine_grained_access_control_findings_count:
                            description:
                                - The number of findings in the Fine-Grained Access Control category.
                            returned: on success
                            type: int
                            sample: 56
                        privileges_and_roles_findings_count:
                            description:
                                - The number of findings in the Privileges and Roles category.
                            returned: on success
                            type: int
                            sample: 56
                        user_accounts_findings_count:
                            description:
                                - The number of findings in the User Accounts category.
                            returned: on success
                            type: int
                            sample: 56
                _pass:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        targets_count:
                            description:
                                - The number of targets that contributed to the counts at this risk level.
                            returned: on success
                            type: int
                            sample: 56
                        auditing_findings_count:
                            description:
                                - The number of findings in the Auditing category.
                            returned: on success
                            type: int
                            sample: 56
                        authorization_control_findings_count:
                            description:
                                - The number of findings in the Authorization Control category.
                            returned: on success
                            type: int
                            sample: 56
                        data_encryption_findings_count:
                            description:
                                - The number of findings in the Data Encryption category.
                            returned: on success
                            type: int
                            sample: 56
                        db_configuration_findings_count:
                            description:
                                - The number of findings in the Database Configuration category.
                            returned: on success
                            type: int
                            sample: 56
                        fine_grained_access_control_findings_count:
                            description:
                                - The number of findings in the Fine-Grained Access Control category.
                            returned: on success
                            type: int
                            sample: 56
                        privileges_and_roles_findings_count:
                            description:
                                - The number of findings in the Privileges and Roles category.
                            returned: on success
                            type: int
                            sample: 56
                        user_accounts_findings_count:
                            description:
                                - The number of findings in the User Accounts category.
                            returned: on success
                            type: int
                            sample: 56
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_assessed": "2013-10-20T19:20:30+01:00",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "target_ids": [],
        "ignored_targets": [],
        "ignored_assessment_ids": [],
        "target_version": "target_version_example",
        "is_baseline": true,
        "is_deviated_from_baseline": true,
        "last_compared_baseline_id": "ocid1.lastcomparedbaseline.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "schedule_security_assessment_id": "ocid1.schedulesecurityassessment.oc1..xxxxxxEXAMPLExxxxxx",
        "triggered_by": "USER",
        "description": "description_example",
        "schedule": "schedule_example",
        "link": "link_example",
        "type": "LATEST",
        "statistics": {
            "targets_count": 56,
            "high_risk": {
                "targets_count": 56,
                "auditing_findings_count": 56,
                "authorization_control_findings_count": 56,
                "data_encryption_findings_count": 56,
                "db_configuration_findings_count": 56,
                "fine_grained_access_control_findings_count": 56,
                "privileges_and_roles_findings_count": 56,
                "user_accounts_findings_count": 56
            },
            "medium_risk": {
                "targets_count": 56,
                "auditing_findings_count": 56,
                "authorization_control_findings_count": 56,
                "data_encryption_findings_count": 56,
                "db_configuration_findings_count": 56,
                "fine_grained_access_control_findings_count": 56,
                "privileges_and_roles_findings_count": 56,
                "user_accounts_findings_count": 56
            },
            "low_risk": {
                "targets_count": 56,
                "auditing_findings_count": 56,
                "authorization_control_findings_count": 56,
                "data_encryption_findings_count": 56,
                "db_configuration_findings_count": 56,
                "fine_grained_access_control_findings_count": 56,
                "privileges_and_roles_findings_count": 56,
                "user_accounts_findings_count": 56
            },
            "advisory": {
                "targets_count": 56,
                "auditing_findings_count": 56,
                "authorization_control_findings_count": 56,
                "data_encryption_findings_count": 56,
                "db_configuration_findings_count": 56,
                "fine_grained_access_control_findings_count": 56,
                "privileges_and_roles_findings_count": 56,
                "user_accounts_findings_count": 56
            },
            "evaluate": {
                "targets_count": 56,
                "auditing_findings_count": 56,
                "authorization_control_findings_count": 56,
                "data_encryption_findings_count": 56,
                "db_configuration_findings_count": 56,
                "fine_grained_access_control_findings_count": 56,
                "privileges_and_roles_findings_count": 56,
                "user_accounts_findings_count": 56
            },
            "_pass": {
                "targets_count": 56,
                "auditing_findings_count": 56,
                "authorization_control_findings_count": 56,
                "data_encryption_findings_count": 56,
                "db_configuration_findings_count": 56,
                "fine_grained_access_control_findings_count": 56,
                "privileges_and_roles_findings_count": 56,
                "user_accounts_findings_count": 56
            }
        },
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
    from oci.data_safe.models import ChangeSecurityAssessmentCompartmentDetails
    from oci.data_safe.models import SecurityAssessmentBaseLineDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeSecurityAssessmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        set_security_assessment_baseline
        unset_security_assessment_baseline
    """

    @staticmethod
    def get_module_resource_id_param():
        return "security_assessment_id"

    def get_module_resource_id(self):
        return self.module.params.get("security_assessment_id")

    def get_get_fn(self):
        return self.client.get_security_assessment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_security_assessment,
            security_assessment_id=self.module.params.get("security_assessment_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSecurityAssessmentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_security_assessment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_assessment_id=self.module.params.get("security_assessment_id"),
                change_security_assessment_compartment_details=action_details,
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

    def set_security_assessment_baseline(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SecurityAssessmentBaseLineDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.set_security_assessment_baseline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_assessment_id=self.module.params.get("security_assessment_id"),
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

    def unset_security_assessment_baseline(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.unset_security_assessment_baseline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_assessment_id=self.module.params.get("security_assessment_id"),
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


DataSafeSecurityAssessmentActionsHelperCustom = get_custom_class(
    "DataSafeSecurityAssessmentActionsHelperCustom"
)


class ResourceHelper(
    DataSafeSecurityAssessmentActionsHelperCustom,
    DataSafeSecurityAssessmentActionsHelperGen,
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
            security_assessment_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "set_security_assessment_baseline",
                    "unset_security_assessment_baseline",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="security_assessment",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
