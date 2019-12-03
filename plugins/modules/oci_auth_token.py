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
module: oci_auth_token
short_description: Manage auth tokens in OCI Identity and Access Management service
description:
    - This module allows the user to perform create, delete & update operations on auth tokens in OCI Identity and
      Access Management service.
version_added: "2.5"
options:
    auth_token_id:
        description: The OCID of the auth token. Required to update an auth token with I(state=present) and delete
                     an auth token with I(state=absent)
        required: false
        aliases: ['id']
    description:
        description: The description you assign to the auth token during creation. Does not have to be unique, and it's
                     changeable. Required when creating an auth token with I(state=present)
        required: false
    user_id:
        description: The OCID of the user.
        required: true
    state:
        description: Create or update an auth token with I(state=present). Delete an auth token with I(state=absent).
        required: false
        default: present
        choices: ['present', 'absent']
author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource]
"""

EXAMPLES = """
- name: Create an auth token
  oci_auth_token:
    user_id: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
    description: "My test auth token"

- name: Update an auth token
  oci_auth_token:
    user_id: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
    id: ocid1.credential.oc1..xxxxxEXAMPLExxxxx...l5aq
    description: "My old test auth token"

- name: Delete an auth token
  oci_auth_token:
    user_id: ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq
    id: ocid1.credential.oc1..xxxxxEXAMPLExxxxx...l5aq
    state: 'absent'
"""

RETURN = """
auth_token:
    description: Information about the Auth token
    returned: On successful operation
    type: complex
    contains:
        token:
            description: The Auth token. The value is available only in the response for CreateAuthToken, and not for
                         ListAuthTokens or UpdateAuthToken.
            returned: always
            type: string
            sample: "Dmmtd<{DXkH1VJ46.F6X"
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
    sample: {
            "description": "test auth token 1",
            "id": "ocid1.credential.oc1..xxxxxEXAMPLExxxxx...l5aq",
            "inactive-status": null,
            "lifecycle-state": "ACTIVE",
            "time-created": "2018-11-08T02:40:25.118000+00:00",
            "time-expires": null,
            "token": null,
            "user-id": "ocid1.user.oc1..xxxxxEXAMPLExxxxx...h5hq"
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import CreateAuthTokenDetails
    from oci.identity.models import UpdateAuthTokenDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

RESOURCE_NAME = "auth_token"


def handle_delete_auth_token(identity_client, module):
    result = oci_utils.delete_and_wait(
        resource_type=RESOURCE_NAME,
        client=identity_client,
        get_fn=oci_utils.get_target_resource_from_list,
        kwargs_get={
            "module": module,
            "list_resource_fn": identity_client.list_auth_tokens,
            "target_resource_id": module.params.get("auth_token_id"),
            "user_id": module.params.get("user_id"),
        },
        delete_fn=identity_client.delete_auth_token,
        kwargs_delete={
            "user_id": module.params["user_id"],
            "auth_token_id": module.params["auth_token_id"],
        },
        module=module,
        wait_applicable=False,
    )
    # XXX: The auth token is not returned by list auth tokens after it
    # is deleted, and so we currently reuse the earlier auth token object and mark
    # its lifecycle state as DELETED.
    # We also don't wait, as there is no state transition that we need to wait for.
    if result["changed"]:
        auth_token = result[RESOURCE_NAME]
        auth_token["lifecycle_state"] = "DELETED"
        result[RESOURCE_NAME] = auth_token
    return result


def handle_create_auth_token(identity_client, module):
    user_id = module.params["user_id"]
    create_auth_token_details = CreateAuthTokenDetails()
    for attribute in create_auth_token_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_auth_token_details, attribute, module.params[attribute])

    # Don't wait as create auth_token always returns with ACTIVE lifecycle state on creation, and the "token" attribute
    # is only provided by the API on creation.
    result = oci_utils.create_and_wait(
        resource_type=RESOURCE_NAME,
        create_fn=identity_client.create_auth_token,
        kwargs_create={
            "user_id": user_id,
            "create_auth_token_details": create_auth_token_details,
        },
        client=identity_client,
        get_fn=None,
        get_param=None,
        module=module,
        wait_applicable=False,
    )
    return result


def handle_update_auth_token(identity_client, module):
    return oci_utils.check_and_update_resource(
        resource_type=RESOURCE_NAME,
        get_fn=oci_utils.get_target_resource_from_list,
        wait_applicable=False,
        kwargs_get={
            "module": module,
            "list_resource_fn": identity_client.list_auth_tokens,
            "target_resource_id": module.params.get("auth_token_id"),
            "user_id": module.params.get("user_id"),
        },
        update_fn=identity_client.update_auth_token,
        primitive_params_update=["user_id", "auth_token_id"],
        kwargs_non_primitive_update={
            UpdateAuthTokenDetails: "update_auth_token_details"
        },
        module=module,
        update_attributes=UpdateAuthTokenDetails().attribute_map.keys(),
    )


def main():
    module_args = oci_utils.get_common_arg_spec(supports_create=True)
    module_args.update(
        dict(
            auth_token_id=dict(type="str", required=False, aliases=["id"]),
            user_id=dict(type="str", required=True),
            description=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[["state", "absent", ["auth_token_id"]]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    state = module.params["state"]
    auth_token_id = module.params["auth_token_id"]

    if state == "absent":
        result = handle_delete_auth_token(identity_client, module)

    else:
        if auth_token_id is None:
            result = oci_utils.check_and_create_resource(
                resource_type="auth_token",
                create_fn=handle_create_auth_token,
                kwargs_create={"identity_client": identity_client, "module": module},
                list_fn=identity_client.list_auth_tokens,
                kwargs_list={"user_id": module.params["user_id"]},
                module=module,
                model=CreateAuthTokenDetails(),
            )

        else:
            result = handle_update_auth_token(identity_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
