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
module: oci_apigateway_deployment
short_description: Manage a Deployment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Deployment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new deployment.
    - "This resource has the following action operations in the M(oracle.oci.oci_apigateway_deployment_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    gateway_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
              resource is created.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    path_prefix:
        description:
            - A path on which to deploy all routes contained in the API
              deployment specification. For more information, see
              L(Deploying an API on an API Gateway by Creating an API
              Deployment,https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - "Example: `My new resource`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    specification:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            request_policies:
                description:
                    - ""
                type: dict
                suboptions:
                    authentication:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            validation_policy:
                                description:
                                    - ""
                                    - Required when type is 'TOKEN_AUTHENTICATION'
                                type: dict
                                suboptions:
                                    uri:
                                        description:
                                            - The uri from which to retrieve the key. It must be accessible
                                              without authentication.
                                            - Required when type is 'REMOTE_JWKS'
                                        type: str
                                    client_details:
                                        description:
                                            - ""
                                            - Required when type is 'REMOTE_DISCOVERY'
                                        type: dict
                                        suboptions:
                                            client_id:
                                                description:
                                                    - Client ID for the OAuth2/OIDC app.
                                                    - Required when type is 'CUSTOM'
                                                type: str
                                            client_secret_id:
                                                description:
                                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Vault
                                                      Service secret resource.
                                                    - Required when type is 'CUSTOM'
                                                type: str
                                            client_secret_version_number:
                                                description:
                                                    - The version number of the client secret to use.
                                                    - Required when type is 'CUSTOM'
                                                type: int
                                            type:
                                                description:
                                                    - To specify where the Client App details should be taken from.
                                                type: str
                                                choices:
                                                    - "CUSTOM"
                                                    - "VALIDATION_BLOCK"
                                                required: true
                                    source_uri_details:
                                        description:
                                            - ""
                                            - Required when type is 'REMOTE_DISCOVERY'
                                        type: dict
                                        suboptions:
                                            uri:
                                                description:
                                                    - The discovery URI for the auth server.
                                                    - Required when type is 'DISCOVERY_URI'
                                                type: str
                                            type:
                                                description:
                                                    - Type of the Uri detail.
                                                type: str
                                                choices:
                                                    - "DISCOVERY_URI"
                                                    - "VALIDATION_BLOCK"
                                                required: true
                                    is_ssl_verify_disabled:
                                        description:
                                            - Defines whether or not to uphold SSL verification.
                                            - Applicable when type is one of ['REMOTE_JWKS', 'REMOTE_DISCOVERY']
                                        type: bool
                                    max_cache_duration_in_hours:
                                        description:
                                            - The duration for which the JWKS should be cached before it is
                                              fetched again.
                                            - Applicable when type is one of ['REMOTE_JWKS', 'REMOTE_DISCOVERY']
                                        type: int
                                    type:
                                        description:
                                            - Type of the token validation policy.
                                        type: str
                                        choices:
                                            - "REMOTE_JWKS"
                                            - "REMOTE_DISCOVERY"
                                            - "STATIC_KEYS"
                                        required: true
                                    additional_validation_policy:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            issuers:
                                                description:
                                                    - A list of parties that could have issued the token.
                                                    - Applicable when type is 'REMOTE_JWKS'
                                                type: list
                                                elements: str
                                            audiences:
                                                description:
                                                    - The list of intended recipients for the token.
                                                    - Applicable when type is 'REMOTE_JWKS'
                                                type: list
                                                elements: str
                                            verify_claims:
                                                description:
                                                    - A list of claims which should be validated to consider the token valid.
                                                    - Applicable when type is 'REMOTE_JWKS'
                                                type: list
                                                elements: dict
                                                suboptions:
                                                    key:
                                                        description:
                                                            - Name of the claim.
                                                            - Required when type is 'REMOTE_JWKS'
                                                        type: str
                                                        required: true
                                                    values:
                                                        description:
                                                            - "The list of acceptable values for a given claim.
                                                              If this value is \\"null\\" or empty and \\"isRequired\\" set to \\"true\\", then
                                                              the presence of this claim in the JWT is validated."
                                                            - Applicable when type is 'REMOTE_JWKS'
                                                        type: list
                                                        elements: str
                                                    is_required:
                                                        description:
                                                            - "Whether the claim is required to be present in the JWT or not. If set
                                                              to \\"false\\", the claim values will be matched only if the claim is
                                                              present in the JWT."
                                                            - Applicable when type is 'REMOTE_JWKS'
                                                        type: bool
                                    keys:
                                        description:
                                            - The set of static public keys.
                                            - Applicable when type is 'STATIC_KEYS'
                                        type: list
                                        elements: dict
                                        suboptions:
                                            kty:
                                                description:
                                                    - The key type.
                                                    - Required when format is 'JSON_WEB_KEY'
                                                type: str
                                                choices:
                                                    - "RSA"
                                            use:
                                                description:
                                                    - The intended use of the public key.
                                                    - Applicable when format is 'JSON_WEB_KEY'
                                                type: str
                                                choices:
                                                    - "sig"
                                            key_ops:
                                                description:
                                                    - The operations for which this key is to be used.
                                                    - Applicable when format is 'JSON_WEB_KEY'
                                                type: list
                                                elements: str
                                                choices:
                                                    - "verify"
                                            alg:
                                                description:
                                                    - The algorithm intended for use with this key.
                                                    - Required when format is 'JSON_WEB_KEY'
                                                type: str
                                            n:
                                                description:
                                                    - The base64 url encoded modulus of the RSA public key represented
                                                      by this key.
                                                    - Required when format is 'JSON_WEB_KEY'
                                                type: str
                                            e:
                                                description:
                                                    - The base64 url encoded exponent of the RSA public key represented
                                                      by this key.
                                                    - Required when format is 'JSON_WEB_KEY'
                                                type: str
                                            kid:
                                                description:
                                                    - "A unique key ID. This key will be used to verify the signature of a
                                                      JWT with matching \\"kid\\"."
                                                type: str
                                                required: true
                                            format:
                                                description:
                                                    - The format of the public key.
                                                type: str
                                                choices:
                                                    - "JSON_WEB_KEY"
                                                    - "PEM"
                                                required: true
                                            key:
                                                description:
                                                    - The content of the PEM-encoded public key.
                                                    - Required when format is 'PEM'
                                                type: str
                            token_auth_scheme:
                                description:
                                    - "The authentication scheme that is to be used when authenticating
                                      the token. This must to be provided if \\"tokenHeader\\" is specified."
                                    - Applicable when type is one of ['TOKEN_AUTHENTICATION', 'JWT_AUTHENTICATION']
                                type: str
                            max_clock_skew_in_seconds:
                                description:
                                    - The maximum expected time difference between the system clocks
                                      of the token issuer and the API Gateway.
                                    - Applicable when type is one of ['TOKEN_AUTHENTICATION', 'JWT_AUTHENTICATION']
                                type: float
                            issuers:
                                description:
                                    - A list of parties that could have issued the token.
                                    - Required when type is 'JWT_AUTHENTICATION'
                                type: list
                                elements: str
                            audiences:
                                description:
                                    - The list of intended recipients for the token.
                                    - Required when type is 'JWT_AUTHENTICATION'
                                type: list
                                elements: str
                            verify_claims:
                                description:
                                    - A list of claims which should be validated to consider the token valid.
                                    - Applicable when type is 'JWT_AUTHENTICATION'
                                type: list
                                elements: dict
                                suboptions:
                                    key:
                                        description:
                                            - Name of the claim.
                                            - Required when type is 'JWT_AUTHENTICATION'
                                        type: str
                                        required: true
                                    values:
                                        description:
                                            - "The list of acceptable values for a given claim.
                                              If this value is \\"null\\" or empty and \\"isRequired\\" set to \\"true\\", then
                                              the presence of this claim in the JWT is validated."
                                            - Applicable when type is 'JWT_AUTHENTICATION'
                                        type: list
                                        elements: str
                                    is_required:
                                        description:
                                            - "Whether the claim is required to be present in the JWT or not. If set
                                              to \\"false\\", the claim values will be matched only if the claim is
                                              present in the JWT."
                                            - Applicable when type is 'JWT_AUTHENTICATION'
                                        type: bool
                            public_keys:
                                description:
                                    - ""
                                    - Required when type is 'JWT_AUTHENTICATION'
                                type: dict
                                suboptions:
                                    keys:
                                        description:
                                            - The set of static public keys.
                                            - Applicable when type is 'STATIC_KEYS'
                                        type: list
                                        elements: dict
                                        suboptions:
                                            kty:
                                                description:
                                                    - The key type.
                                                    - Required when format is 'JSON_WEB_KEY'
                                                type: str
                                                choices:
                                                    - "RSA"
                                            use:
                                                description:
                                                    - The intended use of the public key.
                                                    - Applicable when format is 'JSON_WEB_KEY'
                                                type: str
                                                choices:
                                                    - "sig"
                                            key_ops:
                                                description:
                                                    - The operations for which this key is to be used.
                                                    - Applicable when format is 'JSON_WEB_KEY'
                                                type: list
                                                elements: str
                                                choices:
                                                    - "verify"
                                            alg:
                                                description:
                                                    - The algorithm intended for use with this key.
                                                    - Required when format is 'JSON_WEB_KEY'
                                                type: str
                                            n:
                                                description:
                                                    - The base64 url encoded modulus of the RSA public key represented
                                                      by this key.
                                                    - Required when format is 'JSON_WEB_KEY'
                                                type: str
                                            e:
                                                description:
                                                    - The base64 url encoded exponent of the RSA public key represented
                                                      by this key.
                                                    - Required when format is 'JSON_WEB_KEY'
                                                type: str
                                            kid:
                                                description:
                                                    - "A unique key ID. This key will be used to verify the signature of a
                                                      JWT with matching \\"kid\\"."
                                                type: str
                                                required: true
                                            format:
                                                description:
                                                    - The format of the public key.
                                                type: str
                                                choices:
                                                    - "JSON_WEB_KEY"
                                                    - "PEM"
                                                required: true
                                            key:
                                                description:
                                                    - The content of the PEM-encoded public key.
                                                    - Required when format is 'PEM'
                                                type: str
                                    type:
                                        description:
                                            - Type of the public key set.
                                        type: str
                                        choices:
                                            - "STATIC_KEYS"
                                            - "REMOTE_JWKS"
                                        required: true
                                    uri:
                                        description:
                                            - The uri from which to retrieve the key. It must be accessible
                                              without authentication.
                                            - Required when type is 'REMOTE_JWKS'
                                        type: str
                                    is_ssl_verify_disabled:
                                        description:
                                            - Defines whether or not to uphold SSL verification.
                                            - Applicable when type is 'REMOTE_JWKS'
                                        type: bool
                                    max_cache_duration_in_hours:
                                        description:
                                            - The duration for which the JWKS should be cached before it is
                                              fetched again.
                                            - Applicable when type is 'REMOTE_JWKS'
                                        type: int
                            is_anonymous_access_allowed:
                                description:
                                    - "Whether an unauthenticated user may access the API. Must be \\"true\\" to enable ANONYMOUS
                                      route authorization."
                                type: bool
                            type:
                                description:
                                    - Type of the authentication policy to use.
                                type: str
                                choices:
                                    - "TOKEN_AUTHENTICATION"
                                    - "JWT_AUTHENTICATION"
                                    - "CUSTOM_AUTHENTICATION"
                                required: true
                            function_id:
                                description:
                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function
                                      resource.
                                    - Required when type is 'CUSTOM_AUTHENTICATION'
                                type: str
                            token_header:
                                description:
                                    - The name of the header containing the authentication token.
                                type: str
                            token_query_param:
                                description:
                                    - The name of the query parameter containing the authentication token.
                                type: str
                            parameters:
                                description:
                                    - "A map where key is a user defined string and value is a context expressions whose values will be sent to the custom auth
                                      function. Values should contain an expression.
                                      Example: `{\\"foo\\": \\"request.header[abc]\\"}`"
                                    - Applicable when type is 'CUSTOM_AUTHENTICATION'
                                type: dict
                            cache_key:
                                description:
                                    - "A list of keys from \\"parameters\\" attribute value whose values will be added to the cache key."
                                    - Applicable when type is 'CUSTOM_AUTHENTICATION'
                                type: list
                                elements: str
                            validation_failure_policy:
                                description:
                                    - ""
                                    - Applicable when type is one of ['TOKEN_AUTHENTICATION', 'CUSTOM_AUTHENTICATION']
                                type: dict
                                suboptions:
                                    response_code:
                                        description:
                                            - HTTP response code, can include context variables.
                                            - Applicable when type is 'MODIFY_RESPONSE'
                                        type: str
                                    response_message:
                                        description:
                                            - HTTP response message.
                                            - Applicable when type is 'MODIFY_RESPONSE'
                                        type: str
                                    response_header_transformations:
                                        description:
                                            - ""
                                            - Applicable when type is 'MODIFY_RESPONSE'
                                        type: dict
                                        suboptions:
                                            set_headers:
                                                description:
                                                    - ""
                                                    - Applicable when type is 'MODIFY_RESPONSE'
                                                type: dict
                                                suboptions:
                                                    items:
                                                        description:
                                                            - The list of headers.
                                                            - Required when type is 'MODIFY_RESPONSE'
                                                        type: list
                                                        elements: dict
                                                        required: true
                                                        suboptions:
                                                            name:
                                                                description:
                                                                    - The case-insensitive name of the header.  This name must be unique across transformation
                                                                      policies.
                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                type: str
                                                                required: true
                                                            values:
                                                                description:
                                                                    - A list of new values.  Each value can be a constant or may include one or more expressions
                                                                      enclosed within
                                                                      ${} delimiters.
                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                type: list
                                                                elements: str
                                                                required: true
                                                            if_exists:
                                                                description:
                                                                    - If a header with the same name already exists in the request, OVERWRITE will overwrite the
                                                                      value,
                                                                      APPEND will append to the existing value, or SKIP will keep the existing value.
                                                                    - Applicable when type is 'MODIFY_RESPONSE'
                                                                type: str
                                                                choices:
                                                                    - "OVERWRITE"
                                                                    - "APPEND"
                                                                    - "SKIP"
                                            rename_headers:
                                                description:
                                                    - ""
                                                    - Applicable when type is 'MODIFY_RESPONSE'
                                                type: dict
                                                suboptions:
                                                    items:
                                                        description:
                                                            - The list of headers.
                                                            - Required when type is 'MODIFY_RESPONSE'
                                                        type: list
                                                        elements: dict
                                                        required: true
                                                        suboptions:
                                                            _from:
                                                                description:
                                                                    - The original case-insensitive name of the header.  This name must be unique across
                                                                      transformation policies.
                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                type: str
                                                                required: true
                                                            to:
                                                                description:
                                                                    - The new name of the header.  This name must be unique across transformation policies.
                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                type: str
                                                                required: true
                                            filter_headers:
                                                description:
                                                    - ""
                                                    - Applicable when type is 'MODIFY_RESPONSE'
                                                type: dict
                                                suboptions:
                                                    type:
                                                        description:
                                                            - BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW
                                                              permits only the headers in the list and removes all others, so it acts as an inclusion list.
                                                            - Required when type is 'MODIFY_RESPONSE'
                                                        type: str
                                                        choices:
                                                            - "ALLOW"
                                                            - "BLOCK"
                                                        required: true
                                                    items:
                                                        description:
                                                            - The list of headers.
                                                            - Required when type is 'MODIFY_RESPONSE'
                                                        type: list
                                                        elements: dict
                                                        required: true
                                                        suboptions:
                                                            name:
                                                                description:
                                                                    - The case-insensitive name of the header.  This name must be unique across transformation
                                                                      policies.
                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                type: str
                                                                required: true
                                    type:
                                        description:
                                            - Type of the Validation failure Policy.
                                        type: str
                                        choices:
                                            - "MODIFY_RESPONSE"
                                            - "OAUTH2"
                                        required: true
                                    client_details:
                                        description:
                                            - ""
                                            - Required when type is 'OAUTH2'
                                        type: dict
                                        suboptions:
                                            client_id:
                                                description:
                                                    - Client ID for the OAuth2/OIDC app.
                                                    - Required when type is 'CUSTOM'
                                                type: str
                                            client_secret_id:
                                                description:
                                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Vault
                                                      Service secret resource.
                                                    - Required when type is 'CUSTOM'
                                                type: str
                                            client_secret_version_number:
                                                description:
                                                    - The version number of the client secret to use.
                                                    - Required when type is 'CUSTOM'
                                                type: int
                                            type:
                                                description:
                                                    - To specify where the Client App details should be taken from.
                                                type: str
                                                choices:
                                                    - "CUSTOM"
                                                    - "VALIDATION_BLOCK"
                                                required: true
                                    source_uri_details:
                                        description:
                                            - ""
                                            - Required when type is 'OAUTH2'
                                        type: dict
                                        suboptions:
                                            uri:
                                                description:
                                                    - The discovery URI for the auth server.
                                                    - Required when type is 'DISCOVERY_URI'
                                                type: str
                                            type:
                                                description:
                                                    - Type of the Uri detail.
                                                type: str
                                                choices:
                                                    - "DISCOVERY_URI"
                                                    - "VALIDATION_BLOCK"
                                                required: true
                                    scopes:
                                        description:
                                            - List of scopes.
                                            - Required when type is 'OAUTH2'
                                        type: list
                                        elements: str
                                    max_expiry_duration_in_hours:
                                        description:
                                            - The duration for which the OAuth2 success token should be cached before it is
                                              fetched again.
                                            - Applicable when type is 'OAUTH2'
                                        type: int
                                    use_cookies_for_session:
                                        description:
                                            - Defines whether or not to use cookies for session maintenance.
                                            - Applicable when type is 'OAUTH2'
                                        type: bool
                                    use_cookies_for_intermediate_steps:
                                        description:
                                            - Defines whether or not to use cookies for OAuth2 intermediate steps.
                                            - Applicable when type is 'OAUTH2'
                                        type: bool
                                    use_pkce:
                                        description:
                                            - Defines whether or not to support PKCE.
                                            - Applicable when type is 'OAUTH2'
                                        type: bool
                                    response_type:
                                        description:
                                            - Response Type.
                                            - Required when type is 'OAUTH2'
                                        type: str
                                        choices:
                                            - "CODE"
                                    fallback_redirect_path:
                                        description:
                                            - The path to be used as fallback after OAuth2.
                                            - Applicable when type is 'OAUTH2'
                                        type: str
                                    logout_path:
                                        description:
                                            - The path to be used as logout.
                                            - Applicable when type is 'OAUTH2'
                                        type: str
                    rate_limiting:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            rate_in_requests_per_second:
                                description:
                                    - The maximum number of requests per second to allow.
                                type: int
                                required: true
                            rate_key:
                                description:
                                    - The key used to group requests together.
                                type: str
                                choices:
                                    - "CLIENT_IP"
                                    - "TOTAL"
                                required: true
                    cors:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            allowed_origins:
                                description:
                                    - "The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will
                                      send the Access-Control-Allow-Origin header with the best origin match for the circumstances. '*' will match
                                      any origins, and 'null' will match queries from 'file:' origins. All other origins must be qualified with the
                                      scheme, full hostname, and port if necessary."
                                type: list
                                elements: str
                                required: true
                            allowed_methods:
                                description:
                                    - "The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the
                                      Access-Control-Allow-Methods header. '*' will allow all methods."
                                type: list
                                elements: str
                            allowed_headers:
                                description:
                                    - "The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header.
                                      '*' will allow all headers."
                                type: list
                                elements: str
                            exposed_headers:
                                description:
                                    - "The list of headers that the client will be allowed to see from the response as indicated by the
                                      Access-Control-Expose-Headers header. '*' will expose all headers."
                                type: list
                                elements: str
                            is_allow_credentials_enabled:
                                description:
                                    - Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.
                                type: bool
                            max_age_in_seconds:
                                description:
                                    - The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
                                      if greater than 0.
                                type: int
                    mutual_tls:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            is_verified_certificate_required:
                                description:
                                    - Determines whether to enable client verification when API Consumer makes connection to the gateway.
                                type: bool
                            allowed_sans:
                                description:
                                    - Allowed list of CN or SAN which will be used for verification of certificate.
                                type: list
                                elements: str
                    usage_plans:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            token_locations:
                                description:
                                    - "A list of context variables specifying where API tokens may be located in a request.
                                      Example locations:
                                        - \\"request.headers[token]\\"
                                        - \\"request.query[token]\\"
                                        - \\"request.auth[Token]\\"
                                        - \\"request.path[TOKEN]\\""
                                type: list
                                elements: str
                                required: true
                    dynamic_authentication:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            selection_source:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    type:
                                        description:
                                            - Type of the Selection source to use.
                                        type: str
                                        choices:
                                            - "SINGLE"
                                        default: "SINGLE"
                                    selector:
                                        description:
                                            - String describing the context variable used as selector.
                                        type: str
                                        required: true
                            authentication_servers:
                                description:
                                    - List of authentication servers to choose from during dynamic authentication.
                                type: list
                                elements: dict
                                required: true
                                suboptions:
                                    key:
                                        description:
                                            - ""
                                        type: dict
                                        required: true
                                        suboptions:
                                            expression:
                                                description:
                                                    - "A selection key string containing a wildcard to match with the context variable in an incoming request.
                                                      If the context variable matches the string, the request is sent to the route or authentication server
                                                      associated with the selection key. Valid wildcards are '*' (zero or more characters) and '+' (one or more
                                                      characters). The string can only contain one wildcard, and the wildcard must be at the start or the end of
                                                      the string."
                                                    - Required when type is 'WILDCARD'
                                                type: str
                                            type:
                                                description:
                                                    - Type of the selection key.
                                                type: str
                                                choices:
                                                    - "WILDCARD"
                                                    - "ANY_OF"
                                                default: "ANY_OF"
                                            is_default:
                                                description:
                                                    - Specifies whether to use the route or authentication server associated with this selection key as the
                                                      default. The default is used if the value of a context variable in an incoming request does not match any
                                                      of the other selection key values when dynamically routing and dynamically authenticating requests.
                                                type: bool
                                            name:
                                                description:
                                                    - Name assigned to the branch.
                                                type: str
                                                required: true
                                            values:
                                                description:
                                                    - The set of selection keys to match with the context variable in an incoming request. If the context
                                                      variable exactly matches one of the keys in the set, the request is sent to the route or authentication
                                                      server associated with the set.
                                                    - Applicable when type is 'ANY_OF'
                                                type: list
                                                elements: str
                                    authentication_server_detail:
                                        description:
                                            - ""
                                        type: dict
                                        required: true
                                        suboptions:
                                            validation_policy:
                                                description:
                                                    - ""
                                                    - Required when type is 'TOKEN_AUTHENTICATION'
                                                type: dict
                                                suboptions:
                                                    uri:
                                                        description:
                                                            - The uri from which to retrieve the key. It must be accessible
                                                              without authentication.
                                                            - Required when type is 'REMOTE_JWKS'
                                                        type: str
                                                    client_details:
                                                        description:
                                                            - ""
                                                            - Required when type is 'REMOTE_DISCOVERY'
                                                        type: dict
                                                        suboptions:
                                                            client_id:
                                                                description:
                                                                    - Client ID for the OAuth2/OIDC app.
                                                                    - Required when type is 'CUSTOM'
                                                                type: str
                                                            client_secret_id:
                                                                description:
                                                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                                                                      Oracle Vault Service secret resource.
                                                                    - Required when type is 'CUSTOM'
                                                                type: str
                                                            client_secret_version_number:
                                                                description:
                                                                    - The version number of the client secret to use.
                                                                    - Required when type is 'CUSTOM'
                                                                type: int
                                                            type:
                                                                description:
                                                                    - To specify where the Client App details should be taken from.
                                                                type: str
                                                                choices:
                                                                    - "CUSTOM"
                                                                    - "VALIDATION_BLOCK"
                                                                required: true
                                                    source_uri_details:
                                                        description:
                                                            - ""
                                                            - Required when type is 'REMOTE_DISCOVERY'
                                                        type: dict
                                                        suboptions:
                                                            uri:
                                                                description:
                                                                    - The discovery URI for the auth server.
                                                                    - Required when type is 'DISCOVERY_URI'
                                                                type: str
                                                            type:
                                                                description:
                                                                    - Type of the Uri detail.
                                                                type: str
                                                                choices:
                                                                    - "DISCOVERY_URI"
                                                                    - "VALIDATION_BLOCK"
                                                                required: true
                                                    is_ssl_verify_disabled:
                                                        description:
                                                            - Defines whether or not to uphold SSL verification.
                                                            - Applicable when type is one of ['REMOTE_JWKS', 'REMOTE_DISCOVERY']
                                                        type: bool
                                                    max_cache_duration_in_hours:
                                                        description:
                                                            - The duration for which the JWKS should be cached before it is
                                                              fetched again.
                                                            - Applicable when type is one of ['REMOTE_JWKS', 'REMOTE_DISCOVERY']
                                                        type: int
                                                    type:
                                                        description:
                                                            - Type of the token validation policy.
                                                        type: str
                                                        choices:
                                                            - "REMOTE_JWKS"
                                                            - "REMOTE_DISCOVERY"
                                                            - "STATIC_KEYS"
                                                        required: true
                                                    additional_validation_policy:
                                                        description:
                                                            - ""
                                                        type: dict
                                                        suboptions:
                                                            issuers:
                                                                description:
                                                                    - A list of parties that could have issued the token.
                                                                    - Applicable when type is 'REMOTE_JWKS'
                                                                type: list
                                                                elements: str
                                                            audiences:
                                                                description:
                                                                    - The list of intended recipients for the token.
                                                                    - Applicable when type is 'REMOTE_JWKS'
                                                                type: list
                                                                elements: str
                                                            verify_claims:
                                                                description:
                                                                    - A list of claims which should be validated to consider the token valid.
                                                                    - Applicable when type is 'REMOTE_JWKS'
                                                                type: list
                                                                elements: dict
                                                                suboptions:
                                                                    key:
                                                                        description:
                                                                            - Name of the claim.
                                                                            - Required when type is 'REMOTE_JWKS'
                                                                        type: str
                                                                        required: true
                                                                    values:
                                                                        description:
                                                                            - "The list of acceptable values for a given claim.
                                                                              If this value is \\"null\\" or empty and \\"isRequired\\" set to \\"true\\", then
                                                                              the presence of this claim in the JWT is validated."
                                                                            - Applicable when type is 'REMOTE_JWKS'
                                                                        type: list
                                                                        elements: str
                                                                    is_required:
                                                                        description:
                                                                            - "Whether the claim is required to be present in the JWT or not. If set
                                                                              to \\"false\\", the claim values will be matched only if the claim is
                                                                              present in the JWT."
                                                                            - Applicable when type is 'REMOTE_JWKS'
                                                                        type: bool
                                                    keys:
                                                        description:
                                                            - The set of static public keys.
                                                            - Applicable when type is 'STATIC_KEYS'
                                                        type: list
                                                        elements: dict
                                                        suboptions:
                                                            kty:
                                                                description:
                                                                    - The key type.
                                                                    - Required when format is 'JSON_WEB_KEY'
                                                                type: str
                                                                choices:
                                                                    - "RSA"
                                                            use:
                                                                description:
                                                                    - The intended use of the public key.
                                                                    - Applicable when format is 'JSON_WEB_KEY'
                                                                type: str
                                                                choices:
                                                                    - "sig"
                                                            key_ops:
                                                                description:
                                                                    - The operations for which this key is to be used.
                                                                    - Applicable when format is 'JSON_WEB_KEY'
                                                                type: list
                                                                elements: str
                                                                choices:
                                                                    - "verify"
                                                            alg:
                                                                description:
                                                                    - The algorithm intended for use with this key.
                                                                    - Required when format is 'JSON_WEB_KEY'
                                                                type: str
                                                            n:
                                                                description:
                                                                    - The base64 url encoded modulus of the RSA public key represented
                                                                      by this key.
                                                                    - Required when format is 'JSON_WEB_KEY'
                                                                type: str
                                                            e:
                                                                description:
                                                                    - The base64 url encoded exponent of the RSA public key represented
                                                                      by this key.
                                                                    - Required when format is 'JSON_WEB_KEY'
                                                                type: str
                                                            kid:
                                                                description:
                                                                    - "A unique key ID. This key will be used to verify the signature of a
                                                                      JWT with matching \\"kid\\"."
                                                                type: str
                                                                required: true
                                                            format:
                                                                description:
                                                                    - The format of the public key.
                                                                type: str
                                                                choices:
                                                                    - "JSON_WEB_KEY"
                                                                    - "PEM"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The content of the PEM-encoded public key.
                                                                    - Required when format is 'PEM'
                                                                type: str
                                            token_auth_scheme:
                                                description:
                                                    - "The authentication scheme that is to be used when authenticating
                                                      the token. This must to be provided if \\"tokenHeader\\" is specified."
                                                    - Applicable when type is one of ['TOKEN_AUTHENTICATION', 'JWT_AUTHENTICATION']
                                                type: str
                                            max_clock_skew_in_seconds:
                                                description:
                                                    - The maximum expected time difference between the system clocks
                                                      of the token issuer and the API Gateway.
                                                    - Applicable when type is one of ['TOKEN_AUTHENTICATION', 'JWT_AUTHENTICATION']
                                                type: float
                                            issuers:
                                                description:
                                                    - A list of parties that could have issued the token.
                                                    - Required when type is 'JWT_AUTHENTICATION'
                                                type: list
                                                elements: str
                                            audiences:
                                                description:
                                                    - The list of intended recipients for the token.
                                                    - Required when type is 'JWT_AUTHENTICATION'
                                                type: list
                                                elements: str
                                            verify_claims:
                                                description:
                                                    - A list of claims which should be validated to consider the token valid.
                                                    - Applicable when type is 'JWT_AUTHENTICATION'
                                                type: list
                                                elements: dict
                                                suboptions:
                                                    key:
                                                        description:
                                                            - Name of the claim.
                                                            - Required when type is 'JWT_AUTHENTICATION'
                                                        type: str
                                                        required: true
                                                    values:
                                                        description:
                                                            - "The list of acceptable values for a given claim.
                                                              If this value is \\"null\\" or empty and \\"isRequired\\" set to \\"true\\", then
                                                              the presence of this claim in the JWT is validated."
                                                            - Applicable when type is 'JWT_AUTHENTICATION'
                                                        type: list
                                                        elements: str
                                                    is_required:
                                                        description:
                                                            - "Whether the claim is required to be present in the JWT or not. If set
                                                              to \\"false\\", the claim values will be matched only if the claim is
                                                              present in the JWT."
                                                            - Applicable when type is 'JWT_AUTHENTICATION'
                                                        type: bool
                                            public_keys:
                                                description:
                                                    - ""
                                                    - Required when type is 'JWT_AUTHENTICATION'
                                                type: dict
                                                suboptions:
                                                    keys:
                                                        description:
                                                            - The set of static public keys.
                                                            - Applicable when type is 'STATIC_KEYS'
                                                        type: list
                                                        elements: dict
                                                        suboptions:
                                                            kty:
                                                                description:
                                                                    - The key type.
                                                                    - Required when format is 'JSON_WEB_KEY'
                                                                type: str
                                                                choices:
                                                                    - "RSA"
                                                            use:
                                                                description:
                                                                    - The intended use of the public key.
                                                                    - Applicable when format is 'JSON_WEB_KEY'
                                                                type: str
                                                                choices:
                                                                    - "sig"
                                                            key_ops:
                                                                description:
                                                                    - The operations for which this key is to be used.
                                                                    - Applicable when format is 'JSON_WEB_KEY'
                                                                type: list
                                                                elements: str
                                                                choices:
                                                                    - "verify"
                                                            alg:
                                                                description:
                                                                    - The algorithm intended for use with this key.
                                                                    - Required when format is 'JSON_WEB_KEY'
                                                                type: str
                                                            n:
                                                                description:
                                                                    - The base64 url encoded modulus of the RSA public key represented
                                                                      by this key.
                                                                    - Required when format is 'JSON_WEB_KEY'
                                                                type: str
                                                            e:
                                                                description:
                                                                    - The base64 url encoded exponent of the RSA public key represented
                                                                      by this key.
                                                                    - Required when format is 'JSON_WEB_KEY'
                                                                type: str
                                                            kid:
                                                                description:
                                                                    - "A unique key ID. This key will be used to verify the signature of a
                                                                      JWT with matching \\"kid\\"."
                                                                type: str
                                                                required: true
                                                            format:
                                                                description:
                                                                    - The format of the public key.
                                                                type: str
                                                                choices:
                                                                    - "JSON_WEB_KEY"
                                                                    - "PEM"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The content of the PEM-encoded public key.
                                                                    - Required when format is 'PEM'
                                                                type: str
                                                    type:
                                                        description:
                                                            - Type of the public key set.
                                                        type: str
                                                        choices:
                                                            - "STATIC_KEYS"
                                                            - "REMOTE_JWKS"
                                                        required: true
                                                    uri:
                                                        description:
                                                            - The uri from which to retrieve the key. It must be accessible
                                                              without authentication.
                                                            - Required when type is 'REMOTE_JWKS'
                                                        type: str
                                                    is_ssl_verify_disabled:
                                                        description:
                                                            - Defines whether or not to uphold SSL verification.
                                                            - Applicable when type is 'REMOTE_JWKS'
                                                        type: bool
                                                    max_cache_duration_in_hours:
                                                        description:
                                                            - The duration for which the JWKS should be cached before it is
                                                              fetched again.
                                                            - Applicable when type is 'REMOTE_JWKS'
                                                        type: int
                                            is_anonymous_access_allowed:
                                                description:
                                                    - "Whether an unauthenticated user may access the API. Must be \\"true\\" to enable ANONYMOUS
                                                      route authorization."
                                                type: bool
                                            type:
                                                description:
                                                    - Type of the authentication policy to use.
                                                type: str
                                                choices:
                                                    - "TOKEN_AUTHENTICATION"
                                                    - "JWT_AUTHENTICATION"
                                                    - "CUSTOM_AUTHENTICATION"
                                                required: true
                                            function_id:
                                                description:
                                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions
                                                      function resource.
                                                    - Required when type is 'CUSTOM_AUTHENTICATION'
                                                type: str
                                            token_header:
                                                description:
                                                    - The name of the header containing the authentication token.
                                                type: str
                                            token_query_param:
                                                description:
                                                    - The name of the query parameter containing the authentication token.
                                                type: str
                                            parameters:
                                                description:
                                                    - "A map where key is a user defined string and value is a context expressions whose values will be sent to
                                                      the custom auth function. Values should contain an expression.
                                                      Example: `{\\"foo\\": \\"request.header[abc]\\"}`"
                                                    - Applicable when type is 'CUSTOM_AUTHENTICATION'
                                                type: dict
                                            cache_key:
                                                description:
                                                    - "A list of keys from \\"parameters\\" attribute value whose values will be added to the cache key."
                                                    - Applicable when type is 'CUSTOM_AUTHENTICATION'
                                                type: list
                                                elements: str
                                            validation_failure_policy:
                                                description:
                                                    - ""
                                                    - Applicable when type is one of ['TOKEN_AUTHENTICATION', 'CUSTOM_AUTHENTICATION']
                                                type: dict
                                                suboptions:
                                                    response_code:
                                                        description:
                                                            - HTTP response code, can include context variables.
                                                            - Applicable when type is 'MODIFY_RESPONSE'
                                                        type: str
                                                    response_message:
                                                        description:
                                                            - HTTP response message.
                                                            - Applicable when type is 'MODIFY_RESPONSE'
                                                        type: str
                                                    response_header_transformations:
                                                        description:
                                                            - ""
                                                            - Applicable when type is 'MODIFY_RESPONSE'
                                                        type: dict
                                                        suboptions:
                                                            set_headers:
                                                                description:
                                                                    - ""
                                                                    - Applicable when type is 'MODIFY_RESPONSE'
                                                                type: dict
                                                                suboptions:
                                                                    items:
                                                                        description:
                                                                            - The list of headers.
                                                                            - Required when type is 'MODIFY_RESPONSE'
                                                                        type: list
                                                                        elements: dict
                                                                        required: true
                                                                        suboptions:
                                                                            name:
                                                                                description:
                                                                                    - The case-insensitive name of the header.  This name must be unique across
                                                                                      transformation policies.
                                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                                type: str
                                                                                required: true
                                                                            values:
                                                                                description:
                                                                                    - A list of new values.  Each value can be a constant or may include one or
                                                                                      more expressions enclosed within
                                                                                      ${} delimiters.
                                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                                type: list
                                                                                elements: str
                                                                                required: true
                                                                            if_exists:
                                                                                description:
                                                                                    - If a header with the same name already exists in the request, OVERWRITE
                                                                                      will overwrite the value,
                                                                                      APPEND will append to the existing value, or SKIP will keep the existing
                                                                                      value.
                                                                                    - Applicable when type is 'MODIFY_RESPONSE'
                                                                                type: str
                                                                                choices:
                                                                                    - "OVERWRITE"
                                                                                    - "APPEND"
                                                                                    - "SKIP"
                                                            rename_headers:
                                                                description:
                                                                    - ""
                                                                    - Applicable when type is 'MODIFY_RESPONSE'
                                                                type: dict
                                                                suboptions:
                                                                    items:
                                                                        description:
                                                                            - The list of headers.
                                                                            - Required when type is 'MODIFY_RESPONSE'
                                                                        type: list
                                                                        elements: dict
                                                                        required: true
                                                                        suboptions:
                                                                            _from:
                                                                                description:
                                                                                    - The original case-insensitive name of the header.  This name must be
                                                                                      unique across transformation policies.
                                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                                type: str
                                                                                required: true
                                                                            to:
                                                                                description:
                                                                                    - The new name of the header.  This name must be unique across
                                                                                      transformation policies.
                                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                                type: str
                                                                                required: true
                                                            filter_headers:
                                                                description:
                                                                    - ""
                                                                    - Applicable when type is 'MODIFY_RESPONSE'
                                                                type: dict
                                                                suboptions:
                                                                    type:
                                                                        description:
                                                                            - BLOCK drops any headers that are in the list of items, so it acts as an exclusion
                                                                              list.  ALLOW
                                                                              permits only the headers in the list and removes all others, so it acts as an
                                                                              inclusion list.
                                                                            - Required when type is 'MODIFY_RESPONSE'
                                                                        type: str
                                                                        choices:
                                                                            - "ALLOW"
                                                                            - "BLOCK"
                                                                        required: true
                                                                    items:
                                                                        description:
                                                                            - The list of headers.
                                                                            - Required when type is 'MODIFY_RESPONSE'
                                                                        type: list
                                                                        elements: dict
                                                                        required: true
                                                                        suboptions:
                                                                            name:
                                                                                description:
                                                                                    - The case-insensitive name of the header.  This name must be unique across
                                                                                      transformation policies.
                                                                                    - Required when type is 'MODIFY_RESPONSE'
                                                                                type: str
                                                                                required: true
                                                    type:
                                                        description:
                                                            - Type of the Validation failure Policy.
                                                        type: str
                                                        choices:
                                                            - "MODIFY_RESPONSE"
                                                            - "OAUTH2"
                                                        required: true
                                                    client_details:
                                                        description:
                                                            - ""
                                                            - Required when type is 'OAUTH2'
                                                        type: dict
                                                        suboptions:
                                                            client_id:
                                                                description:
                                                                    - Client ID for the OAuth2/OIDC app.
                                                                    - Required when type is 'CUSTOM'
                                                                type: str
                                                            client_secret_id:
                                                                description:
                                                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the
                                                                      Oracle Vault Service secret resource.
                                                                    - Required when type is 'CUSTOM'
                                                                type: str
                                                            client_secret_version_number:
                                                                description:
                                                                    - The version number of the client secret to use.
                                                                    - Required when type is 'CUSTOM'
                                                                type: int
                                                            type:
                                                                description:
                                                                    - To specify where the Client App details should be taken from.
                                                                type: str
                                                                choices:
                                                                    - "CUSTOM"
                                                                    - "VALIDATION_BLOCK"
                                                                required: true
                                                    source_uri_details:
                                                        description:
                                                            - ""
                                                            - Required when type is 'OAUTH2'
                                                        type: dict
                                                        suboptions:
                                                            uri:
                                                                description:
                                                                    - The discovery URI for the auth server.
                                                                    - Required when type is 'DISCOVERY_URI'
                                                                type: str
                                                            type:
                                                                description:
                                                                    - Type of the Uri detail.
                                                                type: str
                                                                choices:
                                                                    - "DISCOVERY_URI"
                                                                    - "VALIDATION_BLOCK"
                                                                required: true
                                                    scopes:
                                                        description:
                                                            - List of scopes.
                                                            - Required when type is 'OAUTH2'
                                                        type: list
                                                        elements: str
                                                    max_expiry_duration_in_hours:
                                                        description:
                                                            - The duration for which the OAuth2 success token should be cached before it is
                                                              fetched again.
                                                            - Applicable when type is 'OAUTH2'
                                                        type: int
                                                    use_cookies_for_session:
                                                        description:
                                                            - Defines whether or not to use cookies for session maintenance.
                                                            - Applicable when type is 'OAUTH2'
                                                        type: bool
                                                    use_cookies_for_intermediate_steps:
                                                        description:
                                                            - Defines whether or not to use cookies for OAuth2 intermediate steps.
                                                            - Applicable when type is 'OAUTH2'
                                                        type: bool
                                                    use_pkce:
                                                        description:
                                                            - Defines whether or not to support PKCE.
                                                            - Applicable when type is 'OAUTH2'
                                                        type: bool
                                                    response_type:
                                                        description:
                                                            - Response Type.
                                                            - Required when type is 'OAUTH2'
                                                        type: str
                                                        choices:
                                                            - "CODE"
                                                    fallback_redirect_path:
                                                        description:
                                                            - The path to be used as fallback after OAuth2.
                                                            - Applicable when type is 'OAUTH2'
                                                        type: str
                                                    logout_path:
                                                        description:
                                                            - The path to be used as logout.
                                                            - Applicable when type is 'OAUTH2'
                                                        type: str
            logging_policies:
                description:
                    - ""
                type: dict
                suboptions:
                    access_log:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            is_enabled:
                                description:
                                    - Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.
                                    - Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs
                                      for an API Deployment. If there is an active log object for the API Deployment and its
                                      category is set to 'access' in OCI Logging service, the logs will not be uploaded to the
                                      legacy OCI Object Storage log archival bucket.
                                    - Please note that the functionality to push to the legacy OCI Object Storage log
                                      archival bucket has been deprecated and will be removed in the future.
                                type: bool
                    execution_log:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            is_enabled:
                                description:
                                    - Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.
                                    - Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs
                                      for an API Deployment. If there is an active log object for the API Deployment and its
                                      category is set to 'execution' in OCI Logging service, the logs will not be uploaded to the legacy
                                      OCI Object Storage log archival bucket.
                                    - Please note that the functionality to push to the legacy OCI Object Storage log
                                      archival bucket has been deprecated and will be removed in the future.
                                type: bool
                            log_level:
                                description:
                                    - Specifies the log level used to control logging output of execution logs.
                                      Enabling logging at a given level also enables logging at all higher levels.
                                type: str
                                choices:
                                    - "INFO"
                                    - "WARN"
                                    - "ERROR"
            routes:
                description:
                    - A list of routes that this API exposes.
                type: list
                elements: dict
                suboptions:
                    path:
                        description:
                            - A URL path pattern that must be matched on this route. The path pattern may contain a subset of RFC 6570 identifiers
                              to allow wildcard and parameterized matching.
                        type: str
                        required: true
                    methods:
                        description:
                            - A list of allowed methods on this route.
                        type: list
                        elements: str
                        choices:
                            - "ANY"
                            - "HEAD"
                            - "GET"
                            - "POST"
                            - "PUT"
                            - "PATCH"
                            - "DELETE"
                            - "OPTIONS"
                    request_policies:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            authorization:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    allowed_scope:
                                        description:
                                            - A user whose scope includes any of these access ranges is allowed on
                                              this route. Access ranges are case-sensitive.
                                            - Required when type is 'ANY_OF'
                                        type: list
                                        elements: str
                                    type:
                                        description:
                                            - "Indicates how authorization should be applied. For a type of ANY_OF, an \\"allowedScope\\"
                                              property must also be specified. Otherwise, only a type is required. For a type of ANONYMOUS, an
                                              authenticated API must have the \\"isAnonymousAccessAllowed\\" property set to \\"true\\" in the authentication
                                              policy."
                                        type: str
                                        choices:
                                            - "ANY_OF"
                                            - "ANONYMOUS"
                                            - "AUTHENTICATION_ONLY"
                                        default: "AUTHENTICATION_ONLY"
                            cors:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    allowed_origins:
                                        description:
                                            - "The list of allowed origins that the CORS handler will use to respond to CORS requests. The gateway will
                                              send the Access-Control-Allow-Origin header with the best origin match for the circumstances. '*' will match
                                              any origins, and 'null' will match queries from 'file:' origins. All other origins must be qualified with the
                                              scheme, full hostname, and port if necessary."
                                        type: list
                                        elements: str
                                        required: true
                                    allowed_methods:
                                        description:
                                            - "The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the
                                              Access-Control-Allow-Methods header. '*' will allow all methods."
                                        type: list
                                        elements: str
                                    allowed_headers:
                                        description:
                                            - "The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header.
                                              '*' will allow all headers."
                                        type: list
                                        elements: str
                                    exposed_headers:
                                        description:
                                            - "The list of headers that the client will be allowed to see from the response as indicated by the
                                              Access-Control-Expose-Headers header. '*' will expose all headers."
                                        type: list
                                        elements: str
                                    is_allow_credentials_enabled:
                                        description:
                                            - Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.
                                        type: bool
                                    max_age_in_seconds:
                                        description:
                                            - The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
                                              if greater than 0.
                                        type: int
                            query_parameter_validations:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    parameters:
                                        description:
                                            - ""
                                        type: list
                                        elements: dict
                                        suboptions:
                                            required:
                                                description:
                                                    - Determines if the parameter is required in the request.
                                                type: bool
                                            name:
                                                description:
                                                    - Parameter name.
                                                type: str
                                                required: true
                                    validation_mode:
                                        description:
                                            - Validation behavior mode.
                                            - In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
                                              and not sent to the backend.
                                            - In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
                                              will follow the normal path.
                                            - "`DISABLED` type turns the validation off."
                                        type: str
                                        choices:
                                            - "ENFORCING"
                                            - "PERMISSIVE"
                                            - "DISABLED"
                            header_validations:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    headers:
                                        description:
                                            - ""
                                        type: list
                                        elements: dict
                                        suboptions:
                                            required:
                                                description:
                                                    - Determines if the header is required in the request.
                                                type: bool
                                            name:
                                                description:
                                                    - Parameter name.
                                                type: str
                                                required: true
                                    validation_mode:
                                        description:
                                            - Validation behavior mode.
                                            - In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
                                              and not sent to the backend.
                                            - In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
                                              will follow the normal path.
                                            - "`DISABLED` type turns the validation off."
                                        type: str
                                        choices:
                                            - "ENFORCING"
                                            - "PERMISSIVE"
                                            - "DISABLED"
                            body_validation:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    required:
                                        description:
                                            - Determines if the request body is required in the request.
                                        type: bool
                                    content:
                                        description:
                                            - The content of the request body. The key is a L(media type range,https://tools.ietf.org/html/rfc7231#appendix-D)
                                              subset restricted to the following schema
                                            - "   key ::= (
                                                        / (  \\"*\\" \\"/\\" \\"*\\" )
                                                        / ( type \\"/\\" \\"*\\" )
                                                        / ( type \\"/\\" subtype )
                                                        )"
                                            - "For requests that match multiple keys, only the most specific key is applicable.
                                              e.g. `text/plain` overrides `text/*`"
                                        type: dict
                                        required: true
                                        suboptions:
                                            validation_type:
                                                description:
                                                    - Validation type defines the content validation method.
                                                    - Make the validation to first parse the body as the respective format.
                                                type: str
                                                choices:
                                                    - "NONE"
                                                default: "NONE"
                                    validation_mode:
                                        description:
                                            - Validation behavior mode.
                                            - In `ENFORCING` mode, upon a validation failure, the request will be rejected with a 4xx response
                                              and not sent to the backend.
                                            - In `PERMISSIVE` mode, the result of the validation will be exposed as metrics while the request
                                              will follow the normal path.
                                            - "`DISABLED` type turns the validation off."
                                        type: str
                                        choices:
                                            - "ENFORCING"
                                            - "PERMISSIVE"
                                            - "DISABLED"
                            header_transformations:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    set_headers:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            items:
                                                description:
                                                    - The list of headers.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    name:
                                                        description:
                                                            - The case-insensitive name of the header.  This name must be unique across transformation policies.
                                                        type: str
                                                        required: true
                                                    values:
                                                        description:
                                                            - A list of new values.  Each value can be a constant or may include one or more expressions
                                                              enclosed within
                                                              ${} delimiters.
                                                        type: list
                                                        elements: str
                                                        required: true
                                                    if_exists:
                                                        description:
                                                            - If a header with the same name already exists in the request, OVERWRITE will overwrite the value,
                                                              APPEND will append to the existing value, or SKIP will keep the existing value.
                                                        type: str
                                                        choices:
                                                            - "OVERWRITE"
                                                            - "APPEND"
                                                            - "SKIP"
                                    rename_headers:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            items:
                                                description:
                                                    - The list of headers.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    _from:
                                                        description:
                                                            - The original case-insensitive name of the header.  This name must be unique across transformation
                                                              policies.
                                                        type: str
                                                        required: true
                                                    to:
                                                        description:
                                                            - The new name of the header.  This name must be unique across transformation policies.
                                                        type: str
                                                        required: true
                                    filter_headers:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            type:
                                                description:
                                                    - BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW
                                                      permits only the headers in the list and removes all others, so it acts as an inclusion list.
                                                type: str
                                                choices:
                                                    - "ALLOW"
                                                    - "BLOCK"
                                                required: true
                                            items:
                                                description:
                                                    - The list of headers.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    name:
                                                        description:
                                                            - The case-insensitive name of the header.  This name must be unique across transformation policies.
                                                        type: str
                                                        required: true
                            query_parameter_transformations:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    set_query_parameters:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            items:
                                                description:
                                                    - The list of query parameters.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    name:
                                                        description:
                                                            - The case-sensitive name of the query parameter.  This name must be unique across transformation
                                                              policies.
                                                        type: str
                                                        required: true
                                                    values:
                                                        description:
                                                            - A list of new values.  Each value can be a constant or may include one or more expressions
                                                              enclosed within
                                                              ${} delimiters.
                                                        type: list
                                                        elements: str
                                                        required: true
                                                    if_exists:
                                                        description:
                                                            - If a query parameter with the same name already exists in the request, OVERWRITE will overwrite
                                                              the value,
                                                              APPEND will append to the existing value, or SKIP will keep the existing value.
                                                        type: str
                                                        choices:
                                                            - "OVERWRITE"
                                                            - "APPEND"
                                                            - "SKIP"
                                    rename_query_parameters:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            items:
                                                description:
                                                    - The list of query parameters.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    _from:
                                                        description:
                                                            - The original case-sensitive name of the query parameter.  This name must be unique across
                                                              transformation
                                                              policies.
                                                        type: str
                                                        required: true
                                                    to:
                                                        description:
                                                            - The new name of the query parameter.  This name must be unique across transformation policies.
                                                        type: str
                                                        required: true
                                    filter_query_parameters:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            type:
                                                description:
                                                    - BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list.  ALLOW
                                                      permits only the parameters in the list and removes all others, so it acts as an inclusion list.
                                                type: str
                                                choices:
                                                    - "ALLOW"
                                                    - "BLOCK"
                                                required: true
                                            items:
                                                description:
                                                    - The list of query parameters.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    name:
                                                        description:
                                                            - The case-sensitive name of the query parameter.
                                                        type: str
                                                        required: true
                            response_cache_lookup:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    type:
                                        description:
                                            - Type of the Response Cache Store Policy.
                                        type: str
                                        choices:
                                            - "SIMPLE_LOOKUP_POLICY"
                                        required: true
                                    is_enabled:
                                        description:
                                            - Whether this policy is currently enabled.
                                        type: bool
                                    is_private_caching_enabled:
                                        description:
                                            - Set true to allow caching responses where the request has an Authorization header. Ensure you have configured your
                                              cache key additions to get the level of isolation across authenticated requests that you require.
                                            - When false, any request with an Authorization header will not be stored in the Response Cache.
                                            - If using the CustomAuthenticationPolicy then the tokenHeader/tokenQueryParam are also subject to this check.
                                        type: bool
                                    cache_key_additions:
                                        description:
                                            - A list of context expressions whose values will be added to the base cache key. Values should contain an
                                              expression enclosed within
                                              ${} delimiters. Only the request context is available.
                                        type: list
                                        elements: str
                    response_policies:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            header_transformations:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    set_headers:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            items:
                                                description:
                                                    - The list of headers.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    name:
                                                        description:
                                                            - The case-insensitive name of the header.  This name must be unique across transformation policies.
                                                        type: str
                                                        required: true
                                                    values:
                                                        description:
                                                            - A list of new values.  Each value can be a constant or may include one or more expressions
                                                              enclosed within
                                                              ${} delimiters.
                                                        type: list
                                                        elements: str
                                                        required: true
                                                    if_exists:
                                                        description:
                                                            - If a header with the same name already exists in the request, OVERWRITE will overwrite the value,
                                                              APPEND will append to the existing value, or SKIP will keep the existing value.
                                                        type: str
                                                        choices:
                                                            - "OVERWRITE"
                                                            - "APPEND"
                                                            - "SKIP"
                                    rename_headers:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            items:
                                                description:
                                                    - The list of headers.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    _from:
                                                        description:
                                                            - The original case-insensitive name of the header.  This name must be unique across transformation
                                                              policies.
                                                        type: str
                                                        required: true
                                                    to:
                                                        description:
                                                            - The new name of the header.  This name must be unique across transformation policies.
                                                        type: str
                                                        required: true
                                    filter_headers:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            type:
                                                description:
                                                    - BLOCK drops any headers that are in the list of items, so it acts as an exclusion list.  ALLOW
                                                      permits only the headers in the list and removes all others, so it acts as an inclusion list.
                                                type: str
                                                choices:
                                                    - "ALLOW"
                                                    - "BLOCK"
                                                required: true
                                            items:
                                                description:
                                                    - The list of headers.
                                                type: list
                                                elements: dict
                                                required: true
                                                suboptions:
                                                    name:
                                                        description:
                                                            - The case-insensitive name of the header.  This name must be unique across transformation policies.
                                                        type: str
                                                        required: true
                            response_cache_store:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    type:
                                        description:
                                            - Type of the Response Cache Store Policy.
                                        type: str
                                        choices:
                                            - "FIXED_TTL_STORE_POLICY"
                                        required: true
                                    time_to_live_in_seconds:
                                        description:
                                            - Sets the number of seconds for a response from a backend being stored in the Response Cache before it expires.
                                        type: int
                                        required: true
                    logging_policies:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            access_log:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    is_enabled:
                                        description:
                                            - Enables pushing of access logs to the legacy OCI Object Storage log archival bucket.
                                            - Oracle recommends using the OCI Logging service to enable, retrieve, and query access logs
                                              for an API Deployment. If there is an active log object for the API Deployment and its
                                              category is set to 'access' in OCI Logging service, the logs will not be uploaded to the
                                              legacy OCI Object Storage log archival bucket.
                                            - Please note that the functionality to push to the legacy OCI Object Storage log
                                              archival bucket has been deprecated and will be removed in the future.
                                        type: bool
                            execution_log:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    is_enabled:
                                        description:
                                            - Enables pushing of execution logs to the legacy OCI Object Storage log archival bucket.
                                            - Oracle recommends using the OCI Logging service to enable, retrieve, and query execution logs
                                              for an API Deployment. If there is an active log object for the API Deployment and its
                                              category is set to 'execution' in OCI Logging service, the logs will not be uploaded to the legacy
                                              OCI Object Storage log archival bucket.
                                            - Please note that the functionality to push to the legacy OCI Object Storage log
                                              archival bucket has been deprecated and will be removed in the future.
                                        type: bool
                                    log_level:
                                        description:
                                            - Specifies the log level used to control logging output of execution logs.
                                              Enabling logging at a given level also enables logging at all higher levels.
                                        type: str
                                        choices:
                                            - "INFO"
                                            - "WARN"
                                            - "ERROR"
                    backend:
                        description:
                            - ""
                        type: dict
                        required: true
                        suboptions:
                            allowed_post_logout_uris:
                                description:
                                    - ""
                                    - Applicable when type is 'OAUTH2_LOGOUT_BACKEND'
                                type: list
                                elements: str
                            post_logout_state:
                                description:
                                    - Defines a state that should be shared on redirecting to postLogout URL.
                                    - Applicable when type is 'OAUTH2_LOGOUT_BACKEND'
                                type: str
                            url:
                                description:
                                    - ""
                                    - Required when type is 'HTTP_BACKEND'
                                type: str
                            connect_timeout_in_seconds:
                                description:
                                    - Defines a timeout for establishing a connection with a proxied server.
                                    - Applicable when type is 'HTTP_BACKEND'
                                type: float
                            read_timeout_in_seconds:
                                description:
                                    - Defines a timeout for reading a response from the proxied server.
                                    - Applicable when type is 'HTTP_BACKEND'
                                type: float
                            send_timeout_in_seconds:
                                description:
                                    - Defines a timeout for transmitting a request to the proxied server.
                                    - Applicable when type is 'HTTP_BACKEND'
                                type: float
                            is_ssl_verify_disabled:
                                description:
                                    - Defines whether or not to uphold SSL verification.
                                    - Applicable when type is 'HTTP_BACKEND'
                                type: bool
                            function_id:
                                description:
                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function
                                      resource.
                                    - Required when type is 'ORACLE_FUNCTIONS_BACKEND'
                                type: str
                            body:
                                description:
                                    - The body of the stock response from the mock backend.
                                    - Applicable when type is 'STOCK_RESPONSE_BACKEND'
                                type: str
                            status:
                                description:
                                    - The status code of the stock response from the mock backend.
                                    - Required when type is 'STOCK_RESPONSE_BACKEND'
                                type: int
                            headers:
                                description:
                                    - The headers of the stock response from the mock backend.
                                    - Applicable when type is 'STOCK_RESPONSE_BACKEND'
                                type: list
                                elements: dict
                                suboptions:
                                    name:
                                        description:
                                            - Name of the header.
                                            - Applicable when type is 'STOCK_RESPONSE_BACKEND'
                                        type: str
                                    value:
                                        description:
                                            - Value of the header.
                                            - Applicable when type is 'STOCK_RESPONSE_BACKEND'
                                        type: str
                            type:
                                description:
                                    - Type of the API backend.
                                type: str
                                choices:
                                    - "OAUTH2_LOGOUT_BACKEND"
                                    - "HTTP_BACKEND"
                                    - "ORACLE_FUNCTIONS_BACKEND"
                                    - "STOCK_RESPONSE_BACKEND"
                                    - "DYNAMIC_ROUTING_BACKEND"
                                required: true
                            selection_source:
                                description:
                                    - ""
                                    - Required when type is 'DYNAMIC_ROUTING_BACKEND'
                                type: dict
                                suboptions:
                                    type:
                                        description:
                                            - Type of the Selection source to use.
                                        type: str
                                        choices:
                                            - "SINGLE"
                                        default: "SINGLE"
                                    selector:
                                        description:
                                            - String describing the context variable used as selector.
                                        type: str
                                        required: true
                            routing_backends:
                                description:
                                    - List of backends to chose from for Dynamic Routing.
                                    - Required when type is 'DYNAMIC_ROUTING_BACKEND'
                                type: list
                                elements: dict
                                suboptions:
                                    key:
                                        description:
                                            - ""
                                            - Required when type is 'DYNAMIC_ROUTING_BACKEND'
                                        type: dict
                                        required: true
                                        suboptions:
                                            expression:
                                                description:
                                                    - "A selection key string containing a wildcard to match with the context variable in an incoming request.
                                                      If the context variable matches the string, the request is sent to the route or authentication server
                                                      associated with the selection key. Valid wildcards are '*' (zero or more characters) and '+' (one or more
                                                      characters). The string can only contain one wildcard, and the wildcard must be at the start or the end of
                                                      the string."
                                                    - Required when type is 'WILDCARD'
                                                type: str
                                            type:
                                                description:
                                                    - Type of the selection key.
                                                type: str
                                                choices:
                                                    - "WILDCARD"
                                                    - "ANY_OF"
                                                default: "ANY_OF"
                                            is_default:
                                                description:
                                                    - Specifies whether to use the route or authentication server associated with this selection key as the
                                                      default. The default is used if the value of a context variable in an incoming request does not match any
                                                      of the other selection key values when dynamically routing and dynamically authenticating requests.
                                                type: bool
                                            name:
                                                description:
                                                    - Name assigned to the branch.
                                                type: str
                                                required: true
                                            values:
                                                description:
                                                    - The set of selection keys to match with the context variable in an incoming request. If the context
                                                      variable exactly matches one of the keys in the set, the request is sent to the route or authentication
                                                      server associated with the set.
                                                    - Applicable when type is 'ANY_OF'
                                                type: list
                                                elements: str
                                    backend:
                                        description:
                                            - ""
                                            - Required when type is 'DYNAMIC_ROUTING_BACKEND'
                                        type: dict
                                        required: true
                                        suboptions:
                                            type:
                                                description:
                                                    - Type of the API backend.
                                                type: str
                                                choices:
                                                    - "ORACLE_FUNCTIONS_BACKEND"
                                                    - "HTTP_BACKEND"
                                                    - "STOCK_RESPONSE_BACKEND"
                                                    - "DYNAMIC_ROUTING_BACKEND"
                                                    - "OAUTH2_LOGOUT_BACKEND"
                                                required: true
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair
              with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    deployment_id:
        description:
            - The ocid of the deployment.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Deployment.
            - Use I(state=present) to create or update a Deployment.
            - Use I(state=absent) to delete a Deployment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deployment
  oci_apigateway_deployment:
    # required
    gateway_id: "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    path_prefix: path_prefix_example
    specification:
      # optional
      request_policies:
        # optional
        authentication:
          # required
          validation_policy:
            # required
            uri: uri_example
            type: REMOTE_JWKS

            # optional
            is_ssl_verify_disabled: true
            max_cache_duration_in_hours: 56
            additional_validation_policy:
              # optional
              issuers: [ "issuers_example" ]
              audiences: [ "audiences_example" ]
              verify_claims:
              - # required
                key: key_example

                # optional
                values: [ "values_example" ]
                is_required: true
          type: TOKEN_AUTHENTICATION

                # optional
          token_auth_scheme: token_auth_scheme_example
          max_clock_skew_in_seconds: 3.4
          is_anonymous_access_allowed: true
          token_header: token_header_example
          token_query_param: token_query_param_example
          validation_failure_policy:
            # required
            type: MODIFY_RESPONSE

            # optional
            response_code: response_code_example
            response_message: response_message_example
            response_header_transformations:
              # optional
              set_headers:
                # required
                items:
                - # required
                  name: name_example
                  values: [ "values_example" ]

                  # optional
                  if_exists: OVERWRITE
              rename_headers:
                # required
                items:
                - # required
                  _from: _from_example
                  to: to_example
              filter_headers:
                # required
                type: ALLOW
                items:
                - # required
                  name: name_example
        rate_limiting:
          # required
          rate_in_requests_per_second: 56
          rate_key: CLIENT_IP
        cors:
          # required
          allowed_origins: [ "allowed_origins_example" ]

          # optional
          allowed_methods: [ "allowed_methods_example" ]
          allowed_headers: [ "allowed_headers_example" ]
          exposed_headers: [ "exposed_headers_example" ]
          is_allow_credentials_enabled: true
          max_age_in_seconds: 56
        mutual_tls:
          # optional
          is_verified_certificate_required: true
          allowed_sans: [ "allowed_sans_example" ]
        usage_plans:
          # required
          token_locations: [ "token_locations_example" ]
        dynamic_authentication:
          # required
          selection_source:
            # required
            selector: selector_example

            # optional
            type: SINGLE
          authentication_servers:
          - # required
            key:
              # required
              expression: expression_example
              type: WILDCARD
              name: name_example

              # optional
              is_default: true
            authentication_server_detail:
              # required
              validation_policy:
                # required
                uri: uri_example
                type: REMOTE_JWKS

                # optional
                is_ssl_verify_disabled: true
                max_cache_duration_in_hours: 56
                additional_validation_policy:
                  # optional
                  issuers: [ "issuers_example" ]
                  audiences: [ "audiences_example" ]
                  verify_claims:
                  - # required
                    key: key_example

                    # optional
                    values: [ "values_example" ]
                    is_required: true
              type: TOKEN_AUTHENTICATION

                    # optional
              token_auth_scheme: token_auth_scheme_example
              max_clock_skew_in_seconds: 3.4
              is_anonymous_access_allowed: true
              token_header: token_header_example
              token_query_param: token_query_param_example
              validation_failure_policy:
                # required
                type: MODIFY_RESPONSE

                # optional
                response_code: response_code_example
                response_message: response_message_example
                response_header_transformations:
                  # optional
                  set_headers:
                    # required
                    items:
                    - # required
                      name: name_example
                      values: [ "values_example" ]

                      # optional
                      if_exists: OVERWRITE
                  rename_headers:
                    # required
                    items:
                    - # required
                      _from: _from_example
                      to: to_example
                  filter_headers:
                    # required
                    type: ALLOW
                    items:
                    - # required
                      name: name_example
      logging_policies:
        # optional
        access_log:
          # optional
          is_enabled: true
        execution_log:
          # optional
          is_enabled: true
          log_level: INFO
      routes:
      - # required
        path: path_example
        backend:
          # required
          type: OAUTH2_LOGOUT_BACKEND

          # optional
          allowed_post_logout_uris: [ "allowed_post_logout_uris_example" ]
          post_logout_state: post_logout_state_example

        # optional
        methods: [ "ANY" ]
        request_policies:
          # optional
          authorization:
            # required
            allowed_scope: [ "allowed_scope_example" ]
            type: ANY_OF
          cors:
            # required
            allowed_origins: [ "allowed_origins_example" ]

            # optional
            allowed_methods: [ "allowed_methods_example" ]
            allowed_headers: [ "allowed_headers_example" ]
            exposed_headers: [ "exposed_headers_example" ]
            is_allow_credentials_enabled: true
            max_age_in_seconds: 56
          query_parameter_validations:
            # optional
            parameters:
            - # required
              name: name_example

              # optional
              required: true
            validation_mode: ENFORCING
          header_validations:
            # optional
            headers:
            - # required
              name: name_example

              # optional
              required: true
            validation_mode: ENFORCING
          body_validation:
            # required
            content:
              # optional
              validation_type: NONE
              # optional
            required: true
            validation_mode: ENFORCING
          header_transformations:
            # optional
            set_headers:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_headers:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_headers:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          query_parameter_transformations:
            # optional
            set_query_parameters:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_query_parameters:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_query_parameters:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          response_cache_lookup:
            # required
            type: SIMPLE_LOOKUP_POLICY

            # optional
            is_enabled: true
            is_private_caching_enabled: true
            cache_key_additions: [ "cache_key_additions_example" ]
        response_policies:
          # optional
          header_transformations:
            # optional
            set_headers:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_headers:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_headers:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          response_cache_store:
            # required
            type: FIXED_TTL_STORE_POLICY
            time_to_live_in_seconds: 56
        logging_policies:
          # optional
          access_log:
            # optional
            is_enabled: true
          execution_log:
            # optional
            is_enabled: true
            log_level: INFO

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deployment
  oci_apigateway_deployment:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    specification:
      # optional
      request_policies:
        # optional
        authentication:
          # required
          validation_policy:
            # required
            uri: uri_example
            type: REMOTE_JWKS

            # optional
            is_ssl_verify_disabled: true
            max_cache_duration_in_hours: 56
            additional_validation_policy:
              # optional
              issuers: [ "issuers_example" ]
              audiences: [ "audiences_example" ]
              verify_claims:
              - # required
                key: key_example

                # optional
                values: [ "values_example" ]
                is_required: true
          type: TOKEN_AUTHENTICATION

                # optional
          token_auth_scheme: token_auth_scheme_example
          max_clock_skew_in_seconds: 3.4
          is_anonymous_access_allowed: true
          token_header: token_header_example
          token_query_param: token_query_param_example
          validation_failure_policy:
            # required
            type: MODIFY_RESPONSE

            # optional
            response_code: response_code_example
            response_message: response_message_example
            response_header_transformations:
              # optional
              set_headers:
                # required
                items:
                - # required
                  name: name_example
                  values: [ "values_example" ]

                  # optional
                  if_exists: OVERWRITE
              rename_headers:
                # required
                items:
                - # required
                  _from: _from_example
                  to: to_example
              filter_headers:
                # required
                type: ALLOW
                items:
                - # required
                  name: name_example
        rate_limiting:
          # required
          rate_in_requests_per_second: 56
          rate_key: CLIENT_IP
        cors:
          # required
          allowed_origins: [ "allowed_origins_example" ]

          # optional
          allowed_methods: [ "allowed_methods_example" ]
          allowed_headers: [ "allowed_headers_example" ]
          exposed_headers: [ "exposed_headers_example" ]
          is_allow_credentials_enabled: true
          max_age_in_seconds: 56
        mutual_tls:
          # optional
          is_verified_certificate_required: true
          allowed_sans: [ "allowed_sans_example" ]
        usage_plans:
          # required
          token_locations: [ "token_locations_example" ]
        dynamic_authentication:
          # required
          selection_source:
            # required
            selector: selector_example

            # optional
            type: SINGLE
          authentication_servers:
          - # required
            key:
              # required
              expression: expression_example
              type: WILDCARD
              name: name_example

              # optional
              is_default: true
            authentication_server_detail:
              # required
              validation_policy:
                # required
                uri: uri_example
                type: REMOTE_JWKS

                # optional
                is_ssl_verify_disabled: true
                max_cache_duration_in_hours: 56
                additional_validation_policy:
                  # optional
                  issuers: [ "issuers_example" ]
                  audiences: [ "audiences_example" ]
                  verify_claims:
                  - # required
                    key: key_example

                    # optional
                    values: [ "values_example" ]
                    is_required: true
              type: TOKEN_AUTHENTICATION

                    # optional
              token_auth_scheme: token_auth_scheme_example
              max_clock_skew_in_seconds: 3.4
              is_anonymous_access_allowed: true
              token_header: token_header_example
              token_query_param: token_query_param_example
              validation_failure_policy:
                # required
                type: MODIFY_RESPONSE

                # optional
                response_code: response_code_example
                response_message: response_message_example
                response_header_transformations:
                  # optional
                  set_headers:
                    # required
                    items:
                    - # required
                      name: name_example
                      values: [ "values_example" ]

                      # optional
                      if_exists: OVERWRITE
                  rename_headers:
                    # required
                    items:
                    - # required
                      _from: _from_example
                      to: to_example
                  filter_headers:
                    # required
                    type: ALLOW
                    items:
                    - # required
                      name: name_example
      logging_policies:
        # optional
        access_log:
          # optional
          is_enabled: true
        execution_log:
          # optional
          is_enabled: true
          log_level: INFO
      routes:
      - # required
        path: path_example
        backend:
          # required
          type: OAUTH2_LOGOUT_BACKEND

          # optional
          allowed_post_logout_uris: [ "allowed_post_logout_uris_example" ]
          post_logout_state: post_logout_state_example

        # optional
        methods: [ "ANY" ]
        request_policies:
          # optional
          authorization:
            # required
            allowed_scope: [ "allowed_scope_example" ]
            type: ANY_OF
          cors:
            # required
            allowed_origins: [ "allowed_origins_example" ]

            # optional
            allowed_methods: [ "allowed_methods_example" ]
            allowed_headers: [ "allowed_headers_example" ]
            exposed_headers: [ "exposed_headers_example" ]
            is_allow_credentials_enabled: true
            max_age_in_seconds: 56
          query_parameter_validations:
            # optional
            parameters:
            - # required
              name: name_example

              # optional
              required: true
            validation_mode: ENFORCING
          header_validations:
            # optional
            headers:
            - # required
              name: name_example

              # optional
              required: true
            validation_mode: ENFORCING
          body_validation:
            # required
            content:
              # optional
              validation_type: NONE
              # optional
            required: true
            validation_mode: ENFORCING
          header_transformations:
            # optional
            set_headers:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_headers:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_headers:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          query_parameter_transformations:
            # optional
            set_query_parameters:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_query_parameters:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_query_parameters:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          response_cache_lookup:
            # required
            type: SIMPLE_LOOKUP_POLICY

            # optional
            is_enabled: true
            is_private_caching_enabled: true
            cache_key_additions: [ "cache_key_additions_example" ]
        response_policies:
          # optional
          header_transformations:
            # optional
            set_headers:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_headers:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_headers:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          response_cache_store:
            # required
            type: FIXED_TTL_STORE_POLICY
            time_to_live_in_seconds: 56
        logging_policies:
          # optional
          access_log:
            # optional
            is_enabled: true
          execution_log:
            # optional
            is_enabled: true
            log_level: INFO
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apigateway_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    specification:
      # optional
      request_policies:
        # optional
        authentication:
          # required
          validation_policy:
            # required
            uri: uri_example
            type: REMOTE_JWKS

            # optional
            is_ssl_verify_disabled: true
            max_cache_duration_in_hours: 56
            additional_validation_policy:
              # optional
              issuers: [ "issuers_example" ]
              audiences: [ "audiences_example" ]
              verify_claims:
              - # required
                key: key_example

                # optional
                values: [ "values_example" ]
                is_required: true
          type: TOKEN_AUTHENTICATION

                # optional
          token_auth_scheme: token_auth_scheme_example
          max_clock_skew_in_seconds: 3.4
          is_anonymous_access_allowed: true
          token_header: token_header_example
          token_query_param: token_query_param_example
          validation_failure_policy:
            # required
            type: MODIFY_RESPONSE

            # optional
            response_code: response_code_example
            response_message: response_message_example
            response_header_transformations:
              # optional
              set_headers:
                # required
                items:
                - # required
                  name: name_example
                  values: [ "values_example" ]

                  # optional
                  if_exists: OVERWRITE
              rename_headers:
                # required
                items:
                - # required
                  _from: _from_example
                  to: to_example
              filter_headers:
                # required
                type: ALLOW
                items:
                - # required
                  name: name_example
        rate_limiting:
          # required
          rate_in_requests_per_second: 56
          rate_key: CLIENT_IP
        cors:
          # required
          allowed_origins: [ "allowed_origins_example" ]

          # optional
          allowed_methods: [ "allowed_methods_example" ]
          allowed_headers: [ "allowed_headers_example" ]
          exposed_headers: [ "exposed_headers_example" ]
          is_allow_credentials_enabled: true
          max_age_in_seconds: 56
        mutual_tls:
          # optional
          is_verified_certificate_required: true
          allowed_sans: [ "allowed_sans_example" ]
        usage_plans:
          # required
          token_locations: [ "token_locations_example" ]
        dynamic_authentication:
          # required
          selection_source:
            # required
            selector: selector_example

            # optional
            type: SINGLE
          authentication_servers:
          - # required
            key:
              # required
              expression: expression_example
              type: WILDCARD
              name: name_example

              # optional
              is_default: true
            authentication_server_detail:
              # required
              validation_policy:
                # required
                uri: uri_example
                type: REMOTE_JWKS

                # optional
                is_ssl_verify_disabled: true
                max_cache_duration_in_hours: 56
                additional_validation_policy:
                  # optional
                  issuers: [ "issuers_example" ]
                  audiences: [ "audiences_example" ]
                  verify_claims:
                  - # required
                    key: key_example

                    # optional
                    values: [ "values_example" ]
                    is_required: true
              type: TOKEN_AUTHENTICATION

                    # optional
              token_auth_scheme: token_auth_scheme_example
              max_clock_skew_in_seconds: 3.4
              is_anonymous_access_allowed: true
              token_header: token_header_example
              token_query_param: token_query_param_example
              validation_failure_policy:
                # required
                type: MODIFY_RESPONSE

                # optional
                response_code: response_code_example
                response_message: response_message_example
                response_header_transformations:
                  # optional
                  set_headers:
                    # required
                    items:
                    - # required
                      name: name_example
                      values: [ "values_example" ]

                      # optional
                      if_exists: OVERWRITE
                  rename_headers:
                    # required
                    items:
                    - # required
                      _from: _from_example
                      to: to_example
                  filter_headers:
                    # required
                    type: ALLOW
                    items:
                    - # required
                      name: name_example
      logging_policies:
        # optional
        access_log:
          # optional
          is_enabled: true
        execution_log:
          # optional
          is_enabled: true
          log_level: INFO
      routes:
      - # required
        path: path_example
        backend:
          # required
          type: OAUTH2_LOGOUT_BACKEND

          # optional
          allowed_post_logout_uris: [ "allowed_post_logout_uris_example" ]
          post_logout_state: post_logout_state_example

        # optional
        methods: [ "ANY" ]
        request_policies:
          # optional
          authorization:
            # required
            allowed_scope: [ "allowed_scope_example" ]
            type: ANY_OF
          cors:
            # required
            allowed_origins: [ "allowed_origins_example" ]

            # optional
            allowed_methods: [ "allowed_methods_example" ]
            allowed_headers: [ "allowed_headers_example" ]
            exposed_headers: [ "exposed_headers_example" ]
            is_allow_credentials_enabled: true
            max_age_in_seconds: 56
          query_parameter_validations:
            # optional
            parameters:
            - # required
              name: name_example

              # optional
              required: true
            validation_mode: ENFORCING
          header_validations:
            # optional
            headers:
            - # required
              name: name_example

              # optional
              required: true
            validation_mode: ENFORCING
          body_validation:
            # required
            content:
              # optional
              validation_type: NONE
              # optional
            required: true
            validation_mode: ENFORCING
          header_transformations:
            # optional
            set_headers:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_headers:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_headers:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          query_parameter_transformations:
            # optional
            set_query_parameters:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_query_parameters:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_query_parameters:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          response_cache_lookup:
            # required
            type: SIMPLE_LOOKUP_POLICY

            # optional
            is_enabled: true
            is_private_caching_enabled: true
            cache_key_additions: [ "cache_key_additions_example" ]
        response_policies:
          # optional
          header_transformations:
            # optional
            set_headers:
              # required
              items:
              - # required
                name: name_example
                values: [ "values_example" ]

                # optional
                if_exists: OVERWRITE
            rename_headers:
              # required
              items:
              - # required
                _from: _from_example
                to: to_example
            filter_headers:
              # required
              type: ALLOW
              items:
              - # required
                name: name_example
          response_cache_store:
            # required
            type: FIXED_TTL_STORE_POLICY
            time_to_live_in_seconds: 56
        logging_policies:
          # optional
          access_log:
            # optional
            is_enabled: true
          execution_log:
            # optional
            is_enabled: true
            log_level: INFO
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete deployment
  oci_apigateway_deployment:
    # required
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apigateway_deployment:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.apigateway import WorkRequestsClient
    from oci.apigateway import DeploymentClient
    from oci.apigateway.models import CreateDeploymentDetails
    from oci.apigateway.models import UpdateDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayDeploymentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_possible_entity_types(self):
        return super(
            ApigatewayDeploymentHelperGen, self
        ).get_possible_entity_types() + [
            "deployment",
            "deployments",
            "apigatewaydeployment",
            "apigatewaydeployments",
            "deploymentresource",
            "deploymentsresource",
            "apigateway",
        ]

    def get_module_resource_id_param(self):
        return "deployment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deployment_id")

    def get_get_fn(self):
        return self.client.get_deployment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment, deployment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["gateway_id", "display_name"]

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
            self.client.list_deployments, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeploymentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deployment_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeploymentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deployment_id=self.module.params.get("deployment_id"),
                update_deployment_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deployment,
            call_fn_args=(),
            call_fn_kwargs=dict(deployment_id=self.module.params.get("deployment_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ApigatewayDeploymentHelperCustom = get_custom_class("ApigatewayDeploymentHelperCustom")


class ResourceHelper(ApigatewayDeploymentHelperCustom, ApigatewayDeploymentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            gateway_id=dict(type="str"),
            compartment_id=dict(type="str"),
            path_prefix=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            specification=dict(
                type="dict",
                options=dict(
                    request_policies=dict(
                        type="dict",
                        options=dict(
                            authentication=dict(
                                type="dict",
                                options=dict(
                                    validation_policy=dict(
                                        type="dict",
                                        options=dict(
                                            uri=dict(type="str"),
                                            client_details=dict(
                                                type="dict",
                                                options=dict(
                                                    client_id=dict(type="str"),
                                                    client_secret_id=dict(type="str"),
                                                    client_secret_version_number=dict(
                                                        type="int", no_log=True
                                                    ),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "CUSTOM",
                                                            "VALIDATION_BLOCK",
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            source_uri_details=dict(
                                                type="dict",
                                                options=dict(
                                                    uri=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "DISCOVERY_URI",
                                                            "VALIDATION_BLOCK",
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            is_ssl_verify_disabled=dict(type="bool"),
                                            max_cache_duration_in_hours=dict(
                                                type="int"
                                            ),
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "REMOTE_JWKS",
                                                    "REMOTE_DISCOVERY",
                                                    "STATIC_KEYS",
                                                ],
                                            ),
                                            additional_validation_policy=dict(
                                                type="dict",
                                                options=dict(
                                                    issuers=dict(
                                                        type="list", elements="str"
                                                    ),
                                                    audiences=dict(
                                                        type="list", elements="str"
                                                    ),
                                                    verify_claims=dict(
                                                        type="list",
                                                        elements="dict",
                                                        options=dict(
                                                            key=dict(
                                                                type="str",
                                                                required=True,
                                                                no_log=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                            ),
                                                            is_required=dict(
                                                                type="bool"
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            keys=dict(
                                                type="list",
                                                elements="dict",
                                                no_log=False,
                                                options=dict(
                                                    kty=dict(
                                                        type="str", choices=["RSA"]
                                                    ),
                                                    use=dict(
                                                        type="str", choices=["sig"]
                                                    ),
                                                    key_ops=dict(
                                                        type="list",
                                                        elements="str",
                                                        choices=["verify"],
                                                        no_log=True,
                                                    ),
                                                    alg=dict(type="str"),
                                                    n=dict(type="str"),
                                                    e=dict(type="str"),
                                                    kid=dict(type="str", required=True),
                                                    format=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["JSON_WEB_KEY", "PEM"],
                                                    ),
                                                    key=dict(type="str", no_log=True),
                                                ),
                                            ),
                                        ),
                                    ),
                                    token_auth_scheme=dict(type="str", no_log=True),
                                    max_clock_skew_in_seconds=dict(type="float"),
                                    issuers=dict(type="list", elements="str"),
                                    audiences=dict(type="list", elements="str"),
                                    verify_claims=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(
                                                type="str", required=True, no_log=True
                                            ),
                                            values=dict(type="list", elements="str"),
                                            is_required=dict(type="bool"),
                                        ),
                                    ),
                                    public_keys=dict(
                                        type="dict",
                                        no_log=False,
                                        options=dict(
                                            keys=dict(
                                                type="list",
                                                elements="dict",
                                                no_log=False,
                                                options=dict(
                                                    kty=dict(
                                                        type="str", choices=["RSA"]
                                                    ),
                                                    use=dict(
                                                        type="str", choices=["sig"]
                                                    ),
                                                    key_ops=dict(
                                                        type="list",
                                                        elements="str",
                                                        choices=["verify"],
                                                        no_log=True,
                                                    ),
                                                    alg=dict(type="str"),
                                                    n=dict(type="str"),
                                                    e=dict(type="str"),
                                                    kid=dict(type="str", required=True),
                                                    format=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["JSON_WEB_KEY", "PEM"],
                                                    ),
                                                    key=dict(type="str", no_log=True),
                                                ),
                                            ),
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["STATIC_KEYS", "REMOTE_JWKS"],
                                            ),
                                            uri=dict(type="str"),
                                            is_ssl_verify_disabled=dict(type="bool"),
                                            max_cache_duration_in_hours=dict(
                                                type="int"
                                            ),
                                        ),
                                    ),
                                    is_anonymous_access_allowed=dict(type="bool"),
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "TOKEN_AUTHENTICATION",
                                            "JWT_AUTHENTICATION",
                                            "CUSTOM_AUTHENTICATION",
                                        ],
                                    ),
                                    function_id=dict(type="str"),
                                    token_header=dict(type="str", no_log=True),
                                    token_query_param=dict(type="str", no_log=True),
                                    parameters=dict(type="dict"),
                                    cache_key=dict(
                                        type="list", elements="str", no_log=True
                                    ),
                                    validation_failure_policy=dict(
                                        type="dict",
                                        options=dict(
                                            response_code=dict(type="str"),
                                            response_message=dict(type="str"),
                                            response_header_transformations=dict(
                                                type="dict",
                                                options=dict(
                                                    set_headers=dict(
                                                        type="dict",
                                                        options=dict(
                                                            items=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    name=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                    values=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                        required=True,
                                                                    ),
                                                                    if_exists=dict(
                                                                        type="str",
                                                                        choices=[
                                                                            "OVERWRITE",
                                                                            "APPEND",
                                                                            "SKIP",
                                                                        ],
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    rename_headers=dict(
                                                        type="dict",
                                                        options=dict(
                                                            items=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    _from=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                    to=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                ),
                                                            )
                                                        ),
                                                    ),
                                                    filter_headers=dict(
                                                        type="dict",
                                                        options=dict(
                                                            type=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "ALLOW",
                                                                    "BLOCK",
                                                                ],
                                                            ),
                                                            items=dict(
                                                                type="list",
                                                                elements="dict",
                                                                required=True,
                                                                options=dict(
                                                                    name=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["MODIFY_RESPONSE", "OAUTH2"],
                                            ),
                                            client_details=dict(
                                                type="dict",
                                                options=dict(
                                                    client_id=dict(type="str"),
                                                    client_secret_id=dict(type="str"),
                                                    client_secret_version_number=dict(
                                                        type="int", no_log=True
                                                    ),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "CUSTOM",
                                                            "VALIDATION_BLOCK",
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            source_uri_details=dict(
                                                type="dict",
                                                options=dict(
                                                    uri=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "DISCOVERY_URI",
                                                            "VALIDATION_BLOCK",
                                                        ],
                                                    ),
                                                ),
                                            ),
                                            scopes=dict(type="list", elements="str"),
                                            max_expiry_duration_in_hours=dict(
                                                type="int"
                                            ),
                                            use_cookies_for_session=dict(type="bool"),
                                            use_cookies_for_intermediate_steps=dict(
                                                type="bool"
                                            ),
                                            use_pkce=dict(type="bool"),
                                            response_type=dict(
                                                type="str", choices=["CODE"]
                                            ),
                                            fallback_redirect_path=dict(type="str"),
                                            logout_path=dict(type="str"),
                                        ),
                                    ),
                                ),
                            ),
                            rate_limiting=dict(
                                type="dict",
                                options=dict(
                                    rate_in_requests_per_second=dict(
                                        type="int", required=True
                                    ),
                                    rate_key=dict(
                                        type="str",
                                        required=True,
                                        choices=["CLIENT_IP", "TOTAL"],
                                        no_log=True,
                                    ),
                                ),
                            ),
                            cors=dict(
                                type="dict",
                                options=dict(
                                    allowed_origins=dict(
                                        type="list", elements="str", required=True
                                    ),
                                    allowed_methods=dict(type="list", elements="str"),
                                    allowed_headers=dict(type="list", elements="str"),
                                    exposed_headers=dict(type="list", elements="str"),
                                    is_allow_credentials_enabled=dict(type="bool"),
                                    max_age_in_seconds=dict(type="int"),
                                ),
                            ),
                            mutual_tls=dict(
                                type="dict",
                                options=dict(
                                    is_verified_certificate_required=dict(type="bool"),
                                    allowed_sans=dict(type="list", elements="str"),
                                ),
                            ),
                            usage_plans=dict(
                                type="dict",
                                options=dict(
                                    token_locations=dict(
                                        type="list",
                                        elements="str",
                                        required=True,
                                        no_log=True,
                                    )
                                ),
                            ),
                            dynamic_authentication=dict(
                                type="dict",
                                options=dict(
                                    selection_source=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                default="SINGLE",
                                                choices=["SINGLE"],
                                            ),
                                            selector=dict(type="str", required=True),
                                        ),
                                    ),
                                    authentication_servers=dict(
                                        type="list",
                                        elements="dict",
                                        required=True,
                                        options=dict(
                                            key=dict(
                                                type="dict",
                                                required=True,
                                                no_log=False,
                                                options=dict(
                                                    expression=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        default="ANY_OF",
                                                        choices=["WILDCARD", "ANY_OF"],
                                                    ),
                                                    is_default=dict(type="bool"),
                                                    name=dict(
                                                        type="str", required=True
                                                    ),
                                                    values=dict(
                                                        type="list", elements="str"
                                                    ),
                                                ),
                                            ),
                                            authentication_server_detail=dict(
                                                type="dict",
                                                required=True,
                                                options=dict(
                                                    validation_policy=dict(
                                                        type="dict",
                                                        options=dict(
                                                            uri=dict(type="str"),
                                                            client_details=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    client_id=dict(
                                                                        type="str"
                                                                    ),
                                                                    client_secret_id=dict(
                                                                        type="str"
                                                                    ),
                                                                    client_secret_version_number=dict(
                                                                        type="int",
                                                                        no_log=True,
                                                                    ),
                                                                    type=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "CUSTOM",
                                                                            "VALIDATION_BLOCK",
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            source_uri_details=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    uri=dict(
                                                                        type="str"
                                                                    ),
                                                                    type=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "DISCOVERY_URI",
                                                                            "VALIDATION_BLOCK",
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            is_ssl_verify_disabled=dict(
                                                                type="bool"
                                                            ),
                                                            max_cache_duration_in_hours=dict(
                                                                type="int"
                                                            ),
                                                            type=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "REMOTE_JWKS",
                                                                    "REMOTE_DISCOVERY",
                                                                    "STATIC_KEYS",
                                                                ],
                                                            ),
                                                            additional_validation_policy=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    issuers=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                    ),
                                                                    audiences=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                    ),
                                                                    verify_claims=dict(
                                                                        type="list",
                                                                        elements="dict",
                                                                        options=dict(
                                                                            key=dict(
                                                                                type="str",
                                                                                required=True,
                                                                                no_log=True,
                                                                            ),
                                                                            values=dict(
                                                                                type="list",
                                                                                elements="str",
                                                                            ),
                                                                            is_required=dict(
                                                                                type="bool"
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                            keys=dict(
                                                                type="list",
                                                                elements="dict",
                                                                no_log=False,
                                                                options=dict(
                                                                    kty=dict(
                                                                        type="str",
                                                                        choices=["RSA"],
                                                                    ),
                                                                    use=dict(
                                                                        type="str",
                                                                        choices=["sig"],
                                                                    ),
                                                                    key_ops=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                        choices=[
                                                                            "verify"
                                                                        ],
                                                                        no_log=True,
                                                                    ),
                                                                    alg=dict(
                                                                        type="str"
                                                                    ),
                                                                    n=dict(type="str"),
                                                                    e=dict(type="str"),
                                                                    kid=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                    format=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "JSON_WEB_KEY",
                                                                            "PEM",
                                                                        ],
                                                                    ),
                                                                    key=dict(
                                                                        type="str",
                                                                        no_log=True,
                                                                    ),
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                    token_auth_scheme=dict(
                                                        type="str", no_log=True
                                                    ),
                                                    max_clock_skew_in_seconds=dict(
                                                        type="float"
                                                    ),
                                                    issuers=dict(
                                                        type="list", elements="str"
                                                    ),
                                                    audiences=dict(
                                                        type="list", elements="str"
                                                    ),
                                                    verify_claims=dict(
                                                        type="list",
                                                        elements="dict",
                                                        options=dict(
                                                            key=dict(
                                                                type="str",
                                                                required=True,
                                                                no_log=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                            ),
                                                            is_required=dict(
                                                                type="bool"
                                                            ),
                                                        ),
                                                    ),
                                                    public_keys=dict(
                                                        type="dict",
                                                        no_log=False,
                                                        options=dict(
                                                            keys=dict(
                                                                type="list",
                                                                elements="dict",
                                                                no_log=False,
                                                                options=dict(
                                                                    kty=dict(
                                                                        type="str",
                                                                        choices=["RSA"],
                                                                    ),
                                                                    use=dict(
                                                                        type="str",
                                                                        choices=["sig"],
                                                                    ),
                                                                    key_ops=dict(
                                                                        type="list",
                                                                        elements="str",
                                                                        choices=[
                                                                            "verify"
                                                                        ],
                                                                        no_log=True,
                                                                    ),
                                                                    alg=dict(
                                                                        type="str"
                                                                    ),
                                                                    n=dict(type="str"),
                                                                    e=dict(type="str"),
                                                                    kid=dict(
                                                                        type="str",
                                                                        required=True,
                                                                    ),
                                                                    format=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "JSON_WEB_KEY",
                                                                            "PEM",
                                                                        ],
                                                                    ),
                                                                    key=dict(
                                                                        type="str",
                                                                        no_log=True,
                                                                    ),
                                                                ),
                                                            ),
                                                            type=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "STATIC_KEYS",
                                                                    "REMOTE_JWKS",
                                                                ],
                                                            ),
                                                            uri=dict(type="str"),
                                                            is_ssl_verify_disabled=dict(
                                                                type="bool"
                                                            ),
                                                            max_cache_duration_in_hours=dict(
                                                                type="int"
                                                            ),
                                                        ),
                                                    ),
                                                    is_anonymous_access_allowed=dict(
                                                        type="bool"
                                                    ),
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "TOKEN_AUTHENTICATION",
                                                            "JWT_AUTHENTICATION",
                                                            "CUSTOM_AUTHENTICATION",
                                                        ],
                                                    ),
                                                    function_id=dict(type="str"),
                                                    token_header=dict(
                                                        type="str", no_log=True
                                                    ),
                                                    token_query_param=dict(
                                                        type="str", no_log=True
                                                    ),
                                                    parameters=dict(type="dict"),
                                                    cache_key=dict(
                                                        type="list",
                                                        elements="str",
                                                        no_log=True,
                                                    ),
                                                    validation_failure_policy=dict(
                                                        type="dict",
                                                        options=dict(
                                                            response_code=dict(
                                                                type="str"
                                                            ),
                                                            response_message=dict(
                                                                type="str"
                                                            ),
                                                            response_header_transformations=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    set_headers=dict(
                                                                        type="dict",
                                                                        options=dict(
                                                                            items=dict(
                                                                                type="list",
                                                                                elements="dict",
                                                                                required=True,
                                                                                options=dict(
                                                                                    name=dict(
                                                                                        type="str",
                                                                                        required=True,
                                                                                    ),
                                                                                    values=dict(
                                                                                        type="list",
                                                                                        elements="str",
                                                                                        required=True,
                                                                                    ),
                                                                                    if_exists=dict(
                                                                                        type="str",
                                                                                        choices=[
                                                                                            "OVERWRITE",
                                                                                            "APPEND",
                                                                                            "SKIP",
                                                                                        ],
                                                                                    ),
                                                                                ),
                                                                            )
                                                                        ),
                                                                    ),
                                                                    rename_headers=dict(
                                                                        type="dict",
                                                                        options=dict(
                                                                            items=dict(
                                                                                type="list",
                                                                                elements="dict",
                                                                                required=True,
                                                                                options=dict(
                                                                                    _from=dict(
                                                                                        type="str",
                                                                                        required=True,
                                                                                    ),
                                                                                    to=dict(
                                                                                        type="str",
                                                                                        required=True,
                                                                                    ),
                                                                                ),
                                                                            )
                                                                        ),
                                                                    ),
                                                                    filter_headers=dict(
                                                                        type="dict",
                                                                        options=dict(
                                                                            type=dict(
                                                                                type="str",
                                                                                required=True,
                                                                                choices=[
                                                                                    "ALLOW",
                                                                                    "BLOCK",
                                                                                ],
                                                                            ),
                                                                            items=dict(
                                                                                type="list",
                                                                                elements="dict",
                                                                                required=True,
                                                                                options=dict(
                                                                                    name=dict(
                                                                                        type="str",
                                                                                        required=True,
                                                                                    )
                                                                                ),
                                                                            ),
                                                                        ),
                                                                    ),
                                                                ),
                                                            ),
                                                            type=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "MODIFY_RESPONSE",
                                                                    "OAUTH2",
                                                                ],
                                                            ),
                                                            client_details=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    client_id=dict(
                                                                        type="str"
                                                                    ),
                                                                    client_secret_id=dict(
                                                                        type="str"
                                                                    ),
                                                                    client_secret_version_number=dict(
                                                                        type="int",
                                                                        no_log=True,
                                                                    ),
                                                                    type=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "CUSTOM",
                                                                            "VALIDATION_BLOCK",
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            source_uri_details=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    uri=dict(
                                                                        type="str"
                                                                    ),
                                                                    type=dict(
                                                                        type="str",
                                                                        required=True,
                                                                        choices=[
                                                                            "DISCOVERY_URI",
                                                                            "VALIDATION_BLOCK",
                                                                        ],
                                                                    ),
                                                                ),
                                                            ),
                                                            scopes=dict(
                                                                type="list",
                                                                elements="str",
                                                            ),
                                                            max_expiry_duration_in_hours=dict(
                                                                type="int"
                                                            ),
                                                            use_cookies_for_session=dict(
                                                                type="bool"
                                                            ),
                                                            use_cookies_for_intermediate_steps=dict(
                                                                type="bool"
                                                            ),
                                                            use_pkce=dict(type="bool"),
                                                            response_type=dict(
                                                                type="str",
                                                                choices=["CODE"],
                                                            ),
                                                            fallback_redirect_path=dict(
                                                                type="str"
                                                            ),
                                                            logout_path=dict(
                                                                type="str"
                                                            ),
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    logging_policies=dict(
                        type="dict",
                        options=dict(
                            access_log=dict(
                                type="dict", options=dict(is_enabled=dict(type="bool"))
                            ),
                            execution_log=dict(
                                type="dict",
                                options=dict(
                                    is_enabled=dict(type="bool"),
                                    log_level=dict(
                                        type="str", choices=["INFO", "WARN", "ERROR"]
                                    ),
                                ),
                            ),
                        ),
                    ),
                    routes=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            path=dict(type="str", required=True),
                            methods=dict(
                                type="list",
                                elements="str",
                                choices=[
                                    "ANY",
                                    "HEAD",
                                    "GET",
                                    "POST",
                                    "PUT",
                                    "PATCH",
                                    "DELETE",
                                    "OPTIONS",
                                ],
                            ),
                            request_policies=dict(
                                type="dict",
                                options=dict(
                                    authorization=dict(
                                        type="dict",
                                        options=dict(
                                            allowed_scope=dict(
                                                type="list", elements="str"
                                            ),
                                            type=dict(
                                                type="str",
                                                default="AUTHENTICATION_ONLY",
                                                choices=[
                                                    "ANY_OF",
                                                    "ANONYMOUS",
                                                    "AUTHENTICATION_ONLY",
                                                ],
                                            ),
                                        ),
                                    ),
                                    cors=dict(
                                        type="dict",
                                        options=dict(
                                            allowed_origins=dict(
                                                type="list",
                                                elements="str",
                                                required=True,
                                            ),
                                            allowed_methods=dict(
                                                type="list", elements="str"
                                            ),
                                            allowed_headers=dict(
                                                type="list", elements="str"
                                            ),
                                            exposed_headers=dict(
                                                type="list", elements="str"
                                            ),
                                            is_allow_credentials_enabled=dict(
                                                type="bool"
                                            ),
                                            max_age_in_seconds=dict(type="int"),
                                        ),
                                    ),
                                    query_parameter_validations=dict(
                                        type="dict",
                                        options=dict(
                                            parameters=dict(
                                                type="list",
                                                elements="dict",
                                                options=dict(
                                                    required=dict(type="bool"),
                                                    name=dict(
                                                        type="str", required=True
                                                    ),
                                                ),
                                            ),
                                            validation_mode=dict(
                                                type="str",
                                                choices=[
                                                    "ENFORCING",
                                                    "PERMISSIVE",
                                                    "DISABLED",
                                                ],
                                            ),
                                        ),
                                    ),
                                    header_validations=dict(
                                        type="dict",
                                        options=dict(
                                            headers=dict(
                                                type="list",
                                                elements="dict",
                                                options=dict(
                                                    required=dict(type="bool"),
                                                    name=dict(
                                                        type="str", required=True
                                                    ),
                                                ),
                                            ),
                                            validation_mode=dict(
                                                type="str",
                                                choices=[
                                                    "ENFORCING",
                                                    "PERMISSIVE",
                                                    "DISABLED",
                                                ],
                                            ),
                                        ),
                                    ),
                                    body_validation=dict(
                                        type="dict",
                                        options=dict(
                                            required=dict(type="bool"),
                                            content=dict(type="dict", required=True),
                                            validation_mode=dict(
                                                type="str",
                                                choices=[
                                                    "ENFORCING",
                                                    "PERMISSIVE",
                                                    "DISABLED",
                                                ],
                                            ),
                                        ),
                                    ),
                                    header_transformations=dict(
                                        type="dict",
                                        options=dict(
                                            set_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                                required=True,
                                                            ),
                                                            if_exists=dict(
                                                                type="str",
                                                                choices=[
                                                                    "OVERWRITE",
                                                                    "APPEND",
                                                                    "SKIP",
                                                                ],
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            rename_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            _from=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            to=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            filter_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["ALLOW", "BLOCK"],
                                                    ),
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                    query_parameter_transformations=dict(
                                        type="dict",
                                        options=dict(
                                            set_query_parameters=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                                required=True,
                                                            ),
                                                            if_exists=dict(
                                                                type="str",
                                                                choices=[
                                                                    "OVERWRITE",
                                                                    "APPEND",
                                                                    "SKIP",
                                                                ],
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            rename_query_parameters=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            _from=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            to=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            filter_query_parameters=dict(
                                                type="dict",
                                                options=dict(
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["ALLOW", "BLOCK"],
                                                    ),
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                    response_cache_lookup=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["SIMPLE_LOOKUP_POLICY"],
                                            ),
                                            is_enabled=dict(type="bool"),
                                            is_private_caching_enabled=dict(
                                                type="bool"
                                            ),
                                            cache_key_additions=dict(
                                                type="list", elements="str", no_log=True
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            response_policies=dict(
                                type="dict",
                                options=dict(
                                    header_transformations=dict(
                                        type="dict",
                                        options=dict(
                                            set_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            values=dict(
                                                                type="list",
                                                                elements="str",
                                                                required=True,
                                                            ),
                                                            if_exists=dict(
                                                                type="str",
                                                                choices=[
                                                                    "OVERWRITE",
                                                                    "APPEND",
                                                                    "SKIP",
                                                                ],
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            rename_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            _from=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                            to=dict(
                                                                type="str",
                                                                required=True,
                                                            ),
                                                        ),
                                                    )
                                                ),
                                            ),
                                            filter_headers=dict(
                                                type="dict",
                                                options=dict(
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["ALLOW", "BLOCK"],
                                                    ),
                                                    items=dict(
                                                        type="list",
                                                        elements="dict",
                                                        required=True,
                                                        options=dict(
                                                            name=dict(
                                                                type="str",
                                                                required=True,
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    ),
                                    response_cache_store=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["FIXED_TTL_STORE_POLICY"],
                                            ),
                                            time_to_live_in_seconds=dict(
                                                type="int", required=True
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            logging_policies=dict(
                                type="dict",
                                options=dict(
                                    access_log=dict(
                                        type="dict",
                                        options=dict(is_enabled=dict(type="bool")),
                                    ),
                                    execution_log=dict(
                                        type="dict",
                                        options=dict(
                                            is_enabled=dict(type="bool"),
                                            log_level=dict(
                                                type="str",
                                                choices=["INFO", "WARN", "ERROR"],
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            backend=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    allowed_post_logout_uris=dict(
                                        type="list", elements="str"
                                    ),
                                    post_logout_state=dict(type="str"),
                                    url=dict(type="str"),
                                    connect_timeout_in_seconds=dict(type="float"),
                                    read_timeout_in_seconds=dict(type="float"),
                                    send_timeout_in_seconds=dict(type="float"),
                                    is_ssl_verify_disabled=dict(type="bool"),
                                    function_id=dict(type="str"),
                                    body=dict(type="str"),
                                    status=dict(type="int"),
                                    headers=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            name=dict(type="str"),
                                            value=dict(type="str"),
                                        ),
                                    ),
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "OAUTH2_LOGOUT_BACKEND",
                                            "HTTP_BACKEND",
                                            "ORACLE_FUNCTIONS_BACKEND",
                                            "STOCK_RESPONSE_BACKEND",
                                            "DYNAMIC_ROUTING_BACKEND",
                                        ],
                                    ),
                                    selection_source=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                default="SINGLE",
                                                choices=["SINGLE"],
                                            ),
                                            selector=dict(type="str", required=True),
                                        ),
                                    ),
                                    routing_backends=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(
                                                type="dict",
                                                required=True,
                                                no_log=False,
                                                options=dict(
                                                    expression=dict(type="str"),
                                                    type=dict(
                                                        type="str",
                                                        default="ANY_OF",
                                                        choices=["WILDCARD", "ANY_OF"],
                                                    ),
                                                    is_default=dict(type="bool"),
                                                    name=dict(
                                                        type="str", required=True
                                                    ),
                                                    values=dict(
                                                        type="list", elements="str"
                                                    ),
                                                ),
                                            ),
                                            backend=dict(
                                                type="dict",
                                                required=True,
                                                options=dict(
                                                    type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "ORACLE_FUNCTIONS_BACKEND",
                                                            "HTTP_BACKEND",
                                                            "STOCK_RESPONSE_BACKEND",
                                                            "DYNAMIC_ROUTING_BACKEND",
                                                            "OAUTH2_LOGOUT_BACKEND",
                                                        ],
                                                    )
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            deployment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
