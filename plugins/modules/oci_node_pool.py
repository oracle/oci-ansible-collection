#!/usr/bin/python
# Copyright (c) 2018, 2019 Oracle and/or its affiliates.
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
module: oci_node_pool
short_description: Manage node pools in OCI Container Engine for Kubernetes Service
description:
    - This module allows the user to create, delete and update node pools in OCI Container Engine for Kubernetes
      Service.
version_added: "2.5"
options:
    cluster_id:
        description: The OCID of the cluster to which this node pool is attached. Required to create a node pool.
        required: false
    compartment_id:
        description: The OCID of the compartment in which the node pool exists. Required to create a node pool.
        required: false
    initial_node_labels:
        description: A list of key/value pairs to add to nodes after they join the Kubernetes cluster.
        required: false
        suboptions:
            key:
                description: The key of the pair.
                required: true
            value:
                description: The value of the pair.
                required: true
    kubernetes_version:
        description: The version of Kubernetes to install on the nodes in the node pool. Required to create a node pool.
        required: false
    name:
        description: The name of the node pool. Avoid entering confidential information. Required to create a node pool.
        required: false
    node_image_name:
        description: The name of the image running on the nodes in the node pool. Required to create a node pool.
        required: false
    node_pool_id:
        description: The OCID of the node pool. Required to update or delete a node pool.
        required: false
        aliases: ['id']
    node_shape:
        description: The name of the node shape of the nodes in the node pool. Required to create a node pool.
        required: false
    quantity_per_subnet:
        description: The number of nodes to create in each subnet.
        required: false
    ssh_public_key:
        description: The SSH public key to add to each node in the node pool.
        required: false
    subnet_ids:
        description: The OCIDs of the subnets in which to place nodes for this node pool. Required to create a node
                     pool.
        required: false
    state:
        description: Create or update a node pool with I(state=present). Use I(state=absent) to delete a node pool.
        required: false
        default: present
        choices: ['present', 'absent']
    wait:
        description: While creating or updating a node pool, whether to wait for a number of nodes specified using
                     I(count_of_nodes_to_wait) to be in a state specified using I(wait_until). While deleting a node
                     pool, whether to wait for the associated work request to get into SUCCEEDED state.
        default: yes
        required: false
        type: bool
    count_of_nodes_to_wait:
        description: Number of nodes in the node pool to wait for getting into a lifecycle state specified using
                     I(wait_until) when I(wait=yes) and I(state=present).
        default: 1
        required: false
    wait_until:
        description: The lifecycle state of a node in node pool to wait for while creating or updating a node pool with
                     I(wait=yes).
        required: false
        default: ACTIVE
    wait_timeout:
        description: Time, in seconds, to wait when I(wait=yes).
        required: false
        default: 1200
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create a node pool and wait for atleast two nodes in the node pool to reach ACTIVE state before returning
  oci_node_pool:
    cluster_id: ocid1.cluster.oc1..xxxxxEXAMPLExxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: test_node_pool
    kubernetes_version: "v1.9.7"
    node_image_name: "Oracle-Linux-7.4"
    node_shape: "VM.Standard2.1"
    quantity_per_subnet: 1
    subnet_ids:
        - "ocid1.subnet.oc1..xxxxxEXAMPLExxxxx...abcd"
        - "ocid1.subnet.oc1..xxxxxEXAMPLExxxxx...efgh"
        - "ocid1.subnet.oc1..xxxxxEXAMPLExxxxx...ijkl"
    initial_node_labels:
      - key: "vm_type"
        value: "standard"
      - key: "stage"
        value: "dev"
    count_of_nodes_to_wait: 2

- name: Update node pool
  oci_node_pool:
    id: ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx
    name: ansible_node_pool
    kubernetes_version: "v1.10.3"
    initial_node_labels:
      - key: "vm_type"
        value: "standard"
      - key: "stage"
        value: "prod"

- name: Delete node pool
  oci_node_pool:
    id: ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
node_pool:
    description: Information about the node pool
    returned: On successful create, delete & update operations on node pool
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
                    "key": "vm_type",
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
            returned: always
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
    sample: {
            "cluster_id": "ocid1.cluster.oc1..xxxxxEXAMPLExxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx",
            "initial_node_labels": [
                {
                    "key": "vm_type",
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
        }
work_request:
    description: Information of work request
    returned: When a new work request is created
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment in which the work request exists.
            returned: always
            type: string
        id:
            description: The OCID of the work request.
            returned: always
            type: string
        operation_type:
            description: The type of work the work request is doing.
            returned: always
            type: string
        resources:
            description: The resources this work request affects.
            returned: always
            type: list
        status:
            description: The current status of the work request.
            returned: always
            type: string
        time_accepted:
            description: The time the work request was accepted.
            returned: always
            type: datetime
        time_finished:
            description: The time the work request was finished.
            returned: always
            type: datetime
        time_started:
            description: The time the work request was started.
            returned: always
            type: datetime
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.clustersworkrequest.oc1..xxxxxEXAMPLExxxxx",
            "operation_type": "NODEPOOL_UPDATE",
            "resources": [
                {
                    "action_type": "UPDATED",
                    "entity_type": "nodepool",
                    "entity_uri": "/nodePools/ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx",
                    "identifier": "ocid1.nodepool.oc1..xxxxxEXAMPLExxxxx"
                },
                {
                    "action_type": "RELATED",
                    "entity_type": "cluster",
                    "entity_uri": "/clusters/ocid1.cluster.oc1..xxxxxEXAMPLExxxxx",
                    "identifier": "ocid1.cluster.oc1..xxxxxEXAMPLExxxxx"
                }
            ],
            "status": "SUCCEEDED",
            "time_accepted": "2018-08-02T10:22:22+00:00",
            "time_finished": "2018-08-02T10:24:13+00:00",
            "time_started": "2018-08-02T10:24:09+00:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle import oci_ce_utils

try:
    from oci.container_engine.container_engine_client import ContainerEngineClient
    from oci.container_engine.models import CreateNodePoolDetails
    from oci.container_engine.models import UpdateNodePoolDetails
    from oci.container_engine.models import KeyValue

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def delete_node_pool(container_engine_client, module):
    result = oci_ce_utils.delete_and_wait(
        resource_type="node_pool",
        client=container_engine_client,
        get_fn=container_engine_client.get_node_pool,
        kwargs_get={"node_pool_id": module.params["node_pool_id"]},
        delete_fn=container_engine_client.delete_node_pool,
        kwargs_delete={"node_pool_id": module.params["node_pool_id"]},
        module=module,
        wait_applicable=False,
    )
    return result


def update_node_pool(container_engine_client, module):
    result = oci_ce_utils.update_and_wait(
        resource_type="node_pool",
        client=container_engine_client,
        get_fn=container_engine_client.get_node_pool,
        kwargs_get={"node_pool_id": module.params["node_pool_id"]},
        update_fn=container_engine_client.update_node_pool,
        primitive_params_update=["node_pool_id"],
        kwargs_non_primitive_update={UpdateNodePoolDetails: "update_node_pool_details"},
        module=module,
        update_attributes=UpdateNodePoolDetails().attribute_map.keys(),
    )
    return result


def create_node_pool(container_engine_client, module):
    create_node_pool_details = CreateNodePoolDetails()
    for attribute in create_node_pool_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_node_pool_details, attribute, module.params[attribute])

    node_labels = module.params["initial_node_labels"]
    if node_labels:
        initial_node_labels = []
        for d in node_labels:
            keyvalue = KeyValue()
            if d.get("key", None) and d.get("value", None):
                keyvalue.key = d.get("key")
                keyvalue.value = d.get("value")
                initial_node_labels.append(keyvalue)
        create_node_pool_details.initial_node_labels = initial_node_labels
    # Note: `wait` is "True" by default for `oci_node_pool`, unlike other resources because a node pool is only useful
    # if atleast one node in the node pool reaches ACTIVE state (Installation of Helm components are delayed until a
    # node is available).
    result = oci_ce_utils.create_and_wait(
        resource_type="node_pool",
        create_fn=container_engine_client.create_node_pool,
        kwargs_create={"create_node_pool_details": create_node_pool_details},
        client=container_engine_client,
        get_fn=container_engine_client.get_node_pool,
        get_param="node_pool_id",
        module=module,
    )
    return result


def main():
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            node_pool_id=dict(type="str", required=False, aliases=["id"]),
            cluster_id=dict(type="str", required=False),
            kubernetes_version=dict(type="str", required=False),
            name=dict(type="str", required=False),
            initial_node_labels=dict(type=list, required=False),
            subnet_ids=dict(type=list, required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            node_image_name=dict(type="str", required=False),
            node_shape=dict(type="str", required=False),
            quantity_per_subnet=dict(type="int", required=False),
            ssh_public_key=dict(type="str", required=False),
            count_of_nodes_to_wait=dict(type=int, required=False, default=1),
            wait_until=dict(type="str", required=False, default="ACTIVE"),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[("state", "absent", ["node_pool_id"])],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    container_engine_client = oci_utils.create_service_client(
        module, ContainerEngineClient
    )

    state = module.params["state"]
    node_pool_id = module.params["node_pool_id"]

    if state == "absent":
        result = delete_node_pool(container_engine_client, module)

    else:
        if node_pool_id is not None:
            result = update_node_pool(container_engine_client, module)
        else:
            kwargs_list = {"compartment_id": module.params["compartment_id"]}
            exclude_attributes = {"name": True}
            result = oci_utils.check_and_create_resource(
                resource_type="node_pool",
                create_fn=create_node_pool,
                kwargs_create={
                    "container_engine_client": container_engine_client,
                    "module": module,
                },
                list_fn=container_engine_client.list_node_pools,
                kwargs_list=kwargs_list,
                module=module,
                model=CreateNodePoolDetails(),
                exclude_attributes=exclude_attributes,
            )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
