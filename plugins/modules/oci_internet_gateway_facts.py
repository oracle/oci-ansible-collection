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
module: oci_internet_gateway_facts
short_description: Fetches details of the OCI Internet Gateway under a Virtual
                   Cloud Network
description:
    - Fetches details of the OCI Internet Gateway under a Virtual Cloud Network.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment in which this
                     Internet Gateway exists
        required: false
    vcn_id:
        description: Identifier of the Virtual Cloud Network to which the
                     Internet Gateway is attached.
        required: false
    ig_id:
        description: Identifier of the Internet Gateway. Required if any specific
                     Internet Gateway details needs to be fetched. Mutually exclusive
                     with compartment_id and vcn_id.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
#Fetch Internet Gateway
- name: List Internet Gateway
  oci_internet_gateway_facts:
      compartment_id: 'ocid1.compartment..xcds'
      vcn_id: 'ocid1.vcn..dfxs'

#Fetch specific Internet Gateway
- name: List a specific Internet Gateway
  oci_internet_gateway_facts:
      id: 'ocid1.internetgateway..xcds'
"""

RETURN = """
    internet_gateways:
        description: Attributes of the  Internet Gateways.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the Internet Gateway
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            display_name:
                description: Name assigned to the Internet Gateway during creation
                returned: always
                type: string
                sample: ansible_ig
            id:
                description: Identifier of the Internet Gateway
                returned: always
                type: string
                sample: ocid1.internetgateway.oc1.axdf
            vcn_id:
                description: Identifier of the Virtual Cloud Network to which the
                             Internet Gateway is attached.
                returned: always
                type: string
                sample: ocid1.vcn..ixcd
            lifecycle_state:
                description: The current state of the Internet Gateway
                returned: always
                type: string
                sample: ACTIVE
            time_created:
                description: Date and time when the Internet Gateway was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
        sample: [
        {
            "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "freeform_tags":{"region":"east"},
            "defined_tags":{"features":{"capacity":"medium"}},
            "display_name":"ansible_internet_gateway_updated",
            "id":"ocid1.internetgateway.oc1.phx.xxxxxEXAMPLExxxxx",
            "is_enabled":true,
            "lifecycle_state":"AVAILABLE",
            "time_created":"2017-11-14T18:50:50.751000+00:00",
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


def list_internet_gateways(virtual_network_client, module):
    result = dict(internet_gateways="")
    compartment_id = module.params.get("compartment_id")
    vcn_id = module.params.get("vcn_id")
    ig_id = module.params.get("ig_id")
    try:
        if compartment_id and vcn_id:
            existing_igs = oci_utils.list_all_resources(
                virtual_network_client.list_internet_gateways,
                compartment_id=compartment_id,
                vcn_id=vcn_id,
                display_name=module.params["display_name"],
            )
        elif ig_id:
            response = oci_utils.call_with_backoff(
                virtual_network_client.get_internet_gateway, ig_id=ig_id
            )
            existing_igs = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["internet_gateways"] = to_dict(existing_igs)
    return result


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            vcn_id=dict(type="str", required=False),
            ig_id=dict(type="str", required=False, aliases=["id"]),
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

    result = list_internet_gateways(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
