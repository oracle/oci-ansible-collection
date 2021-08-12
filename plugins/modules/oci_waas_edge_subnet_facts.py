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
module: oci_waas_edge_subnet_facts
short_description: Fetches details about one or multiple WaasEdgeSubnet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WaasEdgeSubnet resources in Oracle Cloud Infrastructure
    - Return the list of the tenant's edge node subnets. Use these CIDR blocks to restrict incoming traffic to your origin. These subnets are owned by OCI and
      forward traffic to customer origins. They are not associated with specific regions or compartments.
version_added: "2.9"
author: Oracle (@oracle)
options:
    sort_by:
        description:
            - The value by which edge node subnets are sorted in a paginated 'List' call. If unspecified, defaults to `timeModified`.
        type: str
        choices:
            - "cidr"
            - "region"
            - "timeModified"
    sort_order:
        description:
            - The value of the sorting direction of resources in a paginated 'List' call. If unspecified, defaults to `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List waas_edge_subnets
  oci_waas_edge_subnet_facts:

"""

RETURN = """
waas_edge_subnets:
    description:
        - List of WaasEdgeSubnet resources
    returned: on success
    type: complex
    contains:
        cidr:
            description:
                - An edge node subnet. This can include /24 or /8 addresses.
            returned: on success
            type: string
            sample: 192.0.2.0/24
        time_modified:
            description:
                - The date and time the last change was made to the indicated edge node subnet, expressed in RFC 3339 timestamp format.
            returned: on success
            type: string
            sample: 2018-11-16T21:10:29Z
        region:
            description:
                - The name of the region containing the indicated subnet.
            returned: on success
            type: string
            sample: US-Central
    sample: [{
        "cidr": "192.0.2.0/24",
        "time_modified": "2018-11-16T21:10:29Z",
        "region": "US-Central"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class WaasEdgeSubnetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_edge_subnets, **optional_kwargs
        )


WaasEdgeSubnetFactsHelperCustom = get_custom_class("WaasEdgeSubnetFactsHelperCustom")


class ResourceFactsHelper(
    WaasEdgeSubnetFactsHelperCustom, WaasEdgeSubnetFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            sort_by=dict(type="str", choices=["cidr", "region", "timeModified"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="waas_edge_subnet",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(waas_edge_subnets=result)


if __name__ == "__main__":
    main()
