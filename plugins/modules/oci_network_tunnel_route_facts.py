#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_network_tunnel_route_facts
short_description: Fetches details about one or multiple TunnelRoute resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TunnelRoute resources in Oracle Cloud Infrastructure
    - The routes advertised to the Customer and the routes received from the Customer.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    ipsc_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the IPSec connection.
        type: str
        required: true
    tunnel_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tunnel.
        type: str
        required: true
    advertiser:
        description:
            - Specifies the advertiser of the routes. If set to ORACLE, then returns only the
              routes advertised by ORACLE, else if set to CUSTOMER, then returns only the
              routes advertised by the CUSTOMER.
        type: str
        choices:
            - "CUSTOMER"
            - "ORACLE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List tunnel_routes
  oci_network_tunnel_route_facts:
    # required
    ipsc_id: "ocid1.ipsc.oc1..xxxxxxEXAMPLExxxxxx"
    tunnel_id: "ocid1.tunnel.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    advertiser: advertiser_example

"""

RETURN = """
tunnel_routes:
    description:
        - List of TunnelRoute resources
    returned: on success
    type: complex
    contains:
        prefix:
            description:
                - BGP Network Layer Reachability Information
            returned: on success
            type: str
            sample: prefix_example
        age:
            description:
                - The age of the route
            returned: on success
            type: int
            sample: 56
        is_best_path:
            description:
                - Is this the best route
            returned: on success
            type: bool
            sample: true
        as_path:
            description:
                - List of ASNs in AS Path
            returned: on success
            type: list
            sample: []
        advertiser:
            description:
                - Route advertiser
            returned: on success
            type: str
            sample: CUSTOMER
    sample: [{
        "prefix": "prefix_example",
        "age": 56,
        "is_best_path": true,
        "as_path": [],
        "advertiser": "CUSTOMER"
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


class TunnelRouteFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "ipsc_id",
            "tunnel_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "advertiser",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_ip_sec_connection_tunnel_routes,
            ipsc_id=self.module.params.get("ipsc_id"),
            tunnel_id=self.module.params.get("tunnel_id"),
            **optional_kwargs
        )


TunnelRouteFactsHelperCustom = get_custom_class("TunnelRouteFactsHelperCustom")


class ResourceFactsHelper(TunnelRouteFactsHelperCustom, TunnelRouteFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            ipsc_id=dict(type="str", required=True),
            tunnel_id=dict(type="str", required=True),
            advertiser=dict(type="str", choices=["CUSTOMER", "ORACLE"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tunnel_route",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(tunnel_routes=result)


if __name__ == "__main__":
    main()
