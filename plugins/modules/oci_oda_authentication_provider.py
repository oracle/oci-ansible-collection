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
module: oci_oda_authentication_provider
short_description: Manage an AuthenticationProvider resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AuthenticationProvider resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Authentication Provider
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    grant_type:
        description:
            - The grant type for the Authentication Provider.
            - Required for create using I(state=present).
        type: str
        choices:
            - "CLIENT_CREDENTIALS"
            - "AUTHORIZATION_CODE"
    identity_provider:
        description:
            - Which type of Identity Provider (IDP) you are using.
            - Required for create using I(state=present).
        type: str
        choices:
            - "GENERIC"
            - "OAM"
            - "GOOGLE"
            - "MICROSOFT"
    name:
        description:
            - A name to identify the Authentication Provider.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    is_visible:
        description:
            - Whether this Authentication Provider is visible in the ODA UI.
        type: bool
    token_endpoint_url:
        description:
            - The IDPs URL for requesting access tokens.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    authorization_endpoint_url:
        description:
            - The IDPs URL for the page that users authenticate with by entering the user name and password.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    short_authorization_code_request_url:
        description:
            - A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows
              you to send query parameters).  You might need this because the generated authorization-code-request URL
              could be too long for SMS and older smart phones.
            - This parameter is updatable.
        type: str
    revoke_token_endpoint_url:
        description:
            - If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then
              you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens
              component to revoke the user's tokens for this service.
            - This parameter is updatable.
        type: str
    client_id:
        description:
            - The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration.
              With Microsoft identity platform, use the application ID.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    client_secret:
        description:
            - The client secret for the IDP application (OAuth Client) that was registered as described in Identity Provider
              Registration. With Microsoft identity platform, use the application secret.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    scopes:
        description:
            - A space-separated list of the scopes that must be included when Digital Assistant requests an access token from
              the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled,
              include the scope that???s necessary to get the refresh token (typically offline_access).
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    subject_claim:
        description:
            - The access-token profile claim to use to identify the user.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    refresh_token_retention_period_in_days:
        description:
            - The number of days to keep the refresh token in the Digital Assistant cache.
            - This parameter is updatable.
        type: int
    redirect_url:
        description:
            - The OAuth Redirect URL.
            - This parameter is updatable.
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    authentication_provider_id:
        description:
            - Unique Authentication Provider identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AuthenticationProvider.
            - Use I(state=present) to create or update an AuthenticationProvider.
            - Use I(state=absent) to delete an AuthenticationProvider.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create authentication_provider
  oci_oda_authentication_provider:
    # required
    grant_type: CLIENT_CREDENTIALS
    identity_provider: GENERIC
    name: name_example
    token_endpoint_url: token_endpoint_url_example
    authorization_endpoint_url: authorization_endpoint_url_example
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    client_secret: client_secret_example
    scopes: scopes_example
    subject_claim: subject_claim_example
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_visible: true
    short_authorization_code_request_url: short_authorization_code_request_url_example
    revoke_token_endpoint_url: revoke_token_endpoint_url_example
    refresh_token_retention_period_in_days: 56
    redirect_url: redirect_url_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update authentication_provider
  oci_oda_authentication_provider:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    authentication_provider_id: "ocid1.authenticationprovider.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    token_endpoint_url: token_endpoint_url_example
    authorization_endpoint_url: authorization_endpoint_url_example
    short_authorization_code_request_url: short_authorization_code_request_url_example
    revoke_token_endpoint_url: revoke_token_endpoint_url_example
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    client_secret: client_secret_example
    scopes: scopes_example
    subject_claim: subject_claim_example
    refresh_token_retention_period_in_days: 56
    redirect_url: redirect_url_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update authentication_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_oda_authentication_provider:
    # required
    name: name_example
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    token_endpoint_url: token_endpoint_url_example
    authorization_endpoint_url: authorization_endpoint_url_example
    short_authorization_code_request_url: short_authorization_code_request_url_example
    revoke_token_endpoint_url: revoke_token_endpoint_url_example
    client_id: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
    client_secret: client_secret_example
    scopes: scopes_example
    subject_claim: subject_claim_example
    refresh_token_retention_period_in_days: 56
    redirect_url: redirect_url_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete authentication_provider
  oci_oda_authentication_provider:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    authentication_provider_id: "ocid1.authenticationprovider.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete authentication_provider using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_oda_authentication_provider:
    # required
    name: name_example
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
authentication_provider:
    description:
        - Details of the AuthenticationProvider resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique immutable identifier that was assigned when the Authentication Provider was created.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        grant_type:
            description:
                - The grant type for the Authentication Provider.
            returned: on success
            type: str
            sample: CLIENT_CREDENTIALS
        identity_provider:
            description:
                - Which type of Identity Provider (IDP) you are using.
            returned: on success
            type: str
            sample: GENERIC
        name:
            description:
                - A name to identify the Authentication Provider.
            returned: on success
            type: str
            sample: name_example
        token_endpoint_url:
            description:
                - The IDPs URL for requesting access tokens.
            returned: on success
            type: str
            sample: token_endpoint_url_example
        authorization_endpoint_url:
            description:
                - The IDPs URL for the page that users authenticate with by entering the user name and password.
            returned: on success
            type: str
            sample: authorization_endpoint_url_example
        short_authorization_code_request_url:
            description:
                - A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows
                  you to send query parameters).  You might need this because the generated authorization-code-request URL
                  could be too long for SMS and older smart phones.
            returned: on success
            type: str
            sample: short_authorization_code_request_url_example
        revoke_token_endpoint_url:
            description:
                - If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then
                  you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens
                  component to revoke the user's tokens for this service.
            returned: on success
            type: str
            sample: revoke_token_endpoint_url_example
        client_id:
            description:
                - The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration.
                  With Microsoft identity platform, use the application ID.
            returned: on success
            type: str
            sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        scopes:
            description:
                - A space-separated list of the scopes that must be included when Digital Assistant requests an access token from
                  the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled,
                  include the scope that???s necessary to get the refresh token (typically offline_access).
            returned: on success
            type: str
            sample: scopes_example
        subject_claim:
            description:
                - The access-token profile claim to use to identify the user.
            returned: on success
            type: str
            sample: subject_claim_example
        refresh_token_retention_period_in_days:
            description:
                - The number of days to keep the refresh token in the Digital Assistant cache.
            returned: on success
            type: int
            sample: 56
        redirect_url:
            description:
                - The OAuth Redirect URL.
            returned: on success
            type: str
            sample: redirect_url_example
        is_visible:
            description:
                - Whether this Authentication Provider is visible in the ODA UI.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The Authentication Provider's current state.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - When the resource was created. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - When the resource was last updated. A date-time string as described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339), section 14.29.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "grant_type": "CLIENT_CREDENTIALS",
        "identity_provider": "GENERIC",
        "name": "name_example",
        "token_endpoint_url": "token_endpoint_url_example",
        "authorization_endpoint_url": "authorization_endpoint_url_example",
        "short_authorization_code_request_url": "short_authorization_code_request_url_example",
        "revoke_token_endpoint_url": "revoke_token_endpoint_url_example",
        "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
        "scopes": "scopes_example",
        "subject_claim": "subject_claim_example",
        "refresh_token_retention_period_in_days": 56,
        "redirect_url": "redirect_url_example",
        "is_visible": true,
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.oda import ManagementClient
    from oci.oda.models import CreateAuthenticationProviderDetails
    from oci.oda.models import UpdateAuthenticationProviderDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AuthenticationProviderHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            AuthenticationProviderHelperGen, self
        ).get_possible_entity_types() + [
            "authenticationprovider",
            "authenticationproviders",
            "odaauthenticationprovider",
            "odaauthenticationproviders",
            "authenticationproviderresource",
            "authenticationprovidersresource",
            "oda",
        ]

    def get_module_resource_id_param(self):
        return "authentication_provider_id"

    def get_module_resource_id(self):
        return self.module.params.get("authentication_provider_id")

    def get_get_fn(self):
        return self.client.get_authentication_provider

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_authentication_provider,
            authentication_provider_id=summary_model.id,
            oda_instance_id=self.module.params.get("oda_instance_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_authentication_provider,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            authentication_provider_id=self.module.params.get(
                "authentication_provider_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "oda_instance_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["identity_provider", "name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_authentication_providers, **kwargs
        )

    def get_create_model_class(self):
        return CreateAuthenticationProviderDetails

    def get_exclude_attributes(self):
        return ["client_secret"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_authentication_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                create_authentication_provider_details=create_details,
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
        return UpdateAuthenticationProviderDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_authentication_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                authentication_provider_id=self.module.params.get(
                    "authentication_provider_id"
                ),
                update_authentication_provider_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_authentication_provider,
            call_fn_args=(),
            call_fn_kwargs=dict(
                oda_instance_id=self.module.params.get("oda_instance_id"),
                authentication_provider_id=self.module.params.get(
                    "authentication_provider_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AuthenticationProviderHelperCustom = get_custom_class(
    "AuthenticationProviderHelperCustom"
)


class ResourceHelper(
    AuthenticationProviderHelperCustom, AuthenticationProviderHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            grant_type=dict(
                type="str", choices=["CLIENT_CREDENTIALS", "AUTHORIZATION_CODE"]
            ),
            identity_provider=dict(
                type="str", choices=["GENERIC", "OAM", "GOOGLE", "MICROSOFT"]
            ),
            name=dict(type="str"),
            is_visible=dict(type="bool"),
            token_endpoint_url=dict(type="str", no_log=True),
            authorization_endpoint_url=dict(type="str"),
            short_authorization_code_request_url=dict(type="str"),
            revoke_token_endpoint_url=dict(type="str", no_log=True),
            client_id=dict(type="str"),
            client_secret=dict(type="str", no_log=True),
            scopes=dict(type="str"),
            subject_claim=dict(type="str"),
            refresh_token_retention_period_in_days=dict(type="int", no_log=True),
            redirect_url=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            oda_instance_id=dict(type="str", required=True),
            authentication_provider_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="authentication_provider",
        service_client_class=ManagementClient,
        namespace="oda",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
