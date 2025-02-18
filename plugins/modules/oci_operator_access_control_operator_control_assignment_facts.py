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
module: oci_operator_access_control_operator_control_assignment_facts
short_description: Fetches details about one or multiple OperatorControlAssignment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OperatorControlAssignment resources in Oracle Cloud Infrastructure
    - Lists all Operator Control Assignments.
    - If I(operator_control_assignment_id) is specified, the details of a single OperatorControlAssignment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operator_control_assignment_id:
        description:
            - unique OperatorControl identifier
            - Required to get a specific operator_control_assignment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple operator_control_assignments.
        type: str
    operator_control_name:
        description:
            - A filter to return OperatorControl that match the given operatorControlName.
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
            - A filter to return only resources whose lifecycleState matches the given OperatorControlAssignment lifecycleState.
        type: str
        choices:
            - "CREATED"
            - "APPLIED"
            - "APPLYFAILED"
            - "UPDATING"
            - "UPDATEFAILED"
            - "DELETING"
            - "DELETED"
            - "DELETIONFAILED"
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
- name: Get a specific operator_control_assignment
  oci_operator_access_control_operator_control_assignment_facts:
    # required
    operator_control_assignment_id: "ocid1.operatorcontrolassignment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List operator_control_assignments
  oci_operator_access_control_operator_control_assignment_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    operator_control_name: operator_control_name_example
    resource_name: resource_name_example
    resource_type: resource_type_example
    lifecycle_state: CREATED
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
operator_control_assignments:
    description:
        - List of OperatorControlAssignment resources
    returned: on success
    type: complex
    contains:
        resource_name:
            description:
                - Name of the target resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: resource_name_example
        resource_compartment_id:
            description:
                - The OCID of the compartment that contains the target resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
        assigner_id:
            description:
                - The OCID of the user who created this operator control assignment.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.assigner.oc1..xxxxxxEXAMPLExxxxxx"
        comment:
            description:
                - Comment about the assignment of the operator control to this target resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: comment_example
        unassigner_id:
            description:
                - User id who released the operatorControl.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.unassigner.oc1..xxxxxxEXAMPLExxxxxx"
        time_of_deletion:
            description:
                - "Time on which the operator control assignment was deleted in L(RFC 3339,https://tools.ietf.org/html/rfc3339)timestamp format.Example:
                  '2020-05-22T21:10:29.600Z'"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        detachment_description:
            description:
                - description containing reason for releasing of OperatorControl.
                - Returned for get operation
            returned: on success
            type: str
            sample: detachment_description_example
        remote_syslog_server_ca_cert:
            description:
                - The CA certificate of the remote syslog server.
                - Returned for get operation
            returned: on success
            type: str
            sample: remote_syslog_server_ca_cert_example
        is_auto_approve_during_maintenance:
            description:
                - The boolean if true would autoApprove during maintenance.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        is_default_assignment:
            description:
                - Whether the assignment is a default assignment.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
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
        time_of_assignment:
            description:
                - "Time when the operator control assignment is created in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format. Example:
                  '2020-05-22T21:10:29.600Z'"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "resource_name": "resource_name_example",
        "resource_compartment_id": "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "assigner_id": "ocid1.assigner.oc1..xxxxxxEXAMPLExxxxxx",
        "comment": "comment_example",
        "unassigner_id": "ocid1.unassigner.oc1..xxxxxxEXAMPLExxxxxx",
        "time_of_deletion": "2013-10-20T19:20:30+01:00",
        "detachment_description": "detachment_description_example",
        "remote_syslog_server_ca_cert": "remote_syslog_server_ca_cert_example",
        "is_auto_approve_during_maintenance": true,
        "is_default_assignment": true,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "operator_control_id": "ocid1.operatorcontrol.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_type": "EXACC",
        "time_assignment_from": "2013-10-20T19:20:30+01:00",
        "time_assignment_to": "2013-10-20T19:20:30+01:00",
        "is_enforced_always": true,
        "time_of_assignment": "2013-10-20T19:20:30+01:00",
        "error_code": 56,
        "error_message": "error_message_example",
        "is_log_forwarded": true,
        "remote_syslog_server_address": "remote_syslog_server_address_example",
        "remote_syslog_server_port": 56,
        "lifecycle_state": "CREATED",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.operator_access_control import OperatorControlAssignmentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperatorControlAssignmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "operator_control_assignment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operator_control_assignment,
            operator_control_assignment_id=self.module.params.get(
                "operator_control_assignment_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "operator_control_name",
            "resource_name",
            "resource_type",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_operator_control_assignments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OperatorControlAssignmentFactsHelperCustom = get_custom_class(
    "OperatorControlAssignmentFactsHelperCustom"
)


class ResourceFactsHelper(
    OperatorControlAssignmentFactsHelperCustom, OperatorControlAssignmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            operator_control_assignment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            operator_control_name=dict(type="str"),
            resource_name=dict(type="str"),
            resource_type=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATED",
                    "APPLIED",
                    "APPLYFAILED",
                    "UPDATING",
                    "UPDATEFAILED",
                    "DELETING",
                    "DELETED",
                    "DELETIONFAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="operator_control_assignment",
        service_client_class=OperatorControlAssignmentClient,
        namespace="operator_access_control",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(operator_control_assignments=result)


if __name__ == "__main__":
    main()
