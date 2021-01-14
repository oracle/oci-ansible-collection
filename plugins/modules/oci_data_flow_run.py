#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_data_flow_run
short_description: Manage a Run resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a Run resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a run for an application.
    - "This resource has the following action operations in the M(oci_run_actions) module: cancel."
version_added: "2.9"
author: Oracle (@oracle)
options:
    application_id:
        description:
            - The application ID.
            - Required for create using I(state=present).
        type: str
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
        type: list
    compartment_id:
        description:
            - The OCID of a compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    configuration:
        description:
            - "The Spark configuration passed to the running process.
              See https://spark.apache.org/docs/latest/configuration.html#available-properties.
              Example: { \\"spark.app.name\\" : \\"My App Name\\", \\"spark.shuffle.io.maxRetries\\" : \\"4\\" }
              Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
              not allowed to be overwritten will cause a 400 status to be returned."
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    display_name:
        description:
            - A user-friendly name. It does not have to be unique. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    driver_shape:
        description:
            - The VM shape for the driver. Sets the driver cores and memory.
        type: str
    executor_shape:
        description:
            - The VM shape for the executors. Sets the executor cores and memory.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    logs_bucket_uri:
        description:
            - An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
              See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
        type: str
    num_executors:
        description:
            - The number of executor VMs requested.
        type: int
    parameters:
        description:
            - "An array of name/value pairs used to fill placeholders found in properties like
              `Application.arguments`.  The name must be a string of one or more word characters
              (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
              Example:  [ { name: \\"iterations\\", value: \\"10\\"}, { name: \\"input_file\\", value: \\"mydata.xml\\" }, { name: \\"variable_x\\", value:
              \\"${x}\\"} ]"
        type: list
        suboptions:
            name:
                description:
                    - "The name of the parameter.  It must be a string of one or more word characters
                      (a-z, A-Z, 0-9, _).
                      Examples: \\"iterations\\", \\"input_file\\""
                type: str
                required: true
            value:
                description:
                    - "The value of the parameter. It must be a string of 0 or more characters of any kind.
                      Examples: \\"\\" (empty string), \\"10\\", \\"mydata.xml\\", \\"${x}\\""
                type: str
                required: true
    warehouse_bucket_uri:
        description:
            - An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
              for BATCH SQL runs.
              See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
        type: str
    run_id:
        description:
            - The unique ID for the run
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Run.
            - Use I(state=present) to create or update a Run.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create run
  oci_data_flow_run:
    display_name: test_wordcount_run
    application_id: applicationId
    compartment_id: compartmentId
    driver_shape: VM.Standard2.1
    executor_shape: VM.Standard2.1
    num_executors: 1
    arguments:
    - oci://.../WordCount.txt
    parameters: []
    configuration: {}

- name: Update run using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_flow_run:
    freeform_tags: '{''Department'': ''Finance''}'

- name: Update run
  oci_data_flow_run:
    run_id: ocid1.run.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
run:
    description:
        - Details of the Run resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        archive_uri:
            description:
                - An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution a Python,
                  Java, or Scala application.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
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
                  See https://spark.apache.org/docs/latest/configuration.html#available-properties.
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
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
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
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
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
                - Unique Oracle assigned identifier for the request.
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
        private_endpoint_dns_zones:
            description:
                - "An array of DNS zone names.
                  Example: `[ \\"app.examplecorp.com\\", \\"app.examplecorp2.com\\" ]`"
            returned: on success
            type: list
            sample: []
        private_endpoint_max_host_count:
            description:
                - The maximum number of hosts to be accessed through the private endpoint. This value is used
                  to calculate the relevant CIDR block and should be a multiple of 256.  If the value is not a
                  multiple of 256, it is rounded up to the next multiple of 256. For example, 300 is rounded up
                  to 512.
            returned: on success
            type: int
            sample: 56
        private_endpoint_nsg_ids:
            description:
                - An array of network security group OCIDs.
            returned: on success
            type: list
            sample: []
        private_endpoint_id:
            description:
                - The OCID of a private endpoint.
            returned: on success
            type: string
            sample: ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx
        private_endpoint_subnet_id:
            description:
                - The OCID of a subnet.
            returned: on success
            type: string
            sample: ocid1.privateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx
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
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            returned: on success
            type: string
            sample: warehouse_bucket_uri_example
    sample: {
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
        "private_endpoint_dns_zones": [],
        "private_endpoint_max_host_count": 56,
        "private_endpoint_nsg_ids": [],
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "private_endpoint_subnet_id": "ocid1.privateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "run_duration_in_milliseconds": 56,
        "spark_version": "spark_version_example",
        "time_created": "2018-04-03T21:10:29.600Z",
        "time_updated": "2018-04-03T21:10:29.600Z",
        "total_o_cpu": 56,
        "warehouse_bucket_uri": "warehouse_bucket_uri_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import CreateRunDetails
    from oci.data_flow.models import UpdateRunDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowRunHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_module_resource_id_param(self):
        return "run_id"

    def get_module_resource_id(self):
        return self.module.params.get("run_id")

    def get_get_fn(self):
        return self.client.get_run

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_run, run_id=self.module.params.get("run_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["application_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_runs, **kwargs)

    def get_create_model_class(self):
        return CreateRunDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_run,
            call_fn_args=(),
            call_fn_kwargs=dict(create_run_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateRunDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_run_details=update_details,
                run_id=self.module.params.get("run_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


DataFlowRunHelperCustom = get_custom_class("DataFlowRunHelperCustom")


class ResourceHelper(DataFlowRunHelperCustom, DataFlowRunHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            application_id=dict(type="str"),
            arguments=dict(type="list"),
            compartment_id=dict(type="str"),
            configuration=dict(type="dict"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            driver_shape=dict(type="str"),
            executor_shape=dict(type="str"),
            freeform_tags=dict(type="dict"),
            logs_bucket_uri=dict(type="str"),
            num_executors=dict(type="int"),
            parameters=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value=dict(type="str", required=True),
                ),
            ),
            warehouse_bucket_uri=dict(type="str"),
            run_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="run",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
