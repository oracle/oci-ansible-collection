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
module: oci_network_virtual_circuit_public_prefix_facts
short_description: Fetches details about one or multiple VirtualCircuitPublicPrefix resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VirtualCircuitPublicPrefix resources in Oracle Cloud Infrastructure
    - Lists the public IP prefixes and their details for the specified
      public virtual circuit.
version_added: "2.9"
author: Oracle (@oracle)
options:
    virtual_circuit_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the virtual circuit.
        type: str
        aliases: ["id"]
        required: true
    verification_state:
        description:
            - A filter to only return resources that match the given verification
              state.
            - The state value is case-insensitive.
        type: str
        choices:
            - "IN_PROGRESS"
            - "COMPLETED"
            - "FAILED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List virtual_circuit_public_prefixes
  oci_network_virtual_circuit_public_prefix_facts:
    virtual_circuit_id: "ocid1.virtualcircuit.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
virtual_circuit_public_prefixes:
    description:
        - List of VirtualCircuitPublicPrefix resources
    returned: on success
    type: complex
    contains:
        cidr_block:
            description:
                - Publix IP prefix (CIDR) that the customer specified.
            returned: on success
            type: string
            sample: cidr_block_example
        verification_state:
            description:
                - Oracle must verify that the customer owns the public IP prefix before traffic
                  for that prefix can flow across the virtual circuit. Verification can take a
                  few business days. `IN_PROGRESS` means Oracle is verifying the prefix. `COMPLETED`
                  means verification succeeded. `FAILED` means verification failed and traffic for
                  this prefix will not flow across the connection.
            returned: on success
            type: string
            sample: IN_PROGRESS
    sample: [{
        "cidr_block": "cidr_block_example",
        "verification_state": "IN_PROGRESS"
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


class VirtualCircuitPublicPrefixFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "virtual_circuit_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "verification_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_virtual_circuit_public_prefixes,
            virtual_circuit_id=self.module.params.get("virtual_circuit_id"),
            **optional_kwargs
        )


VirtualCircuitPublicPrefixFactsHelperCustom = get_custom_class(
    "VirtualCircuitPublicPrefixFactsHelperCustom"
)


class ResourceFactsHelper(
    VirtualCircuitPublicPrefixFactsHelperCustom,
    VirtualCircuitPublicPrefixFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            virtual_circuit_id=dict(aliases=["id"], type="str", required=True),
            verification_state=dict(
                type="str", choices=["IN_PROGRESS", "COMPLETED", "FAILED"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="virtual_circuit_public_prefix",
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

    module.exit_json(virtual_circuit_public_prefixes=result)


if __name__ == "__main__":
    main()
