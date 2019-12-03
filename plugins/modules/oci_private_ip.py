#!/usr/bin/python
# Copyright (c) 2017, 2018, Oracle and/or its affiliates.
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
module: oci_private_ip
short_description: Manage private IPs in OCI
description:
    - This module allows the user to create, delete and update private IPs in OCI.
version_added: "2.5"
options:
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information.
        required: false
        aliases: [ 'name' ]
    hostname_label:
        description: The hostname for the private IP. Used for DNS. The value is the hostname portion of the private
                     IP's fully qualified domain name (FQDN) (for example, bminstance-1 in FQDN
                     bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all VNICs in the subnet and
                     comply with RFC 952 and RFC 1123.
        required: false
    ip_address:
        description: A private IP address of your choice. Must be an available IP address within the subnet's CIDR. If
                     you don't specify a value, Oracle automatically assigns a private IP address from the subnet.
        required: false
    private_ip_id:
        description: The OCID of the private IP. Required to update a private IP using I(state=present) or delete a
                     private IP using I(state=absent).
        required: false
        aliases: [ 'id' ]
    state:
        description: Create or update a private IP with I(state=present). Use I(state=absent) to delete a private IP.
        required: false
        default: present
        choices: ['present', 'absent']
    vnic_id:
        description: The OCID of the VNIC to assign the private IP to. The VNIC and private IP must be in the same
                     subnet. Required when creating a private IP using I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_tags ]
"""

EXAMPLES = """
- name: Create a private IP
  oci_private_ip:
    display_name: 'ansible_private_ip'
    hostname_label: 'web'
    ip_address: '10.0.0.114'
    vnic_id: 'ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx'

- name: Update a private IP
  oci_private_ip:
    private_ip_id: 'ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx'
    hostname_label: 'db'

- name: Delete a private IP
  oci_private_ip:
    private_ip_id: 'ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx'
    state: absent
"""

RETURN = """
private_ip:
    description: Information about the private IP
    returned: On successful create, delete & update operation
    type: dict
    sample: {
            "availability_domain": "IwGV:US-ASHBURN-AD-1",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_private_ip",
            "freeform_tags": {},
            "hostname_label": "db",
            "id": "ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx",
            "ip_address": "10.0.0.114",
            "is_primary": false,
            "subnet_id": "ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx",
            "time_created": "2018-03-28T18:37:56.190000+00:00",
            "vnic_id": "ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx"
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreatePrivateIpDetails
    from oci.core.models import UpdatePrivateIpDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_private_ip(virtual_network_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="private_ip",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_private_ip,
        kwargs_get={"private_ip_id": module.params["private_ip_id"]},
        delete_fn=virtual_network_client.delete_private_ip,
        kwargs_delete={"private_ip_id": module.params["private_ip_id"]},
        module=module,
        wait_applicable=False,
    )
    return result


def update_private_ip(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="private_ip",
        get_fn=virtual_network_client.get_private_ip,
        kwargs_get={"private_ip_id": module.params["private_ip_id"]},
        update_fn=virtual_network_client.update_private_ip,
        primitive_params_update=["private_ip_id"],
        kwargs_non_primitive_update={
            UpdatePrivateIpDetails: "update_private_ip_details"
        },
        module=module,
        wait_applicable=False,
        update_attributes=UpdatePrivateIpDetails().attribute_map.keys(),
    )

    return result


def create_private_ip(virtual_network_client, module):
    create_private_ip_details = CreatePrivateIpDetails()
    for attribute in create_private_ip_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_private_ip_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(
        resource_type="private_ip",
        create_fn=virtual_network_client.create_private_ip,
        kwargs_create={"create_private_ip_details": create_private_ip_details},
        client=virtual_network_client,
        get_fn=virtual_network_client.get_private_ip,
        get_param="private_ip_id",
        module=module,
        wait_applicable=False,
    )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec()
    module_args.update(
        dict(
            hostname_label=dict(type="str", required=False),
            ip_address=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            vnic_id=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            private_ip_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["private_ip_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    state = module.params["state"]
    private_ip_id = module.params["private_ip_id"]

    if state == "absent":
        result = delete_private_ip(virtual_network_client, module)

    else:
        if private_ip_id is not None:
            result = update_private_ip(virtual_network_client, module)
        else:
            # Exclude ip_address & display_name when matching private_ips if they are not explicitly specified by user.
            exclude_attributes = {"display_name": True, "ip_address": True}
            subnet_id = oci_utils.call_with_backoff(
                virtual_network_client.get_vnic, vnic_id=module.params["vnic_id"]
            ).data.subnet_id
            result = oci_utils.check_and_create_resource(
                resource_type="private_ip",
                create_fn=create_private_ip,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_private_ips,
                kwargs_list={
                    "vnic_id": module.params["vnic_id"],
                    "subnet_id": subnet_id,
                },
                module=module,
                model=CreatePrivateIpDetails(),
                exclude_attributes=exclude_attributes,
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
