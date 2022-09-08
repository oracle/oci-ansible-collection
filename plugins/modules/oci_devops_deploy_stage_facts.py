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
module: oci_devops_deploy_stage_facts
short_description: Fetches details about one or multiple DeployStage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DeployStage resources in Oracle Cloud Infrastructure
    - Retrieves a list of deployment stages.
    - If I(deploy_stage_id) is specified, the details of a single DeployStage will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    deploy_stage_id:
        description:
            - Unique stage identifier.
            - Required to get a specific deploy_stage.
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
    lifecycle_state:
        description:
            - A filter to return only deployment stages that matches the given lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific deploy_stage
  oci_devops_deploy_stage_facts:
    # required
    deploy_stage_id: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"

- name: List deploy_stages
  oci_devops_deploy_stage_facts:

    # optional
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
deploy_stages:
    description:
        - List of DeployStage resources
    returned: on success
    type: complex
    contains:
        deploy_environment_id_a:
            description:
                - First compute instance group environment OCID for deployment.
                - Returned for get operation
            returned: on success
            type: str
            sample: deploy_environment_id_a_example
        deploy_environment_id_b:
            description:
                - Second compute instance group environment OCID for deployment.
                - Returned for get operation
            returned: on success
            type: str
            sample: deploy_environment_id_b_example
        compute_instance_group_blue_green_deployment_deploy_stage_id:
            description:
                - The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupbluegreendeploymentdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        compute_instance_group_canary_traffic_shift_deploy_stage_id:
            description:
                - A compute instance group canary traffic shift stage OCID for load balancer.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupcanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        test_load_balancer_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                load_balancer_id:
                    description:
                        - The OCID of the load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                listener_name:
                    description:
                        - Name of the load balancer listener.
                    returned: on success
                    type: str
                    sample: listener_name_example
                backend_port:
                    description:
                        - Listen port for the backend server.
                    returned: on success
                    type: int
                    sample: 56
        production_load_balancer_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                load_balancer_id:
                    description:
                        - The OCID of the load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                listener_name:
                    description:
                        - Name of the load balancer listener.
                    returned: on success
                    type: str
                    sample: listener_name_example
                backend_port:
                    description:
                        - Listen port for the backend server.
                    returned: on success
                    type: int
                    sample: 56
        compute_instance_group_canary_deploy_stage_id:
            description:
                - The OCID of an upstream compute instance group canary deployment stage ID in this pipeline.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupcanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        compute_instance_group_deploy_environment_id:
            description:
                - A compute instance group environment OCID for Canary deployment.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_spec_deploy_artifact_id:
            description:
                - The OCID of the artifact that contains the deployment specification.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids:
            description:
                - The list of file artifact OCIDs to deploy.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        failure_policy:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                failure_count:
                    description:
                        - The threshold count of failed instances in the group, which when reached or exceeded sets the stage as Failed.
                    returned: on success
                    type: int
                    sample: 56
                policy_type:
                    description:
                        - Specifies if the failure instance size is given by absolute number or by percentage.
                    returned: on success
                    type: str
                    sample: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT
                failure_percentage:
                    description:
                        - The failure percentage threshold, which when reached or exceeded sets the stage as Failed. Percentage is computed as the ceiling value
                          of the number of failed instances over the total count of the instances in the group.
                    returned: on success
                    type: int
                    sample: 56
        docker_image_deploy_artifact_id:
            description:
                - A Docker image artifact OCID.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        config:
            description:
                - User provided key and value pair configuration, which is assigned through constants or parameter.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        max_memory_in_mbs:
            description:
                - Maximum usable memory for the Function (in MB).
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        function_timeout_in_seconds:
            description:
                - Timeout for execution of the Function. Value in seconds.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        function_deploy_environment_id:
            description:
                - Function environment OCID.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_id:
            description:
                - Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage's execution.
                  If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace
                  the placeholders in the artifact content.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        is_async:
            description:
                - A boolean flag specifies whether this stage executes asynchronously.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        is_validation_enabled:
            description:
                - A boolean flag specifies whether the invoked function must be validated.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        blue_backend_ips:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - The IP address of the backend server. A server could be a compute instance or a load balancer.
                    returned: on success
                    type: list
                    sample: []
        green_backend_ips:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - The IP address of the backend server. A server could be a compute instance or a load balancer.
                    returned: on success
                    type: list
                    sample: []
        traffic_shift_target:
            description:
                - Specifies the target or destination backend set.
                - Returned for get operation
            returned: on success
            type: str
            sample: AUTO_SELECT
        load_balancer_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                load_balancer_id:
                    description:
                        - The OCID of the load balancer.
                    returned: on success
                    type: str
                    sample: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
                listener_name:
                    description:
                        - Name of the load balancer listener.
                    returned: on success
                    type: str
                    sample: listener_name_example
                backend_port:
                    description:
                        - Listen port for the backend server.
                    returned: on success
                    type: int
                    sample: 56
        blue_green_strategy:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                strategy_type:
                    description:
                        - Blue-Green strategy type.
                    returned: on success
                    type: str
                    sample: NGINX_BLUE_GREEN_STRATEGY
                namespace_a:
                    description:
                        - Namespace A for deployment.
                    returned: on success
                    type: str
                    sample: namespace_a_example
                namespace_b:
                    description:
                        - Namespace B for deployment.
                    returned: on success
                    type: str
                    sample: namespace_b_example
                ingress_name:
                    description:
                        - Name of the Ingress resource.
                    returned: on success
                    type: str
                    sample: ingress_name_example
        oke_blue_green_deploy_stage_id:
            description:
                - The OCID of the upstream OKE blue-green deployment stage in this pipeline.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.okebluegreendeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        oke_canary_traffic_shift_deploy_stage_id:
            description:
                - The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.okecanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        approval_policy:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                approval_policy_type:
                    description:
                        - Approval policy type.
                    returned: on success
                    type: str
                    sample: COUNT_BASED_APPROVAL
                number_of_approvals_required:
                    description:
                        - A minimum number of approvals required for stage to proceed.
                    returned: on success
                    type: int
                    sample: 56
        canary_strategy:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                strategy_type:
                    description:
                        - Canary strategy type.
                    returned: on success
                    type: str
                    sample: NGINX_CANARY_STRATEGY
                namespace:
                    description:
                        - Canary namespace to be used for Kubernetes canary deployment.
                    returned: on success
                    type: str
                    sample: namespace_example
                ingress_name:
                    description:
                        - Name of the Ingress resource.
                    returned: on success
                    type: str
                    sample: ingress_name_example
        oke_canary_deploy_stage_id:
            description:
                - The OCID of an upstream OKE canary deployment stage in this pipeline.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.okecanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        rollout_policy:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                batch_count:
                    description:
                        - The number that will be used to determine how many instances will be deployed concurrently.
                    returned: on success
                    type: int
                    sample: 56
                policy_type:
                    description:
                        - The type of policy used for rolling out a deployment stage.
                    returned: on success
                    type: str
                    sample: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT
                batch_delay_in_seconds:
                    description:
                        - The duration of delay between batch rollout. The default delay is 1 minute.
                    returned: on success
                    type: int
                    sample: 56
                batch_percentage:
                    description:
                        - The percentage that will be used to determine how many instances will be deployed concurrently.
                    returned: on success
                    type: int
                    sample: 56
                ramp_limit_percent:
                    description:
                        - Indicates the criteria to stop.
                    returned: on success
                    type: float
                    sample: 3.4
        kubernetes_manifest_deploy_artifact_ids:
            description:
                - List of Kubernetes manifest artifact OCIDs
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        oke_cluster_deploy_environment_id:
            description:
                - Kubernetes cluster environment OCID for deployment.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        helm_chart_deploy_artifact_id:
            description:
                - Helm chart artifact OCID.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        values_artifact_ids:
            description:
                - List of values.yaml file artifact OCIDs.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        release_name:
            description:
                - Release name of the Helm chart.
                - Returned for get operation
            returned: on success
            type: str
            sample: release_name_example
        namespace:
            description:
                - Default namespace to be used for Kubernetes deployment when not specified in the manifest.
                - Returned for get operation
            returned: on success
            type: str
            sample: namespace_example
        timeout_in_seconds:
            description:
                - Time to wait for execution of a helm stage. Defaults to 300 seconds.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        rollback_policy:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                policy_type:
                    description:
                        - Specifies type of the deployment stage rollback policy.
                    returned: on success
                    type: str
                    sample: AUTOMATED_STAGE_ROLLBACK_POLICY
        wait_criteria:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                wait_type:
                    description:
                        - Wait criteria type.
                    returned: on success
                    type: str
                    sample: ABSOLUTE_WAIT
                wait_duration:
                    description:
                        - The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can
                          be up to 2 days.
                    returned: on success
                    type: str
                    sample: wait_duration_example
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the deployment stage.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
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
        deploy_stage_type:
            description:
                - Deployment stage type.
            returned: on success
            type: str
            sample: WAIT
        time_created:
            description:
                - Time the deployment stage was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the deployment stage was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the deployment stage.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        deploy_stage_predecessor_collection:
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
                                - The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's OCID.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
        "deploy_environment_id_a": "deploy_environment_id_a_example",
        "deploy_environment_id_b": "deploy_environment_id_b_example",
        "compute_instance_group_blue_green_deployment_deploy_stage_id": "ocid1.computeinstancegroupbluegreendeploymentdeploystage.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_instance_group_canary_traffic_shift_deploy_stage_id": "ocid1.computeinstancegroupcanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx",
        "test_load_balancer_config": {
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "listener_name": "listener_name_example",
            "backend_port": 56
        },
        "production_load_balancer_config": {
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "listener_name": "listener_name_example",
            "backend_port": 56
        },
        "compute_instance_group_canary_deploy_stage_id": "ocid1.computeinstancegroupcanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_instance_group_deploy_environment_id": "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "deployment_spec_deploy_artifact_id": "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_artifact_ids": [],
        "failure_policy": {
            "failure_count": 56,
            "policy_type": "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT",
            "failure_percentage": 56
        },
        "docker_image_deploy_artifact_id": "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "config": {},
        "max_memory_in_mbs": 56,
        "function_timeout_in_seconds": 56,
        "function_deploy_environment_id": "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "is_async": true,
        "is_validation_enabled": true,
        "blue_backend_ips": {
            "items": []
        },
        "green_backend_ips": {
            "items": []
        },
        "traffic_shift_target": "AUTO_SELECT",
        "load_balancer_config": {
            "load_balancer_id": "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx",
            "listener_name": "listener_name_example",
            "backend_port": 56
        },
        "blue_green_strategy": {
            "strategy_type": "NGINX_BLUE_GREEN_STRATEGY",
            "namespace_a": "namespace_a_example",
            "namespace_b": "namespace_b_example",
            "ingress_name": "ingress_name_example"
        },
        "oke_blue_green_deploy_stage_id": "ocid1.okebluegreendeploystage.oc1..xxxxxxEXAMPLExxxxxx",
        "oke_canary_traffic_shift_deploy_stage_id": "ocid1.okecanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx",
        "approval_policy": {
            "approval_policy_type": "COUNT_BASED_APPROVAL",
            "number_of_approvals_required": 56
        },
        "canary_strategy": {
            "strategy_type": "NGINX_CANARY_STRATEGY",
            "namespace": "namespace_example",
            "ingress_name": "ingress_name_example"
        },
        "oke_canary_deploy_stage_id": "ocid1.okecanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx",
        "rollout_policy": {
            "batch_count": 56,
            "policy_type": "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT",
            "batch_delay_in_seconds": 56,
            "batch_percentage": 56,
            "ramp_limit_percent": 3.4
        },
        "kubernetes_manifest_deploy_artifact_ids": [],
        "oke_cluster_deploy_environment_id": "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx",
        "helm_chart_deploy_artifact_id": "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "values_artifact_ids": [],
        "release_name": "release_name_example",
        "namespace": "namespace_example",
        "timeout_in_seconds": 56,
        "rollback_policy": {
            "policy_type": "AUTOMATED_STAGE_ROLLBACK_POLICY"
        },
        "wait_criteria": {
            "wait_type": "ABSOLUTE_WAIT",
            "wait_duration": "wait_duration_example"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_pipeline_id": "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_stage_type": "WAIT",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "deploy_stage_predecessor_collection": {
            "items": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeployStageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "deploy_stage_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_stage,
            deploy_stage_id=self.module.params.get("deploy_stage_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "deploy_pipeline_id",
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_deploy_stages, **optional_kwargs
        )


DeployStageFactsHelperCustom = get_custom_class("DeployStageFactsHelperCustom")


class ResourceFactsHelper(DeployStageFactsHelperCustom, DeployStageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deploy_stage_id=dict(aliases=["id"], type="str"),
            deploy_pipeline_id=dict(type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="deploy_stage",
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

    module.exit_json(deploy_stages=result)


if __name__ == "__main__":
    main()
