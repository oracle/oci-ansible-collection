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
module: oci_public_ip
short_description: Manage public IPs in OCI
description:
    - This module allows the user to create, delete and update public IPs in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment to contain the public IP. For ephemeral public IPs, you must set this
                     to the private IP's compartment OCID. Required to create a public IP.
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information.
        required: false
        aliases: [ 'name' ]
    private_ip_id:
        description: The OCID of the private IP to assign the public IP to. Required for an ephemeral public IP because
                     it must always be assigned to a private IP (specifically a primary private IP). Optional for a
                     reserved public IP. If you don't provide it, the public IP is created but not assigned to a private
                     IP.
        required: false
    public_ip_id:
        description: The OCID of the public IP. Required to delete or update a public IP.
        required: false
        aliases: [ 'id' ]
    lifetime:
        description: Defines when the public IP is deleted and released back to the Oracle Cloud Infrastructure public
                     IP pool. Required to create a public IP.
        required: false
        choices: ['EPHEMERAL', 'RESERVED']
    state:
        description: Create or update a public IP with I(state=present). Use I(state=absent) to delete a public IP.
        required: false
        default: present
        choices: ['present', 'absent']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_tags, oracle_wait_options  ]
"""

EXAMPLES = """
- name: Create a public IP with lifetime as RESERVED
  oci_public_ip:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    display_name: ansible_public_ip
    lifetime: RESERVED

- name: Create a public IP with lifetime as EPHEMERAL
  oci_public_ip:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    display_name: ansible_public_ip
    lifetime: EPHEMERAL
    private_ip_id: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx

- name: Assign a reserved public IP to a private IP
  oci_public_ip:
    id: ocid1.publicip.oc1.iad.xxxxxEXAMPLExxxxx
    private_ip_id: ocid1.privateip.oc1.iad.xxxxxEXAMPLExxxxx

- name: Unassign a reserved public IP from a private IP by passing an empty string
  oci_public_ip:
    id: ocid1.publicip.oc1.iad.xxxxxEXAMPLExxxxx
    private_ip_id: ""

- name: Delete a public IP
  oci_public_ip:
    id: ocid1.publicip.oc1.iad.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
public_ip:
    description: Information about the public IP
    returned: On successful create, delete & update operation
    type: dict
    sample: {
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
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci import wait_until
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreatePublicIpDetails
    from oci.core.models import UpdatePublicIpDetails
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_public_ip(virtual_network_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="public_ip",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_public_ip,
        kwargs_get={"public_ip_id": module.params["public_ip_id"]},
        delete_fn=virtual_network_client.delete_public_ip,
        kwargs_delete={"public_ip_id": module.params["public_ip_id"]},
        module=module,
    )
    return result


def update_public_ip(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="public_ip",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_public_ip,
        kwargs_get={"public_ip_id": module.params["public_ip_id"]},
        update_fn=virtual_network_client.update_public_ip,
        primitive_params_update=["public_ip_id"],
        kwargs_non_primitive_update={UpdatePublicIpDetails: "update_public_ip_details"},
        module=module,
        update_attributes=UpdatePublicIpDetails().attribute_map.keys(),
    )
    # Since assigning, moving, and unassigning a reserved public IP are asynchronous operation, wait for the operation
    # to complete based on module invocation paramters.
    if result["changed"]:
        if module.params.get("wait", None):
            response_get = oci_utils.call_with_backoff(
                virtual_network_client.get_public_ip,
                public_ip_id=module.params["public_ip_id"],
            )
            # After the update operation, the public IP can have "ASSIGNED" or "AVAILABLE" steady lifecycle state.
            states = module.params.get("wait_until") or ["ASSIGNED", "AVAILABLE"]
            result["public_ip"] = to_dict(
                wait_until(
                    virtual_network_client,
                    response_get,
                    evaluate_response=lambda r: r.data.lifecycle_state in states,
                    max_wait_seconds=module.params.get("wait_timeout", 1200),
                ).data
            )
    return result


def create_public_ip(virtual_network_client, module):
    create_public_ip_details = CreatePublicIpDetails()
    for attribute in create_public_ip_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_public_ip_details, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(
        resource_type="public_ip",
        create_fn=virtual_network_client.create_public_ip,
        kwargs_create={"create_public_ip_details": create_public_ip_details},
        client=virtual_network_client,
        get_fn=virtual_network_client.get_public_ip,
        get_param="public_ip_id",
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            lifetime=dict(
                type="str", required=False, choices=["EPHEMERAL", "RESERVED"]
            ),
            display_name=dict(type="str", required=False, aliases=["name"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            private_ip_id=dict(type="str", required=False),
            public_ip_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[
            ("state", "absent", ["public_ip_id"]),
            ("lifetime", "EPHEMERAL", ["private_ip_id"]),
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    state = module.params["state"]
    public_ip_id = module.params["public_ip_id"]

    if state == "absent":
        result = delete_public_ip(virtual_network_client, module)

    else:
        if public_ip_id is not None:
            result = update_public_ip(virtual_network_client, module)
        else:
            exclude_attributes = {"display_name": True}
            # If the user desired lifetime of the public IP to be created is RESERVED, then use SCOPE as REGION for
            # making a call to list all the public IPs else use SCOPE as AVAILABILITY_DOMAIN.
            if module.params["lifetime"] == "RESERVED":
                kwargs_list = {
                    "scope": "REGION",
                    "compartment_id": module.params["compartment_id"],
                }
            else:
                # To list ephemeral public IPs, availability domain parameter is required. An ephemeral public IP is
                # always in the same Availability Domain as the private IP it's assigned to. Get the AD from private_ip.
                pvt_ip_ad = virtual_network_client.get_private_ip(
                    module.params["private_ip_id"]
                ).data.availability_domain
                kwargs_list = {
                    "scope": "AVAILABILITY_DOMAIN",
                    "compartment_id": module.params["compartment_id"],
                    "availability_domain": pvt_ip_ad,
                }
            result = oci_utils.check_and_create_resource(
                resource_type="public_ip",
                create_fn=create_public_ip,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_public_ips,
                kwargs_list=kwargs_list,
                module=module,
                model=CreatePublicIpDetails(),
                exclude_attributes=exclude_attributes,
            )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
