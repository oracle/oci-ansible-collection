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
module: oci_fast_connect_provider_virtual_circuit_bandwidth_shape_facts
short_description: Fetches details of one or more OCI Fast Connect Provider Virtual Circuit Bandwidth
description:
     - Fetches details of the OCI Fast Connect Provider Virtual Circuit Bandwidth
version_added: "2.5"
options:
    provider_service_id:
        description: Identifier of the fast connect provider service whose virtual circuit bandwidth needs to be fetched.
        required: true
        aliases: [ 'id' ]
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Fetch All Fast Connect Provider Virtual Circuit Bandwidth under a specific Provider Service
- name: Fetch All Fast Connect Provider Virtual Circuit Bandwidth under a specific Provider Service
  oci_fast_connect_provider_virtual_circuit_bandwidth_shape_facts:
      provider_service_id: 'ocid1.serviceprovider.oc1.iad.xxxxxEXAMPLExxxxx'
"""

RETURN = """
    oci_fast_connect_provider_virtual_circuit_bandwidth_shapes:
        description: Attributes of the Fast Connect Provider Service.
        returned: success
        type: complex
        contains:
            bandwidth_in_mbps:
                description: The bandwidth in Mbps.
                returned: always
                type: int
                sample: 1000
            name:
                description: The name of the bandwidth shape.
                returned: always
                type: string
                sample: 1 Gbps
        sample: [{
                    "bandwidth_in_mbps":1000,
                    "name":"1 Gbps"
                },
                {
                    "bandwidth_in_mbps":2000,
                    "name":"2 Gbps"
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


def list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
    virtual_network_client, module
):
    result = dict(fast_connect_provider_virtual_circuit_bandwidth_shapes="")
    existing_fast_connect_provider_virtual_circuit_bandwidth_shapes = None
    provider_service_id = module.params.get("provider_service_id")
    try:
        existing_fast_connect_provider_virtual_circuit_bandwidth_shapes = oci_utils.list_all_resources(
            virtual_network_client.list_fast_connect_provider_virtual_circuit_bandwidth_shapes,
            provider_service_id=provider_service_id,
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    result["fast_connect_provider_virtual_circuit_bandwidth_shapes"] = to_dict(
        existing_fast_connect_provider_virtual_circuit_bandwidth_shapes
    )
    return result


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(provider_service_id=dict(type="str", required=True, aliases=["id"]))
    )
    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    virtual_network_client = oci_utils.create_service_client(
        module, VirtualNetworkClient
    )

    result = list_fast_connect_provider_virtual_circuit_bandwidth_shapes(
        virtual_network_client, module
    )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
