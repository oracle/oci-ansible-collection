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
module: oci_data_flow_statement_facts
short_description: Fetches details about one or multiple Statement resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Statement resources in Oracle Cloud Infrastructure
    - Lists all statements for a Session run.
    - If I(statement_id) is specified, the details of a single Statement will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    statement_id:
        description:
            - The unique ID for the statement.
            - Required to get a specific statement.
        type: str
        aliases: ["id"]
    run_id:
        description:
            - The unique ID for the run
        type: str
        required: true
    lifecycle_state:
        description:
            - The LifecycleState of the statement.
        type: str
        choices:
            - "ACCEPTED"
            - "CANCELLING"
            - "CANCELLED"
            - "FAILED"
            - "IN_PROGRESS"
            - "SUCCEEDED"
    sort_by:
        description:
            - The field used to sort the results. Multiple fields are not supported.
        type: str
        choices:
            - "timeCreated"
    sort_order:
        description:
            - The ordering of results in ascending or descending order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific statement
  oci_data_flow_statement_facts:
    # required
    statement_id: "ocid1.statement.oc1..xxxxxxEXAMPLExxxxxx"
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"

- name: List statements
  oci_data_flow_statement_facts:
    # required
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: ACCEPTED
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
statements:
    description:
        - List of Statement resources
    returned: on success
    type: complex
    contains:
        code:
            description:
                - "The statement code to execute.
                  Example: `println(sc.version)`"
                - Returned for get operation
            returned: on success
            type: str
            sample: code_example
        output:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: float
            sample: 1.2
        id:
            description:
                - The statement ID.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of this statement.
            returned: on success
            type: str
            sample: ACCEPTED
        run_id:
            description:
                - The ID of a run.
            returned: on success
            type: str
            sample: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
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
    sample: [{
        "code": "code_example",
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
        "id": 56,
        "lifecycle_state": "ACCEPTED",
        "run_id": "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_completed": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_flow import DataFlowClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowStatementFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "run_id",
            "statement_id",
        ]

    def get_required_params_for_list(self):
        return [
            "run_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_statement,
            run_id=self.module.params.get("run_id"),
            statement_id=self.module.params.get("statement_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_statements,
            run_id=self.module.params.get("run_id"),
            **optional_kwargs
        )


DataFlowStatementFactsHelperCustom = get_custom_class(
    "DataFlowStatementFactsHelperCustom"
)


class ResourceFactsHelper(
    DataFlowStatementFactsHelperCustom, DataFlowStatementFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            statement_id=dict(aliases=["id"], type="str"),
            run_id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "CANCELLING",
                    "CANCELLED",
                    "FAILED",
                    "IN_PROGRESS",
                    "SUCCEEDED",
                ],
            ),
            sort_by=dict(type="str", choices=["timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="statement",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(statements=result)


if __name__ == "__main__":
    main()
