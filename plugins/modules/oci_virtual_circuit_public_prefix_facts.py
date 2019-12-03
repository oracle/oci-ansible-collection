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
module: oci_virtual_circuit_public_prefix_facts
short_description: Fetches details of one or more OCI Virtual Circuit Public Prefixes
description:
     - Fetches details of all Virtual Circuit Public Prefixes of a specified Virtual Circuit.
version_added: "2.5"
options:
    virtual_circuit_id:
        description: Identifier of the Virtual Circuit whose Public Prefixes needs to be fetched.
        required: false
        aliases: [ 'id' ]
    verification_state:
        description: A filter to return only resources that match the given verification state.
        required: false
        choices: ["IN_PROGRESS", "COMPLETED", "FAILED"]
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch All Virtual Circuit Public Prefixes of a specific Virtual Circuit
- name: Fetch All Virtual Circuit Public Prefixes of a specific Virtual Circuit
  oci_virtual_circuit_public_prefix_facts:
      virtual_circuit_id: 'ocid1.virtualcircuit.oc1.iad.xxxxxEXAMPLExxxxx'


# Fetch All Virtual Circuit Public Prefixes of a specific Virtual Circuit, filtered by
# verification state
- name: Fetch All Virtual Circuits under a specific compartment, filtered by display name and lifecycle state
  oci_virtual_circuit_public_prefix_facts:
      virtual_circuit_id: 'ocid1.virtualcircuit.oc1.iad.xxxxxEXAMPLExxxxx'
      verification_state: 'COMPLETED'
"""

RETURN = """
    oci_virtual_circuit_public_prefixes:
        description: Attributes of the Fetched Virtual Circuit Public Prefixes.
        returned: success
        type: complex
        contains:
            cidr_block:
                description: Publix IP prefix (CIDR) that the customer specified.
                returned: always
                type: string
                sample: 10.0.0.21/31
            verification_state:
                description: Oracle must verify that the customer owns the public
                             IP prefix before traffic for that prefix can flow across the
                             virtual circuit. Verification can take a few business days.
                             IN_PROGRESS means Oracle is verifying the prefix. COMPLETED
                             means verification succeeded. FAILED means verification failed
                             and traffic for this prefix will not flow across the connection.
                returned: always
                type: string
                sample: COMPLETED
        sample: [{
                    "cidr_block":"10.0.0.20/31",
                    "verification_state":"COMPLETED"
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


def list_virtual_circuit_public_prefixes(virtual_network_client, module):
    result = dict(virtual_circuit_public_prefixes="")
    virtual_circuit_id = module.params.get("virtual_circuit_id")
    try:
        optional_list_method_params = ["verification_state"]
        optional_kwargs = dict(
            (param, module.params[param])
            for param in optional_list_method_params
            if module.params.get(param) is not None
        )
        existing_virtual_circuit_public_prefixes = oci_utils.list_all_resources(
            virtual_network_client.list_virtual_circuit_public_prefixes,
            virtual_circuit_id=virtual_circuit_id,
            **optional_kwargs
        )
        result["virtual_circuit_public_prefixes"] = to_dict(
            existing_virtual_circuit_public_prefixes
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    return result


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            virtual_circuit_id=dict(type="str", required=False, aliases=["id"]),
            verification_state=dict(
                type="str",
                required=False,
                choices=["IN_PROGRESS", "COMPLETED", "FAILED"],
            ),
        )
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_virtual_circuit_public_prefixes(virtual_network_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
