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
module: oci_devops_deployment
short_description: Manage a Deployment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a Deployment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new deployment.
version_added: "2.9"
author: Oracle (@oracle)
options:
    deploy_pipeline_id:
        description:
            - The OCID of a pipeline.
            - Required for create using I(state=present).
        type: str
    deployment_type:
        description:
            - Specifies type for this deployment.
        type: str
        choices:
            - "PIPELINE_REDEPLOYMENT"
            - "PIPELINE_DEPLOYMENT"
            - "SINGLE_STAGE_DEPLOYMENT"
        required: true
    display_name:
        description:
            - Deployment display name. Avoid entering confidential information.
            - Required for create, update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    previous_deployment_id:
        description:
            - Specifies the OCID of the previous deployment to be redeployed.
            - Applicable when deployment_type is 'PIPELINE_REDEPLOYMENT'
        type: str
    deployment_arguments:
        description:
            - ""
            - Applicable when deployment_type is one of ['PIPELINE_DEPLOYMENT', 'SINGLE_STAGE_DEPLOYMENT']
        type: dict
        suboptions:
            items:
                description:
                    - List of arguments provided at the time of deployment.
                    - Required when deployment_type is 'PIPELINE_DEPLOYMENT'
                type: list
                required: true
                suboptions:
                    name:
                        description:
                            - Name of the parameter (case-sensitive).
                            - Required when deployment_type is 'PIPELINE_DEPLOYMENT'
                        type: str
                        required: true
                    value:
                        description:
                            - value of the argument.
                            - Required when deployment_type is 'PIPELINE_DEPLOYMENT'
                        type: str
                        required: true
    deploy_artifact_override_arguments:
        description:
            - ""
            - Applicable when deployment_type is one of ['PIPELINE_DEPLOYMENT', 'SINGLE_STAGE_DEPLOYMENT']
        type: dict
        suboptions:
            items:
                description:
                    - List of artifact override arguments at the time of deployment.
                    - Required when deployment_type is 'PIPELINE_DEPLOYMENT'
                type: list
                required: true
                suboptions:
                    deploy_artifact_id:
                        description:
                            - The OCID of the artifact to which this parameter applies.
                            - Required when deployment_type is 'PIPELINE_DEPLOYMENT'
                        type: str
                        required: true
                    name:
                        description:
                            - Name of the parameter (case-sensitive).
                            - Required when deployment_type is 'PIPELINE_DEPLOYMENT'
                        type: str
                        required: true
                    value:
                        description:
                            - Value of the parameter.
                            - Required when deployment_type is 'PIPELINE_DEPLOYMENT'
                        type: str
                        required: true
    deploy_stage_id:
        description:
            - Specifies the OCID of the stage to be redeployed.
            - Applicable when deployment_type is 'SINGLE_STAGE_DEPLOYMENT'
        type: str
    deployment_id:
        description:
            - Unique deployment identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Deployment.
            - Use I(state=present) to create or update a Deployment.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deployment
  oci_devops_deployment:
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_type: SINGLE_STAGE_DEPLOYMENT

- name: Update deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_deployment:
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_type: SINGLE_STAGE_DEPLOYMENT
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deployment
  oci_devops_deployment:
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deployment_type: SINGLE_STAGE_DEPLOYMENT
    display_name: display_name_example
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
deployment:
    description:
        - Details of the Deployment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        deploy_pipeline_artifacts:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                deploy_artifact_id:
                    description:
                        - The OCID of an artifact
                    returned: on success
                    type: string
                    sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Display name of the artifact. Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                deploy_pipeline_stages:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        deploy_stage_id:
                            description:
                                - The OCID of a stage
                            returned: on success
                            type: string
                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - Display name of the stage. Avoid entering confidential information.
                            returned: on success
                            type: string
                            sample: display_name_example
        deploy_pipeline_environments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                deploy_environment_id:
                    description:
                        - The OCID of an Environment
                    returned: on success
                    type: string
                    sample: "ocid1.deployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Display name of the environment. Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                deploy_pipeline_stages:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        deploy_stage_id:
                            description:
                                - The OCID of a stage
                            returned: on success
                            type: string
                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - Display name of the stage. Avoid entering confidential information.
                            returned: on success
                            type: string
                            sample: display_name_example
        deployment_type:
            description:
                - Specifies type of Deployment
            returned: on success
            type: string
            sample: PIPELINE_DEPLOYMENT
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Deployment identifier which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        project_id:
            description:
                - The OCID of a project.
            returned: on success
            type: string
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id:
            description:
                - The OCID of a pipeline.
            returned: on success
            type: string
            sample: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Time the deployment was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - Time the deployment was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the deployment.
            returned: on success
            type: string
            sample: ACCEPTED
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        deployment_arguments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of the parameter (case-sensitive).
                    returned: on success
                    type: string
                    sample: name_example
                value:
                    description:
                        - value of the argument.
                    returned: on success
                    type: string
                    sample: value_example
        deploy_artifact_override_arguments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                deploy_artifact_id:
                    description:
                        - The OCID of the artifact to which this parameter applies.
                    returned: on success
                    type: string
                    sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - Name of the parameter (case-sensitive).
                    returned: on success
                    type: string
                    sample: name_example
                value:
                    description:
                        - Value of the parameter.
                    returned: on success
                    type: string
                    sample: value_example
        deployment_execution_progress:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_started:
                    description:
                        - Time the deployment is started. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_finished:
                    description:
                        - Time the deployment is finished. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                deploy_stage_execution_progress:
                    description:
                        - Map of stage OCIDs to deploy stage execution progress model.
                    returned: on success
                    type: complex
                    contains:
                        deploy_stage_display_name:
                            description:
                                - Stage display name. Avoid entering confidential information.
                            returned: on success
                            type: string
                            sample: deploy_stage_display_name_example
                        deploy_stage_type:
                            description:
                                - Deployment stage type.
                            returned: on success
                            type: string
                            sample: deploy_stage_type_example
                        deploy_stage_id:
                            description:
                                - The OCID of the stage.
                            returned: on success
                            type: string
                            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
                        time_started:
                            description:
                                - Time the stage started executing. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                            returned: on success
                            type: string
                            sample: 2013-10-20T19:20:30+01:00
                        time_finished:
                            description:
                                - Time the stage finished executing. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                            returned: on success
                            type: string
                            sample: 2013-10-20T19:20:30+01:00
                        status:
                            description:
                                - The current state of the stage.
                            returned: on success
                            type: string
                            sample: ACCEPTED
                        deploy_stage_predecessors:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                id:
                                    description:
                                        - The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's OCID.
                                    returned: on success
                                    type: string
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
                                    type: string
                                    sample: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
                                target_group:
                                    description:
                                        - Group for the target environment for example, the batch number for an Instance Group deployment.
                                    returned: on success
                                    type: string
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
                                            type: string
                                            sample: name_example
                                        state:
                                            description:
                                                - State of the step.
                                            returned: on success
                                            type: string
                                            sample: WAITING
                                        time_started:
                                            description:
                                                - Time when the step started.
                                            returned: on success
                                            type: string
                                            sample: 2013-10-20T19:20:30+01:00
                                        time_finished:
                                            description:
                                                - Time when the step finished.
                                            returned: on success
                                            type: string
                                            sample: 2013-10-20T19:20:30+01:00
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
                                            type: string
                                            sample: name_example
                                        state:
                                            description:
                                                - State of the step.
                                            returned: on success
                                            type: string
                                            sample: WAITING
                                        time_started:
                                            description:
                                                - Time when the step started.
                                            returned: on success
                                            type: string
                                            sample: 2013-10-20T19:20:30+01:00
                                        time_finished:
                                            description:
                                                - Time when the step finished.
                                            returned: on success
                                            type: string
                                            sample: 2013-10-20T19:20:30+01:00
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
                                    type: string
                                    sample: "ocid1.subject.oc1..xxxxxxEXAMPLExxxxxx"
                                action:
                                    description:
                                        - The action of the user on the DevOps deployment stage.
                                    returned: on success
                                    type: string
                                    sample: APPROVE
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
        previous_deployment_id:
            description:
                - Specifies the OCID of the previous deployment to be redeployed.
            returned: on success
            type: string
            sample: "ocid1.previousdeployment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_stage_id:
            description:
                - Specifies the OCID of the stage to be deployed.
            returned: on success
            type: string
            sample: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "deploy_pipeline_artifacts": {
            "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "deploy_pipeline_stages": {
                "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example"
            }
        },
        "deploy_pipeline_environments": {
            "deploy_environment_id": "ocid1.deployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "deploy_pipeline_stages": {
                "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example"
            }
        },
        "deployment_type": "PIPELINE_DEPLOYMENT",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_pipeline_id": "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example",
        "deployment_arguments": {
            "name": "name_example",
            "value": "value_example"
        },
        "deploy_artifact_override_arguments": {
            "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "value": "value_example"
        },
        "deployment_execution_progress": {
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_finished": "2013-10-20T19:20:30+01:00",
            "deploy_stage_execution_progress": {
                "deploy_stage_display_name": "deploy_stage_display_name_example",
                "deploy_stage_type": "deploy_stage_type_example",
                "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx",
                "time_started": "2013-10-20T19:20:30+01:00",
                "time_finished": "2013-10-20T19:20:30+01:00",
                "status": "ACCEPTED",
                "deploy_stage_predecessors": {
                    "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
                }],
                "approval_actions": [{
                    "subject_id": "ocid1.subject.oc1..xxxxxxEXAMPLExxxxxx",
                    "action": "APPROVE"
                }]
            }
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "previous_deployment_id": "ocid1.previousdeployment.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_stage_id": "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.devops import DevopsClient
    from oci.devops.models import CreateDeploymentDetails
    from oci.devops.models import UpdateDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeploymentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_module_resource_id_param(self):
        return "deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_id")

    def get_get_fn(self):
        return self.client.get_deployment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["deploy_pipeline_id", "display_name"]

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
            self.client.list_deployments, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeploymentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deployment_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDeploymentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                update_deployment_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


DeploymentHelperCustom = get_custom_class("DeploymentHelperCustom")


class ResourceHelper(DeploymentHelperCustom, DeploymentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            deploy_pipeline_id=dict(type="str"),
            deployment_type=dict(
                type="str",
                required=True,
                choices=[
                    "PIPELINE_REDEPLOYMENT",
                    "PIPELINE_DEPLOYMENT",
                    "SINGLE_STAGE_DEPLOYMENT",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            previous_deployment_id=dict(type="str"),
            deployment_arguments=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    )
                ),
            ),
            deploy_artifact_override_arguments=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            deploy_artifact_id=dict(type="str", required=True),
                            name=dict(type="str", required=True),
                            value=dict(type="str", required=True),
                        ),
                    )
                ),
            ),
            deploy_stage_id=dict(type="str"),
            deployment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment",
        service_client_class=DevopsClient,
        namespace="devops",
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
