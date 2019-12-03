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
module: oci_waas_edge_subnet_facts
short_description: Retrieve facts of subnets corresponding the Web Application Firewall.
description:
    - Returns a list of subnets corresponding the Web Application Firewall. Return the list of the tenant's edge node
      subnets. Use these CIDR blocks to restrict incoming traffic to your origin. These subnets are owned by OCI and
      forward traffic to customer origins. They are not associated with specific regions or compartments.
version_added: "2.5"
options:
    sort_by:
        description: The value by which edge node subnets are sorted.
        choices: ["cidr", "region", "timeModified"]
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_sort_order_option ]
"""

EXAMPLES = """
- name: Get all the edge subnets
  oci_waas_edge_subnet_facts:

- name: Get all the edge subnets sorted by region
  oci_waas_edge_subnet_facts:
    sort_by: region
    sort_order: DESC
"""

RETURN = """
waas_edge_subnets:
    description: List of the tenant's edge node subnets.
    returned: on success
    type: complex
    contains:
        cidr:
            description: CIDR of an edge node subnet. This can include /24 or /8 addresses.
            returned: success
            type: str
            sample: 52.28.32.104
        region:
            description: The name of the region containing the indicated subnet.
            returned: success
            type: str
            sample: Europe
        time_modified:
            description: The date and time the last change was made to the indicated edge node subnet, expressed in
                         RFC 3339 timestamp format.
            returned: success
            type: str
            sample: 2017-01-30T13:27:08+00:00
    sample: [{
                "cidr": "52.28.32.104",
                "region": "Europe",
                "time_modified": "2017-01-30T13:27:08+00:00"
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.waas.waas_client import WaasClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def list_edge_subnets(waas_client, module):
    optional_list_method_params = ["sort_by", "sort_order"]
    optional_kwargs = dict(
        (param, module.params[param])
        for param in optional_list_method_params
        if module.params.get(param) is not None
    )
    return to_dict(
        oci_utils.list_all_resources(waas_client.list_edge_subnets, **optional_kwargs)
    )


def main():
    module_args = oci_utils.get_facts_module_arg_spec(
        filter_by_display_name=False,
        supports_sort=True,
        sort_by_choices=["cidr", "region", "timeModified"],
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    waas_client = oci_utils.create_service_client(module, WaasClient)
    try:
        result = list_edge_subnets(waas_client, module)
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(waas_edge_subnets=result)


if __name__ == "__main__":
    main()
