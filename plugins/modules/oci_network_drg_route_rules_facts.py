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
module: oci_network_drg_route_rules_facts
short_description: Fetches details about one or multiple DrgRouteRules resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DrgRouteRules resources in Oracle Cloud Infrastructure
    - Lists the route rules in the specified DRG route table.
version_added: "2.9"
author: Oracle (@oracle)
options:
    drg_route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
        type: str
        required: true
    route_type:
        description:
            - Static routes are specified through the DRG route table API.
              Dynamic routes are learned by the DRG from the DRG attachments through various routing protocols.
        type: str
        choices:
            - "STATIC"
            - "DYNAMIC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List drg_route_rules
  oci_network_drg_route_rules_facts:
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
drg_route_rules:
    description:
        - List of DrgRouteRules resources
    returned: on success
    type: complex
    contains:
        destination:
            description:
                - Represents the range of IP addresses to match against when routing traffic.
                - "Potential values:
                    * An IP address range (IPv4 or IPv6) in CIDR notation. For example: `192.168.1.0/24`
                    or `2001:0db8:0123:45::/56`.
                    * When you're setting up a security rule for traffic destined for a particular `Service` through
                    a service gateway, this is the `cidrBlock` value associated with that L(Service,https://docs.cloud.oracle.com/en-
                    us/iaas/api/#/en/iaas/20160918/Service/). For example: `oci-phx-objectstorage`."
            returned: on success
            type: string
            sample: destination_example
        destination_type:
            description:
                - The type of destination for the rule. the type is required if `direction` = `EGRESS`.
                - "Allowed values:"
                - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.
                    * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                      L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                      particular `Service` through a service gateway)."
            returned: on success
            type: string
            sample: CIDR_BLOCK
        next_hop_drg_attachment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment responsible
                  for reaching the network destination.
                - A value of `BLACKHOLE` means traffic for this route is discarded without notification.
            returned: on success
            type: string
            sample: "ocid1.nexthopdrgattachment.oc1..xxxxxxEXAMPLExxxxxx"
        route_type:
            description:
                - You can specify static routes for the DRG route table using the API.
                  The DRG learns dynamic routes from the DRG attachments using various routing protocols.
            returned: on success
            type: string
            sample: STATIC
        is_conflict:
            description:
                - Indicates that the route was not imported due to a conflict between route rules.
            returned: on success
            type: bool
            sample: true
        is_blackhole:
            description:
                - Indicates that if the next hop attachment does not exist, so traffic for this route is discarded without notification.
            returned: on success
            type: bool
            sample: true
        id:
            description:
                - The Oracle-assigned ID of the DRG route rule.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        route_provenance:
            description:
                - The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment,
                  and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`,
                  because that is the earliest origin.
                - No routes with a provenance `IPSEC_TUNNEL` or `VIRTUAL_CIRCUIT` will be exported to IPsec tunnel or virtual circuit attachments,
                  regardless of the attachment's export distribution.
            returned: on success
            type: string
            sample: STATIC
    sample: [{
        "destination": "destination_example",
        "destination_type": "CIDR_BLOCK",
        "next_hop_drg_attachment_id": "ocid1.nexthopdrgattachment.oc1..xxxxxxEXAMPLExxxxxx",
        "route_type": "STATIC",
        "is_conflict": true,
        "is_blackhole": true,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "route_provenance": "STATIC"
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


class DrgRouteRulesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "drg_route_table_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "route_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_drg_route_rules,
            drg_route_table_id=self.module.params.get("drg_route_table_id"),
            **optional_kwargs
        )


DrgRouteRulesFactsHelperCustom = get_custom_class("DrgRouteRulesFactsHelperCustom")


class ResourceFactsHelper(DrgRouteRulesFactsHelperCustom, DrgRouteRulesFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            drg_route_table_id=dict(type="str", required=True),
            route_type=dict(type="str", choices=["STATIC", "DYNAMIC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="drg_route_rules",
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

    module.exit_json(drg_route_rules=result)


if __name__ == "__main__":
    main()
