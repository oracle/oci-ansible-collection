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
module: oci_loadbalancer_backend_set_facts
short_description: Fetches details about one or multiple BackendSet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BackendSet resources in Oracle Cloud Infrastructure
    - Lists all backend sets associated with a given load balancer.
    - If I(backend_set_name) is specified, the details of a single BackendSet will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the specified load balancer.
        type: str
        aliases: ["id"]
        required: true
    backend_set_name:
        description:
            - The name of the backend set to retrieve.
            - "Example: `example_backend_set`"
            - Required to get a specific backend_set.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List backend_sets
  oci_loadbalancer_backend_set_facts:
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific backend_set
  oci_loadbalancer_backend_set_facts:
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    backend_set_name: example_backend_set

"""

RETURN = """
backend_sets:
    description:
        - List of BackendSet resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - A friendly name for the backend set. It must be unique and it cannot be changed.
                - Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
                  contain spaces. Avoid entering confidential information.
                - "Example: `example_backend_set`"
            returned: on success
            type: str
            sample: example_backend_set
        policy:
            description:
                - The load balancer policy for the backend set. To get a list of available policies, use the
                  L(ListPolicies,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerPolicy/ListPolicies) operation.
                - "Example: `LEAST_CONNECTIONS`"
            returned: on success
            type: str
            sample: LEAST_CONNECTIONS
        backends:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A read-only field showing the IP address and port that uniquely identify this backend server in the backend set.
                        - "Example: `10.0.0.3:8080`"
                    returned: on success
                    type: str
                    sample: 10.0.0.3:8080
                ip_address:
                    description:
                        - The IP address of the backend server.
                        - "Example: `10.0.0.3`"
                    returned: on success
                    type: str
                    sample: 10.0.0.3
                port:
                    description:
                        - The communication port for the backend server.
                        - "Example: `8080`"
                    returned: on success
                    type: int
                    sample: 8080
                weight:
                    description:
                        - The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
                          proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
                          as a server weighted '1'.
                          For more information on load balancing policies, see
                          L(How Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
                        - "Example: `3`"
                    returned: on success
                    type: int
                    sample: 3
                drain:
                    description:
                        - "Whether the load balancer should drain this server. Servers marked \\"drain\\" receive no new
                          incoming traffic."
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
                backup:
                    description:
                        - "Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
                          traffic to this backend server unless all other backend servers not marked as \\"backup\\" fail the health check policy."
                        - "**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy."
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
                offline:
                    description:
                        - Whether the load balancer should treat this server as offline. Offline servers receive no incoming
                          traffic.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
        health_checker:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                protocol:
                    description:
                        - The protocol the health check must use; either HTTP or TCP.
                        - "Example: `HTTP`"
                    returned: on success
                    type: str
                    sample: HTTP
                url_path:
                    description:
                        - The path against which to run the health check.
                        - "Example: `/healthcheck`"
                    returned: on success
                    type: str
                    sample: /healthcheck
                port:
                    description:
                        - The backend server port against which to run the health check. If the port is not specified, the load balancer uses the
                          port information from the `Backend` object.
                        - "Example: `8080`"
                    returned: on success
                    type: int
                    sample: 0
                return_code:
                    description:
                        - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                          you can use common HTTP status codes such as \\"200\\"."
                        - "Example: `200`"
                    returned: on success
                    type: int
                    sample: 0
                retries:
                    description:
                        - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                          when recovering a server to the \\"healthy\\" state. Defaults to 3."
                        - "Example: `3`"
                    returned: on success
                    type: int
                    sample: 3
                timeout_in_millis:
                    description:
                        - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                          returns within this timeout period. Defaults to 3000 (3 seconds).
                        - "Example: `3000`"
                    returned: on success
                    type: int
                    sample: 3000
                interval_in_millis:
                    description:
                        - The interval between health checks, in milliseconds. The default is 10000 (10 seconds).
                        - "Example: `10000`"
                    returned: on success
                    type: int
                    sample: 10000
                response_body_regex:
                    description:
                        - A regular expression for parsing the response body from the backend server.
                        - "Example: `^((?!false).|\\\\s)*$`"
                    returned: on success
                    type: str
                    sample: "^((?!false).|\\\\s)*$"
        ssl_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                verify_depth:
                    description:
                        - The maximum depth for peer certificate chain verification.
                        - "Example: `3`"
                    returned: on success
                    type: int
                    sample: 3
                verify_peer_certificate:
                    description:
                        - Whether the load balancer listener should verify peer certificates.
                        - "Example: `true`"
                    returned: on success
                    type: bool
                    sample: true
                certificate_name:
                    description:
                        - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                          Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                          Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                        - "Example: `example_certificate_bundle`"
                    returned: on success
                    type: str
                    sample: example_certificate_bundle
                server_order_preference:
                    description:
                        - When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client
                          ciphers.
                        - "**Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This
                                    field is ignored when the `SSLConfiguration` object is associated with a backend set."
                    returned: on success
                    type: str
                    sample: ENABLED
                cipher_suite_name:
                    description:
                        - The name of the cipher suite to use for HTTPS or SSL connections.
                        - If this field is not specified, the default is `oci-default-ssl-cipher-suite-v1`.
                        - "**Notes:**"
                        - "*  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
                             suite. Clients cannot perform an SSL handshake if there is an incompatible configuration.
                          *  You must ensure compatibility between the ciphers configured in the cipher suite and the configured
                             certificates. For example, RSA-based ciphers require RSA certificates and ECDSA-based ciphers require ECDSA
                             certificates.
                          *  If the cipher configuration is not modified after load balancer creation, the `GET` operation returns
                             `oci-default-ssl-cipher-suite-v1` as the value of this field in the SSL configuration for existing listeners
                             that predate this feature.
                          *  If the cipher configuration was modified using Oracle operations after load balancer creation, the `GET`
                             operation returns `oci-customized-ssl-cipher-suite` as the value of this field in the SSL configuration for
                             existing listeners that predate this feature.
                          *  The `GET` operation returns `oci-wider-compatible-ssl-cipher-suite-v1` as the value of this field in the SSL
                             configuration for existing backend sets that predate this feature.
                          *  If the `GET` operation on a listener returns `oci-customized-ssl-cipher-suite` as the value of this field,
                             you must specify an appropriate predefined or custom cipher suite name when updating the resource.
                          *  The `oci-customized-ssl-cipher-suite` Oracle reserved cipher suite name is not accepted as valid input for
                             this field."
                        - "example: `example_cipher_suite`"
                    returned: on success
                    type: str
                    sample: cipher_suite_name_example
                protocols:
                    description:
                        - A list of SSL protocols the load balancer must support for HTTPS or SSL connections.
                        - The load balancer uses SSL protocols to establish a secure connection between a client and a server. A secure
                          connection ensures that all data passed between the client and the server is private.
                        - "The Load Balancing service supports the following protocols:"
                        - "*  TLSv1
                          *  TLSv1.1
                          *  TLSv1.2"
                        - If this field is not specified, TLSv1.2 is the default.
                        - "**Warning:** All SSL listeners created on a given port must use the same set of SSL protocols."
                        - "**Notes:**"
                        - "*  The handshake to establish an SSL connection fails if the client supports none of the specified protocols.
                          *  You must ensure compatibility between the specified SSL protocols and the ciphers configured in the cipher
                             suite.
                          *  For all existing load balancer listeners and backend sets that predate this feature, the `GET` operation
                             displays a list of SSL protocols currently used by those resources."
                        - "example: `[\\"TLSv1.1\\", \\"TLSv1.2\\"]`"
                    returned: on success
                    type: list
                    sample: []
        session_persistence_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                cookie_name:
                    description:
                        - "The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
                          that any cookie set by the backend causes the session to persist."
                        - "Example: `example_cookie`"
                    returned: on success
                    type: str
                    sample: example_cookie
                disable_fallback:
                    description:
                        - Whether the load balancer is prevented from directing traffic from a persistent session client to
                          a different backend server if the original server is unavailable. Defaults to false.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
        lb_cookie_session_persistence_configuration:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                cookie_name:
                    description:
                        - "The name of the cookie inserted by the load balancer. If this field is not configured, the cookie name defaults
                          to \\"X-Oracle-BMC-LBS-Route\\"."
                        - "Example: `example_cookie`"
                        - "**Notes:**"
                        - "*  Ensure that the cookie name used at the backend application servers is different from the cookie name used
                             at the load balancer. To minimize the chance of name collision, Oracle recommends that you use a prefix
                             such as \\"X-Oracle-OCI-\\" for this field."
                        - "*  If a backend server and the load balancer both insert cookies with the same name, the client or browser
                             behavior can vary depending on the domain and path values associated with the cookie. If the name, domain,
                             and path values of the `Set-cookie` generated by a backend server and the `Set-cookie` generated by the
                             load balancer are all the same, the client or browser treats them as one cookie and returns only one of
                             the cookie values in subsequent requests. If both `Set-cookie` names are the same, but the domain and path
                             names are different, the client or browser treats them as two different cookies."
                    returned: on success
                    type: str
                    sample: example_cookie
                disable_fallback:
                    description:
                        - Whether the load balancer is prevented from directing traffic from a persistent session client to
                          a different backend server if the original server is unavailable. Defaults to false.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: false
                domain:
                    description:
                        - The domain in which the cookie is valid. The `Set-cookie` header inserted by the load balancer contains a
                          domain attribute with the specified value.
                        - This attribute has no default value. If you do not specify a value, the load balancer does not insert the domain
                          attribute into the `Set-cookie` header.
                        - "**Notes:**"
                        - "*  L(RFC 6265 - HTTP State Management Mechanism,https://www.ietf.org/rfc/rfc6265.txt) describes client and
                             browser behavior when the domain attribute is present or not present in the `Set-cookie` header."
                        -    If the value of the `Domain` attribute is `example.com` in the `Set-cookie` header, the client includes
                             the same cookie in the `Cookie` header when making HTTP requests to `example.com`, `www.example.com`, and
                             `www.abc.example.com`. If the `Domain` attribute is not present, the client returns the cookie only for
                             the domain to which the original request was made.
                        - "*  Ensure that this attribute specifies the correct domain value. If the `Domain` attribute in the `Set-cookie`
                             header does not include the domain to which the original request was made, the client or browser might reject
                             the cookie. As specified in RFC 6265, the client accepts a cookie with the `Domain` attribute value `example.com`
                             or `www.example.com` sent from `www.example.com`. It does not accept a cookie with the `Domain` attribute
                             `abc.example.com` or `www.abc.example.com` sent from `www.example.com`."
                        - "Example: `example.com`"
                    returned: on success
                    type: str
                    sample: example.com
                path:
                    description:
                        - The path in which the cookie is valid. The `Set-cookie header` inserted by the load balancer contains a `Path`
                          attribute with the specified value.
                        - Clients include the cookie in an HTTP request only if the path portion of the request-uri matches, or is a
                          subdirectory of, the cookie's `Path` attribute.
                        - The default value is `/`.
                        - "Example: `/example`"
                    returned: on success
                    type: str
                    sample: /example
                max_age_in_seconds:
                    description:
                        - The amount of time the cookie remains valid. The `Set-cookie` header inserted by the load balancer contains
                          a `Max-Age` attribute with the specified value.
                        - The specified value must be at least one second. There is no default value for this attribute. If you do not
                          specify a value, the load balancer does not include the `Max-Age` attribute in the `Set-cookie` header. In
                          most cases, the client or browser retains the cookie until the current session ends, as defined by the client.
                        - "Example: `3600`"
                    returned: on success
                    type: int
                    sample: 3600
                is_secure:
                    description:
                        - Whether the `Set-cookie` header should contain the `Secure` attribute. If `true`, the `Set-cookie` header
                          inserted by the load balancer contains the `Secure` attribute, which directs the client or browser to send the
                          cookie only using a secure protocol.
                        - "**Note:** If you set this field to `true`, you cannot associate the corresponding backend set with an HTTP
                          listener."
                        - "Example: `true`"
                    returned: on success
                    type: bool
                    sample: true
                is_http_only:
                    description:
                        - Whether the `Set-cookie` header should contain the `HttpOnly` attribute. If `true`, the `Set-cookie` header
                          inserted by the load balancer contains the `HttpOnly` attribute, which limits the scope of the cookie to HTTP
                          requests. This attribute directs the client or browser to omit the cookie when providing access to cookies
                          through non-HTTP APIs. For example, it restricts the cookie from JavaScript channels.
                        - "Example: `true`"
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
        "name": "example_backend_set",
        "policy": "LEAST_CONNECTIONS",
        "backends": [{
            "name": "10.0.0.3:8080",
            "ip_address": "10.0.0.3",
            "port": 8080,
            "weight": 3,
            "drain": false,
            "backup": false,
            "offline": false
        }],
        "health_checker": {
            "protocol": "HTTP",
            "url_path": "/healthcheck",
            "port": 0,
            "return_code": 0,
            "retries": 3,
            "timeout_in_millis": 3000,
            "interval_in_millis": 10000,
            "response_body_regex": "^((?!false).|\\\\s)*$"
        },
        "ssl_configuration": {
            "verify_depth": 3,
            "verify_peer_certificate": true,
            "certificate_name": "example_certificate_bundle",
            "server_order_preference": "ENABLED",
            "cipher_suite_name": "cipher_suite_name_example",
            "protocols": []
        },
        "session_persistence_configuration": {
            "cookie_name": "example_cookie",
            "disable_fallback": false
        },
        "lb_cookie_session_persistence_configuration": {
            "cookie_name": "example_cookie",
            "disable_fallback": false,
            "domain": "example.com",
            "path": "/example",
            "max_age_in_seconds": 3600,
            "is_secure": true,
            "is_http_only": true
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.load_balancer import LoadBalancerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackendSetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "load_balancer_id",
            "backend_set_name",
        ]

    def get_required_params_for_list(self):
        return [
            "load_balancer_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend_set,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("backend_set_name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_backend_sets,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            **optional_kwargs
        )


BackendSetFactsHelperCustom = get_custom_class("BackendSetFactsHelperCustom")


class ResourceFactsHelper(BackendSetFactsHelperCustom, BackendSetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
            backend_set_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="backend_set",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(backend_sets=result)


if __name__ == "__main__":
    main()
