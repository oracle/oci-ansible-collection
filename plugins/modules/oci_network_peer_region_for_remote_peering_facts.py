#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_network_peer_region_for_remote_peering_facts
short_description: Fetches details about one or multiple PeerRegionForRemotePeering resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PeerRegionForRemotePeering resources in Oracle Cloud Infrastructure
    - Lists the regions that support remote VCN peering (which is peering across regions).
      For more information, see L(VCN Peering,https://docs.cloud.oracle.com/Content/Network/Tasks/VCNpeering.htm).
version_added: "2.9"
author: Oracle (@oracle)
options: {}
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List peer_region_for_remote_peerings
  oci_network_peer_region_for_remote_peering_facts:

"""

RETURN = """
peer_region_for_remote_peerings:
    description:
        - List of PeerRegionForRemotePeering resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The region's name.
                - "Example: `us-phoenix-1`"
            returned: on success
            type: string
            sample: us-phoenix-1
    sample: [{
        "name": "us-phoenix-1"
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


class PeerRegionForRemotePeeringFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_allowed_peer_regions_for_remote_peering, **optional_kwargs
        )


PeerRegionForRemotePeeringFactsHelperCustom = get_custom_class(
    "PeerRegionForRemotePeeringFactsHelperCustom"
)


class ResourceFactsHelper(
    PeerRegionForRemotePeeringFactsHelperCustom,
    PeerRegionForRemotePeeringFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(name=dict(type="str"),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="peer_region_for_remote_peering",
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

    module.exit_json(peer_region_for_remote_peerings=result)


if __name__ == "__main__":
    main()
