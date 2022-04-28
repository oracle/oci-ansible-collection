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
module: oci_data_safe_security_assessment_facts
short_description: Fetches details about one or multiple SecurityAssessment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SecurityAssessment resources in Oracle Cloud Infrastructure
    - Gets a list of security assessments.
    - The ListSecurityAssessments operation returns only the assessments in the specified `compartmentId`.
      The list does not include any subcompartments of the compartmentId passed.
    - The parameter `accessLevel` specifies whether to return only those compartments for which the
      requestor has INSPECT permissions on at least one resource directly
      or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if
      Principal doesn't have access to even one of the child compartments. This is valid only when
      `compartmentIdInSubtree` is set to `true`.
    - The parameter `compartmentIdInSubtree` applies when you perform ListSecurityAssessments on the
      `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned.
      To get a full list of all compartments and subcompartments in the tenancy (root compartment),
      set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.
    - If I(security_assessment_id) is specified, the details of a single SecurityAssessment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    security_assessment_id:
        description:
            - The OCID of the security assessment.
            - Required to get a specific security_assessment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - A filter to return only resources that match the specified compartment OCID.
            - Required to list multiple security_assessments.
        type: str
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned. Depends on the
              'accessLevel' setting.
        type: bool
    access_level:
        description:
            - Valid values are RESTRICTED and ACCESSIBLE. Default is RESTRICTED.
              Setting this to ACCESSIBLE returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment). When set to RESTRICTED permissions are checked and no partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
    display_name:
        description:
            - A filter to return only resources that match the specified display name.
        type: str
        aliases: ["name"]
    type:
        description:
            - A filter to return only items that match the specified security assessment type.
        type: str
        choices:
            - "LATEST"
            - "SAVED"
            - "SAVE_SCHEDULE"
            - "COMPARTMENT"
    schedule_assessment_id:
        description:
            - The OCID of the security assessment of type SAVE_SCHEDULE.
        type: str
    is_schedule_assessment:
        description:
            - A filter to return only security assessments of type save schedule.
        type: bool
    triggered_by:
        description:
            - A filter to return only security asessments that were created by either user or system.
        type: str
        choices:
            - "USER"
            - "SYSTEM"
    target_id:
        description:
            - A filter to return only items related to a specific target OCID.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    is_baseline:
        description:
            - A filter to return only security assessments that are set as baseline.
        type: bool
    sort_by:
        description:
            - The field to sort by. You can specify only one sort order(sortOrder). The default order for timeCreated is descending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    time_created_greater_than_or_equal_to:
        description:
            - A filter to return only the resources that were created after the specified date and time, as defined by
              L(RFC3339,https://tools.ietf.org/html/rfc3339).
              Using TimeCreatedGreaterThanOrEqualToQueryParam parameter retrieves all resources created after that date.
            - "**Example:** 2016-12-19T16:39:57.600Z"
        type: str
    time_created_less_than:
        description:
            - "Search for resources that were created before a specific date.
              Specifying this parameter corresponding `timeCreatedLessThan`
              parameter will retrieve all resources created before the
              specified created date, in \\"YYYY-MM-ddThh:mmZ\\" format with a Z offset, as
              defined by RFC 3339."
            - "**Example:** 2016-12-19T16:39:57.600Z"
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "SUCCEEDED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific security_assessment
  oci_data_safe_security_assessment_facts:
    # required
    security_assessment_id: "ocid1.securityassessment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List security_assessments
  oci_data_safe_security_assessment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    display_name: display_name_example
    type: LATEST
    schedule_assessment_id: "ocid1.scheduleassessment.oc1..xxxxxxEXAMPLExxxxxx"
    is_schedule_assessment: true
    triggered_by: USER
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    is_baseline: true
    sort_by: timeCreated
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_created_less_than: 2013-10-20T19:20:30+01:00
    lifecycle_state: CREATING

"""

RETURN = """
security_assessments:
    description:
        - List of SecurityAssessment resources
    returned: on success
    type: complex
    contains:
        ignored_targets:
            description:
                - "List containing maps as values.
                  Example: `{\\"Operations\\": [ {\\"CostCenter\\": \\"42\\"} ] }`"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        target_version:
            description:
                - The version of the target database.
                - Returned for get operation
            returned: on success
            type: str
            sample: target_version_example
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace. For more information, see Resource Tags.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        id:
            description:
                - The OCID of the security assessment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The description of the security assessment.
            returned: on success
            type: str
            sample: description_example
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
        ignored_target_ids:
            description:
                - "List containing maps as values.
                  Example: `{\\"Operations\\": [ {\\"CostCenter\\": \\"42\\"} ] }`"
                - Returned for list operation
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
        schedule_security_assessment_id:
            description:
                - The OCID of the security assessment that is responsible for creating this scheduled save assessment.
            returned: on success
            type: str
            sample: "ocid1.schedulesecurityassessment.oc1..xxxxxxEXAMPLExxxxxx"
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
        triggered_by:
            description:
                - Indicates whether the security assessment was created by system or by a user.
            returned: on success
            type: str
            sample: USER
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
    sample: [{
        "ignored_targets": [],
        "target_version": "target_version_example",
        "system_tags": {},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "target_ids": [],
        "ignored_target_ids": [],
        "ignored_assessment_ids": [],
        "is_baseline": true,
        "is_deviated_from_baseline": true,
        "last_compared_baseline_id": "ocid1.lastcomparedbaseline.oc1..xxxxxxEXAMPLExxxxxx",
        "schedule_security_assessment_id": "ocid1.schedulesecurityassessment.oc1..xxxxxxEXAMPLExxxxxx",
        "schedule": "schedule_example",
        "triggered_by": "USER",
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
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_safe import DataSafeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeSecurityAssessmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "security_assessment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_security_assessment,
            security_assessment_id=self.module.params.get("security_assessment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "access_level",
            "display_name",
            "type",
            "schedule_assessment_id",
            "is_schedule_assessment",
            "triggered_by",
            "target_id",
            "sort_order",
            "is_baseline",
            "sort_by",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_security_assessments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataSafeSecurityAssessmentFactsHelperCustom = get_custom_class(
    "DataSafeSecurityAssessmentFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSafeSecurityAssessmentFactsHelperCustom,
    DataSafeSecurityAssessmentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            security_assessment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            display_name=dict(aliases=["name"], type="str"),
            type=dict(
                type="str", choices=["LATEST", "SAVED", "SAVE_SCHEDULE", "COMPARTMENT"]
            ),
            schedule_assessment_id=dict(type="str"),
            is_schedule_assessment=dict(type="bool"),
            triggered_by=dict(type="str", choices=["USER", "SYSTEM"]),
            target_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            is_baseline=dict(type="bool"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "SUCCEEDED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="security_assessment",
        service_client_class=DataSafeClient,
        namespace="data_safe",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(security_assessments=result)


if __name__ == "__main__":
    main()
