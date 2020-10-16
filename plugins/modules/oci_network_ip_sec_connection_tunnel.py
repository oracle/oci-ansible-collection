#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_network_ip_sec_connection_tunnel
short_description: Manage an IpSecConnectionTunnel resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an IpSecConnectionTunnel resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    ipsc_id:
        description:
            - The OCID of the IPSec connection.
        type: str
        required: true
    tunnel_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the tunnel.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
              entering confidential information.
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    routing:
        description:
            - The type of routing to use for this tunnel (either BGP dynamic routing or static routing).
            - This parameter is updatable.
        type: str
        choices:
            - "BGP"
            - "STATIC"
    ike_version:
        description:
            - Internet Key Exchange protocol version.
            - This parameter is updatable.
        type: str
        choices:
            - "V1"
            - "V2"
    bgp_session_config:
        description:
            - Information for establishing a BGP session for the IPSec tunnel.
            - This parameter is updatable.
        type: dict
        suboptions:
            oracle_interface_ip:
                description:
                    - The IP address for the Oracle end of the inside tunnel interface.
                    - If the tunnel's `routing` attribute is set to `BGP`
                      (see L(UpdateIPSecConnectionTunnelDetails,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/iaas/20160918/datatypes/UpdateIPSecConnectionTunnelDetails)), this IP address
                      is used for the tunnel's BGP session.
                    - If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or
                      monitor the tunnel.
                    - The value must be a /30 or /31.
                    - If you are switching the tunnel from using BGP dynamic routing to static routing and want
                      to remove the value for `oracleInterfaceIp`, you can set the value to an empty string.
                    - "Example: `10.0.0.4/31`"
                    - This parameter is updatable.
                type: str
            customer_interface_ip:
                description:
                    - The IP address for the CPE end of the inside tunnel interface.
                    - If the tunnel's `routing` attribute is set to `BGP`
                      (see L(UpdateIPSecConnectionTunnelDetails,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/iaas/20160918/datatypes/UpdateIPSecConnectionTunnelDetails)), this IP address
                      is used for the tunnel's BGP session.
                    - If `routing` is instead set to `STATIC`, you can set this IP address to troubleshoot or
                      monitor the tunnel.
                    - The value must be a /30 or /31.
                    - If you are switching the tunnel from using BGP dynamic routing to static routing and want
                      to remove the value for `customerInterfaceIp`, you can set the value to an empty string.
                    - "Example: `10.0.0.5/31`"
                    - This parameter is updatable.
                type: str
            customer_bgp_asn:
                description:
                    - "The BGP ASN of the network on the CPE end of the BGP session. Can be a 2-byte or 4-byte ASN.
                      Uses \\"asplain\\" format."
                    - If you are switching the tunnel from using BGP dynamic routing to static routing, the
                      `customerBgpAsn` must be null.
                    - "Example: `12345` (2-byte) or `1587232876` (4-byte)"
                    - This parameter is updatable.
                type: str
    state:
        description:
            - The state of the IpSecConnectionTunnel.
            - Use I(state=present) to update an existing an IpSecConnectionTunnel.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update ip_sec_connection_tunnel using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_ip_sec_connection_tunnel:
    ipsc_id: ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    routing: BGP
    ike_version: V1

- name: Update ip_sec_connection_tunnel
  oci_network_ip_sec_connection_tunnel:
    ipsc_id: ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx
    tunnel_id: ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
ip_sec_connection_tunnel:
    description:
        - Details of the IpSecConnectionTunnel resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment containing the tunnel.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the tunnel.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        vpn_ip:
            description:
                - The IP address of Oracle's VPN headend.
                - "Example: `203.0.113.21`"
            returned: on success
            type: string
            sample: 203.0.113.21
        cpe_ip:
            description:
                - The IP address of the CPE's VPN headend.
                - "Example: `203.0.113.22`"
            returned: on success
            type: string
            sample: 203.0.113.22
        status:
            description:
                - The status of the tunnel based on IPSec protocol characteristics.
            returned: on success
            type: string
            sample: UP
        ike_version:
            description:
                - Internet Key Exchange protocol version.
            returned: on success
            type: string
            sample: V1
        lifecycle_state:
            description:
                - The tunnel's lifecycle state.
            returned: on success
            type: string
            sample: PROVISIONING
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
                  entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        bgp_session_info:
            description:
                - Information for establishing the tunnel's BGP session.
            returned: on success
            type: complex
            contains:
                oracle_interface_ip:
                    description:
                        - The IP address for the Oracle end of the inside tunnel interface.
                        - If the tunnel's `routing` attribute is set to `BGP`
                          (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnel/)), this IP address
                          is required and used for the tunnel's BGP session.
                        - If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                          address so you can troubleshoot or monitor the tunnel.
                        - The value must be a /30 or /31.
                        - "Example: `10.0.0.4/31`"
                    returned: on success
                    type: string
                    sample: 10.0.0.4/31
                customer_interface_ip:
                    description:
                        - The IP address for the CPE end of the inside tunnel interface.
                        - If the tunnel's `routing` attribute is set to `BGP`
                          (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnel/)), this IP address
                          is required and used for the tunnel's BGP session.
                        - If `routing` is instead set to `STATIC`, this IP address is optional. You can set this IP
                          address so you can troubleshoot or monitor the tunnel.
                        - The value must be a /30 or /31.
                        - "Example: `10.0.0.5/31`"
                    returned: on success
                    type: string
                    sample: 10.0.0.5/31
                oracle_bgp_asn:
                    description:
                        - The Oracle BGP ASN.
                    returned: on success
                    type: string
                    sample: oracle_bgp_asn_example
                customer_bgp_asn:
                    description:
                        - "If the tunnel's `routing` attribute is set to `BGP`
                          (see L(IPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnel/)), this ASN
                          is required and used for the tunnel's BGP session. This is the ASN of the network on the
                          CPE end of the BGP session. Can be a 2-byte or 4-byte ASN. Uses \\"asplain\\" format."
                        - If the tunnel uses static routing, the `customerBgpAsn` must be null.
                        - "Example: `12345` (2-byte) or `1587232876` (4-byte)"
                    returned: on success
                    type: string
                    sample: 12345
                bgp_state:
                    description:
                        - The state of the BGP session.
                    returned: on success
                    type: string
                    sample: UP
        routing:
            description:
                - The type of routing used for this tunnel (either BGP dynamic routing or static routing).
            returned: on success
            type: string
            sample: BGP
        time_created:
            description:
                - The date and time the IPSec connection tunnel was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        time_status_updated:
            description:
                - When the status of the tunnel last changed, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "vpn_ip": "203.0.113.21",
        "cpe_ip": "203.0.113.22",
        "status": "UP",
        "ike_version": "V1",
        "lifecycle_state": "PROVISIONING",
        "display_name": "display_name_example",
        "bgp_session_info": {
            "oracle_interface_ip": "10.0.0.4/31",
            "customer_interface_ip": "10.0.0.5/31",
            "oracle_bgp_asn": "oracle_bgp_asn_example",
            "customer_bgp_asn": "12345",
            "bgp_state": "UP"
        },
        "routing": "BGP",
        "time_created": "2016-08-25T21:10:29.600Z",
        "time_status_updated": "2016-08-25T21:10:29.600Z"
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
    from oci.core import VirtualNetworkClient
    from oci.core.models import UpdateIPSecConnectionTunnelDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionTunnelHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_module_resource_id_param(self):
        return "tunnel_id"

    def get_module_resource_id(self):
        return self.module.params.get("tunnel_id")

    def get_get_fn(self):
        return self.client.get_ip_sec_connection_tunnel

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection_tunnel,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "ipsc_id",
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
            self.client.list_ip_sec_connection_tunnels, **kwargs
        )

    def get_update_model_class(self):
        return UpdateIPSecConnectionTunnelDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_ip_sec_connection_tunnel,
            call_fn_args=(),
            call_fn_kwargs=dict(
                ipsc_id=self.module.params.get("ipsc_id"),
                tunnel_id=self.module.params.get("tunnel_id"),
                update_ip_sec_connection_tunnel_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


IpSecConnectionTunnelHelperCustom = get_custom_class(
    "IpSecConnectionTunnelHelperCustom"
)


class ResourceHelper(IpSecConnectionTunnelHelperCustom, IpSecConnectionTunnelHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            ipsc_id=dict(type="str", required=True),
            tunnel_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            routing=dict(type="str", choices=["BGP", "STATIC"]),
            ike_version=dict(type="str", choices=["V1", "V2"]),
            bgp_session_config=dict(
                type="dict",
                options=dict(
                    oracle_interface_ip=dict(type="str"),
                    customer_interface_ip=dict(type="str"),
                    customer_bgp_asn=dict(type="str"),
                ),
            ),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="ip_sec_connection_tunnel",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
