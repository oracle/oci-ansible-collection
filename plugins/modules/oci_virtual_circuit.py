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
module: oci_virtual_circuit
short_description: Create, update and delete OCI Virtual Circuit
description:
    - Create an OCI Virtual Circuit to use with Oracle Cloud Infrastructure FastConnect
    - Update an OCI Virtual Circuit, if present
    - Delete an OCI Virtual Circuit, if present.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which this Virtual Circuit
                     would be created. Mandatory for create operation.
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
                     Avoid entering confidential information.
        required: false
        aliases: ['name']
    virtual_circuit_id:
        description: Identifier of the Virtual Circuit. Mandatory for delete and update.
        required: false
        aliases: ['id']
    bandwidth_shape_name:
        description: The provisioned data rate of the connection.
        required: false
    cross_connect_mappings:
        description: An array of mappings, each containing properties for a cross-connect or
                     cross-connect group that is associated with this virtual circuit.
        suboptions:
            bgp_md5_auth_key:
               description: The key for BGP MD5 authentication. Only applicable if your system
                            requires MD5 authentication. If empty or not set, that means
                            you don't use BGP MD5 authentication.
               required: false
            cross_connect_or_cross_connect_group_id:
               description: The OCID of the cross-connect or cross-connect group for this mapping.
                            Specified by the owner of the cross-connect or cross-connect group
                            (the customer if the customer is colocated with Oracle, or the provider
                            if the customer is connecting via provider).
               required: false
            customer_bgp_peering_ip:
               description: The BGP IP address for the router on the other end of the BGP session from
                            Oracle. Specified by the owner of that router. If the session goes from Oracle
                            to a customer, this is the BGP IP address of the customer's edge router. If the
                            session goes from Oracle to a provider, this is the BGP IP address of the provider's
                            edge router. Must use a /30 or /31 subnet mask. There's one exception, for a public
                            virtual circuit, Oracle specifies the BGP IP addresses.
               required: false
            oracle_bgp_peering_ip:
               description: The IP address for Oracle's end of the BGP session. Must use a /30 or /31 subnet mask.
                            If the session goes from Oracle to a customer's edge router, the customer specifies this
                            information. If the session goes from Oracle to a provider's edge router, the provider
                            specifies this. There's one exception, for a public virtual circuit, Oracle specifies the
                            BGP IP addresses.
               required: false
            vlan:
               description: The number of the specific VLAN (on the cross-connect or cross-connect group) that is assigned
                            to this virtual circuit. Specified by the owner of the cross-connect or cross-connect group
                            (the customer if the customer is colocated with Oracle, or the provider if the customer is
                            connecting via provider).
               required: false
        required: false
    customer_bgp_asn:
        description: Your BGP ASN (either public or private). Provide this value only if there's a BGP session that goes from
                     your edge router to Oracle. Otherwise, leave this empty or null.
        required: false
    gateway_id:
        description: For private virtual circuits only. The OCID of the dynamic routing gateway (DRG) that this virtual circuit uses.
        required: false
    provider_name:
        description: Deprecated. Instead use provider_service_id.
        required: false
    provider_service_id:
        description: The OCID of the service offered by the provider (if you're connecting via a provider).
        required: false
    provider_service_name:
        description: Deprecated. Instead use provider_service_id.
        required: false
    public_prefixes:
        description: For a public virtual circuit. The public IP prefixes (CIDRs) the customer wants to advertise across the connection.
        suboptions:
              cidr_block:
                    description: An individual public IP prefix (CIDR) to add to the public virtual circuit. Must be /31 or less specific.
                    required: true
        required: false
    region:
        description: The Oracle Cloud Infrastructure region where this virtual circuit is located.
        required: false
    type:
        description: The type of IP addresses used in this virtual circuit. PRIVATE means RFC 1918 addresses (10.0.0.0/8, 172.16/12, and 192.168/16).
                     Only PRIVATE is supported.
        required: false
        choices: ['PUBLIC','PRIVATE']
    purge_cross_connect_mappings:
        description: Purge cross connect mappings from virtual circuit which are not present in the provided cross connect
                     mappings list.If I(purge_cross_connect_mappings=no), provided cross connect mappings would be appended to
                     existing cross connect mappings. I(purge_cross_connect_mappings) and I(delete_cross_connect_mappings) are
                     mutually exclusive.
        required: false
        default: true
        type: bool
    delete_cross_connect_mappings:
        description: Delete any cross connect mappings in the virtual circuit that is specified in I(cross_connect_mappings).
                     If I(delete_cross_connect_mappings=yes), cross connect mappings provided by I(cross_connect_mappings)
                     would be deleted from existing cross connect mappings, if they are part of existing cross connect mappings.
                     If they are not part of existing cross connect mappings, they will be ignored. I(delete_cross_connect_mappings)
                     and I(purge_cross_connect_mappings) are mutually exclusive.
        required: false
        default: 'no'
        type: bool
    delete_public_prefixes:
        description: Indicates whether public prefixes associated with a public virtual circuit needs to be deleted.
                     If I(delete_public_prefixes=false), then input publi prefixes gets added.
        required: false
        default: false
    reference_comment:
        description: Provider-supplied reference information about this virtual circuit. Relevant only if the customer
                     is using FastConnect via a provider. To be updated only by the provider.
        required: false
    provider_state:
        description: The provider's state in relation to this virtual circuit. Relevant only if the customer is using
                     FastConnect via a provider. ACTIVE means the provider has provisioned the virtual circuit from
                     their end. INACTIVE means the provider has not yet provisioned the virtual circuit, or has
                     de-provisioned it.
        required: false
        choices: ['ACTIVE','INACTIVE']
    state:
        description: Create,update or delete cross-connect group. For I(state=present), if it
                     does not exists, it gets created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options, oracle_creatable_resource ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create a new colocated Virtual Circuit
- name: Create a new colocated Virtual Circuit
  oci_virtual_circuit:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      display_name: 'ansible-virtual-circuit'
      cross_connect_mappings:
            - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
              vlan: 100
      public_prefixes:
             - 206.209.218.0/24
      customer_bgp_asn: 5
      type: 'PUBLIC'
      port_speed_shape_name: '10 Gbps'
      state: 'present'

# Create a new colocated Virtual Circuit
- name: Create a new colocated Virtual Circuit of private type
  oci_virtual_circuit:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      display_name: 'ansible-virtual-circuit-private'
      cross_connect_mappings:
            - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
              customer_bgp_peering_ip: '10.0.0.18/31'
              oracle_bgp_peering_ip: '10.0.0.19/31'
              vlan: 100
      customer_bgp_asn: 5
      type: 'PRIVATE'
      port_speed_shape_name: '10 Gbps'
      state: 'present'

# Create a Virtual Circuit using Provider
- name: Create a Virtual Circuit using Provider
  oci_virtual_circuit:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      display_name: 'ansible-virtual-circuit'
      provider_service_id: 'ocid1.providerservice...xxxxxEXAMPLExxxxx'
      customer_bgp_asn: 5
      type: 'PUBLIC'
      port_speed_shape_name: '10 Gbps'
      state: 'present'

# Update an existing Virtual Circuit's Cross Connect Mappings
- name: Update an existing Virtual Circuit's Cross Connect Mappings
  oci_virtual_circuit:
      virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
      cross_connect_mappings:
            - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
              vlan: 105
      state: 'present'

# Update an existing Virtual Circuit's Cross Connect Mappings by appending new Cross Connect Mappings
- name: Update an existing Virtual Circuit's Cross Connect Mappings by appending new Cross Connect Mappings
  oci_virtual_circuit:
      virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
      cross_connect_mappings:
            - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
              vlan: 100
      purge_cross_connect_mappings: false
      state: 'present'

# Update an existing Virtual Circuit's Cross Connect Mappings by deleting a Cross Connect Mappings
- name: Update an existing Virtual Circuit's Cross Connect Mappings by deleting a Cross Connect Mappings
  oci_virtual_circuit:
      virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
      cross_connect_mappings:
            - cross_connect_or_cross_connect_group_id: 'ocid1.crossconnectgroup..xxxxxEXAMPLExxxxx'
              vlan: 100
      delete_cross_connect_mappings: false
      state: 'present'

# Update an existing Virtual Circuit by deleting Public Prefixes
- name: Update an existing Virtual Circuit by deleting Public Prefixes
  oci_virtual_circuit:
      virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
      public_prefixes:
            - '10.0.0.21/31'
      delete_public_prefixes: true
      state: 'present'

# Delete Virtual Circuit
- name: Delete Virtual Circuit
  oci_virtual_circuit:
      virtual_circuit_id: 'ocid1.virtualcircuit..xxxxxEXAMPLExxxxx'
      state: 'absent'
"""

RETURN = """
    oci_virtual_circuit:
        description: Attributes of the Virtual Circuit.
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
        sample: {
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
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from operator import eq

try:
    from oci.core import VirtualNetworkClient
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict
    from oci.core.models import (
        CreateVirtualCircuitDetails,
        CrossConnectMapping,
        CreateVirtualCircuitPublicPrefixDetails,
        DeleteVirtualCircuitPublicPrefixDetails,
        UpdateVirtualCircuitDetails,
        BulkAddVirtualCircuitPublicPrefixesDetails,
        BulkDeleteVirtualCircuitPublicPrefixesDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_virtual_circuit(virtual_network_client, module):
    result = dict(changed=False, virtual_circuit="")
    virtual_circuit_id = module.params.get("virtual_circuit_id")
    exclude_attributes = {"display_name": True, "public_prefixes": True}
    try:
        if virtual_circuit_id:
            existing_virtual_circuit = oci_utils.get_existing_resource(
                virtual_network_client.get_virtual_circuit,
                module,
                virtual_circuit_id=virtual_circuit_id,
            )
            result = update_virtual_circuit(
                virtual_network_client, existing_virtual_circuit, module
            )
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="virtual_circuit",
                create_fn=create_virtual_circuit,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_virtual_circuits,
                kwargs_list={"compartment_id": module.params.get("compartment_id")},
                module=module,
                exclude_attributes=exclude_attributes,
                model=CreateVirtualCircuitDetails(),
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    return result


def create_virtual_circuit(virtual_network_client, module):
    create_virtual_circuit_details = CreateVirtualCircuitDetails()
    for attribute in create_virtual_circuit_details.attribute_map:
        create_virtual_circuit_details.__setattr__(
            attribute, module.params.get(attribute)
        )
    create_virtual_circuit_details.cross_connect_mappings = get_cross_connect_mappings(
        module
    )
    create_virtual_circuit_details.public_prefixes = get_public_prefixes(module)
    result = oci_utils.create_and_wait(
        resource_type="virtual_circuit",
        create_fn=virtual_network_client.create_virtual_circuit,
        kwargs_create={
            "create_virtual_circuit_details": create_virtual_circuit_details
        },
        client=virtual_network_client,
        get_fn=virtual_network_client.get_virtual_circuit,
        get_param="virtual_circuit_id",
        module=module,
    )
    return result


def get_cross_connect_mappings(module):
    input_cross_connect_mappings = module.params.get("cross_connect_mappings")
    if input_cross_connect_mappings is None:
        return None
    result_cross_connect_mappings = []
    for input_cross_connect_mapping_dict in input_cross_connect_mappings:
        cross_connect_mapping = oci_utils.create_hashed_instance(CrossConnectMapping)
        if module.params.get("type") == "PUBLIC" and (
            input_cross_connect_mapping_dict.get("oracle_bgp_peering_ip")
            or input_cross_connect_mapping_dict.get("customer_bgp_peering_ip")
        ):
            module.fail_json(
                msg="oracle_bgp_peering_ip or customer_bgp_peering_ip is not allowed for public virual circuit"
            )
        if module.params.get("type") == "PRIVATE" and (
            input_cross_connect_mapping_dict.get("oracle_bgp_peering_ip") is None
            or input_cross_connect_mapping_dict.get("customer_bgp_peering_ip") is None
        ):
            module.fail_json(
                msg="oracle_bgp_peering_ip and customer_bgp_peering_ip are mandatory for private virual circuit"
            )
        for attribute in cross_connect_mapping.attribute_map:
            cross_connect_mapping.__setattr__(
                attribute, input_cross_connect_mapping_dict.get(attribute)
            )
        result_cross_connect_mappings.append(cross_connect_mapping)
    return result_cross_connect_mappings


def get_public_prefixes(module):
    input_public_prefixes = module.params.get("public_prefixes")
    if input_public_prefixes is None:
        return None
    result_public_prefixes = []
    virtual_circuit_public_prefixes_details = None
    for input_public_prefix in input_public_prefixes:
        if module.params.get("delete_public_prefixes"):
            virtual_circuit_public_prefixes_details = (
                DeleteVirtualCircuitPublicPrefixDetails()
            )
        else:
            virtual_circuit_public_prefixes_details = (
                CreateVirtualCircuitPublicPrefixDetails()
            )
        virtual_circuit_public_prefixes_details.cidr_block = input_public_prefix
        result_public_prefixes.append(virtual_circuit_public_prefixes_details)

    return result_public_prefixes


def update_virtual_circuit(virtual_network_client, existing_virtual_circuit, module):
    result = dict(virtual_circuit=to_dict(existing_virtual_circuit), changed=False)
    attributes_changed = False
    cross_connect_mappings_changed = False
    update_virtual_circuit_details = UpdateVirtualCircuitDetails()
    for attribute in update_virtual_circuit_details.attribute_map:
        if attribute != "cross_connect_mappings":
            if module.params.get(attribute) is not None and not eq(
                module.params.get(attribute),
                getattr(existing_virtual_circuit, attribute),
            ):
                attributes_changed = True
                update_virtual_circuit_details.__setattr__(
                    attribute, module.params.get(attribute)
                )
    purge_cross_connect_mappings = module.params.get(
        "purge_cross_connect_mappings", True
    )
    delete_cross_connect_mappings = module.params.get("delete_cross_connect_mappings")
    input_cross_connect_mappings = get_cross_connect_mappings(module)
    existing_cross_connect_mappings = oci_utils.get_hashed_object_list(
        CrossConnectMapping, existing_virtual_circuit.cross_connect_mappings
    )
    if existing_virtual_circuit.type == "PUBLIC":
        remove_assigned_bgp_peering_ips(existing_cross_connect_mappings)
    if input_cross_connect_mappings is not None:
        cross_connect_mappings, cross_connect_mappings_changed = oci_utils.check_and_return_component_list_difference(
            input_cross_connect_mappings,
            existing_cross_connect_mappings,
            purge_cross_connect_mappings,
            delete_cross_connect_mappings,
        )
    if cross_connect_mappings_changed:
        update_virtual_circuit_details.cross_connect_mappings = cross_connect_mappings
    else:
        update_virtual_circuit_details.cross_connect_mappings = (
            existing_cross_connect_mappings
        )
    if attributes_changed or cross_connect_mappings_changed:
        result = oci_utils.update_and_wait(
            resource_type="virtual_circuit",
            update_fn=virtual_network_client.update_virtual_circuit,
            kwargs_update={
                "update_virtual_circuit_details": update_virtual_circuit_details,
                "virtual_circuit_id": existing_virtual_circuit.id,
            },
            client=virtual_network_client,
            get_fn=virtual_network_client.get_virtual_circuit,
            get_param="virtual_circuit_id",
            module=module,
        )

    if module.params.get("public_prefixes") is not None:
        result = bulk_add_or_delete_public_prefixes(
            get_public_prefixes(module),
            virtual_network_client,
            existing_virtual_circuit.id,
            module,
        )

    return result


def bulk_add_or_delete_public_prefixes(
    input_public_prefixes, virtual_network_client, virtual_circuit_id, module
):
    update_fn = None
    kwargs_update = None
    virtual_circuit_public_prefixes_details = None
    if module.params.get("delete_public_prefixes"):
        virtual_circuit_public_prefixes_details = (
            BulkDeleteVirtualCircuitPublicPrefixesDetails()
        )
        update_fn = virtual_network_client.bulk_delete_virtual_circuit_public_prefixes
        kwargs_update = {
            "bulk_delete_virtual_circuit_public_prefixes_details": virtual_circuit_public_prefixes_details,
            "virtual_circuit_id": virtual_circuit_id,
        }
    else:
        virtual_circuit_public_prefixes_details = (
            BulkAddVirtualCircuitPublicPrefixesDetails()
        )
        update_fn = virtual_network_client.bulk_add_virtual_circuit_public_prefixes
        kwargs_update = {
            "bulk_add_virtual_circuit_public_prefixes_details": virtual_circuit_public_prefixes_details,
            "virtual_circuit_id": virtual_circuit_id,
        }
    virtual_circuit_public_prefixes_details.public_prefixes = input_public_prefixes
    result = oci_utils.update_and_wait(
        resource_type="virtual_circuit",
        update_fn=update_fn,
        kwargs_update=kwargs_update,
        client=virtual_network_client,
        get_fn=virtual_network_client.get_virtual_circuit,
        kwargs_get={"virtual_circuit_id": virtual_circuit_id},
        get_param=None,
        module=module,
    )
    return result


def remove_assigned_bgp_peering_ips(existing_cross_connect_mappings):
    for existing_cross_connect_mapping in existing_cross_connect_mappings:
        existing_cross_connect_mapping.oracle_bgp_peering_ip = None
        existing_cross_connect_mapping.customer_bgp_peering_ip = None


def delete_virtual_circuit(virtual_network_client, module):
    return oci_utils.delete_and_wait(
        resource_type="virtual_circuit",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_virtual_circuit,
        kwargs_get={"virtual_circuit_id": module.params["virtual_circuit_id"]},
        delete_fn=virtual_network_client.delete_virtual_circuit,
        kwargs_delete={"virtual_circuit_id": module.params["virtual_circuit_id"]},
        module=module,
    )


def main():
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        compartment_id=dict(type="str", required=False),
        display_name=dict(type="str", required=False, aliases=["name"]),
        virtual_circuit_id=dict(type="str", required=False, aliases=["id"]),
        bandwidth_shape_name=dict(type="str", required=False),
        cross_connect_mappings=dict(type=list, required=False),
        customer_bgp_asn=dict(type=int, required=False),
        state=dict(
            type="str", required=False, default="present", choices=["present", "absent"]
        ),
        gateway_id=dict(type="str", required=False),
        provider_name=dict(type="str", required=False),
        provider_service_id=dict(type="str", required=False),
        provider_service_name=dict(type="str", required=False),
        public_prefixes=dict(type=list, required=False),
        reference_comment=dict(type="str", required=False),
        region=dict(type="str", required=False),
        provider_state=dict(type="str", required=False, choices=["ACTIVE", "INACTIVE"]),
        type=dict(type="str", required=False, choices=["PUBLIC", "PRIVATE"]),
        purge_cross_connect_mappings=dict(type="bool", required=False, default=True),
        delete_cross_connect_mappings=dict(type="bool", required=False, default=False),
        delete_public_prefixes=dict(type=bool, required=False, default=False),
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[
            ["purge_cross_connect_mappings", "delete_cross_connect_mappings"]
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    state = module.params["state"]

    if state == "present":
        result = create_or_update_virtual_circuit(virtual_network_client, module)
    elif state == "absent":
        result = delete_virtual_circuit(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
