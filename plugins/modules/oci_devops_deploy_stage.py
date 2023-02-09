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
module: oci_devops_deploy_stage
short_description: Manage a DeployStage resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DeployStage resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new deployment stage.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    oke_canary_deploy_stage_id:
        description:
            - The OCID of an upstream OKE canary deployment stage in this pipeline.
            - Required when deploy_stage_type is 'OKE_CANARY_TRAFFIC_SHIFT'
        type: str
    oke_blue_green_deploy_stage_id:
        description:
            - The OCID of the upstream OKE blue-green deployment stage in this pipeline.
            - Required when deploy_stage_type is 'OKE_BLUE_GREEN_TRAFFIC_SHIFT'
        type: str
    compute_instance_group_blue_green_deployment_deploy_stage_id:
        description:
            - The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.
            - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT'
        type: str
    blue_green_strategy:
        description:
            - ""
            - Required when deploy_stage_type is 'OKE_BLUE_GREEN_DEPLOYMENT'
        type: dict
        suboptions:
            strategy_type:
                description:
                    - Blue-Green strategy type.
                type: str
                choices:
                    - "NGINX_BLUE_GREEN_STRATEGY"
                required: true
            namespace_a:
                description:
                    - "Namespace A for deployment. Example: namespaceA - first Namespace name."
                type: str
                required: true
            namespace_b:
                description:
                    - "Namespace B for deployment. Example: namespaceB - second Namespace name."
                type: str
                required: true
            ingress_name:
                description:
                    - Name of the Ingress resource.
                type: str
                required: true
    canary_strategy:
        description:
            - ""
            - Required when deploy_stage_type is 'OKE_CANARY_DEPLOYMENT'
        type: dict
        suboptions:
            strategy_type:
                description:
                    - Canary strategy type.
                type: str
                choices:
                    - "NGINX_CANARY_STRATEGY"
                required: true
            namespace:
                description:
                    - "Canary namespace to be used for Kubernetes canary deployment. Example: canary - Name of the Canary namespace."
                type: str
                required: true
            ingress_name:
                description:
                    - Name of the Ingress resource.
                type: str
                required: true
    compute_instance_group_canary_deploy_stage_id:
        description:
            - A compute instance group canary stage OCID for load balancer.
            - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT'
        type: str
    compute_instance_group_canary_traffic_shift_deploy_stage_id:
        description:
            - A compute instance group canary traffic shift stage OCID for load balancer.
            - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL'
        type: str
    deploy_environment_id_a:
        description:
            - First compute instance group environment OCID for deployment.
            - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT'
        type: str
    deploy_environment_id_b:
        description:
            - Second compute instance group environment OCID for deployment.
            - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT'
        type: str
    production_load_balancer_config:
        description:
            - ""
            - Required when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT']
        type: dict
        suboptions:
            load_balancer_id:
                description:
                    - The OCID of the load balancer.
                    - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'
                type: str
                required: true
            listener_name:
                description:
                    - Name of the load balancer listener.
                    - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'
                type: str
                required: true
            backend_port:
                description:
                    - Listen port for the backend server.
                    - Applicable when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'
                type: int
    deploy_pipeline_id:
        description:
            - The OCID of a pipeline.
            - Required for create using I(state=present).
        type: str
    oke_canary_traffic_shift_deploy_stage_id:
        description:
            - The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.
            - Required when deploy_stage_type is 'OKE_CANARY_APPROVAL'
        type: str
    helm_chart_deploy_artifact_id:
        description:
            - Helm chart artifact OCID.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'OKE_HELM_CHART_DEPLOYMENT'
            - Required when deploy_stage_type is 'OKE_HELM_CHART_DEPLOYMENT'
        type: str
    values_artifact_ids:
        description:
            - List of values.yaml file artifact OCIDs.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'OKE_HELM_CHART_DEPLOYMENT'
        type: list
        elements: str
    release_name:
        description:
            - Default name of the chart instance. Must be unique within a Kubernetes namespace.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'OKE_HELM_CHART_DEPLOYMENT'
            - Required when deploy_stage_type is 'OKE_HELM_CHART_DEPLOYMENT'
        type: str
    compute_instance_group_deploy_environment_id:
        description:
            - A compute instance group environment OCID for Canary deployment.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT'
            - Required when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT']
        type: str
    container_config:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'SHELL'
            - Required when deploy_stage_type is 'SHELL'
        type: dict
        suboptions:
            container_config_type:
                description:
                    - Container configuration type.
                type: str
                choices:
                    - "CONTAINER_INSTANCE_CONFIG"
                required: true
            compartment_id:
                description:
                    - The OCID of the compartment where the ContainerInstance will be created.
                type: str
            availability_domain:
                description:
                    - Availability domain where the ContainerInstance will be created.
                type: str
            shape_name:
                description:
                    - The shape of the ContainerInstance. The shape determines the resources available to the ContainerInstance.
                type: str
                required: true
            shape_config:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the instance.
                        type: float
                        required: true
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the instance, in gigabytes.
                        type: float
            network_channel:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    network_channel_type:
                        description:
                            - Network channel type.
                        type: str
                        choices:
                            - "SERVICE_VNIC_CHANNEL"
                            - "PRIVATE_ENDPOINT_CHANNEL"
                        required: true
                    subnet_id:
                        description:
                            - The OCID of the subnet where private resources exist.
                        type: str
                        required: true
                    nsg_ids:
                        description:
                            - An array of network security group OCIDs.
                        type: list
                        elements: str
    command_spec_deploy_artifact_id:
        description:
            - The OCID of the artifact that contains the command specification.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'SHELL'
            - Required when deploy_stage_type is 'SHELL'
        type: str
    timeout_in_seconds:
        description:
            - Time to wait for execution of a shell stage. Defaults to 36000 seconds.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['SHELL', 'OKE_HELM_CHART_DEPLOYMENT']
        type: int
    oke_cluster_deploy_environment_id:
        description:
            - Kubernetes cluster environment OCID for deployment.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['OKE_DEPLOYMENT', 'OKE_HELM_CHART_DEPLOYMENT']
            - Required when deploy_stage_type is one of ['OKE_DEPLOYMENT', 'OKE_CANARY_DEPLOYMENT', 'OKE_HELM_CHART_DEPLOYMENT', 'OKE_BLUE_GREEN_DEPLOYMENT']
        type: str
    namespace:
        description:
            - Default namespace to be used for Kubernetes deployment when not specified in the manifest.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['OKE_DEPLOYMENT', 'OKE_HELM_CHART_DEPLOYMENT']
        type: str
    blue_backend_ips:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
            - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
        type: dict
        suboptions:
            items:
                description:
                    - The IP address of the backend server. A server could be a compute instance or a load balancer.
                    - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: list
                elements: str
    green_backend_ips:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
            - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
        type: dict
        suboptions:
            items:
                description:
                    - The IP address of the backend server. A server could be a compute instance or a load balancer.
                    - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: list
                elements: str
    traffic_shift_target:
        description:
            - "Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue
              Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to blue Backend IPs ser as per
              rolloutPolicy."
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
            - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
        type: str
    load_balancer_config:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'LOAD_BALANCER_TRAFFIC_SHIFT']
            - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
        type: dict
        suboptions:
            load_balancer_id:
                description:
                    - The OCID of the load balancer.
                    - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: str
                required: true
            listener_name:
                description:
                    - Name of the load balancer listener.
                    - Required when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: str
                required: true
            backend_port:
                description:
                    - Listen port for the backend server.
                    - Applicable when deploy_stage_type is 'LOAD_BALANCER_TRAFFIC_SHIFT'
                type: int
    rollback_policy:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'OKE_DEPLOYMENT', 'OKE_HELM_CHART_DEPLOYMENT',
              'LOAD_BALANCER_TRAFFIC_SHIFT']
        type: dict
        suboptions:
            policy_type:
                description:
                    - Specifies type of the deployment stage rollback policy.
                type: str
                choices:
                    - "NO_STAGE_ROLLBACK_POLICY"
                    - "AUTOMATED_STAGE_ROLLBACK_POLICY"
                required: true
    kubernetes_manifest_deploy_artifact_ids:
        description:
            - List of Kubernetes manifest artifact OCIDs.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['OKE_DEPLOYMENT', 'OKE_CANARY_DEPLOYMENT', 'OKE_BLUE_GREEN_DEPLOYMENT']
            - Required when deploy_stage_type is one of ['OKE_DEPLOYMENT', 'OKE_CANARY_DEPLOYMENT', 'OKE_BLUE_GREEN_DEPLOYMENT']
        type: list
        elements: str
    wait_criteria:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'WAIT'
            - Required when deploy_stage_type is 'WAIT'
        type: dict
        suboptions:
            wait_type:
                description:
                    - Wait criteria type.
                type: str
                choices:
                    - "ABSOLUTE_WAIT"
                required: true
            wait_duration:
                description:
                    - The absolute wait duration. An ISO 8601 formatted duration string. Minimum waitDuration should be 5 seconds. Maximum waitDuration can be
                      up to 2 days.
                type: str
                required: true
    approval_policy:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL', 'MANUAL_APPROVAL', 'OKE_CANARY_APPROVAL']
            - Required when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL', 'MANUAL_APPROVAL', 'OKE_CANARY_APPROVAL']
        type: dict
        suboptions:
            approval_policy_type:
                description:
                    - Approval policy type.
                type: str
                choices:
                    - "COUNT_BASED_APPROVAL"
                required: true
            number_of_approvals_required:
                description:
                    - A minimum number of approvals required for stage to proceed.
                type: int
                required: true
    failure_policy:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT']
        type: dict
        suboptions:
            failure_percentage:
                description:
                    - The failure percentage threshold, which when reached or exceeded sets the stage as Failed. Percentage is computed as the ceiling value of
                      the number of failed instances over the total count of the instances in the group.
                    - Required when policy_type is 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE'
                type: int
            policy_type:
                description:
                    - Specifies if the failure instance size is given by absolute number or by percentage.
                type: str
                choices:
                    - "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE"
                    - "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT"
                required: true
            failure_count:
                description:
                    - The threshold count of failed instances in the group, which when reached or exceeded sets the stage as Failed.
                    - Required when policy_type is 'COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT'
                type: int
    deployment_spec_deploy_artifact_id:
        description:
            - The OCID of the artifact that contains the deployment specification.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT',
              'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT']
            - Required when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT',
              'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT']
        type: str
    deploy_artifact_ids:
        description:
            - The list of file artifact OCIDs to deploy.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT',
              'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT']
        type: list
        elements: str
    test_load_balancer_config:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT']
        type: dict
        suboptions:
            load_balancer_id:
                description:
                    - The OCID of the load balancer.
                    - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'
                type: str
                required: true
            listener_name:
                description:
                    - Name of the load balancer listener.
                    - Required when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'
                type: str
                required: true
            backend_port:
                description:
                    - Listen port for the backend server.
                    - Applicable when deploy_stage_type is 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT'
                type: int
    docker_image_deploy_artifact_id:
        description:
            - A Docker image artifact OCID.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'DEPLOY_FUNCTION'
            - Required when deploy_stage_type is 'DEPLOY_FUNCTION'
        type: str
    config:
        description:
            - User provided key and value pair configuration, which is assigned through constants or parameter.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'DEPLOY_FUNCTION'
        type: dict
    max_memory_in_mbs:
        description:
            - Maximum usable memory for the Function (in MB).
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'DEPLOY_FUNCTION'
        type: int
    function_timeout_in_seconds:
        description:
            - Timeout for execution of the Function. Value in seconds.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'DEPLOY_FUNCTION'
        type: int
    rollout_policy:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT',
              'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT', 'OKE_CANARY_TRAFFIC_SHIFT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT',
              'LOAD_BALANCER_TRAFFIC_SHIFT']
            - Required when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT',
              'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT', 'OKE_CANARY_TRAFFIC_SHIFT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT',
              'LOAD_BALANCER_TRAFFIC_SHIFT']
        type: dict
        suboptions:
            ramp_limit_percent:
                description:
                    - Indicates the criteria to stop.
                    - Applicable when deploy_stage_type is 'OKE_CANARY_TRAFFIC_SHIFT'
                type: float
            batch_percentage:
                description:
                    - The percentage that will be used to determine how many instances will be deployed concurrently.
                    - Required when policy_type is 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE'
                type: int
            policy_type:
                description:
                    - The type of policy used for rolling out a deployment stage.
                type: str
                choices:
                    - "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE"
                    - "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT"
            batch_delay_in_seconds:
                description:
                    - Specifies delay in seconds between batches. The default delay is 1 minute.
                    - Applicable when deploy_stage_type is one of ['OKE_CANARY_TRAFFIC_SHIFT', 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE',
                      'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT']
                type: int
            batch_count:
                description:
                    - Specifies number of batches for this stage.
                    - Required when deploy_stage_type is one of ['OKE_CANARY_TRAFFIC_SHIFT', 'COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT']
                type: int
    description:
        description:
            - Optional description about the deployment stage.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - Deployment stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    deploy_stage_type:
        description:
            - Deployment stage type.
            - Required for create using I(state=present), update using I(state=present) with deploy_stage_id present.
        type: str
        choices:
            - "OKE_CANARY_TRAFFIC_SHIFT"
            - "OKE_BLUE_GREEN_TRAFFIC_SHIFT"
            - "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT"
            - "WAIT"
            - "LOAD_BALANCER_TRAFFIC_SHIFT"
            - "SHELL"
            - "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT"
            - "OKE_BLUE_GREEN_DEPLOYMENT"
            - "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT"
            - "INVOKE_FUNCTION"
            - "DEPLOY_FUNCTION"
            - "OKE_CANARY_DEPLOYMENT"
            - "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT"
            - "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL"
            - "OKE_HELM_CHART_DEPLOYMENT"
            - "MANUAL_APPROVAL"
            - "OKE_DEPLOYMENT"
            - "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT"
            - "OKE_CANARY_APPROVAL"
    deploy_stage_predecessor_collection:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT', 'OKE_BLUE_GREEN_TRAFFIC_SHIFT', 'SHELL',
              'OKE_DEPLOYMENT', 'DEPLOY_FUNCTION', 'OKE_CANARY_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT', 'OKE_HELM_CHART_DEPLOYMENT',
              'OKE_BLUE_GREEN_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT', 'OKE_CANARY_APPROVAL',
              'COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT', 'COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT', 'OKE_CANARY_TRAFFIC_SHIFT',
              'COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL', 'MANUAL_APPROVAL', 'LOAD_BALANCER_TRAFFIC_SHIFT', 'WAIT', 'INVOKE_FUNCTION']
        type: dict
        suboptions:
            items:
                description:
                    - A list of stage predecessors for a stage.
                    - Required when deploy_stage_type is 'OKE_CANARY_TRAFFIC_SHIFT'
                type: list
                elements: dict
                required: true
                suboptions:
                    id:
                        description:
                            - The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's OCID.
                            - Required when deploy_stage_type is 'OKE_CANARY_TRAFFIC_SHIFT'
                        type: str
                        required: true
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
    function_deploy_environment_id:
        description:
            - Function environment OCID.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is one of ['DEPLOY_FUNCTION', 'INVOKE_FUNCTION']
            - Required when deploy_stage_type is one of ['DEPLOY_FUNCTION', 'INVOKE_FUNCTION']
        type: str
    deploy_artifact_id:
        description:
            - Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage's execution.
              If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace the
              placeholders in the artifact content.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'INVOKE_FUNCTION'
        type: str
    is_async:
        description:
            - A boolean flag specifies whether this stage executes asynchronously.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'INVOKE_FUNCTION'
            - Required when deploy_stage_type is 'INVOKE_FUNCTION'
        type: bool
    is_validation_enabled:
        description:
            - A boolean flag specifies whether the invoked function should be validated.
            - This parameter is updatable.
            - Applicable when deploy_stage_type is 'INVOKE_FUNCTION'
            - Required when deploy_stage_type is 'INVOKE_FUNCTION'
        type: bool
    deploy_stage_id:
        description:
            - Unique stage identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DeployStage.
            - Use I(state=present) to create or update a DeployStage.
            - Use I(state=absent) to delete a DeployStage.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deploy_stage with deploy_stage_type = OKE_CANARY_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    oke_canary_deploy_stage_id: "ocid1.okecanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_CANARY_TRAFFIC_SHIFT

    # optional
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = OKE_BLUE_GREEN_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    oke_blue_green_deploy_stage_id: "ocid1.okebluegreendeploystage.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_BLUE_GREEN_TRAFFIC_SHIFT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    production_load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT

    # optional
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    test_load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = WAIT
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: WAIT

    # optional
    wait_criteria:
      # required
      wait_type: ABSOLUTE_WAIT
      wait_duration: wait_duration_example
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT

    # optional
    blue_backend_ips:
      # optional
      items: [ "items_example" ]
    green_backend_ips:
      # optional
      items: [ "items_example" ]
    traffic_shift_target: traffic_shift_target_example
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = SHELL
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: SHELL

    # optional
    container_config:
      # required
      container_config_type: CONTAINER_INSTANCE_CONFIG
      shape_name: shape_name_example
      shape_config:
        # required
        ocpus: 3.4

        # optional
        memory_in_gbs: 3.4
      network_channel:
        # required
        network_channel_type: SERVICE_VNIC_CHANNEL
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        nsg_ids: [ "nsg_ids_example" ]

        # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      availability_domain: Uocm:PHX-AD-1
    command_spec_deploy_artifact_id: "ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    timeout_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    compute_instance_group_blue_green_deployment_deploy_stage_id: "ocid1.computeinstancegroupbluegreendeploymentdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = OKE_BLUE_GREEN_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    blue_green_strategy:
      # required
      strategy_type: NGINX_BLUE_GREEN_STRATEGY
      namespace_a: namespace_a_example
      namespace_b: namespace_b_example
      ingress_name: ingress_name_example
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_BLUE_GREEN_DEPLOYMENT

    # optional
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT

    # optional
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    failure_policy:
      # required
      failure_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = INVOKE_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: INVOKE_FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    is_async: true
    is_validation_enabled: true

- name: Create deploy_stage with deploy_stage_type = DEPLOY_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: DEPLOY_FUNCTION

    # optional
    docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    config: null
    max_memory_in_mbs: 56
    function_timeout_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create deploy_stage with deploy_stage_type = OKE_CANARY_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    canary_strategy:
      # required
      strategy_type: NGINX_CANARY_STRATEGY
      namespace: namespace_example
      ingress_name: ingress_name_example
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_CANARY_DEPLOYMENT

    # optional
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    compute_instance_group_canary_deploy_stage_id: "ocid1.computeinstancegroupcanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT

    # optional
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL
  oci_devops_deploy_stage:
    # required
    compute_instance_group_canary_traffic_shift_deploy_stage_id: "ocid1.computeinstancegroupcanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = OKE_HELM_CHART_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_HELM_CHART_DEPLOYMENT

    # optional
    helm_chart_deploy_artifact_id: "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    values_artifact_ids: [ "values_artifact_ids_example" ]
    release_name: release_name_example
    timeout_in_seconds: 56
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = MANUAL_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: MANUAL_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = OKE_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_DEPLOYMENT

    # optional
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_environment_id_a: deploy_environment_id_a_example
    deploy_environment_id_b: deploy_environment_id_b_example
    production_load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT

    # optional
    failure_policy:
      # required
      failure_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    test_load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create deploy_stage with deploy_stage_type = OKE_CANARY_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_pipeline_id: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
    oke_canary_traffic_shift_deploy_stage_id: "ocid1.okecanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_CANARY_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = OKE_CANARY_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_CANARY_TRAFFIC_SHIFT

    # optional
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = OKE_BLUE_GREEN_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_BLUE_GREEN_TRAFFIC_SHIFT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT

    # optional
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    test_load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = WAIT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: WAIT

    # optional
    wait_criteria:
      # required
      wait_type: ABSOLUTE_WAIT
      wait_duration: wait_duration_example
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT

    # optional
    blue_backend_ips:
      # optional
      items: [ "items_example" ]
    green_backend_ips:
      # optional
      items: [ "items_example" ]
    traffic_shift_target: traffic_shift_target_example
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = SHELL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: SHELL

    # optional
    container_config:
      # required
      container_config_type: CONTAINER_INSTANCE_CONFIG
      shape_name: shape_name_example
      shape_config:
        # required
        ocpus: 3.4

        # optional
        memory_in_gbs: 3.4
      network_channel:
        # required
        network_channel_type: SERVICE_VNIC_CHANNEL
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        nsg_ids: [ "nsg_ids_example" ]

        # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      availability_domain: Uocm:PHX-AD-1
    command_spec_deploy_artifact_id: "ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    timeout_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = OKE_BLUE_GREEN_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_BLUE_GREEN_DEPLOYMENT

    # optional
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT

    # optional
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    failure_policy:
      # required
      failure_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = INVOKE_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: INVOKE_FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    is_async: true
    is_validation_enabled: true

- name: Update deploy_stage with deploy_stage_type = DEPLOY_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: DEPLOY_FUNCTION

    # optional
    docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    config: null
    max_memory_in_mbs: 56
    function_timeout_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update deploy_stage with deploy_stage_type = OKE_CANARY_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_CANARY_DEPLOYMENT

    # optional
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT

    # optional
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = OKE_HELM_CHART_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_HELM_CHART_DEPLOYMENT

    # optional
    helm_chart_deploy_artifact_id: "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    values_artifact_ids: [ "values_artifact_ids_example" ]
    release_name: release_name_example
    timeout_in_seconds: 56
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = MANUAL_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: MANUAL_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = OKE_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_DEPLOYMENT

    # optional
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT

    # optional
    failure_policy:
      # required
      failure_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    test_load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage with deploy_stage_type = OKE_CANARY_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_CANARY_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_CANARY_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_CANARY_TRAFFIC_SHIFT

    # optional
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_BLUE_GREEN_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_BLUE_GREEN_TRAFFIC_SHIFT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: >
    Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT

    # optional
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    test_load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = WAIT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: WAIT

    # optional
    wait_criteria:
      # required
      wait_type: ABSOLUTE_WAIT
      wait_duration: wait_duration_example
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = LOAD_BALANCER_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: LOAD_BALANCER_TRAFFIC_SHIFT

    # optional
    blue_backend_ips:
      # optional
      items: [ "items_example" ]
    green_backend_ips:
      # optional
      items: [ "items_example" ]
    traffic_shift_target: traffic_shift_target_example
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = SHELL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: SHELL

    # optional
    container_config:
      # required
      container_config_type: CONTAINER_INSTANCE_CONFIG
      shape_name: shape_name_example
      shape_config:
        # required
        ocpus: 3.4

        # optional
        memory_in_gbs: 3.4
      network_channel:
        # required
        network_channel_type: SERVICE_VNIC_CHANNEL
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        nsg_ids: [ "nsg_ids_example" ]

        # optional
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      availability_domain: Uocm:PHX-AD-1
    command_spec_deploy_artifact_id: "ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    timeout_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: >
    Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_BLUE_GREEN_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_BLUE_GREEN_DEPLOYMENT

    # optional
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: >
    Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with deploy_stage_type = COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT

    # optional
    compute_instance_group_deploy_environment_id: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    failure_policy:
      # required
      failure_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = INVOKE_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: INVOKE_FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    is_async: true
    is_validation_enabled: true

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = DEPLOY_FUNCTION
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: DEPLOY_FUNCTION

    # optional
    docker_image_deploy_artifact_id: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    config: null
    max_memory_in_mbs: 56
    function_timeout_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_deploy_environment_id: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_CANARY_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_stage_type: OKE_CANARY_DEPLOYMENT

    # optional
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: >
    Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT

    # optional
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: >
    Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with deploy_stage_type = COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_HELM_CHART_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_HELM_CHART_DEPLOYMENT

    # optional
    helm_chart_deploy_artifact_id: "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    values_artifact_ids: [ "values_artifact_ids_example" ]
    release_name: release_name_example
    timeout_in_seconds: 56
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = MANUAL_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: MANUAL_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_DEPLOYMENT

    # optional
    oke_cluster_deploy_environment_id: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    namespace: namespace_example
    rollback_policy:
      # required
      policy_type: NO_STAGE_ROLLBACK_POLICY
    kubernetes_manifest_deploy_artifact_ids: [ "kubernetes_manifest_deploy_artifact_ids_example" ]
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: >
    Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
    with deploy_stage_type = COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT

    # optional
    failure_policy:
      # required
      failure_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE
    deployment_spec_deploy_artifact_id: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    deploy_artifact_ids: [ "deploy_artifact_ids_example" ]
    test_load_balancer_config:
      # required
      load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
      listener_name: listener_name_example

      # optional
      backend_port: 56
    rollout_policy:
      # required
      batch_percentage: 56
      policy_type: COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE

      # optional
      batch_delay_in_seconds: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_stage_type = OKE_CANARY_APPROVAL
  oci_devops_deploy_stage:
    # required
    deploy_stage_type: OKE_CANARY_APPROVAL

    # optional
    approval_policy:
      # required
      approval_policy_type: COUNT_BASED_APPROVAL
      number_of_approvals_required: 56
    description: description_example
    display_name: display_name_example
    deploy_stage_predecessor_collection:
      # required
      items:
      - # required
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete deploy_stage
  oci_devops_deploy_stage:
    # required
    deploy_stage_id: "ocid1.deploystage.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete deploy_stage using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_deploy_stage:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
deploy_stage:
    description:
        - Details of the DeployStage resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        deploy_environment_id_a:
            description:
                - First compute instance group environment OCID for deployment.
            returned: on success
            type: str
            sample: deploy_environment_id_a_example
        deploy_environment_id_b:
            description:
                - Second compute instance group environment OCID for deployment.
            returned: on success
            type: str
            sample: deploy_environment_id_b_example
        compute_instance_group_blue_green_deployment_deploy_stage_id:
            description:
                - The OCID of the upstream compute instance group blue-green deployment stage in this pipeline.
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupbluegreendeploymentdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        compute_instance_group_canary_traffic_shift_deploy_stage_id:
            description:
                - A compute instance group canary traffic shift stage OCID for load balancer.
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupcanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        test_load_balancer_config:
            description:
                - ""
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
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupcanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        compute_instance_group_deploy_environment_id:
            description:
                - A compute instance group environment OCID for Canary deployment.
            returned: on success
            type: str
            sample: "ocid1.computeinstancegroupdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deployment_spec_deploy_artifact_id:
            description:
                - The OCID of the artifact that contains the deployment specification.
            returned: on success
            type: str
            sample: "ocid1.deploymentspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_ids:
            description:
                - The list of file artifact OCIDs to deploy.
            returned: on success
            type: list
            sample: []
        failure_policy:
            description:
                - ""
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
            returned: on success
            type: str
            sample: "ocid1.dockerimagedeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        config:
            description:
                - User provided key and value pair configuration, which is assigned through constants or parameter.
            returned: on success
            type: dict
            sample: {}
        max_memory_in_mbs:
            description:
                - Maximum usable memory for the Function (in MB).
            returned: on success
            type: int
            sample: 56
        function_timeout_in_seconds:
            description:
                - Timeout for execution of the Function. Value in seconds.
            returned: on success
            type: int
            sample: 56
        function_deploy_environment_id:
            description:
                - Function environment OCID.
            returned: on success
            type: str
            sample: "ocid1.functiondeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_id:
            description:
                - Optional artifact OCID. The artifact will be included in the body for the function invocation during the stage's execution.
                  If the DeployArtifact.argumentSubstituitionMode is set to SUBSTITUTE_PLACEHOLDERS, then the pipeline parameter values will be used to replace
                  the placeholders in the artifact content.
            returned: on success
            type: str
            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        is_async:
            description:
                - A boolean flag specifies whether this stage executes asynchronously.
            returned: on success
            type: bool
            sample: true
        is_validation_enabled:
            description:
                - A boolean flag specifies whether the invoked function must be validated.
            returned: on success
            type: bool
            sample: true
        blue_backend_ips:
            description:
                - ""
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
                - "Specifies the target or destination backend set. Example: BLUE - Traffic from the existing backends of managed Load Balance Listener to blue
                  Backend IPs, as per rolloutPolicy. GREEN - Traffic from the existing backends of managed Load Balance Listener to green Backend IPs as per
                  rolloutPolicy."
            returned: on success
            type: str
            sample: AUTO_SELECT
        load_balancer_config:
            description:
                - ""
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
                        - "Namespace A for deployment. Example: namespaceA - first Namespace name."
                    returned: on success
                    type: str
                    sample: namespace_a_example
                namespace_b:
                    description:
                        - "Namespace B for deployment. Example: namespaceB - second Namespace name."
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
            returned: on success
            type: str
            sample: "ocid1.okebluegreendeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        oke_canary_traffic_shift_deploy_stage_id:
            description:
                - The OCID of an upstream OKE canary deployment traffic shift stage in this pipeline.
            returned: on success
            type: str
            sample: "ocid1.okecanarytrafficshiftdeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        approval_policy:
            description:
                - ""
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
                        - "Canary namespace to be used for Kubernetes canary deployment. Example: canary - Name of the Canary namespace."
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
            returned: on success
            type: str
            sample: "ocid1.okecanarydeploystage.oc1..xxxxxxEXAMPLExxxxxx"
        rollout_policy:
            description:
                - ""
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
            returned: on success
            type: list
            sample: []
        oke_cluster_deploy_environment_id:
            description:
                - Kubernetes cluster environment OCID for deployment.
            returned: on success
            type: str
            sample: "ocid1.okeclusterdeployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
        helm_chart_deploy_artifact_id:
            description:
                - Helm chart artifact OCID.
            returned: on success
            type: str
            sample: "ocid1.helmchartdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        values_artifact_ids:
            description:
                - List of values.yaml file artifact OCIDs.
            returned: on success
            type: list
            sample: []
        release_name:
            description:
                - Release name of the Helm chart.
            returned: on success
            type: str
            sample: release_name_example
        namespace:
            description:
                - Default namespace to be used for Kubernetes deployment when not specified in the manifest.
            returned: on success
            type: str
            sample: namespace_example
        rollback_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                policy_type:
                    description:
                        - Specifies type of the deployment stage rollback policy.
                    returned: on success
                    type: str
                    sample: AUTOMATED_STAGE_ROLLBACK_POLICY
        container_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                container_config_type:
                    description:
                        - Container configuration type.
                    returned: on success
                    type: str
                    sample: CONTAINER_INSTANCE_CONFIG
                compartment_id:
                    description:
                        - The OCID of the compartment where the ContainerInstance will be created.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                availability_domain:
                    description:
                        - Availability domain where the ContainerInstance will be created.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                shape_name:
                    description:
                        - The shape of the ContainerInstance. The shape determines the resources available to the ContainerInstance.
                    returned: on success
                    type: str
                    sample: shape_name_example
                shape_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ocpus:
                            description:
                                - The total number of OCPUs available to the instance.
                            returned: on success
                            type: float
                            sample: 3.4
                        memory_in_gbs:
                            description:
                                - The total amount of memory available to the instance, in gigabytes.
                            returned: on success
                            type: float
                            sample: 3.4
                network_channel:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        network_channel_type:
                            description:
                                - Network channel type.
                            returned: on success
                            type: str
                            sample: PRIVATE_ENDPOINT_CHANNEL
                        subnet_id:
                            description:
                                - The OCID of the subnet where VNIC resources will be created for private endpoint.
                            returned: on success
                            type: str
                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                        nsg_ids:
                            description:
                                - An array of network security group OCIDs.
                            returned: on success
                            type: list
                            sample: []
        command_spec_deploy_artifact_id:
            description:
                - The OCID of the artifact that contains the command specification.
            returned: on success
            type: str
            sample: "ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx"
        timeout_in_seconds:
            description:
                - Time to wait for execution of a helm stage. Defaults to 300 seconds.
            returned: on success
            type: int
            sample: 56
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
        wait_criteria:
            description:
                - ""
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
    sample: {
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
        "rollback_policy": {
            "policy_type": "AUTOMATED_STAGE_ROLLBACK_POLICY"
        },
        "container_config": {
            "container_config_type": "CONTAINER_INSTANCE_CONFIG",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "availability_domain": "Uocm:PHX-AD-1",
            "shape_name": "shape_name_example",
            "shape_config": {
                "ocpus": 3.4,
                "memory_in_gbs": 3.4
            },
            "network_channel": {
                "network_channel_type": "PRIVATE_ENDPOINT_CHANNEL",
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
                "nsg_ids": []
            }
        },
        "command_spec_deploy_artifact_id": "ocid1.commandspecdeployartifact.oc1..xxxxxxEXAMPLExxxxxx",
        "timeout_in_seconds": 56,
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
        "system_tags": {},
        "wait_criteria": {
            "wait_type": "ABSOLUTE_WAIT",
            "wait_duration": "wait_duration_example"
        }
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
    from oci.devops import DevopsClient
    from oci.devops.models import CreateDeployStageDetails
    from oci.devops.models import UpdateDeployStageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsDeployStageHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DevopsDeployStageHelperGen, self).get_possible_entity_types() + [
            "devopsdeploystage",
            "devopsdeploystages",
            "devopsdevopsdeploystage",
            "devopsdevopsdeploystages",
            "devopsdeploystageresource",
            "devopsdeploystagesresource",
            "deploystage",
            "deploystages",
            "deploystageresource",
            "deploystagesresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "deploy_stage_id"

    def get_module_resource_id(self):
        return self.module.params.get("deploy_stage_id")

    def get_get_fn(self):
        return self.client.get_deploy_stage

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_stage, deploy_stage_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_stage,
            deploy_stage_id=self.module.params.get("deploy_stage_id"),
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
            self.client.list_deploy_stages, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeployStageDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deploy_stage_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeployStageDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_stage_id=self.module.params.get("deploy_stage_id"),
                update_deploy_stage_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deploy_stage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_stage_id=self.module.params.get("deploy_stage_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DevopsDeployStageHelperCustom = get_custom_class("DevopsDeployStageHelperCustom")


class ResourceHelper(DevopsDeployStageHelperCustom, DevopsDeployStageHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            oke_canary_deploy_stage_id=dict(type="str"),
            oke_blue_green_deploy_stage_id=dict(type="str"),
            compute_instance_group_blue_green_deployment_deploy_stage_id=dict(
                type="str"
            ),
            blue_green_strategy=dict(
                type="dict",
                options=dict(
                    strategy_type=dict(
                        type="str", required=True, choices=["NGINX_BLUE_GREEN_STRATEGY"]
                    ),
                    namespace_a=dict(type="str", required=True),
                    namespace_b=dict(type="str", required=True),
                    ingress_name=dict(type="str", required=True),
                ),
            ),
            canary_strategy=dict(
                type="dict",
                options=dict(
                    strategy_type=dict(
                        type="str", required=True, choices=["NGINX_CANARY_STRATEGY"]
                    ),
                    namespace=dict(type="str", required=True),
                    ingress_name=dict(type="str", required=True),
                ),
            ),
            compute_instance_group_canary_deploy_stage_id=dict(type="str"),
            compute_instance_group_canary_traffic_shift_deploy_stage_id=dict(
                type="str"
            ),
            deploy_environment_id_a=dict(type="str"),
            deploy_environment_id_b=dict(type="str"),
            production_load_balancer_config=dict(
                type="dict",
                options=dict(
                    load_balancer_id=dict(type="str", required=True),
                    listener_name=dict(type="str", required=True),
                    backend_port=dict(type="int"),
                ),
            ),
            deploy_pipeline_id=dict(type="str"),
            oke_canary_traffic_shift_deploy_stage_id=dict(type="str"),
            helm_chart_deploy_artifact_id=dict(type="str"),
            values_artifact_ids=dict(type="list", elements="str"),
            release_name=dict(type="str"),
            compute_instance_group_deploy_environment_id=dict(type="str"),
            container_config=dict(
                type="dict",
                options=dict(
                    container_config_type=dict(
                        type="str", required=True, choices=["CONTAINER_INSTANCE_CONFIG"]
                    ),
                    compartment_id=dict(type="str"),
                    availability_domain=dict(type="str"),
                    shape_name=dict(type="str", required=True),
                    shape_config=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            ocpus=dict(type="float", required=True),
                            memory_in_gbs=dict(type="float"),
                        ),
                    ),
                    network_channel=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            network_channel_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "SERVICE_VNIC_CHANNEL",
                                    "PRIVATE_ENDPOINT_CHANNEL",
                                ],
                            ),
                            subnet_id=dict(type="str", required=True),
                            nsg_ids=dict(type="list", elements="str"),
                        ),
                    ),
                ),
            ),
            command_spec_deploy_artifact_id=dict(type="str"),
            timeout_in_seconds=dict(type="int"),
            oke_cluster_deploy_environment_id=dict(type="str"),
            namespace=dict(type="str"),
            blue_backend_ips=dict(
                type="dict", options=dict(items=dict(type="list", elements="str"))
            ),
            green_backend_ips=dict(
                type="dict", options=dict(items=dict(type="list", elements="str"))
            ),
            traffic_shift_target=dict(type="str"),
            load_balancer_config=dict(
                type="dict",
                options=dict(
                    load_balancer_id=dict(type="str", required=True),
                    listener_name=dict(type="str", required=True),
                    backend_port=dict(type="int"),
                ),
            ),
            rollback_policy=dict(
                type="dict",
                options=dict(
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "NO_STAGE_ROLLBACK_POLICY",
                            "AUTOMATED_STAGE_ROLLBACK_POLICY",
                        ],
                    )
                ),
            ),
            kubernetes_manifest_deploy_artifact_ids=dict(type="list", elements="str"),
            wait_criteria=dict(
                type="dict",
                options=dict(
                    wait_type=dict(
                        type="str", required=True, choices=["ABSOLUTE_WAIT"]
                    ),
                    wait_duration=dict(type="str", required=True),
                ),
            ),
            approval_policy=dict(
                type="dict",
                options=dict(
                    approval_policy_type=dict(
                        type="str", required=True, choices=["COUNT_BASED_APPROVAL"]
                    ),
                    number_of_approvals_required=dict(type="int", required=True),
                ),
            ),
            failure_policy=dict(
                type="dict",
                options=dict(
                    failure_percentage=dict(type="int"),
                    policy_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_PERCENTAGE",
                            "COMPUTE_INSTANCE_GROUP_FAILURE_POLICY_BY_COUNT",
                        ],
                    ),
                    failure_count=dict(type="int"),
                ),
            ),
            deployment_spec_deploy_artifact_id=dict(type="str"),
            deploy_artifact_ids=dict(type="list", elements="str"),
            test_load_balancer_config=dict(
                type="dict",
                options=dict(
                    load_balancer_id=dict(type="str", required=True),
                    listener_name=dict(type="str", required=True),
                    backend_port=dict(type="int"),
                ),
            ),
            docker_image_deploy_artifact_id=dict(type="str"),
            config=dict(type="dict"),
            max_memory_in_mbs=dict(type="int"),
            function_timeout_in_seconds=dict(type="int"),
            rollout_policy=dict(
                type="dict",
                options=dict(
                    ramp_limit_percent=dict(type="float"),
                    batch_percentage=dict(type="int"),
                    policy_type=dict(
                        type="str",
                        choices=[
                            "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_PERCENTAGE",
                            "COMPUTE_INSTANCE_GROUP_LINEAR_ROLLOUT_POLICY_BY_COUNT",
                        ],
                    ),
                    batch_delay_in_seconds=dict(type="int"),
                    batch_count=dict(type="int"),
                ),
            ),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            deploy_stage_type=dict(
                type="str",
                choices=[
                    "OKE_CANARY_TRAFFIC_SHIFT",
                    "OKE_BLUE_GREEN_TRAFFIC_SHIFT",
                    "COMPUTE_INSTANCE_GROUP_CANARY_DEPLOYMENT",
                    "WAIT",
                    "LOAD_BALANCER_TRAFFIC_SHIFT",
                    "SHELL",
                    "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_TRAFFIC_SHIFT",
                    "OKE_BLUE_GREEN_DEPLOYMENT",
                    "COMPUTE_INSTANCE_GROUP_ROLLING_DEPLOYMENT",
                    "INVOKE_FUNCTION",
                    "DEPLOY_FUNCTION",
                    "OKE_CANARY_DEPLOYMENT",
                    "COMPUTE_INSTANCE_GROUP_CANARY_TRAFFIC_SHIFT",
                    "COMPUTE_INSTANCE_GROUP_CANARY_APPROVAL",
                    "OKE_HELM_CHART_DEPLOYMENT",
                    "MANUAL_APPROVAL",
                    "OKE_DEPLOYMENT",
                    "COMPUTE_INSTANCE_GROUP_BLUE_GREEN_DEPLOYMENT",
                    "OKE_CANARY_APPROVAL",
                ],
            ),
            deploy_stage_predecessor_collection=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(id=dict(type="str", required=True)),
                    )
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            function_deploy_environment_id=dict(type="str"),
            deploy_artifact_id=dict(type="str"),
            is_async=dict(type="bool"),
            is_validation_enabled=dict(type="bool"),
            deploy_stage_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deploy_stage",
        service_client_class=DevopsClient,
        namespace="devops",
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
