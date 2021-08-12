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
module: oci_container_engine_node_pool_options_facts
short_description: Fetches details about a NodePoolOptions resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a NodePoolOptions resource in Oracle Cloud Infrastructure
    - Get options available for node pools.
version_added: "2.9"
author: Oracle (@oracle)
options:
    node_pool_option_id:
        description:
            - "The id of the option set to retrieve. Use \\"all\\" get all options, or use a cluster ID to get options specific to the provided cluster."
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific node_pool_options
  oci_container_engine_node_pool_options_facts:
    node_pool_option_id: "all"

- name: Get a specific node_pool_options
  oci_container_engine_node_pool_options_facts:
    node_pool_option_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
node_pool_options:
    description:
        - NodePoolOptions resource
    returned: on success
    type: complex
    contains:
        kubernetes_versions:
            description:
                - Available Kubernetes versions.
            returned: on success
            type: list
            sample: []
        shapes:
            description:
                - Available shapes for nodes.
            returned: on success
            type: list
            sample: []
        images:
            description:
                - Deprecated. See sources.
                  When creating a node pool using the `CreateNodePoolDetails` object, only image names contained in this
                  property can be passed to the `nodeImageName` property.
            returned: on success
            type: list
            sample: []
        sources:
            description:
                - Available source of the node.
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - The source type of this option.
                          `IMAGE` means the OCID is of an image.
                    returned: on success
                    type: string
                    sample: IMAGE
                source_name:
                    description:
                        - The user-friendly name of the entity corresponding to the OCID.
                    returned: on success
                    type: string
                    sample: source_name_example
                image_id:
                    description:
                        - The OCID of the image.
                    returned: on success
                    type: string
                    sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "kubernetes_versions": [],
        "shapes": [],
        "images": [],
        "sources": [{
            "source_type": "IMAGE",
            "source_name": "source_name_example",
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        }]
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NodePoolOptionsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "node_pool_option_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_node_pool_options,
            node_pool_option_id=self.module.params.get("node_pool_option_id"),
            **optional_kwargs
        )


NodePoolOptionsFactsHelperCustom = get_custom_class("NodePoolOptionsFactsHelperCustom")


class ResourceFactsHelper(
    NodePoolOptionsFactsHelperCustom, NodePoolOptionsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            node_pool_option_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="node_pool_options",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(node_pool_options=result)


if __name__ == "__main__":
    main()
