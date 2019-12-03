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
module: oci_suppression
short_description: Create and delete a Suppression in OCI Email Delivery Module
description:
    - Create a OCI Suppression
    - Delete a OCI Suppression, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this Suppression would be created.
                     Mandatory for create operation.
        required: false
    email_address:
        description: Email Address of the Suppression. Mandatory for create operation.
        required: false
    suppression_id:
        description: Identifier of the existing Suppression which required to be deleted.
                     Mandatory for delete.
        required: false
        aliases: ['id']
    state:
        description: Create and delete Suppression. For I(state=present), if it does not exist, it gets created.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Suppression
- name: Create Suppression
  oci_suppression:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    email_address: 'ansible-test@oracle.com'
    state: 'present'

# Delete Suppression
- name: Delete Suppression
  oci_suppression:
    suppression_id: 'ocid1.emailsuppression.oc1..xxxxxEXAMPLExxxxx'
    state: 'absent'
"""

RETURN = """
    suppression:
        description: Attributes of the created Suppression. For delete, deleted Suppression description will be returned.
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

        sample: {
                  "email_address":"ansible-test@oracle.com",
                  "id":"ocid1.emailsuppression.oc1.iad.xxxxxEXAMPLExxxxx",
                  "reason":"MANUAL",
                  "time_created":"2018-10-31T09:20:52.245000+00:00"
                 }
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.email.email_client import EmailClient
    from oci.exceptions import ServiceError, ClientError
    from oci.email.models import CreateSuppressionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_suppression(email_client, module):
    create_suppression_details = CreateSuppressionDetails()
    for attribute in create_suppression_details.attribute_map:
        create_suppression_details.__setattr__(attribute, module.params.get(attribute))

    result = oci_utils.create_resource(
        resource_type="suppression",
        create_fn=email_client.create_suppression,
        kwargs_create={"create_suppression_details": create_suppression_details},
        module=module,
    )
    return result


def delete_suppression(email_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="suppression",
        client=email_client,
        get_fn=email_client.get_suppression,
        kwargs_get={"suppression_id": module.params["suppression_id"]},
        delete_fn=email_client.delete_suppression,
        kwargs_delete={"suppression_id": module.params["suppression_id"]},
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_autonomous_database")
    set_logger(logger)

    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            suppression_id=dict(type="str", required=False, aliases=["id"]),
            email_address=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    email_client = oci_utils.create_service_client(module, EmailClient)
    state = module.params["state"]

    if state == "present":
        try:
            result = oci_utils.check_and_create_resource(
                resource_type="suppression",
                create_fn=create_suppression,
                kwargs_create={"email_client": email_client, "module": module},
                list_fn=email_client.list_suppressions,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module,
                model=CreateSuppressionDetails(),
            )
        except ServiceError as ex:
            get_logger().error("Unable to create suppression due to: %s", ex.message)
            module.fail_json(msg=ex.message)
        except ClientError as ex:
            get_logger().error("Unable to create suppression due to: %s", str(ex))
            module.fail_json(msg=str(ex))
    elif state == "absent":
        result = delete_suppression(email_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
