#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_container_engine_cluster_options_facts
short_description: Fetches details about a ClusterOptions resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ClusterOptions resource in Oracle Cloud Infrastructure
    - Get options available for clusters.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    cluster_option_id:
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
- name: Get a specific cluster_options
  oci_container_engine_cluster_options_facts:
    # required
    cluster_option_id: "ocid1.clusteroption.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
cluster_options:
    description:
        - ClusterOptions resource
    returned: on success
    type: complex
    contains:
        kubernetes_versions:
            description:
                - Available Kubernetes versions.
            returned: on success
            type: list
            sample: []
        cluster_pod_network_options:
            description:
                - Available CNIs and network options for existing and new node pools of the cluster
            returned: on success
            type: complex
            contains:
                cni_type:
                    description:
                        - The CNI used by the node pools of this cluster
                    returned: on success
                    type: str
                    sample: OCI_VCN_IP_NATIVE
    sample: {
        "kubernetes_versions": [],
        "cluster_pod_network_options": [{
            "cni_type": "OCI_VCN_IP_NATIVE"
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.container_engine import ContainerEngineClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ClusterOptionsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "cluster_option_id",
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
            self.client.get_cluster_options,
            cluster_option_id=self.module.params.get("cluster_option_id"),
            **optional_kwargs
        )


ClusterOptionsFactsHelperCustom = get_custom_class("ClusterOptionsFactsHelperCustom")


class ResourceFactsHelper(
    ClusterOptionsFactsHelperCustom, ClusterOptionsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            cluster_option_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cluster_options",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(cluster_options=result)


if __name__ == "__main__":
    main()
