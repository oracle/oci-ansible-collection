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
module: oci_network_ip_sec_connection_tunnel_cpe_device_config_content_facts
short_description: Fetches details about a IpSecConnectionTunnelCpeDeviceConfigContent resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a IpSecConnectionTunnelCpeDeviceConfigContent resource in Oracle Cloud Infrastructure
    - Renders a set of CPE configuration content for the specified IPSec tunnel. The content helps a
      network engineer configure the actual CPE device (for example, a hardware router) that the specified
      IPSec tunnel terminates on.
    - The rendered content is specific to the type of CPE device (for example, Cisco ASA). Therefore the
      L(Cpe,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Cpe/) used by the specified L(IPSecConnection,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/iaas/20160918/IPSecConnection/)
      must have the CPE's device type specified by the `cpeDeviceShapeId` attribute. The content
      optionally includes answers that the customer provides (see
      L(UpdateTunnelCpeDeviceConfig,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/TunnelCpeDeviceConfig/UpdateTunnelCpeDeviceConfig)),
      merged with a template of other information specific to the CPE device type.
    - "The operation returns configuration information for only the specified IPSec tunnel.
      Here are other similar operations:"
    - " * L(GetIpsecCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnection/GetIpsecCpeDeviceConfigContent)
        returns CPE configuration content for all tunnels in a single IPSec connection.
        * L(GetCpeDeviceConfigContent,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Cpe/GetCpeDeviceConfigContent)
        returns CPE configuration content for *all* IPSec connections that use a specific CPE."
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
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ip_sec_connection_tunnel_cpe_device_config_content
  oci_network_ip_sec_connection_tunnel_cpe_device_config_content_facts:
    ipsc_id: ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx
    tunnel_id: ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
ip_sec_connection_tunnel_cpe_device_config_content:
    description:
        - IpSecConnectionTunnelCpeDeviceConfigContent resource
    returned: on success
    type: str
    sample: "sample"
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils._text import to_text
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


class IpSecConnectionTunnelCpeDeviceConfigContentFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "ipsc_id",
            "tunnel_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_tunnel_cpe_device_config_content,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
        )

    def get(self):
        response_data = self.get_resource().data
        return to_text(response_data)


IpSecConnectionTunnelCpeDeviceConfigContentFactsHelperCustom = get_custom_class(
    "IpSecConnectionTunnelCpeDeviceConfigContentFactsHelperCustom"
)


class ResourceFactsHelper(
    IpSecConnectionTunnelCpeDeviceConfigContentFactsHelperCustom,
    IpSecConnectionTunnelCpeDeviceConfigContentFactsHelperGen,
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
        resource_type="ip_sec_connection_tunnel_cpe_device_config_content",
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

    module.exit_json(ip_sec_connection_tunnel_cpe_device_config_content=result)


if __name__ == "__main__":
    main()
