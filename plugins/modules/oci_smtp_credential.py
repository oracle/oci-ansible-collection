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
module: oci_smtp_credential
short_description: Manage SMTP credential in OCI Identity and Access Management service
description:
    - This module allows the user to perform create, delete & update operations on SMTP credential in OCI Identity and
      Access Management service.
version_added: "2.5"
options:
    smtp_credential_id:
        description: The OCID of the SMTP credential. Required to update an SMTP credential with I(state=present) and
                     delete a SMTP credential with I(state=absent)
        required: false
        aliases: ['id']
    description:
        description: The description you assign to the SMTP credential during creation. Does not have to be unique,
                     and it's changeable. Required when creating a SMTP credential with I(state=present)
        required: false
    user_id:
        description: The OCID of the user.
        required: true
    state:
        description: Create or update a SMTP credential with I(state=present). Delete a SMTP credential
                     with I(state=absent).
        required: false
        default: present
        choices: ['present', 'absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource ]
"""


EXAMPLES = """
- name: Create a SMTP credential
  oci_smtp_credential:
    user_id: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
    description: "Test SMTP Credential"

- name: Update a SMTP credential
  oci_smtp_credential:
    user_id: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
    id: ocid1.credential.oc1..xxxxxEXAMPLExxxxx...l5aq
    description: "Updated SMTP credential"

- name: Delete a SMTP credential
  oci_smtp_credential:
    user_id: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
    id: ocid1.credential.oc1..xxxxxEXAMPLExxxxx...l5aq
    state: 'absent'
"""


RETURN = """
smtp_credential:
    description: Information about the SMTP credential
    returned: On successful operation
    type: complex
    contains:
        user_name:
            description: The SMTP user name.
            returned: always
            type: string
            sample: "ocid1.user.oc1.xxxxxEXAMPLExxxxx.@ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx.za.com"
        password:
            description: The SMTP password. The value is available only in the response for create operation.
                         Not retuned for update and delete operation.
            returned: always
            type: string
            sample: ".bi9zaqZ8Gr"
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
            description: Date and time when this SMTP credential will expire, in the format defined by RFC3339. Null if
                         it never expires.
            returned: always
            type: string
            sample: null
    sample: {
              "description":"Test SMTP credential",
              "id":"ocid1.credential.oc1..xxxxxEXAMPLExxxxx",
              "inactive_status":null,
              "lifecycle_state":"ACTIVE",
              "password":".bi9zaqZ8Gr",
              "time_created":"2018-11-13T06:45:32.246000+00:00",
              "time_expires":null,
              "user_id":"ocid1.user.oc1..xxxxxEXAMPLExxxxx",
              "username":"ocid1.user.oc1..xxxxxEXAMPLExxxxx@ocid1.tenancy.oc1..xxxxxEXAMPLExxxxx.za.com"
             }
"""


from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.exceptions import ServiceError, ClientError
    from oci.identity.models import (
        CreateSmtpCredentialDetails,
        UpdateSmtpCredentialDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


RESOURCE_NAME = "smtp_credential"


def create_or_update_smtp_credential(identity_client, module):
    result = dict(changed=False, export="")
    smtp_credential_id = module.params.get("smtp_credential_id")
    try:
        if smtp_credential_id:
            result = update_smtp_credential(identity_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type=RESOURCE_NAME,
                create_fn=create_smtp_credential,
                kwargs_create={"identity_client": identity_client, "module": module},
                list_fn=identity_client.list_smtp_credentials,
                kwargs_list={"user_id": module.params.get("user_id")},
                module=module,
                model=CreateSmtpCredentialDetails(),
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to create/update SMTP credential due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error(
            "Unable to create/update SMTP credential due to: %s", str(ex)
        )
        module.fail_json(msg=str(ex))

    return result


def create_smtp_credential(identity_client, module):
    user_id = module.params["user_id"]
    create_smtp_credential_details = CreateSmtpCredentialDetails()
    for attribute in create_smtp_credential_details.attribute_map:
        create_smtp_credential_details.__setattr__(
            attribute, module.params.get(attribute)
        )

    # Don't wait as create operation of smtp credential always returns with ACTIVE lifecycle state on creation.
    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        create_fn=identity_client.create_smtp_credential,
        kwargs_create={
            "user_id": user_id,
            "create_smtp_credential_details": create_smtp_credential_details,
        },
        client=identity_client,
        get_fn=None,
        get_param=None,
        module=module,
        wait_applicable=False,
    )
    return result


def update_smtp_credential(identity_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type=RESOURCE_NAME,
        get_fn=oci_utils.get_target_resource_from_list,
        kwargs_get={
            "module": module,
            "list_resource_fn": identity_client.list_smtp_credentials,
            "target_resource_id": module.params.get("smtp_credential_id"),
            "user_id": module.params.get("user_id"),
        },
        update_fn=identity_client.update_smtp_credential,
        primitive_params_update=["user_id", "smtp_credential_id"],
        kwargs_non_primitive_update={
            UpdateSmtpCredentialDetails: "update_smtp_credential_details"
        },
        module=module,
        update_attributes=UpdateSmtpCredentialDetails().attribute_map,
        wait_applicable=False,
    )
    return result


def delete_smtp_credential(identity_client, module):
    result = oci_utils.delete_and_wait(
        resource_type=RESOURCE_NAME,
        client=identity_client,
        get_fn=oci_utils.get_target_resource_from_list,
        kwargs_get={
            "module": module,
            "list_resource_fn": identity_client.list_smtp_credentials,
            "target_resource_id": module.params.get("smtp_credential_id"),
            "user_id": module.params.get("user_id"),
        },
        delete_fn=identity_client.delete_smtp_credential,
        kwargs_delete={
            "user_id": module.params["user_id"],
            "smtp_credential_id": module.params["smtp_credential_id"],
        },
        module=module,
        wait_applicable=False,
    )
    # XXX: The smtp credential is not returned after it is deleted,
    # and so we currently reuse the earlier smtp credential object and mark
    # its lifecycle state as DELETED.
    # We also don't wait, as there is no state transition that we need to wait for.
    if result["changed"]:
        smtp_credential = result[RESOURCE_NAME]
        smtp_credential["lifecycle_state"] = "DELETED"
        result[RESOURCE_NAME] = smtp_credential
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_smtp_credential")
    set_logger(logger)

    module_args = oci_utils.get_common_arg_spec(supports_create=True)
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            smtp_credential_id=dict(type="str", required=False, aliases=["id"]),
            description=dict(type="str", required=False),
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

    identity_client = oci_utils.create_service_client(module, IdentityClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_smtp_credential(identity_client, module)
    elif state == "absent":
        result = delete_smtp_credential(identity_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
