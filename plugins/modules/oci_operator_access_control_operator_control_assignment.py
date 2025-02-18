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
module: oci_operator_access_control_operator_control_assignment
short_description: Manage an OperatorControlAssignment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OperatorControlAssignment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an Operator Control Assignment resource. In effect, this brings the target resource under the governance of the Operator
      Control for specified time duration.
    - "This resource has the following action operations in the M(oracle.oci.oci_operator_access_control_operator_control_assignment_actions) module:
      change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operator_control_id:
        description:
            - The OCID of the operator control that is being assigned to a target resource.
            - Required for create using I(state=present).
        type: str
    resource_id:
        description:
            - The OCID of the target resource being brought under the governance of the operator control.
            - Required for create using I(state=present).
        type: str
    resource_name:
        description:
            - Name of the target resource.
            - Required for create using I(state=present).
        type: str
    resource_type:
        description:
            - Type of the target resource.
            - Required for create using I(state=present).
        type: str
        choices:
            - "EXACC"
            - "EXADATAINFRASTRUCTURE"
            - "AUTONOMOUSVMCLUSTER"
            - "CLOUDAUTONOMOUSVMCLUSTER"
            - "CCCINFRASTRUCTURE"
    resource_compartment_id:
        description:
            - The OCID of the compartment that contains the target resource.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that contains the operator control assignment.
            - Required for create using I(state=present).
        type: str
    time_assignment_from:
        description:
            - "The time at which the target resource will be brought under the governance of the operator control in L(RFC
              3339,https://tools.ietf.org/html/rfc3339) timestamp format. Example: '2020-05-22T21:10:29.600Z'"
            - This parameter is updatable.
        type: str
    time_assignment_to:
        description:
            - "The time at which the target resource will leave the governance of the operator control in L(RFC
              3339,https://tools.ietf.org/html/rfc3339)timestamp format.Example: '2020-05-22T21:10:29.600Z'"
            - This parameter is updatable.
        type: str
    is_enforced_always:
        description:
            - If set, then the target resource is always governed by the operator control.
            - Required for create using I(state=present), update using I(state=present) with operator_control_assignment_id present.
        type: bool
    comment:
        description:
            - Comment about the assignment of the operator control to this target resource.
            - This parameter is updatable.
        type: str
    is_log_forwarded:
        description:
            - If set, then the audit logs will be forwarded to the relevant remote logging server
            - This parameter is updatable.
        type: bool
    remote_syslog_server_address:
        description:
            - The address of the remote syslog server where the audit logs will be forwarded to. Address in host or IP format.
            - This parameter is updatable.
        type: str
    remote_syslog_server_port:
        description:
            - "The listening port of the remote syslog server. The port range is 0 - 65535. Only TCP supported."
            - This parameter is updatable.
        type: int
    remote_syslog_server_ca_cert:
        description:
            - The CA certificate of the remote syslog server. Identity of the remote syslog server will be asserted based on this certificate.
            - This parameter is updatable.
        type: str
    is_auto_approve_during_maintenance:
        description:
            - The boolean if true would autoApprove during maintenance.
            - This parameter is updatable.
        type: bool
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
    operator_control_assignment_id:
        description:
            - unique OperatorControl identifier
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    description:
        description:
            - reason for detachment of OperatorAssignment.
        type: str
    state:
        description:
            - The state of the OperatorControlAssignment.
            - Use I(state=present) to create or update an OperatorControlAssignment.
            - Use I(state=absent) to delete an OperatorControlAssignment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create operator_control_assignment
  oci_operator_access_control_operator_control_assignment:
    # required
    operator_control_id: "ocid1.operatorcontrol.oc1..xxxxxxEXAMPLExxxxxx"
    resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    resource_name: resource_name_example
    resource_type: EXACC
    resource_compartment_id: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_enforced_always: true

    # optional
    time_assignment_from: time_assignment_from_example
    time_assignment_to: time_assignment_to_example
    comment: comment_example
    is_log_forwarded: true
    remote_syslog_server_address: remote_syslog_server_address_example
    remote_syslog_server_port: 56
    remote_syslog_server_ca_cert: remote_syslog_server_ca_cert_example
    is_auto_approve_during_maintenance: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update operator_control_assignment
  oci_operator_access_control_operator_control_assignment:
    # required
    is_enforced_always: true
    operator_control_assignment_id: "ocid1.operatorcontrolassignment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_assignment_from: time_assignment_from_example
    time_assignment_to: time_assignment_to_example
    comment: comment_example
    is_log_forwarded: true
    remote_syslog_server_address: remote_syslog_server_address_example
    remote_syslog_server_port: 56
    remote_syslog_server_ca_cert: remote_syslog_server_ca_cert_example
    is_auto_approve_during_maintenance: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete operator_control_assignment
  oci_operator_access_control_operator_control_assignment:
    # required
    operator_control_assignment_id: "ocid1.operatorcontrolassignment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    description: description_example

"""

RETURN = """
operator_control_assignment:
    description:
        - Details of the OperatorControlAssignment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the operator control assignment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        operator_control_id:
            description:
                - The OCID of the operator control.
            returned: on success
            type: str
            sample: "ocid1.operatorcontrol.oc1..xxxxxxEXAMPLExxxxxx"
        resource_id:
            description:
                - The OCID of the target resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        resource_name:
            description:
                - Name of the target resource.
            returned: on success
            type: str
            sample: resource_name_example
        resource_compartment_id:
            description:
                - The OCID of the compartment that contains the target resource.
            returned: on success
            type: str
            sample: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the comparment that contains the operator control assignment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        resource_type:
            description:
                - resourceType for which the OperatorControlAssignment is applicable
            returned: on success
            type: str
            sample: EXACC
        time_assignment_from:
            description:
                - "The time at which the target resource will be brought under the governance of the operator control expressed in L(RFC
                  3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_assignment_to:
            description:
                - "The time at which the target resource will leave the governance of the operator control expressed in L(RFC
                  3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_enforced_always:
            description:
                - If set, then the target resource is always governed by the operator control.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current lifcycle state of the OperatorControl.
            returned: on success
            type: str
            sample: CREATED
        lifecycle_details:
            description:
                - More in detail about the lifeCycleState.
            returned: on success
            type: str
            sample: lifecycle_details_example
        assigner_id:
            description:
                - The OCID of the user who created this operator control assignment.
            returned: on success
            type: str
            sample: "ocid1.assigner.oc1..xxxxxxEXAMPLExxxxxx"
        time_of_assignment:
            description:
                - "Time when the operator control assignment is created in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        comment:
            description:
                - Comment about the assignment of the operator control to this target resource.
            returned: on success
            type: str
            sample: comment_example
        unassigner_id:
            description:
                - User id who released the operatorControl.
            returned: on success
            type: str
            sample: "ocid1.unassigner.oc1..xxxxxxEXAMPLExxxxxx"
        time_of_deletion:
            description:
                - "Time on which the operator control assignment was deleted in L(RFC 3339,https://tools.ietf.org/html/rfc3339)timestamp format.Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        detachment_description:
            description:
                - description containing reason for releasing of OperatorControl.
            returned: on success
            type: str
            sample: detachment_description_example
        is_log_forwarded:
            description:
                - If set indicates that the audit logs are being forwarded to the relevant remote logging server
            returned: on success
            type: bool
            sample: true
        remote_syslog_server_address:
            description:
                - The address of the remote syslog server where the audit logs are being forwarded to. Address in host or IP format.
            returned: on success
            type: str
            sample: remote_syslog_server_address_example
        remote_syslog_server_port:
            description:
                - "The listening port of the remote syslog server. The port range is 0 - 65535. Only TCP supported."
            returned: on success
            type: int
            sample: 56
        remote_syslog_server_ca_cert:
            description:
                - The CA certificate of the remote syslog server.
            returned: on success
            type: str
            sample: remote_syslog_server_ca_cert_example
        is_auto_approve_during_maintenance:
            description:
                - The boolean if true would autoApprove during maintenance.
            returned: on success
            type: bool
            sample: true
        error_code:
            description:
                - The code identifying the error occurred during Assignment operation.
            returned: on success
            type: int
            sample: 56
        error_message:
            description:
                - The message describing the error occurred during Assignment operation.
            returned: on success
            type: str
            sample: error_message_example
        is_default_assignment:
            description:
                - Whether the assignment is a default assignment.
            returned: on success
            type: bool
            sample: true
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
        "operator_control_id": "ocid1.operatorcontrol.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_name": "resource_name_example",
        "resource_compartment_id": "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_type": "EXACC",
        "time_assignment_from": "2013-10-20T19:20:30+01:00",
        "time_assignment_to": "2013-10-20T19:20:30+01:00",
        "is_enforced_always": true,
        "lifecycle_state": "CREATED",
        "lifecycle_details": "lifecycle_details_example",
        "assigner_id": "ocid1.assigner.oc1..xxxxxxEXAMPLExxxxxx",
        "time_of_assignment": "2013-10-20T19:20:30+01:00",
        "comment": "comment_example",
        "unassigner_id": "ocid1.unassigner.oc1..xxxxxxEXAMPLExxxxxx",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "detachment_description": "detachment_description_example",
        "is_log_forwarded": true,
        "remote_syslog_server_address": "remote_syslog_server_address_example",
        "remote_syslog_server_port": 56,
        "remote_syslog_server_ca_cert": "remote_syslog_server_ca_cert_example",
        "is_auto_approve_during_maintenance": true,
        "error_code": 56,
        "error_message": "error_message_example",
        "is_default_assignment": true,
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
    from oci.operator_access_control import OperatorControlAssignmentClient
    from oci.operator_access_control.models import (
        CreateOperatorControlAssignmentDetails,
    )
    from oci.operator_access_control.models import (
        UpdateOperatorControlAssignmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperatorControlAssignmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            OperatorControlAssignmentHelperGen, self
        ).get_possible_entity_types() + [
            "operatorcontrolassignment",
            "operatorcontrolassignments",
            "operatorAccessControloperatorcontrolassignment",
            "operatorAccessControloperatorcontrolassignments",
            "operatorcontrolassignmentresource",
            "operatorcontrolassignmentsresource",
            "operatoraccesscontrol",
        ]

    def get_module_resource_id_param(self):
        return "operator_control_assignment_id"

    def get_module_resource_id(self):
        return self.module.params.get("operator_control_assignment_id")

    def get_get_fn(self):
        return self.client.get_operator_control_assignment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_control_assignment,
            operator_control_assignment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_control_assignment,
            operator_control_assignment_id=self.module.params.get(
                "operator_control_assignment_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["resource_name", "resource_type"]

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
            self.client.list_operator_control_assignments, **kwargs
        )

    def get_create_model_class(self):
        return CreateOperatorControlAssignmentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_operator_control_assignment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_operator_control_assignment_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateOperatorControlAssignmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_operator_control_assignment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operator_control_assignment_id=self.module.params.get(
                    "operator_control_assignment_id"
                ),
                update_operator_control_assignment_details=update_details,
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
            call_fn=self.client.delete_operator_control_assignment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operator_control_assignment_id=self.module.params.get(
                    "operator_control_assignment_id"
                ),
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


OperatorControlAssignmentHelperCustom = get_custom_class(
    "OperatorControlAssignmentHelperCustom"
)


class ResourceHelper(
    OperatorControlAssignmentHelperCustom, OperatorControlAssignmentHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            operator_control_id=dict(type="str"),
            resource_id=dict(type="str"),
            resource_name=dict(type="str"),
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
            resource_compartment_id=dict(type="str"),
            compartment_id=dict(type="str"),
            time_assignment_from=dict(type="str"),
            time_assignment_to=dict(type="str"),
            is_enforced_always=dict(type="bool"),
            comment=dict(type="str"),
            is_log_forwarded=dict(type="bool"),
            remote_syslog_server_address=dict(type="str"),
            remote_syslog_server_port=dict(type="int"),
            remote_syslog_server_ca_cert=dict(type="str"),
            is_auto_approve_during_maintenance=dict(type="bool"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            operator_control_assignment_id=dict(aliases=["id"], type="str"),
            description=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="operator_control_assignment",
        service_client_class=OperatorControlAssignmentClient,
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
