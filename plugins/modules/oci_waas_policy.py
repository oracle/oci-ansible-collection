#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_waas_policy
short_description: Manage a WaasPolicy resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a WaasPolicy resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Web Application Acceleration and Security (WAAS) policy in the specified compartment. A WAAS policy must be
      established before creating Web Application Firewall (WAF) rules. To use WAF rules, your web application's origin servers must defined in the `WaasPolicy`
      schema.
    - A domain name must be specified when creating a WAAS policy. The domain name should be different from the origins specified in your `WaasPolicy`. Once
      domain name is entered and stored, it is unchangeable.
    - Use the record data returned in the `cname` field of the `WaasPolicy` object to create a CNAME record in your DNS configuration that will direct your
      domain's traffic through the WAF.
    - For the purposes of access control, you must provide the OCID of the compartment where you want the service to reside. For information about access
      control and compartments, see L(Overview of the IAM Service,https://docs.cloud.oracle.com/iaas/Content/Identity/Concepts/overview.htm).
    - You must specify a display name and domain for the WAAS policy. The display name does not have to be unique and can be changed. The domain name should be
      different from every origin specified in `WaasPolicy`.
    - All Oracle Cloud Infrastructure resources, including WAAS policies, receive a unique, Oracle-assigned ID called an Oracle Cloud Identifier (OCID). When a
      resource is created, you can find its OCID in the response. You can also retrieve a resource's OCID by using a list API operation for that resource type,
      or by viewing the resource in the Console. Fore more information, see L(Resource
      Identifiers,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
    - "**Note:** After sending the POST request, the new object's state will temporarily be `CREATING`. Ensure that the resource's state has changed to `ACTIVE`
      before use."
    - "This resource has the following action operations in the M(oracle.oci.oci_waas_policy_actions) module: accept_recommendations, change_compartment,
      purge_cache."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment in which to create the WAAS policy.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - A user-friendly name for the WAAS policy. The name can be changed and does not need to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    domain:
        description:
            - The web application domain that the WAAS policy protects.
            - Required for create using I(state=present).
        type: str
    additional_domains:
        description:
            - An array of additional domains for the specified web application.
            - This parameter is updatable.
        type: list
        elements: str
    origins:
        description:
            - A map of host to origin for the web application. The key should be a customer friendly name for the host, ex. primary, secondary, etc.
            - This parameter is updatable.
        type: dict
        suboptions:
            uri:
                description:
                    - The URI of the origin. Does not support paths. Port numbers should be specified in the `httpPort` and `httpsPort` fields.
                type: str
                required: true
            http_port:
                description:
                    - "The HTTP port on the origin that the web application listens on. If unspecified, defaults to `80`. If `0` is specified - the origin is
                      not used for HTTP traffic."
                type: int
            https_port:
                description:
                    - "The HTTPS port on the origin that the web application listens on. If unspecified, defaults to `443`. If `0` is specified - the origin is
                      not used for HTTPS traffic."
                type: int
            custom_headers:
                description:
                    - A list of HTTP headers to forward to your origin.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - The name of the header.
                        type: str
                        required: true
                    value:
                        description:
                            - The value of the header.
                        type: str
                        required: true
    origin_groups:
        description:
            - The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of
              origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
              To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.
            - This parameter is updatable.
        type: dict
        suboptions:
            origins:
                description:
                    - The list of objects containing origin references and additional properties.
                type: list
                elements: dict
                suboptions:
                    origin:
                        description:
                            - The IP address or CIDR notation of the origin server.
                        type: str
                    weight:
                        description:
                            - The weight of the origin used in load balancing. Origins with higher weights will receive larger proportions of client requests.
                        type: int
    policy_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            certificate_id:
                description:
                    - The OCID of the SSL certificate to use if HTTPS is supported.
                type: str
            is_https_enabled:
                description:
                    - Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.
                type: bool
            is_https_forced:
                description:
                    - Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.
                type: bool
            tls_protocols:
                description:
                    - "A list of allowed TLS protocols. Only applicable when HTTPS support is enabled.
                      The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client
                      browser will be selected. If no such version exists, the connection will be aborted.
                      - **TLS_V1:** corresponds to TLS 1.0 specification."
                    - "- **TLS_V1_1:** corresponds to TLS 1.1 specification."
                    - "- **TLS_V1_2:** corresponds to TLS 1.2 specification."
                    - "- **TLS_V1_3:** corresponds to TLS 1.3 specification."
                    - Enabled TLS protocols must go in a row. For example if `TLS_v1_1` and `TLS_V1_3` are enabled, `TLS_V1_2` must be enabled too.
                type: list
                elements: str
                choices:
                    - "TLS_V1"
                    - "TLS_V1_1"
                    - "TLS_V1_2"
                    - "TLS_V1_3"
            is_origin_compression_enabled:
                description:
                    - "Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise, the
                      empty `Accept-Encoding:` header is used."
                type: bool
            is_behind_cdn:
                description:
                    - Enabling `isBehindCdn` allows for the collection of IP addresses from client requests if the WAF is connected to a CDN.
                type: bool
            client_address_header:
                description:
                    - Specifies an HTTP header name which is treated as the connecting client's IP address. Applicable only if `isBehindCdn` is enabled.
                    - The edge node reads this header and its value and sets the client IP address as specified. It does not create the header if the header is
                      not present in the request. If the header is not present, the connecting IP address will be used as the client's true IP address. It uses
                      the last IP address in the header's value as the true IP address.
                    - "Example: `X-Client-Ip: 11.1.1.1, 13.3.3.3`"
                    - In the case of multiple headers with the same name, only the first header will be used. It is assumed that CDN sets the correct client IP
                      address to prevent spoofing.
                    - "- **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name."
                    - "- **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name."
                    - "- **X_REAL_IP:** Corresponds to `X-Real-Ip` header name."
                    - "- **CLIENT_IP:** Corresponds to `Client-Ip` header name."
                    - "- **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name."
                type: str
                choices:
                    - "X_FORWARDED_FOR"
                    - "X_CLIENT_IP"
                    - "X_REAL_IP"
                    - "CLIENT_IP"
                    - "TRUE_CLIENT_IP"
            is_cache_control_respected:
                description:
                    - "Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a
                      proxy cache. Caching is usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned
                      resource is valid for 120 seconds. Caching rules will overwrite this setting."
                type: bool
            is_response_buffering_enabled:
                description:
                    - Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly
                      increases Time To First Byte.
                type: bool
            cipher_group:
                description:
                    - "The set cipher group for the configured TLS protocol. This sets the configuration for the TLS connections between clients and edge nodes
                      only.
                      - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-
                        AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-
                        DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-
                        RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-
                        DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-
                        SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-
                        CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`"
                type: str
                choices:
                    - "DEFAULT"
            load_balancing_method:
                description:
                    - An object that represents a load balancing method and its properties.
                type: dict
                suboptions:
                    method:
                        description:
                            - Load balancing methods are algorithms used to efficiently distribute traffic among origin servers.
                            - "- **L(IP_HASH,https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/IPHashLoadBalancingMethod):** All the incoming
                              requests from the same client IP address should go to the same content origination server. IP_HASH load balancing method uses
                              origin weights when choosing which origin should the hash be assigned to initially."
                            - "- **L(ROUND_ROBIN,https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/RoundRobinLoadBalancingMethod):** Forwards
                              requests sequentially to the available origin servers. The first request - to the first origin server, the second request - to the
                              next origin server, and so on. After it sends a request to the last origin server, it starts again with the first origin server.
                              When using weights on origins, Weighted Round Robin assigns more requests to origins with a greater weight. Over a period of time,
                              origins will receive a number of requests in proportion to their weight."
                            - "- **L(STICKY_COOKIE,https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/StickyCookieLoadBalancingMethod):** Adds a
                              session cookie to the first response from the origin server and identifies the server that sent the response. The client's next
                              request contains the cookie value, and nginx routes the request to the origin server that responded to the first request.
                              STICKY_COOKIE load balancing method falls back to Round Robin for the first request."
                        type: str
                        choices:
                            - "ROUND_ROBIN"
                            - "STICKY_COOKIE"
                            - "IP_HASH"
                        required: true
                    name:
                        description:
                            - The name of the cookie used to track the persistence.
                              Can contain any US-ASCII character except separator or control character.
                            - Applicable when method is 'STICKY_COOKIE'
                        type: str
                    domain:
                        description:
                            - The domain for which the cookie is set, defaults to WAAS policy domain.
                            - Applicable when method is 'STICKY_COOKIE'
                        type: str
                    expiration_time_in_seconds:
                        description:
                            - The time for which a browser should keep the cookie in seconds.
                              Empty value will cause the cookie to expire at the end of a browser session.
                            - Applicable when method is 'STICKY_COOKIE'
                        type: int
            websocket_path_prefixes:
                description:
                    - ModSecurity is not capable to inspect WebSockets. Therefore paths specified here have WAF disabled if Connection request header from the
                      client has the value Upgrade (case insensitive matching) and Upgrade request header has the value websocket (case insensitive matching).
                      Paths matches if the concatenation of request URL path and query starts with the contents of the one of `websocketPathPrefixes` array
                      value. In All other cases challenges, like JSC, HIC and etc., remain active.
                type: list
                elements: str
            is_sni_enabled:
                description:
                    - SNI stands for Server Name Indication and is an extension of the TLS protocol. It indicates which hostname is being contacted by the
                      browser at the beginning of the 'handshake'-process. This allows a server to connect multiple SSL Certificates to one IP address and port.
                type: bool
            health_checks:
                description:
                    - ""
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the health checks.
                        type: bool
                    method:
                        description:
                            - An HTTP verb (i.e. HEAD, GET, or POST) to use when performing the health check.
                        type: str
                        choices:
                            - "GET"
                            - "HEAD"
                            - "POST"
                    path:
                        description:
                            - Path to visit on your origins when performing the health check.
                        type: str
                    headers:
                        description:
                            - "HTTP header fields to include in health check requests, expressed as `\\"name\\": \\"value\\"` properties. Because HTTP header
                              field names are case-insensitive, any use of names that are case-insensitive equal to other names will be rejected. If Host is not
                              specified, requests will include a Host header field with value matching the policy's protected domain. If User-Agent is not
                              specified, requests will include a User-Agent header field with value \\"waf health checks\\"."
                            - "**Note:** The only currently-supported header fields are Host and User-Agent."
                        type: dict
                    expected_response_code_group:
                        description:
                            - "The HTTP response codes that signify a healthy state.
                              - **2XX:** Success response code group.
                              - **3XX:** Redirection response code group.
                              - **4XX:** Client errors response code group.
                              - **5XX:** Server errors response code group."
                        type: list
                        elements: str
                        choices:
                            - "2XX"
                            - "3XX"
                            - "4XX"
                            - "5XX"
                    is_response_text_check_enabled:
                        description:
                            - Enables or disables additional check for predefined text in addition to response code.
                        type: bool
                    expected_response_text:
                        description:
                            - Health check will search for the given text in a case-sensitive manner within the response body and will fail if the text is not
                              found.
                        type: str
                    interval_in_seconds:
                        description:
                            - Time between health checks of an individual origin server, in seconds.
                        type: int
                    timeout_in_seconds:
                        description:
                            - Response timeout represents wait time until request is considered failed, in seconds.
                        type: int
                    healthy_threshold:
                        description:
                            - Number of successful health checks after which the server is marked up.
                        type: int
                    unhealthy_threshold:
                        description:
                            - Number of failed health checks after which the server is marked down.
                        type: int
    waf_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            access_rules:
                description:
                    - The access rules applied to the Web Application Firewall. Access rules allow custom content access policies to be defined and `ALLOW`,
                      `DETECT`, or `BLOCK` actions to be taken on a request when specified criteria are met.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - The unique name of the access rule.
                        type: str
                        required: true
                    criteria:
                        description:
                            - The list of access rule criteria. The rule would be applied only for the requests that matched all the listed conditions.
                        type: list
                        elements: dict
                        required: true
                        suboptions:
                            condition:
                                description:
                                    - "The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
                                      - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value`
                                        field. URL must start with a `/`.
                                      - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the
                                        `value` field. URL must start with a `/`.
                                      - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value`
                                        field. URL must start with a `/`.
                                      - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value`
                                        field.
                                      - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value`
                                        field.
                                      - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the
                                        value field. The value must be a valid regular expression recognized by the PCRE library in Nginx
                                        (https://www.pcre.org).
                                      - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular
                                        expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx
                                        (https://www.pcre.org).
                                      - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents
                                        of the `value` field.
                                      - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents
                                        of the `value` field.
                                      - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the
                                        contents of the `value` field.
                                      - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The
                                        `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                                      *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                                      - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address
                                        list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                                      *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                                      - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list.
                                        The `value` in this case is OCID of the address list.
                                      - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address
                                        list. The `value` field in this case is OCID of the address list.
                                      - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a
                                        header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is
                                        the header field name and `test.example.com` is the header field value. A request matches when the header field name is
                                        a case insensitive match and the header field value is a case insensitive, substring match.
                                      *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com`
                                      is the value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a
                                      request with header values of `host: www.example.com` or `host: test.sub.example.com` will not match.
                                      - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this
                                        case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available methods:
                                        `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                                    - "*Example:* \\"GET\\\\nPOST\\""
                                    - "- **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The
                                      `value` in this case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available
                                      methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                                    - "*Example:* \\"GET\\\\nPOST\\""
                                    - "- **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this case
                                      is string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1 alpha-2
                                      format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                      *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                                      - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The `value` in
                                        this case is string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1
                                        alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                      *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                                      - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field.
                                      *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
                                      - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
                                      *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`"
                                type: str
                                choices:
                                    - "URL_IS"
                                    - "URL_IS_NOT"
                                    - "URL_STARTS_WITH"
                                    - "URL_PART_ENDS_WITH"
                                    - "URL_PART_CONTAINS"
                                    - "URL_REGEX"
                                    - "URL_DOES_NOT_MATCH_REGEX"
                                    - "URL_DOES_NOT_START_WITH"
                                    - "URL_PART_DOES_NOT_CONTAIN"
                                    - "URL_PART_DOES_NOT_END_WITH"
                                    - "IP_IS"
                                    - "IP_IS_NOT"
                                    - "IP_IN_LIST"
                                    - "IP_NOT_IN_LIST"
                                    - "HTTP_HEADER_CONTAINS"
                                    - "HTTP_METHOD_IS"
                                    - "HTTP_METHOD_IS_NOT"
                                    - "COUNTRY_IS"
                                    - "COUNTRY_IS_NOT"
                                    - "USER_AGENT_IS"
                                    - "USER_AGENT_IS_NOT"
                                required: true
                            value:
                                description:
                                    - The criteria value.
                                type: str
                                required: true
                            is_case_sensitive:
                                description:
                                    - When enabled, the condition will be matched with case-sensitive rules.
                                type: bool
                    action:
                        description:
                            - The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.
                            - "- **ALLOW:** Takes no action, just logs the request."
                            - "- **DETECT:** Takes no action, but creates an alert for the request."
                            - "- **BLOCK:** Blocks the request by returning specified response code or showing error page."
                            - "- **BYPASS:** Bypasses some or all challenges."
                            - "- **REDIRECT:** Redirects the request to the specified URL. These fields are required when `REDIRECT` is selected: `redirectUrl`,
                              `redirectResponseCode`."
                            - "- **SHOW_CAPTCHA:** Show a CAPTCHA Challenge page instead of the requested page."
                            - Regardless of action, no further rules are processed once a rule is matched.
                        type: str
                        choices:
                            - "ALLOW"
                            - "DETECT"
                            - "BLOCK"
                            - "BYPASS"
                            - "REDIRECT"
                            - "SHOW_CAPTCHA"
                        required: true
                    block_action:
                        description:
                            - The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to
                              `SET_RESPONSE_CODE`.
                        type: str
                        choices:
                            - "SET_RESPONSE_CODE"
                            - "SHOW_ERROR_PAGE"
                    block_response_code:
                        description:
                            - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the access
                              criteria are met. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`, `206`,
                              `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`,
                              `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`."
                        type: int
                    block_error_page_message:
                        description:
                            - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the access
                              criteria are met. If unspecified, defaults to 'Access to the website is blocked.'
                        type: str
                    block_error_page_code:
                        description:
                            - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                              access criteria are met. If unspecified, defaults to 'Access rules'.
                        type: str
                    block_error_page_description:
                        description:
                            - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                              access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'
                        type: str
                    bypass_challenges:
                        description:
                            - The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed.
                            - "- **JS_CHALLENGE:** Bypasses JavaScript Challenge."
                            - "- **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge."
                            - "- **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge."
                            - "- **CAPTCHA:** Bypasses CAPTCHA Challenge."
                        type: list
                        elements: str
                        choices:
                            - "JS_CHALLENGE"
                            - "DEVICE_FINGERPRINT_CHALLENGE"
                            - "HUMAN_INTERACTION_CHALLENGE"
                            - "CAPTCHA"
                    redirect_url:
                        description:
                            - The target to which the request should be redirected, represented as a URI reference. Required when `action` is `REDIRECT`.
                        type: str
                    redirect_response_code:
                        description:
                            - The response status code to return when `action` is set to `REDIRECT`.
                            - "- **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301)."
                            - "- **FOUND:** Used for designating the temporary movement of a page (numerical code - 302)."
                        type: str
                        choices:
                            - "MOVED_PERMANENTLY"
                            - "FOUND"
                    captcha_title:
                        description:
                            - The title used when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
                        type: str
                    captcha_header:
                        description:
                            - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is
                              challenged.
                        type: str
                    captcha_footer:
                        description:
                            - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is
                              challenged.
                        type: str
                    captcha_submit_label:
                        description:
                            - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `SHOW_CAPTCHA` and the request is
                              challenged.
                        type: str
                    response_header_manipulation:
                        description:
                            - An object that represents an action to apply to an HTTP response headers if all rule criteria will be matched regardless of
                              `action` value.
                        type: list
                        elements: dict
                        suboptions:
                            action:
                                description:
                                    - ""
                                type: str
                                choices:
                                    - "EXTEND_HTTP_RESPONSE_HEADER"
                                    - "ADD_HTTP_RESPONSE_HEADER"
                                    - "REMOVE_HTTP_RESPONSE_HEADER"
                                required: true
                            header:
                                description:
                                    - A header field name that conforms to RFC 7230.
                                    - "Example: `example_header_name`"
                                type: str
                                required: true
                            value:
                                description:
                                    - A header field value that conforms to RFC 7230.
                                    - "Example: `example_value`"
                                    - Required when action is one of ['ADD_HTTP_RESPONSE_HEADER', 'EXTEND_HTTP_RESPONSE_HEADER']
                                type: str
            address_rate_limiting:
                description:
                    - The settings used to limit the number of requests from an IP address.
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the address rate limiting Web Application Firewall feature.
                        type: bool
                        required: true
                    allowed_rate_per_address:
                        description:
                            - The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.
                        type: int
                    max_delayed_count_per_address:
                        description:
                            - The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.
                        type: int
                    block_response_code:
                        description:
                            - "The response status code returned when a request is blocked. If unspecified, defaults to `503`. The list of available response
                              codes: `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `494`, `495`, `496`,
                              `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`."
                        type: int
            captchas:
                description:
                    - A list of CAPTCHA challenge settings. CAPTCHAs challenge requests to ensure a human is attempting to reach the specified URL and not a
                      bot.
                type: list
                elements: dict
                suboptions:
                    url:
                        description:
                            - The unique URL path at which to show the CAPTCHA challenge.
                        type: str
                        required: true
                    session_expiration_in_seconds:
                        description:
                            - The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.
                        type: int
                        required: true
                    title:
                        description:
                            - The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`
                        type: str
                        required: true
                    header_text:
                        description:
                            - The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased number
                              of attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by entering the
                              text from the image below.'
                        type: str
                    footer_text:
                        description:
                            - The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as
                              they are shown in the image above.'
                        type: str
                    failure_message:
                        description:
                            - The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`
                        type: str
                        required: true
                    submit_label:
                        description:
                            - The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.
                        type: str
                        required: true
            device_fingerprint_challenge:
                description:
                    - The device fingerprint challenge settings. Blocks bots based on unique device fingerprint information.
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the device fingerprint challenge Web Application Firewall feature.
                        type: bool
                        required: true
                    action:
                        description:
                            - The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.
                        type: str
                        choices:
                            - "DETECT"
                            - "BLOCK"
                    failure_threshold:
                        description:
                            - The number of failed requests allowed before taking action. If unspecified, defaults to `10`.
                        type: int
                    action_expiration_in_seconds:
                        description:
                            - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
                        type: int
                    failure_threshold_expiration_in_seconds:
                        description:
                            - The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.
                        type: int
                    max_address_count:
                        description:
                            - The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.
                        type: int
                    max_address_count_expiration_in_seconds:
                        description:
                            - The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.
                        type: int
                    challenge_settings:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            block_action:
                                description:
                                    - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                      `SHOW_ERROR_PAGE`.
                                type: str
                                choices:
                                    - "SET_RESPONSE_CODE"
                                    - "SHOW_ERROR_PAGE"
                                    - "SHOW_CAPTCHA"
                            block_response_code:
                                description:
                                    - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                      `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes:
                                      `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`,
                                      `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`,
                                      `503`, `504`, `507`."
                                type: int
                            block_error_page_message:
                                description:
                                    - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                      request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                type: str
                            block_error_page_description:
                                description:
                                    - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`,
                                      and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                                type: str
                            block_error_page_code:
                                description:
                                    - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and
                                      the request is blocked. If unspecified, defaults to `403`.
                                type: str
                            captcha_title:
                                description:
                                    - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`,
                                      and the request is blocked. If unspecified, defaults to `Are you human?`
                                type: str
                            captcha_header:
                                description:
                                    - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts
                                      to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the
                                      text from captcha below.`
                                type: str
                            captcha_footer:
                                description:
                                    - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in
                                      image above`.
                                type: str
                            captcha_submit_label:
                                description:
                                    - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set
                                      to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                type: str
            human_interaction_challenge:
                description:
                    - The human interaction challenge settings. Detects natural human interactions such as mouse movements, time on site, and page scrolling to
                      identify bots.
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the human interaction challenge Web Application Firewall feature.
                        type: bool
                        required: true
                    action:
                        description:
                            - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
                        type: str
                        choices:
                            - "DETECT"
                            - "BLOCK"
                    failure_threshold:
                        description:
                            - The number of failed requests before taking action. If unspecified, defaults to `10`.
                        type: int
                    action_expiration_in_seconds:
                        description:
                            - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
                        type: int
                    failure_threshold_expiration_in_seconds:
                        description:
                            - The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.
                        type: int
                    interaction_threshold:
                        description:
                            - The number of interactions required to pass the challenge. If unspecified, defaults to `3`.
                        type: int
                    recording_period_in_seconds:
                        description:
                            - The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.
                        type: int
                    set_http_header:
                        description:
                            - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the
                              `action` is set to `DETECT`.
                        type: dict
                        suboptions:
                            name:
                                description:
                                    - The name of the header.
                                type: str
                                required: true
                            value:
                                description:
                                    - The value of the header.
                                type: str
                                required: true
                    challenge_settings:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            block_action:
                                description:
                                    - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                      `SHOW_ERROR_PAGE`.
                                type: str
                                choices:
                                    - "SET_RESPONSE_CODE"
                                    - "SHOW_ERROR_PAGE"
                                    - "SHOW_CAPTCHA"
                            block_response_code:
                                description:
                                    - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                      `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes:
                                      `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`,
                                      `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`,
                                      `503`, `504`, `507`."
                                type: int
                            block_error_page_message:
                                description:
                                    - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                      request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                type: str
                            block_error_page_description:
                                description:
                                    - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`,
                                      and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                                type: str
                            block_error_page_code:
                                description:
                                    - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and
                                      the request is blocked. If unspecified, defaults to `403`.
                                type: str
                            captcha_title:
                                description:
                                    - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`,
                                      and the request is blocked. If unspecified, defaults to `Are you human?`
                                type: str
                            captcha_header:
                                description:
                                    - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts
                                      to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the
                                      text from captcha below.`
                                type: str
                            captcha_footer:
                                description:
                                    - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in
                                      image above`.
                                type: str
                            captcha_submit_label:
                                description:
                                    - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set
                                      to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                type: str
                    is_nat_enabled:
                        description:
                            - When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking
                              visitors with shared IP addresses.
                        type: bool
            js_challenge:
                description:
                    - The JavaScript challenge settings. Blocks bots by challenging requests from browsers that have no JavaScript support.
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Enables or disables the JavaScript challenge Web Application Firewall feature.
                        type: bool
                        required: true
                    action:
                        description:
                            - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
                        type: str
                        choices:
                            - "DETECT"
                            - "BLOCK"
                    failure_threshold:
                        description:
                            - The number of failed requests before taking action. If unspecified, defaults to `10`.
                        type: int
                    action_expiration_in_seconds:
                        description:
                            - The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.
                        type: int
                    set_http_header:
                        description:
                            - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the
                              `action` is set to `DETECT`.
                        type: dict
                        suboptions:
                            name:
                                description:
                                    - The name of the header.
                                type: str
                                required: true
                            value:
                                description:
                                    - The value of the header.
                                type: str
                                required: true
                    challenge_settings:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            block_action:
                                description:
                                    - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                      `SHOW_ERROR_PAGE`.
                                type: str
                                choices:
                                    - "SET_RESPONSE_CODE"
                                    - "SHOW_ERROR_PAGE"
                                    - "SHOW_CAPTCHA"
                            block_response_code:
                                description:
                                    - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                      `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response codes:
                                      `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`,
                                      `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`,
                                      `503`, `504`, `507`."
                                type: int
                            block_error_page_message:
                                description:
                                    - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                      request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                type: str
                            block_error_page_description:
                                description:
                                    - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`,
                                      and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please contact support.`
                                type: str
                            block_error_page_code:
                                description:
                                    - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE` and
                                      the request is blocked. If unspecified, defaults to `403`.
                                type: str
                            captcha_title:
                                description:
                                    - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_CAPTCHA`,
                                      and the request is blocked. If unspecified, defaults to `Are you human?`
                                type: str
                            captcha_header:
                                description:
                                    - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of attempts
                                      to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by entering the
                                      text from captcha below.`
                                type: str
                            captcha_footer:
                                description:
                                    - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                      `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are shown in
                                      image above`.
                                type: str
                            captcha_submit_label:
                                description:
                                    - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is set
                                      to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                type: str
                    are_redirects_challenged:
                        description:
                            - When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin to
                              HTTP 200 with an HTML body containing JavaScript page redirection.
                        type: bool
                    criteria:
                        description:
                            - When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.
                        type: list
                        elements: dict
                        suboptions:
                            condition:
                                description:
                                    - "The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
                                      - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value`
                                        field. URL must start with a `/`.
                                      - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the
                                        `value` field. URL must start with a `/`.
                                      - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value`
                                        field. URL must start with a `/`.
                                      - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the `value`
                                        field.
                                      - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value`
                                        field.
                                      - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in the
                                        value field. The value must be a valid regular expression recognized by the PCRE library in Nginx
                                        (https://www.pcre.org).
                                      - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the regular
                                        expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library in Nginx
                                        (https://www.pcre.org).
                                      - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the contents
                                        of the `value` field.
                                      - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the contents
                                        of the `value` field.
                                      - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the
                                        contents of the `value` field.
                                      - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The
                                        `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                                      *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                                      - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined address
                                        list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                                      *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                                      - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address list.
                                        The `value` in this case is OCID of the address list.
                                      - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced address
                                        list. The `value` field in this case is OCID of the address list.
                                      - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon: a
                                        header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host` is
                                        the header field name and `test.example.com` is the header field value. A request matches when the header field name is
                                        a case insensitive match and the header field value is a case insensitive, substring match.
                                      *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and `test.example.com`
                                      is the value of the host field, a request with the header values, `Host: www.test.example.com` will match, where as a
                                      request with header values of `host: www.example.com` or `host: test.sub.example.com` will not match.
                                      - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in this
                                        case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available methods:
                                        `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                                    - "*Example:* \\"GET\\\\nPOST\\""
                                    - "- **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The
                                      `value` in this case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available
                                      methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                                    - "*Example:* \\"GET\\\\nPOST\\""
                                    - "- **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this case
                                      is string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1 alpha-2
                                      format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                      *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                                      - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The `value` in
                                        this case is string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1
                                        alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                      *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                                      - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field.
                                      *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
                                      - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
                                      *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`"
                                type: str
                                choices:
                                    - "URL_IS"
                                    - "URL_IS_NOT"
                                    - "URL_STARTS_WITH"
                                    - "URL_PART_ENDS_WITH"
                                    - "URL_PART_CONTAINS"
                                    - "URL_REGEX"
                                    - "URL_DOES_NOT_MATCH_REGEX"
                                    - "URL_DOES_NOT_START_WITH"
                                    - "URL_PART_DOES_NOT_CONTAIN"
                                    - "URL_PART_DOES_NOT_END_WITH"
                                    - "IP_IS"
                                    - "IP_IS_NOT"
                                    - "IP_IN_LIST"
                                    - "IP_NOT_IN_LIST"
                                    - "HTTP_HEADER_CONTAINS"
                                    - "HTTP_METHOD_IS"
                                    - "HTTP_METHOD_IS_NOT"
                                    - "COUNTRY_IS"
                                    - "COUNTRY_IS_NOT"
                                    - "USER_AGENT_IS"
                                    - "USER_AGENT_IS_NOT"
                                required: true
                            value:
                                description:
                                    - The criteria value.
                                type: str
                                required: true
                            is_case_sensitive:
                                description:
                                    - When enabled, the condition will be matched with case-sensitive rules.
                                type: bool
                    is_nat_enabled:
                        description:
                            - When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking
                              visitors with shared IP addresses.
                        type: bool
            origin:
                description:
                    - The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in
                      `Origins`. Required when creating the `WafConfig` resource, but is not required upon updating the configuration.
                    - This parameter is updatable.
                type: str
            caching_rules:
                description:
                    - A list of caching rules applied to the web application.
                type: list
                elements: dict
                suboptions:
                    key:
                        description:
                            - The unique key for the caching rule.
                        type: str
                    name:
                        description:
                            - The name of the caching rule.
                        type: str
                        required: true
                    action:
                        description:
                            - "The action to take when the criteria of a caching rule are met.
                              - **CACHE:** Caches requested content when the criteria of the rule are met."
                            - "- **BYPASS_CACHE:** Allows requests to bypass the cache and be directed to the origin when the criteria of the rule is met."
                        type: str
                        choices:
                            - "CACHE"
                            - "BYPASS_CACHE"
                        required: true
                    caching_duration:
                        description:
                            - "The duration to cache content for the caching rule, specified in ISO 8601 extended format. Supported units: seconds, minutes,
                              hours, days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported.
                              Only applies when the `action` is set to `CACHE`.
                              Example: `PT1H`"
                        type: str
                    is_client_caching_enabled:
                        description:
                            - Enables or disables client caching.
                              Browsers use the `Cache-Control` header value for caching content locally in the browser. This setting overrides the addition of a
                              `Cache-Control` header in responses.
                        type: bool
                    client_caching_duration:
                        description:
                            - "The duration to cache content in the user's browser, specified in ISO 8601 extended format. Supported units: seconds, minutes,
                              hours, days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported.
                              Only applies when the `action` is set to `CACHE`.
                              Example: `PT1H`"
                        type: str
                    criteria:
                        description:
                            - The array of the rule criteria with condition and value. The caching rule would be applied for the requests that matched any of
                              the listed conditions.
                        type: list
                        elements: dict
                        required: true
                        suboptions:
                            condition:
                                description:
                                    - "The condition of the caching rule criteria.
                                      - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value`
                                        field."
                                    - "- **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the `value`
                                      field."
                                    - "- **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the
                                      `value` field."
                                    - "- **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the `value`
                                      field."
                                    - URLs must start with a `/`. URLs can't contain restricted double slashes `//`. URLs can't contain the restricted `'` `&`
                                      `?` symbols. Resources to cache can only be specified by a URL, any query parameters are ignored.
                                type: str
                                choices:
                                    - "URL_IS"
                                    - "URL_STARTS_WITH"
                                    - "URL_PART_ENDS_WITH"
                                    - "URL_PART_CONTAINS"
                                required: true
                            value:
                                description:
                                    - The value of the caching rule criteria.
                                type: str
                                required: true
            custom_protection_rules:
                description:
                    - A list of the custom protection rule OCIDs and their actions.
                type: list
                elements: dict
                suboptions:
                    id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule.
                        type: str
                    action:
                        description:
                            - "The action to take when the custom protection rule is triggered.
                              `DETECT` - Logs the request when the criteria of the custom protection rule are met. `BLOCK` - Blocks the request when the
                              criteria of the custom protection rule are met."
                        type: str
                        choices:
                            - "DETECT"
                            - "BLOCK"
                    exclusions:
                        description:
                            - ""
                        type: list
                        elements: dict
                        suboptions:
                            target:
                                description:
                                    - The target of the exclusion.
                                type: str
                                choices:
                                    - "REQUEST_COOKIES"
                                    - "REQUEST_COOKIE_NAMES"
                                    - "ARGS"
                                    - "ARGS_NAMES"
                            exclusions:
                                description:
                                    - ""
                                type: list
                                elements: str
            origin_groups:
                description:
                    - The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups
                      of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
                      To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.
                    - This parameter is updatable.
                type: list
                elements: str
            protection_settings:
                description:
                    - The settings applied to protection rules.
                type: dict
                suboptions:
                    block_action:
                        description:
                            - If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If
                              unspecified, defaults to `SET_RESPONSE_CODE`.
                        type: str
                        choices:
                            - "SHOW_ERROR_PAGE"
                            - "SET_RESPONSE_CODE"
                    block_response_code:
                        description:
                            - "The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is
                              detected as malicious by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`, `401`,
                              `403`, `405`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`."
                        type: int
                    block_error_page_message:
                        description:
                            - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the traffic
                              is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'
                        type: str
                    block_error_page_code:
                        description:
                            - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                              traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.
                        type: str
                    block_error_page_description:
                        description:
                            - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                              traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner. Please
                              contact support.`
                        type: str
                    max_argument_count:
                        description:
                            - "The maximum number of arguments allowed to be passed to your application before an action is taken. Arguements are query
                              parameters or body parameters in a PUT or POST request. If unspecified, defaults to `255`. This setting only applies if a
                              corresponding protection rule is enabled, such as the \\"Number of Arguments Limits\\" rule (key: 960335)."
                            - "Example: If `maxArgumentCount` to `2` for the Max Number of Arguments protection rule (key: 960335), the following requests would
                              be blocked:
                              `GET /myapp/path?query=one&query=two&query=three`
                              `POST /myapp/path` with Body `{\\"argument1\\":\\"one\\",\\"argument2\\":\\"two\\",\\"argument3\\":\\"three\\"}`"
                        type: int
                    max_name_length_per_argument:
                        description:
                            - "The maximum length allowed for each argument name, in characters. Arguements are query parameters or body parameters in a PUT or
                              POST request. If unspecified, defaults to `400`. This setting only applies if a corresponding protection rule is enabled, such as
                              the \\"Values Limits\\" rule (key: 960208)."
                        type: int
                    max_total_name_length_of_arguments:
                        description:
                            - "The maximum length allowed for the sum of the argument name and value, in characters. Arguements are query parameters or body
                              parameters in a PUT or POST request. If unspecified, defaults to `64000`. This setting only applies if a corresponding protection
                              rule is enabled, such as the \\"Total Arguments Limits\\" rule (key: 960341)."
                        type: int
                    recommendations_period_in_days:
                        description:
                            - The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If
                              unspecified, defaults to `10`.
                            - Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.
                        type: int
                    is_response_inspected:
                        description:
                            - Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to
                              `false`.
                            - "**Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected."
                        type: bool
                    max_response_size_in_ki_b:
                        description:
                            - The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially inspected.
                              If unspecified, defaults to `1024`.
                        type: int
                    allowed_http_methods:
                        description:
                            - "The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a
                              corresponding protection rule is enabled, such as the \\"Restrict HTTP Request Methods\\" rule (key: 911100)."
                        type: list
                        elements: str
                        choices:
                            - "OPTIONS"
                            - "GET"
                            - "HEAD"
                            - "POST"
                            - "PUT"
                            - "DELETE"
                            - "TRACE"
                            - "CONNECT"
                            - "PATCH"
                            - "PROPFIND"
                    media_types:
                        description:
                            - "The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this list
                              will be inspected. If unspecified, defaults to `[\\"text/html\\", \\"text/plain\\", \\"text/xml\\"]`."
                            - "   Supported MIME types include:"
                            - "   - text/html
                                  - text/plain
                                  - text/asp
                                  - text/css
                                  - text/x-script
                                  - application/json
                                  - text/webviewhtml
                                  - text/x-java-source
                                  - application/x-javascript
                                  - application/javascript
                                  - application/ecmascript
                                  - text/javascript
                                  - text/ecmascript
                                  - text/x-script.perl
                                  - text/x-script.phyton
                                  - application/plain
                                  - application/xml
                                  - text/xml"
                        type: list
                        elements: str
            whitelists:
                description:
                    - A list of IP addresses that bypass the Web Application Firewall.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - The unique name of the whitelist.
                        type: str
                        required: true
                    addresses:
                        description:
                            - A set of IP addresses or CIDR notations to include in the whitelist.
                        type: list
                        elements: str
                    address_lists:
                        description:
                            - A list of L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of IP address lists to include in the
                              whitelist.
                        type: list
                        elements: str
            good_bots:
                description:
                    - A list of bots allowed to access the web application.
                type: list
                elements: dict
                suboptions:
                    key:
                        description:
                            - The unique key for the bot.
                            - This parameter is updatable.
                        type: str
                        required: true
                    name:
                        description:
                            - The bot name.
                            - This parameter is updatable.
                        type: str
                    is_enabled:
                        description:
                            - Enables or disables the bot.
                            - This parameter is updatable.
                        type: bool
                        required: true
                    description:
                        description:
                            - The description of the bot.
                            - This parameter is updatable.
                        type: str
            protection_rules:
                description:
                    - A list of the protection rules and their details.
                type: list
                elements: dict
                suboptions:
                    key:
                        description:
                            - The unique key of the protection rule.
                            - This parameter is updatable.
                        type: str
                    mod_security_rule_ids:
                        description:
                            - The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source WAF
                              rules, see L(Mod Security's documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
                            - This parameter is updatable.
                        type: list
                        elements: str
                    name:
                        description:
                            - The name of the protection rule.
                            - This parameter is updatable.
                        type: str
                    description:
                        description:
                            - The description of the protection rule.
                            - This parameter is updatable.
                        type: str
                    action:
                        description:
                            - The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "OFF"
                            - "DETECT"
                            - "BLOCK"
                    labels:
                        description:
                            - The list of labels for the protection rule.
                            - "**Note:** Protection rules with a `ResponseBody` label will have no effect unless `isResponseInspected` is true."
                            - This parameter is updatable.
                        type: list
                        elements: str
                    exclusions:
                        description:
                            - ""
                        type: list
                        elements: dict
                        suboptions:
                            target:
                                description:
                                    - The target of the exclusion.
                                    - This parameter is updatable.
                                type: str
                                choices:
                                    - "REQUEST_COOKIES"
                                    - "REQUEST_COOKIE_NAMES"
                                    - "ARGS"
                                    - "ARGS_NAMES"
                            exclusions:
                                description:
                                    - ""
                                    - This parameter is updatable.
                                type: list
                                elements: str
            threat_feeds:
                description:
                    - A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.
                type: list
                elements: dict
                suboptions:
                    key:
                        description:
                            - The unique key of the threat intelligence feed.
                            - This parameter is updatable.
                        type: str
                    name:
                        description:
                            - The name of the threat intelligence feed.
                            - This parameter is updatable.
                        type: str
                    action:
                        description:
                            - The action to take when traffic is flagged as malicious by data from the threat intelligence feed. If unspecified, defaults to
                              `OFF`.
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "OFF"
                            - "DETECT"
                            - "BLOCK"
                    description:
                        description:
                            - The description of the threat intelligence feed.
                            - This parameter is updatable.
                        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the WaasPolicy.
            - Use I(state=present) to create or update a WaasPolicy.
            - Use I(state=absent) to delete a WaasPolicy.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create waas_policy
  oci_waas_policy:
    # required
    compartment_id: "ocid1.compartment.oc1.."
    domain: example.com

    # optional
    display_name: Policy
    additional_domains: [ "null" ]
    origins:
      # required
      uri: uri_example

      # optional
      http_port: 56
      https_port: 56
      custom_headers:
      - # required
        name: name_example
        value: value_example
    origin_groups:
      # optional
      origins:
      - # optional
        origin: origin_example
        weight: 56
    policy_config:
      # optional
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
      is_https_enabled: true
      is_https_forced: true
      tls_protocols: [ "null" ]
      is_origin_compression_enabled: true
      is_behind_cdn: true
      client_address_header: "X-Client-Ip: 11.1.1.1, 13.3.3.3"
      is_cache_control_respected: true
      is_response_buffering_enabled: true
      cipher_group: DEFAULT
      load_balancing_method:
        # required
        method: ROUND_ROBIN
      websocket_path_prefixes: [ "null" ]
      is_sni_enabled: true
      health_checks:
        # optional
        is_enabled: true
        method: GET
        path: path_example
        headers: null
        expected_response_code_group: [ "null" ]
        is_response_text_check_enabled: true
        expected_response_text: expected_response_text_example
        interval_in_seconds: 56
        timeout_in_seconds: 56
        healthy_threshold: 56
        unhealthy_threshold: 56
    waf_config:
      # optional
      access_rules:
      - # required
        name: name_example
        criteria:
        - # required
          condition: URL_IS
          value: value_example

          # optional
          is_case_sensitive: true
        action: ALLOW

        # optional
        block_action: SET_RESPONSE_CODE
        block_response_code: 56
        block_error_page_message: block_error_page_message_example
        block_error_page_code: block_error_page_code_example
        block_error_page_description: block_error_page_description_example
        bypass_challenges: [ "null" ]
        redirect_url: redirect_url_example
        redirect_response_code: MOVED_PERMANENTLY
        captcha_title: captcha_title_example
        captcha_header: captcha_header_example
        captcha_footer: captcha_footer_example
        captcha_submit_label: captcha_submit_label_example
        response_header_manipulation:
        - # required
          action: EXTEND_HTTP_RESPONSE_HEADER
          header: example_header_name
          value: example_value
      address_rate_limiting:
        # required
        is_enabled: true

        # optional
        allowed_rate_per_address: 56
        max_delayed_count_per_address: 56
        block_response_code: 56
      captchas:
      - # required
        url: url_example
        session_expiration_in_seconds: 56
        title: title_example
        failure_message: failure_message_example
        submit_label: submit_label_example

        # optional
        header_text: header_text_example
        footer_text: footer_text_example
      device_fingerprint_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        failure_threshold_expiration_in_seconds: 56
        max_address_count: 56
        max_address_count_expiration_in_seconds: 56
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
      human_interaction_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        failure_threshold_expiration_in_seconds: 56
        interaction_threshold: 56
        recording_period_in_seconds: 56
        set_http_header:
          # required
          name: name_example
          value: value_example
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
        is_nat_enabled: true
      js_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        set_http_header:
          # required
          name: name_example
          value: value_example
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
        are_redirects_challenged: true
        criteria:
        - # required
          condition: URL_IS
          value: value_example

          # optional
          is_case_sensitive: true
        is_nat_enabled: true
      origin: origin_example
      caching_rules:
      - # required
        name: name_example
        action: CACHE
        criteria:
        - # required
          condition: URL_IS
          value: value_example

        # optional
        key: key_example
        caching_duration: PT1H
        is_client_caching_enabled: true
        client_caching_duration: PT1H
      custom_protection_rules:
      - # optional
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        action: DETECT
        exclusions:
        - # optional
          target: REQUEST_COOKIES
          exclusions: [ "null" ]
      origin_groups: [ "null" ]
      protection_settings:
        # optional
        block_action: SHOW_ERROR_PAGE
        block_response_code: 56
        block_error_page_message: block_error_page_message_example
        block_error_page_code: block_error_page_code_example
        block_error_page_description: block_error_page_description_example
        max_argument_count: 56
        max_name_length_per_argument: 56
        max_total_name_length_of_arguments: 56
        recommendations_period_in_days: 56
        is_response_inspected: true
        max_response_size_in_ki_b: 56
        allowed_http_methods: [ "null" ]
        media_types: [ "null" ]
      whitelists:
      - # required
        name: name_example

        # optional
        addresses: [ "null" ]
        address_lists: [ "null" ]
      good_bots:
      - # required
        key: key_example
        is_enabled: true

        # optional
        name: name_example
        description: description_example
      protection_rules:
      - # optional
        key: key_example
        mod_security_rule_ids: [ "null" ]
        name: name_example
        description: description_example
        action: OFF
        labels: [ "null" ]
        exclusions:
        - # optional
          target: REQUEST_COOKIES
          exclusions: [ "null" ]
      threat_feeds:
      - # optional
        key: key_example
        name: name_example
        action: OFF
        description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update waas_policy
  oci_waas_policy:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: Policy
    additional_domains: [ "null" ]
    origins:
      # required
      uri: uri_example

      # optional
      http_port: 56
      https_port: 56
      custom_headers:
      - # required
        name: name_example
        value: value_example
    origin_groups:
      # optional
      origins:
      - # optional
        origin: origin_example
        weight: 56
    policy_config:
      # optional
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
      is_https_enabled: true
      is_https_forced: true
      tls_protocols: [ "null" ]
      is_origin_compression_enabled: true
      is_behind_cdn: true
      client_address_header: "X-Client-Ip: 11.1.1.1, 13.3.3.3"
      is_cache_control_respected: true
      is_response_buffering_enabled: true
      cipher_group: DEFAULT
      load_balancing_method:
        # required
        method: ROUND_ROBIN
      websocket_path_prefixes: [ "null" ]
      is_sni_enabled: true
      health_checks:
        # optional
        is_enabled: true
        method: GET
        path: path_example
        headers: null
        expected_response_code_group: [ "null" ]
        is_response_text_check_enabled: true
        expected_response_text: expected_response_text_example
        interval_in_seconds: 56
        timeout_in_seconds: 56
        healthy_threshold: 56
        unhealthy_threshold: 56
    waf_config:
      # optional
      access_rules:
      - # required
        name: name_example
        criteria:
        - # required
          condition: URL_IS
          value: value_example

          # optional
          is_case_sensitive: true
        action: ALLOW

        # optional
        block_action: SET_RESPONSE_CODE
        block_response_code: 56
        block_error_page_message: block_error_page_message_example
        block_error_page_code: block_error_page_code_example
        block_error_page_description: block_error_page_description_example
        bypass_challenges: [ "null" ]
        redirect_url: redirect_url_example
        redirect_response_code: MOVED_PERMANENTLY
        captcha_title: captcha_title_example
        captcha_header: captcha_header_example
        captcha_footer: captcha_footer_example
        captcha_submit_label: captcha_submit_label_example
        response_header_manipulation:
        - # required
          action: EXTEND_HTTP_RESPONSE_HEADER
          header: example_header_name
          value: example_value
      address_rate_limiting:
        # required
        is_enabled: true

        # optional
        allowed_rate_per_address: 56
        max_delayed_count_per_address: 56
        block_response_code: 56
      captchas:
      - # required
        url: url_example
        session_expiration_in_seconds: 56
        title: title_example
        failure_message: failure_message_example
        submit_label: submit_label_example

        # optional
        header_text: header_text_example
        footer_text: footer_text_example
      device_fingerprint_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        failure_threshold_expiration_in_seconds: 56
        max_address_count: 56
        max_address_count_expiration_in_seconds: 56
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
      human_interaction_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        failure_threshold_expiration_in_seconds: 56
        interaction_threshold: 56
        recording_period_in_seconds: 56
        set_http_header:
          # required
          name: name_example
          value: value_example
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
        is_nat_enabled: true
      js_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        set_http_header:
          # required
          name: name_example
          value: value_example
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
        are_redirects_challenged: true
        criteria:
        - # required
          condition: URL_IS
          value: value_example

          # optional
          is_case_sensitive: true
        is_nat_enabled: true
      origin: origin_example
      caching_rules:
      - # required
        name: name_example
        action: CACHE
        criteria:
        - # required
          condition: URL_IS
          value: value_example

        # optional
        key: key_example
        caching_duration: PT1H
        is_client_caching_enabled: true
        client_caching_duration: PT1H
      custom_protection_rules:
      - # optional
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        action: DETECT
        exclusions:
        - # optional
          target: REQUEST_COOKIES
          exclusions: [ "null" ]
      origin_groups: [ "null" ]
      protection_settings:
        # optional
        block_action: SHOW_ERROR_PAGE
        block_response_code: 56
        block_error_page_message: block_error_page_message_example
        block_error_page_code: block_error_page_code_example
        block_error_page_description: block_error_page_description_example
        max_argument_count: 56
        max_name_length_per_argument: 56
        max_total_name_length_of_arguments: 56
        recommendations_period_in_days: 56
        is_response_inspected: true
        max_response_size_in_ki_b: 56
        allowed_http_methods: [ "null" ]
        media_types: [ "null" ]
      whitelists:
      - # required
        name: name_example

        # optional
        addresses: [ "null" ]
        address_lists: [ "null" ]
      good_bots:
      - # required
        key: key_example
        is_enabled: true

        # optional
        name: name_example
        description: description_example
      protection_rules:
      - # optional
        key: key_example
        mod_security_rule_ids: [ "null" ]
        name: name_example
        description: description_example
        action: OFF
        labels: [ "null" ]
        exclusions:
        - # optional
          target: REQUEST_COOKIES
          exclusions: [ "null" ]
      threat_feeds:
      - # optional
        key: key_example
        name: name_example
        action: OFF
        description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update waas_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waas_policy:
    # required
    compartment_id: "ocid1.compartment.oc1.."
    display_name: Policy

    # optional
    additional_domains: [ "null" ]
    origins:
      # required
      uri: uri_example

      # optional
      http_port: 56
      https_port: 56
      custom_headers:
      - # required
        name: name_example
        value: value_example
    origin_groups:
      # optional
      origins:
      - # optional
        origin: origin_example
        weight: 56
    policy_config:
      # optional
      certificate_id: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
      is_https_enabled: true
      is_https_forced: true
      tls_protocols: [ "null" ]
      is_origin_compression_enabled: true
      is_behind_cdn: true
      client_address_header: "X-Client-Ip: 11.1.1.1, 13.3.3.3"
      is_cache_control_respected: true
      is_response_buffering_enabled: true
      cipher_group: DEFAULT
      load_balancing_method:
        # required
        method: ROUND_ROBIN
      websocket_path_prefixes: [ "null" ]
      is_sni_enabled: true
      health_checks:
        # optional
        is_enabled: true
        method: GET
        path: path_example
        headers: null
        expected_response_code_group: [ "null" ]
        is_response_text_check_enabled: true
        expected_response_text: expected_response_text_example
        interval_in_seconds: 56
        timeout_in_seconds: 56
        healthy_threshold: 56
        unhealthy_threshold: 56
    waf_config:
      # optional
      access_rules:
      - # required
        name: name_example
        criteria:
        - # required
          condition: URL_IS
          value: value_example

          # optional
          is_case_sensitive: true
        action: ALLOW

        # optional
        block_action: SET_RESPONSE_CODE
        block_response_code: 56
        block_error_page_message: block_error_page_message_example
        block_error_page_code: block_error_page_code_example
        block_error_page_description: block_error_page_description_example
        bypass_challenges: [ "null" ]
        redirect_url: redirect_url_example
        redirect_response_code: MOVED_PERMANENTLY
        captcha_title: captcha_title_example
        captcha_header: captcha_header_example
        captcha_footer: captcha_footer_example
        captcha_submit_label: captcha_submit_label_example
        response_header_manipulation:
        - # required
          action: EXTEND_HTTP_RESPONSE_HEADER
          header: example_header_name
          value: example_value
      address_rate_limiting:
        # required
        is_enabled: true

        # optional
        allowed_rate_per_address: 56
        max_delayed_count_per_address: 56
        block_response_code: 56
      captchas:
      - # required
        url: url_example
        session_expiration_in_seconds: 56
        title: title_example
        failure_message: failure_message_example
        submit_label: submit_label_example

        # optional
        header_text: header_text_example
        footer_text: footer_text_example
      device_fingerprint_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        failure_threshold_expiration_in_seconds: 56
        max_address_count: 56
        max_address_count_expiration_in_seconds: 56
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
      human_interaction_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        failure_threshold_expiration_in_seconds: 56
        interaction_threshold: 56
        recording_period_in_seconds: 56
        set_http_header:
          # required
          name: name_example
          value: value_example
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
        is_nat_enabled: true
      js_challenge:
        # required
        is_enabled: true

        # optional
        action: DETECT
        failure_threshold: 56
        action_expiration_in_seconds: 56
        set_http_header:
          # required
          name: name_example
          value: value_example
        challenge_settings:
          # optional
          block_action: SET_RESPONSE_CODE
          block_response_code: 56
          block_error_page_message: block_error_page_message_example
          block_error_page_description: block_error_page_description_example
          block_error_page_code: block_error_page_code_example
          captcha_title: captcha_title_example
          captcha_header: captcha_header_example
          captcha_footer: captcha_footer_example
          captcha_submit_label: captcha_submit_label_example
        are_redirects_challenged: true
        criteria:
        - # required
          condition: URL_IS
          value: value_example

          # optional
          is_case_sensitive: true
        is_nat_enabled: true
      origin: origin_example
      caching_rules:
      - # required
        name: name_example
        action: CACHE
        criteria:
        - # required
          condition: URL_IS
          value: value_example

        # optional
        key: key_example
        caching_duration: PT1H
        is_client_caching_enabled: true
        client_caching_duration: PT1H
      custom_protection_rules:
      - # optional
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        action: DETECT
        exclusions:
        - # optional
          target: REQUEST_COOKIES
          exclusions: [ "null" ]
      origin_groups: [ "null" ]
      protection_settings:
        # optional
        block_action: SHOW_ERROR_PAGE
        block_response_code: 56
        block_error_page_message: block_error_page_message_example
        block_error_page_code: block_error_page_code_example
        block_error_page_description: block_error_page_description_example
        max_argument_count: 56
        max_name_length_per_argument: 56
        max_total_name_length_of_arguments: 56
        recommendations_period_in_days: 56
        is_response_inspected: true
        max_response_size_in_ki_b: 56
        allowed_http_methods: [ "null" ]
        media_types: [ "null" ]
      whitelists:
      - # required
        name: name_example

        # optional
        addresses: [ "null" ]
        address_lists: [ "null" ]
      good_bots:
      - # required
        key: key_example
        is_enabled: true

        # optional
        name: name_example
        description: description_example
      protection_rules:
      - # optional
        key: key_example
        mod_security_rule_ids: [ "null" ]
        name: name_example
        description: description_example
        action: OFF
        labels: [ "null" ]
        exclusions:
        - # optional
          target: REQUEST_COOKIES
          exclusions: [ "null" ]
      threat_feeds:
      - # optional
        key: key_example
        name: name_example
        action: OFF
        description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete waas_policy
  oci_waas_policy:
    # required
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete waas_policy using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_waas_policy:
    # required
    compartment_id: "ocid1.compartment.oc1.."
    display_name: Policy
    state: absent

"""

RETURN = """
waas_policy:
    description:
        - Details of the WaasPolicy resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy's compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name of the WAAS policy. The name can be changed and does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        domain:
            description:
                - The web application domain that the WAAS policy protects.
            returned: on success
            type: str
            sample: domain_example
        additional_domains:
            description:
                - An array of additional domains for this web application.
            returned: on success
            type: list
            sample: []
        cname:
            description:
                - The CNAME record to add to your DNS configuration to route traffic for the domain, and all additional domains, through the WAF.
            returned: on success
            type: str
            sample: cname_example
        lifecycle_state:
            description:
                - The current lifecycle state of the WAAS policy.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the policy was created, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2018-11-16T21:10:29Z"
        origins:
            description:
                - "A map of host servers (origins) and their keys for the web application. Origin keys are used to associate origins to specific protection
                  rules. The key should be a user-friendly name for the host. **Examples:** `primary` or `secondary`."
            returned: on success
            type: complex
            contains:
                uri:
                    description:
                        - The URI of the origin. Does not support paths. Port numbers should be specified in the `httpPort` and `httpsPort` fields.
                    returned: on success
                    type: str
                    sample: uri_example
                http_port:
                    description:
                        - "The HTTP port on the origin that the web application listens on. If unspecified, defaults to `80`. If `0` is specified - the origin
                          is not used for HTTP traffic."
                    returned: on success
                    type: int
                    sample: 56
                https_port:
                    description:
                        - "The HTTPS port on the origin that the web application listens on. If unspecified, defaults to `443`. If `0` is specified - the origin
                          is not used for HTTPS traffic."
                    returned: on success
                    type: int
                    sample: 56
                custom_headers:
                    description:
                        - A list of HTTP headers to forward to your origin.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of the header.
                            returned: on success
                            type: str
                            sample: name_example
                        value:
                            description:
                                - The value of the header.
                            returned: on success
                            type: str
                            sample: value_example
        origin_groups:
            description:
                - The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to groups of
                  origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
            returned: on success
            type: complex
            contains:
                origins:
                    description:
                        - The list of objects containing origin references and additional properties.
                    returned: on success
                    type: complex
                    contains:
                        origin:
                            description:
                                - The IP address or CIDR notation of the origin server.
                            returned: on success
                            type: str
                            sample: origin_example
                        weight:
                            description:
                                - The weight of the origin used in load balancing. Origins with higher weights will receive larger proportions of client
                                  requests.
                            returned: on success
                            type: int
                            sample: 56
        policy_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                certificate_id:
                    description:
                        - The OCID of the SSL certificate to use if HTTPS is supported.
                    returned: on success
                    type: str
                    sample: "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx"
                is_https_enabled:
                    description:
                        - Enable or disable HTTPS support. If true, a `certificateId` is required. If unspecified, defaults to `false`.
                    returned: on success
                    type: bool
                    sample: true
                is_https_forced:
                    description:
                        - Force HTTP to HTTPS redirection. If unspecified, defaults to `false`.
                    returned: on success
                    type: bool
                    sample: true
                tls_protocols:
                    description:
                        - "A list of allowed TLS protocols. Only applicable when HTTPS support is enabled.
                          The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client
                          browser will be selected. If no such version exists, the connection will be aborted.
                          - **TLS_V1:** corresponds to TLS 1.0 specification."
                        - "- **TLS_V1_1:** corresponds to TLS 1.1 specification."
                        - "- **TLS_V1_2:** corresponds to TLS 1.2 specification."
                        - "- **TLS_V1_3:** corresponds to TLS 1.3 specification."
                        - Enabled TLS protocols must go in a row. For example if `TLS_v1_1` and `TLS_V1_3` are enabled, `TLS_V1_2` must be enabled too.
                    returned: on success
                    type: list
                    sample: []
                is_origin_compression_enabled:
                    description:
                        - "Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise,
                          the empty `Accept-Encoding:` header is used."
                    returned: on success
                    type: bool
                    sample: true
                is_behind_cdn:
                    description:
                        - Enabling `isBehindCdn` allows for the collection of IP addresses from client requests if the WAF is connected to a CDN.
                    returned: on success
                    type: bool
                    sample: true
                client_address_header:
                    description:
                        - Specifies an HTTP header name which is treated as the connecting client's IP address. Applicable only if `isBehindCdn` is enabled.
                        - The edge node reads this header and its value and sets the client IP address as specified. It does not create the header if the header
                          is not present in the request. If the header is not present, the connecting IP address will be used as the client's true IP address.
                          It uses the last IP address in the header's value as the true IP address.
                        - "Example: `X-Client-Ip: 11.1.1.1, 13.3.3.3`"
                        - In the case of multiple headers with the same name, only the first header will be used. It is assumed that CDN sets the correct client
                          IP address to prevent spoofing.
                        - "- **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name."
                        - "- **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name."
                        - "- **X_REAL_IP:** Corresponds to `X-Real-Ip` header name."
                        - "- **CLIENT_IP:** Corresponds to `Client-Ip` header name."
                        - "- **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name."
                    returned: on success
                    type: str
                    sample: "X-Client-Ip: 11.1.1.1, 13.3.3.3"
                is_cache_control_respected:
                    description:
                        - "Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a
                          proxy cache. Caching is usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned
                          resource is valid for 120 seconds. Caching rules will overwrite this setting."
                    returned: on success
                    type: bool
                    sample: true
                is_response_buffering_enabled:
                    description:
                        - Enable or disable buffering of responses from the origin. Buffering improves overall stability in case of network issues, but slightly
                          increases Time To First Byte.
                    returned: on success
                    type: bool
                    sample: true
                cipher_group:
                    description:
                        - "The set cipher group for the configured TLS protocol. This sets the configuration for the TLS connections between clients and edge
                          nodes only.
                          - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-
                            AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-
                            SHA256:DHE-DSS-AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-
                            AES128-SHA:ECDHE-RSA-AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-
                            RSA-AES128-SHA:DHE-DSS-AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-
                            SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-
                            CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`"
                    returned: on success
                    type: str
                    sample: DEFAULT
                load_balancing_method:
                    description:
                        - An object that represents a load balancing method and its properties.
                    returned: on success
                    type: complex
                    contains:
                        method:
                            description:
                                - Load balancing methods are algorithms used to efficiently distribute traffic among origin servers.
                                - "- **L(IP_HASH,https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/IPHashLoadBalancingMethod):** All the
                                  incoming requests from the same client IP address should go to the same content origination server. IP_HASH load balancing
                                  method uses origin weights when choosing which origin should the hash be assigned to initially."
                                - "- **L(ROUND_ROBIN,https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/RoundRobinLoadBalancingMethod):**
                                  Forwards requests sequentially to the available origin servers. The first request - to the first origin server, the second
                                  request - to the next origin server, and so on. After it sends a request to the last origin server, it starts again with the
                                  first origin server. When using weights on origins, Weighted Round Robin assigns more requests to origins with a greater
                                  weight. Over a period of time, origins will receive a number of requests in proportion to their weight."
                                - "- **L(STICKY_COOKIE,https://docs.cloud.oracle.com/iaas/api/#/en/waas/latest/datatypes/StickyCookieLoadBalancingMethod):**
                                  Adds a session cookie to the first response from the origin server and identifies the server that sent the response. The
                                  client's next request contains the cookie value, and nginx routes the request to the origin server that responded to the first
                                  request. STICKY_COOKIE load balancing method falls back to Round Robin for the first request."
                            returned: on success
                            type: str
                            sample: IP_HASH
                        name:
                            description:
                                - The name of the cookie used to track the persistence.
                                  Can contain any US-ASCII character except separator or control character.
                            returned: on success
                            type: str
                            sample: name_example
                        domain:
                            description:
                                - The domain for which the cookie is set, defaults to WAAS policy domain.
                            returned: on success
                            type: str
                            sample: domain_example
                        expiration_time_in_seconds:
                            description:
                                - The time for which a browser should keep the cookie in seconds.
                                  Empty value will cause the cookie to expire at the end of a browser session.
                            returned: on success
                            type: int
                            sample: 56
                websocket_path_prefixes:
                    description:
                        - ModSecurity is not capable to inspect WebSockets. Therefore paths specified here have WAF disabled if Connection request header from
                          the client has the value Upgrade (case insensitive matching) and Upgrade request header has the value websocket (case insensitive
                          matching). Paths matches if the concatenation of request URL path and query starts with the contents of the one of
                          `websocketPathPrefixes` array value. In All other cases challenges, like JSC, HIC and etc., remain active.
                    returned: on success
                    type: list
                    sample: []
                is_sni_enabled:
                    description:
                        - SNI stands for Server Name Indication and is an extension of the TLS protocol. It indicates which hostname is being contacted by the
                          browser at the beginning of the 'handshake'-process. This allows a server to connect multiple SSL Certificates to one IP address and
                          port.
                    returned: on success
                    type: bool
                    sample: true
                health_checks:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the health checks.
                            returned: on success
                            type: bool
                            sample: true
                        method:
                            description:
                                - An HTTP verb (i.e. HEAD, GET, or POST) to use when performing the health check.
                            returned: on success
                            type: str
                            sample: GET
                        path:
                            description:
                                - Path to visit on your origins when performing the health check.
                            returned: on success
                            type: str
                            sample: path_example
                        headers:
                            description:
                                - "HTTP header fields to include in health check requests, expressed as `\\"name\\": \\"value\\"` properties. Because HTTP
                                  header field names are case-insensitive, any use of names that are case-insensitive equal to other names will be rejected. If
                                  Host is not specified, requests will include a Host header field with value matching the policy's protected domain. If User-
                                  Agent is not specified, requests will include a User-Agent header field with value \\"waf health checks\\"."
                                - "**Note:** The only currently-supported header fields are Host and User-Agent."
                            returned: on success
                            type: dict
                            sample: {}
                        expected_response_code_group:
                            description:
                                - "The HTTP response codes that signify a healthy state.
                                  - **2XX:** Success response code group.
                                  - **3XX:** Redirection response code group.
                                  - **4XX:** Client errors response code group.
                                  - **5XX:** Server errors response code group."
                            returned: on success
                            type: list
                            sample: []
                        is_response_text_check_enabled:
                            description:
                                - Enables or disables additional check for predefined text in addition to response code.
                            returned: on success
                            type: bool
                            sample: true
                        expected_response_text:
                            description:
                                - Health check will search for the given text in a case-sensitive manner within the response body and will fail if the text is
                                  not found.
                            returned: on success
                            type: str
                            sample: expected_response_text_example
                        interval_in_seconds:
                            description:
                                - Time between health checks of an individual origin server, in seconds.
                            returned: on success
                            type: int
                            sample: 56
                        timeout_in_seconds:
                            description:
                                - Response timeout represents wait time until request is considered failed, in seconds.
                            returned: on success
                            type: int
                            sample: 56
                        healthy_threshold:
                            description:
                                - Number of successful health checks after which the server is marked up.
                            returned: on success
                            type: int
                            sample: 56
                        unhealthy_threshold:
                            description:
                                - Number of failed health checks after which the server is marked down.
                            returned: on success
                            type: int
                            sample: 56
        waf_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                access_rules:
                    description:
                        - The access rules applied to the Web Application Firewall. Used for defining custom access policies with the combination of `ALLOW`,
                          `DETECT`, and `BLOCK` rules, based on different criteria.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The unique name of the access rule.
                            returned: on success
                            type: str
                            sample: name_example
                        criteria:
                            description:
                                - The list of access rule criteria. The rule would be applied only for the requests that matched all the listed conditions.
                            returned: on success
                            type: complex
                            contains:
                                condition:
                                    description:
                                        - "The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
                                          - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value`
                                            field. URL must start with a `/`.
                                          - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the
                                            `value` field. URL must start with a `/`.
                                          - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the
                                            `value` field. URL must start with a `/`.
                                          - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the
                                            `value` field.
                                          - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the
                                            `value` field.
                                          - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in
                                            the value field. The value must be a valid regular expression recognized by the PCRE library in Nginx
                                            (https://www.pcre.org).
                                          - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the
                                            regular expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library
                                            in Nginx (https://www.pcre.org).
                                          - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the
                                            contents of the `value` field.
                                          - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the
                                            contents of the `value` field.
                                          - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the
                                            contents of the `value` field.
                                          - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The
                                            `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                                          *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                                          - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined
                                            address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line
                                            symbol \\\\n
                                          *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                                          - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address
                                            list. The `value` in this case is OCID of the address list.
                                          - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced
                                            address list. The `value` field in this case is OCID of the address list.
                                          - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon:
                                            a header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host`
                                            is the header field name and `test.example.com` is the header field value. A request matches when the header field
                                            name is a case insensitive match and the header field value is a case insensitive, substring match.
                                          *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and
                                          `test.example.com` is the value of the host field, a request with the header values, `Host: www.test.example.com` will
                                          match, where as a request with header values of `host: www.example.com` or `host: test.sub.example.com` will not
                                          match.
                                          - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in
                                            this case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available
                                            methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                                        - "*Example:* \\"GET\\\\nPOST\\""
                                        - "- **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The
                                          `value` in this case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of
                                          available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                                        - "*Example:* \\"GET\\\\nPOST\\""
                                        - "- **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this
                                          case is string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1
                                          alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                          *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                                          - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The
                                            `value` in this case is string with one or multiple countries separated by new line symbol \\\\n Country codes are
                                            in ISO 3166-1 alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                          *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                                          - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field.
                                          *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
                                          - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
                                          *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`"
                                    returned: on success
                                    type: str
                                    sample: URL_IS
                                value:
                                    description:
                                        - The criteria value.
                                    returned: on success
                                    type: str
                                    sample: value_example
                                is_case_sensitive:
                                    description:
                                        - When enabled, the condition will be matched with case-sensitive rules.
                                    returned: on success
                                    type: bool
                                    sample: true
                        action:
                            description:
                                - The action to take when the access criteria are met for a rule. If unspecified, defaults to `ALLOW`.
                                - "- **ALLOW:** Takes no action, just logs the request."
                                - "- **DETECT:** Takes no action, but creates an alert for the request."
                                - "- **BLOCK:** Blocks the request by returning specified response code or showing error page."
                                - "- **BYPASS:** Bypasses some or all challenges."
                                - "- **REDIRECT:** Redirects the request to the specified URL. These fields are required when `REDIRECT` is selected:
                                  `redirectUrl`, `redirectResponseCode`."
                                - "- **SHOW_CAPTCHA:** Show a CAPTCHA Challenge page instead of the requested page."
                                - Regardless of action, no further rules are processed once a rule is matched.
                            returned: on success
                            type: str
                            sample: ALLOW
                        block_action:
                            description:
                                - The method used to block requests if `action` is set to `BLOCK` and the access criteria are met. If unspecified, defaults to
                                  `SET_RESPONSE_CODE`.
                            returned: on success
                            type: str
                            sample: SET_RESPONSE_CODE
                        block_response_code:
                            description:
                                - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the
                                  access criteria are met. If unspecified, defaults to `403`. The list of available response codes: `200`, `201`, `202`, `204`,
                                  `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`,
                                  `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`."
                            returned: on success
                            type: int
                            sample: 56
                        block_error_page_message:
                            description:
                                - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                  access criteria are met. If unspecified, defaults to 'Access to the website is blocked.'
                            returned: on success
                            type: str
                            sample: block_error_page_message_example
                        block_error_page_code:
                            description:
                                - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                  access criteria are met. If unspecified, defaults to 'Access rules'.
                            returned: on success
                            type: str
                            sample: block_error_page_code_example
                        block_error_page_description:
                            description:
                                - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                  the access criteria are met. If unspecified, defaults to 'Access blocked by website owner. Please contact support.'
                            returned: on success
                            type: str
                            sample: block_error_page_description_example
                        bypass_challenges:
                            description:
                                - The list of challenges to bypass when `action` is set to `BYPASS`. If unspecified or empty, all challenges are bypassed.
                                - "- **JS_CHALLENGE:** Bypasses JavaScript Challenge."
                                - "- **DEVICE_FINGERPRINT_CHALLENGE:** Bypasses Device Fingerprint Challenge."
                                - "- **HUMAN_INTERACTION_CHALLENGE:** Bypasses Human Interaction Challenge."
                                - "- **CAPTCHA:** Bypasses CAPTCHA Challenge."
                            returned: on success
                            type: list
                            sample: []
                        redirect_url:
                            description:
                                - The target to which the request should be redirected, represented as a URI reference. Required when `action` is `REDIRECT`.
                            returned: on success
                            type: str
                            sample: redirect_url_example
                        redirect_response_code:
                            description:
                                - The response status code to return when `action` is set to `REDIRECT`.
                                - "- **MOVED_PERMANENTLY:** Used for designating the permanent movement of a page (numerical code - 301)."
                                - "- **FOUND:** Used for designating the temporary movement of a page (numerical code - 302)."
                            returned: on success
                            type: str
                            sample: MOVED_PERMANENTLY
                        captcha_title:
                            description:
                                - The title used when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is challenged.
                            returned: on success
                            type: str
                            sample: captcha_title_example
                        captcha_header:
                            description:
                                - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is
                                  challenged.
                            returned: on success
                            type: str
                            sample: captcha_header_example
                        captcha_footer:
                            description:
                                - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `SHOW_CAPTCHA` and the request is
                                  challenged.
                            returned: on success
                            type: str
                            sample: captcha_footer_example
                        captcha_submit_label:
                            description:
                                - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `SHOW_CAPTCHA` and the request is
                                  challenged.
                            returned: on success
                            type: str
                            sample: captcha_submit_label_example
                        response_header_manipulation:
                            description:
                                - An object that represents an action to apply to an HTTP response headers if all rule criteria will be matched regardless of
                                  `action` value.
                            returned: on success
                            type: complex
                            contains:
                                action:
                                    description:
                                        - ""
                                    returned: on success
                                    type: str
                                    sample: EXTEND_HTTP_RESPONSE_HEADER
                                header:
                                    description:
                                        - A header field name that conforms to RFC 7230.
                                        - "Example: `example_header_name`"
                                    returned: on success
                                    type: str
                                    sample: example_header_name
                                value:
                                    description:
                                        - A header field value that conforms to RFC 7230.
                                        - "Example: `example_value`"
                                    returned: on success
                                    type: str
                                    sample: example_value
                address_rate_limiting:
                    description:
                        - The IP address rate limiting settings used to limit the number of requests from an address.
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the address rate limiting Web Application Firewall feature.
                            returned: on success
                            type: bool
                            sample: true
                        allowed_rate_per_address:
                            description:
                                - The number of allowed requests per second from one IP address. If unspecified, defaults to `1`.
                            returned: on success
                            type: int
                            sample: 56
                        max_delayed_count_per_address:
                            description:
                                - The maximum number of requests allowed to be queued before subsequent requests are dropped. If unspecified, defaults to `10`.
                            returned: on success
                            type: int
                            sample: 56
                        block_response_code:
                            description:
                                - "The response status code returned when a request is blocked. If unspecified, defaults to `503`. The list of available
                                  response codes: `400`, `401`, `403`, `404`, `405`, `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `494`,
                                  `495`, `496`, `497`, `499`, `500`, `501`, `502`, `503`, `504`, `507`."
                            returned: on success
                            type: int
                            sample: 56
                captchas:
                    description:
                        - A list of CAPTCHA challenge settings. These are used to challenge requests with a CAPTCHA to block bots.
                    returned: on success
                    type: complex
                    contains:
                        url:
                            description:
                                - The unique URL path at which to show the CAPTCHA challenge.
                            returned: on success
                            type: str
                            sample: url_example
                        session_expiration_in_seconds:
                            description:
                                - The amount of time before the CAPTCHA expires, in seconds. If unspecified, defaults to `300`.
                            returned: on success
                            type: int
                            sample: 56
                        title:
                            description:
                                - The title used when displaying a CAPTCHA challenge. If unspecified, defaults to `Are you human?`
                            returned: on success
                            type: str
                            sample: title_example
                        header_text:
                            description:
                                - The text to show in the header when showing a CAPTCHA challenge. If unspecified, defaults to 'We have detected an increased
                                  number of attempts to access this website. To help us keep this site secure, please let us know that you are not a robot by
                                  entering the text from the image below.'
                            returned: on success
                            type: str
                            sample: header_text_example
                        footer_text:
                            description:
                                - The text to show in the footer when showing a CAPTCHA challenge. If unspecified, defaults to 'Enter the letters and numbers as
                                  they are shown in the image above.'
                            returned: on success
                            type: str
                            sample: footer_text_example
                        failure_message:
                            description:
                                - The text to show when incorrect CAPTCHA text is entered. If unspecified, defaults to `The CAPTCHA was incorrect. Try again.`
                            returned: on success
                            type: str
                            sample: failure_message_example
                        submit_label:
                            description:
                                - The text to show on the label of the CAPTCHA challenge submit button. If unspecified, defaults to `Yes, I am human`.
                            returned: on success
                            type: str
                            sample: submit_label_example
                device_fingerprint_challenge:
                    description:
                        - The device fingerprint challenge settings. Used to detect unique devices based on the device fingerprint information collected in
                          order to block bots.
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the device fingerprint challenge Web Application Firewall feature.
                            returned: on success
                            type: bool
                            sample: true
                        action:
                            description:
                                - The action to take on requests from detected bots. If unspecified, defaults to `DETECT`.
                            returned: on success
                            type: str
                            sample: DETECT
                        failure_threshold:
                            description:
                                - The number of failed requests allowed before taking action. If unspecified, defaults to `10`.
                            returned: on success
                            type: int
                            sample: 56
                        action_expiration_in_seconds:
                            description:
                                - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        failure_threshold_expiration_in_seconds:
                            description:
                                - The number of seconds before the failure threshold resets. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        max_address_count:
                            description:
                                - The maximum number of IP addresses permitted with the same device fingerprint. If unspecified, defaults to `20`.
                            returned: on success
                            type: int
                            sample: 56
                        max_address_count_expiration_in_seconds:
                            description:
                                - The number of seconds before the maximum addresses count resets. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        challenge_settings:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                block_action:
                                    description:
                                        - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                          `SHOW_ERROR_PAGE`.
                                    returned: on success
                                    type: str
                                    sample: SET_RESPONSE_CODE
                                block_response_code:
                                    description:
                                        - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response
                                          codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`,
                                          `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`,
                                          `502`, `503`, `504`, `507`."
                                    returned: on success
                                    type: int
                                    sample: 56
                                block_error_page_message:
                                    description:
                                        - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                          the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                    returned: on success
                                    type: str
                                    sample: block_error_page_message_example
                                block_error_page_description:
                                    description:
                                        - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please
                                          contact support.`
                                    returned: on success
                                    type: str
                                    sample: block_error_page_description_example
                                block_error_page_code:
                                    description:
                                        - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`
                                          and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: str
                                    sample: block_error_page_code_example
                                captcha_title:
                                    description:
                                        - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
                                    returned: on success
                                    type: str
                                    sample: captcha_title_example
                                captcha_header:
                                    description:
                                        - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of
                                          attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by
                                          entering the text from captcha below.`
                                    returned: on success
                                    type: str
                                    sample: captcha_header_example
                                captcha_footer:
                                    description:
                                        - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are
                                          shown in image above`.
                                    returned: on success
                                    type: str
                                    sample: captcha_footer_example
                                captcha_submit_label:
                                    description:
                                        - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is
                                          set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                    returned: on success
                                    type: str
                                    sample: captcha_submit_label_example
                good_bots:
                    description:
                        - A list of bots allowed to access the web application.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique key for the bot.
                            returned: on success
                            type: str
                            sample: key_example
                        name:
                            description:
                                - The bot name.
                            returned: on success
                            type: str
                            sample: name_example
                        is_enabled:
                            description:
                                - Enables or disables the bot.
                            returned: on success
                            type: bool
                            sample: true
                        description:
                            description:
                                - The description of the bot.
                            returned: on success
                            type: str
                            sample: description_example
                human_interaction_challenge:
                    description:
                        - The human interaction challenge settings. Used to look for natural human interactions such as mouse movements, time on site, and page
                          scrolling to identify bots.
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the human interaction challenge Web Application Firewall feature.
                            returned: on success
                            type: bool
                            sample: true
                        action:
                            description:
                                - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
                            returned: on success
                            type: str
                            sample: DETECT
                        failure_threshold:
                            description:
                                - The number of failed requests before taking action. If unspecified, defaults to `10`.
                            returned: on success
                            type: int
                            sample: 56
                        action_expiration_in_seconds:
                            description:
                                - The number of seconds between challenges for the same IP address. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        failure_threshold_expiration_in_seconds:
                            description:
                                - The number of seconds before the failure threshold resets. If unspecified, defaults to  `60`.
                            returned: on success
                            type: int
                            sample: 56
                        interaction_threshold:
                            description:
                                - The number of interactions required to pass the challenge. If unspecified, defaults to `3`.
                            returned: on success
                            type: int
                            sample: 56
                        recording_period_in_seconds:
                            description:
                                - The number of seconds to record the interactions from the user. If unspecified, defaults to `15`.
                            returned: on success
                            type: int
                            sample: 56
                        set_http_header:
                            description:
                                - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the
                                  `action` is set to `DETECT`.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the header.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - The value of the header.
                                    returned: on success
                                    type: str
                                    sample: value_example
                        challenge_settings:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                block_action:
                                    description:
                                        - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                          `SHOW_ERROR_PAGE`.
                                    returned: on success
                                    type: str
                                    sample: SET_RESPONSE_CODE
                                block_response_code:
                                    description:
                                        - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response
                                          codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`,
                                          `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`,
                                          `502`, `503`, `504`, `507`."
                                    returned: on success
                                    type: int
                                    sample: 56
                                block_error_page_message:
                                    description:
                                        - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                          the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                    returned: on success
                                    type: str
                                    sample: block_error_page_message_example
                                block_error_page_description:
                                    description:
                                        - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please
                                          contact support.`
                                    returned: on success
                                    type: str
                                    sample: block_error_page_description_example
                                block_error_page_code:
                                    description:
                                        - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`
                                          and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: str
                                    sample: block_error_page_code_example
                                captcha_title:
                                    description:
                                        - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
                                    returned: on success
                                    type: str
                                    sample: captcha_title_example
                                captcha_header:
                                    description:
                                        - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of
                                          attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by
                                          entering the text from captcha below.`
                                    returned: on success
                                    type: str
                                    sample: captcha_header_example
                                captcha_footer:
                                    description:
                                        - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are
                                          shown in image above`.
                                    returned: on success
                                    type: str
                                    sample: captcha_footer_example
                                captcha_submit_label:
                                    description:
                                        - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is
                                          set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                    returned: on success
                                    type: str
                                    sample: captcha_submit_label_example
                        is_nat_enabled:
                            description:
                                - When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking
                                  visitors with shared IP addresses.
                            returned: on success
                            type: bool
                            sample: true
                js_challenge:
                    description:
                        - The JavaScript challenge settings. Used to challenge requests with a JavaScript challenge and take the action if a browser has no
                          JavaScript support in order to block bots.
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables or disables the JavaScript challenge Web Application Firewall feature.
                            returned: on success
                            type: bool
                            sample: true
                        action:
                            description:
                                - The action to take against requests from detected bots. If unspecified, defaults to `DETECT`.
                            returned: on success
                            type: str
                            sample: DETECT
                        failure_threshold:
                            description:
                                - The number of failed requests before taking action. If unspecified, defaults to `10`.
                            returned: on success
                            type: int
                            sample: 56
                        action_expiration_in_seconds:
                            description:
                                - The number of seconds between challenges from the same IP address. If unspecified, defaults to `60`.
                            returned: on success
                            type: int
                            sample: 56
                        set_http_header:
                            description:
                                - Adds an additional HTTP header to requests that fail the challenge before being passed to the origin. Only applicable when the
                                  `action` is set to `DETECT`.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - The name of the header.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - The value of the header.
                                    returned: on success
                                    type: str
                                    sample: value_example
                        challenge_settings:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                block_action:
                                    description:
                                        - The method used to block requests that fail the challenge, if `action` is set to `BLOCK`. If unspecified, defaults to
                                          `SHOW_ERROR_PAGE`.
                                    returned: on success
                                    type: str
                                    sample: SET_RESPONSE_CODE
                                block_response_code:
                                    description:
                                        - "The response status code to return when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE` or
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `403`. The list of available response
                                          codes: `200`, `201`, `202`, `204`, `206`, `300`, `301`, `302`, `303`, `304`, `307`, `400`, `401`, `403`, `404`, `405`,
                                          `408`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `422`, `444`, `494`, `495`, `496`, `497`, `499`, `500`, `501`,
                                          `502`, `503`, `504`, `507`."
                                    returned: on success
                                    type: int
                                    sample: 56
                                block_error_page_message:
                                    description:
                                        - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                          the request is blocked. If unspecified, defaults to `Access to the website is blocked`.
                                    returned: on success
                                    type: str
                                    sample: block_error_page_message_example
                                block_error_page_description:
                                    description:
                                        - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_ERROR_PAGE`, and the request is blocked. If unspecified, defaults to `Access blocked by website owner. Please
                                          contact support.`
                                    returned: on success
                                    type: str
                                    sample: block_error_page_description_example
                                block_error_page_code:
                                    description:
                                        - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`
                                          and the request is blocked. If unspecified, defaults to `403`.
                                    returned: on success
                                    type: str
                                    sample: block_error_page_code_example
                                captcha_title:
                                    description:
                                        - The title used when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set to
                                          `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Are you human?`
                                    returned: on success
                                    type: str
                                    sample: captcha_title_example
                                captcha_header:
                                    description:
                                        - The text to show in the header when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `We have detected an increased number of
                                          attempts to access this webapp. To help us keep this webapp secure, please let us know that you are not a robot by
                                          entering the text from captcha below.`
                                    returned: on success
                                    type: str
                                    sample: captcha_header_example
                                captcha_footer:
                                    description:
                                        - The text to show in the footer when showing a CAPTCHA challenge when `action` is set to `BLOCK`, `blockAction` is set
                                          to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, default to `Enter the letters and numbers as they are
                                          shown in image above`.
                                    returned: on success
                                    type: str
                                    sample: captcha_footer_example
                                captcha_submit_label:
                                    description:
                                        - The text to show on the label of the CAPTCHA challenge submit button when `action` is set to `BLOCK`, `blockAction` is
                                          set to `SHOW_CAPTCHA`, and the request is blocked. If unspecified, defaults to `Yes, I am human`.
                                    returned: on success
                                    type: str
                                    sample: captcha_submit_label_example
                        are_redirects_challenged:
                            description:
                                - When enabled, redirect responses from the origin will also be challenged. This will change HTTP 301/302 responses from origin
                                  to HTTP 200 with an HTML body containing JavaScript page redirection.
                            returned: on success
                            type: bool
                            sample: true
                        criteria:
                            description:
                                - When defined, the JavaScript Challenge would be applied only for the requests that matched all the listed conditions.
                            returned: on success
                            type: complex
                            contains:
                                condition:
                                    description:
                                        - "The criteria the access rule and JavaScript Challenge uses to determine if action should be taken on a request.
                                          - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value`
                                            field. URL must start with a `/`.
                                          - **URL_IS_NOT:** Matches if the concatenation of request URL path and query is not identical to the contents of the
                                            `value` field. URL must start with a `/`.
                                          - **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the
                                            `value` field. URL must start with a `/`.
                                          - **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the
                                            `value` field.
                                          - **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the
                                            `value` field.
                                          - **URL_REGEX:** Matches if the concatenation of request URL path and query is described by the regular expression in
                                            the value field. The value must be a valid regular expression recognized by the PCRE library in Nginx
                                            (https://www.pcre.org).
                                          - **URL_DOES_NOT_MATCH_REGEX:** Matches if the concatenation of request URL path and query is not described by the
                                            regular expression in the `value` field. The value must be a valid regular expression recognized by the PCRE library
                                            in Nginx (https://www.pcre.org).
                                          - **URL_DOES_NOT_START_WITH:** Matches if the concatenation of request URL path and query does not start with the
                                            contents of the `value` field.
                                          - **URL_PART_DOES_NOT_CONTAIN:** Matches if the concatenation of request URL path and query does not contain the
                                            contents of the `value` field.
                                          - **URL_PART_DOES_NOT_END_WITH:** Matches if the concatenation of request URL path and query does not end with the
                                            contents of the `value` field.
                                          - **IP_IS:** Matches if the request originates from one of the IP addresses contained in the defined address list. The
                                            `value` in this case is string with one or multiple IPs or CIDR notations separated by new line symbol \\\\n
                                          *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                                          - **IP_IS_NOT:** Matches if the request does not originate from any of the IP addresses contained in the defined
                                            address list. The `value` in this case is string with one or multiple IPs or CIDR notations separated by new line
                                            symbol \\\\n
                                          *Example:* \\"1.1.1.1\\\\n1.1.1.2\\\\n1.2.2.1/30\\"
                                          - **IP_IN_LIST:** Matches if the request originates from one of the IP addresses contained in the referenced address
                                            list. The `value` in this case is OCID of the address list.
                                          - **IP_NOT_IN_LIST:** Matches if the request does not originate from any IP address contained in the referenced
                                            address list. The `value` field in this case is OCID of the address list.
                                          - **HTTP_HEADER_CONTAINS:** The HTTP_HEADER_CONTAINS criteria is defined using a compound value separated by a colon:
                                            a header field name and a header field value. `host:test.example.com` is an example of a criteria value where `host`
                                            is the header field name and `test.example.com` is the header field value. A request matches when the header field
                                            name is a case insensitive match and the header field value is a case insensitive, substring match.
                                          *Example:* With a criteria value of `host:test.example.com`, where `host` is the name of the field and
                                          `test.example.com` is the value of the host field, a request with the header values, `Host: www.test.example.com` will
                                          match, where as a request with header values of `host: www.example.com` or `host: test.sub.example.com` will not
                                          match.
                                          - **HTTP_METHOD_IS:** Matches if the request method is identical to one of the values listed in field. The `value` in
                                            this case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of available
                                            methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                                        - "*Example:* \\"GET\\\\nPOST\\""
                                        - "- **HTTP_METHOD_IS_NOT:** Matches if the request is not identical to any of the contents of the `value` field. The
                                          `value` in this case is string with one or multiple HTTP methods separated by new line symbol \\\\n The list of
                                          available methods: `GET`, `HEAD`, `POST`, `PUT`, `DELETE`, `CONNECT`, `OPTIONS`, `TRACE`, `PATCH`"
                                        - "*Example:* \\"GET\\\\nPOST\\""
                                        - "- **COUNTRY_IS:** Matches if the request originates from one of countries in the `value` field. The `value` in this
                                          case is string with one or multiple countries separated by new line symbol \\\\n Country codes are in ISO 3166-1
                                          alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                          *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                                          - **COUNTRY_IS_NOT:** Matches if the request does not originate from any of countries in the `value` field. The
                                            `value` in this case is string with one or multiple countries separated by new line symbol \\\\n Country codes are
                                            in ISO 3166-1 alpha-2 format. For a list of codes, see L(ISO's website,https://www.iso.org/obp/ui/#search/code/).
                                          *Example:* \\"AL\\\\nDZ\\\\nAM\\"
                                          - **USER_AGENT_IS:** Matches if the requesting user agent is identical to the contents of the `value` field.
                                          *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`
                                          - **USER_AGENT_IS_NOT:** Matches if the requesting user agent is not identical to the contents of the `value` field.
                                          *Example:* `Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:35.0) Gecko/20100101 Firefox/35.0`"
                                    returned: on success
                                    type: str
                                    sample: URL_IS
                                value:
                                    description:
                                        - The criteria value.
                                    returned: on success
                                    type: str
                                    sample: value_example
                                is_case_sensitive:
                                    description:
                                        - When enabled, the condition will be matched with case-sensitive rules.
                                    returned: on success
                                    type: bool
                                    sample: true
                        is_nat_enabled:
                            description:
                                - When enabled, the user is identified not only by the IP address but also by an unique additional hash, which prevents blocking
                                  visitors with shared IP addresses.
                            returned: on success
                            type: bool
                            sample: true
                origin:
                    description:
                        - The key in the map of origins referencing the origin used for the Web Application Firewall. The origin must already be included in
                          `Origins`. Required when creating the `WafConfig` resource, but not on update.
                    returned: on success
                    type: str
                    sample: origin_example
                caching_rules:
                    description:
                        - A list of caching rules applied to the web application.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique key for the caching rule.
                            returned: on success
                            type: str
                            sample: key_example
                        name:
                            description:
                                - The name of the caching rule.
                            returned: on success
                            type: str
                            sample: name_example
                        action:
                            description:
                                - "The action to take when the criteria of a caching rule are met.
                                  - **CACHE:** Caches requested content when the criteria of the rule are met."
                                - "- **BYPASS_CACHE:** Allows requests to bypass the cache and be directed to the origin when the criteria of the rule is met."
                            returned: on success
                            type: str
                            sample: CACHE
                        caching_duration:
                            description:
                                - "The duration to cache content for the caching rule, specified in ISO 8601 extended format. Supported units: seconds, minutes,
                                  hours, days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not supported.
                                  Only applies when the `action` is set to `CACHE`.
                                  Example: `PT1H`"
                            returned: on success
                            type: str
                            sample: PT1H
                        is_client_caching_enabled:
                            description:
                                - Enables or disables client caching.
                                  Browsers use the `Cache-Control` header value for caching content locally in the browser. This setting overrides the addition
                                  of a `Cache-Control` header in responses.
                            returned: on success
                            type: bool
                            sample: true
                        client_caching_duration:
                            description:
                                - "The duration to cache content in the user's browser, specified in ISO 8601 extended format. Supported units: seconds,
                                  minutes, hours, days, weeks, months. The maximum value that can be set for any unit is `99`. Mixing of multiple units is not
                                  supported. Only applies when the `action` is set to `CACHE`.
                                  Example: `PT1H`"
                            returned: on success
                            type: str
                            sample: PT1H
                        criteria:
                            description:
                                - The array of the rule criteria with condition and value. The caching rule would be applied for the requests that matched any
                                  of the listed conditions.
                            returned: on success
                            type: complex
                            contains:
                                condition:
                                    description:
                                        - "The condition of the caching rule criteria.
                                          - **URL_IS:** Matches if the concatenation of request URL path and query is identical to the contents of the `value`
                                            field."
                                        - "- **URL_STARTS_WITH:** Matches if the concatenation of request URL path and query starts with the contents of the
                                          `value` field."
                                        - "- **URL_PART_ENDS_WITH:** Matches if the concatenation of request URL path and query ends with the contents of the
                                          `value` field."
                                        - "- **URL_PART_CONTAINS:** Matches if the concatenation of request URL path and query contains the contents of the
                                          `value` field."
                                        - URLs must start with a `/`. URLs can't contain restricted double slashes `//`. URLs can't contain the restricted `'`
                                          `&` `?` symbols. Resources to cache can only be specified by a URL, any query parameters are ignored.
                                    returned: on success
                                    type: str
                                    sample: URL_IS
                                value:
                                    description:
                                        - The value of the caching rule criteria.
                                    returned: on success
                                    type: str
                                    sample: value_example
                custom_protection_rules:
                    description:
                        - A list of the custom protection rule OCIDs and their actions.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the custom protection rule.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        action:
                            description:
                                - "The action to take when the custom protection rule is triggered.
                                  `DETECT` - Logs the request when the criteria of the custom protection rule are met. `BLOCK` - Blocks the request when the
                                  criteria of the custom protection rule are met."
                            returned: on success
                            type: str
                            sample: DETECT
                        exclusions:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                target:
                                    description:
                                        - The target of the exclusion.
                                    returned: on success
                                    type: str
                                    sample: REQUEST_COOKIES
                                exclusions:
                                    description:
                                        - ""
                                    returned: on success
                                    type: list
                                    sample: []
                origin_groups:
                    description:
                        - The map of origin groups and their keys used to associate origins to the `wafConfig`. Origin groups allow you to apply weights to
                          groups of origins for load balancing purposes. Origins with higher weights will receive larger proportions of client requests.
                          To add additional origins to your WAAS policy, update the `origins` field of a `UpdateWaasPolicy` request.
                    returned: on success
                    type: list
                    sample: []
                protection_rules:
                    description:
                        - A list of the protection rules and their details.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique key of the protection rule.
                            returned: on success
                            type: str
                            sample: key_example
                        mod_security_rule_ids:
                            description:
                                - The list of the ModSecurity rule IDs that apply to this protection rule. For more information about ModSecurity's open source
                                  WAF rules, see L(Mod Security's documentation,https://www.modsecurity.org/CRS/Documentation/index.html).
                            returned: on success
                            type: list
                            sample: []
                        name:
                            description:
                                - The name of the protection rule.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - The description of the protection rule.
                            returned: on success
                            type: str
                            sample: description_example
                        action:
                            description:
                                - The action to take when the traffic is detected as malicious. If unspecified, defaults to `OFF`.
                            returned: on success
                            type: str
                            sample: OFF
                        labels:
                            description:
                                - The list of labels for the protection rule.
                                - "**Note:** Protection rules with a `ResponseBody` label will have no effect unless `isResponseInspected` is true."
                            returned: on success
                            type: list
                            sample: []
                        exclusions:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                target:
                                    description:
                                        - The target of the exclusion.
                                    returned: on success
                                    type: str
                                    sample: REQUEST_COOKIES
                                exclusions:
                                    description:
                                        - ""
                                    returned: on success
                                    type: list
                                    sample: []
                protection_settings:
                    description:
                        - The settings to apply to protection rules.
                    returned: on success
                    type: complex
                    contains:
                        block_action:
                            description:
                                - If `action` is set to `BLOCK`, this specifies how the traffic is blocked when detected as malicious by a protection rule. If
                                  unspecified, defaults to `SET_RESPONSE_CODE`.
                            returned: on success
                            type: str
                            sample: SHOW_ERROR_PAGE
                        block_response_code:
                            description:
                                - "The response code returned when `action` is set to `BLOCK`, `blockAction` is set to `SET_RESPONSE_CODE`, and the traffic is
                                  detected as malicious by a protection rule. If unspecified, defaults to `403`. The list of available response codes: `400`,
                                  `401`, `403`, `405`, `409`, `411`, `412`, `413`, `414`, `415`, `416`, `500`, `501`, `502`, `503`, `504`, `507`."
                            returned: on success
                            type: int
                            sample: 56
                        block_error_page_message:
                            description:
                                - The message to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                  traffic is detected as malicious by a protection rule. If unspecified, defaults to 'Access to the website is blocked.'
                            returned: on success
                            type: str
                            sample: block_error_page_message_example
                        block_error_page_code:
                            description:
                                - The error code to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and the
                                  traffic is detected as malicious by a protection rule. If unspecified, defaults to `403`.
                            returned: on success
                            type: str
                            sample: block_error_page_code_example
                        block_error_page_description:
                            description:
                                - The description text to show on the error page when `action` is set to `BLOCK`, `blockAction` is set to `SHOW_ERROR_PAGE`, and
                                  the traffic is detected as malicious by a protection rule. If unspecified, defaults to `Access blocked by website owner.
                                  Please contact support.`
                            returned: on success
                            type: str
                            sample: block_error_page_description_example
                        max_argument_count:
                            description:
                                - "The maximum number of arguments allowed to be passed to your application before an action is taken. Arguements are query
                                  parameters or body parameters in a PUT or POST request. If unspecified, defaults to `255`. This setting only applies if a
                                  corresponding protection rule is enabled, such as the \\"Number of Arguments Limits\\" rule (key: 960335)."
                                - "Example: If `maxArgumentCount` to `2` for the Max Number of Arguments protection rule (key: 960335), the following requests
                                  would be blocked:
                                  `GET /myapp/path?query=one&query=two&query=three`
                                  `POST /myapp/path` with Body `{\\"argument1\\":\\"one\\",\\"argument2\\":\\"two\\",\\"argument3\\":\\"three\\"}`"
                            returned: on success
                            type: int
                            sample: 56
                        max_name_length_per_argument:
                            description:
                                - "The maximum length allowed for each argument name, in characters. Arguements are query parameters or body parameters in a PUT
                                  or POST request. If unspecified, defaults to `400`. This setting only applies if a corresponding protection rule is enabled,
                                  such as the \\"Values Limits\\" rule (key: 960208)."
                            returned: on success
                            type: int
                            sample: 56
                        max_total_name_length_of_arguments:
                            description:
                                - "The maximum length allowed for the sum of the argument name and value, in characters. Arguements are query parameters or body
                                  parameters in a PUT or POST request. If unspecified, defaults to `64000`. This setting only applies if a corresponding
                                  protection rule is enabled, such as the \\"Total Arguments Limits\\" rule (key: 960341)."
                            returned: on success
                            type: int
                            sample: 56
                        recommendations_period_in_days:
                            description:
                                - The length of time to analyze traffic traffic, in days. After the analysis period, `WafRecommendations` will be populated. If
                                  unspecified, defaults to `10`.
                                - Use `GET /waasPolicies/{waasPolicyId}/wafRecommendations` to view WAF recommendations.
                            returned: on success
                            type: int
                            sample: 56
                        is_response_inspected:
                            description:
                                - Inspects the response body of origin responses. Can be used to detect leakage of sensitive data. If unspecified, defaults to
                                  `false`.
                                - "**Note:** Only origin responses with a Content-Type matching a value in `mediaTypes` will be inspected."
                            returned: on success
                            type: bool
                            sample: true
                        max_response_size_in_ki_b:
                            description:
                                - The maximum response size to be fully inspected, in binary kilobytes (KiB). Anything over this limit will be partially
                                  inspected. If unspecified, defaults to `1024`.
                            returned: on success
                            type: int
                            sample: 56
                        allowed_http_methods:
                            description:
                                - "The list of allowed HTTP methods. If unspecified, default to `[OPTIONS, GET, HEAD, POST]`. This setting only applies if a
                                  corresponding protection rule is enabled, such as the \\"Restrict HTTP Request Methods\\" rule (key: 911100)."
                            returned: on success
                            type: list
                            sample: []
                        media_types:
                            description:
                                - "The list of media types to allow for inspection, if `isResponseInspected` is enabled. Only responses with MIME types in this
                                  list will be inspected. If unspecified, defaults to `[\\"text/html\\", \\"text/plain\\", \\"text/xml\\"]`."
                                - "   Supported MIME types include:"
                                - "   - text/html
                                      - text/plain
                                      - text/asp
                                      - text/css
                                      - text/x-script
                                      - application/json
                                      - text/webviewhtml
                                      - text/x-java-source
                                      - application/x-javascript
                                      - application/javascript
                                      - application/ecmascript
                                      - text/javascript
                                      - text/ecmascript
                                      - text/x-script.perl
                                      - text/x-script.phyton
                                      - application/plain
                                      - application/xml
                                      - text/xml"
                            returned: on success
                            type: list
                            sample: []
                threat_feeds:
                    description:
                        - A list of threat intelligence feeds and the actions to apply to known malicious traffic based on internet intelligence.
                    returned: on success
                    type: complex
                    contains:
                        key:
                            description:
                                - The unique key of the threat intelligence feed.
                            returned: on success
                            type: str
                            sample: key_example
                        name:
                            description:
                                - The name of the threat intelligence feed.
                            returned: on success
                            type: str
                            sample: name_example
                        action:
                            description:
                                - The action to take when traffic is flagged as malicious by data from the threat intelligence feed. If unspecified, defaults to
                                  `OFF`.
                            returned: on success
                            type: str
                            sample: OFF
                        description:
                            description:
                                - The description of the threat intelligence feed.
                            returned: on success
                            type: str
                            sample: description_example
                whitelists:
                    description:
                        - A list of IP addresses that bypass the Web Application Firewall.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The unique name of the whitelist.
                            returned: on success
                            type: str
                            sample: name_example
                        addresses:
                            description:
                                - A set of IP addresses or CIDR notations to include in the whitelist.
                            returned: on success
                            type: list
                            sample: []
                        address_lists:
                            description:
                                - A list of L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of IP address lists to include in the
                                  whitelist.
                            returned: on success
                            type: list
                            sample: []
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "domain": "domain_example",
        "additional_domains": [],
        "cname": "cname_example",
        "lifecycle_state": "CREATING",
        "time_created": "2018-11-16T21:10:29Z",
        "origins": {
            "uri": "uri_example",
            "http_port": 56,
            "https_port": 56,
            "custom_headers": [{
                "name": "name_example",
                "value": "value_example"
            }]
        },
        "origin_groups": {
            "origins": [{
                "origin": "origin_example",
                "weight": 56
            }]
        },
        "policy_config": {
            "certificate_id": "ocid1.certificate.oc1..xxxxxxEXAMPLExxxxxx",
            "is_https_enabled": true,
            "is_https_forced": true,
            "tls_protocols": [],
            "is_origin_compression_enabled": true,
            "is_behind_cdn": true,
            "client_address_header": "X-Client-Ip: 11.1.1.1, 13.3.3.3",
            "is_cache_control_respected": true,
            "is_response_buffering_enabled": true,
            "cipher_group": "DEFAULT",
            "load_balancing_method": {
                "method": "IP_HASH",
                "name": "name_example",
                "domain": "domain_example",
                "expiration_time_in_seconds": 56
            },
            "websocket_path_prefixes": [],
            "is_sni_enabled": true,
            "health_checks": {
                "is_enabled": true,
                "method": "GET",
                "path": "path_example",
                "headers": {},
                "expected_response_code_group": [],
                "is_response_text_check_enabled": true,
                "expected_response_text": "expected_response_text_example",
                "interval_in_seconds": 56,
                "timeout_in_seconds": 56,
                "healthy_threshold": 56,
                "unhealthy_threshold": 56
            }
        },
        "waf_config": {
            "access_rules": [{
                "name": "name_example",
                "criteria": [{
                    "condition": "URL_IS",
                    "value": "value_example",
                    "is_case_sensitive": true
                }],
                "action": "ALLOW",
                "block_action": "SET_RESPONSE_CODE",
                "block_response_code": 56,
                "block_error_page_message": "block_error_page_message_example",
                "block_error_page_code": "block_error_page_code_example",
                "block_error_page_description": "block_error_page_description_example",
                "bypass_challenges": [],
                "redirect_url": "redirect_url_example",
                "redirect_response_code": "MOVED_PERMANENTLY",
                "captcha_title": "captcha_title_example",
                "captcha_header": "captcha_header_example",
                "captcha_footer": "captcha_footer_example",
                "captcha_submit_label": "captcha_submit_label_example",
                "response_header_manipulation": [{
                    "action": "EXTEND_HTTP_RESPONSE_HEADER",
                    "header": "example_header_name",
                    "value": "example_value"
                }]
            }],
            "address_rate_limiting": {
                "is_enabled": true,
                "allowed_rate_per_address": 56,
                "max_delayed_count_per_address": 56,
                "block_response_code": 56
            },
            "captchas": [{
                "url": "url_example",
                "session_expiration_in_seconds": 56,
                "title": "title_example",
                "header_text": "header_text_example",
                "footer_text": "footer_text_example",
                "failure_message": "failure_message_example",
                "submit_label": "submit_label_example"
            }],
            "device_fingerprint_challenge": {
                "is_enabled": true,
                "action": "DETECT",
                "failure_threshold": 56,
                "action_expiration_in_seconds": 56,
                "failure_threshold_expiration_in_seconds": 56,
                "max_address_count": 56,
                "max_address_count_expiration_in_seconds": 56,
                "challenge_settings": {
                    "block_action": "SET_RESPONSE_CODE",
                    "block_response_code": 56,
                    "block_error_page_message": "block_error_page_message_example",
                    "block_error_page_description": "block_error_page_description_example",
                    "block_error_page_code": "block_error_page_code_example",
                    "captcha_title": "captcha_title_example",
                    "captcha_header": "captcha_header_example",
                    "captcha_footer": "captcha_footer_example",
                    "captcha_submit_label": "captcha_submit_label_example"
                }
            },
            "good_bots": [{
                "key": "key_example",
                "name": "name_example",
                "is_enabled": true,
                "description": "description_example"
            }],
            "human_interaction_challenge": {
                "is_enabled": true,
                "action": "DETECT",
                "failure_threshold": 56,
                "action_expiration_in_seconds": 56,
                "failure_threshold_expiration_in_seconds": 56,
                "interaction_threshold": 56,
                "recording_period_in_seconds": 56,
                "set_http_header": {
                    "name": "name_example",
                    "value": "value_example"
                },
                "challenge_settings": {
                    "block_action": "SET_RESPONSE_CODE",
                    "block_response_code": 56,
                    "block_error_page_message": "block_error_page_message_example",
                    "block_error_page_description": "block_error_page_description_example",
                    "block_error_page_code": "block_error_page_code_example",
                    "captcha_title": "captcha_title_example",
                    "captcha_header": "captcha_header_example",
                    "captcha_footer": "captcha_footer_example",
                    "captcha_submit_label": "captcha_submit_label_example"
                },
                "is_nat_enabled": true
            },
            "js_challenge": {
                "is_enabled": true,
                "action": "DETECT",
                "failure_threshold": 56,
                "action_expiration_in_seconds": 56,
                "set_http_header": {
                    "name": "name_example",
                    "value": "value_example"
                },
                "challenge_settings": {
                    "block_action": "SET_RESPONSE_CODE",
                    "block_response_code": 56,
                    "block_error_page_message": "block_error_page_message_example",
                    "block_error_page_description": "block_error_page_description_example",
                    "block_error_page_code": "block_error_page_code_example",
                    "captcha_title": "captcha_title_example",
                    "captcha_header": "captcha_header_example",
                    "captcha_footer": "captcha_footer_example",
                    "captcha_submit_label": "captcha_submit_label_example"
                },
                "are_redirects_challenged": true,
                "criteria": [{
                    "condition": "URL_IS",
                    "value": "value_example",
                    "is_case_sensitive": true
                }],
                "is_nat_enabled": true
            },
            "origin": "origin_example",
            "caching_rules": [{
                "key": "key_example",
                "name": "name_example",
                "action": "CACHE",
                "caching_duration": "PT1H",
                "is_client_caching_enabled": true,
                "client_caching_duration": "PT1H",
                "criteria": [{
                    "condition": "URL_IS",
                    "value": "value_example"
                }]
            }],
            "custom_protection_rules": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "action": "DETECT",
                "exclusions": [{
                    "target": "REQUEST_COOKIES",
                    "exclusions": []
                }]
            }],
            "origin_groups": [],
            "protection_rules": [{
                "key": "key_example",
                "mod_security_rule_ids": [],
                "name": "name_example",
                "description": "description_example",
                "action": "OFF",
                "labels": [],
                "exclusions": [{
                    "target": "REQUEST_COOKIES",
                    "exclusions": []
                }]
            }],
            "protection_settings": {
                "block_action": "SHOW_ERROR_PAGE",
                "block_response_code": 56,
                "block_error_page_message": "block_error_page_message_example",
                "block_error_page_code": "block_error_page_code_example",
                "block_error_page_description": "block_error_page_description_example",
                "max_argument_count": 56,
                "max_name_length_per_argument": 56,
                "max_total_name_length_of_arguments": 56,
                "recommendations_period_in_days": 56,
                "is_response_inspected": true,
                "max_response_size_in_ki_b": 56,
                "allowed_http_methods": [],
                "media_types": []
            },
            "threat_feeds": [{
                "key": "key_example",
                "name": "name_example",
                "action": "OFF",
                "description": "description_example"
            }],
            "whitelists": [{
                "name": "name_example",
                "addresses": [],
                "address_lists": []
            }]
        },
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
    from oci.waas import WaasClient
    from oci.waas.models import CreateWaasPolicyDetails
    from oci.waas.models import UpdateWaasPolicyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasPolicyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "waas_policy_id"

    def get_module_resource_id(self):
        return self.module.params.get("waas_policy_id")

    def get_get_fn(self):
        return self.client.get_waas_policy

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_waas_policy,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_waas_policies, **kwargs
        )

    def get_create_model_class(self):
        return CreateWaasPolicyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_waas_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(create_waas_policy_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateWaasPolicyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_waas_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
                update_waas_policy_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_waas_policy,
            call_fn_args=(),
            call_fn_kwargs=dict(
                waas_policy_id=self.module.params.get("waas_policy_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


WaasPolicyHelperCustom = get_custom_class("WaasPolicyHelperCustom")


class ResourceHelper(WaasPolicyHelperCustom, WaasPolicyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            domain=dict(type="str"),
            additional_domains=dict(type="list", elements="str"),
            origins=dict(type="dict"),
            origin_groups=dict(type="dict"),
            policy_config=dict(
                type="dict",
                options=dict(
                    certificate_id=dict(type="str"),
                    is_https_enabled=dict(type="bool"),
                    is_https_forced=dict(type="bool"),
                    tls_protocols=dict(
                        type="list",
                        elements="str",
                        choices=["TLS_V1", "TLS_V1_1", "TLS_V1_2", "TLS_V1_3"],
                    ),
                    is_origin_compression_enabled=dict(type="bool"),
                    is_behind_cdn=dict(type="bool"),
                    client_address_header=dict(
                        type="str",
                        choices=[
                            "X_FORWARDED_FOR",
                            "X_CLIENT_IP",
                            "X_REAL_IP",
                            "CLIENT_IP",
                            "TRUE_CLIENT_IP",
                        ],
                    ),
                    is_cache_control_respected=dict(type="bool"),
                    is_response_buffering_enabled=dict(type="bool"),
                    cipher_group=dict(type="str", choices=["DEFAULT"]),
                    load_balancing_method=dict(
                        type="dict",
                        options=dict(
                            method=dict(
                                type="str",
                                required=True,
                                choices=["ROUND_ROBIN", "STICKY_COOKIE", "IP_HASH"],
                            ),
                            name=dict(type="str"),
                            domain=dict(type="str"),
                            expiration_time_in_seconds=dict(type="int"),
                        ),
                    ),
                    websocket_path_prefixes=dict(type="list", elements="str"),
                    is_sni_enabled=dict(type="bool"),
                    health_checks=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool"),
                            method=dict(type="str", choices=["GET", "HEAD", "POST"]),
                            path=dict(type="str"),
                            headers=dict(type="dict"),
                            expected_response_code_group=dict(
                                type="list",
                                elements="str",
                                choices=["2XX", "3XX", "4XX", "5XX"],
                            ),
                            is_response_text_check_enabled=dict(type="bool"),
                            expected_response_text=dict(type="str"),
                            interval_in_seconds=dict(type="int"),
                            timeout_in_seconds=dict(type="int"),
                            healthy_threshold=dict(type="int"),
                            unhealthy_threshold=dict(type="int"),
                        ),
                    ),
                ),
            ),
            waf_config=dict(
                type="dict",
                options=dict(
                    access_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            criteria=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    condition=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "URL_IS",
                                            "URL_IS_NOT",
                                            "URL_STARTS_WITH",
                                            "URL_PART_ENDS_WITH",
                                            "URL_PART_CONTAINS",
                                            "URL_REGEX",
                                            "URL_DOES_NOT_MATCH_REGEX",
                                            "URL_DOES_NOT_START_WITH",
                                            "URL_PART_DOES_NOT_CONTAIN",
                                            "URL_PART_DOES_NOT_END_WITH",
                                            "IP_IS",
                                            "IP_IS_NOT",
                                            "IP_IN_LIST",
                                            "IP_NOT_IN_LIST",
                                            "HTTP_HEADER_CONTAINS",
                                            "HTTP_METHOD_IS",
                                            "HTTP_METHOD_IS_NOT",
                                            "COUNTRY_IS",
                                            "COUNTRY_IS_NOT",
                                            "USER_AGENT_IS",
                                            "USER_AGENT_IS_NOT",
                                        ],
                                    ),
                                    value=dict(type="str", required=True),
                                    is_case_sensitive=dict(type="bool"),
                                ),
                            ),
                            action=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ALLOW",
                                    "DETECT",
                                    "BLOCK",
                                    "BYPASS",
                                    "REDIRECT",
                                    "SHOW_CAPTCHA",
                                ],
                            ),
                            block_action=dict(
                                type="str",
                                choices=["SET_RESPONSE_CODE", "SHOW_ERROR_PAGE"],
                            ),
                            block_response_code=dict(type="int"),
                            block_error_page_message=dict(type="str"),
                            block_error_page_code=dict(type="str"),
                            block_error_page_description=dict(type="str"),
                            bypass_challenges=dict(
                                type="list",
                                elements="str",
                                choices=[
                                    "JS_CHALLENGE",
                                    "DEVICE_FINGERPRINT_CHALLENGE",
                                    "HUMAN_INTERACTION_CHALLENGE",
                                    "CAPTCHA",
                                ],
                                no_log=True,
                            ),
                            redirect_url=dict(type="str"),
                            redirect_response_code=dict(
                                type="str", choices=["MOVED_PERMANENTLY", "FOUND"]
                            ),
                            captcha_title=dict(type="str"),
                            captcha_header=dict(type="str"),
                            captcha_footer=dict(type="str"),
                            captcha_submit_label=dict(type="str"),
                            response_header_manipulation=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    action=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "EXTEND_HTTP_RESPONSE_HEADER",
                                            "ADD_HTTP_RESPONSE_HEADER",
                                            "REMOVE_HTTP_RESPONSE_HEADER",
                                        ],
                                    ),
                                    header=dict(type="str", required=True),
                                    value=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    address_rate_limiting=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            allowed_rate_per_address=dict(type="int"),
                            max_delayed_count_per_address=dict(type="int"),
                            block_response_code=dict(type="int"),
                        ),
                    ),
                    captchas=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            url=dict(type="str", required=True),
                            session_expiration_in_seconds=dict(
                                type="int", required=True
                            ),
                            title=dict(type="str", required=True),
                            header_text=dict(type="str"),
                            footer_text=dict(type="str"),
                            failure_message=dict(type="str", required=True),
                            submit_label=dict(type="str", required=True),
                        ),
                    ),
                    device_fingerprint_challenge=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            action=dict(type="str", choices=["DETECT", "BLOCK"]),
                            failure_threshold=dict(type="int"),
                            action_expiration_in_seconds=dict(type="int"),
                            failure_threshold_expiration_in_seconds=dict(type="int"),
                            max_address_count=dict(type="int"),
                            max_address_count_expiration_in_seconds=dict(type="int"),
                            challenge_settings=dict(
                                type="dict",
                                options=dict(
                                    block_action=dict(
                                        type="str",
                                        choices=[
                                            "SET_RESPONSE_CODE",
                                            "SHOW_ERROR_PAGE",
                                            "SHOW_CAPTCHA",
                                        ],
                                    ),
                                    block_response_code=dict(type="int"),
                                    block_error_page_message=dict(type="str"),
                                    block_error_page_description=dict(type="str"),
                                    block_error_page_code=dict(type="str"),
                                    captcha_title=dict(type="str"),
                                    captcha_header=dict(type="str"),
                                    captcha_footer=dict(type="str"),
                                    captcha_submit_label=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    human_interaction_challenge=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            action=dict(type="str", choices=["DETECT", "BLOCK"]),
                            failure_threshold=dict(type="int"),
                            action_expiration_in_seconds=dict(type="int"),
                            failure_threshold_expiration_in_seconds=dict(type="int"),
                            interaction_threshold=dict(type="int"),
                            recording_period_in_seconds=dict(type="int"),
                            set_http_header=dict(
                                type="dict",
                                options=dict(
                                    name=dict(type="str", required=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            challenge_settings=dict(
                                type="dict",
                                options=dict(
                                    block_action=dict(
                                        type="str",
                                        choices=[
                                            "SET_RESPONSE_CODE",
                                            "SHOW_ERROR_PAGE",
                                            "SHOW_CAPTCHA",
                                        ],
                                    ),
                                    block_response_code=dict(type="int"),
                                    block_error_page_message=dict(type="str"),
                                    block_error_page_description=dict(type="str"),
                                    block_error_page_code=dict(type="str"),
                                    captcha_title=dict(type="str"),
                                    captcha_header=dict(type="str"),
                                    captcha_footer=dict(type="str"),
                                    captcha_submit_label=dict(type="str"),
                                ),
                            ),
                            is_nat_enabled=dict(type="bool"),
                        ),
                    ),
                    js_challenge=dict(
                        type="dict",
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            action=dict(type="str", choices=["DETECT", "BLOCK"]),
                            failure_threshold=dict(type="int"),
                            action_expiration_in_seconds=dict(type="int"),
                            set_http_header=dict(
                                type="dict",
                                options=dict(
                                    name=dict(type="str", required=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            challenge_settings=dict(
                                type="dict",
                                options=dict(
                                    block_action=dict(
                                        type="str",
                                        choices=[
                                            "SET_RESPONSE_CODE",
                                            "SHOW_ERROR_PAGE",
                                            "SHOW_CAPTCHA",
                                        ],
                                    ),
                                    block_response_code=dict(type="int"),
                                    block_error_page_message=dict(type="str"),
                                    block_error_page_description=dict(type="str"),
                                    block_error_page_code=dict(type="str"),
                                    captcha_title=dict(type="str"),
                                    captcha_header=dict(type="str"),
                                    captcha_footer=dict(type="str"),
                                    captcha_submit_label=dict(type="str"),
                                ),
                            ),
                            are_redirects_challenged=dict(type="bool"),
                            criteria=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    condition=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "URL_IS",
                                            "URL_IS_NOT",
                                            "URL_STARTS_WITH",
                                            "URL_PART_ENDS_WITH",
                                            "URL_PART_CONTAINS",
                                            "URL_REGEX",
                                            "URL_DOES_NOT_MATCH_REGEX",
                                            "URL_DOES_NOT_START_WITH",
                                            "URL_PART_DOES_NOT_CONTAIN",
                                            "URL_PART_DOES_NOT_END_WITH",
                                            "IP_IS",
                                            "IP_IS_NOT",
                                            "IP_IN_LIST",
                                            "IP_NOT_IN_LIST",
                                            "HTTP_HEADER_CONTAINS",
                                            "HTTP_METHOD_IS",
                                            "HTTP_METHOD_IS_NOT",
                                            "COUNTRY_IS",
                                            "COUNTRY_IS_NOT",
                                            "USER_AGENT_IS",
                                            "USER_AGENT_IS_NOT",
                                        ],
                                    ),
                                    value=dict(type="str", required=True),
                                    is_case_sensitive=dict(type="bool"),
                                ),
                            ),
                            is_nat_enabled=dict(type="bool"),
                        ),
                    ),
                    origin=dict(type="str"),
                    caching_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str", no_log=True),
                            name=dict(type="str", required=True),
                            action=dict(
                                type="str",
                                required=True,
                                choices=["CACHE", "BYPASS_CACHE"],
                            ),
                            caching_duration=dict(type="str"),
                            is_client_caching_enabled=dict(type="bool"),
                            client_caching_duration=dict(type="str"),
                            criteria=dict(
                                type="list",
                                elements="dict",
                                required=True,
                                options=dict(
                                    condition=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "URL_IS",
                                            "URL_STARTS_WITH",
                                            "URL_PART_ENDS_WITH",
                                            "URL_PART_CONTAINS",
                                        ],
                                    ),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                        ),
                    ),
                    custom_protection_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            id=dict(type="str"),
                            action=dict(type="str", choices=["DETECT", "BLOCK"]),
                            exclusions=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    target=dict(
                                        type="str",
                                        choices=[
                                            "REQUEST_COOKIES",
                                            "REQUEST_COOKIE_NAMES",
                                            "ARGS",
                                            "ARGS_NAMES",
                                        ],
                                    ),
                                    exclusions=dict(type="list", elements="str"),
                                ),
                            ),
                        ),
                    ),
                    origin_groups=dict(type="list", elements="str"),
                    protection_settings=dict(
                        type="dict",
                        options=dict(
                            block_action=dict(
                                type="str",
                                choices=["SHOW_ERROR_PAGE", "SET_RESPONSE_CODE"],
                            ),
                            block_response_code=dict(type="int"),
                            block_error_page_message=dict(type="str"),
                            block_error_page_code=dict(type="str"),
                            block_error_page_description=dict(type="str"),
                            max_argument_count=dict(type="int"),
                            max_name_length_per_argument=dict(type="int"),
                            max_total_name_length_of_arguments=dict(type="int"),
                            recommendations_period_in_days=dict(type="int"),
                            is_response_inspected=dict(type="bool"),
                            max_response_size_in_ki_b=dict(type="int"),
                            allowed_http_methods=dict(
                                type="list",
                                elements="str",
                                choices=[
                                    "OPTIONS",
                                    "GET",
                                    "HEAD",
                                    "POST",
                                    "PUT",
                                    "DELETE",
                                    "TRACE",
                                    "CONNECT",
                                    "PATCH",
                                    "PROPFIND",
                                ],
                            ),
                            media_types=dict(type="list", elements="str"),
                        ),
                    ),
                    whitelists=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(type="str", required=True),
                            addresses=dict(type="list", elements="str"),
                            address_lists=dict(type="list", elements="str"),
                        ),
                    ),
                    good_bots=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str", required=True, no_log=True),
                            name=dict(type="str"),
                            is_enabled=dict(type="bool", required=True),
                            description=dict(type="str"),
                        ),
                    ),
                    protection_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str", no_log=True),
                            mod_security_rule_ids=dict(type="list", elements="str"),
                            name=dict(type="str"),
                            description=dict(type="str"),
                            action=dict(type="str", choices=["OFF", "DETECT", "BLOCK"]),
                            labels=dict(type="list", elements="str"),
                            exclusions=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    target=dict(
                                        type="str",
                                        choices=[
                                            "REQUEST_COOKIES",
                                            "REQUEST_COOKIE_NAMES",
                                            "ARGS",
                                            "ARGS_NAMES",
                                        ],
                                    ),
                                    exclusions=dict(type="list", elements="str"),
                                ),
                            ),
                        ),
                    ),
                    threat_feeds=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str", no_log=True),
                            name=dict(type="str"),
                            action=dict(type="str", choices=["OFF", "DETECT", "BLOCK"]),
                            description=dict(type="str"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            waas_policy_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="waas_policy",
        service_client_class=WaasClient,
        namespace="waas",
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
