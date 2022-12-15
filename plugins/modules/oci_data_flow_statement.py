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
module: oci_data_flow_statement
short_description: Manage a Statement resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a Statement resource in Oracle Cloud Infrastructure
    - For I(state=present), executes a statement for a Session run.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    code:
        description:
            - "The statement code to execute.
              Example: `println(sc.version)`"
            - Required for create using I(state=present).
        type: str
    run_id:
        description:
            - The unique ID for the run
        type: str
        required: true
    statement_id:
        description:
            - The unique ID for the statement.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Statement.
            - Use I(state=present) to create a Statement.
            - Use I(state=absent) to delete a Statement.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create statement
  oci_data_flow_statement:
    # required
    code: code_example
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete statement
  oci_data_flow_statement:
    # required
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"
    statement_id: "ocid1.statement.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
statement:
    description:
        - Details of the Statement resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The statement ID.
            returned: on success
            type: int
            sample: 56
        code:
            description:
                - "The statement code to execute.
                  Example: `println(sc.version)`"
            returned: on success
            type: str
            sample: code_example
        lifecycle_state:
            description:
                - The current state of this statement.
            returned: on success
            type: str
            sample: ACCEPTED
        output:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                data:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - The type of the `StatementOutputData` like `TEXT_PLAIN`, `TEXT_HTML` or `IMAGE_PNG`.
                            returned: on success
                            type: str
                            sample: TEXT_PLAIN
                        value:
                            description:
                                - The statement code execution output in png format.
                            returned: on success
                            type: str
                            sample: "null"

                status:
                    description:
                        - Status of the statement output.
                    returned: on success
                    type: str
                    sample: OK
                error_name:
                    description:
                        - The name of the error in the statement output.
                    returned: on success
                    type: str
                    sample: error_name_example
                error_value:
                    description:
                        - The value of the error in the statement output.
                    returned: on success
                    type: str
                    sample: error_value_example
                traceback:
                    description:
                        - The traceback of the statement output.
                    returned: on success
                    type: list
                    sample: []
        progress:
            description:
                - The execution progress.
            returned: on success
            type: float
            sample: 1.2
        run_id:
            description:
                - The ID of a run.
            returned: on success
            type: str
            sample: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time a application was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_completed:
            description:
                - "The date and time a statement execution was completed, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2022-05-31T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": 56,
        "code": "code_example",
        "lifecycle_state": "ACCEPTED",
        "output": {
            "data": {
                "type": "TEXT_PLAIN",
                "value": null
            },
            "status": "OK",
            "error_name": "error_name_example",
            "error_value": "error_value_example",
            "traceback": []
        },
        "progress": 1.2,
        "run_id": "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_completed": "2013-10-20T19:20:30+01:00"
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
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import CreateStatementDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowStatementHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DataFlowStatementHelperGen, self).get_possible_entity_types() + [
            "dataflowrun",
            "dataflowruns",
            "dataFlowdataflowrun",
            "dataFlowdataflowruns",
            "dataflowrunresource",
            "dataflowrunsresource",
            "statement",
            "statements",
            "dataFlowstatement",
            "dataFlowstatements",
            "statementresource",
            "statementsresource",
            "dataflow",
        ]

    def get_module_resource_id_param(self):
        return "statement_id"

    def get_module_resource_id(self):
        return self.module.params.get("statement_id")

    def get_get_fn(self):
        return self.client.get_statement

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_statement,
            statement_id=summary_model.id,
            run_id=self.module.params.get("run_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_statement,
            run_id=self.module.params.get("run_id"),
            statement_id=self.module.params.get("statement_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "run_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_statements, **kwargs
        )

    def get_create_model_class(self):
        return CreateStatementDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_statement,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_statement_details=create_details,
                run_id=self.module.params.get("run_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_statement,
            call_fn_args=(),
            call_fn_kwargs=dict(
                run_id=self.module.params.get("run_id"),
                statement_id=self.module.params.get("statement_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataFlowStatementHelperCustom = get_custom_class("DataFlowStatementHelperCustom")


class ResourceHelper(DataFlowStatementHelperCustom, DataFlowStatementHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            code=dict(type="str"),
            run_id=dict(type="str", required=True),
            statement_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="statement",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
