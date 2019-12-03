#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
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
module: oci_public_ip_facts
short_description: Retrieve facts of public IPs
description:
    - This module retrieves information of the specified public IP or all public IPs in the specified compartment.
version_added: "2.5"
options:
    public_ip_id:
        description: OCID of the public IP. Use I(public_ip_id) to retrieve a specific public IP's information using its
                     OCID.
        required: false
        aliases: [ 'id' ]
    private_ip_id:
        description: OCID of the private IP that the public IP is assigned to. Use I(private_ip_id) to retrieve
                     information of a public IP assigned to it.
        required: false
    ip_address:
        description: The public IP address. Use I(ip_address) to get the public IP based on the public IP address.
        required: false
    scope:
        description: Whether the public IP is regional or specific to a particular Availability Domain. Reserved public
                     IPs have I(scope=REGION). Ephemeral public IPs have I(scope=AVAILABILITY_DOMAIN). I(scope) is
                     required to list all the public IPs in a compartment.
        required: false
        choices: ["REGION", "AVAILABILITY_DOMAIN"]
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to list all the public IPs in a
                     compartment.
        required: false
    availability_domain:
        description: The name of the Availability Domain. I(availability_domain) is required to list all the ephemeral
                     public IPs in the specified I(compartment_id) and I(availability_domain).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the reserved public IPs in a compartment
  oci_public_ip_facts:
    scope: REGION
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get all the ephemeral public IPs in a compartment and availability domain
  oci_public_ip_facts:
    scope: AVAILABILITY_DOMAIN
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    availability_domain: "BnQb:PHX-AD-1"

- name: Get a specific public IP using its OCID
  oci_public_ip_facts:
    public_ip_id: ocid1.publicip.oc1.iad.xxxxxEXAMPLExxxxx

- name: Get a specific public IP using the OCID of the private IP to which it is assigned
  oci_public_ip_facts:
    private_ip_id: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx

- name: Get a specific public IP using its public IP address
  oci_public_ip_facts:
    ip_address: 129.146.2.1
"""

RETURN = """
public_ips:
    description: List of public IP details
    returned: always
    type: complex
    contains:
        availability_domain:
            description: The public IP's Availability Domain. This property is set only for ephemeral public IPs
                         (that is, when the scope of the public IP is set to AVAILABILITY_DOMAIN). The value is the
                         Availability Domain of the assigned private IP.
            returned: always
            type: string
            sample: IwGV:US-ASHBURN-AD-1
        compartment_id:
            description: The OCID of the compartment containing the public IP. For an ephemeral public IP, this is the
                         same compartment as the private IP's. For a reserved public IP that is currently assigned, this
                         can be a different compartment than the assigned private IP's.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering
                         confidential information.
            returned: always
            type: string
            sample: ansible_public_ip
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: The public IP's Oracle ID (OCID).
            returned: always
            type: string
            sample: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx
        ip_address:
            description: The public IP address of the publicIp object.
            returned: always
            type: string
            sample: 129.146.2.1
        lifecycle_state:
            description: The public IP's current state.
            returned: always
            type: string
            sample: ASSIGNED
        lifetime:
            description: Defines when the public IP is deleted and released back to Oracle's public IP pool.
            returned: always
            type: string
            sample: EPHEMERAL
        private_ip_id:
            description: The OCID of the private IP that the public IP is currently assigned to, or in the process of
                         being assigned to.
            returned: always
            type: string
            sample: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx
        scope:
            description: Whether the public IP is regional or specific to a particular Availability Domain.
            returned: always
            type: string
            sample: REGION
        time_created:
            description: The date and time the private IP was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2018-06-22T15:25:25.569000+00:00
    sample: [{
            "availability_domain": null,
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible_public_ip",
            "id": "ocid1.publicip.oc1.iad.xxxxxEXAMPLExxxxx",
            "ip_address": "129.213.14.148",
            "lifecycle_state": "AVAILABLE",
            "lifetime": "RESERVED",
            "private_ip_id": null,
            "scope": "REGION",
            "time_created": "2018-06-22T15:25:25.569000+00:00"
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models.get_public_ip_by_private_ip_id_details import (
        GetPublicIpByPrivateIpIdDetails,
    )
    from oci.core.models.get_public_ip_by_ip_address_details import (
        GetPublicIpByIpAddressDetails,
    )
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            public_ip_id=dict(type="str", required=False, aliases=["id"]),
            private_ip_id=dict(type="str", required=False),
            ip_address=dict(type="str", required=False),
            scope=dict(
                type="str", required=False, choices=["REGION", "AVAILABILITY_DOMAIN"]
            ),
            compartment_id=dict(type="str", required=False),
            availability_domain=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    public_ip_id = module.params["public_ip_id"]

    try:
        if public_ip_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_public_ip, public_ip_id=public_ip_id
                    ).data
                )
            ]
        elif module.params["private_ip_id"] is not None:
            pvt_ip_id_details = GetPublicIpByPrivateIpIdDetails(
                private_ip_id=module.params["private_ip_id"]
            )
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_public_ip_by_private_ip_id,
                        get_public_ip_by_private_ip_id_details=pvt_ip_id_details,
                    ).data
                )
            ]
        elif module.params["ip_address"] is not None:
            ip_address_details = GetPublicIpByIpAddressDetails(
                ip_address=module.params["ip_address"]
            )
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_public_ip_by_ip_address,
                        get_public_ip_by_ip_address_details=ip_address_details,
                    ).data
                )
            ]
        elif module.params["scope"] is not None:
            list_args = {
                "scope": module.params["scope"],
                "compartment_id": module.params["compartment_id"],
                "display_name": module.params["display_name"],
            }
            if module.params["availability_domain"] is not None:
                list_args["availability_domain"] = module.params["availability_domain"]

            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_public_ips, **list_args
                )
            )
        else:
            module.fail_json(
                msg="Specify scope along with compartment_id to list all public IPs or one of"
                "public_ip_id/private_ip_id/ip_address."
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(public_ips=result)


if __name__ == "__main__":
    main()
