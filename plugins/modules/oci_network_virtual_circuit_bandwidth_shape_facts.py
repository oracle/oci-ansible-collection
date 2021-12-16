#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_network_virtual_circuit_bandwidth_shape_facts
short_description: Fetches details about one or multiple VirtualCircuitBandwidthShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VirtualCircuitBandwidthShape resources in Oracle Cloud Infrastructure
    - The deprecated operation lists available bandwidth levels for virtual circuits. For the compartment ID, provide the
      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of your tenancy (the root compartment).
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List virtual_circuit_bandwidth_shapes
  oci_network_virtual_circuit_bandwidth_shape_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
virtual_circuit_bandwidth_shapes:
    description:
        - List of VirtualCircuitBandwidthShape resources
    returned: on success
    type: complex
    contains:
        bandwidth_in_mbps:
            description:
                - The bandwidth in Mbps.
                - "Example: `10000`"
            returned: on success
            type: int
            sample: 56
        name:
            description:
                - The name of the bandwidth shape.
                - "Example: `10 Gbps`"
            returned: on success
            type: str
            sample: name_example
    sample: [{
        "bandwidth_in_mbps": 56,
        "name": "name_example"
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


class VirtualCircuitBandwidthShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
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
            self.client.list_virtual_circuit_bandwidth_shapes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


VirtualCircuitBandwidthShapeFactsHelperCustom = get_custom_class(
    "VirtualCircuitBandwidthShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    VirtualCircuitBandwidthShapeFactsHelperCustom,
    VirtualCircuitBandwidthShapeFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(compartment_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="virtual_circuit_bandwidth_shape",
        service_client_class=VirtualNetworkClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(virtual_circuit_bandwidth_shapes=result)


if __name__ == "__main__":
    main()
