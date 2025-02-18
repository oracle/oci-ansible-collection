#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_artifacts_container_image_facts
short_description: Fetches details about one or multiple ContainerImage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ContainerImage resources in Oracle Cloud Infrastructure
    - List container images in a compartment.
    - If I(image_id) is specified, the details of a single ContainerImage will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple container_images.
        type: str
    compartment_id_in_subtree:
        description:
            - When set to true, the hierarchy of compartments is traversed
              and all compartments and subcompartments in the tenancy are
              inspected depending on the the setting of `accessLevel`.
              Default is false. Can only be set to true when calling the API
              on the tenancy (root compartment).
        type: bool
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container image.
            - "Example: `ocid1.containerimage.oc1..exampleuniqueID`"
            - Required to get a specific container_image.
        type: str
        aliases: ["id"]
    is_versioned:
        description:
            - A filter to return container images based on whether there are any associated versions.
        type: bool
    repository_id:
        description:
            - A filter to return container images only for the specified container repository OCID.
        type: str
    repository_name:
        description:
            - A filter to return container images or container image signatures that match the repository name.
            - "Example: `foo` or `foo*`"
        type: str
    version:
        description:
            - A filter to return container images that match the version.
            - "Example: `foo` or `foo*`"
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific container_image
  oci_artifacts_container_image_facts:
    # required
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"

- name: List container_images
  oci_artifacts_container_image_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id_in_subtree: true
    display_name: display_name_example
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    is_versioned: true
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    repository_name: repository_name_example
    version: version_example
    lifecycle_state: lifecycle_state_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
container_images:
    description:
        - List of ContainerImage resources
    returned: on success
    type: complex
    contains:
        created_by:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the user or principal that created the resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: created_by_example
        layers:
            description:
                - Layers of which the image is composed, ordered by the layer digest.
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        manifest_size_in_bytes:
            description:
                - The size of the container image manifest in bytes.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        pull_count:
            description:
                - Total number of pulls.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        time_last_pulled:
            description:
                - An RFC 3339 timestamp indicating when the image was last pulled.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        versions:
            description:
                - The versions associated with this image.
                - Returned for get operation
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
        compartment_id:
            description:
                - The compartment OCID to which the container image belongs. Inferred from the container repository.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        lifecycle_state:
            description:
                - The current state of the container image.
            returned: on success
            type: str
            sample: AVAILABLE
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
        version:
            description:
                - The most recent version associated with this image.
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
    sample: [{
        "created_by": "created_by_example",
        "layers": [{
            "digest": "digest_example",
            "size_in_bytes": 56,
            "time_created": "2013-10-20T19:20:30+01:00"
        }],
        "layers_size_in_bytes": 56,
        "manifest_size_in_bytes": 56,
        "pull_count": 56,
        "time_last_pulled": "2013-10-20T19:20:30+01:00",
        "versions": [{
            "created_by": "created_by_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "version": "version_example"
        }],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "digest": "digest_example",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "AVAILABLE",
        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
        "repository_name": "repository_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "version": "version_example",
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
    from oci.artifacts import ArtifactsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerImageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "image_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_image,
            image_id=self.module.params.get("image_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "display_name",
            "image_id",
            "is_versioned",
            "repository_id",
            "repository_name",
            "version",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_container_images,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ContainerImageFactsHelperCustom = get_custom_class("ContainerImageFactsHelperCustom")


class ResourceFactsHelper(
    ContainerImageFactsHelperCustom, ContainerImageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            image_id=dict(aliases=["id"], type="str"),
            is_versioned=dict(type="bool"),
            repository_id=dict(type="str"),
            repository_name=dict(type="str"),
            version=dict(type="str"),
            lifecycle_state=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="container_image",
        service_client_class=ArtifactsClient,
        namespace="artifacts",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(container_images=result)


if __name__ == "__main__":
    main()
