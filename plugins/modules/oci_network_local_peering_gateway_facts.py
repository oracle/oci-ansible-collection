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
module: oci_network_local_peering_gateway_facts
short_description: Fetches details about one or multiple LocalPeeringGateway resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LocalPeeringGateway resources in Oracle Cloud Infrastructure
    - Lists the local peering gateways (LPGs) for the specified VCN and specified compartment.
      If the VCN ID is not provided, then the list includes the LPGs from all VCNs in the specified compartment.
    - If I(local_peering_gateway_id) is specified, the details of a single LocalPeeringGateway will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    local_peering_gateway_id:
        description:
            - The OCID of the local peering gateway.
            - Required to get a specific local_peering_gateway.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple local_peering_gateways.
        type: str
    vcn_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VCN.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List local_peering_gateways
  oci_network_local_peering_gateway_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific local_peering_gateway
  oci_network_local_peering_gateway_facts:
    local_peering_gateway_id: ocid1.localpeeringgateway.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
local_peering_gateways:
    description:
        - List of LocalPeeringGateway resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment containing the LPG.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a
                  namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable. Avoid
                  entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The LPG's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
            type: string
            sample: PROVISIONING
        peer_advertised_cidr:
            description:
                - The smallest aggregate CIDR that contains all the CIDR routes advertised by the VCN
                  at the other end of the peering from this LPG. See `peerAdvertisedCidrDetails` for
                  the individual CIDRs. The value is `null` if the LPG is not peered.
                - "Example: `192.168.0.0/16`, or if aggregated with `172.16.0.0/24` then `128.0.0.0/1`"
            returned: on success
            type: string
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
            type: string
            sample: INVALID
        peering_status_details:
            description:
                - Additional information regarding the peering status, if applicable.
            returned: on success
            type: string
            sample: peering_status_details_example
        route_table_id:
            description:
                - The OCID of the route table the LPG is using.
                - "For information about why you would associate a route table with an LPG, see
                  L(Transit Routing: Access to Multiple VCNs in Same Region,https://docs.cloud.oracle.com/Content/Network/Tasks/transitrouting.htm)."
            returned: on success
            type: string
            sample: ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx
        time_created:
            description:
                - The date and time the LPG was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        vcn_id:
            description:
                - The OCID of the VCN the LPG belongs to.
            returned: on success
            type: string
            sample: ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
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
        "route_table_id": "ocid1.routetable.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2016-08-25T21:10:29.600Z",
        "vcn_id": "ocid1.vcn.oc1..xxxxxxEXAMPLExxxxxx"
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


class LocalPeeringGatewayFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "local_peering_gateway_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_local_peering_gateway,
            local_peering_gateway_id=self.module.params.get("local_peering_gateway_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "vcn_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_local_peering_gateways,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LocalPeeringGatewayFactsHelperCustom = get_custom_class(
    "LocalPeeringGatewayFactsHelperCustom"
)


class ResourceFactsHelper(
    LocalPeeringGatewayFactsHelperCustom, LocalPeeringGatewayFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            local_peering_gateway_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            vcn_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="local_peering_gateway",
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

    module.exit_json(local_peering_gateways=result)


if __name__ == "__main__":
    main()
