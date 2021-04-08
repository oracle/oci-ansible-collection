#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_network_fast_connect_provider_service_facts
short_description: Fetches details about one or multiple FastConnectProviderService resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple FastConnectProviderService resources in Oracle Cloud Infrastructure
    - Lists the service offerings from supported providers. You need this
      information so you can specify your desired provider and service
      offering when you create a virtual circuit.
    - For the compartment ID, provide the OCID of your tenancy (the root compartment).
    - For more information, see L(FastConnect Overview,https://docs.cloud.oracle.com/iaas/Content/Network/Concepts/fastconnect.htm).
    - If I(provider_service_id) is specified, the details of a single FastConnectProviderService will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    provider_service_id:
        description:
            - The OCID of the provider service.
            - Required to get a specific fast_connect_provider_service.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple fast_connect_provider_services.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List fast_connect_provider_services
  oci_network_fast_connect_provider_service_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific fast_connect_provider_service
  oci_network_fast_connect_provider_service_facts:
    provider_service_id: "ocid1.providerservice.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
fast_connect_provider_services:
    description:
        - List of FastConnectProviderService resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - The location of the provider's website or portal. This portal is where you can get information
                  about the provider service, create a virtual circuit connection from the provider to Oracle
                  Cloud Infrastructure, and retrieve your provider service key for that virtual circuit connection.
                - "Example: `https://example.com`"
            returned: on success
            type: string
            sample: https://example.com
        id:
            description:
                - The OCID of the service offered by the provider.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        private_peering_bgp_management:
            description:
                - Who is responsible for managing the private peering BGP information.
            returned: on success
            type: string
            sample: CUSTOMER_MANAGED
        provider_name:
            description:
                - The name of the provider.
            returned: on success
            type: string
            sample: provider_name_example
        provider_service_name:
            description:
                - The name of the service offered by the provider.
            returned: on success
            type: string
            sample: provider_service_name_example
        public_peering_bgp_management:
            description:
                - Who is responsible for managing the public peering BGP information.
            returned: on success
            type: string
            sample: CUSTOMER_MANAGED
        supported_virtual_circuit_types:
            description:
                - An array of virtual circuit types supported by this service.
            returned: on success
            type: list
            sample: []
        customer_asn_management:
            description:
                - Who is responsible for managing the ASN information for the network at the other end
                  of the connection from Oracle.
            returned: on success
            type: string
            sample: CUSTOMER_MANAGED
        provider_service_key_management:
            description:
                - Who is responsible for managing the provider service key.
            returned: on success
            type: string
            sample: CUSTOMER_MANAGED
        bandwith_shape_management:
            description:
                - Who is responsible for managing the virtual circuit bandwidth.
            returned: on success
            type: string
            sample: CUSTOMER_MANAGED
        required_total_cross_connects:
            description:
                - Total number of cross-connect or cross-connect groups required for the virtual circuit.
            returned: on success
            type: int
            sample: 56
        type:
            description:
                - Provider service type.
            returned: on success
            type: string
            sample: LAYER2
    sample: [{
        "description": "https://example.com",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "private_peering_bgp_management": "CUSTOMER_MANAGED",
        "provider_name": "provider_name_example",
        "provider_service_name": "provider_service_name_example",
        "public_peering_bgp_management": "CUSTOMER_MANAGED",
        "supported_virtual_circuit_types": [],
        "customer_asn_management": "CUSTOMER_MANAGED",
        "provider_service_key_management": "CUSTOMER_MANAGED",
        "bandwith_shape_management": "CUSTOMER_MANAGED",
        "required_total_cross_connects": 56,
        "type": "LAYER2"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import VirtualNetworkClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FastConnectProviderServiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "provider_service_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_fast_connect_provider_service,
            provider_service_id=self.module.params.get("provider_service_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_fast_connect_provider_services,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


FastConnectProviderServiceFactsHelperCustom = get_custom_class(
    "FastConnectProviderServiceFactsHelperCustom"
)


class ResourceFactsHelper(
    FastConnectProviderServiceFactsHelperCustom,
    FastConnectProviderServiceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            provider_service_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="fast_connect_provider_service",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(fast_connect_provider_services=result)


if __name__ == "__main__":
    main()
