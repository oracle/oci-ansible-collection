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
module: oci_artifacts_container_repository_facts
short_description: Fetches details about one or multiple ContainerRepository resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ContainerRepository resources in Oracle Cloud Infrastructure
    - List container repositories in a compartment.
    - If I(repository_id) is specified, the details of a single ContainerRepository will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    repository_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container repository.
            - "Example: `ocid1.containerrepo.oc1..exampleuniqueID`"
            - Required to get a specific container_repository.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple container_repositories.
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
    is_public:
        description:
            - A filter to return resources that match the isPublic value.
        type: bool
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
- name: Get a specific container_repository
  oci_artifacts_container_repository_facts:
    # required
    repository_id: "ocid1.containerrepo.oc1..exampleuniqueID"

- name: List container_repositories
  oci_artifacts_container_repository_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    repository_id: "ocid1.containerrepo.oc1..exampleuniqueID"
    compartment_id_in_subtree: true
    display_name: display_name_example
    is_public: true
    lifecycle_state: lifecycle_state_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
container_repositories:
    description:
        - List of ContainerRepository resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment in which the container repository exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        created_by:
            description:
                - The id of the user or principal that created the resource.
            returned: on success
            type: str
            sample: created_by_example
        display_name:
            description:
                - The container repository name.
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container repository.
                - "Example: `ocid1.containerrepo.oc1..exampleuniqueID`"
            returned: on success
            type: str
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
            type: str
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
                    type: str
                    sample: content_example
                format:
                    description:
                        - Readme format. Supported formats are text/plain and text/markdown.
                    returned: on success
                    type: str
                    sample: TEXT_MARKDOWN
        time_created:
            description:
                - An RFC 3339 timestamp indicating when the repository was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_pushed:
            description:
                - An RFC 3339 timestamp indicating when an image was last pushed to the repository.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        billable_size_in_gbs:
            description:
                - Total storage size in GBs that will be charged.
            returned: on success
            type: int
            sample: 56
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.artifacts import ArtifactsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerRepositoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "repository_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_repository,
            repository_id=self.module.params.get("repository_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "repository_id",
            "display_name",
            "is_public",
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
            self.client.list_container_repositories,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ContainerRepositoryFactsHelperCustom = get_custom_class(
    "ContainerRepositoryFactsHelperCustom"
)


class ResourceFactsHelper(
    ContainerRepositoryFactsHelperCustom, ContainerRepositoryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            repository_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            display_name=dict(aliases=["name"], type="str"),
            is_public=dict(type="bool"),
            lifecycle_state=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="container_repository",
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

    module.exit_json(container_repositories=result)


if __name__ == "__main__":
    main()
