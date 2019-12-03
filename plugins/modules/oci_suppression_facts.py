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
module: oci_suppression_facts
short_description: Fetches details of OCI Suppression.
description:
    - Fetches details of all OCI Suppression in a compartment or a specific OCI Suppression
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which details of all Suppressions must be fetched.
        required: false
    suppression_id:
        description: Identifier of the Suppression whose details needs to be fetched.
        required: false
        aliases: ['id']
    email_address:
        description: A filter to only return Suppression that match the given Email Adress.
        required: false
    time_created_greater_than_or_equal_to:
        description: Search for suppressions that were created within a specific date range,
                     using this parameter to specify the earliest creation date for the returned
                     list (inclusive). Specifying this parameter without the corresponding
                     time_created_less_than parameter will retrieve suppressions created from the
                     given time_created_greater_than_or_equal_to to the current time, in
                     "YYYY-MM-ddThh:mmZ" format with a Z offset, as defined by RFC 3339.
        required: false
    time_created_less_than:
        description: Search for suppressions that were created within a specific date range,
                     using this parameter to specify the latest creation date for the returned
                     list (exclusive). Specifying this parameter without the corresponding
                     time_created_greater_than_or_equal_to parameter will retrieve all suppressions
                     created before the specified end date, in "YYYY-MM-ddThh:mmZ" format with
                     a Z offset, as defined by RFC 3339.
        required: false

author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Fetch Suppression
- name: List all Suppressions in a compartment
  oci_suppression_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'

# Fetch Suppression with specific Email Address
- name: List suppression in a compartment, filetered by Email Address
  oci_suppression_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      email_address: 'ansible-test@oracle.com'

# Fetch Suppression filtered by time_created_greater_than_or_equal_to
- name: List Suppression in a compartment, filetered by time_created_greater_than_or_equal_to
  oci_suppression_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      time_created_greater_than_or_equal_to: '2018-10-31T09:27:14Z'

# Fetch Suppression filtered by time_created_less_than
- name: List Suppression in a compartment, filetered by time_created_less_than
  oci_suppression_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      time_created_less_than: '2018-10-31T09:27:14Z'

# Fetch Suppression filtered by time_created_greater_than_or_equal_to and time_created_less_than
- name: List Suppression in a compartment, filetered by time_created_greater_than_or_equal_to and time_created_less_than
  oci_suppression_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      time_created_greater_than_or_equal_to: '2018-10-31T09:25:14Z'
      time_created_less_than: '2018-10-31T09:27:14Z'

# Fetch a specific Suppression
- name: List a specific Suppression
  oci_suppression_facts:
      suppression_id: 'ocid1.emailsuppression.oc1..xxxxxEXAMPLExxxxx..qndq'
"""

RETURN = """
    suppressions:
        description: Attributes of the Fetched Suppression.
        returned: success
        type: complex
        contains:
            email_address:
                description: Email Address of the Suppression
                returned: always
                type: string
                sample: ansible-test@oracle.com
            reason:
                description: The reason that the email address was suppressed.
                returned: always
                type: string
                sample: MANUAL
            time_created:
                description: Date and time when the Suppression was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            id:
                description: The identifier of the Suppression
                returned: always
                type: string
                sample: ocid1.emailsuppression.oc1.xzvf..xxxxxEXAMPLExxxxx

        sample: [{
                  "email_address":"ansible-test@oracle.com",
                  "id":"ocid1.emailsuppression.oc1.iad.xxxxxEXAMPLExxxxx",
                  "reason":"MANUAL",
                  "time_created":"2018-10-31T09:20:52.245000+00:00"
                 },
                 {
                  "email_address":"ansible-user@oracle.com",
                  "id":"ocid1.emailsuppression.oc1.iad.xxxxxEXAMPLExxxxx",
                  "reason":"MANUAL",
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


def list_suppressions(email_client, module):
    result = dict(suppressions="")
    compartment_id = module.params.get("compartment_id")
    suppression_id = module.params.get("suppression_id")
    try:
        if compartment_id:
            get_logger().debug(
                "Listing all suppressions under compartment %s", compartment_id
            )
            optional_list_method_params = [
                "email_address",
                "time_created_greater_than_or_equal_to",
                "time_created_less_than",
            ]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_suppressions_summary = to_dict(
                oci_utils.list_all_resources(
                    email_client.list_suppressions,
                    compartment_id=compartment_id,
                    **optional_kwargs
                )
            )
            existing_suppressions = [
                oci_utils.call_with_backoff(
                    email_client.get_suppression, suppression_id=suppression["id"]
                ).data
                for suppression in existing_suppressions_summary
            ]
        elif suppression_id:
            get_logger().debug("Listing suppression %s", suppression_id)
            response = oci_utils.call_with_backoff(
                email_client.get_suppression, suppression_id=suppression_id
            )
            existing_suppressions = [response.data]
    except ServiceError as ex:
        get_logger().error("Unable to list suppressions due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["suppressions"] = to_dict(existing_suppressions)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_suppression_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            suppression_id=dict(type="str", required=False, aliases=["id"]),
            time_created_greater_than_or_equal_to=dict(type="str", required=False),
            time_created_less_than=dict(type="str", required=False),
            email_address=dict(type=str, required=False),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "suppression_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    email_client = oci_utils.create_service_client(module, EmailClient)
    result = list_suppressions(email_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
