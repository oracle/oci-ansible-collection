#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019 Oracle and/or its affiliates.
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
module: oci_vnic_facts
short_description: Retrieve details about a specific VNIC
description:
    - This module retrieves details about a specific VNIC.
version_added: "2.5"
options:
    vnic_id:
        description: The OCID of the VNIC. Required for retrieving information about a specific VNIC.
        required: false
        aliases: ['id']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get details of a specific VNIC
  oci_vnic_facts:
    id: 'ocid1.vnic.oc1..xxxxxEXAMPLExxxxx...vm62xq'
"""

RETURN = """
vnic:
    description: Information about a specific VNIC
    returned: on success
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain of the VNIC
            returned: always
            type: string
            sample: Uocm:PHX-AD-1
        compartment_id:
            description: The OCID of the compartment containing the VNIC
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...vm62xq'
        display_name:
            description: A user-friendly name for the image. It does not have to be unique, and it's changeable.
            returned: always
            type: string
            sample: my-vnic1
        id:
            description: The OCID of the VNIC
            returned: always
            type: string
            sample: ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...asdadv3qca
        hostname_label:
            description: The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion
                         of the primary private IP's fully qualified domain name (FQDN) (for example, bminstance-1 in
                         FQDN bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all VNICs in the subnet
                         and comply with RFC 952 and RFC 1123.
            returned: always
            type: string
            sample: my-host-1
        is_primary:
            description: Whether the VNIC is the primary VNIC
            returned: always
            type: boolean
            sample: true
        lifecycle_state:
            description: The current state of the VNIC.
            returned: always
            type: string
            sample: AVAILABLE
        mac_address:
            description: The MAC address of the VNIC.
            returned: always
            type: string
            sample: 00:00:17:B6:4D:DD
        private_ip:
            description: The private IP address of the primary privateIp object on the VNIC. The address is within the
                         CIDR of the VNIC's subnet.
            returned: always
            type: string
            sample: 10.0.3.3
        public_ip:
            description: The public IP address of the VNIC, if one is assigned.
            returned: always
            type: string
            sample: 10.1.2.3
        skip_source_dest_check:
            description: Whether the source/destination check is disabled on the VNIC. Defaults to false, which means
                         the check is performed.
            returned: always
            type: string
            sample: true
        subnet_id:
            description: The OCID of the subnet the VNIC is in.
            returned: always
            type: string
            sample: ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...pbf7yux45iddusmpqpaoa
        time_created:
            description: The date and time the image was created, in the format defined by RFC3339
            returned: always
            type: string
            sample: 2017-11-20T04:52:54.541000+00:00
    sample: [{"availability_domain": "BnQb:PHX-AD-1",
              "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...lwbvm62xq",
              "display_name": "my-vnic-1",
              "hostname_label": "myhostname-1",
              "id": "ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...u7ybd56p6a",
              "is_primary": true,
              "lifecycle_state": "AVAILABLE",
              "mac_address": "00:00:17:00:6C:A2",
              "private_ip": "10.0.0.10",
              "public_ip": null,
              "skip_source_dest_check": false,
              "subnet_id": "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...dusmpqpaoa",
              "time_created": "2017-11-26T16:23:29.932000+00:00"
              }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(dict(vnic_id=dict(type="str", required=False, aliases=["id"])))

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[("id", "compartment_id")],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtnw_client = oci_utils.create_service_client(module, VirtualNetworkClient)

    id = module.params["vnic_id"]

    result = dict()
    try:
        inst = oci_utils.call_with_backoff(virtnw_client.get_vnic, vnic_id=id).data
        result = to_dict(inst)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as mwte:
        module.fail_json(msg=str(mwte))

    module.exit_json(vnic=result)


if __name__ == "__main__":
    main()
