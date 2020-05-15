#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
version_added: "2.5"
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
author:
    - Manoj Meda (@manojmeda)
    - Mike Ross (@mross22)
    - Nabeel Al-Saber (@nalsaber)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific node_pool_options
  oci_container_engine_node_pool_options_facts:
    node_pool_option_id: all

- name: Get a specific node_pool_options
  oci_container_engine_node_pool_options_facts:
    node_pool_option_id: ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx

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
                - Available image names.
            returned: on success
            type: list
            sample: []
    sample: {
        "kubernetes_versions": [],
        "shapes": [],
        "images": []
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
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(node_pool_options=result)


if __name__ == "__main__":
    main()
