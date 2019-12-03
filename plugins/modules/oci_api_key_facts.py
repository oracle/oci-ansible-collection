#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_api_key_facts
short_description: Retrieve details of api signing keys for a specified user
description:
    - This module retrieves details of api signing keys of a specified user. Note that this is not the SSH key for
      accessing compute instances. This is the credential for securing requests to the Oracle Cloud Infrastructure
      REST API.
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user whose API signing keys must be retrieved
        required: true
    api_key_id:
        description: The OCID of the api signing key. Required when facts about a specific api signing key for the
                     specified user needs to be obtained.
        required: false
        aliases: ['id']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of all the api signing keys of the specified user
  oci_api_key_facts:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"

- name: Get details of a specific api signing key of a user
  oci_api_key_facts:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    id: "ocid1.credential.oc1..xxxxxEXAMPLExxxxx"
"""

RETURN = """
api_keys:
    description: Information about one or more api signing keys of the specified user
    returned: on success
    type: complex
    contains:
        key_id:
            description: The OCID of the API signing key. An Oracle-assigned identifier for the key, in this format
                         TENANCY_OCID/USER_OCID/KEY_FINGERPRINT.
            returned: always
            type: string
            sample: "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx/ocid1.user.oc1..xxxxxEXAMPLExxxxx/08:07:a6:7d:06:b4:73:91:e9:2c:da"
        key_value:
            description: The key's value.
            returned: always
            type: string
            sample: "-----BEGIN PUBLIC KEY-----...urt/fN8jNz2nZwIDAQAB-----END PUBLIC KEY-----"
        fingerprint:
            description: The key's fingerprint
            returned: always
            type: string
            sample: 12:34:56:78:90:ab:cd:ef:12:34:56:78:90:ab:cd:ef
        user_id:
            description: Date and time the ApiKey object was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_status:
            description: The API key's current state.
            returned: always
            type: string
            sample: ACTIVE
        inactive_status:
            description: The detailed status of INACTIVE lifecycleState.
            returned: Only when the I(lifecycle_state) is 'INACTIVE'
            type: string
            sample: null
    sample: {
       "api_keys": [
             {
                "fingerprint": "08:07:a6:7d:06:b4:73:91:e9:2c:da:42:c8:cb:df:02",
                "inactive_status": null,
                "key_id": "ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx/ocid1.user.oc1..xxxxxEXAMPLExxxxx/08:07:a6:7d:06:b4:73:91:e9:2c:da",
                "key_value": "-----BEGIN PUBLIC KEY-----...urt/fN8jNz2nZwIDAQAB-----END PUBLIC KEY-----",
                "lifecycle_state": "ACTIVE",
                "time_created": "2018-01-08T09:33:59.705000+00:00",
                "user_id": "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
           }
         ]
       }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_api_keys(identity_client, user_id, api_key_id, module):
    try:
        api_keys = oci_utils.call_with_backoff(
            identity_client.list_api_keys, user_id=user_id
        ).data
        if api_key_id:
            return next(
                (
                    to_dict([api_key])
                    for api_key in api_keys
                    if api_key.key_id == api_key_id
                ),
                {},
            )
        return to_dict(api_keys)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            api_key_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    user_id = module.params.get("user_id")
    api_key_id = module.params.get("api_key_id", None)
    result = list_api_keys(identity_client, user_id, api_key_id, module)

    module.exit_json(api_keys=result)


if __name__ == "__main__":
    main()
