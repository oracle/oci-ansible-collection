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
module: oci_data_science_pipeline_run
short_description: Manage a PipelineRun resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a PipelineRun resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new PipelineRun.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_science_pipeline_run_actions) module: cancel, change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    project_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate the pipeline run with.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the pipeline
              run.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    pipeline_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline for which pipeline run is created.
            - Required for create using I(state=present).
        type: str
    configuration_override_details:
        description:
            - ""
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
    log_configuration_override_details:
        description:
            - ""
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
    step_override_details:
        description:
            - Array of step override details. Only Step Configuration is allowed to be overridden.
        type: list
        elements: dict
        suboptions:
            step_name:
                description:
                    - The name of the step.
                type: str
                required: true
            step_configuration_details:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    maximum_runtime_in_minutes:
                        description:
                            - A time bound for the execution of the step.
                        type: int
                    environment_variables:
                        description:
                            - Environment variables to set for step.
                        type: dict
                    command_line_arguments:
                        description:
                            - The command line arguments to set for step.
                        type: str
    system_tags:
        description:
            - "Usage of system tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly display name for the resource.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
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
    pipeline_run_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline run.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    delete_related_job_runs:
        description:
            - A boolean value to specify whether to delete related jobRuns or not.
        type: bool
    state:
        description:
            - The state of the PipelineRun.
            - Use I(state=present) to create or update a PipelineRun.
            - Use I(state=absent) to delete a PipelineRun.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create pipeline_run
  oci_data_science_pipeline_run:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    pipeline_id: "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    configuration_override_details:
      # required
      type: DEFAULT

      # optional
      maximum_runtime_in_minutes: 56
      environment_variables: null
      command_line_arguments: command_line_arguments_example
    log_configuration_override_details:
      # optional
      enable_logging: true
      enable_auto_log_creation: true
      log_group_id: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
      log_id: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
    step_override_details:
    - # required
      step_name: step_name_example
      step_configuration_details:
        # optional
        maximum_runtime_in_minutes: 56
        environment_variables: null
        command_line_arguments: command_line_arguments_example
    system_tags: null
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update pipeline_run
  oci_data_science_pipeline_run:
    # required
    pipeline_run_id: "ocid1.pipelinerun.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update pipeline_run using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_pipeline_run:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete pipeline_run
  oci_data_science_pipeline_run:
    # required
    pipeline_run_id: "ocid1.pipelinerun.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    delete_related_job_runs: true

- name: Delete pipeline_run using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_science_pipeline_run:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
pipeline_run:
    description:
        - Details of the PipelineRun resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline run.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_accepted:
            description:
                - The date and time the pipeline run was accepted in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_started:
            description:
                - The date and time the pipeline run request was started in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the pipeline run was updated in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_finished:
            description:
                - The date and time the pipeline run request was finished in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the pipeline run.
            returned: on success
            type: str
            sample: created_by_example
        project_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the project to associate the pipeline run with.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment where you want to create the
                  pipeline run.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        pipeline_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline.
            returned: on success
            type: str
            sample: "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly display name for the resource.
            returned: on success
            type: str
            sample: display_name_example
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
        configuration_override_details:
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
        log_configuration_override_details:
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
        step_override_details:
            description:
                - Array of step override details. Only Step Configuration is allowed to be overridden.
            returned: on success
            type: complex
            contains:
                step_name:
                    description:
                        - The name of the step.
                    returned: on success
                    type: str
                    sample: step_name_example
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
        log_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                log_group_id:
                    description:
                        - The log group id for where log objects will be for pipeline runs.
                    returned: on success
                    type: str
                    sample: "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx"
                log_id:
                    description:
                        - The log id of the log object the pipeline run logs will be shipped to.
                    returned: on success
                    type: str
                    sample: "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        step_runs:
            description:
                - Array of StepRun object for each step.
            returned: on success
            type: complex
            contains:
                step_type:
                    description:
                        - The type of step.
                    returned: on success
                    type: str
                    sample: ML_JOB
                time_started:
                    description:
                        - The date and time the pipeline step run was started in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_finished:
                    description:
                        - The date and time the pipeline step run finshed executing in the timestamp format defined by
                          L(RFC3339,https://tools.ietf.org/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                step_name:
                    description:
                        - The name of the step.
                    returned: on success
                    type: str
                    sample: step_name_example
                lifecycle_state:
                    description:
                        - The state of the step run.
                    returned: on success
                    type: str
                    sample: WAITING
                lifecycle_details:
                    description:
                        - Details of the state of the step run.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                job_run_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the job run triggered for this step run.
                    returned: on success
                    type: str
                    sample: "ocid1.jobrun.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the pipeline run.
            returned: on success
            type: str
            sample: ACCEPTED
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
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "pipeline_id": "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "configuration_details": {
            "type": "DEFAULT",
            "maximum_runtime_in_minutes": 56,
            "environment_variables": {},
            "command_line_arguments": "command_line_arguments_example"
        },
        "configuration_override_details": {
            "type": "DEFAULT",
            "maximum_runtime_in_minutes": 56,
            "environment_variables": {},
            "command_line_arguments": "command_line_arguments_example"
        },
        "log_configuration_override_details": {
            "enable_logging": true,
            "enable_auto_log_creation": true,
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "step_override_details": [{
            "step_name": "step_name_example",
            "step_configuration_details": {
                "maximum_runtime_in_minutes": 56,
                "environment_variables": {},
                "command_line_arguments": "command_line_arguments_example"
            }
        }],
        "log_details": {
            "log_group_id": "ocid1.loggroup.oc1..xxxxxxEXAMPLExxxxxx",
            "log_id": "ocid1.log.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "step_runs": [{
            "step_type": "ML_JOB",
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_finished": "2013-10-20T19:20:30+01:00",
            "step_name": "step_name_example",
            "lifecycle_state": "WAITING",
            "lifecycle_details": "lifecycle_details_example",
            "job_run_id": "ocid1.jobrun.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "lifecycle_state": "ACCEPTED",
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
    from oci.data_science.models import CreatePipelineRunDetails
    from oci.data_science.models import UpdatePipelineRunDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSciencePipelineRunHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataSciencePipelineRunHelperGen, self
        ).get_possible_entity_types() + [
            "pipelinerun",
            "pipelineruns",
            "dataSciencepipelinerun",
            "dataSciencepipelineruns",
            "pipelinerunresource",
            "pipelinerunsresource",
            "datascience",
        ]

    def get_module_resource_id_param(self):
        return "pipeline_run_id"

    def get_module_resource_id(self):
        return self.module.params.get("pipeline_run_id")

    def get_get_fn(self):
        return self.client.get_pipeline_run

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_pipeline_run, pipeline_run_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pipeline_run,
            pipeline_run_id=self.module.params.get("pipeline_run_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["pipeline_id", "display_name"]

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
            self.client.list_pipeline_runs, **kwargs
        )

    def get_create_model_class(self):
        return CreatePipelineRunDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_pipeline_run,
            call_fn_args=(),
            call_fn_kwargs=dict(create_pipeline_run_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdatePipelineRunDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_pipeline_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pipeline_run_id=self.module.params.get("pipeline_run_id"),
                update_pipeline_run_details=update_details,
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
            call_fn=self.client.delete_pipeline_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                pipeline_run_id=self.module.params.get("pipeline_run_id"),
                delete_related_job_runs=self.module.params.get(
                    "delete_related_job_runs"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataSciencePipelineRunHelperCustom = get_custom_class(
    "DataSciencePipelineRunHelperCustom"
)


class ResourceHelper(
    DataSciencePipelineRunHelperCustom, DataSciencePipelineRunHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
            pipeline_id=dict(type="str"),
            configuration_override_details=dict(
                type="dict",
                options=dict(
                    type=dict(type="str", required=True, choices=["DEFAULT"]),
                    maximum_runtime_in_minutes=dict(type="int"),
                    environment_variables=dict(type="dict"),
                    command_line_arguments=dict(type="str"),
                ),
            ),
            log_configuration_override_details=dict(
                type="dict",
                options=dict(
                    enable_logging=dict(type="bool"),
                    enable_auto_log_creation=dict(type="bool"),
                    log_group_id=dict(type="str"),
                    log_id=dict(type="str"),
                ),
            ),
            step_override_details=dict(
                type="list",
                elements="dict",
                options=dict(
                    step_name=dict(type="str", required=True),
                    step_configuration_details=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            maximum_runtime_in_minutes=dict(type="int"),
                            environment_variables=dict(type="dict"),
                            command_line_arguments=dict(type="str"),
                        ),
                    ),
                ),
            ),
            system_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            pipeline_run_id=dict(aliases=["id"], type="str"),
            delete_related_job_runs=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="pipeline_run",
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
