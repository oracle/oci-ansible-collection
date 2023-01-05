#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_oda_authentication_provider_facts
short_description: Fetches details about one or multiple AuthenticationProvider resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AuthenticationProvider resources in Oracle Cloud Infrastructure
    - Returns a page of Authentication Providers that belong to the specified Digital Assistant instance.
    - If the `opc-next-page` header appears in the response, then
      there are more items to retrieve. To get the next page in the subsequent
      GET request, include the header's value as the `page` query parameter.
    - If I(authentication_provider_id) is specified, the details of a single AuthenticationProvider will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    authentication_provider_id:
        description:
            - Unique Authentication Provider identifier.
            - Required to get a specific authentication_provider.
        type: str
        aliases: ["id"]
    oda_instance_id:
        description:
            - Unique Digital Assistant instance identifier.
        type: str
        required: true
    identity_provider:
        description:
            - List only Authentication Providers for this Identity Provider.
        type: str
        choices:
            - "GENERIC"
            - "OAM"
            - "GOOGLE"
            - "MICROSOFT"
    name:
        description:
            - List only the information for Authentication Providers with this name. Authentication Provider names are unique and may not change.
            - "Example: `MyProvider`"
        type: str
    lifecycle_state:
        description:
            - List only the resources that are in this lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - Sort the results in this order, use either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Sort on this field. You can specify one sort order only. The default sort field is `timeCreated`.
            - The default sort order for `timeCreated` and `timeUpdated` is descending.
              For all other sort fields the default sort order is ascending.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "name"
            - "identityProvider"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific authentication_provider
  oci_oda_authentication_provider_facts:
    # required
    authentication_provider_id: "ocid1.authenticationprovider.oc1..xxxxxxEXAMPLExxxxxx"
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List authentication_providers
  oci_oda_authentication_provider_facts:
    # required
    oda_instance_id: "ocid1.odainstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    identity_provider: GENERIC
    name: name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
authentication_providers:
    description:
        - List of AuthenticationProvider resources
    returned: on success
    type: complex
    contains:
        token_endpoint_url:
            description:
                - The IDPs URL for requesting access tokens.
                - Returned for get operation
            returned: on success
            type: str
            sample: token_endpoint_url_example
        authorization_endpoint_url:
            description:
                - The IDPs URL for the page that users authenticate with by entering the user name and password.
                - Returned for get operation
            returned: on success
            type: str
            sample: authorization_endpoint_url_example
        short_authorization_code_request_url:
            description:
                - A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows
                  you to send query parameters).  You might need this because the generated authorization-code-request URL
                  could be too long for SMS and older smart phones.
                - Returned for get operation
            returned: on success
            type: str
            sample: short_authorization_code_request_url_example
        revoke_token_endpoint_url:
            description:
                - If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then
                  you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens
                  component to revoke the user's tokens for this service.
                - Returned for get operation
            returned: on success
            type: str
            sample: revoke_token_endpoint_url_example
        client_id:
            description:
                - The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration.
                  With Microsoft identity platform, use the application ID.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
        scopes:
            description:
                - A space-separated list of the scopes that must be included when Digital Assistant requests an access token from
                  the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled,
                  include the scope that???s necessary to get the refresh token (typically offline_access).
                - Returned for get operation
            returned: on success
            type: str
            sample: scopes_example
        subject_claim:
            description:
                - The access-token profile claim to use to identify the user.
                - Returned for get operation
            returned: on success
            type: str
            sample: subject_claim_example
        refresh_token_retention_period_in_days:
            description:
                - The number of days to keep the refresh token in the Digital Assistant cache.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        redirect_url:
            description:
                - The OAuth Redirect URL.
                - Returned for get operation
            returned: on success
            type: str
            sample: redirect_url_example
        is_visible:
            description:
                - Whether this Authentication Provider is visible in the ODA UI.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
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
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "grant_type": "CLIENT_CREDENTIALS",
        "identity_provider": "GENERIC",
        "name": "name_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.oda import ManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AuthenticationProviderFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "oda_instance_id",
            "authentication_provider_id",
        ]

    def get_required_params_for_list(self):
        return [
            "oda_instance_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_authentication_provider,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            authentication_provider_id=self.module.params.get(
                "authentication_provider_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "identity_provider",
            "name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_authentication_providers,
            oda_instance_id=self.module.params.get("oda_instance_id"),
            **optional_kwargs
        )


AuthenticationProviderFactsHelperCustom = get_custom_class(
    "AuthenticationProviderFactsHelperCustom"
)


class ResourceFactsHelper(
    AuthenticationProviderFactsHelperCustom, AuthenticationProviderFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            authentication_provider_id=dict(aliases=["id"], type="str"),
            oda_instance_id=dict(type="str", required=True),
            identity_provider=dict(
                type="str", choices=["GENERIC", "OAM", "GOOGLE", "MICROSOFT"]
            ),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=["timeCreated", "timeUpdated", "name", "identityProvider"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="authentication_provider",
        service_client_class=ManagementClient,
        namespace="oda",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(authentication_providers=result)


if __name__ == "__main__":
    main()
