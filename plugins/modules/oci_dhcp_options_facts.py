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
module: oci_dhcp_options_facts
short_description: Fetches details of a specific Dhcp Options or a list of Dhcp Optionss in the specified VCN and
                   compartment
description:
    - Fetches details of a specific Dhcp Options or a list of Dhcp Optionss in the specified VCN and compartment.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment details about
                     whose Dhcp Options must be retrived
        required: false
    vcn_id:
        description: Identifier of the Virtual Cloud Network to which the
                     Dhcp Options is attached.
        required: false
    dhcp_id:
        description: Identifier of the Dhcp Options. Required if the detailsof a
                     specific Dhcp Options details needs to be fetched. Mutually
                     exclusive with compartment_id and vcn_id.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
# Fetch details of all Dhcp Optionss in the specified compartment and VCN
- name: List Dhcp Options
  oci_dhcp_options:
      compartment_id: 'ocid1.compartment..xcds'
      vcn_id: 'ocid1.vcn..dfxs'

#Fetch specific Dhcp Options
- name: List a specific Dhcp Options
  oci_dhcp_options::
      dhcp_id: 'ocid1.dhcpoptions..xcds'
"""

RETURN = """
    dhcp_options_list:
        description: Attributes of the fetched Dhcp Options(s).
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Dhcp Options
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Dhcp Options during creation
                returned: always
                type: string
                sample: ansible_dhcp_options
            id:
                description: Identifier of the Dhcp Options
                returned: always
                type: string
                sample: ocid1.dhcpoptions.oc1.axdf
            vcn_id:
                description: Identifier of the Virtual Cloud Network to which the
                             Dhcp Options is attached.
                returned: always
                type: string
                sample: ocid1.vcn..ixcd
            lifecycle_state:
                description: The current state of the Dhcp Options
                returned: always
                type: string
                sample: AVAILABLE
            options:
                description: A list of dhcp options.
                returned: always
                type: list
                sample: [{"custom_dns_servers": [],"server_type": "CustomDnsServer","type": "DomainNameServer"},
                        {"search_domain_names": ["myansiblevcn.oraclevcn.com"],"type": "SearchDomain"}]
            time_created:
                description: Date and time when the Dhcp Options was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
        sample: [
            {
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "freeform_tags":{"region":"east"},
                    "defined_tags":{"features":{"capacity":"medium"}},
                    "display_name":"ansible_dhcp_options",
                    "id":"ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"AVAILABLE",
                    "options":[
                                {
                                    "custom_dns_servers":[],
                                    "server_type":"VcnLocalPlusInternet",
                                    "type":"DomainNameServer"
                                },
                                {
                                    "search_domain_names":["ansibletestvcn.oraclevcn.com"],
                                    "type":"SearchDomain"
                                },
                                {
                                    "custom_dns_servers":["10.0.0.8"],
                                    "server_type":"CustomDnsServer",
                                    "type":"DomainNameServer"
                                }
                            ],
                    "time_created":"2017-11-26T16:41:06.996000+00:00",
                    "vcn_id":"ocid1.vcn.oc1.phx.xxxxxEXAMPLExxxxx"
                },
            {
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "freeform_tags":{"region":"west"},
                    "defined_tags":{"features":{"capacity":"large"}},
                    "display_name":"ansible_dhcp_options_two",
                    "id":"ocid1.dhcpoptions.oc1.phx.xxxxxEXAMPLExxxxx",
                    "lifecycle_state":"AVAILABLE",
                    "options":[
                                {
                                    "custom_dns_servers":[],
                                    "server_type":"VcnLocalPlusInternet",
                                    "type":"DomainNameServer"
                                },
                                {
                                    "search_domain_names":["vcn.oraclevcn.com"],
                                    "type":"SearchDomain"
                                },
                                {
                                    "custom_dns_servers":["10.0.0.8","10.0.0.12","10.0.0.14"],
                                    "server_type":"CustomDnsServer",
                                    "type":"DomainNameServer"
                                }
                            ],
                    "time_created":"2017-10-26T16:41:06.996000+00:00",
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


def list_dhcp_options(virtual_network_client, module):
    result = dict()
    compartment_id = module.params.get("compartment_id")
    vcn_id = module.params.get("vcn_id")
    dhcp_id = module.params.get("dhcp_id")
    try:
        if compartment_id and vcn_id:
            existing_dhcp_options = oci_utils.list_all_resources(
                virtual_network_client.list_dhcp_options,
                compartment_id=compartment_id,
                vcn_id=vcn_id,
                display_name=module.params["display_name"],
            )
        elif dhcp_id:
            response = oci_utils.call_with_backoff(
                virtual_network_client.get_dhcp_options, dhcp_id=dhcp_id
            )
            existing_dhcp_options = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["dhcp_options_list"] = to_dict(existing_dhcp_options)
    return result


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            vcn_id=dict(type="str", required=False),
            dhcp_id=dict(type="str", required=False, aliases=["id"]),
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

    result = list_dhcp_options(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
