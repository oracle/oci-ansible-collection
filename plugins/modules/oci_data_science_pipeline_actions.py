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
module: oci_data_science_pipeline_actions
short_description: Perform actions on a Pipeline resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Pipeline resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a resource into a different compartment. When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    pipeline_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Pipeline.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on pipeline
  oci_data_science_pipeline_actions:
    # required
    pipeline_id: "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.data_science import DataScienceClient
    from oci.data_science.models import ChangePipelineCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSciencePipelineActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "pipeline_id"

    def get_module_resource_id(self):
        return self.module.params.get("pipeline_id")

    def get_get_fn(self):
        return self.client.get_pipeline

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pipeline, pipeline_id=self.module.params.get("pipeline_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangePipelineCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_pipeline_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pipeline_id=self.module.params.get("pipeline_id"),
                change_pipeline_compartment_details=action_details,
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


DataSciencePipelineActionsHelperCustom = get_custom_class(
    "DataSciencePipelineActionsHelperCustom"
)


class ResourceHelper(
    DataSciencePipelineActionsHelperCustom, DataSciencePipelineActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            pipeline_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
