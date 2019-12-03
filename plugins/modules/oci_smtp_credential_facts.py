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
module: oci_smtp_credential_facts
short_description: Retrieve facts of SMTP credentials in OCI Identity and Access Management Service
description:
    - This module retrieves information of all the SMTP credentials for a specified user.
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user.
        required: true
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""


EXAMPLES = """
- name: Get information of all the SMTP credentials for a specific user
  oci_smtp_credential_facts:
    user_id: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
"""


RETURN = """
smtp_credentials:
    description: Attributes of the fetched SMTP credential
    returned: On successful operation
    type: complex
    contains:
        user_name:
            description: The SMTP user name.
            returned: always
            type: string
            sample: "ocid1.user.oc1.xxxxxEXAMPLExxxxx.@ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx.za.com"
        id:
            description: The OCID of the SMTP credential.
            returned: always
            type: string
            sample: ocid1.credential.oc1..xxxxxEXAMPLExxxxx...l5aq
        user_id:
            description: The OCID of the user the SMTP credential belongs to.
            returned: always
            type: string
            sample: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
        description:
            description: The description you assign to the SMTP credential. Does not have to be unique,
                         and it's changeable.
            returned: always
            type: string
            sample: "Test SMTP credential"
        lifecycle_state:
            description: The credential's current state.
            returned: always
            type: string
            sample: ACTIVE
        inactive_status:
            description: The detailed status of INACTIVE lifecycle state.
            returned: always
            type: string
            sample: null
        time_created:
            description: Date and time the SmtpCredential object was created, in the format defined by RFC3339.
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
              "description":"Test SMTP credential",
              "id":"ocid1.credential.oc1..xxxxxEXAMPLExxxxx",
              "inactive_status":null,
              "lifecycle_state":"ACTIVE",
              "password":".bi9zaqZ8Gr",
              "time_created":"2018-11-13T06:45:32.246000+00:00",
              "time_expires":null,
              "user_id":"ocid1.user.oc1..xxxxxEXAMPLExxxxx",
              "username":"ocid1.user.oc1..xxxxxEXAMPLExxxxx@ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx.za.com"
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


def list_smtp_credentials(identity_client, module):
    result = dict(smtp_credentials="")
    user_id = module.params.get("user_id")
    try:
        get_logger().debug("Listing all SMTP credentials for User %s", user_id)
        existing_smtp_credentials = to_dict(
            oci_utils.list_all_resources(
                identity_client.list_smtp_credentials, user_id=user_id
            )
        )
    except ServiceError as ex:
        get_logger().error("Unable to list SMTP credentials due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["smtp_credentials"] = to_dict(existing_smtp_credentials)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_smtp_credential_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(user_id=dict(type="str", required=True)))

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    result = list_smtp_credentials(identity_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
