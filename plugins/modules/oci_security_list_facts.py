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
module: oci_security_list_facts
short_description: Fetches details of a specific Security List or a
                   list of Security Lists in the specified VCN and
                   compartment
description:
    - Fetches details of a specific Security List or a list of Security Lists in the specified VCN and compartment.oc
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment details about
                     whose Security List must be retrieved
        required: false
    vcn_id:
        description: Identifier of the Virtual Cloud Network to which the
                     Security List is attached.
        required: false
    security_list_id:
        description: Identifier of the Security List. Required if the details of a
                     specific Security List details needs to be fetched. Mutually
                     exclusive with compartment_id and vcn_id.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Get information about all Security List
- name: Get information about all security list within a vcn and compartment
  oci_security_list_facts:
    compartment_id: 'ocid.compartment..xxxxxEXAMPLExxxxx'
    vcn_id: 'ocid.vcn..xxxxxEXAMPLExxxxx'

# Get information about a specific Security List
- name: Get information about security list by id
  oci_security_list_facts:
    id: 'ocid1.securitylist.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    security_lists:
        description: Attributes of the fetched Security List(s).
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Security List
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Security List during creation
                returned: always
                type: string
                sample: ansible_security_list
            id:
                description: Identifier of the Security List
                returned: always
                type: string
                sample: ocid1.securitylist.oc1.axdf
            vcn_id:
                description: Identifier of the Virtual Cloud Network to which the
                             Security List is attached.
                returned: always
                type: string
                sample: ocid1.vcn..ixcd
            lifecycle_state:
                description: The current state of the Security List
                returned: always
                type: string
                sample: AVAILABLE
            ingress_security_rules:
                description: Rules for allowing ingress IP packets
                returned: always
                type: list
                sample: [{"icmp-options": null,"is-stateless": null,"protocol": "6",
                "source": "0.0.0.0/0","tcp-options": {"destination-port-range":
                {"max": 22,"min": 22},"source-port-range": null},"udp-options": null}]
            egress_security_rules:
                description: Rules for allowing egress IP packets
                returned: always
                type: list
                sample:   [{"destination": "0.0.0.0/0","icmp-options": null,
                "is-stateless": null,"protocol": "all","tcp-options": null,
                "udp-options": null}]
            time_created:
                description: Date and time when the Security List was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
        sample: [{
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "freeform_tags":{"region":"east"},
                    "defined_tags":{"features":{"capacity":"medium"}},
                    "display_name":"ansible_security_list_one",
                    "egress_security_rules":[
                                                {
                                                    "destination":"0.0.0.0/0",
                                                    "destination_type":"CIDR_BLOCK",
                                                    "icmp_options":null,
                                                    "is_stateless":null,
                                                    "protocol":"all",
                                                    "tcp_options":null,
                                                    "udp_options":null
                                                  }
                                                ],
                    "id":"ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx",
                    "ingress_security_rules":[
                                                {
                                                    "icmp_options":null,
                                                    "is_stateless":false,
                                                    "protocol":"6",
                                                    "source":"0.0.0.0/0",
                                                    "source_type":"CIDR_BLOCK",
                                                    "tcp_options":{
                                                        "destination_port_range":{
                                                                                "max":22,
                                                                                "min":22
                                                                                },
                                                        "source_port_range":null
                                                    },
                                                    "udp_options":null
                                                },
                                                {
                                                    "icmp_options":{
                                                        "code":4,
                                                        "type":3
                                                    },
                                                    "is_stateless":false,
                                                    "protocol":"1",
                                                    "source":"0.0.0.0/0",
                                                    "source_type":"CIDR_BLOCK",
                                                    "tcp_options":null,
                                                    "udp_options":null
                                                },
                                                {
                                                    "icmp_options":{
                                                        "code":null,
                                                        "type":3
                                                    },
                                                    "is_stateless":false,
                                                    "protocol":"1",
                                                    "source":"oci-iad-objectstorage",
                                                    "source_type":"SERVICE_CIDR_BLOCK",
                                                    "tcp_options":null,
                                                    "udp_options":null
                                                }
                                            ],
                    "lifecycle_state":"AVAILABLE",
                    "time_created":"2017-11-24T05:33:44.779000+00:00",
                    "vcn_id":"ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
                },
                {
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "freeform_tags":{"region":"west"},
                    "defined_tags":{"features":{"capacity":"large"}},
                    "display_name":"ansible_security_list_two",
                    "egress_security_rules":[
                                                {
                                                    "destination":"10.0.0.0/8",
                                                    "destination_type":"CIDR_BLOCK",
                                                    "icmp_options":null,
                                                    "is_stateless":true,
                                                    "protocol":"all",
                                                    "tcp_options":null,
                                                    "udp_options":null
                                                  }
                                                ],
                    "id":"ocid1.securitylist.oc1.phx.xxxxxEXAMPLExxxxx",
                    "ingress_security_rules":[
                                                {
                                                    "icmp_options":null,
                                                    "is_stateless":false,
                                                    "protocol":"6",
                                                    "source":"0.0.0.0/0",
                                                    "source_type":"CIDR_BLOCK",
                                                    "tcp_options":{
                                                        "destination_port_range":{
                                                                                "max":45,
                                                                                "min":50
                                                                                },
                                                        "source_port_range":null
                                                    },
                                                    "udp_options":null
                                                },
                                                {
                                                    "icmp_options":{
                                                        "code":4,
                                                        "type":3
                                                    },
                                                    "is_stateless":false,
                                                    "protocol":"1",
                                                    "source":"0.0.0.0/0",
                                                    "source_type":"CIDR_BLOCK",
                                                    "tcp_options":null,
                                                    "udp_options":null
                                                }
                                            ],
                    "lifecycle_state":"AVAILABLE",
                    "time_created":"2017-11-24T05:33:44.779000+00:00",
                    "vcn_id":"ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
                }]
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


def list_security_lists(virtual_network_client, module):
    result = dict(security_lists="")
    compartment_id = module.params.get("compartment_id")
    vcn_id = module.params.get("vcn_id")
    security_list_id = module.params.get("security_list_id")
    try:
        if compartment_id and vcn_id:
            existing_security_lists = oci_utils.list_all_resources(
                virtual_network_client.list_security_lists,
                compartment_id=compartment_id,
                vcn_id=vcn_id,
                display_name=module.params["display_name"],
            )
        elif security_list_id:
            response = oci_utils.call_with_backoff(
                virtual_network_client.get_security_list,
                security_list_id=security_list_id,
            )
            existing_security_lists = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["security_lists"] = to_dict(existing_security_lists)
    return result


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            vcn_id=dict(type="str", required=False),
            security_list_id=dict(type="str", required=False, aliases=["id"]),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "id"], ["vcn_id", "id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_security_lists(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
