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
module: oci_apigateway_deployment_facts
short_description: Fetches details about one or multiple Deployment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Deployment resources in Oracle Cloud Infrastructure
    - Returns a list of deployments.
    - If I(deployment_id) is specified, the details of a single Deployment will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    deployment_id:
        description:
            - The ocid of the deployment.
            - Required to get a specific deployment.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ocid of the compartment in which to list resources.
            - Required to list multiple deployments.
        type: str
    gateway_id:
        description:
            - Filter deployments by the gateway ocid.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state.
            - "Example: `SUCCEEDED`"
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'. The default order depends on the sortBy value.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for `timeCreated` is descending. Default order for
              `displayName` is ascending. The `displayName` sort order is case
              sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List deployments
  oci_apigateway_deployment_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific deployment
  oci_apigateway_deployment_facts:
    deployment_id: "ocid1.deployment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
deployments:
    description:
        - List of Deployment resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        gateway_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: string
            sample: "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx"
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
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                                                    type: string
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
                                            type: string
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
                                                    type: string
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
                                            type: string
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
                                                    type: string
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
                                            type: string
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
                                            type: string
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
                                            type: string
                                            sample: FIXED_TTL_STORE_POLICY
                                        time_to_live_in_seconds:
                                            description:
                                                - Sets the number of seconds for a response from a backend being stored in the Response Cache before it expires.
                                            returned: on success
                                            type: int
                                            sample: 300
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
    sample: [{
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
                    "response_cache_store": {
                        "type": "FIXED_TTL_STORE_POLICY",
                        "time_to_live_in_seconds": 300
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apigateway import DeploymentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApigatewayDeploymentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "deployment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deployment,
            deployment_id=self.module.params.get("deployment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "gateway_id",
            "display_name",
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
            self.client.list_deployments,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ApigatewayDeploymentFactsHelperCustom = get_custom_class(
    "ApigatewayDeploymentFactsHelperCustom"
)


class ResourceFactsHelper(
    ApigatewayDeploymentFactsHelperCustom, ApigatewayDeploymentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deployment_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            gateway_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="deployment",
        service_client_class=DeploymentClient,
        namespace="apigateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(deployments=result)


if __name__ == "__main__":
    main()
