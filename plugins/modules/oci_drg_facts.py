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
module: oci_drg_facts
short_description: Retrieve facts of Dynamic Routing Gateways(DRGs)
description:
    - This module retrieves information of the specified dynamic routing gateway(DRG) or lists all the DRG in the
      specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to get all the DRGs in the compartment.
        required: false
    drg_id:
        description: The OCID of the DRG. I(drg_id) is required to get a specific DRG's information.
        required: false
        aliases: [ 'id' ]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the DRGs in a compartment
  oci_drg_facts:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'

- name: Get a specific DRG using its OCID
  oci_drg_facts:
    drg_id: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
drgs:
    description: List of DRG details
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment containing the DRG.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: Name of the DRG.
            returned: always
            type: string
            sample: ansible_drg
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: OCID of the DRG.
            returned: always
            type: string
            sample: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: Current state of the DRG.
            returned: always
            type: string
            sample: AVAILABLE
        time_created:
            description: The date and time the DRG was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-11-13T20:22:40.626000+00:00
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible_drg",
            "id": "ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
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
            drg_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "drg_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    drg_id = module.params["drg_id"]
    compartment_id = module.params["compartment_id"]
    result = []

    try:
        if drg_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_drg, drg_id=drg_id
                    ).data
                )
            ]
        else:
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_drgs,
                    display_name=module.params["display_name"],
                    compartment_id=compartment_id,
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(drgs=result)


if __name__ == "__main__":
    main()
