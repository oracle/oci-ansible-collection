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
module: oci_node_pool_facts
short_description: Retrieve facts of node pools in OCI Container Engine for Kubernetes Service
description:
    - This module retrieves information of a specific node pool or of all the node pools in OCI Container Engine
      for Kubernetes Service.
version_added: "2.5"
options:
    node_pool_id:
        description: The OCID of the node pool. I(node_pool_id) is required to get the details of a node pool.
        required: false
        aliases: [ 'id' ]
    compartment_id:
        description: The OCID of the compartment. I(compartment_id) is required to list all the node pools in a
                     compartment.
        required: false
    cluster_id:
        description: The OCID of the cluster.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_name_option ]
"""

EXAMPLES = """
- name: Get all the node pools in a compartment
  oci_node_pool_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get all the node pools in a compartment and filter by cluster
  oci_node_pool_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    cluster_id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx

- name: Get a specific node pool
  oci_node_pool_facts:
    id: ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx
"""

RETURN = """
node_pools:
    description: List of node pool details
    returned: always
    type: complex
    contains:
        cluster_id:
            description: The OCID of the cluster to which this node pool is attached.
            returned: always
            type: list
            sample: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx
        compartment_id:
            description: The OCID of the compartment in which the node pool exists.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        id:
            description: The OCID of the node pool.
            returned: always
            type: string
            sample: ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx
        initial_node_labels:
            description: A list of key/value pairs to add to nodes after they join the Kubernetes cluster.
            returned: always
            type: list
            sample: [
                {
                    "key": "type",
                    "value": "standard"
                },
                {
                    "key": "stage",
                    "value": "prod"
                }
            ]
        kubernetes_version:
            description: The version of Kubernetes running on the nodes in the node pool.
            returned: always
            type: string
            sample: v1.9.7
        lifecycle_details:
            description: Details about the state of the cluster masters.
            returned: always
            type: string
        name:
            description: The name of the node pool.
            returned: always
            type: string
            sample: sample_node_pool
        node_image_id:
            description: The OCID of the image running on the nodes in the node pool.
            returned: always
            type: string
            sample: ocid1.image.oc1..xxxxxEXAMPLExxxxx
        node_shape:
            description: The name of the node shape of the nodes in the node pool.
            returned: always
            type: string
            sample: VM.Standard2.1
        nodes:
            description: The nodes in the node pool.
            returned: when retrieving a specific node pool
            type: string
        quantity_per_subnet:
            description: The number of nodes in each subnet.
            returned: always
            type: int
            sample: 1
        ssh_public_key:
            description: The SSH public key on each node in the node pool.
            returned: always
            type: string
        subnet_ids:
            description: The OCIDs of the subnets in which to place nodes for this node pool.
            returned: always
            type: list
    sample: [{
            "cluster_id": "ocid1.cluster.oc1..xxxxxEXAMPLExxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx",
            "initial_node_labels": [
                {
                    "key": "type",
                    "value": "standard"
                },
                {
                    "key": "stage",
                    "value": "prod"
                }
            ],
            "kubernetes_version": "v1.9.7",
            "name": "test_node_pool",
            "node_image_id": "ocid1.image.oc1..xxxxxEXAMPLExxxxx",
            "node_image_name": "Oracle-Linux-7.4",
            "node_shape": "VM.Standard2.1",
            "nodes": [
                {
                    "availability_domain": "IwGV:US-ASHBURN-AD-1",
                    "id": "ocid1.instance.oc1..xxxxxEXAMPLExxxxx",
                    "lifecycle_details": "waiting for running compute instance",
                    "lifecycle_state": "UPDATING",
                    "name": "oke-c3dsodfgezw-n3wiztggrrt-st2au5vefpq-0",
                    "node_error": null,
                    "node_pool_id": "ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx",
                    "public_ip": "129.213.129.26",
                    "subnet_id": "ocid1.subnet.oc1..xxxxxEXAMPLExxxxx"
                }
            ],
            "quantity_per_subnet": 1,
            "ssh_public_key": "",
            "subnet_ids": [
                "ocid1.subnet..xxxxxEXAMPLExxxxx"
            ]
        }]
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
    module_args = oci_utils.get_facts_module_arg_spec(filter_by_name=True)
    module_args.update(
        dict(
            node_pool_id=dict(type="str", required=False, aliases=["id"]),
            cluster_id=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    node_pool_id = module.params["node_pool_id"]

    try:
        if node_pool_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        container_engine_client.get_node_pool, node_pool_id=node_pool_id
                    ).data
                )
            ]
        else:
            if module.params["cluster_id"]:
                result = to_dict(
                    oci_utils.list_all_resources(
                        container_engine_client.list_node_pools,
                        compartment_id=module.params["compartment_id"],
                        cluster_id=module.params["cluster_id"],
                        name=module.params["name"],
                    )
                )
            else:
                result = to_dict(
                    oci_utils.list_all_resources(
                        container_engine_client.list_node_pools,
                        compartment_id=module.params["compartment_id"],
                        name=module.params["name"],
                    )
                )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(node_pools=result)


if __name__ == "__main__":
    main()
