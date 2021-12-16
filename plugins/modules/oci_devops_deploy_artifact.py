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
module: oci_devops_deploy_artifact
short_description: Manage a DeployArtifact resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DeployArtifact resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new deployment artifact.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    description:
        description:
            - Optional description about the deployment artifact.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - Deployment artifact display name. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    deploy_artifact_type:
        description:
            - Type of the deployment artifact.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    deploy_artifact_source:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            deploy_artifact_source_type:
                description:
                    - Specifies types of artifact sources.
                type: str
                choices:
                    - "GENERIC_ARTIFACT"
                    - "OCIR"
                    - "INLINE"
                required: true
            repository_id:
                description:
                    - The OCID of a repository
                    - Required when deploy_artifact_source_type is 'GENERIC_ARTIFACT'
                type: str
            deploy_artifact_path:
                description:
                    - Specifies the artifact path in the repository.
                    - Required when deploy_artifact_source_type is 'GENERIC_ARTIFACT'
                type: str
            deploy_artifact_version:
                description:
                    - Users can set this as a placeholder value that refers to a pipeline parameter, for example, ${appVersion}.
                    - Required when deploy_artifact_source_type is 'GENERIC_ARTIFACT'
                type: str
            image_uri:
                description:
                    - "Specifies OCIR Image Path - optionally include tag."
                    - Required when deploy_artifact_source_type is 'OCIR'
                type: str
            image_digest:
                description:
                    - Specifies image digest for the version of the image.
                    - Applicable when deploy_artifact_source_type is 'OCIR'
                type: str
            base64_encoded_content:
                description:
                    - base64 Encoded String
                    - Required when deploy_artifact_source_type is 'INLINE'
                type: str
    argument_substitution_mode:
        description:
            - Mode for artifact parameter substitution.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    project_id:
        description:
            - The OCID of a project.
            - Required for create using I(state=present).
        type: str
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
    deploy_artifact_id:
        description:
            - Unique artifact identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DeployArtifact.
            - Use I(state=present) to create or update a DeployArtifact.
            - Use I(state=absent) to delete a DeployArtifact.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deploy_artifact
  oci_devops_deploy_artifact:
    # required
    deploy_artifact_type: deploy_artifact_type_example
    deploy_artifact_source:
      # required
      deploy_artifact_source_type: GENERIC_ARTIFACT
      repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
      deploy_artifact_path: deploy_artifact_path_example
      deploy_artifact_version: deploy_artifact_version_example
    argument_substitution_mode: argument_substitution_mode_example
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_artifact
  oci_devops_deploy_artifact:
    # required
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    deploy_artifact_type: deploy_artifact_type_example
    deploy_artifact_source:
      # required
      deploy_artifact_source_type: GENERIC_ARTIFACT
      repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
      deploy_artifact_path: deploy_artifact_path_example
      deploy_artifact_version: deploy_artifact_version_example
    argument_substitution_mode: argument_substitution_mode_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deploy_artifact using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_deploy_artifact:
    # required
    display_name: display_name_example

    # optional
    description: description_example
    deploy_artifact_type: deploy_artifact_type_example
    deploy_artifact_source:
      # required
      deploy_artifact_source_type: GENERIC_ARTIFACT
      repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
      deploy_artifact_path: deploy_artifact_path_example
      deploy_artifact_version: deploy_artifact_version_example
    argument_substitution_mode: argument_substitution_mode_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete deploy_artifact
  oci_devops_deploy_artifact:
    # required
    deploy_artifact_id: "ocid1.deployartifact.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete deploy_artifact using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_deploy_artifact:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
deploy_artifact:
    description:
        - Details of the DeployArtifact resource acted upon by the current operation
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
                    sample: deploy_artifact_version_example
                base64_encoded_content:
                    description:
                        - base64 Encoded String
                    returned: on success
                    type: str
                    sample: "null"

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
    sample: {
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
            "deploy_artifact_version": "deploy_artifact_version_example",
            "base64_encoded_content": null,
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
    from oci.devops.models import CreateDeployArtifactDetails
    from oci.devops.models import UpdateDeployArtifactDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeployArtifactHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "deploy_artifact_id"

    def get_module_resource_id(self):
        return self.module.params.get("deploy_artifact_id")

    def get_get_fn(self):
        return self.client.get_deploy_artifact

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_artifact,
            deploy_artifact_id=self.module.params.get("deploy_artifact_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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
            self.client.list_deploy_artifacts, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeployArtifactDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deploy_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deploy_artifact_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeployArtifactDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deploy_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_artifact_id=self.module.params.get("deploy_artifact_id"),
                update_deploy_artifact_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deploy_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_artifact_id=self.module.params.get("deploy_artifact_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DeployArtifactHelperCustom = get_custom_class("DeployArtifactHelperCustom")


class ResourceHelper(DeployArtifactHelperCustom, DeployArtifactHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            deploy_artifact_type=dict(type="str"),
            deploy_artifact_source=dict(
                type="dict",
                options=dict(
                    deploy_artifact_source_type=dict(
                        type="str",
                        required=True,
                        choices=["GENERIC_ARTIFACT", "OCIR", "INLINE"],
                    ),
                    repository_id=dict(type="str"),
                    deploy_artifact_path=dict(type="str"),
                    deploy_artifact_version=dict(type="str"),
                    image_uri=dict(type="str"),
                    image_digest=dict(type="str"),
                    base64_encoded_content=dict(type="str"),
                ),
            ),
            argument_substitution_mode=dict(type="str"),
            project_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            deploy_artifact_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deploy_artifact",
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
