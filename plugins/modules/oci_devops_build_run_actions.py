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
module: oci_devops_build_run_actions
short_description: Perform actions on a BuildRun resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BuildRun resource in Oracle Cloud Infrastructure
    - For I(action=cancel), cancels the build run based on the build run ID provided in the request.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    reason:
        description:
            - The reason for canceling the build run.
        type: str
        required: true
    build_run_id:
        description:
            - Unique build run identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the BuildRun.
        type: str
        required: true
        choices:
            - "cancel"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cancel on build_run
  oci_devops_build_run_actions:
    # required
    reason: reason_example
    build_run_id: "ocid1.buildrun.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel

"""

RETURN = """
build_run:
    description:
        - Details of the BuildRun resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment where the build is running.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The OCID of the DevOps project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        build_pipeline_id:
            description:
                - The OCID of the build pipeline.
            returned: on success
            type: str
            sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        build_run_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                repository_id:
                    description:
                        - The DevOps code repository identifier that invoked the build run.
                    returned: on success
                    type: str
                    sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
                source_type:
                    description:
                        - The source from which the build run is triggered.
                    returned: on success
                    type: str
                    sample: MANUAL
                trigger_id:
                    description:
                        - The trigger that invoked the build run.
                    returned: on success
                    type: str
                    sample: "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx"
                trigger_info:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - Name for Trigger.
                            returned: on success
                            type: str
                            sample: display_name_example
                        actions:
                            description:
                                - The list of actions that are to be performed for this Trigger
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - The type of action that will be taken. Allowed value is TRIGGER_BUILD_PIPELINE.
                                    returned: on success
                                    type: str
                                    sample: TRIGGER_BUILD_PIPELINE
                                filter:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        trigger_source:
                                            description:
                                                - Source of the trigger. Allowed values are, GITHUB and GITLAB.
                                            returned: on success
                                            type: str
                                            sample: BITBUCKET_CLOUD
                                        events:
                                            description:
                                                - The events, for example, PUSH, PULL_REQUEST_MERGE.
                                            returned: on success
                                            type: list
                                            sample: []
                                        include:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                head_ref:
                                                    description:
                                                        - Branch for push event; source branch for pull requests.
                                                    returned: on success
                                                    type: str
                                                    sample: head_ref_example
                                                base_ref:
                                                    description:
                                                        - The target branch for pull requests; not applicable for push requests.
                                                    returned: on success
                                                    type: str
                                                    sample: base_ref_example
                                                file_filter:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        file_paths:
                                                            description:
                                                                - The file paths/glob pattern for files.
                                                            returned: on success
                                                            type: list
                                                            sample: []
                                                repository_name:
                                                    description:
                                                        - The repository name for trigger events.
                                                    returned: on success
                                                    type: str
                                                    sample: repository_name_example
                                        exclude:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                file_filter:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        file_paths:
                                                            description:
                                                                - The file paths/glob pattern for files.
                                                            returned: on success
                                                            type: list
                                                            sample: []
                                build_pipeline_id:
                                    description:
                                        - The OCID of the build pipeline to be triggered.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        build_run_arguments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of arguments provided at the time of running the build.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$.
                                  Example: 'Build_Pipeline_param' is not same as 'build_pipeline_Param'"
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - Value of the argument.
                            returned: on success
                            type: str
                            sample: value_example
        time_created:
            description:
                - The time the build run was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the build run was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the build run.
            returned: on success
            type: str
            sample: ACCEPTED
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        build_run_progress:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_started:
                    description:
                        - The time the build run started. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_finished:
                    description:
                        - The time the build run finished. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                build_pipeline_stage_run_progress:
                    description:
                        - Map of stage OCIDs to build pipeline stage run progress model.
                    returned: on success
                    type: complex
                    contains:
                        actual_build_runner_shape:
                            description:
                                - Name of Build Runner shape where this Build Stage is running.
                            returned: on success
                            type: str
                            sample: actual_build_runner_shape_example
                        actual_build_runner_shape_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                ocpus:
                                    description:
                                        - The total number of OCPUs set for the instance.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                                memory_in_gbs:
                                    description:
                                        - The total amount of memory set for the instance in gigabytes.
                                    returned: on success
                                    type: float
                                    sample: 1.2
                        image:
                            description:
                                - Image name for the Build Environment
                            returned: on success
                            type: str
                            sample: OL7_X86_64_STANDARD_10
                        build_spec_file:
                            description:
                                - The path to the build specification file for this Environment. The default location if not specified is build_spec.yaml
                            returned: on success
                            type: str
                            sample: build_spec_file_example
                        stage_execution_timeout_in_seconds:
                            description:
                                - Timeout for the Build Stage Execution. Value in seconds.
                            returned: on success
                            type: int
                            sample: 56
                        build_source_collection:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - Collection of build sources. In case of UPDATE operation, replaces existing build sources list. Merging with existing
                                          build sources is not supported.
                                    returned: on success
                                    type: complex
                                    contains:
                                        repository_id:
                                            description:
                                                - The DevOps code repository ID.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
                                        name:
                                            description:
                                                - Name of the build source. This must be unique within a build source collection. The name can be used by
                                                  customers to locate the working directory pertinent to this repository.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        connection_type:
                                            description:
                                                - The type of source provider.
                                            returned: on success
                                            type: str
                                            sample: GITHUB
                                        repository_url:
                                            description:
                                                - URL for the repository.
                                            returned: on success
                                            type: str
                                            sample: repository_url_example
                                        branch:
                                            description:
                                                - Branch name.
                                            returned: on success
                                            type: str
                                            sample: branch_example
                                        connection_id:
                                            description:
                                                - Connection identifier pertinent to Bitbucket Cloud source provider
                                            returned: on success
                                            type: str
                                            sample: "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
                        primary_build_source:
                            description:
                                - Name of the BuildSource in which the build_spec.yml file need to be located. If not specified, the 1st entry in the
                                  BuildSource collection will be chosen as Primary.
                            returned: on success
                            type: str
                            sample: primary_build_source_example
                        steps:
                            description:
                                - The details about all the steps in a Build stage
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
                        private_access_config:
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
                        delivered_artifacts:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of artifacts delivered through the Deliver Artifacts stage.
                                    returned: on success
                                    type: complex
                                    contains:
                                        artifact_repository_id:
                                            description:
                                                - The OCID of the artifact registry repository used by the DeliverArtifactStage
                                            returned: on success
                                            type: str
                                            sample: "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx"
                                        delivered_artifact_id:
                                            description:
                                                - The OCID of the artifact pushed by the Deliver Artifacts stage.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                        path:
                                            description:
                                                - Path of the repository where artifact was pushed
                                            returned: on success
                                            type: str
                                            sample: path_example
                                        version:
                                            description:
                                                - Version of the artifact pushed
                                            returned: on success
                                            type: str
                                            sample: version_example
                                        deploy_artifact_id:
                                            description:
                                                - The OCID of the deployment artifact definition.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                        output_artifact_name:
                                            description:
                                                - Name of the output artifact defined in the build specification file.
                                            returned: on success
                                            type: str
                                            sample: output_artifact_name_example
                                        artifact_type:
                                            description:
                                                - Type of artifact delivered.
                                            returned: on success
                                            type: str
                                            sample: GENERIC_ARTIFACT
                                        delivered_artifact_hash:
                                            description:
                                                - The hash of the container registry artifact pushed by the Deliver Artifacts stage.
                                            returned: on success
                                            type: str
                                            sample: delivered_artifact_hash_example
                                        image_uri:
                                            description:
                                                - The imageUri of the OCIR artifact pushed by the DeliverArtifactStage
                                            returned: on success
                                            type: str
                                            sample: image_uri_example
                        exported_variables:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of exported variables.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$."
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        value:
                                            description:
                                                - Value of the argument.
                                            returned: on success
                                            type: str
                                            sample: value_example
                        artifact_override_parameters:
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
                        deployment_id:
                            description:
                                - Identifier of the deployment triggered.
                            returned: on success
                            type: str
                            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
                        stage_display_name:
                            description:
                                - Build Run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: stage_display_name_example
                        build_pipeline_stage_type:
                            description:
                                - Stage types.
                            returned: on success
                            type: str
                            sample: BUILD
                        build_pipeline_stage_id:
                            description:
                                - The stage OCID.
                            returned: on success
                            type: str
                            sample: "ocid1.buildpipelinestage.oc1..xxxxxxEXAMPLExxxxxx"
                        time_started:
                            description:
                                - The time the stage started executing. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_finished:
                            description:
                                - The time the stage finished executing. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        status:
                            description:
                                - The current status of the stage.
                            returned: on success
                            type: str
                            sample: ACCEPTED
                        build_pipeline_stage_predecessors:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - A list of build pipeline stage predecessors for a stage.
                                    returned: on success
                                    type: complex
                                    contains:
                                        id:
                                            description:
                                                - The OCID of the predecessor stage. If a stage is the first stage in the pipeline, then
                                                  the ID is the pipeline's OCID.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        commit_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                repository_url:
                    description:
                        - Repository URL.
                    returned: on success
                    type: str
                    sample: repository_url_example
                repository_branch:
                    description:
                        - Name of the repository branch.
                    returned: on success
                    type: str
                    sample: repository_branch_example
                commit_hash:
                    description:
                        - Commit hash pertinent to the repository URL and the specified branch.
                    returned: on success
                    type: str
                    sample: commit_hash_example
        build_outputs:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                exported_variables:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        items:
                            description:
                                - List of exported variables.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$."
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - Value of the argument.
                                    returned: on success
                                    type: str
                                    sample: value_example
                delivered_artifacts:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        items:
                            description:
                                - List of artifacts delivered through the Deliver Artifacts stage.
                            returned: on success
                            type: complex
                            contains:
                                artifact_repository_id:
                                    description:
                                        - The OCID of the artifact registry repository used by the DeliverArtifactStage
                                    returned: on success
                                    type: str
                                    sample: "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx"
                                delivered_artifact_id:
                                    description:
                                        - The OCID of the artifact pushed by the Deliver Artifacts stage.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                path:
                                    description:
                                        - Path of the repository where artifact was pushed
                                    returned: on success
                                    type: str
                                    sample: path_example
                                version:
                                    description:
                                        - Version of the artifact pushed
                                    returned: on success
                                    type: str
                                    sample: version_example
                                deploy_artifact_id:
                                    description:
                                        - The OCID of the deployment artifact definition.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                output_artifact_name:
                                    description:
                                        - Name of the output artifact defined in the build specification file.
                                    returned: on success
                                    type: str
                                    sample: output_artifact_name_example
                                artifact_type:
                                    description:
                                        - Type of artifact delivered.
                                    returned: on success
                                    type: str
                                    sample: GENERIC_ARTIFACT
                                delivered_artifact_hash:
                                    description:
                                        - The hash of the container registry artifact pushed by the Deliver Artifacts stage.
                                    returned: on success
                                    type: str
                                    sample: delivered_artifact_hash_example
                                image_uri:
                                    description:
                                        - The imageUri of the OCIR artifact pushed by the DeliverArtifactStage
                                    returned: on success
                                    type: str
                                    sample: image_uri_example
                artifact_override_parameters:
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
                vulnerability_audit_summary_collection:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        items:
                            description:
                                - List of vulnerability audit summary.
                            returned: on success
                            type: complex
                            contains:
                                vulnerability_audit_id:
                                    description:
                                        - The OCID of the vulnerability audit.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.vulnerabilityaudit.oc1..xxxxxxEXAMPLExxxxxx"
                                commit_hash:
                                    description:
                                        - Commit hash used while retrieving the pom file for vulnerabilityAudit.
                                    returned: on success
                                    type: str
                                    sample: commit_hash_example
                                build_stage_id:
                                    description:
                                        - Build stage OCID where scan was configured.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.buildstage.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "build_run_source": {
            "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
            "source_type": "MANUAL",
            "trigger_id": "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx",
            "trigger_info": {
                "display_name": "display_name_example",
                "actions": [{
                    "type": "TRIGGER_BUILD_PIPELINE",
                    "filter": {
                        "trigger_source": "BITBUCKET_CLOUD",
                        "events": [],
                        "include": {
                            "head_ref": "head_ref_example",
                            "base_ref": "base_ref_example",
                            "file_filter": {
                                "file_paths": []
                            },
                            "repository_name": "repository_name_example"
                        },
                        "exclude": {
                            "file_filter": {
                                "file_paths": []
                            }
                        }
                    },
                    "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
                }]
            }
        },
        "build_run_arguments": {
            "items": [{
                "name": "name_example",
                "value": "value_example"
            }]
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example",
        "build_run_progress": {
            "time_started": "2013-10-20T19:20:30+01:00",
            "time_finished": "2013-10-20T19:20:30+01:00",
            "build_pipeline_stage_run_progress": {
                "actual_build_runner_shape": "actual_build_runner_shape_example",
                "actual_build_runner_shape_config": {
                    "ocpus": 1.2,
                    "memory_in_gbs": 1.2
                },
                "image": "OL7_X86_64_STANDARD_10",
                "build_spec_file": "build_spec_file_example",
                "stage_execution_timeout_in_seconds": 56,
                "build_source_collection": {
                    "items": [{
                        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
                        "name": "name_example",
                        "connection_type": "GITHUB",
                        "repository_url": "repository_url_example",
                        "branch": "branch_example",
                        "connection_id": "ocid1.connection.oc1..xxxxxxEXAMPLExxxxxx"
                    }]
                },
                "primary_build_source": "primary_build_source_example",
                "steps": [{
                    "name": "name_example",
                    "state": "WAITING",
                    "time_started": "2013-10-20T19:20:30+01:00",
                    "time_finished": "2013-10-20T19:20:30+01:00"
                }],
                "private_access_config": {
                    "network_channel_type": "PRIVATE_ENDPOINT_CHANNEL",
                    "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
                    "nsg_ids": []
                },
                "delivered_artifacts": {
                    "items": [{
                        "artifact_repository_id": "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx",
                        "delivered_artifact_id": "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx",
                        "path": "path_example",
                        "version": "version_example",
                        "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                        "output_artifact_name": "output_artifact_name_example",
                        "artifact_type": "GENERIC_ARTIFACT",
                        "delivered_artifact_hash": "delivered_artifact_hash_example",
                        "image_uri": "image_uri_example"
                    }]
                },
                "exported_variables": {
                    "items": [{
                        "name": "name_example",
                        "value": "value_example"
                    }]
                },
                "artifact_override_parameters": {
                    "items": [{
                        "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                        "name": "name_example",
                        "value": "value_example"
                    }]
                },
                "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx",
                "stage_display_name": "stage_display_name_example",
                "build_pipeline_stage_type": "BUILD",
                "build_pipeline_stage_id": "ocid1.buildpipelinestage.oc1..xxxxxxEXAMPLExxxxxx",
                "time_started": "2013-10-20T19:20:30+01:00",
                "time_finished": "2013-10-20T19:20:30+01:00",
                "status": "ACCEPTED",
                "build_pipeline_stage_predecessors": {
                    "items": [{
                        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                    }]
                }
            }
        },
        "commit_info": {
            "repository_url": "repository_url_example",
            "repository_branch": "repository_branch_example",
            "commit_hash": "commit_hash_example"
        },
        "build_outputs": {
            "exported_variables": {
                "items": [{
                    "name": "name_example",
                    "value": "value_example"
                }]
            },
            "delivered_artifacts": {
                "items": [{
                    "artifact_repository_id": "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx",
                    "delivered_artifact_id": "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx",
                    "path": "path_example",
                    "version": "version_example",
                    "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                    "output_artifact_name": "output_artifact_name_example",
                    "artifact_type": "GENERIC_ARTIFACT",
                    "delivered_artifact_hash": "delivered_artifact_hash_example",
                    "image_uri": "image_uri_example"
                }]
            },
            "artifact_override_parameters": {
                "items": [{
                    "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                    "name": "name_example",
                    "value": "value_example"
                }]
            },
            "vulnerability_audit_summary_collection": {
                "items": [{
                    "vulnerability_audit_id": "ocid1.vulnerabilityaudit.oc1..xxxxxxEXAMPLExxxxxx",
                    "commit_hash": "commit_hash_example",
                    "build_stage_id": "ocid1.buildstage.oc1..xxxxxxEXAMPLExxxxxx"
                }]
            }
        },
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
    from oci.devops import DevopsClient
    from oci.devops.models import CancelBuildRunDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BuildRunActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel
    """

    @staticmethod
    def get_module_resource_id_param():
        return "build_run_id"

    def get_module_resource_id(self):
        return self.module.params.get("build_run_id")

    def get_get_fn(self):
        return self.client.get_build_run

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_build_run,
            build_run_id=self.module.params.get("build_run_id"),
        )

    def cancel(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CancelBuildRunDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_build_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cancel_build_run_details=action_details,
                build_run_id=self.module.params.get("build_run_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


BuildRunActionsHelperCustom = get_custom_class("BuildRunActionsHelperCustom")


class ResourceHelper(BuildRunActionsHelperCustom, BuildRunActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            reason=dict(type="str", required=True),
            build_run_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["cancel"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="build_run",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
