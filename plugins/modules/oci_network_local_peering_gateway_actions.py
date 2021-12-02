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
module: oci_network_local_peering_gateway_actions
short_description: Perform actions on a LocalPeeringGateway resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a LocalPeeringGateway resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a local peering gateway into a different compartment within the same tenancy. For information
      about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
    - "For I(action=connect), connects this local peering gateway (LPG) to another one in the same region.
      This operation must be called by the VCN administrator who is designated as
      the *requestor* in the peering relationship. The *acceptor* must implement
      an Identity and Access Management (IAM) policy that gives the requestor permission
      to connect to LPGs in the acceptor's compartment. Without that permission, this
      operation will fail. For more information, see
      L(VCN Peering,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/VCNpeering.htm)."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    local_peering_gateway_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the local peering gateway.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the
              local peering gateway to.
            - Required for I(action=change_compartment).
        type: str
    peer_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the LPG you want to peer with.
            - Required for I(action=connect).
        type: str
    action:
        description:
            - The action to perform on the LocalPeeringGateway.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "connect"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on local_peering_gateway
  oci_network_local_peering_gateway_actions:
    # required
    local_peering_gateway_id: "ocid1.localpeeringgateway.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action connect on local_peering_gateway
  oci_network_local_peering_gateway_actions:
    # required
    local_peering_gateway_id: "ocid1.localpeeringgateway.oc1..xxxxxxEXAMPLExxxxxx"
    peer_id: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
    action: connect

"""

RETURN = """
local_peering_gateway:
    description:
        - Details of the LocalPeeringGateway resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the LPG.
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
                - The LPG's Oracle ID (L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm)).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_cross_tenancy_peering:
            description:
                - Whether the VCN at the other end of the peering is in a different tenancy.
                - "Example: `false`"
            returned: on success
            type: bool
            sample: false
        lifecycle_state:
            description:
                - The LPG's current lifecycle state.
            returned: on success
            type: str
            sample: PROVISIONING
        peer_advertised_cidr:
            description:
                - The smallest aggregate CIDR that contains all the CIDR routes advertised by the VCN
                  at the other end of the peering from this LPG. See `peerAdvertisedCidrDetails` for
                  the individual CIDRs. The value is `null` if the LPG is not peered.
                - "Example: `192.168.0.0/16`, or if aggregated with `172.16.0.0/24` then `128.0.0.0/1`"
            returned: on success
            type: str
            sample: 192.168.0.0/16
        peer_advertised_cidr_details:
            description:
                - The specific ranges of IP addresses available on or via the VCN at the other
                  end of the peering from this LPG. The value is `null` if the LPG is not peered.
                  You can use these as destination CIDRs for route rules to route a subnet's
                  traffic to this LPG.
                - "Example: [`192.168.0.0/16`, `172.16.0.0/24`]"
            returned: on success
            type: list
            sample: []
        peering_status:
            description:
                - Whether the LPG is peered with another LPG. `NEW` means the LPG has not yet been
                  peered. `PENDING` means the peering is being established. `REVOKED` means the
                  LPG at the other end of the peering has been deleted.
            returned: on success
            type: str
            sample: INVALID
        peering_status_details:
            description:
                - Additional information regarding the peering status, if applicable.
            returned: on success
            type: str
            sample: peering_status_details_example
        peer_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the peered LPG.
            returned: on success
            type: str
            sample: "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx"
        route_table_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the route table the LPG is using.
                - "For information about why you would associate a route table with an LPG, see
                  L(Transit Routing: Access to Multiple VCNs in Same Region,https://docs.cloud.oracle.com/iaas/Content/Network/Tasks/transitrouting.htm)."
            returned: on success
            type: str
            sample: "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the LPG was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2016-08-25T21:10:29.600Z"
        vcn_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the VCN that uses the LPG.
            returned: on success
            type: str
            sample: "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cross_tenancy_peering": false,
        "lifecycle_state": "PROVISIONING",
        "peer_advertised_cidr": "192.168.0.0/16",
        "peer_advertised_cidr_details": [],
        "peering_status": "INVALID",
        "peering_status_details": "peering_status_details_example",
        "peer_id": "ocid1.peer.oc1..xxxxxxEXAMPLExxxxxx",
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import ChangeLocalPeeringGatewayCompartmentDetails
    from oci.core.models import ConnectLocalPeeringGatewaysDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LocalPeeringGatewayActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        connect
    """

    @staticmethod
    def get_module_resource_id_param():
        return "local_peering_gateway_id"

    def get_module_resource_id(self):
        return self.module.params.get("local_peering_gateway_id")

    def get_get_fn(self):
        return self.client.get_local_peering_gateway

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_local_peering_gateway,
            local_peering_gateway_id=self.module.params.get("local_peering_gateway_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeLocalPeeringGatewayCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_local_peering_gateway_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                local_peering_gateway_id=self.module.params.get(
                    "local_peering_gateway_id"
                ),
                change_local_peering_gateway_compartment_details=action_details,
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

    def connect(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ConnectLocalPeeringGatewaysDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.connect_local_peering_gateways,
            call_fn_args=(),
            call_fn_kwargs=dict(
                local_peering_gateway_id=self.module.params.get(
                    "local_peering_gateway_id"
                ),
                connect_local_peering_gateways_details=action_details,
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


LocalPeeringGatewayActionsHelperCustom = get_custom_class(
    "LocalPeeringGatewayActionsHelperCustom"
)


class ResourceHelper(
    LocalPeeringGatewayActionsHelperCustom, LocalPeeringGatewayActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            local_peering_gateway_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
            peer_id=dict(type="str"),
            action=dict(
                type="str", required=True, choices=["change_compartment", "connect"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="local_peering_gateway",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
