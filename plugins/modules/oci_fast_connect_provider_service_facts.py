#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
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
module: oci_fast_connect_provider_service_facts
short_description: Fetches details of one or more OCI Fast Connect Provider Services
description:
     - Fetches details of the OCI Fast Connect Provider Services
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment under which the specified fast connect provider service exists
        required: false
    provider_service_id:
        description: Identifier of the fast connect provider service whose details needs to be fetched.
        required: false
        aliases: [ 'id' ]
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch All Fast Connect Provider Services under a specific compartment
- name: Fetch All Fast Connect Provider Services under a specific compartment
  oci_fast_connect_provider_service_facts:
      compartment_id: 'ocid1.compartment.oc1.iad.xxxxxEXAMPLExxxxx'

# Fetch a specific Fast Connect Provider Service
- name: Fetch a specific Fast Connect Provider Service
  oci_fast_connect_provider_service_facts:
      provider_service_id: 'ocid1.serviceprovider.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    oci_fast_connect_provider_services:
        description: Attributes of the Fast Connect Provider Service.
        returned: success
        type: complex
        contains:
            description:
                description: A description of the service offered by the provider.
                returned: always
                type: string
                sample: https://megaport.al/
            id:
                description: Identifier of the Fast Connect Provider Service
                returned: always
                type: string
                sample: ocid1.providerservice.oc1.iad.xxxxxEXAMPLExxxxx
            private_peering_bgp_management:
                description: Who is responsible for managing the private peering BGP information.
                returned: always
                type: string
                sample: CUSTOMER_MANAGED
            provider_name:
                description: The name of the provider.
                returned: always
                type: string
                sample: Megaport
            provider_service_name:
                description: The name of the service offered by the provider.
                returned: always
                type: string
                sample: Service
            public_peering_bgp_management:
                description: Who is responsible for managing the public peering BGP information.
                returned: always
                type: string
                sample: ORACLE_MANAGED
            supported_virtual_circuit_types:
                description: An array of virtual circuit types supported by this service.
                returned: always
                type: list
                sample: ["PRIVATE", "PUBLIC"]
            type:
                description: Provider service type.
                returned: always
                type: list
                sample: LAYER2
        sample: [{
                        "description":"https://megaport.al/",
                        "id":"ocid1.providerservice.oc1.iad.xxxxxEXAMPLExxxxx",
                        "private_peering_bgp_management":"CUSTOMER_MANAGED",
                        "provider_name":"Megaport",
                        "provider_service_name":"Service",
                        "public_peering_bgp_management":"ORACLE_MANAGED",
                        "supported_virtual_circuit_types":null,
                        "type":"LAYER2"
                },
                {
                         "description":"https://marketplaceportal.com/web/guest/login",
                         "id":"ocid1.providerservice.oc1.iad.xxxxxEXAMPLExxxxx",
                         "private_peering_bgp_management":"CUSTOMER_MANAGED",
                         "provider_name":"Digital Realty",
                         "provider_service_name":"Service Exchange",
                         "public_peering_bgp_management":"ORACLE_MANAGED",
                         "supported_virtual_circuit_types":[
                                                             "PRIVATE",
                                                             "PUBLIC"
                                                           ],
                         "type":"LAYER2"
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


def list_fast_connect_provider_services(virtual_network_client, module):
    result = dict(fast_connect_provider_services="")
    compartment_id = module.params.get("compartment_id")
    provider_service_id = module.params.get("provider_service_id")
    try:
        if compartment_id:
            existing_fast_connect_provider_services = oci_utils.list_all_resources(
                virtual_network_client.list_fast_connect_provider_services,
                compartment_id=compartment_id,
            )
        elif provider_service_id:
            response = oci_utils.call_with_backoff(
                virtual_network_client.get_fast_connect_provider_service,
                provider_service_id=provider_service_id,
            )
            existing_fast_connect_provider_services = [response.data]
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["fast_connect_provider_services"] = to_dict(
        existing_fast_connect_provider_services
    )
    return result


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            provider_service_id=dict(type="str", required=False, aliases=["id"]),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args, mutually_exclusive=[["compartment_id", "id"]]
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_fast_connect_provider_services(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
