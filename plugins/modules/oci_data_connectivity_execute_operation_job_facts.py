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
module: oci_data_connectivity_execute_operation_job_facts
short_description: Fetches details about a ExecuteOperationJob resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ExecuteOperationJob resource in Oracle Cloud Infrastructure
    - Get the status or the result of the execution.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry OCID.
        type: str
        required: true
    connection_key:
        description:
            - The connection key.
        type: str
        required: true
    schema_resource_name:
        description:
            - The schema resource name used for retrieving schemas.
        type: str
        required: true
    execute_operation_job_key:
        description:
            - Job ID returned by the execute operation job API.
        type: str
        required: true
    endpoint_id:
        description:
            - Endpoint ID used for getDataAssetFullDetails.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific execute_operation_job
  oci_data_connectivity_execute_operation_job_facts:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    connection_key: connection_key_example
    schema_resource_name: schema_resource_name_example
    execute_operation_job_key: execute_operation_job_key_example

    # optional
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
execute_operation_job:
    description:
        - ExecuteOperationJob resource
    returned: on success
    type: complex
    contains:
        operation_status:
            description:
                - Status of the operation job for all sets of input.
            returned: on success
            type: str
            sample: operation_status_example
        error_message:
            description:
                - Error message when the whole operation fails.
            returned: on success
            type: str
            sample: error_message_example
        operation_name:
            description:
                - Name of the operation.
            returned: on success
            type: str
            sample: operation_name_example
        out_params:
            description:
                - The list of names of OUT/INOUT parameters.
            returned: on success
            type: list
            sample: []
        operation_result:
            description:
                - The list of operation execution result for each input set.
            returned: on success
            type: complex
            contains:
                execution_status:
                    description:
                        - Status of the operation job for a particular set of input.
                    returned: on success
                    type: str
                    sample: FAILED
                error_message:
                    description:
                        - Error message when the execution of operation fails.
                    returned: on success
                    type: str
                    sample: error_message_example
                metrics:
                    description:
                        - Metrics of operation execution job.
                    returned: on success
                    type: dict
                    sample: {}
                output_values:
                    description:
                        - The list of emitted rows for each OUT/INOUT parameter.
                    returned: on success
                    type: list
                    sample: []
                is_whitelisted_error_message:
                    description:
                        - True, if the error message must be displayed in the UI.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "operation_status": "operation_status_example",
        "error_message": "error_message_example",
        "operation_name": "operation_name_example",
        "out_params": [],
        "operation_result": [{
            "execution_status": "FAILED",
            "error_message": "error_message_example",
            "metrics": {},
            "output_values": [],
            "is_whitelisted_error_message": true
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExecuteOperationJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "registry_id",
            "connection_key",
            "schema_resource_name",
            "execute_operation_job_key",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "endpoint_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_execute_operation_job,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
            schema_resource_name=self.module.params.get("schema_resource_name"),
            execute_operation_job_key=self.module.params.get(
                "execute_operation_job_key"
            ),
            **optional_kwargs
        )


ExecuteOperationJobFactsHelperCustom = get_custom_class(
    "ExecuteOperationJobFactsHelperCustom"
)


class ResourceFactsHelper(
    ExecuteOperationJobFactsHelperCustom, ExecuteOperationJobFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            registry_id=dict(type="str", required=True),
            connection_key=dict(type="str", required=True, no_log=True),
            schema_resource_name=dict(type="str", required=True),
            execute_operation_job_key=dict(type="str", required=True, no_log=True),
            endpoint_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="execute_operation_job",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(execute_operation_job=result)


if __name__ == "__main__":
    main()
