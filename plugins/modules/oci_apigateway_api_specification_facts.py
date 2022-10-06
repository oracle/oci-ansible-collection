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
module: oci_apigateway_api_specification_facts
short_description: Fetches details about a ApiSpecification resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ApiSpecification resource in Oracle Cloud Infrastructure
    - Gets an API Deployment specification by identifier.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    api_id:
        description:
            - The ocid of the API.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific api_specification
  oci_apigateway_api_specification_facts:
    # required
    api_id: "ocid1.api.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
api_specification:
    description:
        - ApiSpecification resource
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
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function resource.
                            returned: on success
                            type: str
                            sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                        parameters:
                            description:
                                - "A map where key is a user defined string and value is a context expressions whose values will be sent to the custom auth
                                  function. Values should contain an expression.
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
                        validation_failure_policy:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - Type of the Validation failure Policy.
                                    returned: on success
                                    type: str
                                    sample: MODIFY_RESPONSE
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
                        max_clock_skew_in_seconds:
                            description:
                                - The maximum expected time difference between the system clocks
                                  of the token issuer and the API Gateway.
                            returned: on success
                            type: float
                            sample: 3.4
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
                                                - Information regarding the set of values of selector for which this branch should be selected.
                                            returned: on success
                                            type: list
                                            sample: []
                                        type:
                                            description:
                                                - Information regarding type of the selection key.
                                            returned: on success
                                            type: str
                                            sample: ANY_OF
                                        is_default:
                                            description:
                                                - Information regarding whether this is the default branch.
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
                                                - String describing the expression with wildcards.
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
                                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions
                                                  function resource.
                                            returned: on success
                                            type: str
                                            sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                                        parameters:
                                            description:
                                                - "A map where key is a user defined string and value is a context expressions whose values will be sent to the
                                                  custom auth function. Values should contain an expression.
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
                                        validation_failure_policy:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                type:
                                                    description:
                                                        - Type of the Validation failure Policy.
                                                    returned: on success
                                                    type: str
                                                    sample: MODIFY_RESPONSE
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
                                                                                - If a header with the same name already exists in the request, OVERWRITE will
                                                                                  overwrite the value,
                                                                                  APPEND will append to the existing value, or SKIP will keep the existing
                                                                                  value.
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
                                                                                - The original case-insensitive name of the header.  This name must be unique
                                                                                  across transformation policies.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: _from_example
                                                                        to:
                                                                            description:
                                                                                - The new name of the header.  This name must be unique across transformation
                                                                                  policies.
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
                                                                        - BLOCK drops any headers that are in the list of items, so it acts as an exclusion
                                                                          list.  ALLOW
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
                                                                                - The case-insensitive name of the header.  This name must be unique across
                                                                                  transformation policies.
                                                                            returned: on success
                                                                            type: str
                                                                            sample: name_example
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
                                        max_clock_skew_in_seconds:
                                            description:
                                                - The maximum expected time difference between the system clocks
                                                  of the token issuer and the API Gateway.
                                            returned: on success
                                            type: float
                                            sample: 3.4
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
                                          authenticated API must have the \\"isAnonymousAccessAllowed\\" property set to \\"true\\" in the authentication
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
                                        - The content of the request body. The key is a L(media type range,https://tools.ietf.org/html/rfc7231#appendix-D)
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
                                                        - The case-insensitive name of the header.  This name must be unique across transformation policies.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                values:
                                                    description:
                                                        - A list of new values.  Each value can be a constant or may include one or more expressions enclosed
                                                          within
                                                          ${} delimiters.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                if_exists:
                                                    description:
                                                        - If a header with the same name already exists in the request, OVERWRITE will overwrite the value,
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
                                                        - The original case-insensitive name of the header.  This name must be unique across transformation
                                                          policies.
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
                                                        - The case-insensitive name of the header.  This name must be unique across transformation policies.
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
                                                        - The case-sensitive name of the query parameter.  This name must be unique across transformation
                                                          policies.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                values:
                                                    description:
                                                        - A list of new values.  Each value can be a constant or may include one or more expressions enclosed
                                                          within
                                                          ${} delimiters.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                if_exists:
                                                    description:
                                                        - If a query parameter with the same name already exists in the request, OVERWRITE will overwrite the
                                                          value,
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
                                                - BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list.  ALLOW
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
                                        - Set true to allow caching responses where the request has an Authorization header. Ensure you have configured your
                                          cache key additions to get the level of isolation across authenticated requests that you require.
                                        - When false, any request with an Authorization header will not be stored in the Response Cache.
                                        - If using the CustomAuthenticationPolicy then the tokenHeader/tokenQueryParam are also subject to this check.
                                    returned: on success
                                    type: bool
                                    sample: true
                                cache_key_additions:
                                    description:
                                        - A list of context expressions whose values will be added to the base cache key. Values should contain an expression
                                          enclosed within
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
                                                        - The case-insensitive name of the header.  This name must be unique across transformation policies.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                values:
                                                    description:
                                                        - A list of new values.  Each value can be a constant or may include one or more expressions enclosed
                                                          within
                                                          ${} delimiters.
                                                    returned: on success
                                                    type: list
                                                    sample: []
                                                if_exists:
                                                    description:
                                                        - If a header with the same name already exists in the request, OVERWRITE will overwrite the value,
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
                                                        - The original case-insensitive name of the header.  This name must be unique across transformation
                                                          policies.
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
                                                        - The case-insensitive name of the header.  This name must be unique across transformation policies.
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
                                                - Information regarding the set of values of selector for which this branch should be selected.
                                            returned: on success
                                            type: list
                                            sample: []
                                        type:
                                            description:
                                                - Information regarding type of the selection key.
                                            returned: on success
                                            type: str
                                            sample: ANY_OF
                                        is_default:
                                            description:
                                                - Information regarding whether this is the default branch.
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
                                                - String describing the expression with wildcards.
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
                        function_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function resource.
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
    sample: {
        "request_policies": {
            "authentication": {
                "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
                "parameters": {},
                "cache_key": [],
                "validation_failure_policy": {
                    "type": "MODIFY_RESPONSE",
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
                    }
                },
                "is_anonymous_access_allowed": true,
                "type": "CUSTOM_AUTHENTICATION",
                "token_header": "token_header_example",
                "token_query_param": "token_query_param_example",
                "token_auth_scheme": "token_auth_scheme_example",
                "issuers": [],
                "audiences": [],
                "verify_claims": [{
                    "key": "key_example",
                    "values": [],
                    "is_required": true
                }],
                "max_clock_skew_in_seconds": 3.4,
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
                        "validation_failure_policy": {
                            "type": "MODIFY_RESPONSE",
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
                            }
                        },
                        "is_anonymous_access_allowed": true,
                        "type": "CUSTOM_AUTHENTICATION",
                        "token_header": "token_header_example",
                        "token_query_param": "token_query_param_example",
                        "token_auth_scheme": "token_auth_scheme_example",
                        "issuers": [],
                        "audiences": [],
                        "verify_claims": [{
                            "key": "key_example",
                            "values": [],
                            "is_required": true
                        }],
                        "max_clock_skew_in_seconds": 3.4,
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apigateway import ApiGatewayClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayApiSpecificationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "api_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_api_deployment_specification,
            api_id=self.module.params.get("api_id"),
        )


ApigatewayApiSpecificationFactsHelperCustom = get_custom_class(
    "ApigatewayApiSpecificationFactsHelperCustom"
)


class ResourceFactsHelper(
    ApigatewayApiSpecificationFactsHelperCustom,
    ApigatewayApiSpecificationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(api_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="api_specification",
        service_client_class=ApiGatewayClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(api_specification=result)


if __name__ == "__main__":
    main()
