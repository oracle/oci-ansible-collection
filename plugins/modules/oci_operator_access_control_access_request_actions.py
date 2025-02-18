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
module: oci_operator_access_control_access_request_actions
short_description: Perform actions on an AccessRequest resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AccessRequest resource in Oracle Cloud Infrastructure
    - For I(action=approve), approves an access request.
    - For I(action=interaction_request), posts query for additional information for the given access request.
    - For I(action=reject), rejects an access request.
    - For I(action=review), reviews the access request.
    - For I(action=revoke), revokes an already approved access request.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    audit_type:
        description:
            - "Specifies the type of auditing to be enabled. There are two levels of auditing: command-level and keystroke-level.
              By default, auditing is enabled at the command level i.e., each command issued by the operator is audited. When keystroke-level is chosen,
              in addition to command level logging, key strokes are also logged."
            - Applicable only for I(action=approve).
        type: list
        elements: str
    additional_message:
        description:
            - Message that needs to be displayed to the Ops User.
            - Applicable only for I(action=approve).
        type: str
    time_of_user_creation:
        description:
            - "The time when access request is scheduled to be approved in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.Example:
              '2020-05-22T21:10:29.600Z'"
            - Applicable only for I(action=approve).
        type: str
    more_info_details:
        description:
            - questions for asking to provide more information to operators.
            - Applicable only for I(action=interaction_request).
        type: str
    access_request_id:
        description:
            - unique AccessRequest identifier
        type: str
        aliases: ["id"]
        required: true
    approver_comment:
        description:
            - Comment by the approver during approval.
            - Applicable only for I(action=approve)I(action=reject)I(action=review)I(action=revoke).
        type: str
    action:
        description:
            - The action to perform on the AccessRequest.
        type: str
        required: true
        choices:
            - "approve"
            - "interaction_request"
            - "reject"
            - "review"
            - "revoke"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action approve on access_request
  oci_operator_access_control_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: approve

    # optional
    audit_type: [ "audit_type_example" ]
    additional_message: additional_message_example
    time_of_user_creation: time_of_user_creation_example
    approver_comment: approver_comment_example

- name: Perform action interaction_request on access_request
  oci_operator_access_control_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: interaction_request

    # optional
    more_info_details: more_info_details_example

- name: Perform action reject on access_request
  oci_operator_access_control_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: reject

    # optional
    approver_comment: approver_comment_example

- name: Perform action review on access_request
  oci_operator_access_control_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: review

    # optional
    approver_comment: approver_comment_example

- name: Perform action revoke on access_request
  oci_operator_access_control_access_request_actions:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"
    action: revoke

    # optional
    approver_comment: approver_comment_example

"""

RETURN = """
access_request:
    description:
        - Details of the AccessRequest resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the access request.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        request_id:
            description:
                - This is an automatic identifier generated by the system which is easier for human comprehension.
            returned: on success
            type: str
            sample: "ocid1.request.oc1..xxxxxxEXAMPLExxxxxx"
        access_reason_summary:
            description:
                - Summary comment by the operator creating the access request.
            returned: on success
            type: str
            sample: access_reason_summary_example
        operator_id:
            description:
                - A unique identifier associated with the operator who raised the request. This identifier can not be used directly to identify the operator.
                  You need to provide this identifier if you would like Oracle to provide additional information about the operator action within Oracle
                  tenancy.
            returned: on success
            type: str
            sample: "ocid1.operator.oc1..xxxxxxEXAMPLExxxxxx"
        resource_id:
            description:
                - The OCID of the target resource associated with the access request. The operator raises an access request to get approval to
                  access the target resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        resource_name:
            description:
                - The name of the target resource.
            returned: on success
            type: str
            sample: resource_name_example
        sub_resource_list:
            description:
                - The subresources requested for approval.
            returned: on success
            type: list
            sample: []
        compartment_id:
            description:
                - The OCID of the compartment that contains the access request.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        resource_type:
            description:
                - resourceType for which the AccessRequest is applicable
            returned: on success
            type: str
            sample: EXACC
        action_requests_list:
            description:
                - List of operator actions for which approval is sought by the operator user.
            returned: on success
            type: list
            sample: []
        reason:
            description:
                - Summary reason for which the operator is requesting access on the target resource.
            returned: on success
            type: str
            sample: reason_example
        severity:
            description:
                - Priority assigned to the access request by the operator
            returned: on success
            type: str
            sample: S1
        duration:
            description:
                - Duration in hours for which access is sought on the target resource.
            returned: on success
            type: int
            sample: 56
        extend_duration:
            description:
                - Duration in hours for which extension access is sought on the target resource.
            returned: on success
            type: int
            sample: 56
        workflow_id:
            description:
                - The OCID of the workflow associated with the access request. This is needed if you want to contact Oracle Support for a stuck access request
                  or for an access request that encounters an internal error.
            returned: on success
            type: list
            sample: []
        is_auto_approved:
            description:
                - Whether the access request was automatically approved.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of the AccessRequest.
            returned: on success
            type: str
            sample: CREATED
        lifecycle_details:
            description:
                - more in detail about the lifeCycleState.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_of_creation:
            description:
                - "Time when the access request was created in L(RFC 3339,https://tools.ietf.org/html/rfc3339)timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_modification:
            description:
                - "Time when the access request was last modified in L(RFC 3339,https://tools.ietf.org/html/rfc3339)timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_user_creation:
            description:
                - "The time when access request is scheduled to be approved in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        user_id:
            description:
                - The OCID of the user that last modified the access request.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        approver_comment:
            description:
                - The last recent Comment entered by the approver of the request.
            returned: on success
            type: str
            sample: approver_comment_example
        closure_comment:
            description:
                - The comment entered by the operator while closing the request.
            returned: on success
            type: str
            sample: closure_comment_example
        opctl_id:
            description:
                - The OCID of the operator control governing the target resource.
            returned: on success
            type: str
            sample: "ocid1.opctl.oc1..xxxxxxEXAMPLExxxxxx"
        opctl_name:
            description:
                - Name of the Operator control governing the target resource.
            returned: on success
            type: str
            sample: opctl_name_example
        system_message:
            description:
                - System message that will be displayed to the operator at login to the target resource.
            returned: on success
            type: str
            sample: system_message_example
        opctl_additional_message:
            description:
                - Additional message specific to the access request that can be specified by the approver at the time of approval.
            returned: on success
            type: str
            sample: opctl_additional_message_example
        audit_type:
            description:
                - "Specifies the type of auditing to be enabled. There are two levels of auditing: command-level and keystroke-level.
                  By default, auditing is enabled at the command level i.e., each command issued by the operator is audited. When keystroke-level is chosen,
                  in addition to command level logging, key strokes are also logged."
            returned: on success
            type: list
            sample: []
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
        "request_id": "ocid1.request.oc1..xxxxxxEXAMPLExxxxxx",
        "access_reason_summary": "access_reason_summary_example",
        "operator_id": "ocid1.operator.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_name": "resource_name_example",
        "sub_resource_list": [],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_type": "EXACC",
        "action_requests_list": [],
        "reason": "reason_example",
        "severity": "S1",
        "duration": 56,
        "extend_duration": 56,
        "workflow_id": [],
        "is_auto_approved": true,
        "lifecycle_state": "CREATED",
        "lifecycle_details": "lifecycle_details_example",
        "time_of_creation": "2013-10-20T19:20:30+01:00",
        "time_of_modification": "2013-10-20T19:20:30+01:00",
        "time_of_user_creation": "2013-10-20T19:20:30+01:00",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "approver_comment": "approver_comment_example",
        "closure_comment": "closure_comment_example",
        "opctl_id": "ocid1.opctl.oc1..xxxxxxEXAMPLExxxxxx",
        "opctl_name": "opctl_name_example",
        "system_message": "system_message_example",
        "opctl_additional_message": "opctl_additional_message_example",
        "audit_type": [],
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
    from oci.operator_access_control import AccessRequestsClient
    from oci.operator_access_control.models import ApproveAccessRequestDetails
    from oci.operator_access_control.models import InteractionRequestDetails
    from oci.operator_access_control.models import RejectAccessRequestDetails
    from oci.operator_access_control.models import ReviewAccessRequestDetails
    from oci.operator_access_control.models import RevokeAccessRequestDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRequestActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        approve
        interaction_request
        reject
        review
        revoke
    """

    @staticmethod
    def get_module_resource_id_param():
        return "access_request_id"

    def get_module_resource_id(self):
        return self.module.params.get("access_request_id")

    def get_get_fn(self):
        return self.client.get_access_request

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_request,
            access_request_id=self.module.params.get("access_request_id"),
        )

    def approve(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ApproveAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.approve_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                approve_access_request_details=action_details,
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

    def interaction_request(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InteractionRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.interaction_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                interaction_request_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def reject(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RejectAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reject_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                reject_access_request_details=action_details,
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

    def review(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ReviewAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.review_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                review_access_request_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def revoke(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RevokeAccessRequestDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.revoke_access_request,
            call_fn_args=(),
            call_fn_kwargs=dict(
                access_request_id=self.module.params.get("access_request_id"),
                revoke_access_request_details=action_details,
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


AccessRequestActionsHelperCustom = get_custom_class("AccessRequestActionsHelperCustom")


class ResourceHelper(AccessRequestActionsHelperCustom, AccessRequestActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            audit_type=dict(type="list", elements="str"),
            additional_message=dict(type="str"),
            time_of_user_creation=dict(type="str"),
            more_info_details=dict(type="str"),
            access_request_id=dict(aliases=["id"], type="str", required=True),
            approver_comment=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "approve",
                    "interaction_request",
                    "reject",
                    "review",
                    "revoke",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="access_request",
        service_client_class=AccessRequestsClient,
        namespace="operator_access_control",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
