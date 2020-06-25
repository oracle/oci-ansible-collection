#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
    - For I(state=present), decrypts data using the given L(DecryptDataDetails,https://docs.cloud.oracle.com/api/#/en/key/release/datatypes/DecryptDataDetails)
      resource.
version_added: "2.9"
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
    ciphertext: AAwgpauIe9AAAM6dU7pS7AKwmDFyXOqNh0uAvNY9a3E95rw7Ae3LZNBnDtHWdkB1l/pIDBfg
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
            type: string
            sample: plaintext_example
        plaintext_checksum:
            description:
                - Checksum of the decrypted data.
            returned: on success
            type: string
            sample: plaintext_checksum_example
    sample: {
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
    from oci.key_management.models import DecryptDataDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DecryptedDataHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

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
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
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
            service_endpoint=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
