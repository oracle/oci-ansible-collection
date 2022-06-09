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
module: oci_data_flow_run_actions
short_description: Perform actions on a Run resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Run resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a run into a different compartment. When provided, If-Match is checked against ETag
      values of the resource. Associated resources, like historical metrics, will not be
      automatically moved. The run must be in a terminal state (CANCELED, FAILED, SUCCEEDED) in
      order for it to be moved to a different compartment
    - For I(action=cancel), cancels the specified run if it has not already completed or was previously cancelled.
      If a run is in progress, the executing job will be killed.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of a compartment.
            - Required for I(action=change_compartment).
        type: str
    run_id:
        description:
            - The unique ID for the run
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Run.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "cancel"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on run
  oci_data_flow_run_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action cancel on run
  oci_data_flow_run_actions:
    # required
    run_id: "ocid1.run.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel

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
            type: str
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
            type: str
            sample: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"
        class_name:
            description:
                - The class for the application.
            returned: on success
            type: str
            sample: class_name_example
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
            type: str
            sample: display_name_example
        driver_shape:
            description:
                - The VM shape for the driver. Sets the driver cores and memory.
            returned: on success
            type: str
            sample: driver_shape_example
        driver_shape_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs used for the driver or executors.
                          See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                    returned: on success
                    type: float
                    sample: 10
                memory_in_gbs:
                    description:
                        - The amount of memory used for the driver or executors.
                    returned: on success
                    type: float
                    sample: 10
        execute:
            description:
                - "The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-
                  applications-with-spark-submit.
                  Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments.
                  Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files
                  oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar
                  10``
                  Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during
                  application create/update, or run create/submit,
                  Data Flow service will use derived information from execute input only."
            returned: on success
            type: str
            sample: execute_example
        executor_shape:
            description:
                - The VM shape for the executors. Sets the executor cores and memory.
            returned: on success
            type: str
            sample: executor_shape_example
        executor_shape_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs used for the driver or executors.
                          See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                    returned: on success
                    type: float
                    sample: 10
                memory_in_gbs:
                    description:
                        - The amount of memory used for the driver or executors.
                    returned: on success
                    type: float
                    sample: 10
        file_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the file containing the application to execute.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            returned: on success
            type: str
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
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        language:
            description:
                - The Spark language.
            returned: on success
            type: str
            sample: SCALA
        lifecycle_details:
            description:
                - The detailed messages about the lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of this run.
            returned: on success
            type: str
            sample: ACCEPTED
        logs_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket where the Spark job logs are to be uploaded.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            returned: on success
            type: str
            sample: logs_bucket_uri_example
        metastore_id:
            description:
                - The OCID of OCI Hive Metastore.
            returned: on success
            type: str
            sample: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
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
            type: str
            sample: "ocid1.opcrequest.oc1..xxxxxxEXAMPLExxxxxx"
        owner_principal_id:
            description:
                - The OCID of the user who created the resource.
            returned: on success
            type: str
            sample: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
        owner_user_name:
            description:
                - The username of the user who created the resource.  If the username of the owner does not exist,
                  `null` will be returned and the caller should refer to the ownerPrincipalId value instead.
            returned: on success
            type: str
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
                    type: str
                    sample: name_example
                value:
                    description:
                        - "The value of the parameter. It must be a string of 0 or more characters of any kind.
                          Examples: \\"\\" (empty string), \\"10\\", \\"mydata.xml\\", \\"${x}\\""
                    returned: on success
                    type: str
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
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        private_endpoint_subnet_id:
            description:
                - The OCID of a subnet.
            returned: on success
            type: str
            sample: "ocid1.privateendpointsubnet.oc1..xxxxxxEXAMPLExxxxxx"
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
            type: str
            sample: spark_version_example
        time_created:
            description:
                - "The date and time a application was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time a application was updated, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
                  Example: `2018-04-03T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        total_o_cpu:
            description:
                - The total number of oCPU requested by the run.
            returned: on success
            type: int
            sample: 56
        type:
            description:
                - The Spark application processing type.
            returned: on success
            type: str
            sample: BATCH
        warehouse_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
                  for BATCH SQL runs.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            returned: on success
            type: str
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
        "driver_shape_config": {
            "ocpus": 10,
            "memory_in_gbs": 10
        },
        "execute": "execute_example",
        "executor_shape": "executor_shape_example",
        "executor_shape_config": {
            "ocpus": 10,
            "memory_in_gbs": 10
        },
        "file_uri": "file_uri_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "language": "SCALA",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "ACCEPTED",
        "logs_bucket_uri": "logs_bucket_uri_example",
        "metastore_id": "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx",
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
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "total_o_cpu": 56,
        "type": "BATCH",
        "warehouse_bucket_uri": "warehouse_bucket_uri_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import ChangeRunCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowRunActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        cancel
    """

    @staticmethod
    def get_module_resource_id_param():
        return "run_id"

    def get_module_resource_id(self):
        return self.module.params.get("run_id")

    def get_get_fn(self):
        return self.client.get_run

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_run, run_id=self.module.params.get("run_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeRunCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_run_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                run_id=self.module.params.get("run_id"),
                change_run_compartment_details=action_details,
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

    def cancel(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_run,
            call_fn_args=(),
            call_fn_kwargs=dict(run_id=self.module.params.get("run_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


DataFlowRunActionsHelperCustom = get_custom_class("DataFlowRunActionsHelperCustom")


class ResourceHelper(DataFlowRunActionsHelperCustom, DataFlowRunActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            run_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str", required=True, choices=["change_compartment", "cancel"]
            ),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
