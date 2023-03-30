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
module: oci_devops_build_pipeline_stage_facts
short_description: Fetches details about one or multiple BuildPipelineStage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BuildPipelineStage resources in Oracle Cloud Infrastructure
    - Returns a list of all stages in a compartment or build pipeline.
    - If I(build_pipeline_stage_id) is specified, the details of a single BuildPipelineStage will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    build_pipeline_stage_id:
        description:
            - Unique stage identifier.
            - Required to get a specific build_pipeline_stage.
        type: str
        aliases: ["id"]
    build_pipeline_id:
        description:
            - The OCID of the parent build pipeline.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return the stages that matches the given lifecycle state.
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
- name: Get a specific build_pipeline_stage
  oci_devops_build_pipeline_stage_facts:
    # required
    build_pipeline_stage_id: "ocid1.buildpipelinestage.oc1..xxxxxxEXAMPLExxxxxx"

- name: List build_pipeline_stages
  oci_devops_build_pipeline_stage_facts:

    # optional
    build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
build_pipeline_stages:
    description:
        - List of BuildPipelineStage resources
    returned: on success
    type: complex
    contains:
        image:
            description:
                - Image name for the build environment.
                - Returned for get operation
            returned: on success
            type: str
            sample: OL7_X86_64_STANDARD_10
        build_spec_file:
            description:
                - The path to the build specification file for this environment. The default location of the file if not specified is build_spec.yaml.
                - Returned for get operation
            returned: on success
            type: str
            sample: build_spec_file_example
        stage_execution_timeout_in_seconds:
            description:
                - Timeout for the build stage execution. Specify value in seconds.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        build_source_collection:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - Collection of build sources. In case of UPDATE operation, replaces existing build sources list. Merging with existing build sources is
                          not supported.
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
                                - Name of the build source. This must be unique within a build source collection. The name can be used by customers to locate
                                  the working directory pertinent to this repository.
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
                - Name of the build source where the build_spec.yml file is located. If not specified, then the first entry in the build source collection is
                  chosen as primary build source.
                - Returned for get operation
            returned: on success
            type: str
            sample: primary_build_source_example
        build_runner_shape_config:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs set for the instance.
                    returned: on success
                    type: int
                    sample: 56
                memory_in_gbs:
                    description:
                        - The total amount of memory set for the instance in gigabytes.
                    returned: on success
                    type: int
                    sample: 56
                build_runner_type:
                    description:
                        - Name of the build runner shape in which the execution occurs. If not specified, the default shape is chosen.
                    returned: on success
                    type: str
                    sample: CUSTOM
        private_access_config:
            description:
                - ""
                - Returned for get operation
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
        deliver_artifact_collection:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - Collection of artifacts that were generated in the Build stage and need to be pushed to the artifactory stores. In case of UPDATE
                          operation, replaces existing artifacts list. Merging with existing artifacts is not supported.
                    returned: on success
                    type: complex
                    contains:
                        artifact_name:
                            description:
                                - Name of the artifact specified in the build_spec.yaml file.
                            returned: on success
                            type: str
                            sample: artifact_name_example
                        artifact_id:
                            description:
                                - Artifact identifier that contains the artifact definition.
                            returned: on success
                            type: str
                            sample: "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_pipeline_id:
            description:
                - A target deployment pipeline OCID that will run in this stage.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx"
        is_pass_all_parameters_enabled:
            description:
                - A boolean flag that specifies whether all the parameters must be passed when the deployment is triggered.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
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
        display_name:
            description:
                - Stage display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
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
        compartment_id:
            description:
                - The OCID of the compartment where the pipeline is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        build_pipeline_stage_type:
            description:
                - "Defines the stage type, which is one of the following: BUILD, DELIVER_ARTIFACT, WAIT, and TRIGGER_DEPLOYMENT_PIPELINE."
            returned: on success
            type: str
            sample: WAIT
        time_created:
            description:
                - The time the stage was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the stage was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the stage.
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
        description:
            description:
                - Optional description about the build stage.
            returned: on success
            type: str
            sample: description_example
        build_pipeline_stage_predecessor_collection:
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
        "build_runner_shape_config": {
            "ocpus": 56,
            "memory_in_gbs": 56,
            "build_runner_type": "CUSTOM"
        },
        "private_access_config": {
            "network_channel_type": "PRIVATE_ENDPOINT_CHANNEL",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "nsg_ids": []
        },
        "deliver_artifact_collection": {
            "items": [{
                "artifact_name": "artifact_name_example",
                "artifact_id": "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
        "deploy_pipeline_id": "ocid1.deploypipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "is_pass_all_parameters_enabled": true,
        "wait_criteria": {
            "wait_type": "ABSOLUTE_WAIT",
            "wait_duration": "wait_duration_example"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "build_pipeline_stage_type": "WAIT",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "description": "description_example",
        "build_pipeline_stage_predecessor_collection": {
            "items": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        },
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


class DevopsBuildPipelineStageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "build_pipeline_stage_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_build_pipeline_stage,
            build_pipeline_stage_id=self.module.params.get("build_pipeline_stage_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "build_pipeline_id",
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
            self.client.list_build_pipeline_stages, **optional_kwargs
        )


DevopsBuildPipelineStageFactsHelperCustom = get_custom_class(
    "DevopsBuildPipelineStageFactsHelperCustom"
)


class ResourceFactsHelper(
    DevopsBuildPipelineStageFactsHelperCustom, DevopsBuildPipelineStageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            build_pipeline_stage_id=dict(aliases=["id"], type="str"),
            build_pipeline_id=dict(type="str"),
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

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="build_pipeline_stage",
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

    module.exit_json(build_pipeline_stages=result)


if __name__ == "__main__":
    main()
