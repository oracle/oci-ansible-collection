#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_key_management_decrypted_data
short_description: Manage a DecryptedData resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a DecryptedData resource in Oracle Cloud Infrastructure
    - For I(state=present), decrypts data using the given L(DecryptDataDetails,https://docs.cloud.oracle.com/api/#/en/key/latest/datatypes/DecryptDataDetails)
      resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    associated_data:
        description:
            - Information that can be used to provide an encryption context for the encrypted data.
              The length of the string representation of the associated data must be fewer than 4096 characters.
        type: dict
    ciphertext:
        description:
            - The encrypted data to decrypt.
        type: str
        required: true
    key_id:
        description:
            - The OCID of the key used to encrypt the ciphertext.
        type: str
        required: true
    logging_context:
        description:
            - Information that provides context for audit logging. You can provide this additional
              data as key-value pairs to include in audit logs when audit logging is enabled.
        type: dict
    key_version_id:
        description:
            - The OCID of the key version used to encrypt the ciphertext.
        type: str
    encryption_algorithm:
        description:
            - The encryption algorithm to use to encrypt or decrypt data with a customer-managed key.
              `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and
              that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the
              key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP).
              `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash
              and uses OAEP.
        type: str
        choices:
            - "AES_256_GCM"
            - "RSA_OAEP_SHA_1"
            - "RSA_OAEP_SHA_256"
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
    state:
        description:
            - The state of the DecryptedData.
            - Use I(state=present) to create a DecryptedData.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create decrypted_data
  oci_key_management_decrypted_data:
    # required
    ciphertext: ciphertext_example
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    associated_data: null
    logging_context: null
    key_version_id: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
    encryption_algorithm: AES_256_GCM
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
decrypted_data:
    description:
        - Details of the DecryptedData resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        plaintext:
            description:
                - The decrypted data, expressed as a base64-encoded value.
            returned: on success
            type: str
            sample: plaintext_example
        plaintext_checksum:
            description:
                - The checksum of the decrypted data.
            returned: on success
            type: str
            sample: plaintext_checksum_example
        key_id:
            description:
                - The OCID of the key used to encrypt the ciphertext.
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        key_version_id:
            description:
                - The OCID of the key version used to encrypt the ciphertext.
            returned: on success
            type: str
            sample: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
        encryption_algorithm:
            description:
                - The encryption algorithm to use to encrypt and decrypt data with a customer-managed key
                  `AES_256_GCM` indicates that the key is a symmetric key that uses the Advanced Encryption Standard (AES) algorithm and
                  that the mode of encryption is the Galois/Counter Mode (GCM). `RSA_OAEP_SHA_1` indicates that the
                  key is an asymmetric key that uses the RSA encryption algorithm and uses Optimal Asymmetric Encryption Padding (OAEP).
                  `RSA_OAEP_SHA_256` indicates that the key is an asymmetric key that uses the RSA encryption algorithm with a SHA-256 hash
                  and uses OAEP.
            returned: on success
            type: str
            sample: AES_256_GCM
    sample: {
        "plaintext": "plaintext_example",
        "plaintext_checksum": "plaintext_checksum_example",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "key_version_id": "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx",
        "encryption_algorithm": "AES_256_GCM"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.key_management import KmsCryptoClient
    from oci.key_management.models import DecryptDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DecryptedDataHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_possible_entity_types(self):
        return super(DecryptedDataHelperGen, self).get_possible_entity_types() + [
            "decrypteddata",
            "keyManagementdecrypteddata",
            "decrypteddataresource",
            "decrypt",
            "decrypts",
            "keyManagementdecrypt",
            "keyManagementdecrypts",
            "decryptresource",
            "decryptsresource",
            "keymanagement",
        ]

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return DecryptDataDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.decrypt,
            call_fn_args=(),
            call_fn_kwargs=dict(decrypt_data_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


DecryptedDataHelperCustom = get_custom_class("DecryptedDataHelperCustom")


class ResourceHelper(DecryptedDataHelperCustom, DecryptedDataHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            associated_data=dict(type="dict"),
            ciphertext=dict(type="str", required=True),
            key_id=dict(type="str", required=True),
            logging_context=dict(type="dict"),
            key_version_id=dict(type="str"),
            encryption_algorithm=dict(
                type="str",
                choices=["AES_256_GCM", "RSA_OAEP_SHA_1", "RSA_OAEP_SHA_256"],
            ),
            service_endpoint=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="decrypted_data",
        service_client_class=KmsCryptoClient,
        namespace="key_management",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
