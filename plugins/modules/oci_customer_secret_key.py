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
module: oci_customer_secret_key
short_description: Create, update and delete Customer Secret Keys for the specified user in OCI.
description:
    - "This module allows the user to create, update and delete Customer Secret Keys in OCI. A CustomerSecretKey is an
      Oracle-provided key for using the Object Storage Service's Amazon S3 compatible API. A user can have up to two
      secret keys at a time.
      Note: The secret key is always an Oracle-generated string; you can't change it to a string of your choice."
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user.
        required: true
    customer_secret_key_id:
        description: The OCID of the Customer Secret Key. Required when the secret keys's description needs to be
                     updated with I(state=present) and for deleting a secret key with I(state=absent)
        required: false
        aliases: ['id']
    display_name:
        description: The display name you assign to the secret key. Does not have to be unique, and it's changeable.
                     Required when creating a customer secret key. The length of the description must be between 1 and
                     200 characters.
        required: false
        aliases: ['name']
    state:
        description: The state of the customer secret key that must be asserted to. When I(state=present), and the
                     secret key doesn't exist, the secret key is created. When I(state=absent), the secret key is
                     deleted.
        required: false
        default: "present"
        choices: ['present', 'absent']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create a new customer secret key
  oci_customer_secret_key:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    name: "my first customer secret key"

- name: Update a customer secret key's display name
  oci_customer_secret_key:
    id: "ocid1.credential.oc1..xxxxxEXAMPLExxxxx"
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    name: "customer secret key #1"

- name: Delete a customer secret key
  oci_customer_secret_key:
    id: "ocid1.credential.oc1..xxxxxEXAMPLExxxxx"
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    state: "absent"
"""

RETURN = """
oci_customer_secret_key:
    description: Details of the Customer Secret Key. The "key" attribute is returned only during creation of the
                 customer secret key.
    returned: On success
    type: dict
    sample: {
        'key': 'wtUboLOGc3p8t0LG6d/wVJF+fwj0R700bW87LK41+kU=',
        'time_expires': None,
        'time_created': '2018-01-08T05:20:23.353000+00:00',
        'lifecycle_state': 'ACTIVE',
        'id': 'ocid1.credential.oc1..xxxxxEXAMPLExxxxx',
        'display_name': 'My first customer secret key description 900',
        'user_id': 'ocid1.user.oc1..xxxxxEXAMPLExxxxx',
        'inactive_status': None
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import (
        CreateCustomerSecretKeyDetails,
        UpdateCustomerSecretKeyDetails,
    )
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None
RESOURCE_NAME = "customer_secret_key"


def set_logger(provided_logger):
    global logger
    logger = provided_logger


def get_logger():
    return logger


def _get_customer_secret_key_from_id(identity_client, user_id, id, module):
    try:
        response = oci_utils.call_with_backoff(
            identity_client.list_customer_secret_keys, user_id=user_id
        )
        if response is not None:
            for sk in response.data:
                if sk.id == id:
                    return sk
        return None
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def delete_customer_secret_key(identity_client, user_id, id, module):
    result = {}
    changed = False
    try:
        secret_key = _get_customer_secret_key_from_id(
            identity_client, user_id, id, module
        )
        oci_utils.call_with_backoff(
            identity_client.delete_customer_secret_key,
            user_id=user_id,
            customer_secret_key_id=id,
        )
        get_logger().info("Deleted customer secret key %s", id)
        changed = True
        # The Customer Secret Key is not returned by list customer secret keys after it
        # is deleted, and so we currently reuse the earlier customer secret key object and mark
        # its lifecycle state as DELETED.
        # Note: This current approach has problems around idempotency.
        # We also don't wait, as there is no state transition that we need to wait for.
        secret_key.lifecycle_state = "DELETED"
        result[RESOURCE_NAME] = to_dict(secret_key)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result["changed"] = changed
    return result


def update_customer_secret_key(
    identity_client, user_id, secret_key_id, display_name, module
):
    result = dict()
    changed = False
    try:
        uskd = UpdateCustomerSecretKeyDetails()
        uskd.display_name = display_name
        get_logger().debug(
            "Customer Secret Key %s - updating with new display name: %s",
            secret_key_id,
            display_name,
        )
        response = oci_utils.call_with_backoff(
            identity_client.update_customer_secret_key,
            user_id=user_id,
            customer_secret_key_id=secret_key_id,
            update_customer_secret_key_details=uskd,
        )
        get_logger().info("Updated Customer Secret Key %s", to_dict(response.data))
        result[RESOURCE_NAME] = to_dict(response.data)
        changed = True
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result["changed"] = changed
    return result


def _is_customer_secret_key_active(customer_secret_keys, csk_id):
    result = [
        csk
        for csk in customer_secret_keys
        if csk.id == csk_id and csk.lifecycle_state == "ACTIVE"
    ]
    return len(result) == 1


def create_customer_secret_key(identity_client, user_id, display_name, module):
    result = {}
    try:
        cskd = CreateCustomerSecretKeyDetails()
        cskd.display_name = display_name
        result = oci_utils.create_resource(
            resource_type=RESOURCE_NAME,
            create_fn=identity_client.create_customer_secret_key,
            kwargs_create={
                "user_id": user_id,
                "create_customer_secret_key_details": cskd,
            },
            module=module,
        )
        resource = result[RESOURCE_NAME]
        csk_id = resource["id"]
        get_logger().info("Created Customer Secret Key %s", to_dict(resource))

        response = identity_client.list_customer_secret_keys(user_id)
        # wait until the created Customer Secret Key reaches Active state
        oci.wait_until(
            identity_client,
            response,
            evaluate_response=lambda resp: _is_customer_secret_key_active(
                resp.data, csk_id
            ),
        )

        # Reuse the CSK object returned by "create" API call as only that object has the "key" attribute defined.
        # Update the lifecycle_status to "ACTIVE"
        result[RESOURCE_NAME]["lifecycle_status"] = "ACTIVE"
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))


def main():
    set_logger(oci_utils.get_logger("oci_customer_secret_key"))

    module_args = oci_utils.get_common_arg_spec(supports_create=True)
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            customer_secret_key_id=dict(type="str", required=False, aliases=["id"]),
            name=dict(type="str", required=False, aliases=["display_name"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["customer_secret_key_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)
    state = module.params["state"]

    result = dict(changed=False)

    user_id = module.params.get("user_id", None)
    secret_key_id = module.params.get("customer_secret_key_id", None)
    name = module.params.get("name", None)
    get_logger().debug("Id is " + str(secret_key_id))

    if secret_key_id is not None:
        secret_key = _get_customer_secret_key_from_id(
            identity_client, user_id, secret_key_id, module
        )

        if state == "absent":
            get_logger().debug(
                "Delete Customer Secret Key %s for user %s requested",
                secret_key_id,
                user_id,
            )
            if secret_key is not None:
                get_logger().debug("Deleting %s", secret_key.id)
                result = delete_customer_secret_key(
                    identity_client, user_id, secret_key_id, module
                )
            else:
                get_logger().debug(
                    "Customer secret key %s already deleted.", secret_key_id
                )
        elif state == "present":
            if secret_key.display_name != name:
                result = update_customer_secret_key(
                    identity_client, user_id, secret_key_id, name, module
                )
            else:
                # No change needed, return existing customer secret key details
                result[RESOURCE_NAME] = to_dict(secret_key)
    else:
        result = oci_utils.check_and_create_resource(
            resource_type=RESOURCE_NAME,
            create_fn=create_customer_secret_key,
            kwargs_create={
                "identity_client": identity_client,
                "user_id": user_id,
                "display_name": name,
                "module": module,
            },
            list_fn=identity_client.list_customer_secret_keys,
            kwargs_list={"user_id": user_id},
            module=module,
            model=CreateCustomerSecretKeyDetails(),
        )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
