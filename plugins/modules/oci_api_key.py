#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_api_key
short_description: Upload and delete API signing key of a user in OCI
description:
    - This module allows the user upload and delete API signing keys of a user in OCI. A PEM-format RSA credential for
      securing requests to the Oracle Cloud Infrastructure REST API. Also known as an API signing key. Specifically,
      this is the public key from the key pair. The private key remains with the user calling the API. For information
      about generating a key pair in the required PEM format, see Required Keys and OCIDs.
      Note that this is not the SSH key for accessing compute instances.
      Each user can have a maximum of three API signing keys.
      For more information about user credentials, see
      U(https://docs.us-phoenix-1.oraclecloud.com/Content/API/Concepts/apisigningkey.htm).
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user whose API signing key needs to be created or deleted.
        required: true
    api_signing_key:
        description: The public key. Must be an RSA key in PEM format. Required when the API signing key is
                     uploaded with I(state=present)
        required: false
        aliases: ['key']
    api_key_id:
        description: The API signing key's id. The Id must be of the format TENANCY_OCID/USER_OCID/KEY_FINGERPRINT.
        required: false
        aliases: ['id']
    state:
        description: The state of the api signing key that must be asserted to. When I(state=present), and the
                     api key doesn't exist, the api key is created with the provided C(api_signing_key).
                     When I(state=absent), the api signing key corresponding to the provided C(fingerprint) is deleted.
        required: false
        default: "present"
        choices: ['present', 'absent']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
- name: Upload a new api signing key for the specified user
  oci_api_key:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    key: "-----BEGIN PUBLIC KEY-----cmdnMIIBIjANBgkqhkiG9w0BAQEFA......mwIDAQAB-----END PUBLIC KEY-----"

- name: Delete an API signing key for the specified user
  oci_api_key:
        user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
        "id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx/ocid1.user.oc1..xxxxxEXAMPLExxxxx/08:07:a6:7d:06:b4:73:91:e9:2c:da"
        state: "absent"
"""

RETURN = """
oci_api_key:
    description: Details of the API signing key
    returned: On success
    type: dict
    sample: {
        "fingerprint": "08:07:a6:7d:06:b4:73:91:e9:2c:da:42:c8:cb:df:02",
        "inactive_status": null,
        "key_id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx/ocid1.user.oc1..xxxxxEXAMPLExxxxx/08:07:a6:7d:06:b4:73:91:e9:2c:da",
        "key_value": "-----BEGIN PUBLIC KEY-----...urt/fN8jNz2nZwIDAQAB-----END PUBLIC KEY-----",
        "lifecycle_state": "ACTIVE",
        "time_created": "2018-01-08T09:33:59.705000+00:00",
        "user_id": "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
     }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_common_utils
from ansible.module_utils.oracle.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)


try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import CreateApiKeyDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class ApiKeyHelperGen(OCIResourceHelperBase):
    @staticmethod
    def get_module_resource_id_param():
        return "api_key_id"

    def get_module_resource_id(self):
        return self.module.params.get("api_key_id")

    def get_create_model_class(self):
        return CreateApiKeyDetails

    def list_resources(self):
        return oci_common_utils.list_all_resources(
            self.client.list_api_keys, user_id=self.module.params.get("user_id")
        )

    def create_resource(self):
        create_api_key_details = self.get_create_model()
        return oci_common_utils.call_with_backoff(
            self.client.upload_api_key,
            user_id=self.module.params.get("user_id"),
            create_api_key_details=create_api_key_details,
        )

    def delete_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.delete_api_key,
            user_id=self.module.params.get("user_id"),
            fingerprint=self.module.params.get("fingerprint"),
        )


ApiKeyHelperCustom = get_custom_class("ApiKeyHelperCustom")


class ResourceHelper(ApiKeyHelperCustom, ApiKeyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            api_key_id=dict(type="str", required=False, aliases=["id"]),
            key=dict(type="str", required=False, aliases=["api_signing_key"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module, resource_type="api_key", service_client_class=IdentityClient
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()
    elif resource_helper.is_action():
        result = resource_helper.perform_action(module.params.get("state"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
