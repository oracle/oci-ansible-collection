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
module: oci_operator_access_control_operator_control_actions
short_description: Perform actions on an OperatorControl resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OperatorControl resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the Operator Control resource into a different compartment. When provided, 'If-Match' is checked against 'ETag'
      values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operator_control_id:
        description:
            - unique OperatorControl identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the new compartment to contain the operator contol.
        type: str
    action:
        description:
            - The action to perform on the OperatorControl.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on operator_control
  oci_operator_access_control_operator_control_actions:
    # required
    operator_control_id: "ocid1.operatorcontrol.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
operator_control:
    description:
        - Details of the OperatorControl resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the operator control.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        operator_control_name:
            description:
                - Name of the operator control. The name must be unique.
            returned: on success
            type: str
            sample: operator_control_name_example
        description:
            description:
                - Description of operator control.
            returned: on success
            type: str
            sample: description_example
        approvers_list:
            description:
                - List of users who can approve an access request associated with a target resource under the governance of this operator control.
            returned: on success
            type: list
            sample: []
        approver_groups_list:
            description:
                - List of user groups who can approve an access request associated with a target resource under the governance of this operator control.
            returned: on success
            type: list
            sample: []
        pre_approved_op_action_list:
            description:
                - List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be
                  automatically approved if the access request only contain operator actions in the pre-approved list.
            returned: on success
            type: list
            sample: []
        approval_required_op_action_list:
            description:
                - List of operator actions that need explicit approval. Any operator action not in the pre-approved list will require explicit
                  approval. Access requests associated with a resource governed by this operator control will be
                  require explicit approval if the access request contains any operator action in this list.
            returned: on success
            type: list
            sample: []
        is_fully_pre_approved:
            description:
                - Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator
                  control
                  will be auto-approved.
            returned: on success
            type: bool
            sample: true
        email_id_list:
            description:
                - List of emailId.
            returned: on success
            type: list
            sample: []
        resource_type:
            description:
                - resourceType for which the OperatorControl is applicable
            returned: on success
            type: str
            sample: EXACC
        system_message:
            description:
                - System message that would be displayed to the operator users on accessing the target resource under the governance of this operator control.
            returned: on success
            type: str
            sample: system_message_example
        compartment_id:
            description:
                - The OCID of the compartment that contains the operator control.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current lifecycle state of the operator control.
            returned: on success
            type: str
            sample: CREATED
        time_of_creation:
            description:
                - "Time when the operator control was created expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_modification:
            description:
                - "Time when the operator control was last modified expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_deletion:
            description:
                - "Time when deleted expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)timestamp format. Example: '2020-05-22T21:10:29.600Z'.
                  Note a deleted operator control still stays in the system, so that you can still audit operator actions associated with access requests
                  raised on target resources governed by the deleted operator control."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        last_modified_info:
            description:
                - Description associated with the latest modification of the operator control.
            returned: on success
            type: str
            sample: last_modified_info_example
        freeform_tags:
            description:
                - Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "operator_control_name": "operator_control_name_example",
        "description": "description_example",
        "approvers_list": [],
        "approver_groups_list": [],
        "pre_approved_op_action_list": [],
        "approval_required_op_action_list": [],
        "is_fully_pre_approved": true,
        "email_id_list": [],
        "resource_type": "EXACC",
        "system_message": "system_message_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATED",
        "time_of_creation": "2013-10-20T19:20:30+01:00",
        "time_of_modification": "2013-10-20T19:20:30+01:00",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "last_modified_info": "last_modified_info_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.operator_access_control import OperatorControlClient
    from oci.operator_access_control.models import (
        ChangeOperatorControlCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperatorControlActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "operator_control_id"

    def get_module_resource_id(self):
        return self.module.params.get("operator_control_id")

    def get_get_fn(self):
        return self.client.get_operator_control

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_control,
            operator_control_id=self.module.params.get("operator_control_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeOperatorControlCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_operator_control_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operator_control_id=self.module.params.get("operator_control_id"),
                change_operator_control_compartment_details=action_details,
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


OperatorControlActionsHelperCustom = get_custom_class(
    "OperatorControlActionsHelperCustom"
)


class ResourceHelper(
    OperatorControlActionsHelperCustom, OperatorControlActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            operator_control_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="operator_control",
        service_client_class=OperatorControlClient,
        namespace="operator_access_control",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
