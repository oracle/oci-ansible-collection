#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
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
module: oci_private_ip_facts
short_description: Retrieve facts of private IPs
description:
    - This module retrieves information of a specified private IP or lists all the private IPs in a subnet.
version_added: "2.5"
options:
    private_ip_id:
        description: The OCID of the private IP. I(private_ip_id) is required to get a specific private IP's
                     information.
        required: false
        aliases: [ 'id' ]
    subnet_id:
        description: The OCID of the subnet. Required to list all the private IPs in a subnet.
        required: false
    ip_address:
        description: An IP address.
        required: false
    vnic_id:
        description: The OCID of the VNIC.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Get all the private IPs
  oci_private_ip_facts:
    subnet_id: ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx

- name: Get a specific private IP
  oci_private_ip_facts:
    private_ip_id: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx
"""

RETURN = """
private_ips:
    description: List of private IP details
    returned: always
    type: complex
    contains:
        availability_domain:
            description: The private IP's Availability Domain.
            returned: always
            type: string
            sample: IwGV:US-ASHBURN-AD-1
        compartment_id:
            description: The OCID of the compartment containing the private IP.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: A user-friendly name. Does not have to be unique, and it's changeable.
                         Avoid entering confidential information.
            returned: always
            type: string
            sample: ansible_private_ip
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        hostname_label:
            description: The hostname for the private IP. Used for DNS. The value is the hostname portion of the private
                         IP's fully qualified domain name (FQDN) (for example, bminstance-1 in FQDN
                         bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all VNICs in the subnet and
                         comply with RFC 952 and RFC 1123.
            returned: always
            type: string
            sample: webserver
        id:
            description: The private IP's Oracle ID (OCID).
            returned: always
            type: string
            sample: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx
        ip_address:
            description: The private IP address of the privateIp object. The address is within the CIDR of the VNIC's
                         subnet.
            returned: always
            type: string
            sample: 10.0.0.114
        is_primary:
            description: Whether this private IP is the primary one on the VNIC. Primary private IPs are unassigned and
                         deleted automatically when the VNIC is terminated.
            returned: always
            type: string
            sample: false
        subnet_id:
            description: The OCID of the subnet the VNIC is in.
            returned: always
            type: string
            sample: ocid1.subnet.oc1.iad.xxxxxEXAMPLExxxxx
        time_created:
            description: The date and time the private IP was created, in the format defined by RFC3339.
            returned: always
            type: string
            sample: 2018-03-28T18:37:56.190000+00:00
        vnic_id:
            description: The OCID of the VNIC the private IP is assigned to. The VNIC and private IP must be in the same
                         subnet.
            returned: always
            type: string
            sample: ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx
    sample: [{
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
        }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            private_ip_id=dict(type="str", required=False, aliases=["id"]),
            subnet_id=dict(type="str", required=False),
            ip_address=dict(type="str", required=False),
            vnic_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    private_ip_id = module.params["private_ip_id"]

    try:
        if private_ip_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        virtual_network_client.get_private_ip,
                        private_ip_id=private_ip_id,
                    ).data
                )
            ]
        else:
            optional_list_method_params = ["ip_address", "subnet_id", "vnic_id"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    virtual_network_client.list_private_ips, **optional_kwargs
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(private_ips=result)


if __name__ == "__main__":
    main()
