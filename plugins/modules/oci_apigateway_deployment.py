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
module: oci_apigateway_deployment
short_description: Manage a Deployment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Deployment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new deployment.
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - "Example: `My new resource`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
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
                                    - "JWT_AUTHENTICATION"
                                    - "CUSTOM_AUTHENTICATION"
                                required: true
                            token_header:
                                description:
                                    - The name of the header containing the authentication token.
                                type: str
                            token_query_param:
                                description:
                                    - The name of the query parameter containing the authentication token.
                                type: str
                            token_auth_scheme:
                                description:
                                    - "The authentication scheme that is to be used when authenticating
                                      the token. This must to be provided if \\"tokenHeader\\" is specified."
                                    - Applicable when type is 'JWT_AUTHENTICATION'
                                type: str
                            issuers:
                                description:
                                    - A list of parties that could have issued the token.
                                    - Required when type is 'JWT_AUTHENTICATION'
                                type: list
                            audiences:
                                description:
                                    - The list of intended recipients for the token.
                                    - Required when type is 'JWT_AUTHENTICATION'
                                type: list
                            verify_claims:
                                description:
                                    - A list of claims which should be validated to consider the token valid.
                                    - Applicable when type is 'JWT_AUTHENTICATION'
                                type: list
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
                                    is_required:
                                        description:
                                            - "Whether the claim is required to be present in the JWT or not. If set
                                              to \\"false\\", the claim values will be matched only if the claim is
                                              present in the JWT."
                                            - Applicable when type is 'JWT_AUTHENTICATION'
                                        type: bool
                            max_clock_skew_in_seconds:
                                description:
                                    - The maximum expected time difference between the system clocks
                                      of the token issuer and the API Gateway.
                                    - Applicable when type is 'JWT_AUTHENTICATION'
                                type: float
                            public_keys:
                                description:
                                    - ""
                                    - Required when type is 'JWT_AUTHENTICATION'
                                type: dict
                                suboptions:
                                    type:
                                        description:
                                            - Type of the public key set.
                                        type: str
                                        choices:
                                            - "STATIC_KEYS"
                                            - "REMOTE_JWKS"
                                        required: true
                                    keys:
                                        description:
                                            - The set of static public keys.
                                            - Applicable when type is 'STATIC_KEYS'
                                        type: list
                                        suboptions:
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
                                            key:
                                                description:
                                                    - The content of the PEM-encoded public key.
                                                    - Required when format is 'PEM'
                                                type: str
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
                            function_id:
                                description:
                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function
                                      resource.
                                    - Required when type is 'CUSTOM_AUTHENTICATION'
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
                                required: true
                            allowed_methods:
                                description:
                                    - "The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the
                                      Access-Control-Allow-Methods header. '*' will allow all methods."
                                type: list
                            allowed_headers:
                                description:
                                    - "The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header.
                                      '*' will allow all headers."
                                type: list
                            exposed_headers:
                                description:
                                    - "The list of headers that the client will be allowed to see from the response as indicated by the
                                      Access-Control-Expose-Headers header. '*' will expose all headers."
                                type: list
                            is_allow_credentials_enabled:
                                description:
                                    - Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.
                                type: bool
                            max_age_in_seconds:
                                description:
                                    - The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
                                      if greater than 0.
                                type: int
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
                                    allowed_scope:
                                        description:
                                            - A user whose scope includes any of these access ranges is allowed on
                                              this route. Access ranges are case-sensitive.
                                            - Required when type is 'ANY_OF'
                                        type: list
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
                                        required: true
                                    allowed_methods:
                                        description:
                                            - "The list of allowed HTTP methods that will be returned for the preflight OPTIONS request in the
                                              Access-Control-Allow-Methods header. '*' will allow all methods."
                                        type: list
                                    allowed_headers:
                                        description:
                                            - "The list of headers that will be allowed from the client via the Access-Control-Allow-Headers header.
                                              '*' will allow all headers."
                                        type: list
                                    exposed_headers:
                                        description:
                                            - "The list of headers that the client will be allowed to see from the response as indicated by the
                                              Access-Control-Expose-Headers header. '*' will expose all headers."
                                        type: list
                                    is_allow_credentials_enabled:
                                        description:
                                            - Whether to send the Access-Control-Allow-Credentials header to allow CORS requests with cookies.
                                        type: bool
                                    max_age_in_seconds:
                                        description:
                                            - The time in seconds for the client to cache preflight responses. This is sent as the Access-Control-Max-Age
                                              if greater than 0.
                                        type: int
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
                                                required: true
                                                suboptions:
                                                    name:
                                                        description:
                                                            - The case-sensitive name of the query parameter.
                                                        type: str
                                                        required: true
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
                                                required: true
                                                suboptions:
                                                    name:
                                                        description:
                                                            - The case-insensitive name of the header.  This name must be unique across transformation policies.
                                                        type: str
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
                            type:
                                description:
                                    - Type of the API backend.
                                type: str
                                choices:
                                    - "HTTP_BACKEND"
                                    - "ORACLE_FUNCTIONS_BACKEND"
                                    - "STOCK_RESPONSE_BACKEND"
                                required: true
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
    gateway_id: ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    path_prefix: path_prefix_example

- name: Update deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apigateway_deployment:
    display_name: My new resource
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update deployment
  oci_apigateway_deployment:
    display_name: My new resource
    deployment_id: ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete deployment
  oci_apigateway_deployment:
    deployment_id: ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete deployment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_apigateway_deployment:
    display_name: My new resource
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        gateway_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: string
            sample: ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
                - "Example: `My new resource`"
            returned: on success
            type: string
            sample: My new resource
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which the
                  resource is created.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        path_prefix:
            description:
                - A path on which to deploy all routes contained in the API
                  deployment specification. For more information, see
                  L(Deploying an API on an API Gateway by Creating an API
                  Deployment,https://docs.cloud.oracle.com/iaas/Content/APIGateway/Tasks/apigatewaycreatingdeployment.htm).
            returned: on success
            type: string
            sample: path_prefix_example
        endpoint:
            description:
                - The endpoint to access this deployment on the gateway.
            returned: on success
            type: string
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
                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function
                                          resource.
                                    returned: on success
                                    type: string
                                    sample: ocid1.function.oc1..xxxxxxEXAMPLExxxxxx
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
                                                  authenticated API must have the \\"isAnonymousAccessAllowed\\" property set to \\"true\\" in the
                                                  authentication
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
                                                                - The case-insensitive name of the header.  This name must be unique across transformation
                                                                  policies.
                                                            returned: on success
                                                            type: string
                                                            sample: X-CorrelationID
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
                                                                - The original case-insensitive name of the header.  This name must be unique across
                                                                  transformation policies.
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
                                                                - The case-insensitive name of the header.  This name must be unique across transformation
                                                                  policies.
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
                                                                - The case-sensitive name of the query parameter.  This name must be unique across
                                                                  transformation policies.
                                                            returned: on success
                                                            type: string
                                                            sample: bookIsbn
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
                                                        - BLOCK drops any query parameters that are in the list of items, so it acts as an exclusion list.
                                                          ALLOW
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
                                                                - The case-insensitive name of the header.  This name must be unique across transformation
                                                                  policies.
                                                            returned: on success
                                                            type: string
                                                            sample: X-CorrelationID
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
                                                                - The original case-insensitive name of the header.  This name must be unique across
                                                                  transformation policies.
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
                                                                - The case-insensitive name of the header.  This name must be unique across transformation
                                                                  policies.
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
                                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Functions function
                                          resource.
                                    returned: on success
                                    type: string
                                    sample: ocid1.function.oc1..xxxxxxEXAMPLExxxxxx
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
        time_created:
            description:
                - The time this resource was created. An RFC3339 formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time this resource was last updated. An RFC3339 formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the deployment.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
                  For example, can be used to provide actionable information for a
                  resource in a Failed state.
            returned: on success
            type: string
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
        "display_name": "My new resource",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "path_prefix": "path_prefix_example",
        "endpoint": "endpoint_example",
        "specification": {
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
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.apigateway import DeploymentClient
    from oci.apigateway.models import CreateDeploymentDetails
    from oci.apigateway.models import UpdateDeploymentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayDeploymentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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
            display_name=dict(aliases=["name"], type="str"),
            gateway_id=dict(type="str"),
            compartment_id=dict(type="str"),
            path_prefix=dict(type="str"),
            specification=dict(
                type="dict",
                options=dict(
                    request_policies=dict(
                        type="dict",
                        options=dict(
                            authentication=dict(
                                type="dict",
                                options=dict(
                                    is_anonymous_access_allowed=dict(type="bool"),
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "JWT_AUTHENTICATION",
                                            "CUSTOM_AUTHENTICATION",
                                        ],
                                    ),
                                    token_header=dict(type="str"),
                                    token_query_param=dict(type="str"),
                                    token_auth_scheme=dict(type="str"),
                                    issuers=dict(type="list"),
                                    audiences=dict(type="list"),
                                    verify_claims=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            key=dict(type="str", required=True),
                                            values=dict(type="list"),
                                            is_required=dict(type="bool"),
                                        ),
                                    ),
                                    max_clock_skew_in_seconds=dict(type="float"),
                                    public_keys=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["STATIC_KEYS", "REMOTE_JWKS"],
                                            ),
                                            keys=dict(
                                                type="list",
                                                elements="dict",
                                                options=dict(
                                                    kid=dict(type="str", required=True),
                                                    format=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["JSON_WEB_KEY", "PEM"],
                                                    ),
                                                    kty=dict(
                                                        type="str", choices=["RSA"]
                                                    ),
                                                    use=dict(
                                                        type="str", choices=["sig"]
                                                    ),
                                                    key_ops=dict(
                                                        type="list", choices=["verify"]
                                                    ),
                                                    alg=dict(type="str"),
                                                    n=dict(type="str"),
                                                    e=dict(type="str"),
                                                    key=dict(type="str"),
                                                ),
                                            ),
                                            uri=dict(type="str"),
                                            is_ssl_verify_disabled=dict(type="bool"),
                                            max_cache_duration_in_hours=dict(
                                                type="int"
                                            ),
                                        ),
                                    ),
                                    function_id=dict(type="str"),
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
                                    ),
                                ),
                            ),
                            cors=dict(
                                type="dict",
                                options=dict(
                                    allowed_origins=dict(type="list", required=True),
                                    allowed_methods=dict(type="list"),
                                    allowed_headers=dict(type="list"),
                                    exposed_headers=dict(type="list"),
                                    is_allow_credentials_enabled=dict(type="bool"),
                                    max_age_in_seconds=dict(type="int"),
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
                                            type=dict(
                                                type="str",
                                                default="AUTHENTICATION_ONLY",
                                                choices=[
                                                    "ANY_OF",
                                                    "ANONYMOUS",
                                                    "AUTHENTICATION_ONLY",
                                                ],
                                            ),
                                            allowed_scope=dict(type="list"),
                                        ),
                                    ),
                                    cors=dict(
                                        type="dict",
                                        options=dict(
                                            allowed_origins=dict(
                                                type="list", required=True
                                            ),
                                            allowed_methods=dict(type="list"),
                                            allowed_headers=dict(type="list"),
                                            exposed_headers=dict(type="list"),
                                            is_allow_credentials_enabled=dict(
                                                type="bool"
                                            ),
                                            max_age_in_seconds=dict(type="int"),
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
                                    )
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
                                    type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "HTTP_BACKEND",
                                            "ORACLE_FUNCTIONS_BACKEND",
                                            "STOCK_RESPONSE_BACKEND",
                                        ],
                                    ),
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

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
