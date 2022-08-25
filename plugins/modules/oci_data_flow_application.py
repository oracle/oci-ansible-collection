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
module: oci_data_flow_application
short_description: Manage an Application resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Application resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an application.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_flow_application_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of a compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    type:
        description:
            - The Spark application processing type.
        type: str
        choices:
            - "BATCH"
            - "STREAMING"
    class_name:
        description:
            - The class for the application.
            - This parameter is updatable.
        type: str
    file_uri:
        description:
            - An Oracle Cloud Infrastructure URI of the file containing the application to execute.
              See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    spark_version:
        description:
            - The Spark version utilized to run the application.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    language:
        description:
            - The Spark language.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "SCALA"
            - "JAVA"
            - "PYTHON"
            - "SQL"
    application_log_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            log_group_id:
                description:
                    - The log group id for where log objects will be for Data Flow Runs.
                type: str
                required: true
            log_id:
                description:
                    - The log id of the log object the Application Logs of Data Flow Run will be shipped to.
                type: str
                required: true
    archive_uri:
        description:
            - An Oracle Cloud Infrastructure URI of an archive.zip file containing custom dependencies that may be used to support the execution a Python, Java,
              or Scala application.
              See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            - This parameter is updatable.
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
            - This parameter is updatable.
        type: list
        elements: str
    configuration:
        description:
            - "The Spark configuration passed to the running process.
              See https://spark.apache.org/docs/latest/configuration.html#available-properties.
              Example: { \\"spark.app.name\\" : \\"My App Name\\", \\"spark.shuffle.io.maxRetries\\" : \\"4\\" }
              Note: Not all Spark properties are permitted to be set.  Attempting to set a property that is
              not allowed to be overwritten will cause a 400 status to be returned."
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    description:
        description:
            - A user-friendly description. Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    driver_shape:
        description:
            - The VM shape for the driver. Sets the driver cores and memory.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    driver_shape_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            ocpus:
                description:
                    - The total number of OCPUs used for the driver or executors.
                      See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                type: float
            memory_in_gbs:
                description:
                    - The amount of memory used for the driver or executors.
                type: float
    execute:
        description:
            - "The input used for spark-submit command. For more details see https://spark.apache.org/docs/latest/submitting-applications.html#launching-
              applications-with-spark-submit.
              Supported options include ``--class``, ``--file``, ``--jars``, ``--conf``, ``--py-files``, and main application file with arguments.
              Example: ``--jars oci://path/to/a.jar,oci://path/to/b.jar --files oci://path/to/a.json,oci://path/to/b.csv --py-files
              oci://path/to/a.py,oci://path/to/b.py --conf spark.sql.crossJoin.enabled=true --class org.apache.spark.examples.SparkPi oci://path/to/main.jar
              10``
              Note: If execute is specified together with applicationId, className, configuration, fileUri, language, arguments, parameters during application
              create/update, or run create/submit,
              Data Flow service will use derived information from execute input only."
            - This parameter is updatable.
        type: str
    executor_shape:
        description:
            - The VM shape for the executors. Sets the executor cores and memory.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    executor_shape_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            ocpus:
                description:
                    - The total number of OCPUs used for the driver or executors.
                      See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                type: float
            memory_in_gbs:
                description:
                    - The amount of memory used for the driver or executors.
                type: float
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
            - This parameter is updatable.
        type: str
    metastore_id:
        description:
            - The OCID of OCI Hive Metastore.
            - This parameter is updatable.
        type: str
    num_executors:
        description:
            - The number of executor VMs requested.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    parameters:
        description:
            - "An array of name/value pairs used to fill placeholders found in properties like
              `Application.arguments`.  The name must be a string of one or more word characters
              (a-z, A-Z, 0-9, _).  The value can be a string of 0 or more characters of any kind.
              Example:  [ { name: \\"iterations\\", value: \\"10\\"}, { name: \\"input_file\\", value: \\"mydata.xml\\" }, { name: \\"variable_x\\", value:
              \\"${x}\\"} ]"
            - This parameter is updatable.
        type: list
        elements: dict
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
    private_endpoint_id:
        description:
            - The OCID of a private endpoint.
            - This parameter is updatable.
        type: str
    warehouse_bucket_uri:
        description:
            - An Oracle Cloud Infrastructure URI of the bucket to be used as default warehouse directory
              for BATCH SQL runs.
              See https://docs.cloud.oracle.com/iaas/Content/API/SDKDocs/hdfsconnector.htm#uriformat.
            - This parameter is updatable.
        type: str
    application_id:
        description:
            - The unique ID for an application.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Application.
            - Use I(state=present) to create or update an Application.
            - Use I(state=absent) to delete an Application.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create application
  oci_data_flow_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    file_uri: file_uri_example
    spark_version: spark_version_example
    language: SCALA
    display_name: display_name_example
    driver_shape: driver_shape_example
    executor_shape: executor_shape_example
    num_executors: 56

    # optional
    type: BATCH
    class_name: class_name_example
    application_log_config:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    archive_uri: archive_uri_example
    arguments: [ "arguments_example" ]
    configuration: null
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    driver_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    execute: execute_example
    executor_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    logs_bucket_uri: logs_bucket_uri_example
    metastore_id: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
    parameters:
    - # required
      name: name_example
      value: value_example
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    warehouse_bucket_uri: warehouse_bucket_uri_example

- name: Update application
  oci_data_flow_application:
    # required
    application_id: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    class_name: class_name_example
    file_uri: file_uri_example
    spark_version: spark_version_example
    language: SCALA
    application_log_config:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    archive_uri: archive_uri_example
    arguments: [ "arguments_example" ]
    configuration: null
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    display_name: display_name_example
    driver_shape: driver_shape_example
    driver_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    execute: execute_example
    executor_shape: executor_shape_example
    executor_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    logs_bucket_uri: logs_bucket_uri_example
    metastore_id: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
    num_executors: 56
    parameters:
    - # required
      name: name_example
      value: value_example
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    warehouse_bucket_uri: warehouse_bucket_uri_example

- name: Update application using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_flow_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    class_name: class_name_example
    file_uri: file_uri_example
    spark_version: spark_version_example
    language: SCALA
    application_log_config:
      # required
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    archive_uri: archive_uri_example
    arguments: [ "arguments_example" ]
    configuration: null
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    description: description_example
    driver_shape: driver_shape_example
    driver_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    execute: execute_example
    executor_shape: executor_shape_example
    executor_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    logs_bucket_uri: logs_bucket_uri_example
    metastore_id: "ocid1.metastore.oc1..xxxxxxEXAMPLExxxxxx"
    num_executors: 56
    parameters:
    - # required
      name: name_example
      value: value_example
    private_endpoint_id: "ocid1.privateendpoint.oc1..xxxxxxEXAMPLExxxxxx"
    warehouse_bucket_uri: warehouse_bucket_uri_example

- name: Delete application
  oci_data_flow_application:
    # required
    application_id: "ocid1.application.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete application using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_flow_application:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
application:
    description:
        - Details of the Application resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        application_log_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                log_group_id:
                    description:
                        - The log group id for where log objects will be for Data Flow Runs.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The log id of the log object the Application Logs of Data Flow Run will be shipped to.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
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
        "application_log_config": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "archive_uri": "archive_uri_example",
        "arguments": [],
        "class_name": "class_name_example",
        "configuration": {},
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "description": "description_example",
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.data_flow import DataFlowClient
    from oci.data_flow.models import CreateApplicationDetails
    from oci.data_flow.models import UpdateApplicationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataFlowApplicationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DataFlowApplicationHelperGen, self).get_possible_entity_types() + [
            "dataflowapplication",
            "dataflowapplications",
            "dataFlowdataflowapplication",
            "dataFlowdataflowapplications",
            "dataflowapplicationresource",
            "dataflowapplicationsresource",
            "application",
            "applications",
            "dataFlowapplication",
            "dataFlowapplications",
            "applicationresource",
            "applicationsresource",
            "dataflow",
        ]

    def get_module_resource_id_param(self):
        return "application_id"

    def get_module_resource_id(self):
        return self.module.params.get("application_id")

    def get_get_fn(self):
        return self.client.get_application

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_application, application_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_application,
            application_id=self.module.params.get("application_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "spark_version"]
        )

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
            self.client.list_applications, **kwargs
        )

    def get_create_model_class(self):
        return CreateApplicationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_application,
            call_fn_args=(),
            call_fn_kwargs=dict(create_application_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateApplicationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_application,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_application_details=update_details,
                application_id=self.module.params.get("application_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_application,
            call_fn_args=(),
            call_fn_kwargs=dict(
                application_id=self.module.params.get("application_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataFlowApplicationHelperCustom = get_custom_class("DataFlowApplicationHelperCustom")


class ResourceHelper(DataFlowApplicationHelperCustom, DataFlowApplicationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            type=dict(type="str", choices=["BATCH", "STREAMING"]),
            class_name=dict(type="str"),
            file_uri=dict(type="str"),
            spark_version=dict(type="str"),
            language=dict(type="str", choices=["SCALA", "JAVA", "PYTHON", "SQL"]),
            application_log_config=dict(
                type="dict",
                options=dict(
                    log_group_id=dict(type="str", required=True),
                    log_id=dict(type="str", required=True),
                ),
            ),
            archive_uri=dict(type="str"),
            arguments=dict(type="list", elements="str"),
            configuration=dict(type="dict"),
            defined_tags=dict(type="dict"),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            driver_shape=dict(type="str"),
            driver_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            execute=dict(type="str"),
            executor_shape=dict(type="str"),
            executor_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            freeform_tags=dict(type="dict"),
            logs_bucket_uri=dict(type="str"),
            metastore_id=dict(type="str"),
            num_executors=dict(type="int"),
            parameters=dict(
                type="list",
                elements="dict",
                options=dict(
                    name=dict(type="str", required=True),
                    value=dict(type="str", required=True),
                ),
            ),
            private_endpoint_id=dict(type="str"),
            warehouse_bucket_uri=dict(type="str"),
            application_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="application",
        service_client_class=DataFlowClient,
        namespace="data_flow",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
