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
module: oci_golden_gate_connection_assignment
short_description: Manage a ConnectionAssignment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a ConnectionAssignment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Connection Assignment.
    - "This resource has the following action operations in the M(oracle.oci.oci_golden_gate_connection_assignment_actions) module: test."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection being
              referenced.
            - Required for create using I(state=present).
        type: str
    deployment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            - Required for create using I(state=present).
        type: str
    connection_assignment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Connection Assignment.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    is_lock_override:
        description:
            - Whether to override locks (if any exist).
        type: bool
    compartment_id:
        description:
            - The OCID of the compartment that contains the work request. Work requests should be scoped
              to the same compartment as the resource the work request affects. If the work request concerns
              multiple resources, and those resources are not in the same compartment, it is up to the service team
              to pick the primary resource whose compartment should be used.
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the ConnectionAssignment.
            - Use I(state=present) to create a ConnectionAssignment.
            - Use I(state=absent) to delete a ConnectionAssignment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create connection_assignment
  oci_golden_gate_connection_assignment:
    # required
    connection_id: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_lock_override: true

- name: Delete connection_assignment
  oci_golden_gate_connection_assignment:
    # required
    connection_assignment_id: "ocid1.connectionassignment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    is_lock_override: true

"""

RETURN = """
connection_assignment:
    description:
        - Details of the ConnectionAssignment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection assignment being
                  referenced.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        connection_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the connection being
                  referenced.
            returned: on success
            type: str
            sample: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the deployment being referenced.
            returned: on success
            type: str
            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        alias_name:
            description:
                - Credential store alias.
            returned: on success
            type: str
            sample: alias_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment being referenced.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Possible lifecycle states for connection assignments.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The time the resource was created. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the resource was last updated. The format is defined by
                  L(RFC3339,https://tools.ietf.org/html/rfc3339), such as `2016-08-25T21:10:29.600Z`.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "connection_id": "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
        "alias_name": "alias_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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
    from oci.golden_gate import GoldenGateClient
    from oci.golden_gate.models import CreateConnectionAssignmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionAssignmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            ConnectionAssignmentHelperGen, self
        ).get_possible_entity_types() + [
            "connectionassignment",
            "connectionassignments",
            "goldenGateconnectionassignment",
            "goldenGateconnectionassignments",
            "connectionassignmentresource",
            "connectionassignmentsresource",
            "goldengate",
        ]

    def get_module_resource_id_param(self):
        return "connection_assignment_id"

    def get_module_resource_id(self):
        return self.module.params.get("connection_assignment_id")

    def get_get_fn(self):
        return self.client.get_connection_assignment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection_assignment,
            connection_assignment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection_assignment,
            connection_assignment_id=self.module.params.get("connection_assignment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["deployment_id", "connection_id"]

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
            self.client.list_connection_assignments, **kwargs
        )

    def get_create_model_class(self):
        return CreateConnectionAssignmentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_connection_assignment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_connection_assignment_details=create_details,
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_connection_assignment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                connection_assignment_id=self.module.params.get(
                    "connection_assignment_id"
                ),
                is_lock_override=self.module.params.get("is_lock_override"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ConnectionAssignmentHelperCustom = get_custom_class("ConnectionAssignmentHelperCustom")


class ResourceHelper(ConnectionAssignmentHelperCustom, ConnectionAssignmentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            connection_id=dict(type="str"),
            deployment_id=dict(type="str"),
            connection_assignment_id=dict(aliases=["id"], type="str"),
            is_lock_override=dict(type="bool"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
