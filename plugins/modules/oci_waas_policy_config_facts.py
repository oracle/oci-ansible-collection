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
module: oci_waas_policy_config_facts
short_description: Fetches details about a PolicyConfig resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a PolicyConfig resource in Oracle Cloud Infrastructure
    - Gets the configuration of a WAAS policy.
version_added: "2.9"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific policy_config
  oci_waas_policy_config_facts:
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
policy_config:
    description:
        - PolicyConfig resource
    returned: on success
    type: complex
    contains:
        certificate_id:
            description:
                - The OCID of the SSL certificate to use if HTTPS is supported.
            returned: on success
            type: string
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
                  The TLS protocol is negotiated while the request is connecting and the most recent protocol supported by both the edge node and client browser
                  will be selected. If no such version exists, the connection will be aborted.
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
                - "Enable or disable GZIP compression of origin responses. If enabled, the header `Accept-Encoding: gzip` is sent to origin, otherwise, the
                  empty `Accept-Encoding:` header is used."
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
                - The edge node reads this header and its value and sets the client IP address as specified. It does not create the header if the header is not
                  present in the request. If the header is not present, the connecting IP address will be used as the client's true IP address. It uses the last
                  IP address in the header's value as the true IP address.
                - "Example: `X-Client-Ip: 11.1.1.1, 13.3.3.3`"
                - In the case of multiple headers with the same name, only the first header will be used. It is assumed that CDN sets the correct client IP
                  address to prevent spoofing.
                - "- **X_FORWARDED_FOR:** Corresponds to `X-Forwarded-For` header name."
                - "- **X_CLIENT_IP:** Corresponds to `X-Client-Ip` header name."
                - "- **X_REAL_IP:** Corresponds to `X-Real-Ip` header name."
                - "- **CLIENT_IP:** Corresponds to `Client-Ip` header name."
                - "- **TRUE_CLIENT_IP:** Corresponds to `True-Client-Ip` header name."
            returned: on success
            type: string
            sample: "X-Client-Ip: 11.1.1.1, 13.3.3.3"
        is_cache_control_respected:
            description:
                - "Enable or disable automatic content caching based on the response `cache-control` header. This feature enables the origin to act as a proxy
                  cache. Caching is usually defined using `cache-control` header. For example `cache-control: max-age=120` means that the returned resource is
                  valid for 120 seconds. Caching rules will overwrite this setting."
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
                - "The set cipher group for the configured TLS protocol. This sets the configuration for the TLS connections between clients and edge nodes
                  only.
                  - **DEFAULT:** Cipher group supports TLS 1.0, TLS 1.1, TLS 1.2, TLS 1.3 protocols. It has the following ciphers enabled: `ECDHE-RSA-
                    AES128-GCM-SHA256:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384:DHE-RSA-AES128-GCM-SHA256:DHE-DSS-
                    AES128-GCM-SHA256:kEDH+AESGCM:ECDHE-RSA-AES128-SHA256:ECDHE-ECDSA-AES128-SHA256:ECDHE-RSA-AES128-SHA:ECDHE-ECDSA-AES128-SHA:ECDHE-RSA-
                    AES256-SHA384:ECDHE-ECDSA-AES256-SHA384:ECDHE-RSA-AES256-SHA:ECDHE-ECDSA-AES256-SHA:DHE-RSA-AES128-SHA256:DHE-RSA-AES128-SHA:DHE-DSS-
                    AES128-SHA256:DHE-RSA-AES256-SHA256:DHE-DSS-AES256-SHA:DHE-RSA-AES256-SHA:AES128-GCM-SHA256:AES256-GCM-
                    SHA384:AES128-SHA256:AES256-SHA256:AES128-SHA:AES256-SHA:AES:CAMELLIA:!DES-CBC3-SHA:!aNULL:!eNULL:!EXPORT:!DES:!RC4:!MD5:!PSK:!aECDH:!EDH-
                    DSS-DES-CBC3-SHA:!EDH-RSA-DES-CBC3-SHA:!KRB5-DES-CBC3-SHA`"
            returned: on success
            type: string
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
                        - "- **IP_HASH:** All the incoming requests from the same client IP address should go to the same content origination server. IP_HASH
                          load balancing method uses origin weights when choosing which origin should the hash be assigned to initially."
                        - "- **ROUND_ROBIN:** Forwards requests sequentially to the available origin servers. The first request - to the first origin server,
                          the second request - to the next origin server, and so on. After it sends a request to the last origin server, it starts again with
                          the first origin server. When using weights on origins, Weighted Round Robin assigns more requests to origins with a greater weight.
                          Over a period of time, origins will receive a number of requests in proportion to their weight."
                        - "- **STICKY_COOKIE:** Adds a session cookie to the first response from the origin server and identifies the server that sent the
                          response. The client's next request contains the cookie value, and nginx routes the request to the origin server that responded to the
                          first request. STICKY_COOKIE load balancing method falls back to Round Robin for the first request."
                    returned: on success
                    type: string
                    sample: ROUND_ROBIN
                name:
                    description:
                        - The name of the cookie used to track the persistence.
                          Can contain any US-ASCII character except separator or control character.
                    returned: on success
                    type: string
                    sample: name_example
                domain:
                    description:
                        - The domain for which the cookie is set, defaults to WAAS policy domain.
                    returned: on success
                    type: string
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
                - ModSecurity is not capable to inspect WebSockets. Therefore paths specified here have WAF disabled if Connection request header from the
                  client has the value Upgrade (case insensitive matching) and Upgrade request header has the value websocket (case insensitive matching). Paths
                  matches if the concatenation of request URL path and query starts with the contents of the one of `websocketPathPrefixes` array value. In All
                  other cases challenges, like JSC, HIC and etc., remain active.
            returned: on success
            type: list
            sample: []
        is_sni_enabled:
            description:
                - SNI stands for Server Name Indication and is an extension of the TLS protocol. It indicates which hostname is being contacted by the browser
                  at the beginning of the 'handshake'-process. This allows a server to connect multiple SSL Certificates to one IP address and port.
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
                    type: string
                    sample: GET
                path:
                    description:
                        - Path to visit on your origins when performing the health check.
                    returned: on success
                    type: string
                    sample: path_example
                headers:
                    description:
                        - "HTTP header fields to include in health check requests, expressed as `\\"name\\": \\"value\\"` properties. Because HTTP header field
                          names are case-insensitive, any use of names that are case-insensitive equal to other names will be rejected. If Host is not
                          specified, requests will include a Host header field with value matching the policy's protected domain. If User-Agent is not
                          specified, requests will include a User-Agent header field with value \\"waf health checks\\"."
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
                        - Health check will search for the given text in a case-sensitive manner within the response body and will fail if the text is not
                          found.
                    returned: on success
                    type: string
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
    sample: {
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
            "method": "ROUND_ROBIN",
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PolicyConfigFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "waas_policy_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_policy_config,
            waas_policy_id=self.module.params.get("waas_policy_id"),
        )


PolicyConfigFactsHelperCustom = get_custom_class("PolicyConfigFactsHelperCustom")


class ResourceFactsHelper(PolicyConfigFactsHelperCustom, PolicyConfigFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(waas_policy_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="policy_config",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(policy_config=result)


if __name__ == "__main__":
    main()
