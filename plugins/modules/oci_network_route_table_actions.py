#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_network_route_table_actions
short_description: Perform actions on a RouteTable resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a RouteTable resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a route table into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    rt_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              route table to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the RouteTable.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on route_table
  oci_network_route_table_actions:
    # required
    rt_id: "ocid1.rt.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
route_table:
    description:
        - Details of the RouteTable resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the route table.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The route table's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The route table's current state.
            returned: on success
            type: str
            sample: PROVISIONING
        route_rules:
            description:
                - The collection of rules for routing destination IPs to network devices.
            returned: on success
            type: complex
            contains:
                cidr_block:
                    description:
                        - Deprecated. Instead use `destination` and `destinationType`. Requests that include both
                          `cidrBlock` and `destination` will be rejected.
                        - A destination IP address range in CIDR notation. Matching packets will
                          be routed to the indicated network entity (the target).
                        - Cannot be an IPv6 CIDR.
                        - "Example: `0.0.0.0/0`"
                    returned: on success
                    type: str
                    sample: cidr_block_example
                destination:
                    description:
                        - Conceptually, this is the range of IP addresses used for matching when routing
                          traffic. Required if you provide a `destinationType`.
                        - "Allowed values:"
                        - " * IP address range in CIDR notation. Can be an IPv4 or IPv6 CIDR. For example: `192.168.1.0/24`
                            or `2001:0db8:0123:45::/56`. If you set this to an IPv6 CIDR, the route rule's target
                            can only be a DRG or internet gateway.
                            IPv6 addressing is supported for all commercial and government regions.
                            See L(IPv6 Addresses,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/ipv6.htm)."
                        - " * The `cidrBlock` value for a L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/), if you're
                              setting up a route rule for traffic destined for a particular `Service` through
                              a service gateway. For example: `oci-phx-objectstorage`."
                    returned: on success
                    type: str
                    sample: destination_example
                destination_type:
                    description:
                        - Type of destination for the rule. Required if you provide a `destination`.
                        - " * `CIDR_BLOCK`: If the rule's `destination` is an IP address range in CIDR notation."
                        - " * `SERVICE_CIDR_BLOCK`: If the rule's `destination` is the `cidrBlock` value for a
                              L(Service,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/Service/) (the rule is for traffic destined for a
                              particular `Service` through a service gateway)."
                    returned: on success
                    type: str
                    sample: CIDR_BLOCK
                network_entity_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) for the route rule's target. For information
                          about the type of
                          targets you can specify, see
                          L(Route Tables,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/managingroutetables.htm).
                    returned: on success
                    type: str
                    sample: "ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx"
                description:
                    description:
                        - An optional description of your choice for the rule.
                    returned: on success
                    type: str
                    sample: description_example
                route_type:
                    description:
                        - A route rule can be STATIC if manually added to the route table, LOCAL if added by OCI to the route table.
                    returned: on success
                    type: str
                    sample: STATIC
        time_created:
            description:
                - The date and time the route table was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN the route table list belongs to.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "route_rules": [{
            "cidr_block": "cidr_block_example",
            "destination": "destination_example",
            "destination_type": "CIDR_BLOCK",
            "network_entity_id": "ocid1.networkentity.oc1..xxxxxxEXAMPLExxxxxx",
            "description": "description_example",
            "route_type": "STATIC"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.core.models import ChangeRouteTableCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RouteTableActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "rt_id"

    def get_module_resource_id(self):
        return self.module.params.get("rt_id")

    def get_get_fn(self):
        return self.client.get_route_table

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_route_table, rt_id=self.module.params.get("rt_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeRouteTableCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_route_table_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                rt_id=self.module.params.get("rt_id"),
                change_route_table_compartment_details=action_details,
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


RouteTableActionsHelperCustom = get_custom_class("RouteTableActionsHelperCustom")


class ResourceHelper(RouteTableActionsHelperCustom, RouteTableActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            rt_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="route_table",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
