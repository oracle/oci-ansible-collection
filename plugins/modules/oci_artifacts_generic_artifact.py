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
module: oci_artifacts_generic_artifact
short_description: Manage a GenericArtifact resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a GenericArtifact resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    artifact_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the artifact.
            - "Example: `ocid1.genericartifact.oc1..exampleuniqueID`"
        type: str
        aliases: ["id"]
        required: true
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    state:
        description:
            - The state of the GenericArtifact.
            - Use I(state=present) to update an existing a GenericArtifact.
            - Use I(state=absent) to delete a GenericArtifact.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update generic_artifact
  oci_artifacts_generic_artifact:
    # required
    artifact_id: "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete generic_artifact
  oci_artifacts_generic_artifact:
    # required
    artifact_id: "ocid1.artifact.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
generic_artifact:
    description:
        - Details of the GenericArtifact resource acted upon by the current operation
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
    sample: {
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
    from oci.artifacts.models import UpdateGenericArtifactDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GenericArtifactHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "artifact_id"

    def get_module_resource_id(self):
        return self.module.params.get("artifact_id")

    def get_get_fn(self):
        return self.client.get_generic_artifact

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_generic_artifact,
            artifact_id=self.module.params.get("artifact_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "repository_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_generic_artifacts, **kwargs
        )

    def get_update_model_class(self):
        return UpdateGenericArtifactDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_generic_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(
                artifact_id=self.module.params.get("artifact_id"),
                update_generic_artifact_details=update_details,
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
            call_fn=self.client.delete_generic_artifact,
            call_fn_args=(),
            call_fn_kwargs=dict(artifact_id=self.module.params.get("artifact_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


GenericArtifactHelperCustom = get_custom_class("GenericArtifactHelperCustom")


class ResourceHelper(GenericArtifactHelperCustom, GenericArtifactHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            artifact_id=dict(aliases=["id"], type="str", required=True),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="generic_artifact",
        service_client_class=ArtifactsClient,
        namespace="artifacts",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
