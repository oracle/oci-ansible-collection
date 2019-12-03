#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_virtual_circuit_facts
short_description: Fetches details of one or more OCI Virtual Circuits
description:
     - Fetches details of a specified OCI Virtual Circuit or all Virtual Circuit in a specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which the specified Virtual Circuit exists
        required: false
    virtual_circuit_id:
        description: Identifier of the Virtual Circuit whose details needs to be fetched.
        required: false
        aliases: [ 'id' ]
    lifecycle_state:
        description: A filter to return only resources that match the given lifecycle state.
        required: false
        choices: ["PENDING_PROVIDER", "VERIFYING", "PROVISIONING", "PROVISIONED", "FAILED", "INACTIVE", "TERMINATING", "TERMINATED"]
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option  ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch All Virtual Circuits under a specific compartment
- name: Fetch All Virtual Circuits under a specific compartment
  oci_virtual_circuit_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'


# Fetch All Virtual Circuits under a specific compartment, filtered by
# display name and lifecycle state
- name: Fetch All Virtual Circuits under a specific compartment, filtered by display name and lifecycle state
  oci_virtual_circuit_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'
      display_name: 'ansible-virtual-circuit'
      lifecycle_state: 'PROVISIONED'

# Fetch a specific Virtual Circuit
- name: Fetch a specific Virtual Circuit
  oci_virtual_circuit_facts:
      virtual_circuit_id: 'ocid1.virtualcircuit.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    oci_virtual_circuits:
        description: Attributes of the Fetched Virtual Circuit.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The OCID of the compartment containing the Virtual Circuit.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx
            display_name:
                description: A user-friendly name. Does not have to be unique, and it's changeable.
                             Avoid entering confidential information.
                returned: always
                type: string
                sample: ansible-virtual-circuit
            id:
                description: Identifier of the Virtual Circuit.
                returned: always
                type: string
                sample: ocid1.virtualcircuit.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the Virtual Circuit was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            lifecycle_state:
                description: The current state of the Virtual Circuit.
                returned: always
                type: string
                sample: PROVISIONED
            bgp_management:
                description: BGP management option.
                returned: always
                type: string
                sample: CUSTOMER_MANAGED
            bgp_session_state:
                description: The state of the BGP session associated with the virtual circuit.
                returned: always
                type: string
                sample: UP
            cross_connect_mappings:
                description: An array of mappings, each containing properties for a cross-connect or
                             cross-connect group that is associated with this virtual circuit.
                returned: always
                type: list
                sample: [
                          {
                            "bgp_md5_auth_key":null,
                            "cross_connect_or_cross_connect_group_id":null,
                            "customer_bgp_peering_ip":"10.0.0.18/31",
                            "oracle_bgp_peering_ip":"10.0.0.19/31",
                            "vlan":null
                          }
                       ]
            customer_bgp_asn:
                description: The BGP ASN of the network at the other end of the BGP session from Oracle.
                             If the session is between the customer's edge router and Oracle, the value is
                             the customer's ASN. If the BGP session is between the provider's edge router
                             and Oracle, the value is the provider's ASN.
                returned: always
                type: int
                sample: 10
            gateway_id:
                description: The OCID of the customer's dynamic routing gateway (DRG) that this virtual
                             circuit uses. Applicable only to private virtual circuits.
                returned: always
                type: string
                sample: 'ocid1.drg..xxxxxEXAMPLExxxxx'
            oracle_bgp_asn:
                description: The Oracle BGP ASN.
                returned: always
                type: int
                sample: 31898
            provider_name:
                description: Name of the Provider.
                returned: always
                type: string
                sample: 'Megaport'
            provider_service_id:
                description: The OCID of the service offered by the provider (if the customer is
                             connecting via a provider).
                returned: always
                type: string
                sample: 'ocid1.providerservice.oc1..xxxxxEXAMPLExxxxx'
            provider_service_name:
                description: Name of the Provider Service.
                returned: always
                type: string
                sample: 'Service'
            provider_state:
                description: The provider's state in relation to this virtual circuit (if the customer
                             is connecting via a provider). ACTIVE means the provider has provisioned
                             the virtual circuit from their end. INACTIVE means the provider has not
                             yet provisioned the virtual circuit, or has de-provisioned it.
                returned: always
                type: string
                sample: 'INACTIVE'
            public_prefixes:
                description: For a public virtual circuit. The public IP prefixes (CIDRs) the customer
                             wants to advertise across the connection. Each prefix must be /31 or less
                             specific.
                returned: always
                type: list
                sample: [{
                           'cidr_block': '10.0.0.10/31'

                        }]
            reference_comment:
                description: Provider-supplied reference information about this virtual circuit
                             (if the customer is connecting via a provider).
                returned: always
                type: string
                sample: 'SAMPLE'
            region:
                description: The Oracle Cloud Infrastructure region where this virtual circuit is located.
                returned: always
                type: string
                sample: 'phx'
            service_type:
                description: Provider service type.
                returned: always
                type: string
                sample: 'COLOCATED'
            type:
                description: Whether the virtual circuit supports private or public peering.
                returned: always
                type: string
                sample: 'PUBLIC'
            port_speed_shape_name:
                description: The port speed for this cross-connect.
                returned: always
                type: string
                sample: 10 Gbps
        sample: [{
                    "bandwidth_shape_name":"10 Gbps",
                    "bgp_management":"CUSTOMER_MANAGED",
                    "bgp_session_state":"DOWN",
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "cross_connect_mappings":[
                                              {
                                                "bgp_md5_auth_key":null,
                                                "cross_connect_or_cross_connect_group_id":"ocid1.crossconnectgroup.xxxxxEXAMPLExxxxx",
                                                "customer_bgp_peering_ip":"169.254.203.202/30",
                                                "oracle_bgp_peering_ip":"169.254.203.201/30",
                                                "vlan":105
                                              }
                                             ],
                    "customer_bgp_asn":5,
                    "display_name":"sample-virtual-circuit",
                    "gateway_id":null,
                    "id":"ocid1.virtualcircuit.oc1..xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"PROVISIONED",
                    "oracle_bgp_asn":31898,
                    "provider_name":null,
                    "provider_service_id":null,
                    "provider_service_name":null,
                    "provider_state":null,
                    "public_prefixes":null,
                    "reference_comment":null,
                    "region":null,
                    "service_type":"COLOCATED",
                    "time_created":"2018-12-15T12:09:34.999000+00:00",
                    "type":"PUBLIC"
                }]
"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_virtual_circuits(virtual_network_client, module):
    result = dict(virtual_circuits="")
    compartment_id = module.params.get("compartment_id")
    virtual_circuit_id = module.params.get("virtual_circuit_id")
    try:
        if compartment_id:
            optional_list_method_params = ["display_name", "lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_virtual_circuits = oci_utils.list_all_resources(
                virtual_network_client.list_virtual_circuits,
                compartment_id=compartment_id,
                **optional_kwargs
            )
        elif virtual_circuit_id:
            response = oci_utils.call_with_backoff(
                virtual_network_client.get_virtual_circuit,
                virtual_circuit_id=virtual_circuit_id,
            )
            existing_virtual_circuits = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["virtual_circuits"] = to_dict(existing_virtual_circuits)
    return result


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            virtual_circuit_id=dict(type="str", required=False, aliases=["id"]),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=[
                    "PENDING_PROVIDER",
                    "VERIFYING",
                    "PROVISIONING",
                    "PROVISIONED",
                    "FAILED",
                    "INACTIVE",
                    "TERMINATING",
                    "TERMINATED",
                ],
            ),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args, mutually_exclusive=[["compartment_id", "id"]]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_virtual_circuits(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
