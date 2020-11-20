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
module: oci_network_byoip_allocated_range_facts
short_description: Fetches details about one or multiple ByoipAllocatedRange resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ByoipAllocatedRange resources in Oracle Cloud Infrastructure
    - Lists the ByoipAllocatedRange objects for the ByoipRange.
      Each ByoipAllocatedRange object has a CIDR block part of the ByoipRange and the PublicIpPool it is assigned to.
version_added: "2.9"
author: Oracle (@oracle)
options:
    byoip_range_id:
        description:
            - The OCID of the Byoip Range object.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List byoip_allocated_ranges
  oci_network_byoip_allocated_range_facts:
    byoip_range_id: ocid1.byoiprange.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
byoip_allocated_ranges:
    description:
        - List of ByoipAllocatedRange resources
    returned: on success
    type: complex
    contains:
        cidr_block:
            description:
                - The address range part of the ByoipRange which is used for a publicIpPool.
            returned: on success
            type: string
            sample: cidr_block_example
        public_ip_pool_id:
            description:
                - The OCID of the PublicIpPool containing the part of the Byoip range.
            returned: on success
            type: string
            sample: ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
        "cidr_block": "cidr_block_example",
        "public_ip_pool_id": "ocid1.publicippool.oc1..xxxxxxEXAMPLExxxxxx"
    }]
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


class ByoipAllocatedRangeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "byoip_range_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_byoip_allocated_ranges,
            byoip_range_id=self.module.params.get("byoip_range_id"),
            **optional_kwargs
        )


ByoipAllocatedRangeFactsHelperCustom = get_custom_class(
    "ByoipAllocatedRangeFactsHelperCustom"
)


class ResourceFactsHelper(
    ByoipAllocatedRangeFactsHelperCustom, ByoipAllocatedRangeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(byoip_range_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="byoip_allocated_range",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(byoip_allocated_ranges=result)


if __name__ == "__main__":
    main()
