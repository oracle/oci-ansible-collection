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
module: oci_artifacts_container_repository_actions
short_description: Perform actions on a ContainerRepository resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ContainerRepository resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a container repository into a different compartment within the same tenancy. For information about moving
      resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container repository.
            - "Example: `ocid1.containerrepo.oc1..exampleuniqueID`"
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment into which to move the resource.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ContainerRepository.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on container_repository
  oci_artifacts_container_repository_actions:
    repository_id: "ocid1.containerrepo.oc1..exampleuniqueID"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
        billable_size_in_gbs:
            description:
                - Total storage size in GBs that will be charged.
            returned: on success
            type: int
            sample: 56
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
        "time_last_pushed": "2013-10-20T19:20:30+01:00",
        "billable_size_in_gbs": 56
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
    from oci.artifacts import ArtifactsClient
    from oci.artifacts.models import ChangeContainerRepositoryCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerRepositoryActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeContainerRepositoryCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_container_repository_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                repository_id=self.module.params.get("repository_id"),
                change_container_repository_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
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


ContainerRepositoryActionsHelperCustom = get_custom_class(
    "ContainerRepositoryActionsHelperCustom"
)


class ResourceHelper(
    ContainerRepositoryActionsHelperCustom, ContainerRepositoryActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            repository_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
