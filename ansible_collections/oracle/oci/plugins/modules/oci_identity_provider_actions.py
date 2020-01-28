#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_identity_provider_actions
short_description: Perform actions on an IdentityProvider resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an IdentityProvider resource in Oracle Cloud Infrastructure
    - For I(action=reset_idp_scim_client), resets the OAuth2 client credentials for the SCIM client associated with this identity provider.
version_added: "2.5"
options:
    identity_provider_id:
        description:
            - The OCID of the identity provider.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the IdentityProvider.
        type: str
        required: true
        choices: ["reset_idp_scim_client"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action reset_idp_scim_client on identity_provider
  oci_identity_provider_actions:
    identity_provider_id: ocid1.identityprovider.oc1..xxxxxxEXAMPLExxxxxx
    action: reset_idp_scim_client

"""

RETURN = """
identity_provider:
    description:
        - Details of the IdentityProvider resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        client_id:
            description:
                - The client identifier.
            returned: on success
            type: string
            sample: ocid1.client.oc1..xxxxxxEXAMPLExxxxxx
        client_secret:
            description:
                - The client secret.
            returned: on success
            type: string
            sample: client_secret_example
    sample: {
        "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
        "client_secret": "client_secret_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IdentityProviderActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        reset_idp_scim_client
    """

    @staticmethod
    def get_module_resource_id_param():
        return "identity_provider_id"

    def get_module_resource_id(self):
        return self.module.params.get("identity_provider_id")

    def get_get_fn(self):
        return self.client.get_identity_provider

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_identity_provider,
            identity_provider_id=self.module.params.get("identity_provider_id"),
        )

    def reset_idp_scim_client(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reset_idp_scim_client,
            call_fn_args=(),
            call_fn_kwargs=dict(
                identity_provider_id=self.module.params.get("identity_provider_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.module.params.get("wait_until")
            or self.get_action_desired_states(self.module.params.get("action")),
        )


IdentityProviderActionsHelperCustom = get_custom_class(
    "IdentityProviderActionsHelperCustom"
)


class ResourceHelper(
    IdentityProviderActionsHelperCustom, IdentityProviderActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            identity_provider_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["reset_idp_scim_client"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="identity_provider",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
