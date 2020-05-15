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
module: oci_network_ip_sec_connection_tunnel_shared_secret_facts
short_description: Fetches details about a IpSecConnectionTunnelSharedSecret resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a IpSecConnectionTunnelSharedSecret resource in Oracle Cloud Infrastructure
    - Gets the specified tunnel's shared secret (pre-shared key). To get other information
      about the tunnel, use L(GetIPSecConnectionTunnel,https://docs.cloud.oracle.com/#/en/iaas/20160918/IPSecConnectionTunnel/GetIPSecConnectionTunnel).
version_added: "2.5"
options:
    ipsc_id:
        description:
            - The OCID of the IPSec connection.
        type: str
        required: true
    tunnel_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the tunnel.
        type: str
        aliases: ["id"]
        required: true
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ip_sec_connection_tunnel_shared_secret
  oci_network_ip_sec_connection_tunnel_shared_secret_facts:
    ipsc_id: ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx
    tunnel_id: ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
ip_sec_connection_tunnel_shared_secret:
    description:
        - IpSecConnectionTunnelSharedSecret resource
    returned: on success
    type: complex
    contains:
        shared_secret:
            description:
                - The tunnel's shared secret (pre-shared key).
                - "Example: `EXAMPLEToUis6j1cp8GdVQxcmdfMO0yXMLilZTbYCMDGu4V8o`"
            returned: on success
            type: string
            sample: EXAMPLEToUis6j1cp8GdVQxcmdfMO0yXMLilZTbYCMDGu4V8o
    sample: {
        "shared_secret": "EXAMPLEToUis6j1cp8GdVQxcmdfMO0yXMLilZTbYCMDGu4V8o"
    }
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


class IpSecConnectionTunnelSharedSecretFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "ipsc_id",
            "tunnel_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection_tunnel_shared_secret,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
        )


IpSecConnectionTunnelSharedSecretFactsHelperCustom = get_custom_class(
    "IpSecConnectionTunnelSharedSecretFactsHelperCustom"
)


class ResourceFactsHelper(
    IpSecConnectionTunnelSharedSecretFactsHelperCustom,
    IpSecConnectionTunnelSharedSecretFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ipsc_id=dict(type="str", required=True),
            tunnel_id=dict(aliases=["id"], type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ip_sec_connection_tunnel_shared_secret",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(ip_sec_connection_tunnel_shared_secret=result)


if __name__ == "__main__":
    main()
