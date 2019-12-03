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
module: oci_sender_facts
short_description: Fetches details of OCI Sender.
description:
    - Fetches details of all OCI Sender in a compartment or a specific OCI Sender
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which details of all Senders must be fetched.
        required: false
    sender_id:
        description: Identifier of the Sender whose details needs to be fetched.
        required: false
        aliases: ['id']
    email_address:
        description: A filter to only return Sender that match the given Email Adress.
        required: false
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive.
        required: false
        choices: ['CREATING', 'ACTIVE', 'DELETING', 'DELETED']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Fetch Sender
- name: List all Senders in a compartment
  oci_sender_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'

# Fetch Sender with specific Email Address
- name: List Sender in a compartment, filetered by Email Address
  oci_sender_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      email_address: 'ansible-test@oracle.com'

# Fetch Sender filtered by Lifecycle State
- name: List Sender in a compartment, filetered by Lifecycle State
  oci_sender_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      lifecycle_state: 'ACTIVE'

# Fetch a specific Sender
- name: List a specific Sender
  oci_sender_facts:
      sender_id: 'ocid1.emailsender.oc1..xxxxxEXAMPLExxxxx..qndq'
"""

RETURN = """
    senders:
        description: Attributes of the Fetched Sender.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Sender
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..xxxxxEXAMPLExxxxx
            email_address:
                description: Email Address of the Sender
                returned: always
                type: string
                sample: ansible-test@oracle.com
            is_spf:
                description: Value of the SPF field.
                returned: always
                type: boolean
                sample: False
            time_created:
                description: Date and time when the Sender was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            id:
                description: The identifier of the Sender
                returned: always
                type: string
                sample: ocid1.emailsender.oc1.xzvf..xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the Sender.
                returned: always
                type: string
                sample: ACTIVE

        sample: [{
                  "email_address":"ansible-test@oracle.com",
                  "id":"ocid1.emailsender.oc1.iad.xxxxxEXAMPLExxxxx",
                  "is_spf":false,
                  "lifecycle_state":"ACTIVE",
                  "time_created":"2018-10-31T09:20:52.245000+00:00"
                 },
                 {
                  "email_address":"ansible-user@oracle.com",
                  "id":"ocid1.emailsender.oc1.iad.xxxxxEXAMPLExxxxx",
                  "is_spf":false,
                  "lifecycle_state":"ACTIVE",
                  "time_created":"2018-10-31T09:25:52.245000+00:00"
                 }]

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.email.email_client import EmailClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_senders(email_client, module):
    result = dict(senders="")
    compartment_id = module.params.get("compartment_id")
    sender_id = module.params.get("sender_id")
    try:
        if compartment_id:
            get_logger().debug(
                "Listing all senders under compartment %s", compartment_id
            )
            optional_list_method_params = ["email_address", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_senders_summary = to_dict(
                oci_utils.list_all_resources(
                    email_client.list_senders,
                    compartment_id=compartment_id,
                    **optional_kwargs
                )
            )
            existing_senders = [
                oci_utils.call_with_backoff(
                    email_client.get_sender, sender_id=sender["id"]
                ).data
                for sender in existing_senders_summary
            ]
        elif sender_id:
            get_logger().debug("Listing sender %s", sender_id)
            response = oci_utils.call_with_backoff(
                email_client.get_sender, sender_id=sender_id
            )
            existing_senders = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list senders due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["senders"] = to_dict(existing_senders)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_sender_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            sender_id=dict(type="str", required=False, aliases=["id"]),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED"],
            ),
            email_address=dict(type=str, required=False),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args, mutually_exclusive=[["compartment_id", "sender_id"]]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    email_client = oci_utils.create_service_client(module, EmailClient)
    result = list_senders(email_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
