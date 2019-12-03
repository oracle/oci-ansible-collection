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
module: oci_ip_sec_connection
short_description: Manage IPSec connections in OCI
description:
    - This module allows the user to create, delete and update IPSec connections in OCI.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment to contain the IPSec connection. Required when creating an IPSec
                     connection with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable.
        required: false
        aliases: [ 'name' ]
    state:
        description: Create or update an IPSec connection with I(state=present). Use I(state=absent) to delete an IPSec
                     connection.
        required: false
        default: present
        choices: ['present', 'absent']
    cpe_id:
        description: The OCID of the CPE. Required to create an IPSec connection.
        required: false
        aliases: [ 'id' ]
    drg_id:
        description: The OCID of the DRG. Required to create an IPSec connection.
        required: false
    ipsc_id:
        description: The OCID of the IPSec connection. Required to update or delete an IPSec connection.
        required: false
        aliases: [ 'id' ]
    static_routes:
        description: Static routes to the CPE. At least one route must be included. The CIDR must not be a multicast
                     address or class E address. Required to create an IPSec connection.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create an IPSec connection
  oci_ip_sec_connection:
    compartment_id: 'ocid1.compartment.oc1..xxxxxEXAMPLExxxxx'
    display_name: my_connection
    cpe_id: ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx
    drg_id: ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx
    static_routes:
        - 10.0.1.0/24

- name: Update IPSec connection's display name
  oci_ip_sec_connection:
    id: ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx
    display_name: ansible_ipsec_connection

- name: Delete IPSec connection
  oci_ip_sec_connection:
    id: ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
ip_sec_connection:
    description: Information about the IPSec connection
    returned: On successful operation
    type: dict
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "cpe_id": "ocid1.cpe.oc1.phx.xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_ip_sec_connection",
            "drg_id": "ocid1.drg.oc1.phx.xxxxxEXAMPLExxxxx",
            "freeform_tags": {},
            "id": "ocid1.ipsecconnection.oc1.phx.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "static_routes": ["10.0.1.0/24"],
            "time_created": "2017-11-13T20:22:40.626000+00:00"
            }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.virtual_network_client import VirtualNetworkClient
    from oci.core.models import CreateIPSecConnectionDetails
    from oci.core.models import UpdateIPSecConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_ip_sec_connection(virtual_network_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="ip_sec_connection",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_ip_sec_connection,
        kwargs_get={"ipsc_id": module.params["ipsc_id"]},
        delete_fn=virtual_network_client.delete_ip_sec_connection,
        kwargs_delete={"ipsc_id": module.params["ipsc_id"]},
        module=module,
    )
    return result


def update_ip_sec_connection(virtual_network_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="ip_sec_connection",
        client=virtual_network_client,
        get_fn=virtual_network_client.get_ip_sec_connection,
        kwargs_get={"ipsc_id": module.params["ipsc_id"]},
        update_fn=virtual_network_client.update_ip_sec_connection,
        primitive_params_update=["ipsc_id"],
        kwargs_non_primitive_update={
            UpdateIPSecConnectionDetails: "update_ip_sec_connection_details"
        },
        module=module,
        update_attributes=UpdateIPSecConnectionDetails().attribute_map.keys(),
    )
    return result


def create_ip_sec_connection(virtual_network_client, module):
    create_ip_sec_connection_details = CreateIPSecConnectionDetails()
    for attribute in create_ip_sec_connection_details.attribute_map.keys():
        if attribute in module.params:
            setattr(
                create_ip_sec_connection_details, attribute, module.params[attribute]
            )

    result = oci_utils.create_and_wait(
        resource_type="ip_sec_connection",
        create_fn=virtual_network_client.create_ip_sec_connection,
        kwargs_create={
            "create_ip_sec_connection_details": create_ip_sec_connection_details
        },
        client=virtual_network_client,
        get_fn=virtual_network_client.get_ip_sec_connection,
        get_param="ipsc_id",
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
            display_name=dict(type="str", required=False, aliases=["name"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            ipsc_id=dict(type="str", required=False, aliases=["id"]),
            cpe_id=dict(type="str", required=False),
            drg_id=dict(type="str", required=False),
            static_routes=dict(type="list", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["ipsc_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    exclude_attributes = {"display_name": True}
    state = module.params["state"]

    if state == "absent":
        result = delete_ip_sec_connection(virtual_network_client, module)

    else:
        ip_sec_connection_id = module.params["ipsc_id"]
        if ip_sec_connection_id is not None:
            result = update_ip_sec_connection(virtual_network_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="ip_sec_connection",
                create_fn=create_ip_sec_connection,
                kwargs_create={
                    "virtual_network_client": virtual_network_client,
                    "module": module,
                },
                list_fn=virtual_network_client.list_ip_sec_connections,
                kwargs_list={
                    "compartment_id": module.params["compartment_id"],
                    "drg_id": module.params["drg_id"],
                    "cpe_id": module.params["cpe_id"],
                },
                module=module,
                model=CreateIPSecConnectionDetails(),
                exclude_attributes=exclude_attributes,
            )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
