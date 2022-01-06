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
module: oci_data_safe_security_assessment
short_description: Manage a SecurityAssessment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a SecurityAssessment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new saved security assessment for one or multiple targets in a compartment. When this operation is performed,
      it will save the latest assessments in the specified compartment. If a schedule is passed, it will persist the latest assessments,
      at the defined date and time, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
    - "This resource has the following action operations in the M(oracle.oci.oci_data_safe_security_assessment_actions) module: change_compartment,
      set_security_assessment_baseline, unset_security_assessment_baseline."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that contains the security assessment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The display name of the security assessment.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the security assessment.
            - This parameter is updatable.
        type: str
    target_id:
        description:
            - The OCID of the target database on which security assessment is to be run.
            - Required for create using I(state=present).
        type: str
    schedule:
        description:
            - To schedule the assessment for running periodically, specify the schedule in this attribute.
              Create or schedule one assessment per compartment. If not defined, the assessment runs immediately.
              Format -
              <version-string>;<version-specific-schedule>
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
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm)
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    security_assessment_id:
        description:
            - The OCID of the security assessment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the SecurityAssessment.
            - Use I(state=present) to create or update a SecurityAssessment.
            - Use I(state=absent) to delete a SecurityAssessment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create security_assessment
  oci_data_safe_security_assessment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    schedule: schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update security_assessment
  oci_data_safe_security_assessment:
    # required
    security_assessment_id: "ocid1.securityassessment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    schedule: schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update security_assessment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_security_assessment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    schedule: schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete security_assessment
  oci_data_safe_security_assessment:
    # required
    security_assessment_id: "ocid1.securityassessment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete security_assessment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_security_assessment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import CreateSecurityAssessmentDetails
    from oci.data_safe.models import UpdateSecurityAssessmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeSecurityAssessmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "target_id"]

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
            self.client.list_security_assessments, **kwargs
        )

    def get_create_model_class(self):
        return CreateSecurityAssessmentDetails

    def get_exclude_attributes(self):
        return ["target_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_security_assessment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_security_assessment_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateSecurityAssessmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_security_assessment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_assessment_id=self.module.params.get("security_assessment_id"),
                update_security_assessment_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_security_assessment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                security_assessment_id=self.module.params.get("security_assessment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataSafeSecurityAssessmentHelperCustom = get_custom_class(
    "DataSafeSecurityAssessmentHelperCustom"
)


class ResourceHelper(
    DataSafeSecurityAssessmentHelperCustom, DataSafeSecurityAssessmentHelperGen
):
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
            target_id=dict(type="str"),
            schedule=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            security_assessment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="security_assessment",
        service_client_class=DataSafeClient,
        namespace="data_safe",
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
