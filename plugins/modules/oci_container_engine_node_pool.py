#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_container_engine_node_pool
short_description: Manage a NodePool resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a NodePool resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new node pool.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment in which the node pool exists.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    cluster_id:
        description:
            - The OCID of the cluster to which this node pool is attached.
            - Required for create using I(state=present).
        type: str
    name:
        description:
            - The name of the node pool. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    kubernetes_version:
        description:
            - The version of Kubernetes to install on the nodes in the node pool.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    node_metadata:
        description:
            - A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.
            - This parameter is updatable.
        type: dict
    node_image_name:
        description:
            - Deprecated. Use `nodeSourceDetails` instead.
              If you specify values for both, this value is ignored.
              The name of the image running on the nodes in the node pool.
        type: str
    node_source_details:
        description:
            - Specify the source to use to launch nodes in the node pool. Currently, image is the only supported source.
            - This parameter is updatable.
        type: dict
        suboptions:
            source_type:
                description:
                    - The source type for the node.
                      Use `IMAGE` when specifying an OCID of an image.
                type: str
                choices:
                    - "IMAGE"
                required: true
            image_id:
                description:
                    - The OCID of the image used to boot the node.
                type: str
                required: true
            boot_volume_size_in_gbs:
                description:
                    - The size of the boot volume in GBs. Minimum value is 50 GB. See L(here,https://docs.cloud.oracle.com/en-
                      us/iaas/Content/Block/Concepts/bootvolumes.htm) for max custom boot volume sizing and OS-specific requirements.
                type: int
    node_shape:
        description:
            - The name of the node shape of the nodes in the node pool.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    node_shape_config:
        description:
            - Specify the configuration of the shape to launch nodes in the node pool.
            - This parameter is updatable.
        type: dict
        suboptions:
            ocpus:
                description:
                    - The total number of OCPUs available to each node in the node pool.
                      See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                    - This parameter is updatable.
                type: float
            memory_in_gbs:
                description:
                    - The total amount of memory available to each node, in gigabytes.
                    - This parameter is updatable.
                type: float
    initial_node_labels:
        description:
            - A list of key/value pairs to add to nodes after they join the Kubernetes cluster.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            key:
                description:
                    - The key of the pair.
                type: str
            value:
                description:
                    - The value of the pair.
                type: str
    ssh_public_key:
        description:
            - The SSH public key on each node in the node pool on launch.
            - This parameter is updatable.
        type: str
    quantity_per_subnet:
        description:
            - Optional, default to 1. The number of nodes to create in each subnet specified in subnetIds property.
              When used, subnetIds is required. This property is deprecated, use nodeConfigDetails instead.
            - This parameter is updatable.
        type: int
    subnet_ids:
        description:
            - The OCIDs of the subnets in which to place nodes for this node pool. When used, quantityPerSubnet
              can be provided. This property is deprecated, use nodeConfigDetails. Exactly one of the
              subnetIds or nodeConfigDetails properties must be specified.
            - This parameter is updatable.
        type: list
        elements: str
    node_config_details:
        description:
            - The configuration of nodes in the node pool. Exactly one of the
              subnetIds or nodeConfigDetails properties must be specified.
            - This parameter is updatable.
        type: dict
        suboptions:
            size:
                description:
                    - The number of nodes that should be in the node pool.
                    - This parameter is updatable.
                type: int
            nsg_ids:
                description:
                    - The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see
                      L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                    - This parameter is updatable.
                type: list
                elements: str
            placement_configs:
                description:
                    - The placement configurations for the node pool. Provide one placement
                      configuration for each availability domain in which you intend to launch a node.
                    - To use the node pool with a regional subnet, provide a placement configuration for
                      each availability domain, and include the regional subnet in each placement
                      configuration.
                type: list
                elements: dict
                suboptions:
                    availability_domain:
                        description:
                            - "The availability domain in which to place nodes.
                              Example: `Uocm:PHX-AD-1`"
                        type: str
                        required: true
                    subnet_id:
                        description:
                            - The OCID of the subnet in which to place nodes.
                        type: str
                        required: true
    node_pool_id:
        description:
            - The OCID of the node pool.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the NodePool.
            - Use I(state=present) to create or update a NodePool.
            - Use I(state=absent) to delete a NodePool.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create node_pool
  oci_container_engine_node_pool:
    compartment_id: "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq"
    cluster_id: ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw
    name: My Node Pool
    kubernetes_version: v1.9.4
    node_shape: VM.Standard2.4

- name: Update node_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_node_pool:
    compartment_id: "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq"
    name: My Node Pool
    kubernetes_version: v1.9.4
    node_source_details:
      source_type: IMAGE
      image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    node_shape: VM.Standard2.4
    ssh_public_key: "ssh-rsa AAAAB3NzaC1yc2abc123..."
    quantity_per_subnet: 1

- name: Update node_pool
  oci_container_engine_node_pool:
    name: My Node Pool
    kubernetes_version: v1.9.4
    node_pool_id: "ocid1.nodepool.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete node_pool
  oci_container_engine_node_pool:
    node_pool_id: "ocid1.nodepool.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete node_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_node_pool:
    compartment_id: "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq"
    name: My Node Pool
    state: absent

"""

RETURN = """
node_pool:
    description:
        - Details of the NodePool resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the node pool.
            returned: on success
            type: str
            sample: ocid1.nodepool.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
        compartment_id:
            description:
                - The OCID of the compartment in which the node pool exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq"
        cluster_id:
            description:
                - The OCID of the cluster to which this node pool is attached.
            returned: on success
            type: str
            sample: ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw
        name:
            description:
                - The name of the node pool.
            returned: on success
            type: str
            sample: My Node Pool
        kubernetes_version:
            description:
                - The version of Kubernetes running on the nodes in the node pool.
            returned: on success
            type: str
            sample: v1.9.4
        node_metadata:
            description:
                - A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.
            returned: on success
            type: dict
            sample: {}
        node_image_id:
            description:
                - Deprecated. see `nodeSource`. The OCID of the image running on the nodes in the node pool.
            returned: on success
            type: str
            sample: ocid1.image.oc1.phx.aaaaaaaanclh465xnfvajjojj5bbjzqytunslgvnyvf3fepiiltalnglekoa
        node_image_name:
            description:
                - Deprecated. see `nodeSource`. The name of the image running on the nodes in the node pool.
            returned: on success
            type: str
            sample: Oracle-Linux-7.4
        node_shape_config:
            description:
                - The shape configuration of the nodes.
            returned: on success
            type: complex
            contains:
                ocpus:
                    description:
                        - The total number of OCPUs available to each node in the node pool.
                          See L(here,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/Shape/) for details.
                    returned: on success
                    type: float
                    sample: 3.4
                memory_in_gbs:
                    description:
                        - The total amount of memory available to each node, in gigabytes.
                    returned: on success
                    type: float
                    sample: 3.4
        node_source:
            description:
                - Deprecated. see `nodeSourceDetails`. Source running on the nodes in the node pool.
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - The source type of this option.
                          `IMAGE` means the OCID is of an image.
                    returned: on success
                    type: str
                    sample: IMAGE
                source_name:
                    description:
                        - The user-friendly name of the entity corresponding to the OCID.
                    returned: on success
                    type: str
                    sample: source_name_example
                image_id:
                    description:
                        - The OCID of the image.
                    returned: on success
                    type: str
                    sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        node_source_details:
            description:
                - Source running on the nodes in the node pool.
            returned: on success
            type: complex
            contains:
                source_type:
                    description:
                        - The source type for the node.
                          Use `IMAGE` when specifying an OCID of an image.
                    returned: on success
                    type: str
                    sample: IMAGE
                image_id:
                    description:
                        - The OCID of the image used to boot the node.
                    returned: on success
                    type: str
                    sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                boot_volume_size_in_gbs:
                    description:
                        - The size of the boot volume in GBs. Minimum value is 50 GB. See L(here,https://docs.cloud.oracle.com/en-
                          us/iaas/Content/Block/Concepts/bootvolumes.htm) for max custom boot volume sizing and OS-specific requirements.
                    returned: on success
                    type: int
                    sample: 56
        node_shape:
            description:
                - The name of the node shape of the nodes in the node pool.
            returned: on success
            type: str
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
                    type: str
                    sample: mykey
                value:
                    description:
                        - The value of the pair.
                    returned: on success
                    type: str
                    sample: myvalue
        ssh_public_key:
            description:
                - The SSH public key on each node in the node pool on launch.
            returned: on success
            type: str
            sample: "ssh-rsa AAAAB3NzaC1yc2abc123..."
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
                    type: str
                    sample: ocid1.instance.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgyswgycdoy3tcmtctmyw
                name:
                    description:
                        - The name of the node.
                    returned: on success
                    type: str
                    sample: My Kubernetes Node
                kubernetes_version:
                    description:
                        - The version of Kubernetes this node is running.
                    returned: on success
                    type: str
                    sample: v1.9.4
                availability_domain:
                    description:
                        - The name of the availability domain in which this node is placed.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                subnet_id:
                    description:
                        - The OCID of the subnet in which this node is placed.
                    returned: on success
                    type: str
                    sample: ocid1.subnet.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3ofzxtlyit
                node_pool_id:
                    description:
                        - The OCID of the node pool to which this node belongs.
                    returned: on success
                    type: str
                    sample: ocid1.nodepool.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq
                fault_domain:
                    description:
                        - The fault domain of this node.
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                private_ip:
                    description:
                        - The private IP address of this node.
                    returned: on success
                    type: str
                    sample: 10.0.1.1
                public_ip:
                    description:
                        - The public IP address of this node.
                    returned: on success
                    type: str
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
                            type: str
                            sample: LimitExceeded
                        message:
                            description:
                                - A human-readable error string of the upstream error.
                            returned: on success
                            type: str
                            sample: error validating payload
                        status:
                            description:
                                - The status of the HTTP response encountered in the upstream error.
                            returned: on success
                            type: str
                            sample: 429
                        opc_request_id:
                            description:
                                - Unique Oracle-assigned identifier for the upstream request. If you need to contact Oracle about a particular upstream request,
                                  please provide the request ID.
                            returned: on success
                            type: str
                            sample: BDA258F920471CFA70CF3655A836EAC3/AC26D111CE04292D5398192DCACCD85F/D74FF67547281CFA70CF3655A60B6DF5
                lifecycle_state:
                    description:
                        - The state of the node.
                    returned: on success
                    type: str
                    sample: UPDATING
                lifecycle_details:
                    description:
                        - Details about the state of the node.
                    returned: on success
                    type: str
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
                nsg_ids:
                    description:
                        - The OCIDs of the Network Security Group(s) to associate nodes for this node pool with. For more information about NSGs, see
                          L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                    returned: on success
                    type: list
                    sample: []
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
                            type: str
                            sample: Uocm:PHX-AD-1
                        subnet_id:
                            description:
                                - The OCID of the subnet in which to place nodes.
                            returned: on success
                            type: str
                            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "id": "ocid1.nodepool.oc1.iad.aaaaaaaanifpelnyzmkvnepohbz4ntswkpl35syzzsugdxceth3oihe8hcfq",
        "compartment_id": "ocid1.compartment.oc1..aaaaaaaafqm2df7ckwmmbtdsl2bgxsw4fcpvkoojytxrqst24yww2tdmtqcq",
        "cluster_id": "ocid1.cluster.oc1.iad.aaaaaaaaga3tombrmq3wgyrvmi3gcn3bmfsdizjwgy4wgyldmy3dcmtcmmyw",
        "name": "My Node Pool",
        "kubernetes_version": "v1.9.4",
        "node_metadata": {},
        "node_image_id": "ocid1.image.oc1.phx.aaaaaaaanclh465xnfvajjojj5bbjzqytunslgvnyvf3fepiiltalnglekoa",
        "node_image_name": "Oracle-Linux-7.4",
        "node_shape_config": {
            "ocpus": 3.4,
            "memory_in_gbs": 3.4
        },
        "node_source": {
            "source_type": "IMAGE",
            "source_name": "source_name_example",
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "node_source_details": {
            "source_type": "IMAGE",
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
            "boot_volume_size_in_gbs": 56
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
            "kubernetes_version": "v1.9.4",
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
            "nsg_ids": [],
            "placement_configs": [{
                "availability_domain": "Uocm:PHX-AD-1",
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
            }]
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.container_engine import ContainerEngineClient
    from oci.container_engine.models import CreateNodePoolDetails
    from oci.container_engine.models import UpdateNodePoolDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NodePoolHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "node_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("node_pool_id")

    def get_get_fn(self):
        return self.client.get_node_pool

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_node_pool,
            node_pool_id=self.module.params.get("node_pool_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["cluster_id", "name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_node_pools, **kwargs
        )

    def get_create_model_class(self):
        return CreateNodePoolDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(create_node_pool_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateNodePoolDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(
                node_pool_id=self.module.params.get("node_pool_id"),
                update_node_pool_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_node_pool,
            call_fn_args=(),
            call_fn_kwargs=dict(node_pool_id=self.module.params.get("node_pool_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


NodePoolHelperCustom = get_custom_class("NodePoolHelperCustom")


class ResourceHelper(NodePoolHelperCustom, NodePoolHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            cluster_id=dict(type="str"),
            name=dict(type="str"),
            kubernetes_version=dict(type="str"),
            node_metadata=dict(type="dict"),
            node_image_name=dict(type="str"),
            node_source_details=dict(
                type="dict",
                options=dict(
                    source_type=dict(type="str", required=True, choices=["IMAGE"]),
                    image_id=dict(type="str", required=True),
                    boot_volume_size_in_gbs=dict(type="int"),
                ),
            ),
            node_shape=dict(type="str"),
            node_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            initial_node_labels=dict(
                type="list",
                elements="dict",
                options=dict(key=dict(type="str", no_log=True), value=dict(type="str")),
            ),
            ssh_public_key=dict(type="str", no_log=True),
            quantity_per_subnet=dict(type="int"),
            subnet_ids=dict(type="list", elements="str"),
            node_config_details=dict(
                type="dict",
                options=dict(
                    size=dict(type="int"),
                    nsg_ids=dict(type="list", elements="str"),
                    placement_configs=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            availability_domain=dict(type="str", required=True),
                            subnet_id=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            node_pool_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="node_pool",
        service_client_class=ContainerEngineClient,
        namespace="container_engine",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
