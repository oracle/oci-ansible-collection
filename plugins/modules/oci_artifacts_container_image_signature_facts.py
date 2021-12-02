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
module: oci_artifacts_container_image_signature_facts
short_description: Fetches details about one or multiple ContainerImageSignature resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ContainerImageSignature resources in Oracle Cloud Infrastructure
    - List container image signatures in an image.
    - If I(image_signature_id) is specified, the details of a single ContainerImageSignature will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    image_signature_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container image signature.
            - "Example: `ocid1.containersignature.oc1..exampleuniqueID`"
            - Required to get a specific container_image_signature.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple container_image_signatures.
        type: str
    compartment_id_in_subtree:
        description:
            - When set to true, the hierarchy of compartments is traversed
              and all compartments and subcompartments in the tenancy are
              inspected depending on the the setting of `accessLevel`.
              Default is false. Can only be set to true when calling the API
              on the tenancy (root compartment).
        type: bool
    image_id:
        description:
            - A filter to return a container image summary only for the specified container image OCID.
        type: str
    repository_id:
        description:
            - A filter to return container images only for the specified container repository OCID.
        type: str
    repository_name:
        description:
            - A filter to return container images or container image signatures that match the repository name.
            - "Example: `foo` or `foo*`"
        type: str
    image_digest:
        description:
            - The digest of the container image.
            - "Example: `sha256:e7d38b3517548a1c71e41bffe9c8ae6d6d29546ce46bf62159837aad072c90aa`"
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
    kms_key_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the kmsKeyVersionId used to sign the container image.
            - "Example: `ocid1.keyversion.oc1..exampleuniqueID`"
        type: str
    kms_key_version_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the kmsKeyVersionId used to sign the container image.
            - "Example: `ocid1.keyversion.oc1..exampleuniqueID`"
        type: str
    signing_algorithm:
        description:
            - The algorithm to be used for signing. These are the only supported signing algorithms for container images.
        type: str
        choices:
            - "SHA_224_RSA_PKCS_PSS"
            - "SHA_256_RSA_PKCS_PSS"
            - "SHA_384_RSA_PKCS_PSS"
            - "SHA_512_RSA_PKCS_PSS"
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
- name: Get a specific container_image_signature
  oci_artifacts_container_image_signature_facts:
    # required
    image_signature_id: "ocid1.containersignature.oc1..exampleuniqueID"

- name: List container_image_signatures
  oci_artifacts_container_image_signature_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id_in_subtree: true
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
    repository_name: foo
    image_digest: sha256:e7d38b3517548a1c71e41bffe9c8ae6d6d29546ce46bf62159837aad072c90aa
    display_name: display_name_example
    kms_key_id: "ocid1.keyversion.oc1..exampleuniqueID"
    kms_key_version_id: "ocid1.keyversion.oc1..exampleuniqueID"
    signing_algorithm: SHA_224_RSA_PKCS_PSS
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
container_image_signatures:
    description:
        - List of ContainerImageSignature resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the container repository
                  exists.
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
                - The last 10 characters of the kmsKeyId, the last 10 characters of the kmsKeyVersionId, the signingAlgorithm, and the last 10 characters of the
                  signatureId.
                - "Example: `wrmz22sixa::qdwyc2ptun::SHA_256_RSA_PKCS_PSS::2vwmobasva`"
            returned: on success
            type: str
            sample: wrmz22sixa::qdwyc2ptun::SHA_256_RSA_PKCS_PSS::2vwmobasva
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the container image signature.
                - "Example: `ocid1.containerimagesignature.oc1..exampleuniqueID`"
            returned: on success
            type: str
            sample: "ocid1.containerimagesignature.oc1..exampleuniqueID"
        image_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the container image.
                - "Example: `ocid1.containerimage.oc1..exampleuniqueID`"
            returned: on success
            type: str
            sample: "ocid1.containerimage.oc1..exampleuniqueID"
        kms_key_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the kmsKeyId used to sign the container image.
                - "Example: `ocid1.key.oc1..exampleuniqueID`"
            returned: on success
            type: str
            sample: "ocid1.key.oc1..exampleuniqueID"
        kms_key_version_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the kmsKeyVersionId used to sign the container image.
                - "Example: `ocid1.keyversion.oc1..exampleuniqueID`"
            returned: on success
            type: str
            sample: "ocid1.keyversion.oc1..exampleuniqueID"
        message:
            description:
                - The base64 encoded signature payload that was signed.
            returned: on success
            type: str
            sample: message_example
        signature:
            description:
                - The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.
            returned: on success
            type: str
            sample: signature_example
        signing_algorithm:
            description:
                - The algorithm to be used for signing. These are the only supported signing algorithms for container images.
            returned: on success
            type: str
            sample: SHA_224_RSA_PKCS_PSS
        time_created:
            description:
                - An RFC 3339 timestamp indicating when the image was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "created_by": "created_by_example",
        "display_name": "wrmz22sixa::qdwyc2ptun::SHA_256_RSA_PKCS_PSS::2vwmobasva",
        "id": "ocid1.containerimagesignature.oc1..exampleuniqueID",
        "image_id": "ocid1.containerimage.oc1..exampleuniqueID",
        "kms_key_id": "ocid1.key.oc1..exampleuniqueID",
        "kms_key_version_id": "ocid1.keyversion.oc1..exampleuniqueID",
        "message": "message_example",
        "signature": "signature_example",
        "signing_algorithm": "SHA_224_RSA_PKCS_PSS",
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


class ContainerImageSignatureFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "image_signature_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_image_signature,
            image_signature_id=self.module.params.get("image_signature_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
            "image_id",
            "repository_id",
            "repository_name",
            "image_digest",
            "display_name",
            "kms_key_id",
            "kms_key_version_id",
            "signing_algorithm",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_container_image_signatures,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ContainerImageSignatureFactsHelperCustom = get_custom_class(
    "ContainerImageSignatureFactsHelperCustom"
)


class ResourceFactsHelper(
    ContainerImageSignatureFactsHelperCustom, ContainerImageSignatureFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            image_signature_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            compartment_id_in_subtree=dict(type="bool"),
            image_id=dict(type="str"),
            repository_id=dict(type="str"),
            repository_name=dict(type="str"),
            image_digest=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            kms_key_id=dict(type="str"),
            kms_key_version_id=dict(type="str"),
            signing_algorithm=dict(
                type="str",
                choices=[
                    "SHA_224_RSA_PKCS_PSS",
                    "SHA_256_RSA_PKCS_PSS",
                    "SHA_384_RSA_PKCS_PSS",
                    "SHA_512_RSA_PKCS_PSS",
                ],
            ),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="container_image_signature",
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

    module.exit_json(container_image_signatures=result)


if __name__ == "__main__":
    main()
