#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
    - For I(action=cancel), cancels the Build Run based on build run id provided in request
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    reason:
        description:
            - The reason for canceling the run.
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
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - BuildRun identifier which can be renamed and is not necessarily unique
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - Project Identifier
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        build_pipeline_id:
            description:
                - Pipeline Identifier
            returned: on success
            type: str
            sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        build_run_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - Source from which this build run was triggered
                    returned: on success
                    type: str
                    sample: MANUAL
                trigger_id:
                    description:
                        - The Trigger that invoked this build run
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
                                        - "The type of action that will be taken (allowed value - TRIGGER_BUILD_PIPELINE)"
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
                                                - "Source of the Trigger (allowed values are - GITHUB, GITLAB)"
                                            returned: on success
                                            type: str
                                            sample: DEVOPS_CODE_REPOSITORY
                                        events:
                                            description:
                                                - The events, only support PUSH at this time
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
                                                        - Branch for push event
                                                    returned: on success
                                                    type: str
                                                    sample: head_ref_example
                                                base_ref:
                                                    description:
                                                        - The target branch for pull requests; not applicable for push
                                                    returned: on success
                                                    type: str
                                                    sample: base_ref_example
                                build_pipeline_id:
                                    description:
                                        - The id of the build pipeline to be triggered
                                    returned: on success
                                    type: str
                                    sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
                repository_id:
                    description:
                        - The Devops Code Repository RepoId that invoked this build run
                    returned: on success
                    type: str
                    sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        build_run_arguments:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of arguments provided at the time of BuildRun.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the parameter (Case-sensitive).
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - value of the argument
                            returned: on success
                            type: str
                            sample: value_example
        time_created:
            description:
                - The time the the BuildRun was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the BuildRun was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the BuildRun.
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
                        - The time the the BuildRun is started. An RFC3339 formatted datetime string
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_finished:
                    description:
                        - The time the BuildRun is finished. An RFC3339 formatted datetime string
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                build_pipeline_stage_run_progress:
                    description:
                        - Map of stage OCIDs to BuildPipelineStageRunProgress model.
                    returned: on success
                    type: complex
                    contains:
                        stage_display_name:
                            description:
                                - BuildRun identifier which can be renamed and is not necessarily unique
                            returned: on success
                            type: str
                            sample: stage_display_name_example
                        build_pipeline_stage_type:
                            description:
                                - Stage sub types.
                            returned: on success
                            type: str
                            sample: BUILD
                        build_pipeline_stage_id:
                            description:
                                - Stage id
                            returned: on success
                            type: str
                            sample: "ocid1.buildpipelinestage.oc1..xxxxxxEXAMPLExxxxxx"
                        time_started:
                            description:
                                - The time the Stage was started executing. An RFC3339 formatted datetime string
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_finished:
                            description:
                                - The time the Stage was finished executing. An RFC3339 formatted datetime string
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        status:
                            description:
                                - The current status of the Stage.
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
                                        - A list of BuildPipelineStagePredecessors for a stage.
                                    returned: on success
                                    type: complex
                                    contains:
                                        id:
                                            description:
                                                - The id of the predecessor stage. If a stages is the first stage in the pipeline, then the id is the pipeline's
                                                  id.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
                                        - Collection of Build sources. In case of UPDATE operation, replaces existing Build sources list. Merging with existing
                                          Build Sources is not supported.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - Name of the Build source. This must be unique within a BuildSourceCollection. The name can be used by
                                                  customers to locate the working directory pertinent to this repository.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        connection_type:
                                            description:
                                                - The type of Source Provider.
                                            returned: on success
                                            type: str
                                            sample: GITHUB
                                        repository_url:
                                            description:
                                                - Url for repository
                                            returned: on success
                                            type: str
                                            sample: repository_url_example
                                        branch:
                                            description:
                                                - branch name
                                            returned: on success
                                            type: str
                                            sample: branch_example
                                        repository_id:
                                            description:
                                                - The Devops Code Repository Id
                                            returned: on success
                                            type: str
                                            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
                                        connection_id:
                                            description:
                                                - Connection identifier pertinent to GITHUB source provider
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
                                - The details about all the steps in a Build Stage
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
                        exported_variables:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                items:
                                    description:
                                        - List of exported variables
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - Name of the parameter (Case-sensitive).
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        value:
                                            description:
                                                - value of the argument
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
                                        - List of Artifacts delivered via DeliverArtifactStage
                                    returned: on success
                                    type: complex
                                    contains:
                                        deploy_artifact_id:
                                            description:
                                                - The OCID of the deploy artifact definition
                                            returned: on success
                                            type: str
                                            sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                        output_artifact_name:
                                            description:
                                                - Name of the output artifact defined in the build spec
                                            returned: on success
                                            type: str
                                            sample: output_artifact_name_example
                                        artifact_type:
                                            description:
                                                - Type of Artifact Delivered
                                            returned: on success
                                            type: str
                                            sample: GENERIC_ARTIFACT
                                        artifact_repository_id:
                                            description:
                                                - The OCID of the artifact registry repository used by the DeliverArtifactStage
                                            returned: on success
                                            type: str
                                            sample: "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx"
                                        delivered_artifact_id:
                                            description:
                                                - The OCID of the artifact pushed by the DeliverArtifactStage
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
                                        delivered_artifact_hash:
                                            description:
                                                - The Hash of the OCIR artifact pushed by the DeliverArtifactStage
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
                        deployment_id:
                            description:
                                - Identifier of the Deployment Trigerred.
                            returned: on success
                            type: str
                            sample: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
        commit_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                repository_url:
                    description:
                        - Repository URL
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
                        - Commit Hash pertinent to the repository URL and Branch specified.
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
                                - List of exported variables
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - Name of the parameter (Case-sensitive).
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - value of the argument
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
                                - List of Artifacts delivered via DeliverArtifactStage
                            returned: on success
                            type: complex
                            contains:
                                deploy_artifact_id:
                                    description:
                                        - The OCID of the deploy artifact definition
                                    returned: on success
                                    type: str
                                    sample: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
                                output_artifact_name:
                                    description:
                                        - Name of the output artifact defined in the build spec
                                    returned: on success
                                    type: str
                                    sample: output_artifact_name_example
                                artifact_type:
                                    description:
                                        - Type of Artifact Delivered
                                    returned: on success
                                    type: str
                                    sample: GENERIC_ARTIFACT
                                artifact_repository_id:
                                    description:
                                        - The OCID of the artifact registry repository used by the DeliverArtifactStage
                                    returned: on success
                                    type: str
                                    sample: "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx"
                                delivered_artifact_id:
                                    description:
                                        - The OCID of the artifact pushed by the DeliverArtifactStage
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
                                delivered_artifact_hash:
                                    description:
                                        - The Hash of the OCIR artifact pushed by the DeliverArtifactStage
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
            "source_type": "MANUAL",
            "trigger_id": "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx",
            "trigger_info": {
                "display_name": "display_name_example",
                "actions": [{
                    "type": "TRIGGER_BUILD_PIPELINE",
                    "filter": {
                        "trigger_source": "DEVOPS_CODE_REPOSITORY",
                        "events": [],
                        "include": {
                            "head_ref": "head_ref_example",
                            "base_ref": "base_ref_example"
                        }
                    },
                    "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
                }]
            },
            "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
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
                },
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
                        "name": "name_example",
                        "connection_type": "GITHUB",
                        "repository_url": "repository_url_example",
                        "branch": "branch_example",
                        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
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
                "exported_variables": {
                    "items": [{
                        "name": "name_example",
                        "value": "value_example"
                    }]
                },
                "delivered_artifacts": {
                    "items": [{
                        "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                        "output_artifact_name": "output_artifact_name_example",
                        "artifact_type": "GENERIC_ARTIFACT",
                        "artifact_repository_id": "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx",
                        "delivered_artifact_id": "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx",
                        "path": "path_example",
                        "version": "version_example",
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
                "deployment_id": "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
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
                    "deploy_artifact_id": "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx",
                    "output_artifact_name": "output_artifact_name_example",
                    "artifact_type": "GENERIC_ARTIFACT",
                    "artifact_repository_id": "ocid1.artifactrepository.oc1..xxxxxxEXAMPLExxxxxx",
                    "delivered_artifact_id": "ocid1.deliveredartifact.oc1..xxxxxxEXAMPLExxxxxx",
                    "path": "path_example",
                    "version": "version_example",
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
            }
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
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

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
