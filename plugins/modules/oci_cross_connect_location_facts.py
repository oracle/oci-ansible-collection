#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
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
module: oci_cross_connect_location_facts
short_description: Fetches details of one or more OCI cross-connect Locations
description:
     - Fetches details of the OCI cross-connect Locations
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which cross-connect Locations exists
        required: true
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch All cross-connect Locations under a specific compartment
- name: Fetch All cross-connect Locations under a specific compartment
  oci_cross_connect_location_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    oci_cross_connect_locations:
        description: Attributes of the cross-connect Location.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The OCID of the compartment containing the cross-connect location.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx
        sample: [{
                    "description":"Equinix",
                    "name":"Equinix"
                },
                {
                    "description":"CoreSite",
                    "name":"CoreSite"
                }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_cross_connect_locations(virtual_network_client, module):
    result = dict(cross_connect_locations="")
    compartment_id = module.params.get("compartment_id")
    get_logger().info(
        "Retrieving all cross-connect Locations in Compartment %s", compartment_id
    )
    try:
        result["cross_connect_locations"] = to_dict(
            oci_utils.list_all_resources(
                virtual_network_client.list_cross_connect_locations,
                compartment_id=compartment_id,
            )
        )
    except ServiceError as ex:
        get_logger().error(
            "Unable to list all cross-connect Locations due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_cross_connect_location_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str", required=True)))
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")
    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_cross_connect_locations(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
