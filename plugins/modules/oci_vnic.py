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
module: oci_vnic
short_description: Update a VNIC
description:
    - This module allows the user to update a specified VNIC. To create a primary VNIC, use oci_instance. To create a
      secondary VNIC and attach it to an instance, use oci_vnic_attachment.
version_added: "2.5"
options:
  hostname_label:
        description: The hostname for the VNIC's primary private IP. Used for DNS. The value is the hostname portion of
                     the primary private IP's fully qualified domain name (FQDN) (for example, bminstance-1 in FQDN
                     bminstance-1.subnet123.vcn1.oraclevcn.com). Must be unique across all VNICs in the subnet and
                     comply with RFC 952 and RFC 1123.
        required: false
  name:
        description: A user-friendly name for the VNIC. Does not have to be unique, and it is changeable.
        required: false
        aliases: ['display_name']
  skip_source_dest_check:
        description: Determines whether the source/destination check is disabled on the VNIC. Defaults to false, which
                     means the check is performed.
        required: false
        default: false
        type: bool
  vnic_id:
        description: The OCID of the VNIC. Required when a VNIC needs to be updated.
        required: true
        aliases: ['id']
  state:
        description: The state of the VNIC that must be asserted to. When I(state=present), the VNIC is updated
        required: false
        default: "present"
        choices: ['present']

author: "Sivakumar Thyagarajan (@sivakumart)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Update the specified VNIC with a new name
  oci_vnic:
    id: "ocid1.vnicattachment.oc1.phx.xxxxxEXAMPLExxxxx....yicxjzgyhf47fq"
    name: sec-vnic1-to-instance1

- name: Update the specified VNIC with a new hostname_label
  oci_vnic:
    id: "ocid1.vnicattachment.oc1.phx.xxxxxEXAMPLExxxxx....yicxjzgyhf47fq"
    hostname_label: "newhostname"
"""

RETURN = """
vnic:
    description: Details of the VNIC attachment
    returned: On success
    type: dict
    sample: {
        "availability_domain": "BnQb:PHX-AD-1",
        "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx...lwbvm62xq",
        "display_name": "my_test_secondary_vnic_name_mod",
        "hostname_label": "ansible-test-45-1",
        "id": "ocid1.vnic.oc1.phx.xxxxxEXAMPLExxxxx...2beqa",
        "is_primary": false,
        "lifecycle_state": "AVAILABLE",
        "mac_address": "00:00:17:00:BC:6A",
        "private_ip": "10.0.0.11",
        "public_ip": null,
        "skip_source_dest_check": false,
        "subnet_id": "ocid1.subnet.oc1.phx.xxxxxEXAMPLExxxxx...smpqpaoa",
        "time_created": "2017-11-26T16:24:39.642000+00:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import UpdateVnicDetails
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def debug(s):
    get_logger().debug(s)


def set_logger(my_logger):
    global logger
    logger = my_logger


def get_logger():
    return logger


def main():
    my_logger = oci_utils.get_logger("oci_instance")
    set_logger(my_logger)

    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            name=dict(type="str", required=False, aliases=["display_name"]),
            vnic_id=dict(type="str", required=False, aliases=["id"]),
            hostname_label=dict(type="str", required=False),
            skip_source_dest_check=dict(type="bool", required=False, default=False),
            state=dict(
                type="str", required=False, default="present", choices=["present"]
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "present", ["id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtnetwork_client = oci_utils.create_service_client(module, VirtualNetworkClient)
    result = dict(changed=False)

    id = module.params["id"]
    debug("VNIC Id provided by user is " + str(id))

    try:
        vnic = oci_utils.call_with_backoff(virtnetwork_client.get_vnic, vnic_id=id).data
        if vnic is not None:
            name = module.params["name"]
            hostname_label = module.params["hostname_label"]
            skip_source_dest_check = module.params["skip_source_dest_check"]
            if not oci_utils.are_attrs_equal(vnic, module, vnic.attribute_map.keys()):
                debug("Need to update VNIC " + str(id))

                uvd = UpdateVnicDetails()
                uvd.skip_source_dest_check = skip_source_dest_check
                uvd.hostname_label = hostname_label
                uvd.display_name = name

                oci_utils.call_with_backoff(
                    virtnetwork_client.update_vnic, vnic_id=id, update_vnic_details=uvd
                )
                result["changed"] = True
        resp = oci_utils.call_with_backoff(virtnetwork_client.get_vnic, vnic_id=id)
        result["vnic"] = to_dict(resp.data)
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
