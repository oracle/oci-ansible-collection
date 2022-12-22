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
module: oci_apigateway_deployment_actions
short_description: Perform actions on a Deployment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Deployment resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), changes the deployment compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    deployment_id:
        description:
            - The ocid of the deployment.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
              resource is created.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Deployment.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on deployment
  oci_apigateway_deployment_actions:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
deployment:
    description:
        - Details of the Deployment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        gateway_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - "Example: `My new resource`"
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
                  resource is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        path_prefix:
            description:
                - A path on which to deploy all routes contained in the API
                  deployment specification. For more information, see
                  L(Deploying an API on an API Gateway by Creating an API
                  Deployment,https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).
            returned: on success
            type: str
            sample: path_prefix_example
        endpoint:
            description:
                - The endpoint to access this deployment on the gateway.
            returned: on success
            type: str
            sample: endpoint_example
        specification:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                request_policies:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        authentication:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                function_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function
                                          resource.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                                parameters:
                                    description:
                                        - "A map where key is a user defined string and value is a context expressions whose values will be sent to the custom
                                          auth function. Values should contain an expression.
                                          Example: `{\\"foo\\": \\"request.header[abc]\\"}`"
                                    returned: on success
                                    type: dict
                                    sample: {}
                                cache_key:
                                    description:
                                        - "A list of keys from \\"parameters\\" attribute value whose values will be added to the cache key."
                                    returned: on success
                                    type: list
                                    sample: []
                                issuers:
                                    description:
                                        - A list of parties that could have issued the token.
                                    returned: on success
                                    type: list
                                    sample: []
                                audiences:
                                    description:
                                        - The list of intended recipients for the token.
                                    returned: on success
                                    type: list
                                    sample: []
                                verify_claims:
                                    description:
                                        - A list of claims which should be validated to consider the token valid.
                                    returned: on success
                                    type: complex
                                    contains:
                                        key:
                                            description:
                                                - Name of the claim.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        values:
                                            description:
                                                - "The list of acceptable values for a given claim.
                                                  If this value is \\"null\\" or empty and \\"isRequired\\" set to \\"true\\", then
                                                  the presence of this claim in the JWT is validated."
                                            returned: on success
                                            type: list
                                            sample: []
                                        is_required:
                                            description:
                                                - "Whether the claim is required to be present in the JWT or not. If set
                                                  to \\"false\\", the claim values will be matched only if the claim is
                                                  present in the JWT."
                                            returned: on success
                                            type: bool
                                            sample: true
                                public_keys:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        uri:
                                            description:
                                                - The uri from which to retrieve the key. It must be accessible
                                                  without authentication.
                                            returned: on success
                                            type: str
                                            sample: uri_example
                                        is_ssl_verify_disabled:
                                            description:
                                                - Defines whether or not to uphold SSL verification.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        max_cache_duration_in_hours:
                                            description:
                                                - The duration for which the JWKS should be cached before it is
                                                  fetched again.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        type:
                                            description:
                                                - Type of the public key set.
                                            returned: on success
                                            type: str
                                            sample: STATIC_KEYS
                                        keys:
                                            description:
                                                - The set of static public keys.
                                            returned: on success
                                            type: complex
                                            contains:
                                                kty:
                                                    description:
                                                        - The key type.
                                                    returned: on success
                                                    type: str
                                                    sample: RSA
                                                use:
                                                    description:
                                                        - The intended use of the public key.
                                                    returned: on success
                                                    type: str
                                                    sample: sig
                                                key_ops:
                                                    description:
                                                        - The operations for which this key is to be used.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                alg:
                                                    description:
                                                        - The algorithm intended for use with this key.
                                                    returned: on success
                                                    type: str
                                                    sample: alg_example
                                                n:
                                                    description:
                                                        - The base64 url encoded modulus of the RSA public key represented
                                                          by this key.
                                                    returned: on success
                                                    type: str
                                                    sample: n_example
                                                e:
                                                    description:
                                                        - The base64 url encoded exponent of the RSA public key represented
                                                          by this key.
                                                    returned: on success
                                                    type: str
                                                    sample: e_example
                                                kid:
                                                    description:
                                                        - "A unique key ID. This key will be used to verify the signature of a
                                                          JWT with matching \\"kid\\"."
                                                    returned: on success
                                                    type: str
                                                    sample: kid_example
                                                format:
                                                    description:
                                                        - The format of the public key.
                                                    returned: on success
                                                    type: str
                                                    sample: JSON_WEB_KEY
                                                key:
                                                    description:
                                                        - The content of the PEM-encoded public key.
                                                    returned: on success
                                                    type: str
                                                    sample: key_example
                                is_anonymous_access_allowed:
                                    description:
                                        - "Whether an unauthenticated user may access the API. Must be \\"true\\" to enable ANONYMOUS
                                          route authorization."
                                    returned: on success
                                    type: bool
                                    sample: true
                                type:
                                    description:
                                        - Type of the authentication policy to use.
                                    returned: on success
                                    type: str
                                    sample: CUSTOM_AUTHENTICATION
                                token_header:
                                    description:
                                        - The name of the header containing the authentication token.
                                    returned: on success
                                    type: str
                                    sample: token_header_example
                                token_query_param:
                                    description:
                                        - The name of the query parameter containing the authentication token.
                                    returned: on success
                                    type: str
                                    sample: token_query_param_example
                                token_auth_scheme:
                                    description:
                                        - "The authentication scheme that is to be used when authenticating
                                          the token. This must to be provided if \\"tokenHeader\\" is specified."
                                    returned: on success
                                    type: str
                                    sample: token_auth_scheme_example
                                max_clock_skew_in_seconds:
                                    description:
                                        - The maximum expected time difference between the system clocks
                                          of the token issuer and the API Gateway.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                validation_policy:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        client_details:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                client_id:
                                                    description:
                                                        - Client ID for the OAuth2/OIDC app.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
                                                client_secret_id:
                                                    description:
                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Vault
                                                          Service secret resource.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.clientsecret.oc1..xxxxxxEXAMPLExxxxxx"
                                                client_secret_version_number:
                                                    description:
                                                        - The version number of the client secret to use.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                                type:
                                                    description:
                                                        - To specify where the Client App details should be taken from.
                                                    returned: on success
                                                    type: str
                                                    sample: VALIDATION_BLOCK
                                        source_uri_details:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                uri:
                                                    description:
                                                        - The discovery URI for the auth server.
                                                    returned: on success
                                                    type: str
                                                    sample: uri_example
                                                type:
                                                    description:
                                                        - Type of the Uri detail.
                                                    returned: on success
                                                    type: str
                                                    sample: DISCOVERY_URI
                                        uri:
                                            description:
                                                - The uri from which to retrieve the key. It must be accessible
                                                  without authentication.
                                            returned: on success
                                            type: str
                                            sample: uri_example
                                        is_ssl_verify_disabled:
                                            description:
                                                - Defines whether or not to uphold SSL verification.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        max_cache_duration_in_hours:
                                            description:
                                                - The duration for which the introspect URL response should be cached before it is
                                                  fetched again.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        type:
                                            description:
                                                - Type of the token validation policy.
                                            returned: on success
                                            type: str
                                            sample: STATIC_KEYS
                                        additional_validation_policy:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                issuers:
                                                    description:
                                                        - A list of parties that could have issued the token.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                audiences:
                                                    description:
                                                        - The list of intended recipients for the token.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                verify_claims:
                                                    description:
                                                        - A list of claims which should be validated to consider the token valid.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        key:
                                                            description:
                                                                - Name of the claim.
                                                            returned: on success
                                                            type: str
                                                            sample: key_example
                                                        values:
                                                            description:
                                                                - "The list of acceptable values for a given claim.
                                                                  If this value is \\"null\\" or empty and \\"isRequired\\" set to \\"true\\", then
                                                                  the presence of this claim in the JWT is validated."
                                                            returned: on success
                                                            type: list
                                                            sample: []
                                                        is_required:
                                                            description:
                                                                - "Whether the claim is required to be present in the JWT or not. If set
                                                                  to \\"false\\", the claim values will be matched only if the claim is
                                                                  present in the JWT."
                                                            returned: on success
                                                            type: bool
                                                            sample: true
                                        keys:
                                            description:
                                                - The set of static public keys.
                                            returned: on success
                                            type: complex
                                            contains:
                                                kty:
                                                    description:
                                                        - The key type.
                                                    returned: on success
                                                    type: str
                                                    sample: RSA
                                                use:
                                                    description:
                                                        - The intended use of the public key.
                                                    returned: on success
                                                    type: str
                                                    sample: sig
                                                key_ops:
                                                    description:
                                                        - The operations for which this key is to be used.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                alg:
                                                    description:
                                                        - The algorithm intended for use with this key.
                                                    returned: on success
                                                    type: str
                                                    sample: alg_example
                                                n:
                                                    description:
                                                        - The base64 url encoded modulus of the RSA public key represented
                                                          by this key.
                                                    returned: on success
                                                    type: str
                                                    sample: n_example
                                                e:
                                                    description:
                                                        - The base64 url encoded exponent of the RSA public key represented
                                                          by this key.
                                                    returned: on success
                                                    type: str
                                                    sample: e_example
                                                kid:
                                                    description:
                                                        - "A unique key ID. This key will be used to verify the signature of a
                                                          JWT with matching \\"kid\\"."
                                                    returned: on success
                                                    type: str
                                                    sample: kid_example
                                                format:
                                                    description:
                                                        - The format of the public key.
                                                    returned: on success
                                                    type: str
                                                    sample: JSON_WEB_KEY
                                                key:
                                                    description:
                                                        - The content of the PEM-encoded public key.
                                                    returned: on success
                                                    type: str
                                                    sample: key_example
                                validation_failure_policy:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        response_code:
                                            description:
                                                - HTTP response code, can include context variables.
                                            returned: on success
                                            type: str
                                            sample: response_code_example
                                        response_message:
                                            description:
                                                - HTTP response message.
                                            returned: on success
                                            type: str
                                            sample: response_message_example
                                        response_header_transformations:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                set_headers:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        items:
                                                            description:
                                                                - The list of headers.
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                name:
                                                                    description:
                                                                        - The case-insensitive name of the header.  This name must be unique across
                                                                          transformation policies.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: name_example
                                                                values:
                                                                    description:
                                                                        - A list of new values.  Each value can be a constant or may include one or more
                                                                          expressions enclosed within
                                                                          ${} delimiters.
                                                                    returned: on success
                                                                    type: list
                                                                    sample: []
                                                                if_exists:
                                                                    description:
                                                                        - If a header with the same name already exists in the request, OVERWRITE will overwrite
                                                                          the value,
                                                                          APPEND will append to the existing value, or SKIP will keep the existing value.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: OVERWRITE
                                                rename_headers:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        items:
                                                            description:
                                                                - The list of headers.
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                _from:
                                                                    description:
                                                                        - The original case-insensitive name of the header.  This name must be unique across
                                                                          transformation policies.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: _from_example
                                                                to:
                                                                    description:
                                                                        - The new name of the header.  This name must be unique across transformation policies.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: to_example
                                                filter_headers:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        type:
                                                            description:
                                                                - BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW
                                                                  permits only the headers in the list and removes all others, so it acts as an inclusion list.
                                                            returned: on success
                                                            type: str
                                                            sample: ALLOW
                                                        items:
                                                            description:
                                                                - The list of headers.
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                name:
                                                                    description:
                                                                        - The case-insensitive name of the header.  This name must be unique across
                                                                          transformation policies.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: name_example
                                        type:
                                            description:
                                                - Type of the Validation failure Policy.
                                            returned: on success
                                            type: str
                                            sample: MODIFY_RESPONSE
                                        client_details:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                client_id:
                                                    description:
                                                        - Client ID for the OAuth2/OIDC app.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
                                                client_secret_id:
                                                    description:
                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Vault
                                                          Service secret resource.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.clientsecret.oc1..xxxxxxEXAMPLExxxxxx"
                                                client_secret_version_number:
                                                    description:
                                                        - The version number of the client secret to use.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                                type:
                                                    description:
                                                        - To specify where the Client App details should be taken from.
                                                    returned: on success
                                                    type: str
                                                    sample: VALIDATION_BLOCK
                                        source_uri_details:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                uri:
                                                    description:
                                                        - The discovery URI for the auth server.
                                                    returned: on success
                                                    type: str
                                                    sample: uri_example
                                                type:
                                                    description:
                                                        - Type of the Uri detail.
                                                    returned: on success
                                                    type: str
                                                    sample: DISCOVERY_URI
                                        scopes:
                                            description:
                                                - List of scopes.
                                            returned: on success
                                            type: list
                                            sample: []
                                        max_expiry_duration_in_hours:
                                            description:
                                                - The duration for which the OAuth2 success token should be cached before it is
                                                  fetched again.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        use_cookies_for_session:
                                            description:
                                                - Defines whether or not to use cookies for session maintenance.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        use_cookies_for_intermediate_steps:
                                            description:
                                                - Defines whether or not to use cookies for OAuth2 intermediate steps.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        use_pkce:
                                            description:
                                                - Defines whether or not to support PKCE.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        response_type:
                                            description:
                                                - Response Type.
                                            returned: on success
                                            type: str
                                            sample: CODE
                                        fallback_redirect_path:
                                            description:
                                                - The path to be used as fallback after OAuth2.
                                            returned: on success
                                            type: str
                                            sample: fallback_redirect_path_example
                                        logout_path:
                                            description:
                                                - The path to be used as logout.
                                            returned: on success
                                            type: str
                                            sample: logout_path_example
                        rate_limiting:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                rate_in_requests_per_second:
                                    description:
                                        - The maximum number of requests per second to allow.
                                    returned: on success
                                    type: int
                                    sample: 56
                                rate_key:
                                    description:
                                        - The key used to group requests together.
                                    returned: on success
                                    type: str
                                    sample: CLIENT_IP
                        cors:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                allowed_origins:
                                    description:
                                        - "The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will
                                          send the Access-Control-Allow-Origin header with the best origin match for the circumstances. '*' will match
                                          any origins, and 'null' will match queries from 'file:' origins. All other origins must be qualified with the
                                          scheme, full hostname, and port if necessary."
                                    returned: on success
                                    type: list
                                    sample: []
                                allowed_methods:
                                    description:
                                        - "The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the
                                          Access-Control-Allow-Methods header. '*' will allow all methods."
                                    returned: on success
                                    type: list
                                    sample: []
                                allowed_headers:
                                    description:
                                        - "The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header.
                                          '*' will allow all headers."
                                    returned: on success
                                    type: list
                                    sample: []
                                exposed_headers:
                                    description:
                                        - "The list of headers that the client will be allowed to see from the response as indicated by the
                                          Access-Control-Expose-Headers header. '*' will expose all headers."
                                    returned: on success
                                    type: list
                                    sample: []
                                is_allow_credentials_enabled:
                                    description:
                                        - Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.
                                    returned: on success
                                    type: bool
                                    sample: true
                                max_age_in_seconds:
                                    description:
                                        - The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
                                          if greater than 0.
                                    returned: on success
                                    type: int
                                    sample: 56
                        mutual_tls:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_verified_certificate_required:
                                    description:
                                        - Determines whether to enable client verification when API Consumer makes connection to the gateway.
                                    returned: on success
                                    type: bool
                                    sample: true
                                allowed_sans:
                                    description:
                                        - Allowed list of CN or SAN which will be used for verification of certificate.
                                    returned: on success
                                    type: list
                                    sample: []
                        usage_plans:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                token_locations:
                                    description:
                                        - "A list of context variables specifying where API tokens may be located in a request.
                                          Example locations:
                                            - \\"request.headers[token]\\"
                                            - \\"request.query[token]\\"
                                            - \\"request.auth[Token]\\"
                                            - \\"request.path[TOKEN]\\""
                                    returned: on success
                                    type: list
                                    sample: []
                        dynamic_authentication:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                selection_source:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - Type of the Selection source to use.
                                            returned: on success
                                            type: str
                                            sample: SINGLE
                                        selector:
                                            description:
                                                - String describing the context variable used as selector.
                                            returned: on success
                                            type: str
                                            sample: selector_example
                                authentication_servers:
                                    description:
                                        - List of authentication servers to choose from during dynamic authentication.
                                    returned: on success
                                    type: complex
                                    contains:
                                        key:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                values:
                                                    description:
                                                        - The set of selection keys to match with the context variable in an incoming request. If the context
                                                          variable exactly matches one of the keys in the set, the request is sent to the route or
                                                          authentication server associated with the set.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                type:
                                                    description:
                                                        - Type of the selection key.
                                                    returned: on success
                                                    type: str
                                                    sample: ANY_OF
                                                is_default:
                                                    description:
                                                        - Specifies whether to use the route or authentication server associated with this selection key as the
                                                          default. The default is used if the value of a context variable in an incoming request does not match
                                                          any of the other selection key values when dynamically routing and dynamically authenticating
                                                          requests.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                                name:
                                                    description:
                                                        - Name assigned to the branch.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                expression:
                                                    description:
                                                        - "A selection key string containing a wildcard to match with the context variable in an incoming
                                                          request. If the context variable matches the string, the request is sent to the route or
                                                          authentication server associated with the selection key. Valid wildcards are '*' (zero or more
                                                          characters) and '+' (one or more characters). The string can only contain one wildcard, and the
                                                          wildcard must be at the start or the end of the string."
                                                    returned: on success
                                                    type: str
                                                    sample: expression_example
                                        authentication_server_detail:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                function_id:
                                                    description:
                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle
                                                          Functions function resource.
                                                    returned: on success
                                                    type: str
                                                    sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                                                parameters:
                                                    description:
                                                        - "A map where key is a user defined string and value is a context expressions whose values will be sent
                                                          to the custom auth function. Values should contain an expression.
                                                          Example: `{\\"foo\\": \\"request.header[abc]\\"}`"
                                                    returned: on success
                                                    type: dict
                                                    sample: {}
                                                cache_key:
                                                    description:
                                                        - "A list of keys from \\"parameters\\" attribute value whose values will be added to the cache key."
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                issuers:
                                                    description:
                                                        - A list of parties that could have issued the token.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                audiences:
                                                    description:
                                                        - The list of intended recipients for the token.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                verify_claims:
                                                    description:
                                                        - A list of claims which should be validated to consider the token valid.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        key:
                                                            description:
                                                                - Name of the claim.
                                                            returned: on success
                                                            type: str
                                                            sample: key_example
                                                        values:
                                                            description:
                                                                - "The list of acceptable values for a given claim.
                                                                  If this value is \\"null\\" or empty and \\"isRequired\\" set to \\"true\\", then
                                                                  the presence of this claim in the JWT is validated."
                                                            returned: on success
                                                            type: list
                                                            sample: []
                                                        is_required:
                                                            description:
                                                                - "Whether the claim is required to be present in the JWT or not. If set
                                                                  to \\"false\\", the claim values will be matched only if the claim is
                                                                  present in the JWT."
                                                            returned: on success
                                                            type: bool
                                                            sample: true
                                                public_keys:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        uri:
                                                            description:
                                                                - The uri from which to retrieve the key. It must be accessible
                                                                  without authentication.
                                                            returned: on success
                                                            type: str
                                                            sample: uri_example
                                                        is_ssl_verify_disabled:
                                                            description:
                                                                - Defines whether or not to uphold SSL verification.
                                                            returned: on success
                                                            type: bool
                                                            sample: true
                                                        max_cache_duration_in_hours:
                                                            description:
                                                                - The duration for which the JWKS should be cached before it is
                                                                  fetched again.
                                                            returned: on success
                                                            type: int
                                                            sample: 56
                                                        type:
                                                            description:
                                                                - Type of the public key set.
                                                            returned: on success
                                                            type: str
                                                            sample: STATIC_KEYS
                                                        keys:
                                                            description:
                                                                - The set of static public keys.
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                kty:
                                                                    description:
                                                                        - The key type.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: RSA
                                                                use:
                                                                    description:
                                                                        - The intended use of the public key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: sig
                                                                key_ops:
                                                                    description:
                                                                        - The operations for which this key is to be used.
                                                                    returned: on success
                                                                    type: list
                                                                    sample: []
                                                                alg:
                                                                    description:
                                                                        - The algorithm intended for use with this key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: alg_example
                                                                n:
                                                                    description:
                                                                        - The base64 url encoded modulus of the RSA public key represented
                                                                          by this key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: n_example
                                                                e:
                                                                    description:
                                                                        - The base64 url encoded exponent of the RSA public key represented
                                                                          by this key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: e_example
                                                                kid:
                                                                    description:
                                                                        - "A unique key ID. This key will be used to verify the signature of a
                                                                          JWT with matching \\"kid\\"."
                                                                    returned: on success
                                                                    type: str
                                                                    sample: kid_example
                                                                format:
                                                                    description:
                                                                        - The format of the public key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: JSON_WEB_KEY
                                                                key:
                                                                    description:
                                                                        - The content of the PEM-encoded public key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: key_example
                                                is_anonymous_access_allowed:
                                                    description:
                                                        - "Whether an unauthenticated user may access the API. Must be \\"true\\" to enable ANONYMOUS
                                                          route authorization."
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                                type:
                                                    description:
                                                        - Type of the authentication policy to use.
                                                    returned: on success
                                                    type: str
                                                    sample: CUSTOM_AUTHENTICATION
                                                token_header:
                                                    description:
                                                        - The name of the header containing the authentication token.
                                                    returned: on success
                                                    type: str
                                                    sample: token_header_example
                                                token_query_param:
                                                    description:
                                                        - The name of the query parameter containing the authentication token.
                                                    returned: on success
                                                    type: str
                                                    sample: token_query_param_example
                                                token_auth_scheme:
                                                    description:
                                                        - "The authentication scheme that is to be used when authenticating
                                                          the token. This must to be provided if \\"tokenHeader\\" is specified."
                                                    returned: on success
                                                    type: str
                                                    sample: token_auth_scheme_example
                                                max_clock_skew_in_seconds:
                                                    description:
                                                        - The maximum expected time difference between the system clocks
                                                          of the token issuer and the API Gateway.
                                                    returned: on success
                                                    type: float
                                                    sample: 3.4
                                                validation_policy:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        client_details:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                client_id:
                                                                    description:
                                                                        - Client ID for the OAuth2/OIDC app.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
                                                                client_secret_id:
                                                                    description:
                                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of
                                                                          the Oracle Vault Service secret resource.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: "ocid1.clientsecret.oc1..xxxxxxEXAMPLExxxxxx"
                                                                client_secret_version_number:
                                                                    description:
                                                                        - The version number of the client secret to use.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                type:
                                                                    description:
                                                                        - To specify where the Client App details should be taken from.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: VALIDATION_BLOCK
                                                        source_uri_details:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                uri:
                                                                    description:
                                                                        - The discovery URI for the auth server.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: uri_example
                                                                type:
                                                                    description:
                                                                        - Type of the Uri detail.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: DISCOVERY_URI
                                                        uri:
                                                            description:
                                                                - The uri from which to retrieve the key. It must be accessible
                                                                  without authentication.
                                                            returned: on success
                                                            type: str
                                                            sample: uri_example
                                                        is_ssl_verify_disabled:
                                                            description:
                                                                - Defines whether or not to uphold SSL verification.
                                                            returned: on success
                                                            type: bool
                                                            sample: true
                                                        max_cache_duration_in_hours:
                                                            description:
                                                                - The duration for which the introspect URL response should be cached before it is
                                                                  fetched again.
                                                            returned: on success
                                                            type: int
                                                            sample: 56
                                                        type:
                                                            description:
                                                                - Type of the token validation policy.
                                                            returned: on success
                                                            type: str
                                                            sample: STATIC_KEYS
                                                        additional_validation_policy:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                issuers:
                                                                    description:
                                                                        - A list of parties that could have issued the token.
                                                                    returned: on success
                                                                    type: list
                                                                    sample: []
                                                                audiences:
                                                                    description:
                                                                        - The list of intended recipients for the token.
                                                                    returned: on success
                                                                    type: list
                                                                    sample: []
                                                                verify_claims:
                                                                    description:
                                                                        - A list of claims which should be validated to consider the token valid.
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        key:
                                                                            description:
                                                                                - Name of the claim.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: key_example
                                                                        values:
                                                                            description:
                                                                                - "The list of acceptable values for a given claim.
                                                                                  If this value is \\"null\\" or empty and \\"isRequired\\" set to \\"true\\",
                                                                                  then
                                                                                  the presence of this claim in the JWT is validated."
                                                                            returned: on success
                                                                            type: list
                                                                            sample: []
                                                                        is_required:
                                                                            description:
                                                                                - "Whether the claim is required to be present in the JWT or not. If set
                                                                                  to \\"false\\", the claim values will be matched only if the claim is
                                                                                  present in the JWT."
                                                                            returned: on success
                                                                            type: bool
                                                                            sample: true
                                                        keys:
                                                            description:
                                                                - The set of static public keys.
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                kty:
                                                                    description:
                                                                        - The key type.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: RSA
                                                                use:
                                                                    description:
                                                                        - The intended use of the public key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: sig
                                                                key_ops:
                                                                    description:
                                                                        - The operations for which this key is to be used.
                                                                    returned: on success
                                                                    type: list
                                                                    sample: []
                                                                alg:
                                                                    description:
                                                                        - The algorithm intended for use with this key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: alg_example
                                                                n:
                                                                    description:
                                                                        - The base64 url encoded modulus of the RSA public key represented
                                                                          by this key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: n_example
                                                                e:
                                                                    description:
                                                                        - The base64 url encoded exponent of the RSA public key represented
                                                                          by this key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: e_example
                                                                kid:
                                                                    description:
                                                                        - "A unique key ID. This key will be used to verify the signature of a
                                                                          JWT with matching \\"kid\\"."
                                                                    returned: on success
                                                                    type: str
                                                                    sample: kid_example
                                                                format:
                                                                    description:
                                                                        - The format of the public key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: JSON_WEB_KEY
                                                                key:
                                                                    description:
                                                                        - The content of the PEM-encoded public key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: key_example
                                                validation_failure_policy:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        response_code:
                                                            description:
                                                                - HTTP response code, can include context variables.
                                                            returned: on success
                                                            type: str
                                                            sample: response_code_example
                                                        response_message:
                                                            description:
                                                                - HTTP response message.
                                                            returned: on success
                                                            type: str
                                                            sample: response_message_example
                                                        response_header_transformations:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                set_headers:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        items:
                                                                            description:
                                                                                - The list of headers.
                                                                            returned: on success
                                                                            type: complex
                                                                            contains:
                                                                                name:
                                                                                    description:
                                                                                        - The case-insensitive name of the header.  This name must be unique
                                                                                          across transformation policies.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: name_example
                                                                                values:
                                                                                    description:
                                                                                        - A list of new values.  Each value can be a constant or may include one
                                                                                          or more expressions enclosed within
                                                                                          ${} delimiters.
                                                                                    returned: on success
                                                                                    type: list
                                                                                    sample: []
                                                                                if_exists:
                                                                                    description:
                                                                                        - If a header with the same name already exists in the request,
                                                                                          OVERWRITE will overwrite the value,
                                                                                          APPEND will append to the existing value, or SKIP will keep the
                                                                                          existing value.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: OVERWRITE
                                                                rename_headers:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        items:
                                                                            description:
                                                                                - The list of headers.
                                                                            returned: on success
                                                                            type: complex
                                                                            contains:
                                                                                _from:
                                                                                    description:
                                                                                        - The original case-insensitive name of the header.  This name must be
                                                                                          unique across transformation policies.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: _from_example
                                                                                to:
                                                                                    description:
                                                                                        - The new name of the header.  This name must be unique across
                                                                                          transformation policies.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: to_example
                                                                filter_headers:
                                                                    description:
                                                                        - ""
                                                                    returned: on success
                                                                    type: complex
                                                                    contains:
                                                                        type:
                                                                            description:
                                                                                - BLOCK drops any headers that are in the list of items, so it acts as an
                                                                                  exclusion list.  ALLOW
                                                                                  permits only the headers in the list and removes all others, so it acts as an
                                                                                  inclusion list.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: ALLOW
                                                                        items:
                                                                            description:
                                                                                - The list of headers.
                                                                            returned: on success
                                                                            type: complex
                                                                            contains:
                                                                                name:
                                                                                    description:
                                                                                        - The case-insensitive name of the header.  This name must be unique
                                                                                          across transformation policies.
                                                                                    returned: on success
                                                                                    type: str
                                                                                    sample: name_example
                                                        type:
                                                            description:
                                                                - Type of the Validation failure Policy.
                                                            returned: on success
                                                            type: str
                                                            sample: MODIFY_RESPONSE
                                                        client_details:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                client_id:
                                                                    description:
                                                                        - Client ID for the OAuth2/OIDC app.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx"
                                                                client_secret_id:
                                                                    description:
                                                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of
                                                                          the Oracle Vault Service secret resource.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: "ocid1.clientsecret.oc1..xxxxxxEXAMPLExxxxxx"
                                                                client_secret_version_number:
                                                                    description:
                                                                        - The version number of the client secret to use.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                type:
                                                                    description:
                                                                        - To specify where the Client App details should be taken from.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: VALIDATION_BLOCK
                                                        source_uri_details:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                uri:
                                                                    description:
                                                                        - The discovery URI for the auth server.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: uri_example
                                                                type:
                                                                    description:
                                                                        - Type of the Uri detail.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: DISCOVERY_URI
                                                        scopes:
                                                            description:
                                                                - List of scopes.
                                                            returned: on success
                                                            type: list
                                                            sample: []
                                                        max_expiry_duration_in_hours:
                                                            description:
                                                                - The duration for which the OAuth2 success token should be cached before it is
                                                                  fetched again.
                                                            returned: on success
                                                            type: int
                                                            sample: 56
                                                        use_cookies_for_session:
                                                            description:
                                                                - Defines whether or not to use cookies for session maintenance.
                                                            returned: on success
                                                            type: bool
                                                            sample: true
                                                        use_cookies_for_intermediate_steps:
                                                            description:
                                                                - Defines whether or not to use cookies for OAuth2 intermediate steps.
                                                            returned: on success
                                                            type: bool
                                                            sample: true
                                                        use_pkce:
                                                            description:
                                                                - Defines whether or not to support PKCE.
                                                            returned: on success
                                                            type: bool
                                                            sample: true
                                                        response_type:
                                                            description:
                                                                - Response Type.
                                                            returned: on success
                                                            type: str
                                                            sample: CODE
                                                        fallback_redirect_path:
                                                            description:
                                                                - The path to be used as fallback after OAuth2.
                                                            returned: on success
                                                            type: str
                                                            sample: fallback_redirect_path_example
                                                        logout_path:
                                                            description:
                                                                - The path to be used as logout.
                                                            returned: on success
                                                            type: str
                                                            sample: logout_path_example
                logging_policies:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        access_log:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_enabled:
                                    description:
                                        - Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.
                                        - Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs
                                          for an API Deployment. If there is an active log object for the API Deployment and its
                                          category is set to 'access' in OCI Logging service, the logs will not be uploaded to the
                                          legacy OCI Object Storage log archival bucket.
                                        - Please note that the functionality to push to the legacy OCI Object Storage log
                                          archival bucket has been deprecated and will be removed in the future.
                                    returned: on success
                                    type: bool
                                    sample: true
                        execution_log:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                is_enabled:
                                    description:
                                        - Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.
                                        - Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs
                                          for an API Deployment. If there is an active log object for the API Deployment and its
                                          category is set to 'execution' in OCI Logging service, the logs will not be uploaded to the legacy
                                          OCI Object Storage log archival bucket.
                                        - Please note that the functionality to push to the legacy OCI Object Storage log
                                          archival bucket has been deprecated and will be removed in the future.
                                    returned: on success
                                    type: bool
                                    sample: true
                                log_level:
                                    description:
                                        - Specifies the log level used to control logging output of execution logs.
                                          Enabling logging at a given level also enables logging at all higher levels.
                                    returned: on success
                                    type: str
                                    sample: INFO
                routes:
                    description:
                        - A list of routes that this API exposes.
                    returned: on success
                    type: complex
                    contains:
                        path:
                            description:
                                - A URL path pattern that must be matched on this route. The path pattern may contain a subset of RFC 6570 identifiers
                                  to allow wildcard and parameterized matching.
                            returned: on success
                            type: str
                            sample: path_example
                        methods:
                            description:
                                - A list of allowed methods on this route.
                            returned: on success
                            type: list
                            sample: []
                        request_policies:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                authorization:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        allowed_scope:
                                            description:
                                                - A user whose scope includes any of these access ranges is allowed on
                                                  this route. Access ranges are case-sensitive.
                                            returned: on success
                                            type: list
                                            sample: []
                                        type:
                                            description:
                                                - "Indicates how authorization should be applied. For a type of ANY_OF, an \\"allowedScope\\"
                                                  property must also be specified. Otherwise, only a type is required. For a type of ANONYMOUS, an
                                                  authenticated API must have the \\"isAnonymousAccessAllowed\\" property set to \\"true\\" in the
                                                  authentication
                                                  policy."
                                            returned: on success
                                            type: str
                                            sample: ANONYMOUS
                                cors:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        allowed_origins:
                                            description:
                                                - "The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will
                                                  send the Access-Control-Allow-Origin header with the best origin match for the circumstances. '*' will match
                                                  any origins, and 'null' will match queries from 'file:' origins. All other origins must be qualified with the
                                                  scheme, full hostname, and port if necessary."
                                            returned: on success
                                            type: list
                                            sample: []
                                        allowed_methods:
                                            description:
                                                - "The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the
                                                  Access-Control-Allow-Methods header. '*' will allow all methods."
                                            returned: on success
                                            type: list
                                            sample: []
                                        allowed_headers:
                                            description:
                                                - "The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header.
                                                  '*' will allow all headers."
                                            returned: on success
                                            type: list
                                            sample: []
                                        exposed_headers:
                                            description:
                                                - "The list of headers that the client will be allowed to see from the response as indicated by the
                                                  Access-Control-Expose-Headers header. '*' will expose all headers."
                                            returned: on success
                                            type: list
                                            sample: []
                                        is_allow_credentials_enabled:
                                            description:
                                                - Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        max_age_in_seconds:
                                            description:
                                                - The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
                                                  if greater than 0.
                                            returned: on success
                                            type: int
                                            sample: 56
                                query_parameter_validations:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        parameters:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                required:
                                                    description:
                                                        - Determines if the parameter is required in the request.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                                name:
                                                    description:
                                                        - Parameter name.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                        validation_mode:
                                            description:
                                                - Validation behavior mode.
                                                - In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
                                                  and not sent to the backend.
                                                - In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
                                                  will follow the normal path.
                                                - "`DISABLED` type turns the validation off."
                                            returned: on success
                                            type: str
                                            sample: ENFORCING
                                header_validations:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        headers:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                required:
                                                    description:
                                                        - Determines if the header is required in the request.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                                name:
                                                    description:
                                                        - Parameter name.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                        validation_mode:
                                            description:
                                                - Validation behavior mode.
                                                - In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
                                                  and not sent to the backend.
                                                - In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
                                                  will follow the normal path.
                                                - "`DISABLED` type turns the validation off."
                                            returned: on success
                                            type: str
                                            sample: ENFORCING
                                body_validation:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        required:
                                            description:
                                                - Determines if the request body is required in the request.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        content:
                                            description:
                                                - The content of the request body. The key is a L(media type
                                                  range,https://tools.ietf.org/html/rfc7231#appendix-D)
                                                  subset restricted to the following schema
                                                - "   key ::= (
                                                            / (  \\"*\\" \\"/\\" \\"*\\" )
                                                            / ( type \\"/\\" \\"*\\" )
                                                            / ( type \\"/\\" subtype )
                                                            )"
                                                - "For requests that match multiple keys, only the most specific key is applicable.
                                                  e.g. `text/plain` overrides `text/*`"
                                            returned: on success
                                            type: complex
                                            contains:
                                                validation_type:
                                                    description:
                                                        - Validation type defines the content validation method.
                                                        - Make the validation to first parse the body as the respective format.
                                                    returned: on success
                                                    type: str
                                                    sample: NONE
                                        validation_mode:
                                            description:
                                                - Validation behavior mode.
                                                - In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
                                                  and not sent to the backend.
                                                - In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
                                                  will follow the normal path.
                                                - "`DISABLED` type turns the validation off."
                                            returned: on success
                                            type: str
                                            sample: ENFORCING
                                header_transformations:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        set_headers:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                items:
                                                    description:
                                                        - The list of headers.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        name:
                                                            description:
                                                                - The case-insensitive name of the header.  This name must be unique across transformation
                                                                  policies.
                                                            returned: on success
                                                            type: str
                                                            sample: name_example
                                                        values:
                                                            description:
                                                                - A list of new values.  Each value can be a constant or may include one or more expressions
                                                                  enclosed within
                                                                  ${} delimiters.
                                                            returned: on success
                                                            type: list
                                                            sample: []
                                                        if_exists:
                                                            description:
                                                                - If a header with the same name already exists in the request, OVERWRITE will overwrite the
                                                                  value,
                                                                  APPEND will append to the existing value, or SKIP will keep the existing value.
                                                            returned: on success
                                                            type: str
                                                            sample: OVERWRITE
                                        rename_headers:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                items:
                                                    description:
                                                        - The list of headers.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        _from:
                                                            description:
                                                                - The original case-insensitive name of the header.  This name must be unique across
                                                                  transformation policies.
                                                            returned: on success
                                                            type: str
                                                            sample: _from_example
                                                        to:
                                                            description:
                                                                - The new name of the header.  This name must be unique across transformation policies.
                                                            returned: on success
                                                            type: str
                                                            sample: to_example
                                        filter_headers:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                type:
                                                    description:
                                                        - BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW
                                                          permits only the headers in the list and removes all others, so it acts as an inclusion list.
                                                    returned: on success
                                                    type: str
                                                    sample: ALLOW
                                                items:
                                                    description:
                                                        - The list of headers.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        name:
                                                            description:
                                                                - The case-insensitive name of the header.  This name must be unique across transformation
                                                                  policies.
                                                            returned: on success
                                                            type: str
                                                            sample: name_example
                                query_parameter_transformations:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        set_query_parameters:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                items:
                                                    description:
                                                        - The list of query parameters.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        name:
                                                            description:
                                                                - The case-sensitive name of the query parameter.  This name must be unique across
                                                                  transformation policies.
                                                            returned: on success
                                                            type: str
                                                            sample: name_example
                                                        values:
                                                            description:
                                                                - A list of new values.  Each value can be a constant or may include one or more expressions
                                                                  enclosed within
                                                                  ${} delimiters.
                                                            returned: on success
                                                            type: list
                                                            sample: []
                                                        if_exists:
                                                            description:
                                                                - If a query parameter with the same name already exists in the request, OVERWRITE will
                                                                  overwrite the value,
                                                                  APPEND will append to the existing value, or SKIP will keep the existing value.
                                                            returned: on success
                                                            type: str
                                                            sample: OVERWRITE
                                        rename_query_parameters:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                items:
                                                    description:
                                                        - The list of query parameters.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        _from:
                                                            description:
                                                                - The original case-sensitive name of the query parameter.  This name must be unique across
                                                                  transformation
                                                                  policies.
                                                            returned: on success
                                                            type: str
                                                            sample: _from_example
                                                        to:
                                                            description:
                                                                - The new name of the query parameter.  This name must be unique across transformation policies.
                                                            returned: on success
                                                            type: str
                                                            sample: to_example
                                        filter_query_parameters:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                type:
                                                    description:
                                                        - BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list.
                                                          ALLOW
                                                          permits only the parameters in the list and removes all others, so it acts as an inclusion list.
                                                    returned: on success
                                                    type: str
                                                    sample: ALLOW
                                                items:
                                                    description:
                                                        - The list of query parameters.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        name:
                                                            description:
                                                                - The case-sensitive name of the query parameter.
                                                            returned: on success
                                                            type: str
                                                            sample: name_example
                                response_cache_lookup:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - Type of the Response Cache Store Policy.
                                            returned: on success
                                            type: str
                                            sample: SIMPLE_LOOKUP_POLICY
                                        is_enabled:
                                            description:
                                                - Whether this policy is currently enabled.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_private_caching_enabled:
                                            description:
                                                - Set true to allow caching responses where the request has an Authorization header. Ensure you have configured
                                                  your
                                                  cache key additions to get the level of isolation across authenticated requests that you require.
                                                - When false, any request with an Authorization header will not be stored in the Response Cache.
                                                - If using the CustomAuthenticationPolicy then the tokenHeader/tokenQueryParam are also subject to this check.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        cache_key_additions:
                                            description:
                                                - A list of context expressions whose values will be added to the base cache key. Values should contain an
                                                  expression enclosed within
                                                  ${} delimiters. Only the request context is available.
                                            returned: on success
                                            type: list
                                            sample: []
                        response_policies:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                header_transformations:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        set_headers:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                items:
                                                    description:
                                                        - The list of headers.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        name:
                                                            description:
                                                                - The case-insensitive name of the header.  This name must be unique across transformation
                                                                  policies.
                                                            returned: on success
                                                            type: str
                                                            sample: name_example
                                                        values:
                                                            description:
                                                                - A list of new values.  Each value can be a constant or may include one or more expressions
                                                                  enclosed within
                                                                  ${} delimiters.
                                                            returned: on success
                                                            type: list
                                                            sample: []
                                                        if_exists:
                                                            description:
                                                                - If a header with the same name already exists in the request, OVERWRITE will overwrite the
                                                                  value,
                                                                  APPEND will append to the existing value, or SKIP will keep the existing value.
                                                            returned: on success
                                                            type: str
                                                            sample: OVERWRITE
                                        rename_headers:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                items:
                                                    description:
                                                        - The list of headers.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        _from:
                                                            description:
                                                                - The original case-insensitive name of the header.  This name must be unique across
                                                                  transformation policies.
                                                            returned: on success
                                                            type: str
                                                            sample: _from_example
                                                        to:
                                                            description:
                                                                - The new name of the header.  This name must be unique across transformation policies.
                                                            returned: on success
                                                            type: str
                                                            sample: to_example
                                        filter_headers:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                type:
                                                    description:
                                                        - BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW
                                                          permits only the headers in the list and removes all others, so it acts as an inclusion list.
                                                    returned: on success
                                                    type: str
                                                    sample: ALLOW
                                                items:
                                                    description:
                                                        - The list of headers.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        name:
                                                            description:
                                                                - The case-insensitive name of the header.  This name must be unique across transformation
                                                                  policies.
                                                            returned: on success
                                                            type: str
                                                            sample: name_example
                                response_cache_store:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - Type of the Response Cache Store Policy.
                                            returned: on success
                                            type: str
                                            sample: FIXED_TTL_STORE_POLICY
                                        time_to_live_in_seconds:
                                            description:
                                                - Sets the number of seconds for a response from a backend being stored in the Response Cache before it expires.
                                            returned: on success
                                            type: int
                                            sample: 56
                        logging_policies:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                access_log:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        is_enabled:
                                            description:
                                                - Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.
                                                - Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs
                                                  for an API Deployment. If there is an active log object for the API Deployment and its
                                                  category is set to 'access' in OCI Logging service, the logs will not be uploaded to the
                                                  legacy OCI Object Storage log archival bucket.
                                                - Please note that the functionality to push to the legacy OCI Object Storage log
                                                  archival bucket has been deprecated and will be removed in the future.
                                            returned: on success
                                            type: bool
                                            sample: true
                                execution_log:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        is_enabled:
                                            description:
                                                - Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.
                                                - Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs
                                                  for an API Deployment. If there is an active log object for the API Deployment and its
                                                  category is set to 'execution' in OCI Logging service, the logs will not be uploaded to the legacy
                                                  OCI Object Storage log archival bucket.
                                                - Please note that the functionality to push to the legacy OCI Object Storage log
                                                  archival bucket has been deprecated and will be removed in the future.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        log_level:
                                            description:
                                                - Specifies the log level used to control logging output of execution logs.
                                                  Enabling logging at a given level also enables logging at all higher levels.
                                            returned: on success
                                            type: str
                                            sample: INFO
                        backend:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                selection_source:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - Type of the Selection source to use.
                                            returned: on success
                                            type: str
                                            sample: SINGLE
                                        selector:
                                            description:
                                                - String describing the context variable used as selector.
                                            returned: on success
                                            type: str
                                            sample: selector_example
                                routing_backends:
                                    description:
                                        - List of backends to chose from for Dynamic Routing.
                                    returned: on success
                                    type: complex
                                    contains:
                                        key:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                values:
                                                    description:
                                                        - The set of selection keys to match with the context variable in an incoming request. If the context
                                                          variable exactly matches one of the keys in the set, the request is sent to the route or
                                                          authentication server associated with the set.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                type:
                                                    description:
                                                        - Type of the selection key.
                                                    returned: on success
                                                    type: str
                                                    sample: ANY_OF
                                                is_default:
                                                    description:
                                                        - Specifies whether to use the route or authentication server associated with this selection key as the
                                                          default. The default is used if the value of a context variable in an incoming request does not match
                                                          any of the other selection key values when dynamically routing and dynamically authenticating
                                                          requests.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                                name:
                                                    description:
                                                        - Name assigned to the branch.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                expression:
                                                    description:
                                                        - "A selection key string containing a wildcard to match with the context variable in an incoming
                                                          request. If the context variable matches the string, the request is sent to the route or
                                                          authentication server associated with the selection key. Valid wildcards are '*' (zero or more
                                                          characters) and '+' (one or more characters). The string can only contain one wildcard, and the
                                                          wildcard must be at the start or the end of the string."
                                                    returned: on success
                                                    type: str
                                                    sample: expression_example
                                        backend:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                type:
                                                    description:
                                                        - Type of the API backend.
                                                    returned: on success
                                                    type: str
                                                    sample: ORACLE_FUNCTIONS_BACKEND
                                url:
                                    description:
                                        - ""
                                    returned: on success
                                    type: str
                                    sample: url_example
                                connect_timeout_in_seconds:
                                    description:
                                        - Defines a timeout for establishing a connection with a proxied server.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                read_timeout_in_seconds:
                                    description:
                                        - Defines a timeout for reading a response from the proxied server.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                send_timeout_in_seconds:
                                    description:
                                        - Defines a timeout for transmitting a request to the proxied server.
                                    returned: on success
                                    type: float
                                    sample: 3.4
                                is_ssl_verify_disabled:
                                    description:
                                        - Defines whether or not to uphold SSL verification.
                                    returned: on success
                                    type: bool
                                    sample: true
                                allowed_post_logout_uris:
                                    description:
                                        - ""
                                    returned: on success
                                    type: list
                                    sample: []
                                post_logout_state:
                                    description:
                                        - Defines a state that should be shared on redirecting to postLogout URL.
                                    returned: on success
                                    type: str
                                    sample: post_logout_state_example
                                function_id:
                                    description:
                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function
                                          resource.
                                    returned: on success
                                    type: str
                                    sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                                type:
                                    description:
                                        - Type of the API backend.
                                    returned: on success
                                    type: str
                                    sample: ORACLE_FUNCTIONS_BACKEND
                                body:
                                    description:
                                        - The body of the stock response from the mock backend.
                                    returned: on success
                                    type: str
                                    sample: body_example
                                status:
                                    description:
                                        - The status code of the stock response from the mock backend.
                                    returned: on success
                                    type: int
                                    sample: 56
                                headers:
                                    description:
                                        - The headers of the stock response from the mock backend.
                                    returned: on success
                                    type: complex
                                    contains:
                                        name:
                                            description:
                                                - Name of the header.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        value:
                                            description:
                                                - Value of the header.
                                            returned: on success
                                            type: str
                                            sample: value_example
        time_created:
            description:
                - The time this resource was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time this resource was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the deployment.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a
                  resource in a Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair
                  with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "gateway_id": "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "path_prefix": "path_prefix_example",
        "endpoint": "endpoint_example",
        "specification": {
            "request_policies": {
                "authentication": {
                    "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
                    "parameters": {},
                    "cache_key": [],
                    "issuers": [],
                    "audiences": [],
                    "verify_claims": [{
                        "key": "key_example",
                        "values": [],
                        "is_required": true
                    }],
                    "public_keys": {
                        "uri": "uri_example",
                        "is_ssl_verify_disabled": true,
                        "max_cache_duration_in_hours": 56,
                        "type": "STATIC_KEYS",
                        "keys": [{
                            "kty": "RSA",
                            "use": "sig",
                            "key_ops": [],
                            "alg": "alg_example",
                            "n": "n_example",
                            "e": "e_example",
                            "kid": "kid_example",
                            "format": "JSON_WEB_KEY",
                            "key": "key_example"
                        }]
                    },
                    "is_anonymous_access_allowed": true,
                    "type": "CUSTOM_AUTHENTICATION",
                    "token_header": "token_header_example",
                    "token_query_param": "token_query_param_example",
                    "token_auth_scheme": "token_auth_scheme_example",
                    "max_clock_skew_in_seconds": 3.4,
                    "validation_policy": {
                        "client_details": {
                            "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
                            "client_secret_id": "ocid1.clientsecret.oc1..xxxxxxEXAMPLExxxxxx",
                            "client_secret_version_number": 56,
                            "type": "VALIDATION_BLOCK"
                        },
                        "source_uri_details": {
                            "uri": "uri_example",
                            "type": "DISCOVERY_URI"
                        },
                        "uri": "uri_example",
                        "is_ssl_verify_disabled": true,
                        "max_cache_duration_in_hours": 56,
                        "type": "STATIC_KEYS",
                        "additional_validation_policy": {
                            "issuers": [],
                            "audiences": [],
                            "verify_claims": [{
                                "key": "key_example",
                                "values": [],
                                "is_required": true
                            }]
                        },
                        "keys": [{
                            "kty": "RSA",
                            "use": "sig",
                            "key_ops": [],
                            "alg": "alg_example",
                            "n": "n_example",
                            "e": "e_example",
                            "kid": "kid_example",
                            "format": "JSON_WEB_KEY",
                            "key": "key_example"
                        }]
                    },
                    "validation_failure_policy": {
                        "response_code": "response_code_example",
                        "response_message": "response_message_example",
                        "response_header_transformations": {
                            "set_headers": {
                                "items": [{
                                    "name": "name_example",
                                    "values": [],
                                    "if_exists": "OVERWRITE"
                                }]
                            },
                            "rename_headers": {
                                "items": [{
                                    "_from": "_from_example",
                                    "to": "to_example"
                                }]
                            },
                            "filter_headers": {
                                "type": "ALLOW",
                                "items": [{
                                    "name": "name_example"
                                }]
                            }
                        },
                        "type": "MODIFY_RESPONSE",
                        "client_details": {
                            "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
                            "client_secret_id": "ocid1.clientsecret.oc1..xxxxxxEXAMPLExxxxxx",
                            "client_secret_version_number": 56,
                            "type": "VALIDATION_BLOCK"
                        },
                        "source_uri_details": {
                            "uri": "uri_example",
                            "type": "DISCOVERY_URI"
                        },
                        "scopes": [],
                        "max_expiry_duration_in_hours": 56,
                        "use_cookies_for_session": true,
                        "use_cookies_for_intermediate_steps": true,
                        "use_pkce": true,
                        "response_type": "CODE",
                        "fallback_redirect_path": "fallback_redirect_path_example",
                        "logout_path": "logout_path_example"
                    }
                },
                "rate_limiting": {
                    "rate_in_requests_per_second": 56,
                    "rate_key": "CLIENT_IP"
                },
                "cors": {
                    "allowed_origins": [],
                    "allowed_methods": [],
                    "allowed_headers": [],
                    "exposed_headers": [],
                    "is_allow_credentials_enabled": true,
                    "max_age_in_seconds": 56
                },
                "mutual_tls": {
                    "is_verified_certificate_required": true,
                    "allowed_sans": []
                },
                "usage_plans": {
                    "token_locations": []
                },
                "dynamic_authentication": {
                    "selection_source": {
                        "type": "SINGLE",
                        "selector": "selector_example"
                    },
                    "authentication_servers": [{
                        "key": {
                            "values": [],
                            "type": "ANY_OF",
                            "is_default": true,
                            "name": "name_example",
                            "expression": "expression_example"
                        },
                        "authentication_server_detail": {
                            "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
                            "parameters": {},
                            "cache_key": [],
                            "issuers": [],
                            "audiences": [],
                            "verify_claims": [{
                                "key": "key_example",
                                "values": [],
                                "is_required": true
                            }],
                            "public_keys": {
                                "uri": "uri_example",
                                "is_ssl_verify_disabled": true,
                                "max_cache_duration_in_hours": 56,
                                "type": "STATIC_KEYS",
                                "keys": [{
                                    "kty": "RSA",
                                    "use": "sig",
                                    "key_ops": [],
                                    "alg": "alg_example",
                                    "n": "n_example",
                                    "e": "e_example",
                                    "kid": "kid_example",
                                    "format": "JSON_WEB_KEY",
                                    "key": "key_example"
                                }]
                            },
                            "is_anonymous_access_allowed": true,
                            "type": "CUSTOM_AUTHENTICATION",
                            "token_header": "token_header_example",
                            "token_query_param": "token_query_param_example",
                            "token_auth_scheme": "token_auth_scheme_example",
                            "max_clock_skew_in_seconds": 3.4,
                            "validation_policy": {
                                "client_details": {
                                    "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
                                    "client_secret_id": "ocid1.clientsecret.oc1..xxxxxxEXAMPLExxxxxx",
                                    "client_secret_version_number": 56,
                                    "type": "VALIDATION_BLOCK"
                                },
                                "source_uri_details": {
                                    "uri": "uri_example",
                                    "type": "DISCOVERY_URI"
                                },
                                "uri": "uri_example",
                                "is_ssl_verify_disabled": true,
                                "max_cache_duration_in_hours": 56,
                                "type": "STATIC_KEYS",
                                "additional_validation_policy": {
                                    "issuers": [],
                                    "audiences": [],
                                    "verify_claims": [{
                                        "key": "key_example",
                                        "values": [],
                                        "is_required": true
                                    }]
                                },
                                "keys": [{
                                    "kty": "RSA",
                                    "use": "sig",
                                    "key_ops": [],
                                    "alg": "alg_example",
                                    "n": "n_example",
                                    "e": "e_example",
                                    "kid": "kid_example",
                                    "format": "JSON_WEB_KEY",
                                    "key": "key_example"
                                }]
                            },
                            "validation_failure_policy": {
                                "response_code": "response_code_example",
                                "response_message": "response_message_example",
                                "response_header_transformations": {
                                    "set_headers": {
                                        "items": [{
                                            "name": "name_example",
                                            "values": [],
                                            "if_exists": "OVERWRITE"
                                        }]
                                    },
                                    "rename_headers": {
                                        "items": [{
                                            "_from": "_from_example",
                                            "to": "to_example"
                                        }]
                                    },
                                    "filter_headers": {
                                        "type": "ALLOW",
                                        "items": [{
                                            "name": "name_example"
                                        }]
                                    }
                                },
                                "type": "MODIFY_RESPONSE",
                                "client_details": {
                                    "client_id": "ocid1.client.oc1..xxxxxxEXAMPLExxxxxx",
                                    "client_secret_id": "ocid1.clientsecret.oc1..xxxxxxEXAMPLExxxxxx",
                                    "client_secret_version_number": 56,
                                    "type": "VALIDATION_BLOCK"
                                },
                                "source_uri_details": {
                                    "uri": "uri_example",
                                    "type": "DISCOVERY_URI"
                                },
                                "scopes": [],
                                "max_expiry_duration_in_hours": 56,
                                "use_cookies_for_session": true,
                                "use_cookies_for_intermediate_steps": true,
                                "use_pkce": true,
                                "response_type": "CODE",
                                "fallback_redirect_path": "fallback_redirect_path_example",
                                "logout_path": "logout_path_example"
                            }
                        }
                    }]
                }
            },
            "logging_policies": {
                "access_log": {
                    "is_enabled": true
                },
                "execution_log": {
                    "is_enabled": true,
                    "log_level": "INFO"
                }
            },
            "routes": [{
                "path": "path_example",
                "methods": [],
                "request_policies": {
                    "authorization": {
                        "allowed_scope": [],
                        "type": "ANONYMOUS"
                    },
                    "cors": {
                        "allowed_origins": [],
                        "allowed_methods": [],
                        "allowed_headers": [],
                        "exposed_headers": [],
                        "is_allow_credentials_enabled": true,
                        "max_age_in_seconds": 56
                    },
                    "query_parameter_validations": {
                        "parameters": [{
                            "required": true,
                            "name": "name_example"
                        }],
                        "validation_mode": "ENFORCING"
                    },
                    "header_validations": {
                        "headers": [{
                            "required": true,
                            "name": "name_example"
                        }],
                        "validation_mode": "ENFORCING"
                    },
                    "body_validation": {
                        "required": true,
                        "content": {
                            "validation_type": "NONE"
                        },
                        "validation_mode": "ENFORCING"
                    },
                    "header_transformations": {
                        "set_headers": {
                            "items": [{
                                "name": "name_example",
                                "values": [],
                                "if_exists": "OVERWRITE"
                            }]
                        },
                        "rename_headers": {
                            "items": [{
                                "_from": "_from_example",
                                "to": "to_example"
                            }]
                        },
                        "filter_headers": {
                            "type": "ALLOW",
                            "items": [{
                                "name": "name_example"
                            }]
                        }
                    },
                    "query_parameter_transformations": {
                        "set_query_parameters": {
                            "items": [{
                                "name": "name_example",
                                "values": [],
                                "if_exists": "OVERWRITE"
                            }]
                        },
                        "rename_query_parameters": {
                            "items": [{
                                "_from": "_from_example",
                                "to": "to_example"
                            }]
                        },
                        "filter_query_parameters": {
                            "type": "ALLOW",
                            "items": [{
                                "name": "name_example"
                            }]
                        }
                    },
                    "response_cache_lookup": {
                        "type": "SIMPLE_LOOKUP_POLICY",
                        "is_enabled": true,
                        "is_private_caching_enabled": true,
                        "cache_key_additions": []
                    }
                },
                "response_policies": {
                    "header_transformations": {
                        "set_headers": {
                            "items": [{
                                "name": "name_example",
                                "values": [],
                                "if_exists": "OVERWRITE"
                            }]
                        },
                        "rename_headers": {
                            "items": [{
                                "_from": "_from_example",
                                "to": "to_example"
                            }]
                        },
                        "filter_headers": {
                            "type": "ALLOW",
                            "items": [{
                                "name": "name_example"
                            }]
                        }
                    },
                    "response_cache_store": {
                        "type": "FIXED_TTL_STORE_POLICY",
                        "time_to_live_in_seconds": 56
                    }
                },
                "logging_policies": {
                    "access_log": {
                        "is_enabled": true
                    },
                    "execution_log": {
                        "is_enabled": true,
                        "log_level": "INFO"
                    }
                },
                "backend": {
                    "selection_source": {
                        "type": "SINGLE",
                        "selector": "selector_example"
                    },
                    "routing_backends": [{
                        "key": {
                            "values": [],
                            "type": "ANY_OF",
                            "is_default": true,
                            "name": "name_example",
                            "expression": "expression_example"
                        },
                        "backend": {
                            "type": "ORACLE_FUNCTIONS_BACKEND"
                        }
                    }],
                    "url": "url_example",
                    "connect_timeout_in_seconds": 3.4,
                    "read_timeout_in_seconds": 3.4,
                    "send_timeout_in_seconds": 3.4,
                    "is_ssl_verify_disabled": true,
                    "allowed_post_logout_uris": [],
                    "post_logout_state": "post_logout_state_example",
                    "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
                    "type": "ORACLE_FUNCTIONS_BACKEND",
                    "body": "body_example",
                    "status": 56,
                    "headers": [{
                        "name": "name_example",
                        "value": "value_example"
                    }]
                }
            }]
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.apigateway import WorkRequestsClient
    from oci.apigateway import DeploymentClient
    from oci.apigateway.models import ChangeDeploymentCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayDeploymentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    @staticmethod
    def get_module_resource_id_param():
        return "deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_id")

    def get_get_fn(self):
        return self.client.get_deployment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDeploymentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_deployment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                change_deployment_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ApigatewayDeploymentActionsHelperCustom = get_custom_class(
    "ApigatewayDeploymentActionsHelperCustom"
)


class ResourceHelper(
    ApigatewayDeploymentActionsHelperCustom, ApigatewayDeploymentActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            deployment_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deployment",
        service_client_class=DeploymentClient,
        namespace="apigateway",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
