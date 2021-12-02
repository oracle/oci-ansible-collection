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
module: oci_devops_deploy_artifact_facts
short_description: Fetches details about one or multiple DeployArtifact resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DeployArtifact resources in Oracle Cloud Infrastructure
    - Returns a list of deployment artifacts.
    - If I(deploy_artifact_id) is specified, the details of a single DeployArtifact will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    deploy_artifact_id:
        description:
            - Unique artifact identifier.
            - Required to get a specific deploy_artifact.
        type: str
        aliases: ["id"]
    project_id:
        description:
            - unique project identifier
        type: str
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only DeployArtifacts that matches the given lifecycleState.
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
- name: Get a specific deploy_artifact
  oci_devops_deploy_artifact_facts:
    # required
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"

- name: List deploy_artifacts
  oci_devops_deploy_artifact_facts:

    # optional
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: lifecycle_state_example
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
deploy_artifacts:
    description:
        - List of DeployArtifact resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the artifact to be deployed.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Deployment artifact identifier, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        project_id:
            description:
                - The OCID of a project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_artifact_type:
            description:
                - Type of the deployment artifact.
            returned: on success
            type: str
            sample: DEPLOYMENT_SPEC
        argument_substitution_mode:
            description:
                - Mode for artifact parameter substitution.
            returned: on success
            type: str
            sample: NONE
        deploy_artifact_source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                deploy_artifact_source_type:
                    description:
                        - Specifies types of artifact sources.
                    returned: on success
                    type: str
                    sample: INLINE
                repository_id:
                    description:
                        - The OCID of a repository
                    returned: on success
                    type: str
                    sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
                deploy_artifact_path:
                    description:
                        - Specifies the artifact path in the repository.
                    returned: on success
                    type: str
                    sample: deploy_artifact_path_example
                deploy_artifact_version:
                    description:
                        - Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.
                    returned: on success
                    type: str
                    sample: ${appVersion}
                base64_encoded_content:
                    description:
                        - base64 Encoded String
                    returned: on success
                    type: str
                    sample: "example_base64_encoded_content"
                image_uri:
                    description:
                        - "Specifies OCIR Image Path - optionally include tag."
                    returned: on success
                    type: str
                    sample: image_uri_example
                image_digest:
                    description:
                        - Specifies image digest for the version of the image.
                    returned: on success
                    type: str
                    sample: image_digest_example
        time_created:
            description:
                - Time the deployment artifact was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the deployment artifact was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Current state of the deployment artifact.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A detailed message describing the current state. For example, can be used to provide actionable information for a resource in Failed state.
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_artifact_type": "DEPLOYMENT_SPEC",
        "argument_substitution_mode": "NONE",
        "deploy_artifact_source": {
            "deploy_artifact_source_type": "INLINE",
            "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
            "deploy_artifact_path": "deploy_artifact_path_example",
            "deploy_artifact_version": "${appVersion}",
            "base64_encoded_content": UNKNOWN TYPE - str,
            "image_uri": "image_uri_example",
            "image_digest": "image_digest_example"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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


class DeployArtifactFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "deploy_artifact_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_artifact,
            deploy_artifact_id=self.module.params.get("deploy_artifact_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "project_id",
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
            self.client.list_deploy_artifacts, **optional_kwargs
        )


DeployArtifactFactsHelperCustom = get_custom_class("DeployArtifactFactsHelperCustom")


class ResourceFactsHelper(
    DeployArtifactFactsHelperCustom, DeployArtifactFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deploy_artifact_id=dict(aliases=["id"], type="str"),
            project_id=dict(type="str"),
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
        resource_type="deploy_artifact",
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

    module.exit_json(deploy_artifacts=result)


if __name__ == "__main__":
    main()
