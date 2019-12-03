#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_node_pool_options_facts
short_description: Retrieve options available for node pools in OCI Container Engine for Kubernetes Service
description:
    - This module retrieves options available for node pools in OCI Container Engine for Kubernetes Service.
version_added: "2.5"
options:
    node_pool_option_id:
        description: The id of the option set to retrieve. Use "all" to get all options, or use a cluster ID to get
                     options specific to the provided cluster.
        required: true
        aliases: ['id']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get all the node pool options available for node pools
  oci_node_pool_options_facts:
    node_pool_option_id: all

- name: Get all the node pool options available for a specific cluster
  oci_node_pool_options_facts:
    node_pool_option_id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx
"""

RETURN = """
node_pool_options:
    description: Options available for node pools
    returned: always
    type: complex
    contains:
        images:
            description: Available images for nodes
            returned: always
            type: list
        kubernetes_versions:
            description: Available Kubernetes versions.
            returned: always
            type: list
        shapes:
            description: Available shapes for nodes.
            returned: always
            type: list
    sample: {
            "images": [
                "Oracle-Linux-7.4",
                "Oracle-Linux-7.5"
            ],
            "kubernetes_versions": [
                "v1.8.11",
                "v1.9.7",
                "v1.10.3",
                "v1.11.1"
            ],
            "shapes": [
                "VM.Standard2.1",
                "VM.Standard2.2",
                "VM.Standard2.4",
                "VM.Standard2.8",
                "VM.DenseIO2.8"
            ]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.container_engine.container_engine_client import ContainerEngineClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(node_pool_option_id=dict(type="str", required=True, aliases=["id"]))
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    try:
        result = to_dict(
            oci_utils.call_with_backoff(
                container_engine_client.get_node_pool_options,
                node_pool_option_id=module.params["node_pool_option_id"],
            ).data
        )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(node_pool_options=result)


if __name__ == "__main__":
    main()
