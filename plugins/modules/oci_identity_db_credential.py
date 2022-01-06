#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_identity_db_credential
short_description: Manage a DbCredential resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a DbCredential resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new DB credential for the specified user.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    password:
        description:
            - The password for the DB credentials during creation.
            - Required for create using I(state=present).
        type: str
    description:
        description:
            - The description you assign to the DB credentials during creation.
            - Required for create using I(state=present).
        type: str
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
    db_credential_id:
        description:
            - The OCID of the DB credential.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DbCredential.
            - Use I(state=present) to create a DbCredential.
            - Use I(state=absent) to delete a DbCredential.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create db_credential
  oci_identity_db_credential:
    # required
    password: example-password
    description: description_example
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete db_credential
  oci_identity_db_credential:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    db_credential_id: "ocid1.dbcredential.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
db_credential:
    description:
        - Details of the DbCredential resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the DB credential.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The OCID of the user the DB credential belongs to.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The description you assign to the DB credential. Does not have to be unique, and it's changeable.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - Date and time the `DbCredential` object was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_expires:
            description:
                - Date and time when this credential will expire, in the format defined by RFC3339.
                  Null if it never expires.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The credential's current state. After creating a DB credential, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
            returned: on success
            type: str
            sample: lifecycle_state_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "lifecycle_state_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient
    from oci.identity.models import CreateDbCredentialDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbCredentialHelperGen(OCIResourceHelperBase):
    """Supported operations: create, list and delete"""

    def get_module_resource_id_param(self):
        return "db_credential_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_credential_id")

    def get_resource(self):
        resources = self.list_resources()
        for resource in resources:
            if self.get_module_resource_id() == resource.id:
                return oci_common_utils.get_default_response_from_resource(resource)

        oci_common_utils.raise_does_not_exist_service_error()

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "user_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_db_credentials, **kwargs
        )

    def get_create_model_class(self):
        return CreateDbCredentialDetails

    def get_exclude_attributes(self):
        return ["password"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_db_credential,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_db_credential_details=create_details,
                user_id=self.module.params.get("user_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_db_credential,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                db_credential_id=self.module.params.get("db_credential_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DbCredentialHelperCustom = get_custom_class("DbCredentialHelperCustom")


class ResourceHelper(DbCredentialHelperCustom, DbCredentialHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            password=dict(type="str", no_log=True),
            description=dict(type="str"),
            user_id=dict(type="str", required=True),
            db_credential_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_credential",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
