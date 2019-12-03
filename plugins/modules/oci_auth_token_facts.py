#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_auth_token_facts
short_description: Retrieve facts of auth tokens in OCI Identity and Access Management Service
description:
    - This module retrieves information of all the auth tokens for a specified user.
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user.
        required: true
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get information of all the auth tokens for a specific user
  oci_auth_token_facts:
    user_id: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
"""

RETURN = """
auth_groups:
    description: List of auth token information
    returned: On success
    type: complex
    contains:
        token:
            description: The Auth token. The value is available only in the response for CreateAuthToken, and not for
                         ListAuthTokens or UpdateAuthToken. So the value returned by this fact module would always be
                         null.
            returned: always
            type: string
        id:
            description: The OCID of the auth token.
            returned: always
            type: string
            sample: ocid1.credential.oc1..xxxxxEXAMPLExxxxx...l5aq
        user_id:
            description: The OCID of the user the auth token belongs to.
            returned: always
            type: string
            sample: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
        description:
            description: The description you assign to the auth token. Does not have to be unique, and it's changeable.
            returned: always
            type: string
            sample: "My test auth token"
        time_created:
            description: Date and time the AuthToken object was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: "2018-11-08T02:40:25.118000+00:00"
        time_expires:
            description: Date and time when this auth token will expire, in the format defined by RFC3339. Null if it
                         never expires.
            returned: always
            type: string
            sample: null
    sample: [{
            "description": "test auth token 1",
            "id": "ocid1.credential.oc1..xxxxxEXAMPLExxxxx...l5aq",
            "inactive-status": null,
            "lifecycle-state": "ACTIVE",
            "time-created": "2018-11-08T02:40:25.118000+00:00",
            "time-expires": null,
            "token": null,
            "user-id": "ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq"
        }]
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


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(user_id=dict(type="str", required=False)))

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    try:
        result = to_dict(
            oci_utils.list_all_resources(
                identity_client.list_auth_tokens, user_id=module.params["user_id"]
            )
        )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(auth_tokens=result)


if __name__ == "__main__":
    main()
