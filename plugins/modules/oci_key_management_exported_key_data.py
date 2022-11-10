#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_key_management_exported_key_data
short_description: Manage an ExportedKeyData resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create an ExportedKeyData resource in Oracle Cloud Infrastructure
    - For I(state=present), exports a specific version of a master encryption key according to the details of the request. For their protection,
      keys that you create and store on a hardware security module (HSM) can never leave the HSM. You can only export keys
      stored on the server. For export, the key version is encrypted by an RSA public key that you provide.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    key_id:
        description:
            - The OCID of the master encryption key associated with the key version you want to export.
        type: str
        required: true
    key_version_id:
        description:
            - The OCID of the specific key version to export. If not specified, the service exports the current key version.
        type: str
    algorithm:
        description:
            - The encryption algorithm to use to encrypt exportable key material from a software-backed key. Specifying `RSA_OAEP_AES_SHA256`
              invokes the RSA AES key wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped by the RSA public
              wrapping key provided along with the request, creating a wrapped temporary AES key. The temporary AES key is also used to wrap
              the exportable key material. The wrapped temporary AES key and the wrapped exportable key material are concatenated, producing
              concatenated blob output that jointly represents them. Specifying `RSA_OAEP_SHA256` means that the software key is wrapped by
              the RSA public wrapping key provided along with the request.
        type: str
        choices:
            - "RSA_OAEP_AES_SHA256"
            - "RSA_OAEP_SHA256"
        required: true
    public_key:
        description:
            - The PEM format of the 2048-bit, 3072-bit, or 4096-bit RSA wrapping key in your possession that you want to use to encrypt the key.
        type: str
        required: true
    logging_context:
        description:
            - Information that provides context for audit logging. You can provide this additional
              data as key-value pairs to include in the audit logs when audit logging is enabled.
        type: dict
    service_endpoint:
        description:
            - The endpoint of the service to call using this client. For example 'https://kms.{region}.{secondLevelDomain}'.
        type: str
        required: true
    state:
        description:
            - The state of the ExportedKeyData.
            - Use I(state=present) to create an ExportedKeyData.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create exported_key_data
  oci_key_management_exported_key_data:
    # required
    key_id: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
    algorithm: RSA_OAEP_AES_SHA256
    public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."

    # optional
    key_version_id: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
    logging_context: null
    service_endpoint: "https://xxx.kms.{region}.oraclecloud.com"

"""

RETURN = """
exported_key_data:
    description:
        - Details of the ExportedKeyData resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key_version_id:
            description:
                - The OCID of the key version.
            returned: on success
            type: str
            sample: "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx"
        key_id:
            description:
                - The OCID of the master encryption key associated with this key version.
            returned: on success
            type: str
            sample: "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time this key version was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339) timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vault_id:
            description:
                - The OCID of the vault that contains this key version.
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        encrypted_key:
            description:
                - The base64-encoded exported key material, which is encrypted by using the public RSA wrapping key specified in the export request.
            returned: on success
            type: str
            sample: encrypted_key_example
        algorithm:
            description:
                - The encryption algorithm to use to encrypt exportable key material from a key that persists on the server (as opposed to a key that
                  persists on a hardware security module and, therefore, cannot be exported). Specifying RSA_OAEP_AES_SHA256 invokes the RSA AES key
                  wrap mechanism, which generates a temporary AES key. The temporary AES key is wrapped by the RSA public wrapping key provided along
                  with the request, creating a wrapped temporary AES key. The temporary AES key is also used to wrap the exportable key material. The
                  wrapped temporary AES key and the wrapped exportable key material are concatenated, producing concatenated blob output that jointly
                  represents them. Specifying RSA_OAEP_SHA256 means that the exportable key material is wrapped by the RSA public wrapping key provided
                  along with the request.
            returned: on success
            type: str
            sample: RSA_OAEP_AES_SHA256
    sample: {
        "key_version_id": "ocid1.keyversion.oc1..xxxxxxEXAMPLExxxxxx",
        "key_id": "ocid1.key.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "encrypted_key": "encrypted_key_example",
        "algorithm": "RSA_OAEP_AES_SHA256"
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
    from oci.key_management.models import ExportKeyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ExportedKeyDataHelperGen(OCIResourceHelperBase):
    """Supported operations: create"""

    def get_possible_entity_types(self):
        return super(ExportedKeyDataHelperGen, self).get_possible_entity_types() + [
            "exportedkeydata",
            "keyManagementexportedkeydata",
            "exportedkeydataresource",
            "exportkey",
            "exportkeys",
            "keyManagementexportkey",
            "keyManagementexportkeys",
            "exportkeyresource",
            "exportkeysresource",
            "keymanagement",
        ]

    def get_module_resource_id(self):
        return None

    # There is no idempotency for this module (no get or list ops)
    def get_matching_resource(self):
        return None

    def get_create_model_class(self):
        return ExportKeyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.export_key,
            call_fn_args=(),
            call_fn_kwargs=dict(export_key_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )


ExportedKeyDataHelperCustom = get_custom_class("ExportedKeyDataHelperCustom")


class ResourceHelper(ExportedKeyDataHelperCustom, ExportedKeyDataHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            key_id=dict(type="str", required=True),
            key_version_id=dict(type="str"),
            algorithm=dict(
                type="str",
                required=True,
                choices=["RSA_OAEP_AES_SHA256", "RSA_OAEP_SHA256"],
            ),
            public_key=dict(type="str", required=True),
            logging_context=dict(type="dict"),
            service_endpoint=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="exported_key_data",
        service_client_class=KmsCryptoClient,
        namespace="key_management",
    )

    result = dict(changed=False)

    if resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
