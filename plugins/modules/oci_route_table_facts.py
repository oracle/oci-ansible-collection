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
module: oci_route_table_facts
short_description: Fetches details of a specific Route Table or a
                   list of Route tables in the specified VCN and
                   compartment
description:
    - Fetches details of a specific Route Table or a list of Route tables in the specified VCN and compartment.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment details about
                     whose Route Table must be retrived
        required: false
    vcn_id:
        description: Identifier of the Virtual Cloud Network to which the
                     Route Table is attached.
        required: false
    rt_id:
        description: Identifier of the Route Table. Required if the detailsof a
                     specific Route Table details needs to be fetched. Mutually
                     exclusive with compartment_id and vcn_id.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
# Fetch details of all route tables in the specified compartment and VCN
- name: List Route Table
  oci_route_table_facts:
      compartment_id: 'ocid1.compartment..xcds'
      vcn_id: 'ocid1.vcn..dfxs'

#Fetch specific Route Table
- name: List a specific Route Table
  oci_route_table_facts::
      id: 'ocid1.routetable..xcds'
"""

RETURN = """
    route_tables:
        description: Attributes of the fetched Route Table(s).
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Route Table
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Route Table during creation
                returned: always
                type: string
                sample: ansible_route_table
            id:
                description: Identifier of the Route Table
                returned: always
                type: string
                sample: ocid1.routetable.oc1.axdf
            vcn_id:
                description: Identifier of the Virtual Cloud Network to which the
                             Route Table is attached.
                returned: always
                type: string
                sample: ocid1.vcn..ixcd
            lifecycle_state:
                description: The current state of the Route Table
                returned: always
                type: string
                sample: AVAILABLE
            route_rules:
                description: The collection of rules for routing destination IPs to network devices.
                returned: always
                type: string
                sample: [{'cidr_block': '0.0.0.0/0', 'destination': '0.0.0.0', 'destination_type': 'CIDR_BLOCK',
                    'network_entity_id': 'ocid1.internetgateway.aaa'}]
            time_created:
                description: Date and time when the Route Table was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
        sample: [
            {
                "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                "freeform_tags":{"region":"west"},
                "defined_tags":{"features":{"capacity":"large"}},
                "display_name":"ansible_route_table_two",
                "id":"ocid1.routetable.oc1.phx.xxxxxEXAMPLExxxxx",
                "lifecycle_state":"AVAILABLE",
                "route_rules":[
                                {
                                    "cidr_block":"0.0.0.0/0",
                                    "network_entity_id":"ocid1.internetgateway.xxxxxEXAMPLExxxxx"
                                },
                                {
                                    "cidr_block": null,
                                    "destination": "oci-phx-objectstorage",
                                    "destination_type": "SERVICE_CIDR_BLOCK",
                                    "network_entity_id":"ocid1.servicegateway.oc1.phx.xxxxxEXAMPLExxxxx"
                                }
                            ],
                "time_created":"2017-11-17T17:39:41.522000+00:00",
                "vcn_id":"ocid1.vcn.aaa"
            },
            {
                "compartment_id":"ocid1.compartment.aaaa",
                "freeform_tags":{"region":"east"},
                "defined_tags":{"features":{"capacity":"medium"}},
                "display_name":"updated_ansible_route_table",
                "id":"ocid1.routetable.aaaa",
                "lifecycle_state":"AVAILABLE",
                "route_rules":[
                                {
                                    "cidr_block":"0.0.0.0/0",
                                    "network_entity_id":"ocid1.internetgateway.xxxxxEXAMPLExxxxx"
                                }
                            ],
                "time_created":"2017-11-17T17:39:33.190000+00:00",
                "vcn_id":"ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
            }
        ]

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


def list_route_tables(virtual_network_client, module):
    result = dict(route_tables="")
    compartment_id = module.params.get("compartment_id")
    vcn_id = module.params.get("vcn_id")
    rt_id = module.params.get("rt_id")
    try:
        if compartment_id and vcn_id:
            existing_route_tables = oci_utils.list_all_resources(
                virtual_network_client.list_route_tables,
                compartment_id=compartment_id,
                vcn_id=vcn_id,
                display_name=module.params["display_name"],
            )
        elif rt_id:
            response = oci_utils.call_with_backoff(
                virtual_network_client.get_route_table, rt_id=rt_id
            )
            existing_route_tables = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["route_tables"] = to_dict(existing_route_tables)
    return result


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            vcn_id=dict(type="str", required=False),
            rt_id=dict(type="str", required=False, aliases=["id"]),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "rt_id"], ["vcn_id", "rt_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )
    result = list_route_tables(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
