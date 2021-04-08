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
module: oci_artifacts_container_repository
short_description: Manage a ContainerRepository resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ContainerRepository resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new empty container repository. Avoid entering confidential information.
    - "This resource has the following action operations in the M(oci_container_repository_actions) module: change_compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to create the resource.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - The container repository name.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    is_immutable:
        description:
            - Whether the repository is immutable. Images cannot be overwritten in an immutable repository.
            - This parameter is updatable.
        type: bool
    is_public:
        description:
            - Whether the repository is public. A public repository allows unauthenticated access.
            - This parameter is updatable.
        type: bool
    readme:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            content:
                description:
                    - Readme content. Avoid entering confidential information.
                type: str
                required: true
            format:
                description:
                    - Readme format. Supported formats are text/plain and text/markdown.
                type: str
                choices:
                    - "TEXT_MARKDOWN"
                    - "TEXT_PLAIN"
                required: true
    repository_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container repository.
            - "Example: `ocid1.containerrepo.oc1..exampleuniqueID`"
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ContainerRepository.
            - Use I(state=present) to create or update a ContainerRepository.
            - Use I(state=absent) to delete a ContainerRepository.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create container_repository
  oci_artifacts_container_repository:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

- name: Update container_repository using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_artifacts_container_repository:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    is_immutable: true
    is_public: true
    readme:
      content: content_example
      format: TEXT_MARKDOWN

- name: Update container_repository
  oci_artifacts_container_repository:
    is_immutable: true
    is_public: true
    repository_id: "ocid1.containerrepo.oc1..exampleuniqueID"

- name: Delete container_repository
  oci_artifacts_container_repository:
    repository_id: "ocid1.containerrepo.oc1..exampleuniqueID"
    state: absent

- name: Delete container_repository using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_artifacts_container_repository:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
container_repository:
    description:
        - Details of the ContainerRepository resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment in which the container repository exists.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        created_by:
            description:
                - The id of the user or principal that created the resource.
            returned: on success
            type: string
            sample: created_by_example
        display_name:
            description:
                - The container repository name.
            returned: on success
            type: string
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container repository.
                - "Example: `ocid1.containerrepo.oc1..exampleuniqueID`"
            returned: on success
            type: string
            sample: "ocid1.containerrepo.oc1..exampleuniqueID"
        image_count:
            description:
                - Total number of images.
            returned: on success
            type: int
            sample: 56
        is_immutable:
            description:
                - Whether the repository is immutable. Images cannot be overwritten in an immutable repository.
            returned: on success
            type: bool
            sample: true
        is_public:
            description:
                - Whether the repository is public. A public repository allows unauthenticated access.
            returned: on success
            type: bool
            sample: true
        layer_count:
            description:
                - Total number of layers.
            returned: on success
            type: int
            sample: 56
        layers_size_in_bytes:
            description:
                - Total storage in bytes consumed by layers.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the container repository.
            returned: on success
            type: string
            sample: AVAILABLE
        readme:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                content:
                    description:
                        - Readme content. Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: content_example
                format:
                    description:
                        - Readme format. Supported formats are text/plain and text/markdown.
                    returned: on success
                    type: string
                    sample: TEXT_MARKDOWN
        time_created:
            description:
                - An RFC 3339 timestamp indicating when the repository was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_pushed:
            description:
                - An RFC 3339 timestamp indicating when an image was last pushed to the repository.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "created_by": "created_by_example",
        "display_name": "display_name_example",
        "id": "ocid1.containerrepo.oc1..exampleuniqueID",
        "image_count": 56,
        "is_immutable": true,
        "is_public": true,
        "layer_count": 56,
        "layers_size_in_bytes": 56,
        "lifecycle_state": "AVAILABLE",
        "readme": {
            "content": "content_example",
            "format": "TEXT_MARKDOWN"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_pushed": "2013-10-20T19:20:30+01:00"
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
    from oci.artifacts import ArtifactsClient
    from oci.artifacts.models import CreateContainerRepositoryDetails
    from oci.artifacts.models import UpdateContainerRepositoryDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerRepositoryHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "repository_id"

    def get_module_resource_id(self):
        return self.module.params.get("repository_id")

    def get_get_fn(self):
        return self.client.get_container_repository

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_repository,
            repository_id=self.module.params.get("repository_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["repository_id", "display_name"]
            if self._use_name_as_identifier()
            else ["repository_id", "display_name", "is_public"]
        )

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
            self.client.list_container_repositories, **kwargs
        )

    def get_create_model_class(self):
        return CreateContainerRepositoryDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_container_repository,
            call_fn_args=(),
            call_fn_kwargs=dict(create_container_repository_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateContainerRepositoryDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_container_repository,
            call_fn_args=(),
            call_fn_kwargs=dict(
                repository_id=self.module.params.get("repository_id"),
                update_container_repository_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_container_repository,
            call_fn_args=(),
            call_fn_kwargs=dict(repository_id=self.module.params.get("repository_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ContainerRepositoryHelperCustom = get_custom_class("ContainerRepositoryHelperCustom")


class ResourceHelper(ContainerRepositoryHelperCustom, ContainerRepositoryHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_immutable=dict(type="bool"),
            is_public=dict(type="bool"),
            readme=dict(
                type="dict",
                options=dict(
                    content=dict(type="str", required=True),
                    format=dict(
                        type="str",
                        required=True,
                        choices=["TEXT_MARKDOWN", "TEXT_PLAIN"],
                    ),
                ),
            ),
            repository_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="container_repository",
        service_client_class=ArtifactsClient,
        namespace="artifacts",
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
