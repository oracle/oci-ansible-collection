#!/usr/bin/python
# Copyright (c) 2017, 2019, Oracle and/or its affiliates.
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
module: oci_subnet
short_description: Manage subnets in a VCN in OCI
description:
    - This module allows the user to create, delete and update subnets in a VCN in OCI.
version_added: "2.5"
options:
    availability_domain:
        description: The Availability Domain to contain the subnet. If not specified while using I(state=present) a regional subnet will be created.
        required: false
    cidr_block:
        description: The CIDR IP address range of the subnet. Required when creating a subnet with I(state=present).
        required: false
    compartment_id:
        description: The OCID of the compartment to contain the subnet. Required when creating a subnet with
                     I(state=present).
        required: false
    dhcp_options_id:
        description: The OCID of the set of DHCP options the subnet will use. If you don't provide a value, the subnet
                     will use the VCN's default set of DHCP options.
        required: False
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information.
        required: false
        aliases: [ 'name' ]
    dns_label:
        description: A DNS label for the subnet, used in conjunction with the VNIC's hostname and VCN's DNS label to
                     form a fully qualified domain name (FQDN) for each VNIC within this subnet (for example,
                     bminstance-1.subnet123.vcn1.oraclevcn.com). Must be an alphanumeric string that begins with a
                     letter and is unique within the VCN. The value cannot be changed. This value must be set if you
                     want to use the Internet and VCN Resolver to resolve the hostnames of instances in the subnet. It
                     can only be set if the VCN itself was created with a DNS label.
        required: false
    prohibit_public_ip_on_vnic:
        description: Whether VNICs within this subnet can have public IP addresses. If
                     I(prohibit_public_ip_on_vnic=false), VNICs created in this subnet will automatically be assigned
                     public IP addresses unless specified otherwise during instance launch or VNIC creation (with the
                     assignPublicIp flag in CreateVnicDetails). If I(prohibit_public_ip_on_vnic=true), VNICs created in
                     this subnet cannot have public IP addresses (that is, it's a private subnet).
        required: false
        default: false
        type: bool
    route_table_id:
        description: The OCID of the route table the subnet will use. If you don't provide a value, the subnet will
                     use the VCN's default route table.
        required: false
    security_list_ids:
        description: List of OCIDs of security lists to associate with the subnet. If you don't provide a value,
                     the VCN's default security list will be associated with the subnet. Remember that security lists
                     are associated at the subnet level, but the rules are applied to the individual VNICs in the
                     subnet.
        required: false
    state:
        description: Create or update a subnet with I(state=present). Delete a subnet with I(state=absent).
        required: false
        default: present
        choices: ['present', 'absent']
    subnet_id:
        description: The OCID of the subnet. Required when deleting a subnet with I(state=absent) or updating a subnet
                     with I(state=present).
        required: false
        aliases: [ 'id' ]
    vcn_id:
        description: The OCID of the VCN to contain the subnet. Required when creating a subnet with I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a subnet
  oci_subnet:
    availability_domain: BnQb:PHX-AD-1
    cidr_block: 10.0.1.0/24
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    prohibit_public_ip_on_vnic: true
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx

- name: Create a regional subnet
  oci_subnet:
    cidr_block: 10.0.1.0/24
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    prohibit_public_ip_on_vnic: true
    vcn_id: ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx

- name: Update subnet's display name and associated route table
  oci_subnet:
    display_name: ansible_subnet
    subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx
    route_table_id: "ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx"

- name: Update subnet's associated security lists and DHCP options
  oci_subnet:
    subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx
    security_list_ids: ["ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx"]
    dhcp_options_id: "ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx"

- name: Delete a subnet
  oci_subnet:
    subnet_id: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx
    state: 'absent'
"""

RETURN = """
subnet:
    description: Information about the subnet
    returned: On successful create and update operation
    type: dict
    sample: {
            "availability_domain": "BnQb:PHX-AD-1",
            "cidr_block": "10.0.1.0/24",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "dhcp_options_id": "ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx",
            "display_name": "ansible_subnet",
            "dns_label": ansiblesubnet,
            "id": "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "prohibit_public_ip_on_vnic": true,
            "route_table_id": "ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx",
            "security_list_ids": [
                "ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx"
            ],
            "subnet_domain_name": ansiblesubnet.ansiblevcn.oraclevcn.com,
            "time_created": "2017-11-16T03:05:50.992000+00:00",
            "vcn_id": "ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx",
            "virtual_router_ip": "10.0.1.1",
            "virtual_router_mac": "00:00:17:D1:27:79"
        }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreateSubnetDetails
    from oci.core.models import UpdateSubnetDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_subnet(virtual_network_client, module):
    return oci_utils.delete_and_wait(
        resource_type="subnet",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_subnet,
        kwargs_get={"subnet_id": module.params["subnet_id"]},
        delete_fn=virtual_network_client.delete_subnet,
        kwargs_delete={"subnet_id": module.params["subnet_id"]},
        module=module,
    )


def update_subnet(virtual_network_client, module):
    return oci_utils.check_and_update_resource(
        resource_type="subnet",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_subnet,
        kwargs_get={"subnet_id": module.params["subnet_id"]},
        update_fn=virtual_network_client.update_subnet,
        primitive_params_update=["subnet_id"],
        kwargs_non_primitive_update={UpdateSubnetDetails: "update_subnet_details"},
        module=module,
        update_attributes=UpdateSubnetDetails().attribute_map.keys(),
    )


def create_subnet(virtual_network_client, module):
    create_subnet_details = CreateSubnetDetails()
    for attribute in create_subnet_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_subnet_details, attribute, module.params[attribute])

    return oci_utils.create_and_wait(
        resource_type="subnet",
        create_fn=virtual_network_client.create_subnet,
        kwargs_create={"create_subnet_details": create_subnet_details},
        client=virtual_network_client,
        get_fn=virtual_network_client.get_subnet,
        get_param="subnet_id",
        module=module,
    )


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=False),
            cidr_block=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
            dhcp_options_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            dns_label=dict(type="str", required=False),
            prohibit_public_ip_on_vnic=dict(type="bool", required=False, default=False),
            route_table_id=dict(type="str", required=False),
            security_list_ids=dict(type="list", required=False),
            subnet_id=dict(type="str", required=False, aliases=["id"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            vcn_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )
    exclude_attributes = {
        "display_name": True,
        "dns_label": True,
        "dhcp_options_id": True,
    }
    state = module.params["state"]
    subnet_id = module.params["subnet_id"]

    if state == "absent":
        if subnet_id is not None:
            result = delete_subnet(virtual_network_client, module)
        else:
            module.fail_json(
                msg="Specify subnet_id with state as 'absent' to delete a subnet."
            )

    else:
        if subnet_id is not None:
            result = update_subnet(virtual_network_client, module)
        else:
            vcn = oci_utils.call_with_backoff(
                virtual_network_client.get_vcn, vcn_id=module.params["vcn_id"]
            ).data

            default_attribute_values = {
                "dhcp_options_id": vcn.default_dhcp_options_id,
                "prohibit_public_ip_on_vnic": False,
                "route_table_id": vcn.default_route_table_id,
                "security_list_ids": [vcn.default_security_list_id],
            }

            result = oci_utils.check_and_create_resource(
                resource_type="subnet",
                create_fn=create_subnet,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_subnets,
                kwargs_list={
                    "compartment_id": module.params["compartment_id"],
                    "vcn_id": module.params["vcn_id"],
                },
                module=module,
                model=CreateSubnetDetails(),
                exclude_attributes=exclude_attributes,
                default_attribute_values=default_attribute_values,
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
