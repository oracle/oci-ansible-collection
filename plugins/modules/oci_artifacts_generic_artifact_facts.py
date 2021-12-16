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
module: oci_artifacts_generic_artifact_facts
short_description: Fetches details about one or multiple GenericArtifact resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple GenericArtifact resources in Oracle Cloud Infrastructure
    - Lists artifacts in the specified repository.
    - If I(artifact_id) is specified, the details of a single GenericArtifact will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    artifact_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.
            - "Example: `ocid1.genericartifact.oc1..exampleuniqueID`"
            - Required to get a specific generic_artifact.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple generic_artifacts.
        type: str
    repository_id:
        description:
            - A filter to return the artifacts only for the specified repository OCID.
            - Required to list multiple generic_artifacts.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    artifact_path:
        description:
            - Filter results by a prefix for the `artifactPath` and and return artifacts that begin with the specified prefix in their path.
        type: str
    version:
        description:
            - Filter results by a prefix for `version` and return artifacts that that begin with the specified prefix in their version.
        type: str
    sha256:
        description:
            - Filter results by a specified SHA256 digest for the artifact.
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
- name: Get a specific generic_artifact
  oci_artifacts_generic_artifact_facts:
    # required
    artifact_id: "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"

- name: List generic_artifacts
  oci_artifacts_generic_artifact_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    artifact_path: artifact_path_example
    version: version_example
    sha256: sha256_example
    lifecycle_state: lifecycle_state_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
generic_artifacts:
    description:
        - List of GenericArtifact resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.
                - "Example: `ocid1.genericartifact.oc1..exampleuniqueID`"
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The artifact name with the format of `<artifact-path>:<artifact-version>`. The artifact name is truncated to a maximum length of 255.
                - "Example: `project01/my-web-app/artifact-abc:1.0.0`"
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the repository's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        repository_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the repository.
            returned: on success
            type: str
            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        artifact_path:
            description:
                - A user-defined path to describe the location of an artifact. Slashes do not create a directory structure, but you can use slashes to organize
                  the repository. An artifact path does not include an artifact version.
                - "Example: `project01/my-web-app/artifact-abc`"
            returned: on success
            type: str
            sample: artifact_path_example
        version:
            description:
                - A user-defined string to describe the artifact version.
                - "Example: `1.1.0` or `1.2-beta-2`"
            returned: on success
            type: str
            sample: version_example
        sha256:
            description:
                - The SHA256 digest for the artifact. When you upload an artifact to the repository, a SHA256 digest is calculated and added to the artifact
                  properties.
            returned: on success
            type: str
            sample: sha256_example
        size_in_bytes:
            description:
                - The size of the artifact in bytes.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the artifact.
            returned: on success
            type: str
            sample: AVAILABLE
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
        time_created:
            description:
                - An RFC 3339 timestamp indicating when the repository was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
        "artifact_path": "artifact_path_example",
        "version": "version_example",
        "sha256": "sha256_example",
        "size_in_bytes": 56,
        "lifecycle_state": "AVAILABLE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "time_created": "2013-10-20T19:20:30+01:00"
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


class GenericArtifactFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "artifact_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "repository_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_generic_artifact,
            artifact_id=self.module.params.get("artifact_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "artifact_path",
            "version",
            "sha256",
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
            self.client.list_generic_artifacts,
            compartment_id=self.module.params.get("compartment_id"),
            repository_id=self.module.params.get("repository_id"),
            **optional_kwargs
        )


GenericArtifactFactsHelperCustom = get_custom_class("GenericArtifactFactsHelperCustom")


class ResourceFactsHelper(
    GenericArtifactFactsHelperCustom, GenericArtifactFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            artifact_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            repository_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            artifact_path=dict(type="str"),
            version=dict(type="str"),
            sha256=dict(type="str"),
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
        resource_type="generic_artifact",
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

    module.exit_json(generic_artifacts=result)


if __name__ == "__main__":
    main()
