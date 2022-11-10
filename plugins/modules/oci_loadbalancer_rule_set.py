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
module: oci_loadbalancer_rule_set
short_description: Manage a RuleSet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a RuleSet resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new rule set associated with the specified load balancer. For more information, see
      L(Managing Rule Sets,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    items:
        description:
            - An array of rules that compose the rule set.
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: list
        elements: dict
        suboptions:
            response_code:
                description:
                    - The HTTP status code to return when the incoming request is redirected.
                    - "The status line returned with the code is mapped from the standard HTTP specification. Valid response
                      codes for redirection are:"
                    - "*  301
                      *  302
                      *  303
                      *  307
                      *  308"
                    - The default value is `302` (Found).
                    - "Example: `301`"
                    - Applicable when action is 'REDIRECT'
                type: int
            redirect_uri:
                description:
                    - ""
                    - Applicable when action is 'REDIRECT'
                type: dict
                suboptions:
                    protocol:
                        description:
                            - The HTTP protocol to use in the redirect URI.
                            - "When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the
                              incoming HTTP request URI. Allowed values are:"
                            - "*  HTTP
                              *  HTTPS
                              *  {protocol}"
                            - "`{protocol}` is the only valid token for this property. It can appear only once in the value string."
                            - "Example: `HTTPS`"
                            - Applicable when action is 'REDIRECT'
                        type: str
                    host:
                        description:
                            - The valid domain name (hostname) or IP address to use in the redirect URI.
                            - When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the
                              incoming HTTP request URI.
                            - All RedirectUri tokens are valid for this property. You can use any token more than once.
                            - Curly braces are valid in this property only to surround tokens, such as `{host}`
                            - "Examples:"
                            - "*  **example.com** appears as `example.com` in the redirect URI."
                            - "*  **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the
                                 incoming HTTP request URI."
                            - "*  **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and
                                 the port is `8081` in the incoming HTTP request URI."
                            - Applicable when action is 'REDIRECT'
                        type: str
                    port:
                        description:
                            - The communication port to use in the redirect URI.
                            - Valid values include integers from 1 to 65535.
                            - When this value is null, the service preserves the original port from the incoming HTTP request URI.
                            - "Example: `8081`"
                            - Applicable when action is 'REDIRECT'
                        type: int
                    path:
                        description:
                            - The HTTP URI path to use in the redirect URI.
                            - "When this value is null, not set, or set to `{path}`, the service preserves the original path from the
                              incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, \\"\\"."
                            - All RedirectUri tokens are valid for this property. You can use any token more than once.
                            - The path string must begin with `/` if it does not begin with the `{path}` token.
                            - "Examples:"
                            - "*  __/example/video/123__ appears as `/example/video/123` in the redirect URI."
                            - "*  __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the
                                 incoming HTTP request URI."
                            - "*  __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the
                                 incoming HTTP request URI."
                            - "*  __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video` is the path in the
                                 incoming HTTP request URI."
                            - "*  __/{host}/123__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname
                                 in the incoming HTTP request URI."
                            - "*  __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and
                                 `123` is the port in the incoming HTTP request URI."
                            - "*  __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP
                                 request URI."
                            - Applicable when action is 'REDIRECT'
                        type: str
                    query:
                        description:
                            - The query string to use in the redirect URI.
                            - When this value is null, not set, or set to `{query}`, the service preserves the original query parameters
                              from the incoming HTTP request URI.
                            - All `RedirectUri` tokens are valid for this property. You can use any token more than once.
                            - If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character.
                            - "You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand
                              (&) character. To omit all incoming query parameters from the redirect URI, set this value to an empty
                              string, \\"\\"."
                            - If the specified query string results in a redirect URI ending with `?` or `&`, the last character is truncated.
                              For example, if the incoming URI is `http://host.com:8080/documents` and the query property value is
                              `?lang=en&{query}`, the redirect URI is `http://host.com:8080/documents?lang=en`. The system
                              truncates the final ampersand (&) because the incoming URI included no value to replace the {query} token.
                            - "Examples:
                              * **lang=en&time_zone=PST** appears as `lang=en&time_zone=PST` in the redirect URI."
                            - "* **{query}** appears as `lang=en&time_zone=PST` in the redirect URI if `lang=en&time_zone=PST` is the query
                                string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}`
                                token renders as an empty string."
                            - "* **lang=en&{query}&time_zone=PST** appears as `lang=en&country=us&time_zone=PST` in the redirect URI if
                                `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query
                                parameters, this value renders as `lang=en&time_zone=PST`."
                            - "*  **protocol={protocol}&hostname={host}** appears as `protocol=http&hostname=example.com` in the redirect
                                 URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request."
                            - "*  **port={port}&hostname={host}** appears as `port=8080&hostname=example.com` in the redirect URI if the
                                 port is `8080` and the hostname is `example.com` in the incoming HTTP request URI."
                            - Applicable when action is 'REDIRECT'
                        type: str
            allowed_methods:
                description:
                    - The list of HTTP methods allowed for this listener.
                    - By default, you can specify only the standard HTTP methods defined in the
                      L(HTTP Method Registry,http://www.iana.org/assignments/http-methods/http-methods.xhtml). You can also
                      see a list of supported standard HTTP methods in the Load Balancing service documentation at
                      L(Managing Rule Sets,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm).
                    - Your backend application must be able to handle the methods specified in this list.
                    - The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact
                      L(My Oracle Support,http://support.oracle.com/) to remove the restriction for your tenancy.
                    - "Example: [\\"GET\\", \\"PUT\\", \\"POST\\", \\"PROPFIND\\"]"
                    - Required when action is 'CONTROL_ACCESS_USING_HTTP_METHODS'
                type: list
                elements: str
            status_code:
                description:
                    - The HTTP status code to return when the requested HTTP method is not in the list of allowed methods.
                      The associated status line returned with the code is mapped from the standard HTTP specification. The
                      default value is `405 (Method Not Allowed)`.
                    - "Example: 403"
                    - Applicable when action is 'CONTROL_ACCESS_USING_HTTP_METHODS'
                type: int
            conditions:
                description:
                    - ""
                    - Required when action is one of ['REDIRECT', 'ALLOW']
                type: list
                elements: dict
                suboptions:
                    operator:
                        description:
                            - A string that specifies how to compare the PathMatchCondition object's `attributeValue` string to the
                              incoming URI.
                            - "*  **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string."
                            - "*  **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best,
                                 longest match of the beginning portion of the incoming URI path."
                            - "*  **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the
                                 `attributeValue` string."
                            - "*  **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue`
                                 string."
                            - Required when attribute_name is 'PATH'
                        type: str
                        choices:
                            - "EXACT_MATCH"
                            - "FORCE_LONGEST_PREFIX_MATCH"
                            - "PREFIX_MATCH"
                            - "SUFFIX_MATCH"
                    attribute_name:
                        description:
                            - ""
                        type: str
                        choices:
                            - "SOURCE_VCN_ID"
                            - "SOURCE_IP_ADDRESS"
                            - "PATH"
                            - "SOURCE_VCN_IP_ADDRESS"
                        required: true
                    attribute_value:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the originating VCN that an incoming packet
                              must match.
                            - You can use this condition in conjunction with `SourceVcnIpAddressCondition`.
                            - "**NOTE:** If you define this condition for a rule without a `SourceVcnIpAddressCondition`, this condition
                              matches all incoming traffic in the specified VCN."
                        type: str
                        required: true
            description:
                description:
                    - A brief description of the access control rule. Avoid entering confidential information.
                    - "example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`"
                    - Applicable when action is 'ALLOW'
                type: str
            are_invalid_characters_allowed:
                description:
                    - "Indicates whether or not invalid characters in client header fields will be allowed.
                      Valid names are composed of English letters, digits, hyphens and underscores.
                      If \\"true\\", invalid characters are allowed in the HTTP header.
                      If \\"false\\", invalid characters are not allowed in the HTTP header"
                    - Applicable when action is 'HTTP_HEADER'
                type: bool
            http_large_header_size_in_kb:
                description:
                    - The maximum size of each buffer used for reading http client request header.
                      This value indicates the maximum size allowed for each buffer.
                      The allowed values for buffer size are 8, 16, 32 and 64.
                    - Applicable when action is 'HTTP_HEADER'
                type: int
            value:
                description:
                    - "A header value that conforms to RFC 7230. With the following exceptions:
                      *  value cannot contain `$`
                      *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                    - "Example: `example_value`"
                    - Required when action is one of ['ADD_HTTP_RESPONSE_HEADER', 'ADD_HTTP_REQUEST_HEADER']
                type: str
            action:
                description:
                    - ""
                type: str
                choices:
                    - "ADD_HTTP_REQUEST_HEADER"
                    - "REDIRECT"
                    - "REMOVE_HTTP_REQUEST_HEADER"
                    - "EXTEND_HTTP_REQUEST_HEADER_VALUE"
                    - "REMOVE_HTTP_RESPONSE_HEADER"
                    - "CONTROL_ACCESS_USING_HTTP_METHODS"
                    - "ALLOW"
                    - "HTTP_HEADER"
                    - "ADD_HTTP_RESPONSE_HEADER"
                    - "EXTEND_HTTP_RESPONSE_HEADER_VALUE"
                required: true
            header:
                description:
                    - A header name that conforms to RFC 7230.
                    - "Example: `example_header_name`"
                    - Required when action is one of ['REMOVE_HTTP_REQUEST_HEADER', 'EXTEND_HTTP_REQUEST_HEADER_VALUE', 'ADD_HTTP_RESPONSE_HEADER',
                      'ADD_HTTP_REQUEST_HEADER', 'REMOVE_HTTP_RESPONSE_HEADER', 'EXTEND_HTTP_RESPONSE_HEADER_VALUE']
                type: str
            prefix:
                description:
                    - "A string to prepend to the header value. The resulting header value must conform to RFC 7230.
                      With the following exceptions:
                      *  value cannot contain `$`
                      *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                    - "Example: `example_prefix_value`"
                    - Applicable when action is one of ['EXTEND_HTTP_REQUEST_HEADER_VALUE', 'EXTEND_HTTP_RESPONSE_HEADER_VALUE']
                type: str
            suffix:
                description:
                    - "A string to append to the header value. The resulting header value must conform to RFC 7230.
                      With the following exceptions:
                      *  value cannot contain `$`
                      *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                    - "Example: `example_suffix_value`"
                    - Applicable when action is one of ['EXTEND_HTTP_REQUEST_HEADER_VALUE', 'EXTEND_HTTP_RESPONSE_HEADER_VALUE']
                type: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the specified load balancer.
        type: str
        required: true
    name:
        description:
            - The name for this set of rules. It must be unique and it cannot be changed. Avoid entering
              confidential information.
            - "Example: `example_rule_set`"
        type: str
        required: true
    state:
        description:
            - The state of the RuleSet.
            - Use I(state=present) to create or update a RuleSet.
            - Use I(state=absent) to delete a RuleSet.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create rule_set
  oci_loadbalancer_rule_set:
    # required
    items:
    - # required
      value: value_example
      action: ADD_HTTP_REQUEST_HEADER
      header: header_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

- name: Update rule_set
  oci_loadbalancer_rule_set:
    # required
    items:
    - # required
      value: value_example
      action: ADD_HTTP_REQUEST_HEADER
      header: header_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

- name: Delete rule_set
  oci_loadbalancer_rule_set:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

"""

RETURN = """
rule_set:
    description:
        - Details of the RuleSet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name for this set of rules. It must be unique and it cannot be changed. Avoid entering
                  confidential information.
                - "Example: `example_rule_set`"
            returned: on success
            type: str
            sample: name_example
        items:
            description:
                - An array of rules that compose the rule set.
            returned: on success
            type: complex
            contains:
                value:
                    description:
                        - "A header value that conforms to RFC 7230. With the following exceptions:
                          *  value cannot contain `$`
                          *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                        - "Example: `example_value`"
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - A brief description of the access control rule. Avoid entering confidential information.
                        - "example: `192.168.0.0/16 and 2001:db8::/32 are trusted clients. Whitelist them.`"
                    returned: on success
                    type: str
                    sample: description_example
                allowed_methods:
                    description:
                        - The list of HTTP methods allowed for this listener.
                        - By default, you can specify only the standard HTTP methods defined in the
                          L(HTTP Method Registry,http://www.iana.org/assignments/http-methods/http-methods.xhtml). You can also
                          see a list of supported standard HTTP methods in the Load Balancing service documentation at
                          L(Managing Rule Sets,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrulesets.htm).
                        - Your backend application must be able to handle the methods specified in this list.
                        - The list of HTTP methods is extensible. If you need to configure custom HTTP methods, contact
                          L(My Oracle Support,http://support.oracle.com/) to remove the restriction for your tenancy.
                        - "Example: [\\"GET\\", \\"PUT\\", \\"POST\\", \\"PROPFIND\\"]"
                    returned: on success
                    type: list
                    sample: []
                status_code:
                    description:
                        - The HTTP status code to return when the requested HTTP method is not in the list of allowed methods.
                          The associated status line returned with the code is mapped from the standard HTTP specification. The
                          default value is `405 (Method Not Allowed)`.
                        - "Example: 403"
                    returned: on success
                    type: int
                    sample: 56
                prefix:
                    description:
                        - "A string to prepend to the header value. The resulting header value must conform to RFC 7230.
                          With the following exceptions:
                          *  value cannot contain `$`
                          *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                        - "Example: `example_prefix_value`"
                    returned: on success
                    type: str
                    sample: prefix_example
                suffix:
                    description:
                        - "A string to append to the header value. The resulting header value must conform to RFC 7230.
                          With the following exceptions:
                          *  value cannot contain `$`
                          *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are invalid."
                        - "Example: `example_suffix_value`"
                    returned: on success
                    type: str
                    sample: suffix_example
                are_invalid_characters_allowed:
                    description:
                        - "Indicates whether or not invalid characters in client header fields will be allowed.
                          Valid names are composed of English letters, digits, hyphens and underscores.
                          If \\"true\\", invalid characters are allowed in the HTTP header.
                          If \\"false\\", invalid characters are not allowed in the HTTP header"
                    returned: on success
                    type: bool
                    sample: true
                http_large_header_size_in_kb:
                    description:
                        - The maximum size of each buffer used for reading http client request header.
                          This value indicates the maximum size allowed for each buffer.
                          The allowed values for buffer size are 8, 16, 32 and 64.
                    returned: on success
                    type: int
                    sample: 56
                response_code:
                    description:
                        - The HTTP status code to return when the incoming request is redirected.
                        - "The status line returned with the code is mapped from the standard HTTP specification. Valid response
                          codes for redirection are:"
                        - "*  301
                          *  302
                          *  303
                          *  307
                          *  308"
                        - The default value is `302` (Found).
                        - "Example: `301`"
                    returned: on success
                    type: int
                    sample: 56
                conditions:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        operator:
                            description:
                                - A string that specifies how to compare the PathMatchCondition object's `attributeValue` string to the
                                  incoming URI.
                                - "*  **EXACT_MATCH** - The incoming URI path must exactly and completely match the `attributeValue` string."
                                - "*  **FORCE_LONGEST_PREFIX_MATCH** - The system looks for the `attributeValue` string with the best,
                                     longest match of the beginning portion of the incoming URI path."
                                - "*  **PREFIX_MATCH** - The beginning portion of the incoming URI path must exactly match the
                                     `attributeValue` string."
                                - "*  **SUFFIX_MATCH** - The ending portion of the incoming URI path must exactly match the `attributeValue`
                                     string."
                            returned: on success
                            type: str
                            sample: EXACT_MATCH
                        attribute_name:
                            description:
                                - ""
                            returned: on success
                            type: str
                            sample: SOURCE_IP_ADDRESS
                        attribute_value:
                            description:
                                - The path string that the redirection rule applies to.
                                - "Example: `/example`"
                            returned: on success
                            type: str
                            sample: attribute_value_example
                redirect_uri:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        protocol:
                            description:
                                - The HTTP protocol to use in the redirect URI.
                                - "When this value is null, not set, or set to `{protocol}`, the service preserves the original protocol from the
                                  incoming HTTP request URI. Allowed values are:"
                                - "*  HTTP
                                  *  HTTPS
                                  *  {protocol}"
                                - "`{protocol}` is the only valid token for this property. It can appear only once in the value string."
                                - "Example: `HTTPS`"
                            returned: on success
                            type: str
                            sample: protocol_example
                        host:
                            description:
                                - The valid domain name (hostname) or IP address to use in the redirect URI.
                                - When this value is null, not set, or set to `{host}`, the service preserves the original domain name from the
                                  incoming HTTP request URI.
                                - All RedirectUri tokens are valid for this property. You can use any token more than once.
                                - Curly braces are valid in this property only to surround tokens, such as `{host}`
                                - "Examples:"
                                - "*  **example.com** appears as `example.com` in the redirect URI."
                                - "*  **in{host}** appears as `inexample.com` in the redirect URI if `example.com` is the hostname in the
                                     incoming HTTP request URI."
                                - "*  **{port}{host}** appears as `8081example.com` in the redirect URI if `example.com` is the hostname and
                                     the port is `8081` in the incoming HTTP request URI."
                            returned: on success
                            type: str
                            sample: host_example
                        port:
                            description:
                                - The communication port to use in the redirect URI.
                                - Valid values include integers from 1 to 65535.
                                - When this value is null, the service preserves the original port from the incoming HTTP request URI.
                                - "Example: `8081`"
                            returned: on success
                            type: int
                            sample: 56
                        path:
                            description:
                                - The HTTP URI path to use in the redirect URI.
                                - "When this value is null, not set, or set to `{path}`, the service preserves the original path from the
                                  incoming HTTP request URI. To omit the path from the redirect URI, set this value to an empty string, \\"\\"."
                                - All RedirectUri tokens are valid for this property. You can use any token more than once.
                                - The path string must begin with `/` if it does not begin with the `{path}` token.
                                - "Examples:"
                                - "*  __/example/video/123__ appears as `/example/video/123` in the redirect URI."
                                - "*  __/example{path}__ appears as `/example/video/123` in the redirect URI if `/video/123` is the path in the
                                     incoming HTTP request URI."
                                - "*  __{path}/123__ appears as `/example/video/123` in the redirect URI if `/example/video` is the path in the
                                     incoming HTTP request URI."
                                - "*  __{path}123__ appears as `/example/video123` in the redirect URI if `/example/video` is the path in the
                                     incoming HTTP request URI."
                                - "*  __/{host}/123__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname
                                     in the incoming HTTP request URI."
                                - "*  __/{host}/{port}__ appears as `/example.com/123` in the redirect URI if `example.com` is the hostname and
                                     `123` is the port in the incoming HTTP request URI."
                                - "*  __/{query}__ appears as `/lang=en` in the redirect URI if the query is `lang=en` in the incoming HTTP
                                     request URI."
                            returned: on success
                            type: str
                            sample: path_example
                        query:
                            description:
                                - The query string to use in the redirect URI.
                                - When this value is null, not set, or set to `{query}`, the service preserves the original query parameters
                                  from the incoming HTTP request URI.
                                - All `RedirectUri` tokens are valid for this property. You can use any token more than once.
                                - If the query string does not begin with the `{query}` token, it must begin with the question mark (?) character.
                                - "You can specify multiple query parameters as a single string. Separate each query parameter with an ampersand
                                  (&) character. To omit all incoming query parameters from the redirect URI, set this value to an empty
                                  string, \\"\\"."
                                - If the specified query string results in a redirect URI ending with `?` or `&`, the last character is truncated.
                                  For example, if the incoming URI is `http://host.com:8080/documents` and the query property value is
                                  `?lang=en&{query}`, the redirect URI is `http://host.com:8080/documents?lang=en`. The system
                                  truncates the final ampersand (&) because the incoming URI included no value to replace the {query} token.
                                - "Examples:
                                  * **lang=en&time_zone=PST** appears as `lang=en&time_zone=PST` in the redirect URI."
                                - "* **{query}** appears as `lang=en&time_zone=PST` in the redirect URI if `lang=en&time_zone=PST` is the query
                                    string in the incoming HTTP request. If the incoming HTTP request has no query parameters, the `{query}`
                                    token renders as an empty string."
                                - "* **lang=en&{query}&time_zone=PST** appears as `lang=en&country=us&time_zone=PST` in the redirect URI if
                                    `country=us` is the query string in the incoming HTTP request. If the incoming HTTP request has no query
                                    parameters, this value renders as `lang=en&time_zone=PST`."
                                - "*  **protocol={protocol}&hostname={host}** appears as `protocol=http&hostname=example.com` in the redirect
                                     URI if the protocol is `HTTP` and the hostname is `example.com` in the incoming HTTP request."
                                - "*  **port={port}&hostname={host}** appears as `port=8080&hostname=example.com` in the redirect URI if the
                                     port is `8080` and the hostname is `example.com` in the incoming HTTP request URI."
                            returned: on success
                            type: str
                            sample: query_example
                action:
                    description:
                        - ""
                    returned: on success
                    type: str
                    sample: ADD_HTTP_REQUEST_HEADER
                header:
                    description:
                        - A header name that conforms to RFC 7230.
                        - "Example: `example_header_name`"
                    returned: on success
                    type: str
                    sample: header_example
    sample: {
        "name": "name_example",
        "items": [{
            "value": "value_example",
            "description": "description_example",
            "allowed_methods": [],
            "status_code": 56,
            "prefix": "prefix_example",
            "suffix": "suffix_example",
            "are_invalid_characters_allowed": true,
            "http_large_header_size_in_kb": 56,
            "response_code": 56,
            "conditions": [{
                "operator": "EXACT_MATCH",
                "attribute_name": "SOURCE_IP_ADDRESS",
                "attribute_value": "attribute_value_example"
            }],
            "redirect_uri": {
                "protocol": "protocol_example",
                "host": "host_example",
                "port": 56,
                "path": "path_example",
                "query": "query_example"
            },
            "action": "ADD_HTTP_REQUEST_HEADER",
            "header": "header_example"
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.load_balancer import LoadBalancerClient
    from oci.load_balancer.models import CreateRuleSetDetails
    from oci.load_balancer.models import UpdateRuleSetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RuleSetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(RuleSetHelperGen, self).get_possible_entity_types() + [
            "ruleset",
            "rulesets",
            "loadBalancerruleset",
            "loadBalancerrulesets",
            "rulesetresource",
            "rulesetsresource",
            "loadbalancer",
        ]

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_rule_set

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_rule_set,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            rule_set_name=self.module.params.get("name"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "load_balancer_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_rule_sets, **kwargs)

    def get_create_model_class(self):
        return CreateRuleSetDetails

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_rule_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                create_rule_set_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateRuleSetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_rule_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                rule_set_name=self.module.params.get("name"),
                update_rule_set_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_rule_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                rule_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


RuleSetHelperCustom = get_custom_class("RuleSetHelperCustom")


class ResourceHelper(RuleSetHelperCustom, RuleSetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    response_code=dict(type="int"),
                    redirect_uri=dict(
                        type="dict",
                        options=dict(
                            protocol=dict(type="str"),
                            host=dict(type="str"),
                            port=dict(type="int"),
                            path=dict(type="str"),
                            query=dict(type="str"),
                        ),
                    ),
                    allowed_methods=dict(type="list", elements="str"),
                    status_code=dict(type="int"),
                    conditions=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            operator=dict(
                                type="str",
                                choices=[
                                    "EXACT_MATCH",
                                    "FORCE_LONGEST_PREFIX_MATCH",
                                    "PREFIX_MATCH",
                                    "SUFFIX_MATCH",
                                ],
                            ),
                            attribute_name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "SOURCE_VCN_ID",
                                    "SOURCE_IP_ADDRESS",
                                    "PATH",
                                    "SOURCE_VCN_IP_ADDRESS",
                                ],
                            ),
                            attribute_value=dict(type="str", required=True),
                        ),
                    ),
                    description=dict(type="str"),
                    are_invalid_characters_allowed=dict(type="bool"),
                    http_large_header_size_in_kb=dict(type="int"),
                    value=dict(type="str"),
                    action=dict(
                        type="str",
                        required=True,
                        choices=[
                            "ADD_HTTP_REQUEST_HEADER",
                            "REDIRECT",
                            "REMOVE_HTTP_REQUEST_HEADER",
                            "EXTEND_HTTP_REQUEST_HEADER_VALUE",
                            "REMOVE_HTTP_RESPONSE_HEADER",
                            "CONTROL_ACCESS_USING_HTTP_METHODS",
                            "ALLOW",
                            "HTTP_HEADER",
                            "ADD_HTTP_RESPONSE_HEADER",
                            "EXTEND_HTTP_RESPONSE_HEADER_VALUE",
                        ],
                    ),
                    header=dict(type="str"),
                    prefix=dict(type="str"),
                    suffix=dict(type="str"),
                ),
            ),
            load_balancer_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="rule_set",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
