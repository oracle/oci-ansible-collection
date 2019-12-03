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
    "status": ["deprecated"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_swift_password
short_description: Create, update and delete Swift (OpenStack Object Store Service) passwords in OCI
description:
    - This module allows the user to create, update and delete Swift passwords in OCI. This module is deprecated.
      Please use M(oci_auth_token) instead. This module may be removed in a future release. Swift is the OpenStack
      object storage service. A SwiftPassword is an Oracle-provided password for using a Swift client with the Oracle
      Cloud Infrastructure Object Storage Service. This password is associated with the user's Console login. Swift
      passwords never expire. A user can have up to two Swift passwords at a time. Note - The password is always an
      Oracle-generated string; you can't change it to a string of your choice.
version_added: "2.5"
options:
    user_id:
        description: The OCID of the user.
        required: true
    swift_password_id:
        description: The OCID of the swift password. Required when the password's description needs to be updated
                      with I(state=present) and for deleting a swift password with I(state=absent)
        required: false
        aliases: ['id']
    description:
        description: The description you assign to the Swift password during creation. Does not have to be unique, and
                     it's changeable. Required when creating a swift password. The length of the description must be
                     between 1 and 400 characters.
        required: false
    state:
        description: The state of the swift password that must be asserted to. When I(state=present), and the
                     swift password doesn't exist, the swift password is created. When I(state=absent),
                     the swift password is deleted.
        required: false
        default: "present"
        choices: ['present', 'absent']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create a new swift password
  oci_swift_password:
    user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
    description: "my first swift password"

- name: Update a swift password's description
  oci_swift_password:
        id: "ocid1.credential.oc1..xxxxxEXAMPLExxxxx"
        user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
        description: "swift password #1"

- name: Delete a swift password
  oci_swift_password:
        id: "ocid1.credential.oc1..xxxxxEXAMPLExxxxx"
        user_id: "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
        state: "absent"
"""

RETURN = """
oci_swift_password:
    description: Details of the Swift password
    returned: On success. The password is only returned only during creation.
    type: dict
    sample: {
            "description": "My first swift password description",
            "expires_on": null,
            "id": "ocid1.credential.oc1..xxxxxEXAMPLExxxxx",
            "inactive_status": null,
            "lifecycle_state": "ACTIVE",
            "password": "+)UWHJK8UMgMvo5Qv!md",
            "time_created": "2018-01-03T12:47:25.759000+00:00",
            "user_id": "ocid1.user.oc1..xxxxxEXAMPLExxxxx"
          }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    import oci
    from oci.identity.identity_client import IdentityClient
    from oci.identity.models import (
        CreateSwiftPasswordDetails,
        UpdateSwiftPasswordDetails,
    )
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None
RESOURCE_NAME = "swift_password"


def set_logger(provided_logger):
    global logger
    logger = provided_logger


def get_logger():
    return logger


def _get_swift_password_from_id(identity_client, user_id, id, module):
    try:
        resp = oci_utils.call_with_backoff(
            identity_client.list_swift_passwords, user_id=user_id
        )
        if resp is not None:
            for sw_pass in resp.data:
                if sw_pass.id == id:
                    return sw_pass

        return None
    except ServiceError as ex:
        module.fail_json(msg=ex.message)


def delete_swift_password(identity_client, user_id, id, module):
    result = {}
    changed = False
    try:
        sw_pass = _get_swift_password_from_id(identity_client, user_id, id, module)
        oci_utils.call_with_backoff(
            identity_client.delete_swift_password, user_id=user_id, swift_password_id=id
        )
        get_logger().info("Deleted swift password %s", id)
        changed = True
        # XXX: The Swift password is not returned by list swift passwords after it
        # is deleted, and so we currently reuse the earlier swift password object and mark
        # its lifecycle state as DELETED.
        # Note: This current approach has problems around idempotency.
        # We also don't wait, as there is no state transition that we need to wait for.
        sw_pass.lifecycle_state = "DELETED"
        result[RESOURCE_NAME] = to_dict(sw_pass)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))

    result["changed"] = changed
    return result


def update_swift_password(identity_client, user_id, id, description, module):
    result = dict()
    changed = False
    try:
        uspd = UpdateSwiftPasswordDetails()
        uspd.description = description
        get_logger().debug(
            "Swift Password %s - updating with new description: %s", id, description
        )
        response = oci_utils.call_with_backoff(
            identity_client.update_swift_password,
            user_id=user_id,
            swift_password_id=id,
            update_swift_password_details=uspd,
        )
        get_logger().info("Updated Swift Password %s", to_dict(response.data))
        result[RESOURCE_NAME] = to_dict(response.data)
        changed = True
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    result["changed"] = changed
    return result


def _is_swift_password_active(swift_passwords, sw_pass_id):
    result = [
        sw_pass
        for sw_pass in swift_passwords
        if sw_pass.id == sw_pass_id and sw_pass.lifecycle_state == "ACTIVE"
    ]
    return len(result) == 1


def create_swift_password(identity_client, user_id, description, module):
    result = {}
    try:
        cspd = CreateSwiftPasswordDetails()
        cspd.description = description

        result = oci_utils.create_resource(
            resource_type=RESOURCE_NAME,
            create_fn=identity_client.create_swift_password,
            kwargs_create={"user_id": user_id, "create_swift_password_details": cspd},
            module=module,
        )
        resource = result[RESOURCE_NAME]
        sw_pass_id = resource["id"]
        # cache the swift password's password as it is only provided during creation
        cached_pass = resource["password"]
        get_logger().info("Created Swift Password %s", to_dict(resource))

        response = identity_client.list_swift_passwords(user_id)
        # wait until the created Swift password reaches Active state
        oci.wait_until(
            identity_client,
            response,
            evaluate_response=lambda resp: _is_swift_password_active(
                resp.data, sw_pass_id
            ),
        )

        sw_pass = _get_swift_password_from_id(
            identity_client, user_id, sw_pass_id, module
        )
        # stuff the cached password in the returned swift_password model
        sw_pass.password = cached_pass
        result[RESOURCE_NAME] = to_dict(sw_pass)
        return result
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))


def main():
    set_logger(oci_utils.get_logger("oci_swift_password"))

    module_args = oci_utils.get_common_arg_spec(supports_create=True)
    module_args.update(
        dict(
            user_id=dict(type="str", required=True),
            swift_password_id=dict(
                type="str", required=False, aliases=["id"], no_log=True
            ),
            description=dict(type="str", required=False),
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
        required_if=[("state", "absent", ["swift_password_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    identity_client = oci_utils.create_service_client(module, IdentityClient)

    state = module.params["state"]

    result = dict(changed=False)

    user_id = module.params.get("user_id", None)
    id = module.params.get("swift_password_id", None)
    description = module.params.get("description", None)
    get_logger().debug("Id is " + str(id))

    if id is not None:
        sw_pass = _get_swift_password_from_id(identity_client, user_id, id, module)

        if state == "absent":
            get_logger().debug(
                "Delete swift password %s for user %s requested", id, user_id
            )
            if sw_pass:
                get_logger().debug("Deleting %s", sw_pass.id)
                result = delete_swift_password(identity_client, user_id, id, module)
            else:
                get_logger().debug("Swift Password %s already deleted.", id)
        elif state == "present":
            if sw_pass.description != description:
                result = update_swift_password(
                    identity_client, user_id, id, description, module
                )
            else:
                # No change needed, return existing swift password details
                result[RESOURCE_NAME] = to_dict(sw_pass)
    else:
        # Check and create swift password if necessary
        result = oci_utils.check_and_create_resource(
            resource_type=RESOURCE_NAME,
            create_fn=create_swift_password,
            kwargs_create={
                "identity_client": identity_client,
                "user_id": user_id,
                "description": description,
                "module": module,
            },
            list_fn=identity_client.list_swift_passwords,
            kwargs_list={"user_id": user_id},
            module=module,
            model=CreateSwiftPasswordDetails(),
        )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
