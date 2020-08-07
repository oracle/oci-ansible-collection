#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_data_flow_run_facts
short_description: Fetches details about one or multiple Run resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Run resources in Oracle Cloud Infrastructure
    - Lists all runs of an application in the specified compartment.
    - If I(run_id) is specified, the details of a single Run will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    run_id:
        description:
            - The unique ID for the run
            - Required to get a specific run.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple runs.
        type: str
    application_id:
        description:
            - The ID of the application.
        type: str
    owner_principal_id:
        description:
            - The OCID of the user who created the resource.
        type: str
    display_name_starts_with:
        description:
            - The displayName prefix.
        type: str
    lifecycle_state:
        description:
            - The LifecycleState of the run.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "CANCELING"
            - "CANCELED"
            - "FAILED"
            - "SUCCEEDED"
    time_created_greater_than:
        description:
            - The epoch time that the resource was created.
        type: str
    sort_by:
        description:
            - The field used to sort the results. Multiple fields are not supported.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
            - "language"
            - "runDurationInMilliseconds"
            - "lifecycleState"
            - "totalOCpu"
            - "dataReadInBytes"
            - "dataWrittenInBytes"
    sort_order:
        description:
            - The ordering of results in ascending or descending order.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - The query parameter for the Spark application name.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List runs
  oci_data_flow_run_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific run
  oci_data_flow_run_facts:
    run_id: ocid1.run.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
runs:
    description:
        - List of Run resources
    returned: on success
    type: complex
    contains:
        archive_uri:
            description:
                - An Oracle Cloud Infrastructure URI of an archive (zip) file that may used to support the execution of the application.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat
            returned: on success
            type: string
            sample: archive_uri_example
        arguments:
            description:
                - "The arguments passed to the running application as command line arguments.  An argument is
                  either a plain text or a placeholder. Placeholders are replaced using values from the parameters
                  map.  Each placeholder specified must be represented in the parameters map else the request
                  (POST or PUT) will fail with a HTTP 400 status code.  Placeholders are specified as
                  `Service Api Spec`, where `name` is the name of the parameter.
                  Example:  `[ \\"--input\\", \\"${input_file}\\", \\"--name\\", \\"John Doe\\" ]`
                  If \\"input_file\\" has a value of \\"mydata.xml\\", then the value above will be translated to
                  `--input mydata.xml --name \\"John Doe\\"`"
            returned: on success
            type: list
            sample: []
        application_id:
            description:
                - The application ID.
            returned: on success
            type: string
            sample: ocid1.application.oc1..xxxxxxEXAMPLExxxxxx
        class_name:
            description:
                - The class for the application.
            returned: on success
            type: string
            sample: class_name_example
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        configuration:
            description:
                - "The Spark configuration passed to the running process.
                  See https://spark.apache.org/docs/latest/configuration.html#available-properties
                  Example: { \\"spark.app.name\\" : \\"My App Name\\", \\"spark.shuffle.io.maxRetries\\" : \\"4\\" }
                  Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
                  not allowed to be overwritten will cause a 400 status to be returned."
            returned: on success
            type: dict
            sample: {}
        data_read_in_bytes:
            description:
                - The data read by the run in bytes.
            returned: on success
            type: int
            sample: 56
        data_written_in_bytes:
            description:
                - The data written by the run in bytes.
            returned: on success
            type: int
            sample: 56
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. This name is not necessarily unique.
            returned: on success
            type: string
            sample: display_name_example
        driver_shape:
            description:
                - The VM shape for the driver. Sets the driver cores and memory.
            returned: on success
            type: string
            sample: driver_shape_example
        executor_shape:
            description:
                - The VM shape for the executors. Sets the executor cores and memory.
            returned: on success
            type: string
            sample: executor_shape_example
        file_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the file containing the application to execute.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat
            returned: on success
            type: string
            sample: file_uri_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The ID of a run.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        language:
            description:
                - The Spark language.
            returned: on success
            type: string
            sample: SCALA
        lifecycle_details:
            description:
                - The detailed messages about the lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of this run.
            returned: on success
            type: string
            sample: ACCEPTED
        logs_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat
            returned: on success
            type: string
            sample: logs_bucket_uri_example
        num_executors:
            description:
                - The number of executor VMs requested.
            returned: on success
            type: int
            sample: 56
        opc_request_id:
            description:
                - Unique Oracle-assigned identifier for the request.
                  If you need to contact Oracle about a particular request, please provide the request ID.
            returned: on success
            type: string
            sample: ocid1.opcrequest.oc1..xxxxxxEXAMPLExxxxxx
        owner_principal_id:
            description:
                - The OCID of the user who created the resource.
            returned: on success
            type: string
            sample: ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx
        owner_user_name:
            description:
                - The username of the user who created the resource.  If the username of the owner does not exist,
                  `null` will be returned and the caller should refer to the ownerPrincipalId value instead.
            returned: on success
            type: string
            sample: owner_user_name_example
        parameters:
            description:
                - "An array of name/value pairs used to fill placeholders found in properties like
                  `Application.arguments`.  The name must be a string of one or more word characters
                  (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
                  Example:  [ { name: \\"iterations\\", value: \\"10\\"}, { name: \\"input_file\\", value: \\"mydata.xml\\" }, { name: \\"variable_x\\", value:
                  \\"${x}\\"} ]"
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - "The name of the parameter.  It must be a string of one or more word characters
                          (a-z, A-Z, 0-9, _).
                          Examples: \\"iterations\\", \\"input_file\\""
                    returned: on success
                    type: string
                    sample: name_example
                value:
                    description:
                        - "The value of the parameter. It must be a string of 0 or more characters of any kind.
                          Examples: \\"\\" (empty string), \\"10\\", \\"mydata.xml\\", \\"${x}\\""
                    returned: on success
                    type: string
                    sample: value_example
        run_duration_in_milliseconds:
            description:
                - The duration of the run in milliseconds.
            returned: on success
            type: int
            sample: 56
        spark_version:
            description:
                - The Spark version utilized to run the application.
            returned: on success
            type: string
            sample: spark_version_example
        time_created:
            description:
                - "The date and time a application was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2018-04-03T21:10:29.600Z
        time_updated:
            description:
                - "The date and time a application was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2018-04-03T21:10:29.600Z
        total_o_cpu:
            description:
                - The total number of oCPU requested by the run.
            returned: on success
            type: int
            sample: 56
        warehouse_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
                  for BATCH SQL runs.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat
            returned: on success
            type: string
            sample: warehouse_bucket_uri_example
    sample: [{
        "archive_uri": "archive_uri_example",
        "arguments": [],
        "application_id": "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx",
        "class_name": "class_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "configuration": {},
        "data_read_in_bytes": 56,
        "data_written_in_bytes": 56,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "driver_shape": "driver_shape_example",
        "executor_shape": "executor_shape_example",
        "file_uri": "file_uri_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "language": "SCALA",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACCEPTED",
        "logs_bucket_uri": "logs_bucket_uri_example",
        "num_executors": 56,
        "opc_request_id": "ocid1.opcrequest.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_user_name": "owner_user_name_example",
        "parameters": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "run_duration_in_milliseconds": 56,
        "spark_version": "spark_version_example",
        "time_created": "2018-04-03T21:10:29.600Z",
        "time_updated": "2018-04-03T21:10:29.600Z",
        "total_o_cpu": 56,
        "warehouse_bucket_uri": "warehouse_bucket_uri_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_flow import DataFlowClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowRunFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "run_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_run, run_id=self.module.params.get("run_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "application_id",
            "owner_principal_id",
            "display_name_starts_with",
            "lifecycle_state",
            "time_created_greater_than",
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_runs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataFlowRunFactsHelperCustom = get_custom_class("DataFlowRunFactsHelperCustom")


class ResourceFactsHelper(DataFlowRunFactsHelperCustom, DataFlowRunFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            run_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            application_id=dict(type="str"),
            owner_principal_id=dict(type="str"),
            display_name_starts_with=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "CANCELING",
                    "CANCELED",
                    "FAILED",
                    "SUCCEEDED",
                ],
            ),
            time_created_greater_than=dict(type="str"),
            sort_by=dict(
                type="str",
                choices=[
                    "timeCreated",
                    "displayName",
                    "language",
                    "runDurationInMilliseconds",
                    "lifecycleState",
                    "totalOCpu",
                    "dataReadInBytes",
                    "dataWrittenInBytes",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="run",
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

    module.exit_json(runs=result)


if __name__ == "__main__":
    main()
