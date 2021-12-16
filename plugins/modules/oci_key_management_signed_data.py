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
module: oci_key_management_signed_data
short_description: Manage a SignedData resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a SignedData resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a digital signature for a message or message digest by using the private key of a public-private key pair,
      also known as an asymmetric key. To verify the generated signature, you can use the
      L(Verify,https://docs.cloud.oracle.com/api/#/en/key/latest/VerifiedData/Verify)
      operation. Or, if you want to validate the signature outside of the service, you can do so by using the public key of the same asymmetric key.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    msg:
        description:
            - The base64-encoded binary data object denoting the message or message digest to sign. You can have a message up to 4096 bytes in size. To sign a
              larger message, provide the message digest.
        type: str
        aliases: ["message"]
        required: true
    key_id:
        description:
            - The OCID of the key used to sign the message.
        type: str
        required: true
    key_version_id:
        description:
            - The OCID of the key version used to sign the message.
        type: str
    message_type:
        description:
            - Denotes whether the value of the message parameter is a raw message or a message digest.
              The default value, `RAW`, indicates a message. To indicate a message digest, use `DIGEST`.
        type: str
        choices:
            - "RAW"
            - "DIGEST"
    signing_algorithm:
        description:
            - "The algorithm to use to sign the message or message digest.
              For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with
              different hashing algorithms.
              For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms.
              When you pass a message digest for signing, ensure that you specify the same hashing algorithm
              as used when creating the message digest."
        type: str
        choices:
            - "SHA_224_RSA_PKCS_PSS"
            - "SHA_256_RSA_PKCS_PSS"
            - "SHA_384_RSA_PKCS_PSS"
            - "SHA_512_RSA_PKCS_PSS"
            - "SHA_224_RSA_PKCS1_V1_5"
            - "SHA_256_RSA_PKCS1_V1_5"
            - "SHA_384_RSA_PKCS1_V1_5"
            - "SHA_512_RSA_PKCS1_V1_5"
            - "ECDSA_SHA_256"
            - "ECDSA_SHA_384"
            - "ECDSA_SHA_512"
        required: true
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
    state:
        description:
            - The state of the SignedData.
            - Use I(state=present) to create a SignedData.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create signed_data
  oci_key_management_signed_data:
    # required
    msg: msg_example
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    signing_algorithm: SHA_224_RSA_PKCS_PSS

    # optional
    key_version_id: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
    message_type: RAW
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
signed_data:
    description:
        - Details of the SignedData resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key_id:
            description:
                - The OCID of the key used to sign the message.
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        key_version_id:
            description:
                - The OCID of the key version used to sign the message.
            returned: on success
            type: str
            sample: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
        signature:
            description:
                - The base64-encoded binary data object denoting the cryptographic signature generated for the message or message digest.
            returned: on success
            type: str
            sample: signature_example
        signing_algorithm:
            description:
                - "The algorithm to use to sign the message or message digest.
                  For RSA keys, supported signature schemes include PKCS #1 and RSASSA-PSS, along with
                  different hashing algorithms.
                  For ECDSA keys, ECDSA is the supported signature scheme with different hashing algorithms.
                  When you pass a message digest for signing, ensure that you specify the same hashing algorithm
                  as used when creating the message digest."
            returned: on success
            type: str
            sample: SHA_224_RSA_PKCS_PSS
    sample: {
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "key_version_id": "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx",
        "signature": "signature_example",
        "signing_algorithm": "SHA_224_RSA_PKCS_PSS"
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
    from oci.key_management import KmsCryptoClient
    from oci.key_management.models import SignDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SignedDataHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return SignDataDetails

    def create_resource(self):
        create_details = self.get_create_model()
        setattr(create_details, "message", self.module.params.get("msg"))
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.sign,
            call_fn_args=(),
            call_fn_kwargs=dict(sign_data_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


SignedDataHelperCustom = get_custom_class("SignedDataHelperCustom")


class ResourceHelper(SignedDataHelperCustom, SignedDataHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            msg=dict(aliases=["message"], type="str", required=True),
            key_id=dict(type="str", required=True),
            key_version_id=dict(type="str"),
            message_type=dict(type="str", choices=["RAW", "DIGEST"]),
            signing_algorithm=dict(
                type="str",
                required=True,
                choices=[
                    "SHA_224_RSA_PKCS_PSS",
                    "SHA_256_RSA_PKCS_PSS",
                    "SHA_384_RSA_PKCS_PSS",
                    "SHA_512_RSA_PKCS_PSS",
                    "SHA_224_RSA_PKCS1_V1_5",
                    "SHA_256_RSA_PKCS1_V1_5",
                    "SHA_384_RSA_PKCS1_V1_5",
                    "SHA_512_RSA_PKCS1_V1_5",
                    "ECDSA_SHA_256",
                    "ECDSA_SHA_384",
                    "ECDSA_SHA_512",
                ],
            ),
            service_endpoint=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="signed_data",
        service_client_class=KmsCryptoClient,
        namespace="key_management",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
