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
module: oci_peer_region_for_remote_peering_facts
short_description: Retrieve the regions that support remote VCN peering
description:
    - This module retrieves the regions that support remote VCN peering (which is peering across regions).
version_added: "2.5"
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of the regions that supports remote VCN peering
  oci_peer_region_for_remote_peering_facts:
"""

RETURN = """
peer_region_for_remote_peering:
    description: Details of regions that support remote VCN peering
    returned: always
    type: complex
    contains:
        name:
            description: The region's name.
            returned: always
            type: string
            sample: us-phoenix-1
    sample: [{
            "name": us-phoenix-1
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
    module_args = oci_utils.get_common_arg_spec()

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    try:
        result = to_dict(
            oci_utils.call_with_backoff(
                virtual_network_client.list_allowed_peer_regions_for_remote_peering
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(peer_region_for_remote_peering=result)


if __name__ == "__main__":
    main()
