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
module: oci_network_ip_sec_connection_device_status_facts
short_description: Fetches details about a IpSecConnectionDeviceStatus resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a IpSecConnectionDeviceStatus resource in Oracle Cloud Infrastructure
    - Deprecated. To get the tunnel status, instead use
      L(GetIPSecConnectionTunnel,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/IPSecConnectionTunnel/GetIPSecConnectionTunnel).
version_added: "2.9"
author: Oracle (@oracle)
options:
    ipsc_id:
        description:
            - The OCID of the IPSec connection.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific ip_sec_connection_device_status
  oci_network_ip_sec_connection_device_status_facts:
    ipsc_id: ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
ip_sec_connection_device_status:
    description:
        - IpSecConnectionDeviceStatus resource
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the IPSec connection.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The IPSec connection's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the IPSec connection was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        tunnels:
            description:
                - Two L(TunnelStatus,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/TunnelStatus/) objects.
            returned: on success
            type: complex
            contains:
                ip_address:
                    description:
                        - The IP address of Oracle's VPN headend.
                        - "Example: `203.0.113.50`"
                    returned: on success
                    type: string
                    sample: 203.0.113.50
                lifecycle_state:
                    description:
                        - The tunnel's current state.
                    returned: on success
                    type: string
                    sample: UP
                time_created:
                    description:
                        - The date and time the IPSec connection was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                time_state_modified:
                    description:
                        - When the state of the tunnel last changed, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                        - "Example: `2016-08-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "tunnels": [{
            "ip_address": "203.0.113.50",
            "lifecycle_state": "UP",
            "time_created": "2016-08-25T21:10:29.600Z",
            "time_state_modified": "2016-08-25T21:10:29.600Z"
        }]
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


class IpSecConnectionDeviceStatusFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "ipsc_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_ip_sec_connection_device_status,
            ipsc_id=self.module.params.get("ipsc_id"),
        )


IpSecConnectionDeviceStatusFactsHelperCustom = get_custom_class(
    "IpSecConnectionDeviceStatusFactsHelperCustom"
)


class ResourceFactsHelper(
    IpSecConnectionDeviceStatusFactsHelperCustom,
    IpSecConnectionDeviceStatusFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(ipsc_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="ip_sec_connection_device_status",
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

    module.exit_json(ip_sec_connection_device_status=result)


if __name__ == "__main__":
    main()
