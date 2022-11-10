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
module: oci_data_safe_user_assessment
short_description: Manage an UserAssessment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an UserAssessment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new saved user assessment for one or multiple targets in a compartment. It saves the latest assessments in the
      specified compartment. If a scheduled is passed in, this operation persists the latest assessments that exist at the defined
      date and time, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
    - "This resource has the following action operations in the M(oracle.oci.oci_data_safe_user_assessment_actions) module: change_compartment,
      set_user_assessment_baseline, unset_user_assessment_baseline."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment that contains the user assessment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    target_id:
        description:
            - The OCID of the target database on which the user assessment is to be run.
            - Required for create using I(state=present).
        type: str
    description:
        description:
            - The description of the user assessment.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - The display name of the user assessment.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    schedule:
        description:
            - To schedule the assessment for saving periodically, specify the schedule in this attribute.
              Create or schedule one assessment per compartment. If not defined, the assessment runs immediately.
               Format -
                <version-string>;<version-specific-schedule>
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
    user_assessment_id:
        description:
            - The OCID of the user assessment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the UserAssessment.
            - Use I(state=present) to create or update an UserAssessment.
            - Use I(state=absent) to delete an UserAssessment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create user_assessment
  oci_data_safe_user_assessment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    schedule: schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update user_assessment
  oci_data_safe_user_assessment:
    # required
    user_assessment_id: "ocid1.userassessment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    schedule: schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update user_assessment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_user_assessment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    schedule: schedule_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete user_assessment
  oci_data_safe_user_assessment:
    # required
    user_assessment_id: "ocid1.userassessment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete user_assessment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_safe_user_assessment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
                  of all database risks in one compartment.
                        It is automatically updated once the latest assessment or refresh action is executed, as well as when a target is deleted or move to a
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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_safe import DataSafeClient
    from oci.data_safe.models import CreateUserAssessmentDetails
    from oci.data_safe.models import UpdateUserAssessmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSafeUserAssessmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataSafeUserAssessmentHelperGen, self
        ).get_possible_entity_types() + [
            "userassessment",
            "userassessments",
            "dataSafeuserassessment",
            "dataSafeuserassessments",
            "userassessmentresource",
            "userassessmentsresource",
            "datasafe",
        ]

    def get_module_resource_id_param(self):
        return "user_assessment_id"

    def get_module_resource_id(self):
        return self.module.params.get("user_assessment_id")

    def get_get_fn(self):
        return self.client.get_user_assessment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_user_assessment, user_assessment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user_assessment,
            user_assessment_id=self.module.params.get("user_assessment_id"),
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
            self.client.list_user_assessments, **kwargs
        )

    def get_create_model_class(self):
        return CreateUserAssessmentDetails

    def get_exclude_attributes(self):
        return ["target_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_user_assessment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_user_assessment_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateUserAssessmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_user_assessment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_assessment_id=self.module.params.get("user_assessment_id"),
                update_user_assessment_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_user_assessment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_assessment_id=self.module.params.get("user_assessment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataSafeUserAssessmentHelperCustom = get_custom_class(
    "DataSafeUserAssessmentHelperCustom"
)


class ResourceHelper(
    DataSafeUserAssessmentHelperCustom, DataSafeUserAssessmentHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            target_id=dict(type="str"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            schedule=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            user_assessment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
