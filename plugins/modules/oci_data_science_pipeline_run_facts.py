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
module: oci_data_science_pipeline_run_facts
short_description: Fetches details about one or multiple PipelineRun resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PipelineRun resources in Oracle Cloud Infrastructure
    - Returns a list of PipelineRuns.
    - If I(pipeline_run_id) is specified, the details of a single PipelineRun will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    pipeline_run_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline run.
            - Required to get a specific pipeline_run.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple pipeline_runs.
        type: str
    pipeline_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the pipeline.
        type: str
    display_name:
        description:
            - <b>Filter</b> results by its user-friendly name.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - The current state of the PipelineRun.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "FAILED"
            - "SUCCEEDED"
            - "CANCELING"
            - "CANCELED"
            - "DELETING"
            - "DELETED"
    created_by:
        description:
            - <b>Filter</b> results by the L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the user who created the
              resource.
        type: str
    sort_order:
        description:
            - Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the field to sort by. Accepts only one field.
              By default, when you sort by `timeAccepted`, the results are shown
              in descending order. When you sort by `displayName`, the results are
              shown in ascending order. Sort order for the `displayName` field is case sensitive.
        type: str
        choices:
            - "timeAccepted"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific pipeline_run
  oci_data_science_pipeline_run_facts:
    # required
    pipeline_run_id: "ocid1.pipelinerun.oc1..xxxxxxEXAMPLExxxxxx"

- name: List pipeline_runs
  oci_data_science_pipeline_run_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    pipeline_id: "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: ACCEPTED
    created_by: created_by_example
    sort_order: ASC
    sort_by: timeAccepted

"""

RETURN = """
pipeline_runs:
    description:
        - List of PipelineRun resources
    returned: on success
    type: complex
    contains:
        configuration_details:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
        time_finished:
            description:
                - The date and time the pipeline run request was finished in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the pipeline run was updated in the timestamp format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
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
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_accepted": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_finished": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "pipeline_id": "ocid1.pipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.data_science import DataScienceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataSciencePipelineRunFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "pipeline_run_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pipeline_run,
            pipeline_run_id=self.module.params.get("pipeline_run_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "pipeline_id",
            "display_name",
            "lifecycle_state",
            "created_by",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_pipeline_runs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DataSciencePipelineRunFactsHelperCustom = get_custom_class(
    "DataSciencePipelineRunFactsHelperCustom"
)


class ResourceFactsHelper(
    DataSciencePipelineRunFactsHelperCustom, DataSciencePipelineRunFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            pipeline_run_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            pipeline_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "FAILED",
                    "SUCCEEDED",
                    "CANCELING",
                    "CANCELED",
                    "DELETING",
                    "DELETED",
                ],
            ),
            created_by=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeAccepted", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="pipeline_run",
        service_client_class=DataScienceClient,
        namespace="data_science",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(pipeline_runs=result)


if __name__ == "__main__":
    main()
