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
module: oci_network_ip_sec_connection_tunnel_facts
short_description: Fetches details about one or multiple IpSecConnectionTunnel resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple IpSecConnectionTunnel resources in Oracle Cloud Infrastructure
    - Lists the tunnel information for the specified IPSec connection.
    - If I(tunnel_id) is specified, the details of a single IpSecConnectionTunnel will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ipsc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the IPSec connection.
        type: str
        required: true
    tunnel_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.
            - Required to get a specific ip_sec_connection_tunnel.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific ip_sec_connection_tunnel
  oci_network_ip_sec_connection_tunnel_facts:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"
    tunnel_id: "ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx"

- name: List ip_sec_connection_tunnels
  oci_network_ip_sec_connection_tunnel_facts:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ip_sec_connection_tunnels:
    description:
        - List of IpSecConnectionTunnel resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the tunnel.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        vpn_ip:
            description:
                - The IP address of Oracle's VPN headend.
                - "Example: `203.0.113.21`"
            returned: on success
            type: str
            sample: vpn_ip_example
        cpe_ip:
            description:
                - The IP address of the CPE's VPN headend.
                - "Example: `203.0.113.22`"
            returned: on success
            type: str
            sample: cpe_ip_example
        status:
            description:
                - The status of the tunnel based on IPSec protocol characteristics.
            returned: on success
            type: str
            sample: UP
        ike_version:
            description:
                - Internet Key Exchange protocol version.
            returned: on success
            type: str
            sample: V1
        lifecycle_state:
            description:
                - The tunnel's lifecycle state.
            returned: on success
            type: str
            sample: PROVISIONING
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        bgp_session_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                oracle_interface_ip:
                    description:
                        - The IP address for the Oracle end of the inside tunnel interface.
                        - If the tunnel's `routing` attribute is set to `BGP`
                          (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                          is required and used for the tunnel's BGP session.
                        - If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                          address so you can troubleshoot or monitor the tunnel.
                        - The value must be a /30 or /31.
                        - "Example: `10.0.0.4/31`"
                    returned: on success
                    type: str
                    sample: oracle_interface_ip_example
                customer_interface_ip:
                    description:
                        - The IP address for the CPE end of the inside tunnel interface.
                        - If the tunnel's `routing` attribute is set to `BGP`
                          (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                          is required and used for the tunnel's BGP session.
                        - If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                          address so you can troubleshoot or monitor the tunnel.
                        - The value must be a /30 or /31.
                        - "Example: `10.0.0.5/31`"
                    returned: on success
                    type: str
                    sample: customer_interface_ip_example
                oracle_interface_ipv6:
                    description:
                        - The IPv6 address for the Oracle end of the inside tunnel interface. This IP address is optional.
                        - If the tunnel's `routing` attribute is set to `BGP`
                          (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                          is used for the tunnel's BGP session.
                        - If `routing` is instead set to `STATIC`, you can set this IP
                          address to troubleshoot or monitor the tunnel.
                        - Only subnet masks from /64 up to /127 are allowed.
                        - "Example: `2001:db8::1/64`"
                    returned: on success
                    type: str
                    sample: oracle_interface_ipv6_example
                customer_interface_ipv6:
                    description:
                        - The IPv6 address for the CPE end of the inside tunnel interface. This IP address is optional.
                        - If the tunnel's `routing` attribute is set to `BGP`
                          (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this IP address
                          is used for the tunnel's BGP session.
                        - If `routing` is instead set to `STATIC`, you can set this IP
                          address to troubleshoot or monitor the tunnel.
                        - Only subnet masks from /64 up to /127 are allowed.
                        - "Example: `2001:db8::1/64`"
                    returned: on success
                    type: str
                    sample: customer_interface_ipv6_example
                oracle_bgp_asn:
                    description:
                        - The Oracle BGP ASN.
                    returned: on success
                    type: str
                    sample: oracle_bgp_asn_example
                customer_bgp_asn:
                    description:
                        - "If the tunnel's `routing` attribute is set to `BGP`
                          (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/)), this ASN
                          is required and used for the tunnel's BGP session. This is the ASN of the network on the
                          CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \\"asplain\\" format."
                        - If the tunnel uses static routing, the `customerBgpAsn` must be null.
                        - "Example: `12345` (2-byte) or `1587232876` (4-byte)"
                    returned: on success
                    type: str
                    sample: customer_bgp_asn_example
                bgp_state:
                    description:
                        - The state of the BGP session.
                    returned: on success
                    type: str
                    sample: UP
                bgp_ipv6_state:
                    description:
                        - The state of the BGP IPv6 session.
                    returned: on success
                    type: str
                    sample: UP
        encryption_domain_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                oracle_traffic_selector:
                    description:
                        - Lists IPv4 or IPv6-enabled subnets in your Oracle tenancy.
                    returned: on success
                    type: list
                    sample: []
                cpe_traffic_selector:
                    description:
                        - Lists IPv4 or IPv6-enabled subnets in your on-premises network.
                    returned: on success
                    type: list
                    sample: []
        routing:
            description:
                - The type of routing used for this tunnel (either BGP dynamic routing or static routing).
            returned: on success
            type: str
            sample: BGP
        time_created:
            description:
                - The date and time the IPSec connection tunnel was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_status_updated:
            description:
                - When the status of the tunnel last changed, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        oracle_can_initiate:
            description:
                - Indicates whether Oracle can either initiate the tunnel or respond, or respond only.
            returned: on success
            type: str
            sample: INITIATOR_OR_RESPONDER
        nat_translation_enabled:
            description:
                - Whether NAT-T Enabled on the tunnel
            returned: on success
            type: str
            sample: ENABLED
        dpd_mode:
            description:
                - dpd mode
            returned: on success
            type: str
            sample: INITIATE_AND_RESPOND
        dpd_timeout_in_sec:
            description:
                - Dead peer detection (DPD) timeout in seconds.
            returned: on success
            type: int
            sample: 56
        phase_one_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_custom_phase_one_config:
                    description:
                        - Indicates whether custom phase one configuration is enabled.
                    returned: on success
                    type: bool
                    sample: true
                lifetime:
                    description:
                        - The total configured lifetime of an IKE security association.
                    returned: on success
                    type: int
                    sample: 56
                remaining_lifetime:
                    description:
                        - The lifetime remaining before the key is refreshed.
                    returned: on success
                    type: int
                    sample: 56
                custom_authentication_algorithm:
                    description:
                        - Custom authentication algorithm
                    returned: on success
                    type: str
                    sample: custom_authentication_algorithm_example
                negotiated_authentication_algorithm:
                    description:
                        - The negotiated authentication algorithm.
                    returned: on success
                    type: str
                    sample: negotiated_authentication_algorithm_example
                custom_encryption_algorithm:
                    description:
                        - Custom encryption algorithm.
                    returned: on success
                    type: str
                    sample: custom_encryption_algorithm_example
                negotiated_encryption_algorithm:
                    description:
                        - The negotiated encryption algorithm.
                    returned: on success
                    type: str
                    sample: negotiated_encryption_algorithm_example
                custom_dh_group:
                    description:
                        - Custom Diffie-Hellman group.
                    returned: on success
                    type: str
                    sample: custom_dh_group_example
                negotiated_dh_group:
                    description:
                        - The negotiated Diffie-Hellman group.
                    returned: on success
                    type: str
                    sample: negotiated_dh_group_example
                is_ike_established:
                    description:
                        - Indicates whether IKE Phase 1 is established.
                    returned: on success
                    type: bool
                    sample: true
                remaining_lifetime_last_retrieved:
                    description:
                        - The date and time we retrieved the remaining lifetime, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        phase_two_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_custom_phase_two_config:
                    description:
                        - Indicates whether custom phase two configuration is enabled.
                    returned: on success
                    type: bool
                    sample: true
                lifetime:
                    description:
                        - The total configured lifetime of an IKE security association.
                    returned: on success
                    type: int
                    sample: 56
                remaining_lifetime:
                    description:
                        - The lifetime remaining before the key is refreshed.
                    returned: on success
                    type: int
                    sample: 56
                custom_authentication_algorithm:
                    description:
                        - Phase Two authentication algorithm supported during tunnel negotiation.
                    returned: on success
                    type: str
                    sample: custom_authentication_algorithm_example
                negotiated_authentication_algorithm:
                    description:
                        - The negotiated authentication algorithm.
                    returned: on success
                    type: str
                    sample: negotiated_authentication_algorithm_example
                custom_encryption_algorithm:
                    description:
                        - Custom Encryption Algorithm
                    returned: on success
                    type: str
                    sample: custom_encryption_algorithm_example
                negotiated_encryption_algorithm:
                    description:
                        - The negotiated encryption algorithm.
                    returned: on success
                    type: str
                    sample: negotiated_encryption_algorithm_example
                dh_group:
                    description:
                        - Proposed Diffie-Hellman group.
                    returned: on success
                    type: str
                    sample: dh_group_example
                negotiated_dh_group:
                    description:
                        - The negotiated Diffie-Hellman group.
                    returned: on success
                    type: str
                    sample: negotiated_dh_group_example
                is_esp_established:
                    description:
                        - ESP Phase 2 established
                    returned: on success
                    type: bool
                    sample: true
                is_pfs_enabled:
                    description:
                        - Is PFS (perfect forward secrecy) enabled
                    returned: on success
                    type: bool
                    sample: true
                remaining_lifetime_last_retrieved:
                    description:
                        - The date and time we retrieved the remaining lifetime, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "vpn_ip": "vpn_ip_example",
        "cpe_ip": "cpe_ip_example",
        "status": "UP",
        "ike_version": "V1",
        "lifecycle_state": "PROVISIONING",
        "display_name": "display_name_example",
        "bgp_session_info": {
            "oracle_interface_ip": "oracle_interface_ip_example",
            "customer_interface_ip": "customer_interface_ip_example",
            "oracle_interface_ipv6": "oracle_interface_ipv6_example",
            "customer_interface_ipv6": "customer_interface_ipv6_example",
            "oracle_bgp_asn": "oracle_bgp_asn_example",
            "customer_bgp_asn": "customer_bgp_asn_example",
            "bgp_state": "UP",
            "bgp_ipv6_state": "UP"
        },
        "encryption_domain_config": {
            "oracle_traffic_selector": [],
            "cpe_traffic_selector": []
        },
        "routing": "BGP",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_status_updated": "2013-10-20T19:20:30+01:00",
        "oracle_can_initiate": "INITIATOR_OR_RESPONDER",
        "nat_translation_enabled": "ENABLED",
        "dpd_mode": "INITIATE_AND_RESPOND",
        "dpd_timeout_in_sec": 56,
        "phase_one_details": {
            "is_custom_phase_one_config": true,
            "lifetime": 56,
            "remaining_lifetime": 56,
            "custom_authentication_algorithm": "custom_authentication_algorithm_example",
            "negotiated_authentication_algorithm": "negotiated_authentication_algorithm_example",
            "custom_encryption_algorithm": "custom_encryption_algorithm_example",
            "negotiated_encryption_algorithm": "negotiated_encryption_algorithm_example",
            "custom_dh_group": "custom_dh_group_example",
            "negotiated_dh_group": "negotiated_dh_group_example",
            "is_ike_established": true,
            "remaining_lifetime_last_retrieved": "2013-10-20T19:20:30+01:00"
        },
        "phase_two_details": {
            "is_custom_phase_two_config": true,
            "lifetime": 56,
            "remaining_lifetime": 56,
            "custom_authentication_algorithm": "custom_authentication_algorithm_example",
            "negotiated_authentication_algorithm": "negotiated_authentication_algorithm_example",
            "custom_encryption_algorithm": "custom_encryption_algorithm_example",
            "negotiated_encryption_algorithm": "negotiated_encryption_algorithm_example",
            "dh_group": "dh_group_example",
            "negotiated_dh_group": "negotiated_dh_group_example",
            "is_esp_established": true,
            "is_pfs_enabled": true,
            "remaining_lifetime_last_retrieved": "2013-10-20T19:20:30+01:00"
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
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionTunnelFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "ipsc_id",
            "tunnel_id",
        ]

    def get_required_params_for_list(self):
        return [
            "ipsc_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection_tunnel,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ip_sec_connection_tunnels,
            ipsc_id=self.module.params.get("ipsc_id"),
            **optional_kwargs
        )


IpSecConnectionTunnelFactsHelperCustom = get_custom_class(
    "IpSecConnectionTunnelFactsHelperCustom"
)


class ResourceFactsHelper(
    IpSecConnectionTunnelFactsHelperCustom, IpSecConnectionTunnelFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ipsc_id=dict(type="str", required=True),
            tunnel_id=dict(aliases=["id"], type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ip_sec_connection_tunnel",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(ip_sec_connection_tunnels=result)


if __name__ == "__main__":
    main()
