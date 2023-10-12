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
module: oci_operator_access_control_operator_control_assignment_actions
short_description: Perform actions on an OperatorControlAssignment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OperatorControlAssignment resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), changes the compartment of the specified Operator Control assignment ID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operator_control_assignment_id:
        description:
            - unique OperatorControl identifier
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the new compartment to contain the operator contol assignment.
        type: str
    action:
        description:
            - The action to perform on the OperatorControlAssignment.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on operator_control_assignment
  oci_operator_access_control_operator_control_assignment_actions:
    # required
    operator_control_assignment_id: "ocid1.operatorcontrolassignment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.operator_access_control import OperatorControlAssignmentClient
    from oci.operator_access_control.models import (
        ChangeOperatorControlAssignmentCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperatorControlAssignmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "operator_control_assignment_id"

    def get_module_resource_id(self):
        return self.module.params.get("operator_control_assignment_id")

    def get_get_fn(self):
        return self.client.get_operator_control_assignment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_control_assignment,
            operator_control_assignment_id=self.module.params.get(
                "operator_control_assignment_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeOperatorControlAssignmentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_operator_control_assignment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                operator_control_assignment_id=self.module.params.get(
                    "operator_control_assignment_id"
                ),
                change_operator_control_assignment_compartment_details=action_details,
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


OperatorControlAssignmentActionsHelperCustom = get_custom_class(
    "OperatorControlAssignmentActionsHelperCustom"
)


class ResourceHelper(
    OperatorControlAssignmentActionsHelperCustom,
    OperatorControlAssignmentActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            operator_control_assignment_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
