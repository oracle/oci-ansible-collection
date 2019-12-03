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
module: oci_cpe_facts
short_description: Retrieve facts of Customer-Premises Equipments(CPEs)
description:
    - This module retrieves information of the specified customer-premises equipment(CPE) or lists all the CPEs in the
      specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to get all the CPEs in the compartment.
        required: false
    cpe_id:
        description: The OCID of the CPE. I(cpe_id) is required to get a specific CPE's information.
        required: false
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the CPEs in a compartment
  oci_cpe_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get a specific CPE using its OCID
  oci_cpe_facts:
    cpe_id: ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
cpes:
    description: List of CPE details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the CPE.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: Name of the CPE.
            returned: always
            type: string
            sample: ansible_cpe
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: OCID of the CPE.
            returned: always
            type: string
            sample: ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx
        ip_address:
            description: The public IP address of the on-premises router.
            returned: always
            type: string
            sample: "143.19.23.16"
        time_created:
            description: The date and time the CPE was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible_cpe",
            "id": "ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx",
            "ip_address": "143.19.23.16",
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
            cpe_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "cpe_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    cpe_id = module.params["cpe_id"]
    compartment_id = module.params["compartment_id"]
    result = []

    try:
        if cpe_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_cpe, cpe_id=cpe_id
                    ).data
                )
            ]
        else:
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_cpes,
                    display_name=module.params["display_name"],
                    compartment_id=compartment_id,
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(cpes=result)


if __name__ == "__main__":
    main()
