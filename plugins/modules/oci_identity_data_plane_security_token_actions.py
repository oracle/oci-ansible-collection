#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_identity_data_plane_security_token_actions
short_description: Perform actions on a SecurityToken resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a SecurityToken resource in Oracle Cloud Infrastructure
    - For I(action=generate_scoped_access_token), based on the calling Principal and the input payload, derive the claims, and generate a scoped-access token
      for specific resources. For example, set scope to urn:oracle:db::id::<compartment-id> for access to a database in a compartment.
    - For I(action=generate_user), exchanges a valid user token-based signature (API key and UPST) for a short-lived UPST of the authenticated
      user principal. When not specified, the user session duration is set to a default of 60 minutes in all realms. Resulting UPSTs
      are refreshable while the user session has not expired.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    scope:
        description:
            - Scope definition for the scoped access token
            - Required for I(action=generate_scoped_access_token).
        type: str
    public_key:
        description:
            - A temporary public key, owned by the service. The service also owns the corresponding private key. This public
              key will be put inside the security token by the auth service after successful validation of the certificate.
        type: str
        required: true
    session_expiration_in_minutes:
        description:
            - User session expiration in minutes to which the requested user principal session token (UPST) is bounded.
              Valid values are from 5 to 60 for all realms.
            - Applicable only for I(action=generate_user).
        type: int
    action:
        description:
            - The action to perform on the SecurityToken.
        type: str
        required: true
        choices:
            - "generate_scoped_access_token"
            - "generate_user"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action generate_scoped_access_token on security_token
  oci_identity_data_plane_security_token_actions:
    # required
    scope: scope_example
    public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
    action: generate_scoped_access_token

- name: Perform action generate_user on security_token
  oci_identity_data_plane_security_token_actions:
    # required
    public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
    action: generate_user

    # optional
    session_expiration_in_minutes: 56

"""

RETURN = """
security_token:
    description:
        - Details of the SecurityToken resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        token:
            description:
                - The security token, signed by auth service
            returned: on success
            type: str
            sample: token_example
    sample: {
        "token": "token_example"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.identity_data_plane import DataplaneClient
    from oci.identity_data_plane.models import GenerateScopedAccessTokenDetails
    from oci.identity_data_plane.models import GenerateUserSecurityTokenDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SecurityTokenActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        generate_scoped_access_token
        generate_user
    """

    def generate_scoped_access_token(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateScopedAccessTokenDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_scoped_access_token,
            call_fn_args=(),
            call_fn_kwargs=dict(generate_scoped_access_token_details=action_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def generate_user(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, GenerateUserSecurityTokenDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_user_security_token,
            call_fn_args=(),
            call_fn_kwargs=dict(generate_user_security_token_details=action_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


SecurityTokenActionsHelperCustom = get_custom_class("SecurityTokenActionsHelperCustom")


class ResourceHelper(SecurityTokenActionsHelperCustom, SecurityTokenActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            scope=dict(type="str"),
            public_key=dict(type="str", required=True),
            session_expiration_in_minutes=dict(type="int"),
            action=dict(
                type="str",
                required=True,
                choices=["generate_scoped_access_token", "generate_user"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="security_token",
        service_client_class=DataplaneClient,
        namespace="identity_data_plane",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
