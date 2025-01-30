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
module: oci_golden_gate_connection_assignment_actions
short_description: Perform actions on a ConnectionAssignment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ConnectionAssignment resource in Oracle Cloud Infrastructure
    - For I(action=test), tests the connectivity between given GoldenGate deployment and one of the associated database / service.
      When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_assignment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Connection Assignment.
        type: str
        aliases: ["id"]
        required: true
    type:
        description:
            - The type of the test of the assigned connection.
        type: str
        choices:
            - "DEFAULT"
        required: true
    action:
        description:
            - The action to perform on the ConnectionAssignment.
        type: str
        required: true
        choices:
            - "test"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action test on connection_assignment with type = DEFAULT
  oci_golden_gate_connection_assignment_actions:
    # required
    type: DEFAULT

"""

RETURN = """
test_connection_assignment_result:
    description:
        - Details of the ConnectionAssignment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        result_type:
            description:
                - Type of the result (i.e. Success, Failure or Timeout).
            returned: on success
            type: str
            sample: SUCCEEDED
        error:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                code:
                    description:
                        - A short error code that defines the error, meant for programmatic parsing.
                    returned: on success
                    type: str
                    sample: code_example
                message:
                    description:
                        - A human-readable error string.
                    returned: on success
                    type: str
                    sample: message_example
                issue:
                    description:
                        - The text describing the root cause of the reported issue.
                    returned: on success
                    type: str
                    sample: issue_example
                action:
                    description:
                        - The text describing the action required to fix the issue.
                    returned: on success
                    type: str
                    sample: action_example
    sample: {
        "result_type": "SUCCEEDED",
        "error": {
            "code": "code_example",
            "message": "message_example",
            "issue": "issue_example",
            "action": "action_example"
        }
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import TestConnectionAssignmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionAssignmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        test
    """

    @staticmethod
    def get_module_resource_id_param():
        return "connection_assignment_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_assignment_id")

    def get_get_fn(self):
        return self.client.get_connection_assignment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection_assignment,
            connection_assignment_id=self.module.params.get("connection_assignment_id"),
        )

    def get_response_field_name(self, action):
        response_fields = dict(test="test_connection_assignment_result",)
        return response_fields.get(action, "connection_assignment")

    def test(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, TestConnectionAssignmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.test_connection_assignment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_assignment_id=self.module.params.get(
                    "connection_assignment_id"
                ),
                test_connection_assignment_details=action_details,
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


ConnectionAssignmentActionsHelperCustom = get_custom_class(
    "ConnectionAssignmentActionsHelperCustom"
)


class ResourceHelper(
    ConnectionAssignmentActionsHelperCustom, ConnectionAssignmentActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            connection_assignment_id=dict(aliases=["id"], type="str", required=True),
            type=dict(type="str", required=True, choices=["DEFAULT"]),
            action=dict(type="str", required=True, choices=["test"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection_assignment",
        service_client_class=GoldenGateClient,
        namespace="golden_gate",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
