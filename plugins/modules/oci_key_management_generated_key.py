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
module: oci_key_management_generated_key
short_description: Manage a GeneratedKey resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create a GeneratedKey resource in Oracle Cloud Infrastructure
    - For I(state=present), generates a key that you can use to encrypt or decrypt data.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    associated_data:
        description:
            - Information that can be used to provide an encryption context for the encrypted data.
              The length of the string representation of the associated data must be fewer than 4096
              characters.
        type: dict
    include_plaintext_key:
        description:
            - If true, the generated key is also returned unencrypted.
        type: bool
        required: true
    key_id:
        description:
            - The OCID of the master encryption key to encrypt the generated data encryption key with.
        type: str
        required: true
    key_shape:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            algorithm:
                description:
                    - The algorithm used by a key's key versions to encrypt or decrypt.
                type: str
                choices:
                    - "AES"
                    - "RSA"
                    - "ECDSA"
                required: true
            length:
                description:
                    - "The length of the key in bytes, expressed as an integer. Supported values include the following:
                        - AES: 16, 24, or 32
                        - RSA: 256, 384, or 512
                        - ECDSA: 32, 48, or 66"
                type: int
                required: true
            curve_id:
                description:
                    - Supported curve IDs for ECDSA keys.
                type: str
                choices:
                    - "NIST_P256"
                    - "NIST_P384"
                    - "NIST_P521"
    logging_context:
        description:
            - Information that provides context for audit logging. You can provide this additional
              data by formatting it as key-value pairs to include in audit logs when audit logging is enabled.
        type: dict
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
    state:
        description:
            - The state of the GeneratedKey.
            - Use I(state=present) to create a GeneratedKey.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create generated_key
  oci_key_management_generated_key:
    include_plaintext_key: true
    key_id: "ocid1.key.oc1.iad.exampledaaeug.examplestkvmbjdnbickxcvbotxd5q23tteidhj4q2c6qfauxm32i577yu5a"
    key_shape:
      algorithm: "AES"
      length: 16
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
generated_key:
    description:
        - Details of the GeneratedKey resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        ciphertext:
            description:
                - The encrypted data encryption key generated from a master encryption key.
            returned: on success
            type: str
            sample: ciphertext_example
        plaintext:
            description:
                - "The plaintext data encryption key, a base64-encoded sequence of random bytes, which is
                  included if the L(GenerateDataEncryptionKey,https://docs.cloud.oracle.com/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey)
                  request includes the `includePlaintextKey` parameter and sets its value to \\"true\\"."
            returned: on success
            type: str
            sample: plaintext_example
        plaintext_checksum:
            description:
                - "The checksum of the plaintext data encryption key, which is included if the
                  L(GenerateDataEncryptionKey,https://docs.cloud.oracle.com/api/#/en/key/latest/GeneratedKey/GenerateDataEncryptionKey)
                  request includes the `includePlaintextKey` parameter and sets its value to \\"true\\"."
            returned: on success
            type: str
            sample: plaintext_checksum_example
    sample: {
        "ciphertext": "ciphertext_example",
        "plaintext": "plaintext_example",
        "plaintext_checksum": "plaintext_checksum_example"
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
    from oci.key_management.models import GenerateKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GeneratedKeyHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return GenerateKeyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_data_encryption_key,
            call_fn_args=(),
            call_fn_kwargs=dict(generate_key_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


GeneratedKeyHelperCustom = get_custom_class("GeneratedKeyHelperCustom")


class ResourceHelper(GeneratedKeyHelperCustom, GeneratedKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            associated_data=dict(type="dict"),
            include_plaintext_key=dict(type="bool", required=True, no_log=True),
            key_id=dict(type="str", required=True),
            key_shape=dict(
                type="dict",
                required=True,
                no_log=False,
                options=dict(
                    algorithm=dict(
                        type="str", required=True, choices=["AES", "RSA", "ECDSA"]
                    ),
                    length=dict(type="int", required=True),
                    curve_id=dict(
                        type="str", choices=["NIST_P256", "NIST_P384", "NIST_P521"]
                    ),
                ),
            ),
            logging_context=dict(type="dict"),
            service_endpoint=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="generated_key",
        service_client_class=KmsCryptoClient,
        namespace="key_management",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
