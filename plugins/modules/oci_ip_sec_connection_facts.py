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
module: oci_ip_sec_connection_facts
short_description: Retrieve facts of IPSec connections
description:
    - This module retrieves information of the specified IPSec connection or lists all the IPSec connections in the
      specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to get all the IPSec connections in the
                     compartment.
        required: false
    ipsc_id:
        description: The OCID of the IPSec connection. I(ipsc_id) is required to get a specific IPSec connection's
                     information.
        required: false
        aliases: [ 'id' ]
    drg_id:
        description: The OCID of the DRG. Use I(drg_id) with I(compartment_id) to filter the results by DRG.
        required: false
    cpe_id:
        description: The OCID of the CPE. Use I(cpe_id) with I(compartment_id) to filter the results by CPE.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the IPSec connections in a compartment
  oci_ip_sec_connection_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get a specific IPSec connection using its OCID
  oci_ip_sec_connection_facts:
    ipsc_id: ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
ip_sec_connections:
    description: List of IPSec connection details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the IPSec connection.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        cpe_id:
            description: The OCID of the CPE.
            returned: always
            type: string
            sample: ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering
                         confidential information.
            returned: always
            type: string
            sample: ansible_ip_sec_connection
        drg_id:
            description: The OCID of the DRG.
            returned: always
            type: string
            sample: ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: The IPSec connection's Oracle ID (OCID).
            returned: always
            type: string
            sample: ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: Current state of the IPSec connection.
            returned: always
            type: string
            sample: AVAILABLE
        static_routes:
            description: Static routes to the CPE. At least one route must be included. The CIDR must not be a multicast
                         address or class E address.
            returned: always
            type: string
            sample: [10.0.1.0/24]
        time_created:
            description: The date and time the IPSec connection was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "cpe_id": "ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_ip_sec_connection",
            "drg_id": "ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx",
            "freeform_tags": {},
            "id": "ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "static_routes": ["10.0.1.0/24"],
            "time_created": "2017-11-13T20:22:40.626000+00:00"
            }]
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
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            ipsc_id=dict(type="str", required=False, aliases=["id"]),
            drg_id=dict(type="str", required=False),
            cpe_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "ipsc_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    ip_sec_connection_id = module.params["ipsc_id"]
    result = []

    try:
        if ip_sec_connection_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_ip_sec_connection,
                        ipsc_id=ip_sec_connection_id,
                    ).data
                )
            ]
        else:
            compartment_id = module.params["compartment_id"]
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_ip_sec_connections,
                    display_name=module.params["display_name"],
                    compartment_id=compartment_id,
                    drg_id=module.params["drg_id"],
                    cpe_id=module.params["cpe_id"],
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(ip_sec_connections=result)


if __name__ == "__main__":
    main()
