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
module: oci_devops_deployment_facts
short_description: Fetches details about one or multiple Deployment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Deployment resources in Oracle Cloud Infrastructure
    - Returns a list of deployments.
    - If I(deployment_id) is specified, the details of a single Deployment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    deployment_id:
        description:
            - Unique deployment identifier.
            - Required to get a specific deployment.
        type: str
        aliases: ["id"]
    deploy_pipeline_id:
        description:
            - The ID of the parent pipeline.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
    project_id:
        description:
            - unique project identifier
        type: str
    lifecycle_state:
        description:
            - A filter to return only Deployments that matches the given lifecycleState.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "FAILED"
            - "SUCCEEDED"
            - "CANCELING"
            - "CANCELED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use. Use either ascending or descending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is
              ascending. If no value is specified, then the default time created value is considered.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    time_created_less_than:
        description:
            - "Search for DevOps resources that were created before a specific date. Specifying this parameter corresponding to `timeCreatedLessThan` parameter
              will retrieve all assessments created before the specified created date, in \\"YYYY-MM-ddThh:mmZ\\" format with a Z offset, as defined by
              L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)."
        type: str
    time_created_greater_than_or_equal_to:
        description:
            - "Search for DevOps resources that were created after a specific date. Specifying this parameter corresponding to `timeCreatedGreaterThanOrEqualTo`
              parameter will retrieve all security assessments created after the specified created date, in \\"YYYY-MM-ddThh:mmZ\\" format with a Z offset, as
              defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339)."
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific deployment
  oci_devops_deployment_facts:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List deployments
  oci_devops_deployment_facts:

    # optional
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACCEPTED
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated
    time_created_less_than: 2013-10-20T19:20:30+01:00
    time_created_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00

"""

RETURN = """
deployments:
    description:
        - List of Deployment resources
    returned: on success
    type: complex
    contains:
        deploy_pipeline_artifacts:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of all artifacts used in the pipeline.
                    returned: on success
                    type: complex
                    contains:
                        deploy_artifact_id:
                            description:
                                - The OCID of an artifact
                            returned: on success
                            type: str
                            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - Display name of the artifact. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
                        deploy_pipeline_stages:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of stages.
                                    returned: on success
                                    type: complex
                                    contains:
                                        deploy_stage_id:
                                            description:
                                                - The OCID of a stage
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                                        display_name:
                                            description:
                                                - Display name of the stage. Avoid entering confidential information.
                                            returned: on success
                                            type: str
                                            sample: display_name_example
        deploy_pipeline_environments:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of all environments used in the pipeline.
                    returned: on success
                    type: complex
                    contains:
                        deploy_environment_id:
                            description:
                                - The OCID of an Environment
                            returned: on success
                            type: str
                            sample: "ocid1.deployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - Display name of the environment. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: display_name_example
                        deploy_pipeline_stages:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of stages.
                                    returned: on success
                                    type: complex
                                    contains:
                                        deploy_stage_id:
                                            description:
                                                - The OCID of a stage
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                                        display_name:
                                            description:
                                                - Display name of the stage. Avoid entering confidential information.
                                            returned: on success
                                            type: str
                                            sample: display_name_example
        deployment_execution_progress:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                time_started:
                    description:
                        - Time the deployment is started. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_finished:
                    description:
                        - Time the deployment is finished. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                deploy_stage_execution_progress:
                    description:
                        - Map of stage OCIDs to deploy stage execution progress model.
                    returned: on success
                    type: complex
                    contains:
                        environment_id:
                            description:
                                - The OCID of the environment where the artifacts were deployed.
                            returned: on success
                            type: str
                            sample: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
                        approval_actions:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                subject_id:
                                    description:
                                        - The subject ID of the user who approves or disapproves a DevOps deployment stage.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.subject.oc1..xxxxxxEXAMPLExxxxxx"
                                action:
                                    description:
                                        - The action of the user on the DevOps deployment stage.
                                    returned: on success
                                    type: str
                                    sample: APPROVE
                                reason:
                                    description:
                                        - The reason for approving or rejecting the deployment.
                                    returned: on success
                                    type: str
                                    sample: reason_example
                        release_name:
                            description:
                                - Release name of the Helm chart.
                            returned: on success
                            type: str
                            sample: release_name_example
                        chart_url:
                            description:
                                - The URL of an OCIR repository.
                            returned: on success
                            type: str
                            sample: chart_url_example
                        version:
                            description:
                                - The version of the helm chart stored in OCIR repository.
                            returned: on success
                            type: str
                            sample: version_example
                        namespace:
                            description:
                                - Namespace either environment A or environment B where artifacts are deployed.
                            returned: on success
                            type: str
                            sample: namespace_example
                        deploy_stage_display_name:
                            description:
                                - Stage display name. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: deploy_stage_display_name_example
                        deploy_stage_type:
                            description:
                                - Deployment stage type.
                            returned: on success
                            type: str
                            sample: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT
                        deploy_stage_id:
                            description:
                                - The OCID of the stage.
                            returned: on success
                            type: str
                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                        time_started:
                            description:
                                - Time the stage started executing. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_finished:
                            description:
                                - Time the stage finished executing. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        status:
                            description:
                                - The current state of the stage.
                            returned: on success
                            type: str
                            sample: ACCEPTED
                        deploy_stage_predecessors:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - A list of stage predecessors for a stage.
                                    returned: on success
                                    type: complex
                                    contains:
                                        id:
                                            description:
                                                - The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the
                                                  pipeline's OCID.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        deploy_stage_execution_progress_details:
                            description:
                                - Details about stage execution for all the target environments.
                            returned: on success
                            type: complex
                            contains:
                                target_id:
                                    description:
                                        - The function ID, instance ID or the cluster ID. For Wait stage it will be the stage ID.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
                                target_group:
                                    description:
                                        - Group for the target environment for example, the batch number for an Instance Group deployment.
                                    returned: on success
                                    type: str
                                    sample: target_group_example
                                steps:
                                    description:
                                        - Details about all the steps for one target environment.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - Name of the step.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        state:
                                            description:
                                                - State of the step.
                                            returned: on success
                                            type: str
                                            sample: WAITING
                                        time_started:
                                            description:
                                                - Time when the step started.
                                            returned: on success
                                            type: str
                                            sample: "2013-10-20T19:20:30+01:00"
                                        time_finished:
                                            description:
                                                - Time when the step finished.
                                            returned: on success
                                            type: str
                                            sample: "2013-10-20T19:20:30+01:00"
                                rollback_steps:
                                    description:
                                        - Details about all the rollback steps for one target environment.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - Name of the step.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        state:
                                            description:
                                                - State of the step.
                                            returned: on success
                                            type: str
                                            sample: WAITING
                                        time_started:
                                            description:
                                                - Time when the step started.
                                            returned: on success
                                            type: str
                                            sample: "2013-10-20T19:20:30+01:00"
                                        time_finished:
                                            description:
                                                - Time when the step finished.
                                            returned: on success
                                            type: str
                                            sample: "2013-10-20T19:20:30+01:00"
        previous_deployment_id:
            description:
                - Specifies the OCID of the previous deployment to be redeployed.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.previousdeployment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_id:
            description:
                - Specifies the OCID of the stage to be deployed.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_type:
            description:
                - Specifies type of deployment.
            returned: on success
            type: str
            sample: PIPELINE_DEPLOYMENT
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Deployment identifier which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        project_id:
            description:
                - The OCID of a project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id:
            description:
                - The OCID of a pipeline.
            returned: on success
            type: str
            sample: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Time the deployment was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the deployment was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the deployment.
            returned: on success
            type: str
            sample: ACCEPTED
        deployment_arguments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of arguments provided at the time of deployment.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the parameter (case-sensitive).
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - value of the argument.
                            returned: on success
                            type: str
                            sample: value_example
        deploy_stage_override_arguments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of artifact override arguments at the time of deployment.
                    returned: on success
                    type: complex
                    contains:
                        deploy_stage_id:
                            description:
                                - The OCID of the stage.
                            returned: on success
                            type: str
                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                        name:
                            description:
                                - Name of the parameter (case-sensitive).
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - Value of the parameter.
                            returned: on success
                            type: str
                            sample: value_example
        deploy_artifact_override_arguments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of artifact override arguments at the time of deployment.
                    returned: on success
                    type: complex
                    contains:
                        deploy_artifact_id:
                            description:
                                - The OCID of the artifact to which this parameter applies.
                            returned: on success
                            type: str
                            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                        name:
                            description:
                                - Name of the parameter (case-sensitive).
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - Value of the parameter.
                            returned: on success
                            type: str
                            sample: value_example
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "deploy_pipeline_artifacts": {
            "items": [{
                "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "deploy_pipeline_stages": {
                    "items": [{
                        "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                        "display_name": "display_name_example"
                    }]
                }
            }]
        },
        "deploy_pipeline_environments": {
            "items": [{
                "deploy_environment_id": "ocid1.deployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "deploy_pipeline_stages": {
                    "items": [{
                        "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                        "display_name": "display_name_example"
                    }]
                }
            }]
        },
        "deployment_execution_progress": {
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_finished": "2013-10-20T19:20:30+01:00",
            "deploy_stage_execution_progress": {
                "environment_id": "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx",
                "approval_actions": [{
                    "subject_id": "ocid1.subject.oc1..xxxxxxEXAMPLExxxxxx",
                    "action": "APPROVE",
                    "reason": "reason_example"
                }],
                "release_name": "release_name_example",
                "chart_url": "chart_url_example",
                "version": "version_example",
                "namespace": "namespace_example",
                "deploy_stage_display_name": "deploy_stage_display_name_example",
                "deploy_stage_type": "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT",
                "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                "time_started": "2013-10-20T19:20:30+01:00",
                "time_finished": "2013-10-20T19:20:30+01:00",
                "status": "ACCEPTED",
                "deploy_stage_predecessors": {
                    "items": [{
                        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                    }]
                },
                "deploy_stage_execution_progress_details": [{
                    "target_id": "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx",
                    "target_group": "target_group_example",
                    "steps": [{
                        "name": "name_example",
                        "state": "WAITING",
                        "time_started": "2013-10-20T19:20:30+01:00",
                        "time_finished": "2013-10-20T19:20:30+01:00"
                    }],
                    "rollback_steps": [{
                        "name": "name_example",
                        "state": "WAITING",
                        "time_started": "2013-10-20T19:20:30+01:00",
                        "time_finished": "2013-10-20T19:20:30+01:00"
                    }]
                }]
            }
        },
        "previous_deployment_id": "ocid1.previousdeployment.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_type": "PIPELINE_DEPLOYMENT",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_pipeline_id": "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "deployment_arguments": {
            "items": [{
                "name": "name_example",
                "value": "value_example"
            }]
        },
        "deploy_stage_override_arguments": {
            "items": [{
                "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                "name": "name_example",
                "value": "value_example"
            }]
        },
        "deploy_artifact_override_arguments": {
            "items": [{
                "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                "name": "name_example",
                "value": "value_example"
            }]
        },
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
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsDeploymentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "deployment_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "deploy_pipeline_id",
            "compartment_id",
            "project_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
            "time_created_less_than",
            "time_created_greater_than_or_equal_to",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_deployments, **optional_kwargs
        )


DevopsDeploymentFactsHelperCustom = get_custom_class(
    "DevopsDeploymentFactsHelperCustom"
)


class ResourceFactsHelper(
    DevopsDeploymentFactsHelperCustom, DevopsDeploymentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deployment_id=dict(aliases=["id"], type="str"),
            deploy_pipeline_id=dict(type="str"),
            compartment_id=dict(type="str"),
            project_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "FAILED",
                    "SUCCEEDED",
                    "CANCELING",
                    "CANCELED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            time_created_less_than=dict(type="str"),
            time_created_greater_than_or_equal_to=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="deployment",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(deployments=result)


if __name__ == "__main__":
    main()
