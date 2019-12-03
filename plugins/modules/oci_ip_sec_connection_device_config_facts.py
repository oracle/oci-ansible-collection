#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_ip_sec_connection_device_config_facts
short_description: Retrieve configuration information for the specified IPSec connection
description:
    - This module retrieves configuration information for the specified IPSec connection. For each tunnel, the response
      includes the IP address of Oracle's VPN headend and the shared secret.
version_added: "2.5"
options:
    ipsc_id:
        description: The OCID of the IPSec connection.
        required: true
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get configuration information of IPSec connection
  oci_ip_sec_connection_device_config_facts:
    ipsc_id: ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
ip_sec_connection_device_config:
    description: Configuration information of IPSec connection
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the IPSec connection.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        id:
            description: The IPSec connection's Oracle ID (OCID).
            returned: always
            type: string
            sample: ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx
        time_created:
            description: The date and time the IPSec connection was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2018-09-13T20:22:40.626000+00:00
        tunnels:
            description: Two TunnelConfig objects.
            returned: always
            type: list
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx",
            "time_created": "2018-09-13T20:22:40.626000+00:00",
            "tunnels": [{"ip_address": "129.213.7.49",
                         "shared_secret": "xxxxxEXAMPLExxxxx",
                         "time_created": "2018-09-13T20:22:40.626000+00:00"
                         },
                         {"ip_address": "129.213.6.53",
                          "shared_secret": "xxxxxEXAMPLExxxxx",
                          "time_created": "2018-09-13T20:22:40.626000+00:00"
                         }
                       ]
            }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(ipsc_id=dict(type="str", required=True, aliases=["id"])))

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    ip_sec_connection_id = module.params["ipsc_id"]
    try:
        result = to_dict(
            oci_utils.call_with_backoff(
                virtual_network_client.get_ip_sec_connection_device_config,
                ipsc_id=ip_sec_connection_id,
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(ip_sec_connection_device_config=result)


if __name__ == "__main__":
    main()
