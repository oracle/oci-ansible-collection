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
module: oci_customer_secret_key_facts
short_description: Retrieve details of customer secret keys for a specified user
description:
    - This module retrieves details of customer secret keys of a specified user. The returned object contains the
      customer secret key's OCID, but not the password itself. The actual password is returned only upon creation
      of a customer secret key using the M(oci_customer_secret_key) module.
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user
        required: true
    customer_secret_key_id:
        description: The OCID of the customer secret key. Required when facts about a specific customer secret key for
                     the specified user needs to be obtained.
        required: false
        aliases: ['id']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get details of all the customer secret keys of the specified user
  oci_customer_secret_key_facts:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"

- name: Get details of a specific customer secret key of a user
  oci_customer_secret_key_facts:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    id: "ocid1.credential.oc1..xxxxxEXAMPLExxxxx"
"""

RETURN = """
customer_secret_keys:
    description: Information about one or more customer secret keys in the specified user
    returned: on success
    type: complex
    contains:
        id:
            description: The OCID of the Customer secret key:.
            returned: always
            type: string
            sample: ocid1.credential.oc1..xxxxxEXAMPLExxxxx
        user_id:
            description: The OCID of the user the customer secret key belongs to.
            returned: always
            type: string
            sample: ocid1.user.oc1..xxxxxEXAMPLExxxxx'
        description:
            description: The description that was assigned to the Customer secret key.
            returned: always
            type: string
            sample: My first customer secret key description'
        time_created:
            description: Date and time the Customer secret key object was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2016-08-25T21:10:29.600Z
        expires_on:
            description: Date and time when this secret key will expire, in the format defined by RFC3339. Null if it
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
        "customer_secret_keys": [
            {
              'time_expires': None,
              'time_created': '2018-01-08T04:44:17.784000+00:00',
              'lifecycle_state': 'ACTIVE',
              'id': 'ocid1.credential.oc1..xxxxxEXAMPLExxxxx',
              'display_name': 'My first customer secret key description',
              'user_id': 'ocid1.user.oc1..xxxxxEXAMPLExxxxx',
              'inactive_status': None
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


def list_customer_secret_keys(identity_client, user_id, csk_id, module):
    try:
        customer_secret_keys = oci_utils.list_all_resources(
            identity_client.list_customer_secret_keys,
            user_id=user_id,
            display_name=module.params["display_name"],
        )

        if csk_id:
            return next(
                (
                    to_dict([secret_key])
                    for secret_key in customer_secret_keys
                    if secret_key.id == csk_id
                ),
                {},
            )
        return to_dict(customer_secret_keys)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            customer_secret_key_id=dict(
                type="str", required=False, aliases=["id"], no_log=True
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    user_id = module.params.get("user_id")
    id = module.params.get("customer_secret_key_id", None)
    result = list_customer_secret_keys(identity_client, user_id, id, module)

    module.exit_json(customer_secret_keys=result)


if __name__ == "__main__":
    main()
