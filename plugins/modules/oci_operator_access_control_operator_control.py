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
module: oci_operator_access_control_operator_control
short_description: Manage an OperatorControl resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OperatorControl resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an Operator Control.
    - "This resource has the following action operations in the M(oracle.oci.oci_operator_access_control_operator_control_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    resource_type:
        description:
            - resourceType for which the OperatorControl is applicable
            - Required for create using I(state=present).
        type: str
        choices:
            - "EXACC"
            - "EXADATAINFRASTRUCTURE"
            - "AUTONOMOUSVMCLUSTER"
            - "CLOUDAUTONOMOUSVMCLUSTER"
            - "CCCINFRASTRUCTURE"
    compartment_id:
        description:
            - The OCID of the compartment that contains this operator control.
            - Required for create using I(state=present).
        type: str
    operator_control_name:
        description:
            - Name of the operator control.
            - Required for create using I(state=present), update using I(state=present) with operator_control_id present.
        type: str
    approvers_list:
        description:
            - List of users who can approve an access request associated with a resource governed by this operator control.
            - This parameter is updatable.
        type: list
        elements: str
    approver_groups_list:
        description:
            - List of user groups who can approve an access request associated with a resource governed by this operator control.
            - Required for create using I(state=present), update using I(state=present) with operator_control_id present.
        type: list
        elements: str
    pre_approved_op_action_list:
        description:
            - List of pre-approved operator actions. Access requests associated with a resource governed by this operator control will be
              auto-approved if the access request only contain operator actions in the pre-approved list.
            - This parameter is updatable.
        type: list
        elements: str
    is_fully_pre_approved:
        description:
            - Whether all the operator actions have been pre-approved. If yes, all access requests associated with a resource governed by this operator control
              will be auto-approved.
            - Required for create using I(state=present), update using I(state=present) with operator_control_id present.
        type: bool
    email_id_list:
        description:
            - List of emailId.
            - This parameter is updatable.
        type: list
        elements: str
    system_message:
        description:
            - This is the message that will be displayed to the operator users while accessing the system.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
            - This parameter is updatable.
        type: dict
    operator_control_id:
        description:
            - unique OperatorControl identifier
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    description:
        description:
            - Description of the operator control.
            - This parameter is updatable.
        type: str
    state:
        description:
            - The state of the OperatorControl.
            - Use I(state=present) to create or update an OperatorControl.
            - Use I(state=absent) to delete an OperatorControl.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create operator_control
  oci_operator_access_control_operator_control:
    # required
    resource_type: EXACC
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    operator_control_name: operator_control_name_example
    approver_groups_list: [ "approver_groups_list_example" ]
    is_fully_pre_approved: true

    # optional
    approvers_list: [ "approvers_list_example" ]
    pre_approved_op_action_list: [ "pre_approved_op_action_list_example" ]
    email_id_list: [ "email_id_list_example" ]
    system_message: system_message_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example

- name: Update operator_control
  oci_operator_access_control_operator_control:
    # required
    operator_control_name: operator_control_name_example
    approver_groups_list: [ "approver_groups_list_example" ]
    is_fully_pre_approved: true
    operator_control_id: "ocid1.operatorcontrol.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    approvers_list: [ "approvers_list_example" ]
    pre_approved_op_action_list: [ "pre_approved_op_action_list_example" ]
    email_id_list: [ "email_id_list_example" ]
    system_message: system_message_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example

- name: Delete operator_control
  oci_operator_access_control_operator_control:
    # required
    operator_control_id: "ocid1.operatorcontrol.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    description: description_example

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
        is_default_operator_control:
            description:
                - Whether the operator control is a default Operator Control.
            returned: on success
            type: bool
            sample: true
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
        "is_default_operator_control": true,
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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.operator_access_control import OperatorControlClient
    from oci.operator_access_control.models import CreateOperatorControlDetails
    from oci.operator_access_control.models import UpdateOperatorControlDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperatorControlHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(OperatorControlHelperGen, self).get_possible_entity_types() + [
            "operatorcontrol",
            "operatorcontrols",
            "operatorAccessControloperatorcontrol",
            "operatorAccessControloperatorcontrols",
            "operatorcontrolresource",
            "operatorcontrolsresource",
            "operatoraccesscontrol",
        ]

    def get_module_resource_id_param(self):
        return "operator_control_id"

    def get_module_resource_id(self):
        return self.module.params.get("operator_control_id")

    def get_get_fn(self):
        return self.client.get_operator_control

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_control, operator_control_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_control,
            operator_control_id=self.module.params.get("operator_control_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["resource_type"]

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
            self.client.list_operator_controls, **kwargs
        )

    def get_create_model_class(self):
        return CreateOperatorControlDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_operator_control,
            call_fn_args=(),
            call_fn_kwargs=dict(create_operator_control_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateOperatorControlDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_operator_control,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operator_control_id=self.module.params.get("operator_control_id"),
                update_operator_control_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_operator_control,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operator_control_id=self.module.params.get("operator_control_id"),
                description=self.module.params.get("description"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


OperatorControlHelperCustom = get_custom_class("OperatorControlHelperCustom")


class ResourceHelper(OperatorControlHelperCustom, OperatorControlHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            resource_type=dict(
                type="str",
                choices=[
                    "EXACC",
                    "EXADATAINFRASTRUCTURE",
                    "AUTONOMOUSVMCLUSTER",
                    "CLOUDAUTONOMOUSVMCLUSTER",
                    "CCCINFRASTRUCTURE",
                ],
            ),
            compartment_id=dict(type="str"),
            operator_control_name=dict(type="str"),
            approvers_list=dict(type="list", elements="str"),
            approver_groups_list=dict(type="list", elements="str"),
            pre_approved_op_action_list=dict(type="list", elements="str"),
            is_fully_pre_approved=dict(type="bool"),
            email_id_list=dict(type="list", elements="str"),
            system_message=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            operator_control_id=dict(aliases=["id"], type="str"),
            description=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
