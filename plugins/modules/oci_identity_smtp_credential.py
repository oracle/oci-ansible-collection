#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_identity_smtp_credential
short_description: Manage a SmtpCredential resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a SmtpCredential resource in Oracle Cloud Infrastructure
    - "For I(state=present), creates a new SMTP credential for the specified user. An SMTP credential has an SMTP user name and an SMTP password.
      You must specify a *description* for the SMTP credential (although it can be an empty string). It does not
      have to be unique, and you can change it anytime with
      L(UpdateSmtpCredential,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/SmtpCredentialSummary/UpdateSmtpCredential)."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    description:
        description:
            - The description you assign to the SMTP credentials during creation. Does not have to be unique, and it's changeable.
            - (For tenancies that support identity domains) You can have an empty description.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    user_id:
        description:
            - The OCID of the user.
        type: str
        required: true
    smtp_credential_id:
        description:
            - The OCID of the SMTP credential.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the SmtpCredential.
            - Use I(state=present) to create or update a SmtpCredential.
            - Use I(state=absent) to delete a SmtpCredential.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create smtp_credential
  oci_identity_smtp_credential:
    # required
    description: description_example
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update smtp_credential
  oci_identity_smtp_credential:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    smtp_credential_id: "ocid1.smtpcredential.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example

- name: Delete smtp_credential
  oci_identity_smtp_credential:
    # required
    user_id: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
    smtp_credential_id: "ocid1.smtpcredential.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
smtp_credential:
    description:
        - Details of the SmtpCredential resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        username:
            description:
                - The SMTP user name.
            returned: on success
            type: str
            sample: username_example
        id:
            description:
                - The OCID of the SMTP credential.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        user_id:
            description:
                - The OCID of the user the SMTP credential belongs to.
            returned: on success
            type: str
            sample: "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The description you assign to the SMTP credential. Does not have to be unique, and it's changeable.
                - (For tenancies that support identity domains) You can have an empty description.
            returned: on success
            type: str
            sample: description_example
        time_created:
            description:
                - Date and time the `SmtpCredential` object was created, in the format defined by RFC3339.
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
                - The credential's current state. After creating a SMTP credential, make sure its `lifecycleState` changes from
                  CREATING to ACTIVE before using it.
            returned: on success
            type: str
            sample: CREATING
        inactive_status:
            description:
                - The detailed status of INACTIVE lifecycleState.
            returned: on success
            type: int
            sample: 56
    sample: {
        "username": "username_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "user_id": "ocid1.user.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_expires": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "inactive_status": 56
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient
    from oci.identity.models import CreateSmtpCredentialDetails
    from oci.identity.models import UpdateSmtpCredentialDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SmtpCredentialHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, list and delete"""

    def get_possible_entity_types(self):
        return super(SmtpCredentialHelperGen, self).get_possible_entity_types() + [
            "smtpcredential",
            "smtpcredentials",
            "identitysmtpcredential",
            "identitysmtpcredentials",
            "smtpcredentialresource",
            "smtpcredentialsresource",
            "identity",
        ]

    def get_module_resource_id_param(self):
        return "smtp_credential_id"

    def get_module_resource_id(self):
        return self.module.params.get("smtp_credential_id")

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
            self.client.list_smtp_credentials, **kwargs
        )

    def get_create_model_class(self):
        return CreateSmtpCredentialDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_smtp_credential,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_smtp_credential_details=create_details,
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

    def get_update_model_class(self):
        return UpdateSmtpCredentialDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_smtp_credential,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                smtp_credential_id=self.module.params.get("smtp_credential_id"),
                update_smtp_credential_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_smtp_credential,
            call_fn_args=(),
            call_fn_kwargs=dict(
                user_id=self.module.params.get("user_id"),
                smtp_credential_id=self.module.params.get("smtp_credential_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


SmtpCredentialHelperCustom = get_custom_class("SmtpCredentialHelperCustom")


class ResourceHelper(SmtpCredentialHelperCustom, SmtpCredentialHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            description=dict(type="str"),
            user_id=dict(type="str", required=True),
            smtp_credential_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="smtp_credential",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
