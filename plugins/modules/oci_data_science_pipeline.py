#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_data_science_pipeline
short_description: Manage a Pipeline resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Pipeline resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Pipeline.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_science_pipeline_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate the pipeline with.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the pipeline.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    infrastructure_configuration_details:
        description:
            - ""
        type: dict
        suboptions:
            shape_name:
                description:
                    - The shape used to launch the instance for all step runs in the pipeline.
                type: str
                required: true
            block_storage_size_in_gbs:
                description:
                    - The size of the block storage volume to attach to the instance.
                type: int
                required: true
            shape_config_details:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - A pipeline step run instance of type VM.Standard.E3.Flex allows the ocpu count to be specified.
                        type: float
                    memory_in_gbs:
                        description:
                            - A pipeline step run instance of type VM.Standard.E3.Flex allows memory to be specified. This specifies the size of the memory in
                              GBs.
                        type: float
    display_name:
        description:
            - A user-friendly display name for the resource.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - A short description of the pipeline.
            - This parameter is updatable.
        type: str
    configuration_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            type:
                description:
                    - The type of pipeline.
                type: str
                choices:
                    - "DEFAULT"
                required: true
            maximum_runtime_in_minutes:
                description:
                    - A time bound for the execution of the entire Pipeline. Timer starts when the Pipeline Run is in progress.
                type: int
            environment_variables:
                description:
                    - Environment variables to set for steps in the pipeline.
                type: dict
            command_line_arguments:
                description:
                    - The command line arguments to set for steps in the pipeline.
                type: str
    log_configuration_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            enable_logging:
                description:
                    - If customer logging is enabled for pipeline.
                type: bool
            enable_auto_log_creation:
                description:
                    - If automatic on-behalf-of log object creation is enabled for pipeline runs.
                type: bool
            log_group_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log group.
                type: str
            log_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log.
                type: str
    step_details:
        description:
            - Array of step details for each step.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            job_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job to be used as a step.
                    - Required when step_type is 'ML_JOB'
                type: str
            depends_on:
                description:
                    - The list of step names this current step depends on for execution.
                type: list
                elements: str
            step_infrastructure_configuration_details:
                description:
                    - ""
                    - Applicable when step_type is 'CUSTOM_SCRIPT'
                type: dict
                suboptions:
                    shape_name:
                        description:
                            - The shape used to launch the instance for all step runs in the pipeline.
                            - Required when step_type is 'CUSTOM_SCRIPT'
                        type: str
                        required: true
                    block_storage_size_in_gbs:
                        description:
                            - The size of the block storage volume to attach to the instance.
                            - Required when step_type is 'CUSTOM_SCRIPT'
                        type: int
                        required: true
                    shape_config_details:
                        description:
                            - ""
                            - Applicable when step_type is 'CUSTOM_SCRIPT'
                        type: dict
                        suboptions:
                            ocpus:
                                description:
                                    - A pipeline step run instance of type VM.Standard.E3.Flex allows the ocpu count to be specified.
                                    - Applicable when step_type is 'CUSTOM_SCRIPT'
                                type: float
                            memory_in_gbs:
                                description:
                                    - A pipeline step run instance of type VM.Standard.E3.Flex allows memory to be specified. This specifies the size of the
                                      memory in GBs.
                                    - Applicable when step_type is 'CUSTOM_SCRIPT'
                                type: float
            is_artifact_uploaded:
                description:
                    - A flag to indicate whether the artifact has been uploaded for this step or not.
                    - Applicable when step_type is 'CUSTOM_SCRIPT'
                type: bool
            step_type:
                description:
                    - The type of step.
                    - This parameter is updatable.
                type: str
                choices:
                    - "ML_JOB"
                    - "CUSTOM_SCRIPT"
                required: true
            step_name:
                description:
                    - The name of the step. It must be unique within the pipeline. This is used to create the pipeline DAG.
                    - This parameter is updatable.
                type: str
                required: true
            description:
                description:
                    - A short description of the step.
                    - This parameter is updatable.
                type: str
            step_configuration_details:
                description:
                    - ""
                type: dict
                suboptions:
                    maximum_runtime_in_minutes:
                        description:
                            - A time bound for the execution of the step.
                            - Applicable when step_type is 'ML_JOB'
                        type: int
                    environment_variables:
                        description:
                            - Environment variables to set for step.
                            - Applicable when step_type is 'ML_JOB'
                        type: dict
                    command_line_arguments:
                        description:
                            - The command line arguments to set for step.
                            - Applicable when step_type is 'ML_JOB'
                        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    pipeline_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    delete_related_pipeline_runs:
        description:
            - A boolean value to specify whether to delete related PipelineRuns or not.
        type: bool
    delete_related_job_runs:
        description:
            - A boolean value to specify whether to delete related jobRuns or not.
        type: bool
    state:
        description:
            - The state of the Pipeline.
            - Use I(state=present) to create or update a Pipeline.
            - Use I(state=absent) to delete a Pipeline.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create pipeline
  oci_data_science_pipeline:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    step_details:
    - # required
      job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
      step_type: ML_JOB
      step_name: step_name_example

      # optional
      depends_on: [ "depends_on_example" ]
      description: description_example
      step_configuration_details:
        # optional
        maximum_runtime_in_minutes: 56
        environment_variables: null
        command_line_arguments: command_line_arguments_example

    # optional
    infrastructure_configuration_details:
      # required
      shape_name: shape_name_example
      block_storage_size_in_gbs: 56

      # optional
      shape_config_details:
        # optional
        ocpus: 3.4
        memory_in_gbs: 3.4
    display_name: display_name_example
    description: description_example
    configuration_details:
      # required
      type: DEFAULT

      # optional
      maximum_runtime_in_minutes: 56
      environment_variables: null
      command_line_arguments: command_line_arguments_example
    log_configuration_details:
      # optional
      enable_logging: true
      enable_auto_log_creation: true
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update pipeline
  oci_data_science_pipeline:
    # required
    pipeline_id: "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    configuration_details:
      # required
      type: DEFAULT

      # optional
      maximum_runtime_in_minutes: 56
      environment_variables: null
      command_line_arguments: command_line_arguments_example
    log_configuration_details:
      # optional
      enable_logging: true
      enable_auto_log_creation: true
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    step_details:
    - # required
      job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
      step_type: ML_JOB
      step_name: step_name_example

      # optional
      depends_on: [ "depends_on_example" ]
      description: description_example
      step_configuration_details:
        # optional
        maximum_runtime_in_minutes: 56
        environment_variables: null
        command_line_arguments: command_line_arguments_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update pipeline using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_pipeline:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    configuration_details:
      # required
      type: DEFAULT

      # optional
      maximum_runtime_in_minutes: 56
      environment_variables: null
      command_line_arguments: command_line_arguments_example
    log_configuration_details:
      # optional
      enable_logging: true
      enable_auto_log_creation: true
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    step_details:
    - # required
      job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
      step_type: ML_JOB
      step_name: step_name_example

      # optional
      depends_on: [ "depends_on_example" ]
      description: description_example
      step_configuration_details:
        # optional
        maximum_runtime_in_minutes: 56
        environment_variables: null
        command_line_arguments: command_line_arguments_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete pipeline
  oci_data_science_pipeline:
    # required
    pipeline_id: "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    delete_related_pipeline_runs: true
    delete_related_job_runs: true

- name: Delete pipeline using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_pipeline:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
pipeline:
    description:
        - Details of the Pipeline resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "The date and time the resource was created in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2020-08-06T21:10:29.41Z"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - "The date and time the resource was updated in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: 2020-08-06T21:10:29.41Z"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the pipeline.
            returned: on success
            type: str
            sample: created_by_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate the pipeline with.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the
                  pipeline.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the resource.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - A short description of the pipeline.
            returned: on success
            type: str
            sample: description_example
        configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of pipeline.
                    returned: on success
                    type: str
                    sample: DEFAULT
                maximum_runtime_in_minutes:
                    description:
                        - A time bound for the execution of the entire Pipeline. Timer starts when the Pipeline Run is in progress.
                    returned: on success
                    type: int
                    sample: 56
                environment_variables:
                    description:
                        - Environment variables to set for steps in the pipeline.
                    returned: on success
                    type: dict
                    sample: {}
                command_line_arguments:
                    description:
                        - The command line arguments to set for steps in the pipeline.
                    returned: on success
                    type: str
                    sample: command_line_arguments_example
        log_configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                enable_logging:
                    description:
                        - If customer logging is enabled for pipeline.
                    returned: on success
                    type: bool
                    sample: true
                enable_auto_log_creation:
                    description:
                        - If automatic on-behalf-of log object creation is enabled for pipeline runs.
                    returned: on success
                    type: bool
                    sample: true
                log_group_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log group.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the log.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        infrastructure_configuration_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape_name:
                    description:
                        - The shape used to launch the instance for all step runs in the pipeline.
                    returned: on success
                    type: str
                    sample: shape_name_example
                block_storage_size_in_gbs:
                    description:
                        - The size of the block storage volume to attach to the instance.
                    returned: on success
                    type: int
                    sample: 56
                shape_config_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - A pipeline step run instance of type VM.Standard.E3.Flex allows the ocpu count to be specified.
                            returned: on success
                            type: float
                            sample: 3.4
                        memory_in_gbs:
                            description:
                                - A pipeline step run instance of type VM.Standard.E3.Flex allows memory to be specified. This specifies the size of the memory
                                  in GBs.
                            returned: on success
                            type: float
                            sample: 3.4
        step_details:
            description:
                - Array of step details for each step.
            returned: on success
            type: complex
            contains:
                step_infrastructure_configuration_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        shape_name:
                            description:
                                - The shape used to launch the instance for all step runs in the pipeline.
                            returned: on success
                            type: str
                            sample: shape_name_example
                        block_storage_size_in_gbs:
                            description:
                                - The size of the block storage volume to attach to the instance.
                            returned: on success
                            type: int
                            sample: 56
                        shape_config_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpus:
                                    description:
                                        - A pipeline step run instance of type VM.Standard.E3.Flex allows the ocpu count to be specified.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                memory_in_gbs:
                                    description:
                                        - A pipeline step run instance of type VM.Standard.E3.Flex allows memory to be specified. This specifies the size of the
                                          memory in GBs.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                is_artifact_uploaded:
                    description:
                        - A flag to indicate whether the artifact has been uploaded for this step or not.
                    returned: on success
                    type: bool
                    sample: true
                step_type:
                    description:
                        - The type of step.
                    returned: on success
                    type: str
                    sample: ML_JOB
                step_name:
                    description:
                        - The name of the step. It must be unique within the pipeline. This is used to create the pipeline DAG.
                    returned: on success
                    type: str
                    sample: step_name_example
                description:
                    description:
                        - A short description of the step.
                    returned: on success
                    type: str
                    sample: description_example
                depends_on:
                    description:
                        - The list of step names this current step depends on for execution.
                    returned: on success
                    type: list
                    sample: []
                step_configuration_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        maximum_runtime_in_minutes:
                            description:
                                - A time bound for the execution of the step.
                            returned: on success
                            type: int
                            sample: 56
                        environment_variables:
                            description:
                                - Environment variables to set for step.
                            returned: on success
                            type: dict
                            sample: {}
                        command_line_arguments:
                            description:
                                - The command line arguments to set for step.
                            returned: on success
                            type: str
                            sample: command_line_arguments_example
                job_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job to be used as a step.
                    returned: on success
                    type: str
                    sample: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the pipeline.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in 'Failed'
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "configuration_details": {
            "type": "DEFAULT",
            "maximum_runtime_in_minutes": 56,
            "environment_variables": {},
            "command_line_arguments": "command_line_arguments_example"
        },
        "log_configuration_details": {
            "enable_logging": true,
            "enable_auto_log_creation": true,
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "infrastructure_configuration_details": {
            "shape_name": "shape_name_example",
            "block_storage_size_in_gbs": 56,
            "shape_config_details": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            }
        },
        "step_details": [{
            "step_infrastructure_configuration_details": {
                "shape_name": "shape_name_example",
                "block_storage_size_in_gbs": 56,
                "shape_config_details": {
                    "ocpus": 3.4,
                    "memory_in_gbs": 3.4
                }
            },
            "is_artifact_uploaded": true,
            "step_type": "ML_JOB",
            "step_name": "step_name_example",
            "description": "description_example",
            "depends_on": [],
            "step_configuration_details": {
                "maximum_runtime_in_minutes": 56,
                "environment_variables": {},
                "command_line_arguments": "command_line_arguments_example"
            },
            "job_id": "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.data_science import DataScienceClient
    from oci.data_science.models import CreatePipelineDetails
    from oci.data_science.models import UpdatePipelineDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSciencePipelineHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DataSciencePipelineHelperGen, self).get_possible_entity_types() + [
            "pipeline",
            "pipelines",
            "dataSciencepipeline",
            "dataSciencepipelines",
            "pipelineresource",
            "pipelinesresource",
            "datascience",
        ]

    def get_module_resource_id_param(self):
        return "pipeline_id"

    def get_module_resource_id(self):
        return self.module.params.get("pipeline_id")

    def get_get_fn(self):
        return self.client.get_pipeline

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_pipeline, pipeline_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pipeline, pipeline_id=self.module.params.get("pipeline_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_pipelines, **kwargs)

    def get_create_model_class(self):
        return CreatePipelineDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_pipeline,
            call_fn_args=(),
            call_fn_kwargs=dict(create_pipeline_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePipelineDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_pipeline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pipeline_id=self.module.params.get("pipeline_id"),
                update_pipeline_details=update_details,
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
            call_fn=self.client.delete_pipeline,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pipeline_id=self.module.params.get("pipeline_id"),
                delete_related_pipeline_runs=self.module.params.get(
                    "delete_related_pipeline_runs"
                ),
                delete_related_job_runs=self.module.params.get(
                    "delete_related_job_runs"
                ),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DataSciencePipelineHelperCustom = get_custom_class("DataSciencePipelineHelperCustom")


class ResourceHelper(DataSciencePipelineHelperCustom, DataSciencePipelineHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
            infrastructure_configuration_details=dict(
                type="dict",
                options=dict(
                    shape_name=dict(type="str", required=True),
                    block_storage_size_in_gbs=dict(type="int", required=True),
                    shape_config_details=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                        ),
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            configuration_details=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["DEFAULT"]),
                    maximum_runtime_in_minutes=dict(type="int"),
                    environment_variables=dict(type="dict"),
                    command_line_arguments=dict(type="str"),
                ),
            ),
            log_configuration_details=dict(
                type="dict",
                options=dict(
                    enable_logging=dict(type="bool"),
                    enable_auto_log_creation=dict(type="bool"),
                    log_group_id=dict(type="str"),
                    log_id=dict(type="str"),
                ),
            ),
            step_details=dict(
                type="list",
                elements="dict",
                options=dict(
                    job_id=dict(type="str"),
                    depends_on=dict(type="list", elements="str"),
                    step_infrastructure_configuration_details=dict(
                        type="dict",
                        options=dict(
                            shape_name=dict(type="str", required=True),
                            block_storage_size_in_gbs=dict(type="int", required=True),
                            shape_config_details=dict(
                                type="dict",
                                options=dict(
                                    ocpus=dict(type="float"),
                                    memory_in_gbs=dict(type="float"),
                                ),
                            ),
                        ),
                    ),
                    is_artifact_uploaded=dict(type="bool"),
                    step_type=dict(
                        type="str", required=True, choices=["ML_JOB", "CUSTOM_SCRIPT"]
                    ),
                    step_name=dict(type="str", required=True),
                    description=dict(type="str"),
                    step_configuration_details=dict(
                        type="dict",
                        options=dict(
                            maximum_runtime_in_minutes=dict(type="int"),
                            environment_variables=dict(type="dict"),
                            command_line_arguments=dict(type="str"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            pipeline_id=dict(aliases=["id"], type="str"),
            delete_related_pipeline_runs=dict(type="bool"),
            delete_related_job_runs=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="pipeline",
        service_client_class=DataScienceClient,
        namespace="data_science",
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
