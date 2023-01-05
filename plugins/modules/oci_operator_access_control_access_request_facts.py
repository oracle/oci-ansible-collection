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
module: oci_operator_access_control_access_request_facts
short_description: Fetches details about one or multiple AccessRequest resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AccessRequest resources in Oracle Cloud Infrastructure
    - Lists all access requests in the compartment.
    - If I(access_request_id) is specified, the details of a single AccessRequest will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    access_request_id:
        description:
            - unique AccessRequest identifier
            - Required to get a specific access_request.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple access_requests.
        type: str
    resource_name:
        description:
            - A filter to return only resources that match the given ResourceName.
        type: str
    resource_type:
        description:
            - A filter to return only lists of resources that match the entire given service type.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources whose lifecycleState matches the given AccessRequest lifecycleState.
        type: str
        choices:
            - "CREATED"
            - "APPROVALWAITING"
            - "PREAPPROVED"
            - "APPROVED"
            - "MOREINFO"
            - "REJECTED"
            - "DEPLOYED"
            - "DEPLOYFAILED"
            - "UNDEPLOYED"
            - "UNDEPLOYFAILED"
            - "CLOSEFAILED"
            - "REVOKEFAILED"
            - "EXPIRYFAILED"
            - "REVOKING"
            - "REVOKED"
            - "EXTENDING"
            - "EXTENDED"
            - "EXTENSIONREJECTED"
            - "COMPLETING"
            - "COMPLETED"
            - "EXPIRED"
            - "APPROVEDFORFUTURE"
            - "INREVIEW"
    time_start:
        description:
            - Query start time in UTC in ISO 8601 format(inclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              timeIntervalStart and timeIntervalEnd parameters are used together.
        type: str
    time_end:
        description:
            - Query start time in UTC in ISO 8601 format(inclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              timeIntervalStart and timeIntervalEnd parameters are used together.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific access_request
  oci_operator_access_control_access_request_facts:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"

- name: List access_requests
  oci_operator_access_control_access_request_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    resource_name: resource_name_example
    resource_type: resource_type_example
    lifecycle_state: CREATED
    time_start: 2013-10-20T19:20:30+01:00
    time_end: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
access_requests:
    description:
        - List of AccessRequest resources
    returned: on success
    type: complex
    contains:
        operator_id:
            description:
                - A unique identifier associated with the operator who raised the request. This identifier can not be used directly to identify the operator.
                  You need to provide this identifier if you would like Oracle to provide additional information about the operator action within Oracle
                  tenancy.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.operator.oc1..xxxxxxEXAMPLExxxxxx"
        action_requests_list:
            description:
                - List of operator actions for which approval is sought by the operator user.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        reason:
            description:
                - Summary reason for which the operator is requesting access on the target resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: reason_example
        workflow_id:
            description:
                - The OCID of the workflow associated with the access request. This is needed if you want to contact Oracle Support for a stuck access request
                  or for an access request that encounters an internal error.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        user_id:
            description:
                - The OCID of the user that last modified the access request.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        approver_comment:
            description:
                - The last recent Comment entered by the approver of the request.
                - Returned for get operation
            returned: on success
            type: str
            sample: approver_comment_example
        closure_comment:
            description:
                - The comment entered by the operator while closing the request.
                - Returned for get operation
            returned: on success
            type: str
            sample: closure_comment_example
        opctl_id:
            description:
                - The OCID of the operator control governing the target resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.opctl.oc1..xxxxxxEXAMPLExxxxxx"
        opctl_name:
            description:
                - Name of the Operator control governing the target resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: opctl_name_example
        system_message:
            description:
                - System message that will be displayed to the operator at login to the target resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: system_message_example
        opctl_additional_message:
            description:
                - Additional message specific to the access request that can be specified by the approver at the time of approval.
                - Returned for get operation
            returned: on success
            type: str
            sample: opctl_additional_message_example
        audit_type:
            description:
                - "Specifies the type of auditing to be enabled. There are two levels of auditing: command-level and keystroke-level.
                  By default, auditing is enabled at the command level i.e., each command issued by the operator is audited. When keystroke-level is chosen,
                  in addition to command level logging, key strokes are also logged."
                - Returned for get operation
            returned: on success
            type: list
            sample: []
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
        compartment_id:
            description:
                - The OCID of the compartment that contains the access request.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        resource_type:
            description:
                - resourceType for which the AccessRequest is applicable
            returned: on success
            type: str
            sample: EXACC
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
        severity:
            description:
                - Priority assigned to the access request by the operator
            returned: on success
            type: str
            sample: S1
        is_auto_approved:
            description:
                - Whether the access request was automatically approved.
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
    sample: [{
        "operator_id": "ocid1.operator.oc1..xxxxxxEXAMPLExxxxxx",
        "action_requests_list": [],
        "reason": "reason_example",
        "workflow_id": [],
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "approver_comment": "approver_comment_example",
        "closure_comment": "closure_comment_example",
        "opctl_id": "ocid1.opctl.oc1..xxxxxxEXAMPLExxxxxx",
        "opctl_name": "opctl_name_example",
        "system_message": "system_message_example",
        "opctl_additional_message": "opctl_additional_message_example",
        "audit_type": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "request_id": "ocid1.request.oc1..xxxxxxEXAMPLExxxxxx",
        "access_reason_summary": "access_reason_summary_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_name": "resource_name_example",
        "resource_type": "EXACC",
        "lifecycle_state": "CREATED",
        "lifecycle_details": "lifecycle_details_example",
        "time_of_creation": "2013-10-20T19:20:30+01:00",
        "time_of_modification": "2013-10-20T19:20:30+01:00",
        "time_of_user_creation": "2013-10-20T19:20:30+01:00",
        "duration": 56,
        "extend_duration": 56,
        "severity": "S1",
        "is_auto_approved": true,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.operator_access_control import AccessRequestsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessRequestFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "access_request_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_request,
            access_request_id=self.module.params.get("access_request_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "resource_name",
            "resource_type",
            "lifecycle_state",
            "time_start",
            "time_end",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_access_requests,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AccessRequestFactsHelperCustom = get_custom_class("AccessRequestFactsHelperCustom")


class ResourceFactsHelper(AccessRequestFactsHelperCustom, AccessRequestFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            access_request_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            resource_name=dict(type="str"),
            resource_type=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATED",
                    "APPROVALWAITING",
                    "PREAPPROVED",
                    "APPROVED",
                    "MOREINFO",
                    "REJECTED",
                    "DEPLOYED",
                    "DEPLOYFAILED",
                    "UNDEPLOYED",
                    "UNDEPLOYFAILED",
                    "CLOSEFAILED",
                    "REVOKEFAILED",
                    "EXPIRYFAILED",
                    "REVOKING",
                    "REVOKED",
                    "EXTENDING",
                    "EXTENDED",
                    "EXTENSIONREJECTED",
                    "COMPLETING",
                    "COMPLETED",
                    "EXPIRED",
                    "APPROVEDFORFUTURE",
                    "INREVIEW",
                ],
            ),
            time_start=dict(type="str"),
            time_end=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="access_request",
        service_client_class=AccessRequestsClient,
        namespace="operator_access_control",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(access_requests=result)


if __name__ == "__main__":
    main()
