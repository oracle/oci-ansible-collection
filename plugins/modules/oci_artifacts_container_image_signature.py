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
module: oci_artifacts_container_image_signature
short_description: Manage a ContainerImageSignature resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a ContainerImageSignature resource in Oracle Cloud Infrastructure
    - For I(state=present), upload a signature to an image.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the container repository exists.
            - Required for create using I(state=present).
        type: str
    image_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the container image.
            - "Example: `ocid1.containerimage.oc1..exampleuniqueID`"
            - Required for create using I(state=present).
        type: str
    kms_key_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the kmsKeyId used to sign the container image.
            - "Example: `ocid1.key.oc1..exampleuniqueID`"
            - Required for create using I(state=present).
        type: str
    kms_key_version_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the kmsKeyVersionId used to sign the container image.
            - "Example: `ocid1.keyversion.oc1..exampleuniqueID`"
            - Required for create using I(state=present).
        type: str
    message:
        description:
            - The base64 encoded signature payload that was signed.
            - Required for create using I(state=present).
        type: str
    signature:
        description:
            - The signature of the message field using the kmsKeyId, the kmsKeyVersionId, and the signingAlgorithm.
            - Required for create using I(state=present).
        type: str
    signing_algorithm:
        description:
            - The algorithm to be used for signing. These are the only supported signing algorithms for container images.
            - Required for create using I(state=present).
        type: str
        choices:
            - "SHA_224_RSA_PKCS_PSS"
            - "SHA_256_RSA_PKCS_PSS"
            - "SHA_384_RSA_PKCS_PSS"
            - "SHA_512_RSA_PKCS_PSS"
    image_signature_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the container image signature.
            - "Example: `ocid1.containersignature.oc1..exampleuniqueID`"
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ContainerImageSignature.
            - Use I(state=present) to create a ContainerImageSignature.
            - Use I(state=absent) to delete a ContainerImageSignature.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create container_image_signature
  oci_artifacts_container_image_signature:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    image_id: "ocid1.containerimage.oc1..exampleuniqueID"
    kms_key_id: "ocid1.key.oc1..exampleuniqueID"
    kms_key_version_id: "ocid1.keyversion.oc1..exampleuniqueID"
    message: message_example
    signature: signature_example
    signing_algorithm: SHA_224_RSA_PKCS_PSS

- name: Delete container_image_signature
  oci_artifacts_container_image_signature:
    image_signature_id: "ocid1.containersignature.oc1..exampleuniqueID"
    state: absent

"""

RETURN = """
container_image_signature:
    description:
        - Details of the ContainerImageSignature resource acted upon by the current operation
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
    sample: {
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
    from oci.artifacts.models import CreateContainerImageSignatureDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ContainerImageSignatureHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_module_resource_id_param(self):
        return "image_signature_id"

    def get_module_resource_id(self):
        return self.module.params.get("image_signature_id")

    def get_get_fn(self):
        return self.client.get_container_image_signature

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_container_image_signature,
            image_signature_id=self.module.params.get("image_signature_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "image_id",
            "kms_key_id",
            "kms_key_version_id",
            "signing_algorithm",
        ]

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
            self.client.list_container_image_signatures, **kwargs
        )

    def get_create_model_class(self):
        return CreateContainerImageSignatureDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_container_image_signature,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_container_image_signature_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_container_image_signature,
            call_fn_args=(),
            call_fn_kwargs=dict(
                image_signature_id=self.module.params.get("image_signature_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ContainerImageSignatureHelperCustom = get_custom_class(
    "ContainerImageSignatureHelperCustom"
)


class ResourceHelper(
    ContainerImageSignatureHelperCustom, ContainerImageSignatureHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            image_id=dict(type="str"),
            kms_key_id=dict(type="str"),
            kms_key_version_id=dict(type="str"),
            message=dict(type="str"),
            signature=dict(type="str"),
            signing_algorithm=dict(
                type="str",
                choices=[
                    "SHA_224_RSA_PKCS_PSS",
                    "SHA_256_RSA_PKCS_PSS",
                    "SHA_384_RSA_PKCS_PSS",
                    "SHA_512_RSA_PKCS_PSS",
                ],
            ),
            image_signature_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="container_image_signature",
        service_client_class=ArtifactsClient,
        namespace="artifacts",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
