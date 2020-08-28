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
module: oci_network_virtual_circuit_actions
short_description: Perform actions on a VirtualCircuit resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a VirtualCircuit resource in Oracle Cloud Infrastructure
    - For I(action=bulk_add_virtual_circuit_public_prefixes), adds one or more customer public IP prefixes to the specified public virtual circuit.
      Use this operation (and not L(UpdateVirtualCircuit,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/VirtualCircuit/UpdateVirtualCircuit))
      to add prefixes to the virtual circuit. Oracle must verify the customer's ownership
      of each prefix before traffic for that prefix will flow across the virtual circuit.
    - For I(action=bulk_delete_virtual_circuit_public_prefixes), removes one or more customer public IP prefixes from the specified public virtual circuit.
      Use this operation (and not L(UpdateVirtualCircuit,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/VirtualCircuit/UpdateVirtualCircuit))
      to remove prefixes from the virtual circuit. When the virtual circuit's state switches
      back to PROVISIONED, Oracle stops advertising the specified prefixes across the connection.
version_added: "2.9"
author: Oracle (@oracle)
options:
    virtual_circuit_id:
        description:
            - The OCID of the virtual circuit.
        type: str
        aliases: ["id"]
        required: true
    public_prefixes:
        description:
            - The public IP prefixes (CIDRs) to add to the public virtual circuit.
        type: list
        required: true
        suboptions:
            cidr_block:
                description:
                    - An individual public IP prefix (CIDR) to add to the public virtual circuit.
                      All prefix sizes are allowed.
                type: str
                required: true
    action:
        description:
            - The action to perform on the VirtualCircuit.
        type: str
        required: true
        choices:
            - "bulk_add_virtual_circuit_public_prefixes"
            - "bulk_delete_virtual_circuit_public_prefixes"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action bulk_add_virtual_circuit_public_prefixes on virtual_circuit
  oci_network_virtual_circuit_actions:
    virtual_circuit_id: ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx
    public_prefixes:
    - cidr_block: cidr_block_example
    action: bulk_add_virtual_circuit_public_prefixes

- name: Perform action bulk_delete_virtual_circuit_public_prefixes on virtual_circuit
  oci_network_virtual_circuit_actions:
    virtual_circuit_id: ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx
    public_prefixes:
    - cidr_block: cidr_block_example
    action: bulk_delete_virtual_circuit_public_prefixes

"""

RETURN = """
virtual_circuit:
    description:
        - Details of the VirtualCircuit resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        bandwidth_shape_name:
            description:
                - The provisioned data rate of the connection.  To get a list of the
                  available bandwidth levels (that is, shapes), see
                  L(ListFastConnectProviderServiceVirtualCircuitBandwidthShapes,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderVirtualCircuitBandwidthShapes).
                - "Example: `10 Gbps`"
            returned: on success
            type: string
            sample: 10 Gbps
        bgp_management:
            description:
                - Deprecated. Instead use the information in
                  L(FastConnectProviderService,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/FastConnectProviderService/).
            returned: on success
            type: string
            sample: CUSTOMER_MANAGED
        bgp_session_state:
            description:
                - The state of the BGP session associated with the virtual circuit.
            returned: on success
            type: string
            sample: UP
        compartment_id:
            description:
                - The OCID of the compartment containing the virtual circuit.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        cross_connect_mappings:
            description:
                - An array of mappings, each containing properties for a
                  cross-connect or cross-connect group that is associated with this
                  virtual circuit.
            returned: on success
            type: complex
            contains:
                bgp_md5_auth_key:
                    description:
                        - The key for BGP MD5 authentication. Only applicable if your system
                          requires MD5 authentication. If empty or not set (null), that
                          means you don't use BGP MD5 authentication.
                    returned: on success
                    type: string
                    sample: bgp_md5_auth_key_example
                cross_connect_or_cross_connect_group_id:
                    description:
                        - The OCID of the cross-connect or cross-connect group for this mapping.
                          Specified by the owner of the cross-connect or cross-connect group (the
                          customer if the customer is colocated with Oracle, or the provider if the
                          customer is connecting via provider).
                    returned: on success
                    type: string
                    sample: ocid1.crossconnectorcrossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx
                customer_bgp_peering_ip:
                    description:
                        - The BGP IPv4 address for the router on the other end of the BGP session from
                          Oracle. Specified by the owner of that router. If the session goes from Oracle
                          to a customer, this is the BGP IPv4 address of the customer's edge router. If the
                          session goes from Oracle to a provider, this is the BGP IPv4 address of the
                          provider's edge router. Must use a /30 or /31 subnet mask.
                        - "There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses."
                        - "Example: `10.0.0.18/31`"
                    returned: on success
                    type: string
                    sample: 10.0.0.18/31
                oracle_bgp_peering_ip:
                    description:
                        - The IPv4 address for Oracle's end of the BGP session. Must use a /30 or /31
                          subnet mask. If the session goes from Oracle to a customer's edge router,
                          the customer specifies this information. If the session goes from Oracle to
                          a provider's edge router, the provider specifies this.
                        - "There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses."
                        - "Example: `10.0.0.19/31`"
                    returned: on success
                    type: string
                    sample: 10.0.0.19/31
                vlan:
                    description:
                        - The number of the specific VLAN (on the cross-connect or cross-connect group)
                          that is assigned to this virtual circuit. Specified by the owner of the cross-connect
                          or cross-connect group (the customer if the customer is colocated with Oracle, or
                          the provider if the customer is connecting via provider).
                        - "Example: `200`"
                    returned: on success
                    type: int
                    sample: 200
        customer_bgp_asn:
            description:
                - Deprecated. Instead use `customerAsn`.
                  If you specify values for both, the request will be rejected.
            returned: on success
            type: int
            sample: 56
        customer_asn:
            description:
                - "The BGP ASN of the network at the other end of the BGP
                  session from Oracle. If the session is between the customer's
                  edge router and Oracle, the value is the customer's ASN. If the BGP
                  session is between the provider's edge router and Oracle, the value
                  is the provider's ASN.
                  Can be a 2-byte or 4-byte ASN. Uses \\"asplain\\" format."
            returned: on success
            type: int
            sample: 56
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
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
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
        gateway_id:
            description:
                - The OCID of the customer's L(dynamic routing gateway (DRG),https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Drg)
                  that this virtual circuit uses. Applicable only to private virtual circuits.
            returned: on success
            type: string
            sample: ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx
        id:
            description:
                - The virtual circuit's Oracle ID (OCID).
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The virtual circuit's current state. For information about
                  the different states, see
                  L(FastConnect Overview,https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm).
            returned: on success
            type: string
            sample: PENDING_PROVIDER
        oracle_bgp_asn:
            description:
                - The Oracle BGP ASN.
            returned: on success
            type: int
            sample: 56
        provider_name:
            description:
                - Deprecated. Instead use `providerServiceId`.
            returned: on success
            type: string
            sample: provider_name_example
        provider_service_id:
            description:
                - The OCID of the service offered by the provider (if the customer is connecting via a provider).
            returned: on success
            type: string
            sample: ocid1.providerservice.oc1..xxxxxxEXAMPLExxxxxx
        provider_service_key_name:
            description:
                - The service key name offered by the provider (if the customer is connecting via a provider).
            returned: on success
            type: string
            sample: provider_service_key_name_example
        provider_service_name:
            description:
                - Deprecated. Instead use `providerServiceId`.
            returned: on success
            type: string
            sample: provider_service_name_example
        provider_state:
            description:
                - The provider's state in relation to this virtual circuit (if the
                  customer is connecting via a provider). ACTIVE means
                  the provider has provisioned the virtual circuit from their end.
                  INACTIVE means the provider has not yet provisioned the virtual
                  circuit, or has de-provisioned it.
            returned: on success
            type: string
            sample: ACTIVE
        public_prefixes:
            description:
                - For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
                  advertise across the connection. All prefix sizes are allowed.
            returned: on success
            type: list
            sample: []
        reference_comment:
            description:
                - Provider-supplied reference information about this virtual circuit
                  (if the customer is connecting via a provider).
            returned: on success
            type: string
            sample: reference_comment_example
        region:
            description:
                - The Oracle Cloud Infrastructure region where this virtual
                  circuit is located.
            returned: on success
            type: string
            sample: region_example
        service_type:
            description:
                - Provider service type.
            returned: on success
            type: string
            sample: COLOCATED
        time_created:
            description:
                - The date and time the virtual circuit was created,
                  in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
        type:
            description:
                - Whether the virtual circuit supports private or public peering. For more information,
                  see L(FastConnect Overview,https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm).
            returned: on success
            type: string
            sample: PUBLIC
    sample: {
        "bandwidth_shape_name": "10 Gbps",
        "bgp_management": "CUSTOMER_MANAGED",
        "bgp_session_state": "UP",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "cross_connect_mappings": [{
            "bgp_md5_auth_key": "bgp_md5_auth_key_example",
            "cross_connect_or_cross_connect_group_id": "ocid1.crossconnectorcrossconnectgroup.oc1..xxxxxxEXAMPLExxxxxx",
            "customer_bgp_peering_ip": "10.0.0.18/31",
            "oracle_bgp_peering_ip": "10.0.0.19/31",
            "vlan": 200
        }],
        "customer_bgp_asn": 56,
        "customer_asn": 56,
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "display_name": "display_name_example",
        "freeform_tags": {'Department': 'Finance'},
        "gateway_id": "ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PENDING_PROVIDER",
        "oracle_bgp_asn": 56,
        "provider_name": "provider_name_example",
        "provider_service_id": "ocid1.providerservice.oc1..xxxxxxEXAMPLExxxxxx",
        "provider_service_key_name": "provider_service_key_name_example",
        "provider_service_name": "provider_service_name_example",
        "provider_state": "ACTIVE",
        "public_prefixes": [],
        "reference_comment": "reference_comment_example",
        "region": "region_example",
        "service_type": "COLOCATED",
        "time_created": "2016-08-25T21:10:29.600Z",
        "type": "PUBLIC"
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
    from oci.core.models import BulkAddVirtualCircuitPublicPrefixesDetails
    from oci.core.models import BulkDeleteVirtualCircuitPublicPrefixesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualCircuitActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        bulk_add_virtual_circuit_public_prefixes
        bulk_delete_virtual_circuit_public_prefixes
    """

    @staticmethod
    def get_module_resource_id_param():
        return "virtual_circuit_id"

    def get_module_resource_id(self):
        return self.module.params.get("virtual_circuit_id")

    def get_get_fn(self):
        return self.client.get_virtual_circuit

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_virtual_circuit,
            virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
        )

    def bulk_add_virtual_circuit_public_prefixes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkAddVirtualCircuitPublicPrefixesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_add_virtual_circuit_public_prefixes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
                bulk_add_virtual_circuit_public_prefixes_details=action_details,
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

    def bulk_delete_virtual_circuit_public_prefixes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, BulkDeleteVirtualCircuitPublicPrefixesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.bulk_delete_virtual_circuit_public_prefixes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
                bulk_delete_virtual_circuit_public_prefixes_details=action_details,
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


VirtualCircuitActionsHelperCustom = get_custom_class(
    "VirtualCircuitActionsHelperCustom"
)


class ResourceHelper(VirtualCircuitActionsHelperCustom, VirtualCircuitActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            virtual_circuit_id=dict(aliases=["id"], type="str", required=True),
            public_prefixes=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(cidr_block=dict(type="str", required=True)),
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "bulk_add_virtual_circuit_public_prefixes",
                    "bulk_delete_virtual_circuit_public_prefixes",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="virtual_circuit",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
