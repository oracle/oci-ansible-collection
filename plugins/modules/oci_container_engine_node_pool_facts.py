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
module: oci_container_engine_node_pool_facts
short_description: Fetches details about one or multiple NodePool resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NodePool resources in Oracle Cloud Infrastructure
    - List all the node pools in a compartment, and optionally filter by cluster.
    - If I(node_pool_id) is specified, the details of a single NodePool will be returned.
version_added: "2.5"
options:
    node_pool_id:
        description:
            - The OCID of the node pool.
            - Required to get a specific node_pool.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple node_pools.
        type: str
    cluster_id:
        description:
            - The OCID of the cluster.
        type: str
    name:
        description:
            - The name to filter on.
        type: str
    sort_order:
        description:
            - The optional order in which to sort the results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The optional field to sort the results by.
        type: str
        choices:
            - "ID"
            - "NAME"
            - "TIME_CREATED"
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List node_pools
  oci_container_engine_node_pool_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific node_pool
  oci_container_engine_node_pool_facts:
    node_pool_id: ocid1.nodepool.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
node_pools:
    description:
        - List of NodePool resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the node pool.
            returned: on success
            type: string
            sample: ocid1.nodepool.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
        compartment_id:
            description:
                - The OCID of the compartment in which the node pool exists.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq
        cluster_id:
            description:
                - The OCID of the cluster to which this node pool is attached.
            returned: on success
            type: string
            sample: ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw
        name:
            description:
                - The name of the node pool.
            returned: on success
            type: string
            sample: My Node Pool
        kubernetes_version:
            description:
                - The version of Kubernetes running on the nodes in the node pool.
            returned: on success
            type: string
            sample: v1.9.4
        node_metadata:
            description:
                - A list of key/value pairs to add to each underlying OCI instance in the node pool.
            returned: on success
            type: dict
            sample: {}
        node_image_id:
            description:
                - Deprecated. see `nodeSource`. The OCID of the image running on the nodes in the node pool.
            returned: on success
            type: string
            sample: ocid1.image.oc1.phx.aaaaaaaanclh465xnfvajjojj5bbjzqytunslgvnyvf3fepiiltalnglekoa
        node_image_name:
            description:
                - Deprecated. see `nodeSource`. The name of the image running on the nodes in the node pool.
            returned: on success
            type: string
            sample: Oracle-Linux-7.4
        node_source:
            description:
                - Source running on the nodes in the node pool.
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
                    sample: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
        node_shape:
            description:
                - The name of the node shape of the nodes in the node pool.
            returned: on success
            type: string
            sample: VM.Standard2.4
        initial_node_labels:
            description:
                - A list of key/value pairs to add to nodes after they join the Kubernetes cluster.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - The key of the pair.
                    returned: on success
                    type: string
                    sample: mykey
                value:
                    description:
                        - The value of the pair.
                    returned: on success
                    type: string
                    sample: myvalue
        ssh_public_key:
            description:
                - The SSH public key on each node in the node pool.
            returned: on success
            type: string
            sample: ssh-rsa AAAAB3NzaC1yc2abc123...
        quantity_per_subnet:
            description:
                - The number of nodes in each subnet.
            returned: on success
            type: int
            sample: 1
        subnet_ids:
            description:
                - The OCIDs of the subnets in which to place nodes for this node pool.
            returned: on success
            type: list
            sample: []
        nodes:
            description:
                - The nodes in the node pool.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the compute instance backing this node.
                    returned: on success
                    type: string
                    sample: ocid1.instance.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgyswgycdoy3tcmtctmyw
                name:
                    description:
                        - The name of the node.
                    returned: on success
                    type: string
                    sample: My Kubernetes Node
                availability_domain:
                    description:
                        - The name of the availability domain in which this node is placed.
                    returned: on success
                    type: string
                    sample: Uocm:PHX-AD-1
                subnet_id:
                    description:
                        - The OCID of the subnet in which this node is placed.
                    returned: on success
                    type: string
                    sample: ocid1.subnet.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3ofzxtlyit
                node_pool_id:
                    description:
                        - The OCID of the node pool to which this node belongs.
                    returned: on success
                    type: string
                    sample: ocid1.nodepool.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                fault_domain:
                    description:
                        - The fault domain of this node.
                    returned: on success
                    type: string
                    sample: FAULT-DOMAIN-1
                private_ip:
                    description:
                        - The private IP address of this node.
                    returned: on success
                    type: string
                    sample: 10.0.1.1
                public_ip:
                    description:
                        - The public IP address of this node.
                    returned: on success
                    type: string
                    sample: 129.1.2.3
                node_error:
                    description:
                        - An error that may be associated with the node.
                    returned: on success
                    type: complex
                    contains:
                        code:
                            description:
                                - A short error code that defines the upstream error, meant for programmatic parsing. See L(API Errors,https://docs.us-
                                  phoenix-1.oraclecloud.com/Content/API/References/apierrors.htm).
                            returned: on success
                            type: string
                            sample: LimitExceeded
                        message:
                            description:
                                - A human-readable error string of the upstream error.
                            returned: on success
                            type: string
                            sample: error validating payload
                        status:
                            description:
                                - The status of the HTTP response encountered in the upstream error.
                            returned: on success
                            type: string
                            sample: 429
                        opc_request_id:
                            description:
                                - Unique Oracle-assigned identifier for the upstream request. If you need to contact Oracle about a particular upstream request,
                                  please provide the request ID.
                            returned: on success
                            type: string
                            sample: BDA258F920471CFA70CF3655A836EAC3/AC26D111CE04292D5398192DCACCD85F/D74FF67547281CFA70CF3655A60B6DF5
                lifecycle_state:
                    description:
                        - The state of the node.
                    returned: on success
                    type: string
                    sample: UPDATING
                lifecycle_details:
                    description:
                        - Details about the state of the node.
                    returned: on success
                    type: string
                    sample: waiting for SSH
        node_config_details:
            description:
                - The configuration of nodes in the node pool.
            returned: on success
            type: complex
            contains:
                size:
                    description:
                        - The number of nodes in the node pool.
                    returned: on success
                    type: int
                    sample: 56
                placement_configs:
                    description:
                        - The placement configurations for the node pool. Provide one placement
                          configuration for each availability domain in which you intend to launch a node.
                        - To use the node pool with a regional subnet, provide a placement configuration for
                          each availability domain, and include the regional subnet in each placement
                          configuration.
                    returned: on success
                    type: complex
                    contains:
                        availability_domain:
                            description:
                                - "The availability domain in which to place nodes.
                                  Example: `Uocm:PHX-AD-1`"
                            returned: on success
                            type: string
                            sample: Uocm:PHX-AD-1
                        subnet_id:
                            description:
                                - The OCID of the subnet in which to place nodes.
                            returned: on success
                            type: string
                            sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
        "id": "ocid1.nodepool.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq",
        "compartment_id": "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq",
        "cluster_id": "ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw",
        "name": "My Node Pool",
        "kubernetes_version": "v1.9.4",
        "node_metadata": {},
        "node_image_id": "ocid1.image.oc1.phx.aaaaaaaanclh465xnfvajjojj5bbjzqytunslgvnyvf3fepiiltalnglekoa",
        "node_image_name": "Oracle-Linux-7.4",
        "node_source": {
            "source_type": "IMAGE",
            "source_name": "source_name_example",
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "node_shape": "VM.Standard2.4",
        "initial_node_labels": [{
            "key": "mykey",
            "value": "myvalue"
        }],
        "ssh_public_key": "ssh-rsa AAAAB3NzaC1yc2abc123...",
        "quantity_per_subnet": 1,
        "subnet_ids": [],
        "nodes": [{
            "id": "ocid1.instance.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgyswgycdoy3tcmtctmyw",
            "name": "My Kubernetes Node",
            "availability_domain": "Uocm:PHX-AD-1",
            "subnet_id": "ocid1.subnet.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3ofzxtlyit",
            "node_pool_id": "ocid1.nodepool.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq",
            "fault_domain": "FAULT-DOMAIN-1",
            "private_ip": "10.0.1.1",
            "public_ip": "129.1.2.3",
            "node_error": {
                "code": "LimitExceeded",
                "message": "error validating payload",
                "status": "429",
                "opc_request_id": "BDA258F920471CFA70CF3655A836EAC3/AC26D111CE04292D5398192DCACCD85F/D74FF67547281CFA70CF3655A60B6DF5"
            },
            "lifecycle_state": "UPDATING",
            "lifecycle_details": "waiting for SSH"
        }],
        "node_config_details": {
            "size": 56,
            "placement_configs": [{
                "availability_domain": "Uocm:PHX-AD-1",
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }
    }]
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


class NodePoolFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "node_pool_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_node_pool,
            node_pool_id=self.module.params.get("node_pool_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "cluster_id",
            "name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_node_pools,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


NodePoolFactsHelperCustom = get_custom_class("NodePoolFactsHelperCustom")


class ResourceFactsHelper(NodePoolFactsHelperCustom, NodePoolFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            node_pool_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            cluster_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ID", "NAME", "TIME_CREATED"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="node_pool",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(node_pools=result)


if __name__ == "__main__":
    main()
