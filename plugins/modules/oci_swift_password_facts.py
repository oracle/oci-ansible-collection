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
    "status": ["deprecated"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_swift_password_facts
short_description: Retrieve details of swift passwords for a specified user
description:
    - This module retrieves details of swift passwords of a specified user. T This module is deprecated.
      Please use M(oci_auth_token_facts) instead. This module may be removed in a future release. The returned object
      contains the swift password's OCID, but not the password itself. The actual password is returned only upon
      creation of a swift password using the M(oci_swift_password) module.
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user
        required: true
    swift_password_id:
        description: The OCID of the swift password. Required when facts about a specific swift password for the
                     specified user needs to be obtained.
        required: false
        aliases: ['id']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of all the swift passwords of the specified user
  oci_swift_password_facts:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"

- name: Get details of a specific swift password of a user
  oci_swift_password_facts:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    id: "ocid1.credential.oc1..xxxxxEXAMPLExxxxx"
"""

RETURN = """
swift_passwords:
    description: Information about one or more swift passwords in the specified user
    returned: on success
    type: complex
    contains:
        id:
            description: The OCID of the Swift password.
            returned: always
            type: string
            sample: ocid1.credential.oc1..xxxxxEXAMPLExxxxx
        user_id:
            description: The OCID of the user the password belongs to.
            returned: always
            type: string
            sample: ocid1.user.oc1..xxxxxEXAMPLExxxxx
        description:
            description: The description that was assigned to the Swift password.
            returned: always
            type: string
            sample: "My first swift password description"
        time_created:
            description: Date and time the SwiftPassword object was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2016-08-25T21:10:29.600Z
        expires_on:
            description: Date and time when this password will expire, in the format defined by RFC3339. Null if it
                         never expires.
            returned: always
            type: string
            sample: 2016-08-25T21:10:29.600Z
        lifecycle_state:
            description: The password's current state.
            returned: always
            type: string
            sample: ACTIVE
        inactive_status:
            description: The detailed status of INACTIVE lifecycleState.
            returned: only when the I(lifecycle_state) is 'INACTIVE'
            type: string
    sample: {
       "swift_passwords": [
             {
                "description": "My first swift password description",
                "expires_on": null,
                "id": "ocid1.credential.oc1..xxxxxEXAMPLExxxxx",
                "inactive_status": null,
                "lifecycle_state": "ACTIVE",
                "password": null,
                "time_created": "2018-01-03T13:15:53.082000+00:00",
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


def list_swift_passwords(identity_client, user_id, sw_pass_id, module):
    try:
        swift_passwords = oci_utils.call_with_backoff(
            identity_client.list_swift_passwords, user_id=user_id
        ).data
        if sw_pass_id:
            return next(
                (
                    to_dict([sw_pass])
                    for sw_pass in swift_passwords
                    if sw_pass.id == sw_pass_id
                ),
                {},
            )
        return to_dict(swift_passwords)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            swift_password_id=dict(
                type="str", required=False, aliases=["id"], no_log=True
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    user_id = module.params.get("user_id")
    id = module.params.get("swift_password_id", None)
    result = list_swift_passwords(identity_client, user_id, id, module)

    module.exit_json(swift_passwords=result)


if __name__ == "__main__":
    main()
