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
module: oci_loadbalancer_network_security_groups
short_description: Manage a NetworkSecurityGroups resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a NetworkSecurityGroups resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    network_security_group_ids:
        description:
            - An array of NSG L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated with the load
              balancer.
            - During the load balancer's creation, the service adds the new load balancer to the specified NSGs.
            - "The benefits of associating the load balancer with NSGs include:"
            - "*  NSGs define network security rules to govern ingress and egress traffic for the load balancer."
            - "*  The network security rules of other resources can reference the NSGs associated with the load balancer
                 to ensure access."
            - This parameter is updatable.
        type: list
        elements: str
    load_balancer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer to update the NSGs for.
        type: str
        aliases: ["id"]
        required: true
    state:
        description:
            - The state of the NetworkSecurityGroups.
            - Use I(state=present) to update an existing a NetworkSecurityGroups.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update network_security_groups
  oci_loadbalancer_network_security_groups:
    # required
    load_balancer_id: "ocid1.loadbalancer.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    network_security_group_ids: [ "network_security_group_ids_example" ]

"""

RETURN = """
load_balancer:
    description:
        - Details of the NetworkSecurityGroups resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the load balancer.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the load balancer.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                - "Example: `example_load_balancer`"
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the load balancer.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the load balancer was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        ip_addresses:
            description:
                - An array of IP addresses.
            returned: on success
            type: complex
            contains:
                ip_address:
                    description:
                        - An IP address.
                        - "Example: `192.168.0.3`"
                    returned: on success
                    type: str
                    sample: ip_address_example
                is_public:
                    description:
                        - Whether the IP address is public or private.
                        - "If \\"true\\", the IP address is public and accessible from the internet."
                        - "If \\"false\\", the IP address is private and accessible only from within the associated VCN."
                    returned: on success
                    type: bool
                    sample: true
                reserved_ip:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - ""
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        shape_name:
            description:
                - A template that determines the total pre-provisioned bandwidth (ingress plus egress).
                  To get a list of available shapes, use the L(ListShapes,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerShape/ListShapes)
                  operation.
                - "Example: `100Mbps`"
            returned: on success
            type: str
            sample: shape_name_example
        shape_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                minimum_bandwidth_in_mbps:
                    description:
                        - Bandwidth in Mbps that determines the total pre-provisioned bandwidth (ingress plus egress).
                          The values must be between 10 and the maximumBandwidthInMbps.
                        - "Example: `150`"
                    returned: on success
                    type: int
                    sample: 56
                maximum_bandwidth_in_mbps:
                    description:
                        - Bandwidth in Mbps that determines the maximum bandwidth (ingress plus egress) that the load balancer can
                          achieve. This bandwidth cannot be always guaranteed. For a guaranteed bandwidth use the minimumBandwidthInMbps
                          parameter.
                        - The values must be between minimumBandwidthInMbps and 8192 (8Gbps).
                        - "Example: `1500`"
                    returned: on success
                    type: int
                    sample: 56
        is_private:
            description:
                - Whether the load balancer has a VCN-local (private) IP address.
                - "If \\"true\\", the service assigns a private IP address to the load balancer."
                - "If \\"false\\", the service assigns a public IP address to the load balancer."
                - A public load balancer is accessible from the internet, depending on your VCN's
                  L(security list rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securitylists.htm). For more information about public and
                  private load balancers, see L(How Load Balancing Works,https://docs.cloud.oracle.com/Content/Balance/Concepts/balanceoverview.htm#how-load-
                  balancing-works).
                - "Example: `true`"
            returned: on success
            type: bool
            sample: true
        subnet_ids:
            description:
                - An array of subnet L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: list
            sample: []
        network_security_group_ids:
            description:
                - An array of NSG L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) associated with the load
                  balancer.
                - During the load balancer's creation, the service adds the new load balancer to the specified NSGs.
                - "The benefits of associating the load balancer with NSGs include:"
                - "*  NSGs define network security rules to govern ingress and egress traffic for the load balancer."
                - "*  The network security rules of other resources can reference the NSGs associated with the load balancer
                     to ensure access."
                - "Example: [\\"ocid1.nsg.oc1.phx.unique_ID\\"]"
            returned: on success
            type: list
            sample: []
        listeners:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A friendly name for the listener. It must be unique and it cannot be changed.
                        - "Example: `example_listener`"
                    returned: on success
                    type: str
                    sample: name_example
                default_backend_set_name:
                    description:
                        - The name of the associated backend set.
                        - "Example: `example_backend_set`"
                    returned: on success
                    type: str
                    sample: default_backend_set_name_example
                port:
                    description:
                        - The communication port for the listener.
                        - "Example: `80`"
                    returned: on success
                    type: int
                    sample: 56
                protocol:
                    description:
                        - The protocol on which the listener accepts connection requests.
                          To get a list of valid protocols, use the L(ListProtocols,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/loadbalancer/20170115/LoadBalancerProtocol/ListProtocols)
                          operation.
                        - "Example: `HTTP`"
                    returned: on success
                    type: str
                    sample: protocol_example
                hostname_names:
                    description:
                        - An array of hostname resource names.
                    returned: on success
                    type: list
                    sample: []
                path_route_set_name:
                    description:
                        - Deprecated. Please use `routingPolicies` instead.
                        - The name of the set of path-based routing rules, L(PathRouteSet,https://docs.cloud.oracle.com/en-
                          us/iaas/api/#/en/loadbalancer/20170115/PathRouteSet/),
                          applied to this listener's traffic.
                        - "Example: `example_path_route_set`"
                    returned: on success
                    type: str
                    sample: path_route_set_name_example
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
                connection_configuration:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        idle_timeout:
                            description:
                                - The maximum idle time, in seconds, allowed between two successive receive or two successive send operations
                                  between the client and backend servers. A send operation does not reset the timer for receive operations. A
                                  receive operation does not reset the timer for send operations.
                                - For more information, see L(Connection
                                  Configuration,https://docs.cloud.oracle.com/Content/Balance/Reference/connectionreuse.htm#ConnectionConfiguration).
                                - "Example: `1200`"
                            returned: on success
                            type: int
                            sample: 56
                        backend_tcp_proxy_protocol_version:
                            description:
                                - The backend TCP Proxy Protocol version.
                                - "Example: `1`"
                            returned: on success
                            type: int
                            sample: 56
                rule_set_names:
                    description:
                        - The names of the L(rule sets,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/loadbalancer/20170115/RuleSet/) to apply to the
                          listener.
                        - "Example: [\\"example_rule_set\\"]"
                    returned: on success
                    type: list
                    sample: []
                routing_policy_name:
                    description:
                        - The name of the routing policy applied to this listener's traffic.
                        - "Example: `example_routing_policy_name`"
                    returned: on success
                    type: str
                    sample: routing_policy_name_example
        hostnames:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A friendly name for the hostname resource. It must be unique and it cannot be changed. Avoid entering confidential
                          information.
                        - "Example: `example_hostname_001`"
                    returned: on success
                    type: str
                    sample: name_example
                hostname:
                    description:
                        - A virtual hostname. For more information about virtual hostname string construction, see
                          L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm#routing).
                        - "Example: `app.example.com`"
                    returned: on success
                    type: str
                    sample: hostname_example
        ssl_cipher_suites:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A friendly name for the SSL cipher suite. It must be unique and it cannot be changed.
                        - "**Note:** The name of your user-defined cipher suite must not be the same as any of Oracle's predefined or
                                    reserved SSL cipher suite names:"
                        - "* oci-default-ssl-cipher-suite-v1
                          * oci-modern-ssl-cipher-suite-v1
                          * oci-compatible-ssl-cipher-suite-v1
                          * oci-wider-compatible-ssl-cipher-suite-v1
                          * oci-customized-ssl-cipher-suite"
                        - "example: `example_cipher_suite`"
                    returned: on success
                    type: str
                    sample: name_example
                ciphers:
                    description:
                        - A list of SSL ciphers the load balancer must support for HTTPS or SSL connections.
                        - "The following ciphers are valid values for this property:"
                        - "*  __TLSv1.2 ciphers__"
                        - "       \\"AES128-GCM-SHA256\\"
                                  \\"AES128-SHA256\\"
                                  \\"AES256-GCM-SHA384\\"
                                  \\"AES256-SHA256\\"
                                  \\"DH-DSS-AES128-GCM-SHA256\\"
                                  \\"DH-DSS-AES128-SHA256\\"
                                  \\"DH-DSS-AES256-GCM-SHA384\\"
                                  \\"DH-DSS-AES256-SHA256\\"
                                  \\"DH-RSA-AES128-GCM-SHA256\\"
                                  \\"DH-RSA-AES128-SHA256\\"
                                  \\"DH-RSA-AES256-GCM-SHA384\\"
                                  \\"DH-RSA-AES256-SHA256\\"
                                  \\"DHE-DSS-AES128-GCM-SHA256\\"
                                  \\"DHE-DSS-AES128-SHA256\\"
                                  \\"DHE-DSS-AES256-GCM-SHA384\\"
                                  \\"DHE-DSS-AES256-SHA256\\"
                                  \\"DHE-RSA-AES128-GCM-SHA256\\"
                                  \\"DHE-RSA-AES128-SHA256\\"
                                  \\"DHE-RSA-AES256-GCM-SHA384\\"
                                  \\"DHE-RSA-AES256-SHA256\\"
                                  \\"ECDH-ECDSA-AES128-GCM-SHA256\\"
                                  \\"ECDH-ECDSA-AES128-SHA256\\"
                                  \\"ECDH-ECDSA-AES256-GCM-SHA384\\"
                                  \\"ECDH-ECDSA-AES256-SHA384\\"
                                  \\"ECDH-RSA-AES128-GCM-SHA256\\"
                                  \\"ECDH-RSA-AES128-SHA256\\"
                                  \\"ECDH-RSA-AES256-GCM-SHA384\\"
                                  \\"ECDH-RSA-AES256-SHA384\\"
                                  \\"ECDHE-ECDSA-AES128-GCM-SHA256\\"
                                  \\"ECDHE-ECDSA-AES128-SHA256\\"
                                  \\"ECDHE-ECDSA-AES256-GCM-SHA384\\"
                                  \\"ECDHE-ECDSA-AES256-SHA384\\"
                                  \\"ECDHE-RSA-AES128-GCM-SHA256\\"
                                  \\"ECDHE-RSA-AES128-SHA256\\"
                                  \\"ECDHE-RSA-AES256-GCM-SHA384\\"
                                  \\"ECDHE-RSA-AES256-SHA384\\""
                        - "*  __TLSv1 ciphers also supported by TLSv1.2__"
                        - "       \\"AES128-SHA\\"
                                  \\"AES256-SHA\\"
                                  \\"CAMELLIA128-SHA\\"
                                  \\"CAMELLIA256-SHA\\"
                                  \\"DES-CBC3-SHA\\"
                                  \\"DH-DSS-AES128-SHA\\"
                                  \\"DH-DSS-AES256-SHA\\"
                                  \\"DH-DSS-CAMELLIA128-SHA\\"
                                  \\"DH-DSS-CAMELLIA256-SHA\\"
                                  \\"DH-DSS-DES-CBC3-SHAv\\"
                                  \\"DH-DSS-SEED-SHA\\"
                                  \\"DH-RSA-AES128-SHA\\"
                                  \\"DH-RSA-AES256-SHA\\"
                                  \\"DH-RSA-CAMELLIA128-SHA\\"
                                  \\"DH-RSA-CAMELLIA256-SHA\\"
                                  \\"DH-RSA-DES-CBC3-SHA\\"
                                  \\"DH-RSA-SEED-SHA\\"
                                  \\"DHE-DSS-AES128-SHA\\"
                                  \\"DHE-DSS-AES256-SHA\\"
                                  \\"DHE-DSS-CAMELLIA128-SHA\\"
                                  \\"DHE-DSS-CAMELLIA256-SHA\\"
                                  \\"DHE-DSS-DES-CBC3-SHA\\"
                                  \\"DHE-DSS-SEED-SHA\\"
                                  \\"DHE-RSA-AES128-SHA\\"
                                  \\"DHE-RSA-AES256-SHA\\"
                                  \\"DHE-RSA-CAMELLIA128-SHA\\"
                                  \\"DHE-RSA-CAMELLIA256-SHA\\"
                                  \\"DHE-RSA-DES-CBC3-SHA\\"
                                  \\"DHE-RSA-SEED-SHA\\"
                                  \\"ECDH-ECDSA-AES128-SHA\\"
                                  \\"ECDH-ECDSA-AES256-SHA\\"
                                  \\"ECDH-ECDSA-DES-CBC3-SHA\\"
                                  \\"ECDH-ECDSA-RC4-SHA\\"
                                  \\"ECDH-RSA-AES128-SHA\\"
                                  \\"ECDH-RSA-AES256-SHA\\"
                                  \\"ECDH-RSA-DES-CBC3-SHA\\"
                                  \\"ECDH-RSA-RC4-SHA\\"
                                  \\"ECDHE-ECDSA-AES128-SHA\\"
                                  \\"ECDHE-ECDSA-AES256-SHA\\"
                                  \\"ECDHE-ECDSA-DES-CBC3-SHA\\"
                                  \\"ECDHE-ECDSA-RC4-SHA\\"
                                  \\"ECDHE-RSA-AES128-SHA\\"
                                  \\"ECDHE-RSA-AES256-SHA\\"
                                  \\"ECDHE-RSA-DES-CBC3-SHA\\"
                                  \\"ECDHE-RSA-RC4-SHA\\"
                                  \\"IDEA-CBC-SHA\\"
                                  \\"KRB5-DES-CBC3-MD5\\"
                                  \\"KRB5-DES-CBC3-SHA\\"
                                  \\"KRB5-IDEA-CBC-MD5\\"
                                  \\"KRB5-IDEA-CBC-SHA\\"
                                  \\"KRB5-RC4-MD5\\"
                                  \\"KRB5-RC4-SHA\\"
                                  \\"PSK-3DES-EDE-CBC-SHA\\"
                                  \\"PSK-AES128-CBC-SHA\\"
                                  \\"PSK-AES256-CBC-SHA\\"
                                  \\"PSK-RC4-SHA\\"
                                  \\"RC4-MD5\\"
                                  \\"RC4-SHA\\"
                                  \\"SEED-SHA\\""
                        - "example: `[\\"ECDHE-RSA-AES256-GCM-SHA384\\",\\"ECDHE-ECDSA-AES256-GCM-SHA384\\",\\"ECDHE-RSA-AES128-GCM-SHA256\\"]`"
                    returned: on success
                    type: list
                    sample: []
        certificates:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                certificate_name:
                    description:
                        - A friendly name for the certificate bundle. It must be unique and it cannot be changed.
                          Valid certificate bundle names include only alphanumeric characters, dashes, and underscores.
                          Certificate bundle names cannot contain spaces. Avoid entering confidential information.
                        - "Example: `example_certificate_bundle`"
                    returned: on success
                    type: str
                    sample: certificate_name_example
                public_certificate:
                    description:
                        - The public certificate, in PEM format, that you received from your SSL certificate provider.
                        - "Example:"
                        - "   -----BEGIN CERTIFICATE-----
                              MIIC2jCCAkMCAg38MA0GCSqGSIb3DQEBBQUAMIGbMQswCQYDVQQGEwJKUDEOMAwG
                              A1UECBMFVG9reW8xEDAOBgNVBAcTB0NodW8ta3UxETAPBgNVBAoTCEZyYW5rNERE
                              MRgwFgYDVQQLEw9XZWJDZXJ0IFN1cHBvcnQxGDAWBgNVBAMTD0ZyYW5rNEREIFdl
                              YiBDQTEjMCEGCSqGSIb3DQEJARYUc3VwcG9ydEBmcmFuazRkZC5jb20wHhcNMTIw
                              ...
                              -----END CERTIFICATE-----"
                    returned: on success
                    type: str
                    sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
                ca_certificate:
                    description:
                        - The Certificate Authority certificate, or any interim certificate, that you received from your SSL certificate provider.
                        - "Example:"
                        - "   -----BEGIN CERTIFICATE-----
                              MIIEczCCA1ugAwIBAgIBADANBgkqhkiG9w0BAQQFAD..AkGA1UEBhMCR0Ix
                              EzARBgNVBAgTClNvbWUtU3RhdGUxFDASBgNVBAoTC0..0EgTHRkMTcwNQYD
                              VQQLEy5DbGFzcyAxIFB1YmxpYyBQcmltYXJ5IENlcn..XRpb24gQXV0aG9y
                              aXR5MRQwEgYDVQQDEwtCZXN0IENBIEx0ZDAeFw0wMD..TUwMTZaFw0wMTAy
                              ...
                              -----END CERTIFICATE-----"
                    returned: on success
                    type: str
                    sample: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        backend_sets:
            description:
                - ""
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
        path_route_sets:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The unique name for this set of path route rules. Avoid entering confidential information.
                        - "Example: `example_path_route_set`"
                    returned: on success
                    type: str
                    sample: name_example
                path_routes:
                    description:
                        - The set of path route rules.
                    returned: on success
                    type: complex
                    contains:
                        path:
                            description:
                                - The path string to match against the incoming URI path.
                                - "*  Path strings are case-insensitive."
                                - "*  Asterisk (*) wildcards are not supported."
                                - "*  Regular expressions are not supported."
                                - "Example: `/example/video/123`"
                            returned: on success
                            type: str
                            sample: path_example
                        path_match_type:
                            description:
                                - The type of matching to apply to incoming URIs.
                            returned: on success
                            type: complex
                            contains:
                                match_type:
                                    description:
                                        - Specifies how the load balancing service compares a L(PathRoute,https://docs.cloud.oracle.com/en-
                                          us/iaas/api/#/en/loadbalancer/20170115/requests/PathRoute)
                                          object's `path` string against the incoming URI.
                                        - "*  **EXACT_MATCH** - Looks for a `path` string that exactly matches the incoming URI path."
                                        - "*  **FORCE_LONGEST_PREFIX_MATCH** - Looks for the `path` string with the best, longest match of the beginning
                                             portion of the incoming URI path."
                                        - "*  **PREFIX_MATCH** - Looks for a `path` string that matches the beginning portion of the incoming URI path."
                                        - "*  **SUFFIX_MATCH** - Looks for a `path` string that matches the ending portion of the incoming URI path."
                                        - For a full description of how the system handles `matchType` in a path route set containing multiple rules, see
                                          L(Managing Request Routing,https://docs.cloud.oracle.com/Content/Balance/Tasks/managingrequest.htm).
                                    returned: on success
                                    type: str
                                    sample: EXACT_MATCH
                        backend_set_name:
                            description:
                                - The name of the target backend set for requests where the incoming URI matches the specified path.
                                - "Example: `example_backend_set`"
                            returned: on success
                            type: str
                            sample: backend_set_name_example
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
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        rule_sets:
            description:
                - ""
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
                        value:
                            description:
                                - "A header value that conforms to RFC 7230. With the following exceptions:
                                  *  value cannot contain `$`
                                  *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are
                                  invalid."
                                - "Example: `example_value`"
                            returned: on success
                            type: str
                            sample: value_example
                        conditions:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
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
                                  *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are
                                  invalid."
                                - "Example: `example_prefix_value`"
                            returned: on success
                            type: str
                            sample: prefix_example
                        suffix:
                            description:
                                - "A string to append to the header value. The resulting header value must conform to RFC 7230.
                                  With the following exceptions:
                                  *  value cannot contain `$`
                                  *  value cannot contain patterns like `{variable_name}`. They are reserved for future extensions. Currently, such values are
                                  invalid."
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
        routing_policies:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The unique name for this list of routing rules. Avoid entering confidential information.
                        - "Example: `example_routing_policy`"
                    returned: on success
                    type: str
                    sample: name_example
                condition_language_version:
                    description:
                        - The version of the language in which `condition` of `rules` are composed.
                    returned: on success
                    type: str
                    sample: V1
                rules:
                    description:
                        - The ordered list of routing rules.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - A unique name for the routing policy rule. Avoid entering confidential information.
                            returned: on success
                            type: str
                            sample: name_example
                        condition:
                            description:
                                - A routing rule to evaluate defined conditions against the incoming HTTP request and perform an action.
                            returned: on success
                            type: str
                            sample: condition_example
                        actions:
                            description:
                                - A list of actions to be applied when conditions of the routing rule are met.
                            returned: on success
                            type: complex
                            contains:
                                name:
                                    description:
                                        - ""
                                    returned: on success
                                    type: str
                                    sample: FORWARD_TO_BACKENDSET
                                backend_set_name:
                                    description:
                                        - Name of the backend set the listener will forward the traffic to.
                                        - "Example: `backendSetForImages`"
                                    returned: on success
                                    type: str
                                    sample: backend_set_name_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "ip_addresses": [{
            "ip_address": "ip_address_example",
            "is_public": true,
            "reserved_ip": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            }
        }],
        "shape_name": "shape_name_example",
        "shape_details": {
            "minimum_bandwidth_in_mbps": 56,
            "maximum_bandwidth_in_mbps": 56
        },
        "is_private": true,
        "subnet_ids": [],
        "network_security_group_ids": [],
        "listeners": {
            "name": "name_example",
            "default_backend_set_name": "default_backend_set_name_example",
            "port": 56,
            "protocol": "protocol_example",
            "hostname_names": [],
            "path_route_set_name": "path_route_set_name_example",
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
            "connection_configuration": {
                "idle_timeout": 56,
                "backend_tcp_proxy_protocol_version": 56
            },
            "rule_set_names": [],
            "routing_policy_name": "routing_policy_name_example"
        },
        "hostnames": {
            "name": "name_example",
            "hostname": "hostname_example"
        },
        "ssl_cipher_suites": {
            "name": "name_example",
            "ciphers": []
        },
        "certificates": {
            "certificate_name": "certificate_name_example",
            "public_certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----",
            "ca_certificate": "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
        },
        "backend_sets": {
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
        },
        "path_route_sets": {
            "name": "name_example",
            "path_routes": [{
                "path": "path_example",
                "path_match_type": {
                    "match_type": "EXACT_MATCH"
                },
                "backend_set_name": "backend_set_name_example"
            }]
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "rule_sets": {
            "name": "name_example",
            "items": [{
                "action": "ADD_HTTP_REQUEST_HEADER",
                "header": "header_example",
                "value": "value_example",
                "conditions": [{
                    "attribute_name": "SOURCE_IP_ADDRESS",
                    "attribute_value": "attribute_value_example",
                    "operator": "EXACT_MATCH"
                }],
                "description": "description_example",
                "allowed_methods": [],
                "status_code": 56,
                "prefix": "prefix_example",
                "suffix": "suffix_example",
                "are_invalid_characters_allowed": true,
                "http_large_header_size_in_kb": 56,
                "response_code": 56,
                "redirect_uri": {
                    "protocol": "protocol_example",
                    "host": "host_example",
                    "port": 56,
                    "path": "path_example",
                    "query": "query_example"
                }
            }]
        },
        "routing_policies": {
            "name": "name_example",
            "condition_language_version": "V1",
            "rules": [{
                "name": "name_example",
                "condition": "condition_example",
                "actions": [{
                    "name": "FORWARD_TO_BACKENDSET",
                    "backend_set_name": "backend_set_name_example"
                }]
            }]
        }
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
    from oci.load_balancer import LoadBalancerClient
    from oci.load_balancer.models import UpdateNetworkSecurityGroupsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NetworkSecurityGroupsHelperGen(OCIResourceHelperBase):
    """Supported operations: update"""

    def get_module_resource_id_param(self):
        return "load_balancer_id"

    def get_module_resource_id(self):
        return self.module.params.get("load_balancer_id")

    def get_response_field_name(self):
        return "load_balancer"

    def get_update_model_class(self):
        return UpdateNetworkSecurityGroupsDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_network_security_groups,
            call_fn_args=(),
            call_fn_kwargs=dict(
                update_network_security_groups_details=update_details,
                load_balancer_id=self.module.params.get("load_balancer_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NetworkSecurityGroupsHelperCustom = get_custom_class(
    "NetworkSecurityGroupsHelperCustom"
)


class ResourceHelper(NetworkSecurityGroupsHelperCustom, NetworkSecurityGroupsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            network_security_group_ids=dict(type="list", elements="str"),
            load_balancer_id=dict(aliases=["id"], type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="network_security_groups",
        service_client_class=LoadBalancerClient,
        namespace="load_balancer",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
