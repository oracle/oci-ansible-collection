#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_network_ip_sec_connection_device_config_facts
short_description: Fetches details about a IpSecConnectionDeviceConfig resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a IpSecConnectionDeviceConfig resource in Oracle Cloud Infrastructure
    - "Deprecated. To get tunnel information, instead use:"
    - "* L(GetIPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnel/GetIPSecConnectionTunnel)
      * L(GetIPSecConnectionTunnelSharedSecret,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/iaas/latest/IPSecConnectionTunnelSharedSecret/GetIPSecConnectionTunnelSharedSecret)"
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ipsc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the IPSec connection.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ip_sec_connection_device_config
  oci_network_ip_sec_connection_device_config_facts:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
ip_sec_connection_device_config:
    description:
        - IpSecConnectionDeviceConfig resource
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the IPSec connection.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The IPSec connection's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the IPSec connection was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        tunnels:
            description:
                - Two L(TunnelConfig,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/TunnelConfig/) objects.
            returned: on success
            type: complex
            contains:
                ip_address:
                    description:
                        - The IP address of Oracle's VPN headend.
                        - "Example: `203.0.113.50 `"
                    returned: on success
                    type: str
                    sample: ip_address_example
                shared_secret:
                    description:
                        - The shared secret of the IPSec tunnel.
                    returned: on success
                    type: str
                    sample: shared_secret_example
                time_created:
                    description:
                        - The date and time the IPSec connection was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "tunnels": [{
            "ip_address": "ip_address_example",
            "shared_secret": "shared_secret_example",
            "time_created": "2013-10-20T19:20:30+01:00"
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IpSecConnectionDeviceConfigFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "ipsc_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection_device_config,
            ipsc_id=self.module.params.get("ipsc_id"),
        )


IpSecConnectionDeviceConfigFactsHelperCustom = get_custom_class(
    "IpSecConnectionDeviceConfigFactsHelperCustom"
)


class ResourceFactsHelper(
    IpSecConnectionDeviceConfigFactsHelperCustom,
    IpSecConnectionDeviceConfigFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(ipsc_id=dict(aliases=["id"], type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ip_sec_connection_device_config",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(ip_sec_connection_device_config=result)


if __name__ == "__main__":
    main()
