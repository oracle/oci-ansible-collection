#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
    node_image_name:
        description:
            - Deprecated. Use `nodeSourceDetails` instead.
              If you specify values for both, this value is ignored.
              The name of the image running on the nodes in the node pool.
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
            - This parameter is updatable.
        type: str
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
            kms_key_id:
                description:
                    - The OCID of the Key Management Service key assigned to the boot volume.
                    - This parameter is updatable.
                type: str
            is_pv_encryption_in_transit_enabled:
                description:
                    - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and
                      boot volumes. The default value is false.
                    - This parameter is updatable.
                type: bool
            freeform_tags:
                description:
                    - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                      Example: `{\\"Department\\": \\"Finance\\"}`"
                    - This parameter is updatable.
                type: dict
            defined_tags:
                description:
                    - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                      Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    - This parameter is updatable.
                type: dict
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
                    capacity_reservation_id:
                        description:
                            - The OCID of the compute capacity reservation in which to place the compute instance.
                        type: str
                    preemptible_node_config:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            preemption_action:
                                description:
                                    - ""
                                type: dict
                                required: true
                                suboptions:
                                    type:
                                        description:
                                            - The type of action to run when the instance is interrupted for eviction.
                                        type: str
                                        choices:
                                            - "TERMINATE"
                                        required: true
                                    is_preserve_boot_volume:
                                        description:
                                            - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is
                                              terminated. Defaults to false if not specified.
                                        type: bool
                    fault_domains:
                        description:
                            - A list of fault domains in which to place nodes.
                        type: list
                        elements: str
            node_pool_pod_network_option_details:
                description:
                    - The CNI related configuration of pods in the node pool.
                type: dict
                suboptions:
                    max_pods_per_node:
                        description:
                            - The max number of pods per node in the node pool. This value will be limited by the number of VNICs attachable to the node pool
                              shape
                            - Applicable when cni_type is 'OCI_VCN_IP_NATIVE'
                        type: int
                    pod_nsg_ids:
                        description:
                            - The OCIDs of the Network Security Group(s) to associate pods for this node pool with. For more information about NSGs, see
                              L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                            - Applicable when cni_type is 'OCI_VCN_IP_NATIVE'
                        type: list
                        elements: str
                    pod_subnet_ids:
                        description:
                            - The OCIDs of the subnets in which to place pods for this node pool. This can be one of the node pool subnet IDs
                            - Required when cni_type is 'OCI_VCN_IP_NATIVE'
                        type: list
                        elements: str
                    cni_type:
                        description:
                            - The CNI plugin used by this node pool
                        type: str
                        choices:
                            - "OCI_VCN_IP_NATIVE"
                            - "FLANNEL_OVERLAY"
                        required: true
    node_metadata:
        description:
            - A list of key/value pairs to add to each underlying OCI instance in the node pool on launch.
            - This parameter is updatable.
        type: dict
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
    ssh_public_key:
        description:
            - The SSH public key on each node in the node pool on launch.
            - This parameter is updatable.
        type: str
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
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    node_eviction_node_pool_settings:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            eviction_grace_duration:
                description:
                    - "Duration after which OKE will give up eviction of the pods on the node. PT0M will indicate you want to delete the node without cordon and
                      drain.
                      Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M"
                type: str
            is_force_delete_after_grace_duration:
                description:
                    - If the underlying compute instance should be deleted if you cannot evict all the pods in grace period
                type: bool
    node_pool_cycling_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            maximum_unavailable:
                description:
                    - Maximum active nodes that would be terminated from nodepool during the cycling nodepool process.
                      OKE supports both integer and percentage input.
                      Defaults to 0, Ranges from 0 to Nodepool size or 0% to 100%
                type: str
            maximum_surge:
                description:
                    - Maximum additional new compute instances that would be temporarily created and added to nodepool during the cycling nodepool process.
                      OKE supports both integer and percentage input.
                      Defaults to 1, Ranges from 0 to Nodepool size or 0% to 100%
                type: str
            is_node_cycling_enabled:
                description:
                    - If nodes in the nodepool will be cycled to have new changes.
                type: bool
    node_pool_id:
        description:
            - The OCID of the node pool.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    override_eviction_grace_duration:
        description:
            - "Duration after which OKE will give up eviction of the pods on the node.
              PT0M will indicate you want to delete the node without cordon and drain. Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M"
            - This parameter is updatable.
        type: str
    is_force_deletion_after_override_grace_duration:
        description:
            - If the underlying compute instance should be deleted if you cannot evict all the pods in grace period
            - This parameter is updatable.
        type: bool
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
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    node_shape: node_shape_example

    # optional
    node_image_name: node_image_name_example
    kubernetes_version: kubernetes_version_example
    initial_node_labels:
    - # optional
      key: key_example
      value: value_example
    quantity_per_subnet: 56
    subnet_ids: [ "subnet_ids_example" ]
    node_config_details:
      # optional
      size: 56
      nsg_ids: [ "nsg_ids_example" ]
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
      is_pv_encryption_in_transit_enabled: true
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      placement_configs:
      - # required
        availability_domain: Uocm:PHX-AD-1
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
        preemptible_node_config:
          # required
          preemption_action:
            # required
            type: TERMINATE

            # optional
            is_preserve_boot_volume: true
        fault_domains: [ "fault_domains_example" ]
      node_pool_pod_network_option_details:
        # required
        pod_subnet_ids: [ "pod_subnet_ids_example" ]
        cni_type: OCI_VCN_IP_NATIVE

        # optional
        max_pods_per_node: 56
        pod_nsg_ids: [ "pod_nsg_ids_example" ]
    node_metadata: null
    node_source_details:
      # required
      source_type: IMAGE
      image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      boot_volume_size_in_gbs: 56
    ssh_public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
    node_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    node_eviction_node_pool_settings:
      # optional
      eviction_grace_duration: eviction_grace_duration_example
      is_force_delete_after_grace_duration: true
    node_pool_cycling_details:
      # optional
      maximum_unavailable: maximum_unavailable_example
      maximum_surge: maximum_surge_example
      is_node_cycling_enabled: true

- name: Update node_pool
  oci_container_engine_node_pool:
    # required
    node_pool_id: "ocid1.nodepool.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    kubernetes_version: kubernetes_version_example
    initial_node_labels:
    - # optional
      key: key_example
      value: value_example
    quantity_per_subnet: 56
    subnet_ids: [ "subnet_ids_example" ]
    node_config_details:
      # optional
      size: 56
      nsg_ids: [ "nsg_ids_example" ]
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
      is_pv_encryption_in_transit_enabled: true
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      placement_configs:
      - # required
        availability_domain: Uocm:PHX-AD-1
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
        preemptible_node_config:
          # required
          preemption_action:
            # required
            type: TERMINATE

            # optional
            is_preserve_boot_volume: true
        fault_domains: [ "fault_domains_example" ]
      node_pool_pod_network_option_details:
        # required
        pod_subnet_ids: [ "pod_subnet_ids_example" ]
        cni_type: OCI_VCN_IP_NATIVE

        # optional
        max_pods_per_node: 56
        pod_nsg_ids: [ "pod_nsg_ids_example" ]
    node_metadata: null
    node_source_details:
      # required
      source_type: IMAGE
      image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      boot_volume_size_in_gbs: 56
    ssh_public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
    node_shape: node_shape_example
    node_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    node_eviction_node_pool_settings:
      # optional
      eviction_grace_duration: eviction_grace_duration_example
      is_force_delete_after_grace_duration: true
    node_pool_cycling_details:
      # optional
      maximum_unavailable: maximum_unavailable_example
      maximum_surge: maximum_surge_example
      is_node_cycling_enabled: true
    override_eviction_grace_duration: override_eviction_grace_duration_example
    is_force_deletion_after_override_grace_duration: true

- name: Update node_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_node_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    kubernetes_version: kubernetes_version_example
    initial_node_labels:
    - # optional
      key: key_example
      value: value_example
    quantity_per_subnet: 56
    subnet_ids: [ "subnet_ids_example" ]
    node_config_details:
      # optional
      size: 56
      nsg_ids: [ "nsg_ids_example" ]
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
      is_pv_encryption_in_transit_enabled: true
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      placement_configs:
      - # required
        availability_domain: Uocm:PHX-AD-1
        subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
        capacity_reservation_id: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
        preemptible_node_config:
          # required
          preemption_action:
            # required
            type: TERMINATE

            # optional
            is_preserve_boot_volume: true
        fault_domains: [ "fault_domains_example" ]
      node_pool_pod_network_option_details:
        # required
        pod_subnet_ids: [ "pod_subnet_ids_example" ]
        cni_type: OCI_VCN_IP_NATIVE

        # optional
        max_pods_per_node: 56
        pod_nsg_ids: [ "pod_nsg_ids_example" ]
    node_metadata: null
    node_source_details:
      # required
      source_type: IMAGE
      image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      boot_volume_size_in_gbs: 56
    ssh_public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
    node_shape: node_shape_example
    node_shape_config:
      # optional
      ocpus: 3.4
      memory_in_gbs: 3.4
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    node_eviction_node_pool_settings:
      # optional
      eviction_grace_duration: eviction_grace_duration_example
      is_force_delete_after_grace_duration: true
    node_pool_cycling_details:
      # optional
      maximum_unavailable: maximum_unavailable_example
      maximum_surge: maximum_surge_example
      is_node_cycling_enabled: true
    override_eviction_grace_duration: override_eviction_grace_duration_example
    is_force_deletion_after_override_grace_duration: true

- name: Delete node_pool
  oci_container_engine_node_pool:
    # required
    node_pool_id: "ocid1.nodepool.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    override_eviction_grace_duration: override_eviction_grace_duration_example
    is_force_deletion_after_override_grace_duration: true

- name: Delete node_pool using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_container_engine_node_pool:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
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
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The state of the nodepool.
            returned: on success
            type: str
            sample: DELETED
        lifecycle_details:
            description:
                - Details about the state of the nodepool.
            returned: on success
            type: str
            sample: lifecycle_details_example
        compartment_id:
            description:
                - The OCID of the compartment in which the node pool exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_id:
            description:
                - The OCID of the cluster to which this node pool is attached.
            returned: on success
            type: str
            sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the node pool.
            returned: on success
            type: str
            sample: name_example
        kubernetes_version:
            description:
                - The version of Kubernetes running on the nodes in the node pool.
            returned: on success
            type: str
            sample: kubernetes_version_example
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
            sample: "ocid1.nodeimage.oc1..xxxxxxEXAMPLExxxxxx"
        node_image_name:
            description:
                - Deprecated. see `nodeSource`. The name of the image running on the nodes in the node pool.
            returned: on success
            type: str
            sample: node_image_name_example
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
            sample: node_shape_example
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
                    sample: key_example
                value:
                    description:
                        - The value of the pair.
                    returned: on success
                    type: str
                    sample: value_example
        ssh_public_key:
            description:
                - The SSH public key on each node in the node pool on launch.
            returned: on success
            type: str
            sample: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
        quantity_per_subnet:
            description:
                - The number of nodes in each subnet.
            returned: on success
            type: int
            sample: 56
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
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the node.
                    returned: on success
                    type: str
                    sample: name_example
                kubernetes_version:
                    description:
                        - The version of Kubernetes this node is running.
                    returned: on success
                    type: str
                    sample: kubernetes_version_example
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
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                node_pool_id:
                    description:
                        - The OCID of the node pool to which this node belongs.
                    returned: on success
                    type: str
                    sample: "ocid1.nodepool.oc1..xxxxxxEXAMPLExxxxxx"
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
                    sample: private_ip_example
                public_ip:
                    description:
                        - The public IP address of this node.
                    returned: on success
                    type: str
                    sample: public_ip_example
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
                            sample: code_example
                        message:
                            description:
                                - A human-readable error string of the upstream error.
                            returned: on success
                            type: str
                            sample: message_example
                        status:
                            description:
                                - The status of the HTTP response encountered in the upstream error.
                            returned: on success
                            type: str
                            sample: status_example
                        opc_request_id:
                            description:
                                - Unique Oracle-assigned identifier for the upstream request. If you need to contact Oracle about a particular upstream request,
                                  please provide the request ID.
                            returned: on success
                            type: str
                            sample: "ocid1.opcrequest.oc1..xxxxxxEXAMPLExxxxxx"
                freeform_tags:
                    description:
                        - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
                system_tags:
                    description:
                        - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                          Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
                    returned: on success
                    type: dict
                    sample: {}
                lifecycle_state:
                    description:
                        - The state of the node.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - Details about the state of the node.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
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
                kms_key_id:
                    description:
                        - The OCID of the Key Management Service key assigned to the boot volume.
                    returned: on success
                    type: str
                    sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
                is_pv_encryption_in_transit_enabled:
                    description:
                        - Whether to enable in-transit encryption for the data volume's paravirtualized attachment. This field applies to both block volumes and
                          boot volumes. The default value is false.
                    returned: on success
                    type: bool
                    sample: true
                freeform_tags:
                    description:
                        - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
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
                        capacity_reservation_id:
                            description:
                                - The OCID of the compute capacity reservation in which to place the compute instance.
                            returned: on success
                            type: str
                            sample: "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx"
                        preemptible_node_config:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                preemption_action:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        type:
                                            description:
                                                - The type of action to run when the instance is interrupted for eviction.
                                            returned: on success
                                            type: str
                                            sample: TERMINATE
                                        is_preserve_boot_volume:
                                            description:
                                                - Whether to preserve the boot volume that was used to launch the preemptible instance when the instance is
                                                  terminated. Defaults to false if not specified.
                                            returned: on success
                                            type: bool
                                            sample: true
                        fault_domains:
                            description:
                                - A list of fault domains in which to place nodes.
                            returned: on success
                            type: list
                            sample: []
                node_pool_pod_network_option_details:
                    description:
                        - The CNI related configuration of pods in the node pool.
                    returned: on success
                    type: complex
                    contains:
                        cni_type:
                            description:
                                - The CNI plugin used by this node pool
                            returned: on success
                            type: str
                            sample: OCI_VCN_IP_NATIVE
                        max_pods_per_node:
                            description:
                                - The max number of pods per node in the node pool. This value will be limited by the number of VNICs attachable to the node
                                  pool shape
                            returned: on success
                            type: int
                            sample: 56
                        pod_nsg_ids:
                            description:
                                - The OCIDs of the Network Security Group(s) to associate pods for this node pool with. For more information about NSGs, see
                                  L(NetworkSecurityGroup,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/NetworkSecurityGroup/).
                            returned: on success
                            type: list
                            sample: []
                        pod_subnet_ids:
                            description:
                                - The OCIDs of the subnets in which to place pods for this node pool. This can be one of the node pool subnet IDs
                            returned: on success
                            type: list
                            sample: []
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        node_eviction_node_pool_settings:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                eviction_grace_duration:
                    description:
                        - "Duration after which OKE will give up eviction of the pods on the node. PT0M will indicate you want to delete the node without cordon
                          and drain.
                          Default PT60M, Min PT0M, Max: PT60M. Format ISO 8601 e.g PT30M"
                    returned: on success
                    type: str
                    sample: eviction_grace_duration_example
                is_force_delete_after_grace_duration:
                    description:
                        - If the underlying compute instance should be deleted if you cannot evict all the pods in grace period
                    returned: on success
                    type: bool
                    sample: true
        node_pool_cycling_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                maximum_unavailable:
                    description:
                        - Maximum active nodes that would be terminated from nodepool during the cycling nodepool process.
                          OKE supports both integer and percentage input.
                          Defaults to 0, Ranges from 0 to Nodepool size or 0% to 100%
                    returned: on success
                    type: str
                    sample: maximum_unavailable_example
                maximum_surge:
                    description:
                        - Maximum additional new compute instances that would be temporarily created and added to nodepool during the cycling nodepool process.
                          OKE supports both integer and percentage input.
                          Defaults to 1, Ranges from 0 to Nodepool size or 0% to 100%
                    returned: on success
                    type: str
                    sample: maximum_surge_example
                is_node_cycling_enabled:
                    description:
                        - If nodes in the nodepool will be cycled to have new changes.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "DELETED",
        "lifecycle_details": "lifecycle_details_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "kubernetes_version": "kubernetes_version_example",
        "node_metadata": {},
        "node_image_id": "ocid1.nodeimage.oc1..xxxxxxEXAMPLExxxxxx",
        "node_image_name": "node_image_name_example",
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
        "node_shape": "node_shape_example",
        "initial_node_labels": [{
            "key": "key_example",
            "value": "value_example"
        }],
        "ssh_public_key": "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz...",
        "quantity_per_subnet": 56,
        "subnet_ids": [],
        "nodes": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "kubernetes_version": "kubernetes_version_example",
            "availability_domain": "Uocm:PHX-AD-1",
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "node_pool_id": "ocid1.nodepool.oc1..xxxxxxEXAMPLExxxxxx",
            "fault_domain": "FAULT-DOMAIN-1",
            "private_ip": "private_ip_example",
            "public_ip": "public_ip_example",
            "node_error": {
                "code": "code_example",
                "message": "message_example",
                "status": "status_example",
                "opc_request_id": "ocid1.opcrequest.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "system_tags": {},
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example"
        }],
        "node_config_details": {
            "size": 56,
            "nsg_ids": [],
            "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
            "is_pv_encryption_in_transit_enabled": true,
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "placement_configs": [{
                "availability_domain": "Uocm:PHX-AD-1",
                "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
                "capacity_reservation_id": "ocid1.capacityreservation.oc1..xxxxxxEXAMPLExxxxxx",
                "preemptible_node_config": {
                    "preemption_action": {
                        "type": "TERMINATE",
                        "is_preserve_boot_volume": true
                    }
                },
                "fault_domains": []
            }],
            "node_pool_pod_network_option_details": {
                "cni_type": "OCI_VCN_IP_NATIVE",
                "max_pods_per_node": 56,
                "pod_nsg_ids": [],
                "pod_subnet_ids": []
            }
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "node_eviction_node_pool_settings": {
            "eviction_grace_duration": "eviction_grace_duration_example",
            "is_force_delete_after_grace_duration": true
        },
        "node_pool_cycling_details": {
            "maximum_unavailable": "maximum_unavailable_example",
            "maximum_surge": "maximum_surge_example",
            "is_node_cycling_enabled": true
        }
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
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

    def get_possible_entity_types(self):
        return super(NodePoolHelperGen, self).get_possible_entity_types() + [
            "nodepool",
            "nodepools",
            "containerEnginenodepool",
            "containerEnginenodepools",
            "nodepoolresource",
            "nodepoolsresource",
            "containerengine",
        ]

    def get_module_resource_id_param(self):
        return "node_pool_id"

    def get_module_resource_id(self):
        return self.module.params.get("node_pool_id")

    def get_get_fn(self):
        return self.client.get_node_pool

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_node_pool, node_pool_id=summary_model.id,
        ).data

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
                override_eviction_grace_duration=self.module.params.get(
                    "override_eviction_grace_duration"
                ),
                is_force_deletion_after_override_grace_duration=self.module.params.get(
                    "is_force_deletion_after_override_grace_duration"
                ),
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
            call_fn_kwargs=dict(
                node_pool_id=self.module.params.get("node_pool_id"),
                override_eviction_grace_duration=self.module.params.get(
                    "override_eviction_grace_duration"
                ),
                is_force_deletion_after_override_grace_duration=self.module.params.get(
                    "is_force_deletion_after_override_grace_duration"
                ),
            ),
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
            node_image_name=dict(type="str"),
            name=dict(type="str"),
            kubernetes_version=dict(type="str"),
            initial_node_labels=dict(
                type="list",
                elements="dict",
                options=dict(key=dict(type="str", no_log=True), value=dict(type="str")),
            ),
            quantity_per_subnet=dict(type="int"),
            subnet_ids=dict(type="list", elements="str"),
            node_config_details=dict(
                type="dict",
                options=dict(
                    size=dict(type="int"),
                    nsg_ids=dict(type="list", elements="str"),
                    kms_key_id=dict(type="str"),
                    is_pv_encryption_in_transit_enabled=dict(type="bool"),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                    placement_configs=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            availability_domain=dict(type="str", required=True),
                            subnet_id=dict(type="str", required=True),
                            capacity_reservation_id=dict(type="str"),
                            preemptible_node_config=dict(
                                type="dict",
                                options=dict(
                                    preemption_action=dict(
                                        type="dict",
                                        required=True,
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=["TERMINATE"],
                                            ),
                                            is_preserve_boot_volume=dict(type="bool"),
                                        ),
                                    )
                                ),
                            ),
                            fault_domains=dict(type="list", elements="str"),
                        ),
                    ),
                    node_pool_pod_network_option_details=dict(
                        type="dict",
                        options=dict(
                            max_pods_per_node=dict(type="int"),
                            pod_nsg_ids=dict(type="list", elements="str"),
                            pod_subnet_ids=dict(type="list", elements="str"),
                            cni_type=dict(
                                type="str",
                                required=True,
                                choices=["OCI_VCN_IP_NATIVE", "FLANNEL_OVERLAY"],
                            ),
                        ),
                    ),
                ),
            ),
            node_metadata=dict(type="dict"),
            node_source_details=dict(
                type="dict",
                options=dict(
                    source_type=dict(type="str", required=True, choices=["IMAGE"]),
                    image_id=dict(type="str", required=True),
                    boot_volume_size_in_gbs=dict(type="int"),
                ),
            ),
            ssh_public_key=dict(type="str", no_log=True),
            node_shape=dict(type="str"),
            node_shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="float"), memory_in_gbs=dict(type="float")
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            node_eviction_node_pool_settings=dict(
                type="dict",
                options=dict(
                    eviction_grace_duration=dict(type="str"),
                    is_force_delete_after_grace_duration=dict(type="bool"),
                ),
            ),
            node_pool_cycling_details=dict(
                type="dict",
                options=dict(
                    maximum_unavailable=dict(type="str"),
                    maximum_surge=dict(type="str"),
                    is_node_cycling_enabled=dict(type="bool"),
                ),
            ),
            node_pool_id=dict(aliases=["id"], type="str"),
            override_eviction_grace_duration=dict(type="str"),
            is_force_deletion_after_override_grace_duration=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
