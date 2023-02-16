#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_network_drg_route_rules_actions
short_description: Perform actions on a DrgRouteRules resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DrgRouteRules resource in Oracle Cloud Infrastructure
    - For I(action=add), adds one or more static route rules to the specified DRG route table.
    - For I(action=remove), removes one or more route rules from the specified DRG route table.
    - For I(action=update), updates one or more route rules in the specified DRG route table.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    route_rule_ids:
        description:
            - The Oracle-assigned ID of each DRG route rule to be deleted.
            - Applicable only for I(action=remove).
        type: list
        elements: str
    drg_route_table_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DRG route table.
        type: str
        aliases: ["id"]
        required: true
    route_rules:
        description:
            - The collection of static rules used to insert routes into the DRG route table.
            - Applicable only for I(action=add)I(action=update).
        type: list
        elements: dict
        suboptions:
            id:
                description:
                    - The Oracle-assigned ID of each DRG route rule to update.
                type: str
            destination:
                description:
                    - This is the range of IP addresses used for matching when routing
                      traffic. Only CIDR_BLOCK values are allowed.
                    - "Potential values:
                        * IP address range in CIDR notation. This can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24`
                        or `2001:0db8:0123:45::/56`."
                type: str
            destination_type:
                description:
                    - "Type of destination for the rule.
                      Allowed values:
                        * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                type: str
                choices:
                    - "CIDR_BLOCK"
            next_hop_drg_attachment_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment. The next hop DRG
                      attachment is responsible
                      for reaching the network destination.
                type: str
    action:
        description:
            - The action to perform on the DrgRouteRules.
        type: str
        required: true
        choices:
            - "add"
            - "remove"
            - "update"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action add on drg_route_rules
  oci_network_drg_route_rules_actions:
    # required
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    action: add

    # optional
    route_rules:
    - # optional
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      destination: destination_example
      destination_type: CIDR_BLOCK
      next_hop_drg_attachment_id: "ocid1.nexthopdrgattachment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Perform action remove on drg_route_rules
  oci_network_drg_route_rules_actions:
    # required
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove

    # optional
    route_rule_ids: [ "route_rule_ids_example" ]

- name: Perform action update on drg_route_rules
  oci_network_drg_route_rules_actions:
    # required
    drg_route_table_id: "ocid1.drgroutetable.oc1..xxxxxxEXAMPLExxxxxx"
    action: update

    # optional
    route_rules:
    - # optional
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      destination: destination_example
      destination_type: CIDR_BLOCK
      next_hop_drg_attachment_id: "ocid1.nexthopdrgattachment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
drg_route_rules:
    description:
        - Details of the DrgRouteRules resource acted upon by the current operation
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
            type: str
            sample: destination_example
        destination_type:
            description:
                - The type of destination for the rule.
                - "Allowed values:"
                - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation.
                    * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                      L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                      particular `Service` through a service gateway)."
            returned: on success
            type: str
            sample: CIDR_BLOCK
        next_hop_drg_attachment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the next hop DRG attachment responsible
                  for reaching the network destination.
                - A value of `BLACKHOLE` means traffic for this route is discarded without notification.
            returned: on success
            type: str
            sample: "ocid1.nexthopdrgattachment.oc1..xxxxxxEXAMPLExxxxxx"
        route_type:
            description:
                - You can specify static routes for the DRG route table using the API.
                  The DRG learns dynamic routes from the DRG attachments using various routing protocols.
            returned: on success
            type: str
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
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        route_provenance:
            description:
                - The earliest origin of a route. If a route is advertised to a DRG through an IPsec tunnel attachment,
                  and is propagated to peered DRGs via RPC attachments, the route's provenance in the peered DRGs remains `IPSEC_TUNNEL`,
                  because that is the earliest origin.
                - No routes with a provenance `IPSEC_TUNNEL` or `VIRTUAL_CIRCUIT` will be exported to IPsec tunnel or virtual circuit attachments,
                  regardless of the attachment's export distribution.
            returned: on success
            type: str
            sample: STATIC
        attributes:
            description:
                - Additional properties for the route, computed by the service.
            returned: on success
            type: dict
            sample: {}
    sample: {
        "destination": "destination_example",
        "destination_type": "CIDR_BLOCK",
        "next_hop_drg_attachment_id": "ocid1.nexthopdrgattachment.oc1..xxxxxxEXAMPLExxxxxx",
        "route_type": "STATIC",
        "is_conflict": true,
        "is_blackhole": true,
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "route_provenance": "STATIC",
        "attributes": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import AddDrgRouteRulesDetails
    from oci.core.models import RemoveDrgRouteRulesDetails
    from oci.core.models import UpdateDrgRouteRulesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DrgRouteRulesActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add
        remove
        update
    """

    @staticmethod
    def get_module_resource_id_param():
        return "drg_route_table_id"

    def get_module_resource_id(self):
        return self.module.params.get("drg_route_table_id")

    def add(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddDrgRouteRulesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_drg_route_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_table_id=self.module.params.get("drg_route_table_id"),
                add_drg_route_rules_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def remove(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveDrgRouteRulesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_drg_route_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_table_id=self.module.params.get("drg_route_table_id"),
                remove_drg_route_rules_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def update(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, UpdateDrgRouteRulesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_drg_route_rules,
            call_fn_args=(),
            call_fn_kwargs=dict(
                drg_route_table_id=self.module.params.get("drg_route_table_id"),
                update_drg_route_rules_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


DrgRouteRulesActionsHelperCustom = get_custom_class("DrgRouteRulesActionsHelperCustom")


class ResourceHelper(DrgRouteRulesActionsHelperCustom, DrgRouteRulesActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            route_rule_ids=dict(type="list", elements="str"),
            drg_route_table_id=dict(aliases=["id"], type="str", required=True),
            route_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    id=dict(type="str"),
                    destination=dict(type="str"),
                    destination_type=dict(type="str", choices=["CIDR_BLOCK"]),
                    next_hop_drg_attachment_id=dict(type="str"),
                ),
            ),
            action=dict(type="str", required=True, choices=["add", "remove", "update"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="drg_route_rules",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
