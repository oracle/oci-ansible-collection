#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_data_flow_application_facts
short_description: Fetches details about one or multiple Application resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Application resources in Oracle Cloud Infrastructure
    - Lists all applications in the specified compartment. Only one parameter other than compartmentId may also be included in a query. The query must include
      compartmentId. If the query does not include compartmentId, or includes compartmentId but two or more other parameters an error is returned.
    - If I(application_id) is specified, the details of a single Application will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    application_id:
        description:
            - The unique ID for an application.
            - Required to get a specific application.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple applications.
        type: str
    sort_by:
        description:
            - The field used to sort the results. Multiple fields are not supported.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
            - "language"
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
    owner_principal_id:
        description:
            - The OCID of the user who created the resource.
        type: str
    display_name_starts_with:
        description:
            - The displayName prefix.
        type: str
    spark_version:
        description:
            - The Spark version utilized to run the application.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific application
  oci_data_flow_application_facts:
    # required
    application_id: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"

- name: List applications
  oci_data_flow_application_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: timeCreated
    sort_order: ASC
    display_name: display_name_example
    owner_principal_id: "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx"
    display_name_starts_with: display_name_starts_with_example
    spark_version: spark_version_example

"""

RETURN = """
applications:
    description:
        - List of Application resources
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
        class_name:
            description:
                - The class for the application.
            returned: on success
            type: str
            sample: class_name_example
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
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        description:
            description:
                - A user-friendly description.
            returned: on success
            type: str
            sample: description_example
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
            sample: "`--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv..."
        executor_shape:
            description:
                - The VM shape for the executors. Sets the executor cores and memory.
            returned: on success
            type: str
            sample: executor_shape_example
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
                - The application ID.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        language:
            description:
                - The Spark language.
            returned: on success
            type: str
            sample: SCALA
        lifecycle_state:
            description:
                - The current state of this application.
            returned: on success
            type: str
            sample: ACTIVE
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
        private_endpoint_id:
            description:
                - The OCID of a private endpoint.
            returned: on success
            type: str
            sample: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
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
        warehouse_bucket_uri:
            description:
                - An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
                  for BATCH SQL runs.
                  See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            returned: on success
            type: str
            sample: warehouse_bucket_uri_example
    sample: [{
        "archive_uri": "archive_uri_example",
        "arguments": [],
        "class_name": "class_name_example",
        "configuration": {},
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
        "display_name": "display_name_example",
        "driver_shape": "driver_shape_example",
        "execute": "`--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv...",
        "executor_shape": "executor_shape_example",
        "file_uri": "file_uri_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "language": "SCALA",
        "lifecycle_state": "ACTIVE",
        "logs_bucket_uri": "logs_bucket_uri_example",
        "metastore_id": "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx",
        "num_executors": 56,
        "owner_principal_id": "ocid1.ownerprincipal.oc1..xxxxxxEXAMPLExxxxxx",
        "owner_user_name": "owner_user_name_example",
        "parameters": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "private_endpoint_id": "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx",
        "spark_version": "spark_version_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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


class DataFlowApplicationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "application_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_application,
            application_id=self.module.params.get("application_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "display_name",
            "owner_principal_id",
            "display_name_starts_with",
            "spark_version",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_applications,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataFlowApplicationFactsHelperCustom = get_custom_class(
    "DataFlowApplicationFactsHelperCustom"
)


class ResourceFactsHelper(
    DataFlowApplicationFactsHelperCustom, DataFlowApplicationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            application_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(
                type="str", choices=["timeCreated", "displayName", "language"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
            owner_principal_id=dict(type="str"),
            display_name_starts_with=dict(type="str"),
            spark_version=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="application",
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

    module.exit_json(applications=result)


if __name__ == "__main__":
    main()
