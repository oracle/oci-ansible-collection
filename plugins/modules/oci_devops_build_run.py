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
module: oci_devops_build_run
short_description: Manage a BuildRun resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and update a BuildRun resource in Oracle Cloud Infrastructure
    - For I(state=present), starts a build pipeline run for a predefined build pipeline.
    - "This resource has the following action operations in the M(oracle.oci.oci_devops_build_run_actions) module: cancel."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    build_pipeline_id:
        description:
            - The OCID of the build pipeline.
            - Required for create using I(state=present).
        type: str
    commit_info:
        description:
            - ""
        type: dict
        suboptions:
            repository_url:
                description:
                    - Repository URL.
                type: str
                required: true
            repository_branch:
                description:
                    - Name of the repository branch.
                type: str
                required: true
            commit_hash:
                description:
                    - Commit hash pertinent to the repository URL and the specified branch.
                type: str
                required: true
    build_run_arguments:
        description:
            - ""
        type: dict
        suboptions:
            items:
                description:
                    - List of arguments provided at the time of running the build.
                type: list
                elements: dict
                required: true
                suboptions:
                    name:
                        description:
                            - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$.
                              Example: 'Build_Pipeline_param' is not same as 'build_pipeline_Param'"
                        type: str
                        required: true
                    value:
                        description:
                            - Value of the argument.
                        type: str
                        required: true
    build_run_id:
        description:
            - Unique build run identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - Build run display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
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
    state:
        description:
            - The state of the BuildRun.
            - Use I(state=present) to create or update a BuildRun.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create build_run
  oci_devops_build_run:
    # required
    build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    commit_info:
      # required
      repository_url: repository_url_example
      repository_branch: repository_branch_example
      commit_hash: commit_hash_example
    build_run_arguments:
      # required
      items:
      - # required
        name: name_example
        value: value_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update build_run
  oci_devops_build_run:
    # required
    build_run_id: "ocid1.buildrun.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update build_run using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_build_run:
    # required
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

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
                                            sample: DEVOPS_CODE_REPOSITORY
                                        events:
                                            description:
                                                - The events only support PUSH.
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
                                                        - Branch for push event.
                                                    returned: on success
                                                    type: str
                                                    sample: head_ref_example
                                                base_ref:
                                                    description:
                                                        - The target branch for pull requests; not applicable for push requests.
                                                    returned: on success
                                                    type: str
                                                    sample: base_ref_example
                                build_pipeline_id:
                                    description:
                                        - The OCID of the build pipeline to be triggered.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
                source_type:
                    description:
                        - The source from which the build run is triggered.
                    returned: on success
                    type: str
                    sample: MANUAL
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
                                                - Connection identifier pertinent to GitHub source provider.
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
                                                - The ID of the predecessor stage. If a stage is the first stage in the pipeline, then the ID is the pipeline's
                                                  ID.
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
            "source_type": "MANUAL"
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient
    from oci.devops.models import CreateBuildRunDetails
    from oci.devops.models import UpdateBuildRunDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BuildRunHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get and list"""

    def get_possible_entity_types(self):
        return super(BuildRunHelperGen, self).get_possible_entity_types() + [
            "devopsbuildrun",
            "devopsbuildruns",
            "devopsdevopsbuildrun",
            "devopsdevopsbuildruns",
            "devopsbuildrunresource",
            "devopsbuildrunsresource",
            "buildrun",
            "buildruns",
            "buildrunresource",
            "buildrunsresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "build_run_id"

    def get_module_resource_id(self):
        return self.module.params.get("build_run_id")

    def get_get_fn(self):
        return self.client.get_build_run

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_build_run, build_run_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_build_run,
            build_run_id=self.module.params.get("build_run_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["build_pipeline_id", "display_name"]

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
            self.client.list_build_runs, **kwargs
        )

    def get_create_model_class(self):
        return CreateBuildRunDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_build_run,
            call_fn_args=(),
            call_fn_kwargs=dict(create_build_run_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateBuildRunDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_build_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                build_run_id=self.module.params.get("build_run_id"),
                update_build_run_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


BuildRunHelperCustom = get_custom_class("BuildRunHelperCustom")


class ResourceHelper(BuildRunHelperCustom, BuildRunHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            build_pipeline_id=dict(type="str"),
            commit_info=dict(
                type="dict",
                options=dict(
                    repository_url=dict(type="str", required=True),
                    repository_branch=dict(type="str", required=True),
                    commit_hash=dict(type="str", required=True),
                ),
            ),
            build_run_arguments=dict(
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
            build_run_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            state=dict(type="str", default="present", choices=["present"]),
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
