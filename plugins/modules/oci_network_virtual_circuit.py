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
module: oci_network_virtual_circuit
short_description: Manage a VirtualCircuit resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a VirtualCircuit resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new virtual circuit to use with Oracle Cloud
      Infrastructure FastConnect. For more information, see
      L(FastConnect Overview,https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm).
    - For the purposes of access control, you must provide the OCID of the
      compartment where you want the virtual circuit to reside. If you're
      not sure which compartment to use, put the virtual circuit in the
      same compartment with the DRG it's using. For more information about
      compartments and access control, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
      For information about OCIDs, see
      L(Resource Identifiers,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
    - "You may optionally specify a *display name* for the virtual circuit.
      It does not have to be unique, and you can change it. Avoid entering confidential information."
    - "**Important:** When creating a virtual circuit, you specify a DRG for
      the traffic to flow through. Make sure you attach the DRG to your
      VCN and confirm the VCN's routing sends traffic to the DRG. Otherwise
      traffic will not flow. For more information, see
      L(Route Tables,https://docs.cloud.oracle.com/Content/Network/Tasks/managingroutetables.htm)."
    - "This resource has the following action operations in the M(oci_virtual_circuit_actions) module: bulk_add_virtual_circuit_public_prefixes,
      bulk_delete_virtual_circuit_public_prefixes."
version_added: "2.5"
options:
    bandwidth_shape_name:
        description:
            - The provisioned data rate of the connection.  To get a list of the
              available bandwidth levels (that is, shapes), see
              L(ListFastConnectProviderServiceVirtualCircuitBandwidthShapes,https://docs.cloud.oracle.com/#/en/iaas/20160918/FastConnectProviderService/ListFast
              ConnectProviderVirtualCircuitBandwidthShapes).
            - "Example: `10 Gbps`"
        type: str
    compartment_id:
        description:
            - The OCID of the compartment to contain the virtual circuit.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    cross_connect_mappings:
        description:
            - Create a `CrossConnectMapping` for each cross-connect or cross-connect
              group this virtual circuit will run on.
        type: list
        suboptions:
            bgp_md5_auth_key:
                description:
                    - The key for BGP MD5 authentication. Only applicable if your system
                      requires MD5 authentication. If empty or not set (null), that
                      means you don't use BGP MD5 authentication.
                type: str
            cross_connect_or_cross_connect_group_id:
                description:
                    - The OCID of the cross-connect or cross-connect group for this mapping.
                      Specified by the owner of the cross-connect or cross-connect group (the
                      customer if the customer is colocated with Oracle, or the provider if the
                      customer is connecting via provider).
                type: str
            customer_bgp_peering_ip:
                description:
                    - The BGP IPv4 address for the router on the other end of the BGP session from
                      Oracle. Specified by the owner of that router. If the session goes from Oracle
                      to a customer, this is the BGP IPv4 address of the customer's edge router. If the
                      session goes from Oracle to a provider, this is the BGP IPv4 address of the
                      provider's edge router. Must use a /30 or /31 subnet mask.
                    - "There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses."
                    - "Example: `10.0.0.18/31`"
                type: str
            oracle_bgp_peering_ip:
                description:
                    - The IPv4 address for Oracle's end of the BGP session. Must use a /30 or /31
                      subnet mask. If the session goes from Oracle to a customer's edge router,
                      the customer specifies this information. If the session goes from Oracle to
                      a provider's edge router, the provider specifies this.
                    - "There's one exception: for a public virtual circuit, Oracle specifies the BGP IPv4 addresses."
                    - "Example: `10.0.0.19/31`"
                type: str
            vlan:
                description:
                    - The number of the specific VLAN (on the cross-connect or cross-connect group)
                      that is assigned to this virtual circuit. Specified by the owner of the cross-connect
                      or cross-connect group (the customer if the customer is colocated with Oracle, or
                      the provider if the customer is connecting via provider).
                    - "Example: `200`"
                type: int
    customer_bgp_asn:
        description:
            - Your BGP ASN (either public or private). Provide this value only if
              there's a BGP session that goes from your edge router to Oracle.
              Otherwise, leave this empty or null.
        type: int
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a
              namespace. For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no
              predefined name, type, or namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    gateway_id:
        description:
            - For private virtual circuits only. The OCID of the L(dynamic routing gateway (DRG),https://docs.cloud.oracle.com/#/en/iaas/20160918/Drg)
              that this virtual circuit uses.
        type: str
    provider_name:
        description:
            - Deprecated. Instead use `providerServiceId`.
              To get a list of the provider names, see
              L(ListFastConnectProviderServices,https://docs.cloud.oracle.com/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderServices).
        type: str
    provider_service_id:
        description:
            - The OCID of the service offered by the provider (if you're connecting
              via a provider). To get a list of the available service offerings, see
              L(ListFastConnectProviderServices,https://docs.cloud.oracle.com/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderServices).
        type: str
    provider_service_key_name:
        description:
            - The service key name offered by the provider (if the customer is connecting via a provider).
        type: str
    provider_service_name:
        description:
            - Deprecated. Instead use `providerServiceId`.
              To get a list of the provider names, see
              L(ListFastConnectProviderServices,https://docs.cloud.oracle.com/#/en/iaas/20160918/FastConnectProviderService/ListFastConnectProviderServices).
        type: str
    public_prefixes:
        description:
            - For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to
              advertise across the connection.
        type: list
        suboptions:
            cidr_block:
                description:
                    - An individual public IP prefix (CIDR) to add to the public virtual circuit.
                      All prefix sizes are allowed.
                type: str
                required: true
    region:
        description:
            - "The Oracle Cloud Infrastructure region where this virtual
              circuit is located.
              Example: `phx`"
        type: str
    type:
        description:
            - The type of IP addresses used in this virtual circuit. PRIVATE
              means L(RFC 1918,https://tools.ietf.org/html/rfc1918) addresses
              (10.0.0.0/8, 172.16/12, and 192.168/16).
            - Required for create using I(state=present).
        type: str
        choices:
            - "PUBLIC"
            - "PRIVATE"
    virtual_circuit_id:
        description:
            - The OCID of the virtual circuit.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    provider_state:
        description:
            - The provider's state in relation to this virtual circuit. Relevant only
              if the customer is using FastConnect via a provider.  ACTIVE
              means the provider has provisioned the virtual circuit from their
              end. INACTIVE means the provider has not yet provisioned the virtual
              circuit, or has de-provisioned it.
            - To be updated only by the provider.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
    reference_comment:
        description:
            - Provider-supplied reference information about this virtual circuit.
              Relevant only if the customer is using FastConnect via a provider.
            - To be updated only by the provider.
        type: str
    state:
        description:
            - The state of the VirtualCircuit.
            - Use I(state=present) to create or update a VirtualCircuit.
            - Use I(state=absent) to delete a VirtualCircuit.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create virtual_circuit
  oci_network_virtual_circuit:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    type: PUBLIC

- name: Update virtual_circuit using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_virtual_circuit:
    bandwidth_shape_name: 10 Gbps
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    customer_bgp_asn: 56
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    gateway_id: ocid1.gateway.oc1..xxxxxxEXAMPLExxxxxx
    provider_service_key_name: provider_service_key_name_example
    provider_state: ACTIVE
    reference_comment: reference_comment_example

- name: Update virtual_circuit
  oci_network_virtual_circuit:
    bandwidth_shape_name: 10 Gbps
    virtual_circuit_id: ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete virtual_circuit
  oci_network_virtual_circuit:
    virtual_circuit_id: ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete virtual_circuit using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_network_virtual_circuit:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    display_name: display_name_example
    state: absent

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
                  L(ListFastConnectProviderServiceVirtualCircuitBandwidthShapes,https://docs.cloud.oracle.com/#/en/iaas/20160918/FastConnectProviderService/List
                  FastConnectProviderVirtualCircuitBandwidthShapes).
                - "Example: `10 Gbps`"
            returned: on success
            type: string
            sample: 10 Gbps
        bgp_management:
            description:
                - Deprecated. Instead use the information in
                  L(FastConnectProviderService,https://docs.cloud.oracle.com/#/en/iaas/20160918/FastConnectProviderService/).
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
                - The BGP ASN of the network at the other end of the BGP
                  session from Oracle. If the session is between the customer's
                  edge router and Oracle, the value is the customer's ASN. If the BGP
                  session is between the provider's edge router and Oracle, the value
                  is the provider's ASN.
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
                - The OCID of the customer's L(dynamic routing gateway (DRG),https://docs.cloud.oracle.com/#/en/iaas/20160918/Drg)
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
                  in the format defined by RFC3339.
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient
    from oci.core.models import CreateVirtualCircuitDetails
    from oci.core.models import UpdateVirtualCircuitDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VirtualCircuitHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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

    def list_resources(self):
        required_list_method_params = [
            "compartment_id",
        ]

        optional_list_method_params = [
            "display_name",
        ]

        required_kwargs = dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_virtual_circuits, **kwargs
        )

    def get_create_model_class(self):
        return CreateVirtualCircuitDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_virtual_circuit,
            call_fn_args=(),
            call_fn_kwargs=dict(create_virtual_circuit_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateVirtualCircuitDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_virtual_circuit,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
                update_virtual_circuit_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_virtual_circuit,
            call_fn_args=(),
            call_fn_kwargs=dict(
                virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


VirtualCircuitHelperCustom = get_custom_class("VirtualCircuitHelperCustom")


class ResourceHelper(VirtualCircuitHelperCustom, VirtualCircuitHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            bandwidth_shape_name=dict(type="str"),
            compartment_id=dict(type="str"),
            cross_connect_mappings=dict(
                type="list",
                elements="dict",
                options=dict(
                    bgp_md5_auth_key=dict(type="str"),
                    cross_connect_or_cross_connect_group_id=dict(type="str"),
                    customer_bgp_peering_ip=dict(type="str"),
                    oracle_bgp_peering_ip=dict(type="str"),
                    vlan=dict(type="int"),
                ),
            ),
            customer_bgp_asn=dict(type="int"),
            defined_tags=dict(type="dict"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            gateway_id=dict(type="str"),
            provider_name=dict(type="str"),
            provider_service_id=dict(type="str"),
            provider_service_key_name=dict(type="str"),
            provider_service_name=dict(type="str"),
            public_prefixes=dict(
                type="list",
                elements="dict",
                options=dict(cidr_block=dict(type="str", required=True)),
            ),
            region=dict(type="str"),
            type=dict(type="str", choices=["PUBLIC", "PRIVATE"]),
            virtual_circuit_id=dict(aliases=["id"], type="str"),
            provider_state=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
            reference_comment=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
