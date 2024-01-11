#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_loadbalancer_backend_set
short_description: Manage a BackendSet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BackendSet resource in Oracle Cloud Infrastructure
    - For I(state=present), adds a backend set to a load balancer.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    policy:
        description:
            - The load balancer policy for the backend set. To get a list of available policies, use the
              L(ListPolicies,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerPolicy/ListPolicies) operation.
            - "Example: `LEAST_CONNECTIONS`"
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: str
    backends:
        description:
            - ""
            - Required for update using I(state=present) with name present.
        type: list
        elements: dict
        suboptions:
            ip_address:
                description:
                    - The IP address of the backend server.
                    - "Example: `10.0.0.3`"
                type: str
                required: true
            port:
                description:
                    - The communication port for the backend server.
                    - "Example: `8080`"
                type: int
                required: true
            weight:
                description:
                    - The load balancing policy weight assigned to the server. Backend servers with a higher weight receive a larger
                      proportion of incoming traffic. For example, a server weighted '3' receives 3 times the number of new connections
                      as a server weighted '1'.
                      For more information on load balancing policies, see
                      L(How Load Balancing Policies Work,https://docs.cloud.oracle.com/Content/Balance/Reference/lbpolicies.htm).
                    - "Example: `3`"
                type: int
            backup:
                description:
                    - "Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
                      traffic to this backend server unless all other backend servers not marked as \\"backup\\" fail the health check policy."
                    - "**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy."
                    - "Example: `false`"
                type: bool
            drain:
                description:
                    - "Whether the load balancer should drain this server. Servers marked \\"drain\\" receive no new
                      incoming traffic."
                    - "Example: `false`"
                type: bool
            offline:
                description:
                    - Whether the load balancer should treat this server as offline. Offline servers receive no incoming
                      traffic.
                    - "Example: `false`"
                type: bool
    health_checker:
        description:
            - ""
            - Required for create using I(state=present), update using I(state=present) with name present.
        type: dict
        suboptions:
            protocol:
                description:
                    - The protocol the health check must use; either HTTP or TCP.
                    - "Example: `HTTP`"
                type: str
                required: true
            url_path:
                description:
                    - The path against which to run the health check.
                    - "Example: `/healthcheck`"
                type: str
            port:
                description:
                    - The backend server port against which to run the health check. If the port is not specified, the load balancer uses the
                      port information from the `Backend` object.
                    - "Example: `8080`"
                type: int
            return_code:
                description:
                    - The status code a healthy backend server should return.
                    - "Example: `200`"
                type: int
            retries:
                description:
                    - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                      when recovering a server to the \\"healthy\\" state."
                    - "Example: `3`"
                type: int
            timeout_in_millis:
                description:
                    - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                      returns within this timeout period.
                    - "Example: `3000`"
                type: int
            interval_in_millis:
                description:
                    - The interval between health checks, in milliseconds.
                    - "Example: `10000`"
                type: int
            response_body_regex:
                description:
                    - A regular expression for parsing the response body from the backend server.
                    - "Example: `^((?!false).|\\\\s)*$`"
                type: str
    ssl_configuration:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            verify_depth:
                description:
                    - The maximum depth for peer certificate chain verification.
                    - "Example: `3`"
                type: int
            verify_peer_certificate:
                description:
                    - Whether the load balancer listener should verify peer certificates.
                    - "Example: `true`"
                type: bool
            trusted_certificate_authority_ids:
                description:
                    - Ids for OCI certificates service CA or CA bundles for the load balancer to trust.
                    - "Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`"
                type: list
                elements: str
            certificate_ids:
                description:
                    - Ids for OCI certificates service certificates. Currently only a single Id may be passed.
                    - "Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`"
                type: list
                elements: str
            certificate_name:
                description:
                    - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                      Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                      Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                    - "Example: `example_certificate_bundle`"
                type: str
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
                type: list
                elements: str
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
                type: str
            server_order_preference:
                description:
                    - When this attribute is set to ENABLED, the system gives preference to the server ciphers over the client
                      ciphers.
                    - "**Note:** This configuration is applicable only when the load balancer is acting as an SSL/HTTPS server. This
                                field is ignored when the `SSLConfiguration` object is associated with a backend set."
                type: str
                choices:
                    - "ENABLED"
                    - "DISABLED"
    session_persistence_configuration:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            cookie_name:
                description:
                    - "The name of the cookie used to detect a session initiated by the backend server. Use '*' to specify
                      that any cookie set by the backend causes the session to persist."
                    - "Example: `example_cookie`"
                type: str
                required: true
            disable_fallback:
                description:
                    - Whether the load balancer is prevented from directing traffic from a persistent session client to
                      a different backend server if the original server is unavailable. Defaults to false.
                    - "Example: `false`"
                type: bool
    lb_cookie_session_persistence_configuration:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
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
                type: str
            disable_fallback:
                description:
                    - Whether the load balancer is prevented from directing traffic from a persistent session client to
                      a different backend server if the original server is unavailable. Defaults to false.
                    - "Example: `false`"
                type: bool
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
                type: str
            path:
                description:
                    - The path in which the cookie is valid. The `Set-cookie header` inserted by the load balancer contains a `Path`
                      attribute with the specified value.
                    - Clients include the cookie in an HTTP request only if the path portion of the request-uri matches, or is a
                      subdirectory of, the cookie's `Path` attribute.
                    - The default value is `/`.
                    - "Example: `/example`"
                type: str
            max_age_in_seconds:
                description:
                    - The amount of time the cookie remains valid. The `Set-cookie` header inserted by the load balancer contains
                      a `Max-Age` attribute with the specified value.
                    - The specified value must be at least one second. There is no default value for this attribute. If you do not
                      specify a value, the load balancer does not include the `Max-Age` attribute in the `Set-cookie` header. In
                      most cases, the client or browser retains the cookie until the current session ends, as defined by the client.
                    - "Example: `3600`"
                type: int
            is_secure:
                description:
                    - Whether the `Set-cookie` header should contain the `Secure` attribute. If `true`, the `Set-cookie` header
                      inserted by the load balancer contains the `Secure` attribute, which directs the client or browser to send the
                      cookie only using a secure protocol.
                    - "**Note:** If you set this field to `true`, you cannot associate the corresponding backend set with an HTTP
                      listener."
                    - "Example: `true`"
                type: bool
            is_http_only:
                description:
                    - Whether the `Set-cookie` header should contain the `HttpOnly` attribute. If `true`, the `Set-cookie` header
                      inserted by the load balancer contains the `HttpOnly` attribute, which limits the scope of the cookie to HTTP
                      requests. This attribute directs the client or browser to omit the cookie when providing access to cookies
                      through non-HTTP APIs. For example, it restricts the cookie from JavaScript channels.
                    - "Example: `true`"
                type: bool
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer on which to add a backend set.
        type: str
        aliases: ["id"]
        required: true
    name:
        description:
            - A friendly name for the backend set. It must be unique and it cannot be changed.
            - Valid backend set names include only alphanumeric characters, dashes, and underscores. Backend set names cannot
              contain spaces. Avoid entering confidential information.
            - "Example: `example_backend_set`"
        type: str
        required: true
    state:
        description:
            - The state of the BackendSet.
            - Use I(state=present) to create or update a BackendSet.
            - Use I(state=absent) to delete a BackendSet.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create backend_set
  oci_loadbalancer_backend_set:
    # required
    policy: policy_example
    health_checker:
      # required
      protocol: protocol_example

      # optional
      url_path: url_path_example
      port: 56
      return_code: 56
      retries: 56
      timeout_in_millis: 56
      interval_in_millis: 56
      response_body_regex: response_body_regex_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    backends:
    - # required
      ip_address: ip_address_example
      port: 56

      # optional
      weight: 56
      backup: true
      drain: true
      offline: true
    ssl_configuration:
      # optional
      verify_depth: 56
      verify_peer_certificate: true
      trusted_certificate_authority_ids: [ "trusted_certificate_authority_ids_example" ]
      certificate_ids: [ "certificate_ids_example" ]
      certificate_name: certificate_name_example
      protocols: [ "protocols_example" ]
      cipher_suite_name: cipher_suite_name_example
      server_order_preference: ENABLED
    session_persistence_configuration:
      # required
      cookie_name: cookie_name_example

      # optional
      disable_fallback: true
    lb_cookie_session_persistence_configuration:
      # optional
      cookie_name: cookie_name_example
      disable_fallback: true
      domain: domain_example
      path: path_example
      max_age_in_seconds: 56
      is_secure: true
      is_http_only: true

- name: Update backend_set
  oci_loadbalancer_backend_set:
    # required
    policy: policy_example
    backends:
    - # required
      ip_address: ip_address_example
      port: 56

      # optional
      weight: 56
      backup: true
      drain: true
      offline: true
    health_checker:
      # required
      protocol: protocol_example

      # optional
      url_path: url_path_example
      port: 56
      return_code: 56
      retries: 56
      timeout_in_millis: 56
      interval_in_millis: 56
      response_body_regex: response_body_regex_example
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    ssl_configuration:
      # optional
      verify_depth: 56
      verify_peer_certificate: true
      trusted_certificate_authority_ids: [ "trusted_certificate_authority_ids_example" ]
      certificate_ids: [ "certificate_ids_example" ]
      certificate_name: certificate_name_example
      protocols: [ "protocols_example" ]
      cipher_suite_name: cipher_suite_name_example
      server_order_preference: ENABLED
    session_persistence_configuration:
      # required
      cookie_name: cookie_name_example

      # optional
      disable_fallback: true
    lb_cookie_session_persistence_configuration:
      # optional
      cookie_name: cookie_name_example
      disable_fallback: true
      domain: domain_example
      path: path_example
      max_age_in_seconds: 56
      is_secure: true
      is_http_only: true

- name: Delete backend_set
  oci_loadbalancer_backend_set:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

"""

RETURN = """
backend_set:
    description:
        - Details of the BackendSet resource acted upon by the current operation
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
            sample: name_example
        policy:
            description:
                - The load balancer policy for the backend set. To get a list of available policies, use the
                  L(ListPolicies,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerPolicy/ListPolicies) operation.
                - "Example: `LEAST_CONNECTIONS`"
            returned: on success
            type: str
            sample: policy_example
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
                    sample: name_example
                ip_address:
                    description:
                        - The IP address of the backend server.
                        - "Example: `10.0.0.3`"
                    returned: on success
                    type: str
                    sample: ip_address_example
                port:
                    description:
                        - The communication port for the backend server.
                        - "Example: `8080`"
                    returned: on success
                    type: int
                    sample: 56
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
                    sample: 56
                drain:
                    description:
                        - "Whether the load balancer should drain this server. Servers marked \\"drain\\" receive no new
                          incoming traffic."
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: true
                backup:
                    description:
                        - "Whether the load balancer should treat this server as a backup unit. If `true`, the load balancer forwards no ingress
                          traffic to this backend server unless all other backend servers not marked as \\"backup\\" fail the health check policy."
                        - "**Note:** You cannot add a backend server marked as `backup` to a backend set that uses the IP Hash policy."
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: true
                offline:
                    description:
                        - Whether the load balancer should treat this server as offline. Offline servers receive no incoming
                          traffic.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: true
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
                    sample: protocol_example
                url_path:
                    description:
                        - The path against which to run the health check.
                        - "Example: `/healthcheck`"
                    returned: on success
                    type: str
                    sample: url_path_example
                port:
                    description:
                        - The backend server port against which to run the health check. If the port is not specified, the load balancer uses the
                          port information from the `Backend` object.
                        - "Example: `8080`"
                    returned: on success
                    type: int
                    sample: 56
                return_code:
                    description:
                        - "The status code a healthy backend server should return. If you configure the health check policy to use the HTTP protocol,
                          you can use common HTTP status codes such as \\"200\\"."
                        - "Example: `200`"
                    returned: on success
                    type: int
                    sample: 56
                retries:
                    description:
                        - "The number of retries to attempt before a backend server is considered \\"unhealthy\\". This number also applies
                          when recovering a server to the \\"healthy\\" state. Defaults to 3."
                        - "Example: `3`"
                    returned: on success
                    type: int
                    sample: 56
                timeout_in_millis:
                    description:
                        - The maximum time, in milliseconds, to wait for a reply to a health check. A health check is successful only if a reply
                          returns within this timeout period. Defaults to 3000 (3 seconds).
                        - "Example: `3000`"
                    returned: on success
                    type: int
                    sample: 56
                interval_in_millis:
                    description:
                        - The interval between health checks, in milliseconds. The default is 10000 (10 seconds).
                        - "Example: `10000`"
                    returned: on success
                    type: int
                    sample: 56
                response_body_regex:
                    description:
                        - A regular expression for parsing the response body from the backend server.
                        - "Example: `^((?!false).|\\\\s)*$`"
                    returned: on success
                    type: str
                    sample: response_body_regex_example
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
                    sample: 56
                verify_peer_certificate:
                    description:
                        - Whether the load balancer listener should verify peer certificates.
                        - "Example: `true`"
                    returned: on success
                    type: bool
                    sample: true
                trusted_certificate_authority_ids:
                    description:
                        - Ids for OCI certificates service CA or CA bundles for the load balancer to trust.
                        - "Example: `[ocid1.cabundle.oc1.us-ashburn-1.amaaaaaaav3bgsaagl4zzyqdop5i2vuwoqewdvauuw34llqa74otq2jdsfyq]`"
                    returned: on success
                    type: list
                    sample: []
                certificate_ids:
                    description:
                        - Ids for OCI certificates service certificates. Currently only a single Id may be passed.
                        - "Example: `[ocid1.certificate.oc1.us-ashburn-1.amaaaaaaav3bgsaa5o2q7rh5nfmkkukfkogasqhk6af2opufhjlqg7m6jqzq]`"
                    returned: on success
                    type: list
                    sample: []
                certificate_name:
                    description:
                        - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                          Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                          Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                        - "Example: `example_certificate_bundle`"
                    returned: on success
                    type: str
                    sample: certificate_name_example
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
                    sample: cookie_name_example
                disable_fallback:
                    description:
                        - Whether the load balancer is prevented from directing traffic from a persistent session client to
                          a different backend server if the original server is unavailable. Defaults to false.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: true
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
                    sample: cookie_name_example
                disable_fallback:
                    description:
                        - Whether the load balancer is prevented from directing traffic from a persistent session client to
                          a different backend server if the original server is unavailable. Defaults to false.
                        - "Example: `false`"
                    returned: on success
                    type: bool
                    sample: true
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
                    sample: domain_example
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
                    sample: path_example
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
                    sample: 56
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
    sample: {
        "name": "name_example",
        "policy": "policy_example",
        "backends": [{
            "name": "name_example",
            "ip_address": "ip_address_example",
            "port": 56,
            "weight": 56,
            "drain": true,
            "backup": true,
            "offline": true
        }],
        "health_checker": {
            "protocol": "protocol_example",
            "url_path": "url_path_example",
            "port": 56,
            "return_code": 56,
            "retries": 56,
            "timeout_in_millis": 56,
            "interval_in_millis": 56,
            "response_body_regex": "response_body_regex_example"
        },
        "ssl_configuration": {
            "verify_depth": 56,
            "verify_peer_certificate": true,
            "trusted_certificate_authority_ids": [],
            "certificate_ids": [],
            "certificate_name": "certificate_name_example",
            "server_order_preference": "ENABLED",
            "cipher_suite_name": "cipher_suite_name_example",
            "protocols": []
        },
        "session_persistence_configuration": {
            "cookie_name": "cookie_name_example",
            "disable_fallback": true
        },
        "lb_cookie_session_persistence_configuration": {
            "cookie_name": "cookie_name_example",
            "disable_fallback": true,
            "domain": "domain_example",
            "path": "path_example",
            "max_age_in_seconds": 56,
            "is_secure": true,
            "is_http_only": true
        }
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
    from oci.load_balancer.models import CreateBackendSetDetails
    from oci.load_balancer.models import UpdateBackendSetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BackendSetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(BackendSetHelperGen, self).get_possible_entity_types() + [
            "backendset",
            "backendsets",
            "loadBalancerbackendset",
            "loadBalancerbackendsets",
            "backendsetresource",
            "backendsetsresource",
            "loadbalancer",
        ]

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_backend_set

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_backend_set,
            load_balancer_id=self.module.params.get("load_balancer_id"),
            backend_set_name=self.module.params.get("name"),
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
        return oci_common_utils.list_all_resources(
            self.client.list_backend_sets, **kwargs
        )

    def get_create_model_class(self):
        return CreateBackendSetDetails

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
            call_fn=self.client.create_backend_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_backend_set_details=create_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBackendSetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_backend_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_backend_set_details=update_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
                backend_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_backend_set,
            call_fn_args=(),
            call_fn_kwargs=dict(
                load_balancer_id=self.module.params.get("load_balancer_id"),
                backend_set_name=self.module.params.get("name"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BackendSetHelperCustom = get_custom_class("BackendSetHelperCustom")


class ResourceHelper(BackendSetHelperCustom, BackendSetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            policy=dict(type="str"),
            backends=dict(
                type="list",
                elements="dict",
                options=dict(
                    ip_address=dict(type="str", required=True),
                    port=dict(type="int", required=True),
                    weight=dict(type="int"),
                    backup=dict(type="bool"),
                    drain=dict(type="bool"),
                    offline=dict(type="bool"),
                ),
            ),
            health_checker=dict(
                type="dict",
                options=dict(
                    protocol=dict(type="str", required=True),
                    url_path=dict(type="str"),
                    port=dict(type="int"),
                    return_code=dict(type="int"),
                    retries=dict(type="int"),
                    timeout_in_millis=dict(type="int"),
                    interval_in_millis=dict(type="int"),
                    response_body_regex=dict(type="str"),
                ),
            ),
            ssl_configuration=dict(
                type="dict",
                options=dict(
                    verify_depth=dict(type="int"),
                    verify_peer_certificate=dict(type="bool"),
                    trusted_certificate_authority_ids=dict(type="list", elements="str"),
                    certificate_ids=dict(type="list", elements="str"),
                    certificate_name=dict(type="str"),
                    protocols=dict(type="list", elements="str"),
                    cipher_suite_name=dict(type="str"),
                    server_order_preference=dict(
                        type="str", choices=["ENABLED", "DISABLED"]
                    ),
                ),
            ),
            session_persistence_configuration=dict(
                type="dict",
                options=dict(
                    cookie_name=dict(type="str", required=True),
                    disable_fallback=dict(type="bool"),
                ),
            ),
            lb_cookie_session_persistence_configuration=dict(
                type="dict",
                options=dict(
                    cookie_name=dict(type="str"),
                    disable_fallback=dict(type="bool"),
                    domain=dict(type="str"),
                    path=dict(type="str"),
                    max_age_in_seconds=dict(type="int"),
                    is_secure=dict(type="bool"),
                    is_http_only=dict(type="bool"),
                ),
            ),
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="backend_set",
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
