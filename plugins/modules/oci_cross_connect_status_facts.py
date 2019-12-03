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
module: oci_cross_connect_status_facts
short_description: Fetches details of OCI cross-connect status
description:
     - Fetches details of the OCI cross-connect status
version_added: "2.5"
options:
    cross_connect_id:
        description: Identifier of the cross-connect whose status needs to be fetched
        required: true
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch cross-connect status
- name: Fetch cross-connect status
  oci_cross_connect_status_facts:
      cross_connect_id: 'ocid1.crossconnect.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    oci_cross_connect_status:
        description: Attributes of the cross-connect Status.
        returned: success
        type: complex
        contains:
            cross_connect_id:
                description: The OCID of the cross-connect.
                returned: always
                type: string
                sample: ocid1.crossconect.oc1.iad.xxxxxEXAMPLExxxxx
            interface_state:
                description: Whether Oracle's side of the interface is up or down.
                returned: always
                type: string
                sample: UP
            light_level_ind_bm:
                description: The light level of the cross-connect (in dBm).
                returned: always
                type: string
                sample: 14.0
            light_level_indicator:
                description: tatus indicator corresponding to the light level.
                returned: always
                type: string
                sample: GOOD
        sample: [{
                    "cross_connect_id": "ocid1.crossconect.oc1.iad.xxxxxEXAMPLExxxxx",
                    "interface_state": "UP",
                    "light_level_ind_bm": 14.0,
                    "light_level_indicator": "GOOD"
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


def list_cross_connect_statuses(virtual_network_client, module):
    result = dict(cross_connect_statuses="")
    existing_cross_connect_statuses = None
    cross_connect_id = module.params.get("cross_connect_id")
    get_logger().info(
        "Retrieving cross-connect Status for cross-connect %s", cross_connect_id
    )
    try:
        existing_cross_connect_statuses = oci_utils.call_with_backoff(
            virtual_network_client.get_cross_connect_status,
            cross_connect_id=cross_connect_id,
        )
    except ServiceError as ex:
        get_logger().error("Unable to list cross-connect Status due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    result["cross_connect_statuses"] = to_dict(existing_cross_connect_statuses)

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_cross_connect_status_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(cross_connect_id=dict(type="str", required=True, aliases=["id"]))
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")
    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_cross_connect_statuses(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
