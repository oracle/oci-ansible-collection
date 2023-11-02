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
module: oci_artifacts_container_image_actions
short_description: Perform actions on a ContainerImage resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ContainerImage resource in Oracle Cloud Infrastructure
    - For I(action=remove_container_version), remove version from container image.
    - For I(action=restore), restore a container image.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container image.
            - "Example: `ocid1.containerimage.oc1..exampleuniqueID`"
        type: str
        aliases: ["id"]
        required: true
    version:
        description:
            - The version to remove.
            - Required for I(action=remove_container_version).
        type: str
    action:
        description:
            - The action to perform on the ContainerImage.
        type: str
        required: true
        choices:
            - "remove_container_version"
            - "restore"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action remove_container_version on container_image
  oci_artifacts_container_image_actions:
    # required
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    version: version_example
    action: remove_container_version

- name: Perform action restore on container_image
  oci_artifacts_container_image_actions:
    # required
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    action: restore

    # optional
    version: version_example

"""

RETURN = """
container_image:
    description:
        - Details of the ContainerImage resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The compartment OCID to which the container image belongs. Inferred from the container repository.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the user or principal that created the resource.
            returned: on success
            type: str
            sample: created_by_example
        digest:
            description:
                - The container image digest.
            returned: on success
            type: str
            sample: digest_example
        display_name:
            description:
                - The repository name and the most recent version associated with the image.
                  If there are no versions associated with the image, then last known version and digest are used instead.
                  If the last known version is unavailable, then 'unknown' is used instead of the version.
                - "Example: `ubuntu:latest` or `ubuntu:latest@sha256:45b23dee08af5e43a7fea6c4cf9c25ccf269ee113168c19722f87876677c5cb2`"
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the container image.
                - "Example: `ocid1.containerimage.oc1..exampleuniqueID`"
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        layers:
            description:
                - Layers of which the image is composed, ordered by the layer digest.
            returned: on success
            type: complex
            contains:
                digest:
                    description:
                        - The sha256 digest of the image layer.
                    returned: on success
                    type: str
                    sample: digest_example
                size_in_bytes:
                    description:
                        - The size of the layer in bytes.
                    returned: on success
                    type: int
                    sample: 56
                time_created:
                    description:
                        - An RFC 3339 timestamp indicating when the layer was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        layers_size_in_bytes:
            description:
                - The total size of the container image layers in bytes.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the container image.
            returned: on success
            type: str
            sample: AVAILABLE
        manifest_size_in_bytes:
            description:
                - The size of the container image manifest in bytes.
            returned: on success
            type: int
            sample: 56
        pull_count:
            description:
                - Total number of pulls.
            returned: on success
            type: int
            sample: 56
        repository_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the container repository.
            returned: on success
            type: str
            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        repository_name:
            description:
                - The container repository name.
            returned: on success
            type: str
            sample: repository_name_example
        time_created:
            description:
                - An RFC 3339 timestamp indicating when the image was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_pulled:
            description:
                - An RFC 3339 timestamp indicating when the image was last pulled.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version:
            description:
                - The most recent version associated with this image.
            returned: on success
            type: str
            sample: version_example
        versions:
            description:
                - The versions associated with this image.
            returned: on success
            type: complex
            contains:
                created_by:
                    description:
                        - The OCID of the user or principal that pushed the version.
                    returned: on success
                    type: str
                    sample: created_by_example
                time_created:
                    description:
                        - The creation time of the version.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                version:
                    description:
                        - The version name.
                    returned: on success
                    type: str
                    sample: version_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "created_by": "created_by_example",
        "digest": "digest_example",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "layers": [{
            "digest": "digest_example",
            "size_in_bytes": 56,
            "time_created": "2013-10-20T19:20:30+01:00"
        }],
        "layers_size_in_bytes": 56,
        "lifecycle_state": "AVAILABLE",
        "manifest_size_in_bytes": 56,
        "pull_count": 56,
        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
        "repository_name": "repository_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_pulled": "2013-10-20T19:20:30+01:00",
        "version": "version_example",
        "versions": [{
            "created_by": "created_by_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "version": "version_example"
        }],
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
    from oci.artifacts import ArtifactsClient
    from oci.artifacts.models import RemoveContainerVersionDetails
    from oci.artifacts.models import RestoreContainerImageDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerImageActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        remove_container_version
        restore
    """

    @staticmethod
    def get_module_resource_id_param():
        return "image_id"

    def get_module_resource_id(self):
        return self.module.params.get("image_id")

    def get_get_fn(self):
        return self.client.get_container_image

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_image,
            image_id=self.module.params.get("image_id"),
        )

    def remove_container_version(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveContainerVersionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_container_version,
            call_fn_args=(),
            call_fn_kwargs=dict(
                image_id=self.module.params.get("image_id"),
                remove_container_version_details=action_details,
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

    def restore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreContainerImageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restore_container_image,
            call_fn_args=(),
            call_fn_kwargs=dict(
                image_id=self.module.params.get("image_id"),
                restore_container_image_details=action_details,
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


ContainerImageActionsHelperCustom = get_custom_class(
    "ContainerImageActionsHelperCustom"
)


class ResourceHelper(ContainerImageActionsHelperCustom, ContainerImageActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            image_id=dict(aliases=["id"], type="str", required=True),
            version=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=["remove_container_version", "restore"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="container_image",
        service_client_class=ArtifactsClient,
        namespace="artifacts",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
