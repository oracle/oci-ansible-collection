#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
version_added: "2.9"
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
                            type: string
                            sample: JWT_AUTHENTICATION
                        token_header:
                            description:
                                - The name of the header containing the authentication token.
                            returned: on success
                            type: string
                            sample: Authorization
                        token_query_param:
                            description:
                                - The name of the query parameter containing the authentication token.
                            returned: on success
                            type: string
                            sample: tk
                        token_auth_scheme:
                            description:
                                - "The authentication scheme that is to be used when authenticating
                                  the token. This must to be provided if \\"tokenHeader\\" is specified."
                            returned: on success
                            type: string
                            sample: Bearer
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
                                    type: string
                                    sample: iss
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
                                type:
                                    description:
                                        - Type of the public key set.
                                    returned: on success
                                    type: string
                                    sample: STATIC_KEYS
                                keys:
                                    description:
                                        - The set of static public keys.
                                    returned: on success
                                    type: complex
                                    contains:
                                        kid:
                                            description:
                                                - "A unique key ID. This key will be used to verify the signature of a
                                                  JWT with matching \\"kid\\"."
                                            returned: on success
                                            type: string
                                            sample: kid_example
                                        format:
                                            description:
                                                - The format of the public key.
                                            returned: on success
                                            type: string
                                            sample: JSON_WEB_KEY
                                        kty:
                                            description:
                                                - The key type.
                                            returned: on success
                                            type: string
                                            sample: RSA
                                        use:
                                            description:
                                                - The intended use of the public key.
                                            returned: on success
                                            type: string
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
                                            type: string
                                            sample: alg_example
                                        n:
                                            description:
                                                - The base64 url encoded modulus of the RSA public key represented
                                                  by this key.
                                            returned: on success
                                            type: string
                                            sample: n_example
                                        e:
                                            description:
                                                - The base64 url encoded exponent of the RSA public key represented
                                                  by this key.
                                            returned: on success
                                            type: string
                                            sample: e_example
                                        key:
                                            description:
                                                - The content of the PEM-encoded public key.
                                            returned: on success
                                            type: string
                                            sample: -----BEGIN PUBLIC KEY-----
                                uri:
                                    description:
                                        - The uri from which to retrieve the key. It must be accessible
                                          without authentication.
                                    returned: on success
                                    type: string
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
                        function_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function resource.
                            returned: on success
                            type: string
                            sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
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
                            type: string
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
                            sample: false
                        max_age_in_seconds:
                            description:
                                - The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
                                  if greater than 0.
                            returned: on success
                            type: int
                            sample: 600
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
                            type: string
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
                    type: string
                    sample: /todos
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
                                type:
                                    description:
                                        - "Indicates how authorization should be applied. For a type of ANY_OF, an \\"allowedScope\\"
                                          property must also be specified. Otherwise, only a type is required. For a type of ANONYMOUS, an
                                          authenticated API must have the \\"isAnonymousAccessAllowed\\" property set to \\"true\\" in the authentication
                                          policy."
                                    returned: on success
                                    type: string
                                    sample: ANY_OF
                                allowed_scope:
                                    description:
                                        - A user whose scope includes any of these access ranges is allowed on
                                          this route. Access ranges are case-sensitive.
                                    returned: on success
                                    type: list
                                    sample: []
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
                                    sample: false
                                max_age_in_seconds:
                                    description:
                                        - The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
                                          if greater than 0.
                                    returned: on success
                                    type: int
                                    sample: 600
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
                                                    type: string
                                                    sample: X-CorrelationID
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
                                                    type: string
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
                                                    type: string
                                                    sample: X-Username
                                                to:
                                                    description:
                                                        - The new name of the header.  This name must be unique across transformation policies.
                                                    returned: on success
                                                    type: string
                                                    sample: X-User-ID
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
                                            type: string
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
                                                    type: string
                                                    sample: User-Agent
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
                                                    type: string
                                                    sample: bookIsbn
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
                                                    type: string
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
                                                    type: string
                                                    sample: bookId
                                                to:
                                                    description:
                                                        - The new name of the query parameter.  This name must be unique across transformation policies.
                                                    returned: on success
                                                    type: string
                                                    sample: bookIsbn
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
                                            type: string
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
                                                    type: string
                                                    sample: bookIsbn
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
                                                    type: string
                                                    sample: X-CorrelationID
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
                                                    type: string
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
                                                    type: string
                                                    sample: X-Username
                                                to:
                                                    description:
                                                        - The new name of the header.  This name must be unique across transformation policies.
                                                    returned: on success
                                                    type: string
                                                    sample: X-User-ID
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
                                            type: string
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
                                                    type: string
                                                    sample: User-Agent
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
                                    type: string
                                    sample: INFO
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
                            type: string
                            sample: HTTP_BACKEND
                        url:
                            description:
                                - ""
                            returned: on success
                            type: string
                            sample: https://1.2.3.4:9999
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
                            type: string
                            sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
                        body:
                            description:
                                - The body of the stock response from the mock backend.
                            returned: on success
                            type: string
                            sample: Hello World!
                        status:
                            description:
                                - The status code of the stock response from the mock backend.
                            returned: on success
                            type: int
                            sample: 200
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
                                    type: string
                                    sample: Content-Type
                                value:
                                    description:
                                        - Value of the header.
                                    returned: on success
                                    type: string
                                    sample: application/json
    sample: {
        "request_policies": {
            "authentication": {
                "is_anonymous_access_allowed": true,
                "type": "JWT_AUTHENTICATION",
                "token_header": "Authorization",
                "token_query_param": "tk",
                "token_auth_scheme": "Bearer",
                "issuers": [],
                "audiences": [],
                "verify_claims": [{
                    "key": "iss",
                    "values": [],
                    "is_required": true
                }],
                "max_clock_skew_in_seconds": 3.4,
                "public_keys": {
                    "type": "STATIC_KEYS",
                    "keys": [{
                        "kid": "kid_example",
                        "format": "JSON_WEB_KEY",
                        "kty": "RSA",
                        "use": "sig",
                        "key_ops": [],
                        "alg": "alg_example",
                        "n": "n_example",
                        "e": "e_example",
                        "key": "-----BEGIN PUBLIC KEY-----"
                    }],
                    "uri": "uri_example",
                    "is_ssl_verify_disabled": true,
                    "max_cache_duration_in_hours": 56
                },
                "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
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
                "is_allow_credentials_enabled": false,
                "max_age_in_seconds": 600
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
            "path": "/todos",
            "methods": [],
            "request_policies": {
                "authorization": {
                    "type": "ANY_OF",
                    "allowed_scope": []
                },
                "cors": {
                    "allowed_origins": [],
                    "allowed_methods": [],
                    "allowed_headers": [],
                    "exposed_headers": [],
                    "is_allow_credentials_enabled": false,
                    "max_age_in_seconds": 600
                },
                "header_transformations": {
                    "set_headers": {
                        "items": [{
                            "name": "X-CorrelationID",
                            "values": [],
                            "if_exists": "OVERWRITE"
                        }]
                    },
                    "rename_headers": {
                        "items": [{
                            "_from": "X-Username",
                            "to": "X-User-ID"
                        }]
                    },
                    "filter_headers": {
                        "type": "ALLOW",
                        "items": [{
                            "name": "User-Agent"
                        }]
                    }
                },
                "query_parameter_transformations": {
                    "set_query_parameters": {
                        "items": [{
                            "name": "bookIsbn",
                            "values": [],
                            "if_exists": "OVERWRITE"
                        }]
                    },
                    "rename_query_parameters": {
                        "items": [{
                            "_from": "bookId",
                            "to": "bookIsbn"
                        }]
                    },
                    "filter_query_parameters": {
                        "type": "ALLOW",
                        "items": [{
                            "name": "bookIsbn"
                        }]
                    }
                }
            },
            "response_policies": {
                "header_transformations": {
                    "set_headers": {
                        "items": [{
                            "name": "X-CorrelationID",
                            "values": [],
                            "if_exists": "OVERWRITE"
                        }]
                    },
                    "rename_headers": {
                        "items": [{
                            "_from": "X-Username",
                            "to": "X-User-ID"
                        }]
                    },
                    "filter_headers": {
                        "type": "ALLOW",
                        "items": [{
                            "name": "User-Agent"
                        }]
                    }
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
                "type": "HTTP_BACKEND",
                "url": "https://1.2.3.4:9999",
                "connect_timeout_in_seconds": 3.4,
                "read_timeout_in_seconds": 3.4,
                "send_timeout_in_seconds": 3.4,
                "is_ssl_verify_disabled": true,
                "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
                "body": "Hello World!",
                "status": 200,
                "headers": [{
                    "name": "Content-Type",
                    "value": "application/json"
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
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(api_specification=result)


if __name__ == "__main__":
    main()
