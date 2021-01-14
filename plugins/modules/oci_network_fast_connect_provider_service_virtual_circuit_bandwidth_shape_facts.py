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
module: oci_network_fast_connect_provider_service_virtual_circuit_bandwidth_shape_facts
short_description: Fetches details about one or multiple FastConnectProviderServiceVirtualCircuitBandwidthShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple FastConnectProviderServiceVirtualCircuitBandwidthShape resources in Oracle Cloud Infrastructure
    - Gets the list of available virtual circuit bandwidth levels for a provider.
      You need this information so you can specify your desired bandwidth level (shape) when you create a virtual circuit.
    - For more information about virtual circuits, see L(FastConnect Overview,https://docs.cloud.oracle.com/Content/Network/Concepts/fastconnect.htm).
version_added: "2.9"
author: Oracle (@oracle)
options:
    provider_service_id:
        description:
            - The OCID of the provider service.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List fast_connect_provider_service_virtual_circuit_bandwidth_shapes
  oci_network_fast_connect_provider_service_virtual_circuit_bandwidth_shape_facts:
    provider_service_id: ocid1.providerservice.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
fast_connect_provider_service_virtual_circuit_bandwidth_shapes:
    description:
        - List of FastConnectProviderServiceVirtualCircuitBandwidthShape resources
    returned: on success
    type: complex
    contains:
        bandwidth_in_mbps:
            description:
                - The bandwidth in Mbps.
                - "Example: `10000`"
            returned: on success
            type: int
            sample: 10000
        name:
            description:
                - The name of the bandwidth shape.
                - "Example: `10 Gbps`"
            returned: on success
            type: string
            sample: 10 Gbps
    sample: [{
        "bandwidth_in_mbps": 10000,
        "name": "10 Gbps"
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


class FastConnectProviderServiceVirtualCircuitBandwidthShapeFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "provider_service_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes,
            provider_service_id=self.module.params.get("provider_service_id"),
            **optional_kwargs
        )


FastConnectProviderServiceVirtualCircuitBandwidthShapeFactsHelperCustom = get_custom_class(
    "FastConnectProviderServiceVirtualCircuitBandwidthShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    FastConnectProviderServiceVirtualCircuitBandwidthShapeFactsHelperCustom,
    FastConnectProviderServiceVirtualCircuitBandwidthShapeFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            provider_service_id=dict(aliases=["id"], type="str", required=True),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="fast_connect_provider_service_virtual_circuit_bandwidth_shape",
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

    module.exit_json(
        fast_connect_provider_service_virtual_circuit_bandwidth_shapes=result
    )


if __name__ == "__main__":
    main()
