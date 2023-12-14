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
module: oci_bds_instance_actions
short_description: Perform actions on a BdsInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BdsInstance resource in Oracle Cloud Infrastructure
    - For I(action=add_block_storage), adds block storage to existing worker/compute only worker nodes. The same amount of  storage will be added to all
      worker/compute only worker nodes. No change will be made to storage that is already attached. Block storage cannot be removed.
    - For I(action=add_cloud_sql), adds Cloud SQL to your cluster. You can use Cloud SQL to query against non-relational data stored in multiple big data
      sources, including Apache Hive, HDFS, Oracle NoSQL Database, and Apache HBase. Adding Cloud SQL adds a query server node to the cluster and creates cell
      servers on all the worker nodes in the cluster.
    - For I(action=add_kafka), adds Kafka to a cluster.
    - For I(action=add_master_nodes), increases the size (scales out) of a cluster by adding master nodes. The added master nodes will have the same shape and
      will have the same amount of attached block storage as other master nodes in the cluster.
    - For I(action=add_utility_nodes), increases the size (scales out) of a cluster by adding utility nodes. The added utility nodes will have the same shape
      and will have the same amount of attached block storage as other utility nodes in the cluster.
    - For I(action=add_worker_nodes), increases the size (scales out) a cluster by adding worker nodes(data/compute). The added worker nodes will have the same
      shape and will have the same amount of attached block storage as other worker nodes in the cluster.
    - For I(action=certificate_service_info), a list of services and their certificate details.
    - For I(action=change_compartment), moves a Big Data Service cluster into a different compartment.
    - For I(action=change_shape), changes the size of a cluster by scaling up or scaling down the nodes. Nodes are scaled up or down by changing the shapes of
      all the nodes of the same type to the next larger or smaller shape. The node types are master, utility, worker, and Cloud SQL. Only nodes with VM-STANDARD
      shapes can be scaled.
    - For I(action=disable_certificate), disabling TLS/SSL for various ODH services running on the BDS cluster.
    - For I(action=enable_certificate), configuring TLS/SSL for various ODH services running on the BDS cluster.
    - For I(action=execute_bootstrap_script), execute bootstrap script.
    - For I(action=get_os_patch_details), get the details of an os patch
    - For I(action=install_os_patch), install an os patch on a cluster
    - For I(action=install_patch), install the specified patch to this cluster.
    - For I(action=list_os_patches), list all available os patches for a given cluster
    - For I(action=remove_cloud_sql), removes Cloud SQL from the cluster.
    - For I(action=remove_kafka), remove Kafka from the cluster.
    - For I(action=remove_node), remove a single node of a Big Data Service cluster
    - For I(action=renew_certificate), renewing TLS/SSL for various ODH services running on the BDS cluster.
    - For I(action=restart_node), restarts a single node of a Big Data Service cluster
    - For I(action=start), starts the BDS cluster that was stopped earlier.
    - For I(action=stop), stops the BDS cluster that can be started at later point of time.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    number_of_kafka_nodes:
        description:
            - Number of Kafka nodes for the cluster.
            - Required for I(action=add_kafka).
        type: int
    number_of_master_nodes:
        description:
            - Number of additional master nodes for the cluster.
            - Required for I(action=add_master_nodes).
        type: int
    number_of_utility_nodes:
        description:
            - Number of additional utility nodes for the cluster.
            - Required for I(action=add_utility_nodes).
        type: int
    number_of_worker_nodes:
        description:
            - Number of additional worker nodes for the cluster.
            - Required for I(action=add_worker_nodes).
        type: int
    node_type:
        description:
            - Worker node types.
            - Required for I(action=add_block_storage), I(action=add_worker_nodes).
        type: str
        choices:
            - "WORKER"
            - "COMPUTE_ONLY_WORKER"
            - "KAFKA_BROKER"
            - "EDGE"
    shape:
        description:
            - Shape of the node.
            - Required for I(action=add_cloud_sql), I(action=add_kafka).
        type: str
    block_volume_size_in_gbs:
        description:
            - The size of block volume in GB to be added to each worker node. All the
              details needed for attaching the block volume are managed by service itself.
            - Required for I(action=add_block_storage).
        type: int
    shape_config:
        description:
            - ""
            - Applicable only for I(action=add_cloud_sql)I(action=add_kafka)I(action=add_master_nodes)I(action=add_utility_nodes)I(action=add_worker_nodes).
        type: dict
        suboptions:
            ocpus:
                description:
                    - The total number of OCPUs available to the node.
                type: int
            memory_in_gbs:
                description:
                    - The total amount of memory available to the node, in gigabytes.
                type: int
            nvmes:
                description:
                    - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                type: int
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for I(action=change_compartment).
        type: str
    nodes:
        description:
            - ""
            - Required for I(action=change_shape).
        type: dict
        suboptions:
            worker:
                description:
                    - Change shape of worker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.
                type: str
            worker_shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the node.
                        type: int
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the node, in gigabytes.
                        type: int
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                        type: int
            compute_only_worker:
                description:
                    - Change shape of compute only worker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.
                type: str
            compute_only_worker_shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the node.
                        type: int
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the node, in gigabytes.
                        type: int
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                        type: int
            master:
                description:
                    - Change shape of master nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.
                type: str
            master_shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the node.
                        type: int
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the node, in gigabytes.
                        type: int
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                        type: int
            utility:
                description:
                    - Change shape of utility nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.
                type: str
            utility_shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the node.
                        type: int
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the node, in gigabytes.
                        type: int
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                        type: int
            cloudsql:
                description:
                    - Change shape of the Cloud SQL node to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.
                type: str
            cloudsql_shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the node.
                        type: int
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the node, in gigabytes.
                        type: int
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                        type: int
            edge:
                description:
                    - Change shape of edge nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.
                type: str
            edge_shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the node.
                        type: int
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the node, in gigabytes.
                        type: int
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                        type: int
            kafka_broker:
                description:
                    - Change shape of Kafka Broker nodes to the desired target shape. Both VM_STANDARD and E4 Flex shapes are allowed here.
                type: str
            kafka_broker_shape_config:
                description:
                    - ""
                type: dict
                suboptions:
                    ocpus:
                        description:
                            - The total number of OCPUs available to the node.
                        type: int
                    memory_in_gbs:
                        description:
                            - The total amount of memory available to the node, in gigabytes.
                        type: int
                    nvmes:
                        description:
                            - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                        type: int
    bootstrap_script_url:
        description:
            - pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed.
            - Applicable only for I(action=execute_bootstrap_script).
        type: str
    os_patch_version:
        description:
            - The version of the OS patch.
            - Required for I(action=get_os_patch_details), I(action=install_os_patch).
        type: str
    version:
        description:
            - The version of the patch to be installed.
            - Required for I(action=install_patch).
        type: str
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
            - Applicable only for I(action=list_os_patches).
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
            - Applicable only for I(action=list_os_patches).
        type: str
        choices:
            - "ASC"
            - "DESC"
    is_force_remove_enabled:
        description:
            - Boolean flag specifying whether or not to force remove node if graceful
              removal fails.
            - Applicable only for I(action=remove_node).
        type: bool
    services:
        description:
            - List of services for which TLS/SSL needs to be enabled.
            - Required for I(action=certificate_service_info), I(action=disable_certificate), I(action=enable_certificate).
        type: list
        elements: str
    root_certificate:
        description:
            - Plain text certificate/s in order, separated by new line character. If not provided in request a self-signed root certificate is generated inside
              the cluster. In case hostCertDetails is provided, root certificate is mandatory.
            - Applicable only for I(action=enable_certificate)I(action=renew_certificate).
        type: str
    host_cert_details:
        description:
            - List of leaf certificates to use for services on each host. If custom host certificate is provided the root certificate becomes required.
            - Applicable only for I(action=enable_certificate)I(action=renew_certificate).
        type: list
        elements: dict
        suboptions:
            host_name:
                description:
                    - Fully qualified domain name (FQDN) of the host
                type: str
                required: true
            certificate:
                description:
                    - Certificate value in string format
                type: str
                required: true
            private_key:
                description:
                    - Private key of the provided certificate
                type: str
                required: true
    server_key_password:
        description:
            - Base-64 encoded password for CA certificate's private key. This value can be empty.
            - Applicable only for I(action=enable_certificate)I(action=renew_certificate).
        type: str
    node_id:
        description:
            - OCID of the node to be removed.
            - Required for I(action=remove_node), I(action=restart_node).
        type: str
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        aliases: ["id"]
        required: true
    is_force_stop_jobs:
        description:
            - Boolean indicating whether to force stop jobs while stopping cluster. Defaults to false.
            - Applicable only for I(action=stop).
        type: bool
    cluster_admin_password:
        description:
            - Base-64 encoded password for the cluster (and Cloudera Manager) admin user.
            - Required for I(action=add_block_storage), I(action=add_cloud_sql), I(action=add_kafka), I(action=add_master_nodes), I(action=add_utility_nodes),
              I(action=add_worker_nodes), I(action=change_shape), I(action=disable_certificate), I(action=enable_certificate),
              I(action=execute_bootstrap_script), I(action=install_os_patch), I(action=install_patch), I(action=remove_cloud_sql), I(action=remove_kafka),
              I(action=remove_node), I(action=renew_certificate), I(action=start), I(action=stop).
        type: str
    action:
        description:
            - The action to perform on the BdsInstance.
        type: str
        required: true
        choices:
            - "add_block_storage"
            - "add_cloud_sql"
            - "add_kafka"
            - "add_master_nodes"
            - "add_utility_nodes"
            - "add_worker_nodes"
            - "certificate_service_info"
            - "change_compartment"
            - "change_shape"
            - "disable_certificate"
            - "enable_certificate"
            - "execute_bootstrap_script"
            - "get_os_patch_details"
            - "install_os_patch"
            - "install_patch"
            - "list_os_patches"
            - "remove_cloud_sql"
            - "remove_kafka"
            - "remove_node"
            - "renew_certificate"
            - "restart_node"
            - "start"
            - "stop"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_block_storage on bds_instance
  oci_bds_instance_actions:
    # required
    node_type: WORKER
    block_volume_size_in_gbs: 56
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: add_block_storage

- name: Perform action add_cloud_sql on bds_instance
  oci_bds_instance_actions:
    # required
    shape: shape_example
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: add_cloud_sql

    # optional
    block_volume_size_in_gbs: 56
    shape_config:
      # optional
      ocpus: 56
      memory_in_gbs: 56
      nvmes: 56

- name: Perform action add_kafka on bds_instance
  oci_bds_instance_actions:
    # required
    number_of_kafka_nodes: 56
    shape: shape_example
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: add_kafka

    # optional
    block_volume_size_in_gbs: 56
    shape_config:
      # optional
      ocpus: 56
      memory_in_gbs: 56
      nvmes: 56

- name: Perform action add_master_nodes on bds_instance
  oci_bds_instance_actions:
    # required
    number_of_master_nodes: 56
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: add_master_nodes

    # optional
    shape: shape_example
    block_volume_size_in_gbs: 56
    shape_config:
      # optional
      ocpus: 56
      memory_in_gbs: 56
      nvmes: 56

- name: Perform action add_utility_nodes on bds_instance
  oci_bds_instance_actions:
    # required
    number_of_utility_nodes: 56
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: add_utility_nodes

    # optional
    shape: shape_example
    block_volume_size_in_gbs: 56
    shape_config:
      # optional
      ocpus: 56
      memory_in_gbs: 56
      nvmes: 56

- name: Perform action add_worker_nodes on bds_instance
  oci_bds_instance_actions:
    # required
    number_of_worker_nodes: 56
    node_type: WORKER
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: add_worker_nodes

    # optional
    shape: shape_example
    block_volume_size_in_gbs: 56
    shape_config:
      # optional
      ocpus: 56
      memory_in_gbs: 56
      nvmes: 56

- name: Perform action certificate_service_info on bds_instance
  oci_bds_instance_actions:
    # required
    services: [ "services_example" ]
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: certificate_service_info

- name: Perform action change_compartment on bds_instance
  oci_bds_instance_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action change_shape on bds_instance
  oci_bds_instance_actions:
    # required
    nodes:
      # optional
      worker: worker_example
      worker_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
        nvmes: 56
      compute_only_worker: compute_only_worker_example
      compute_only_worker_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
        nvmes: 56
      master: master_example
      master_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
        nvmes: 56
      utility: utility_example
      utility_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
        nvmes: 56
      cloudsql: cloudsql_example
      cloudsql_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
        nvmes: 56
      edge: edge_example
      edge_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
        nvmes: 56
      kafka_broker: kafka_broker_example
      kafka_broker_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
        nvmes: 56
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: change_shape

- name: Perform action disable_certificate on bds_instance
  oci_bds_instance_actions:
    # required
    services: [ "services_example" ]
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: disable_certificate

- name: Perform action enable_certificate on bds_instance
  oci_bds_instance_actions:
    # required
    services: [ "services_example" ]
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: enable_certificate

    # optional
    root_certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    host_cert_details:
    - # required
      host_name: host_name_example
      certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
      private_key: private_key_example
    server_key_password: example-password

- name: Perform action execute_bootstrap_script on bds_instance
  oci_bds_instance_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: execute_bootstrap_script

    # optional
    bootstrap_script_url: bootstrap_script_url_example

- name: Perform action get_os_patch_details on bds_instance
  oci_bds_instance_actions:
    # required
    os_patch_version: os_patch_version_example
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: get_os_patch_details

- name: Perform action install_os_patch on bds_instance
  oci_bds_instance_actions:
    # required
    os_patch_version: os_patch_version_example
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: install_os_patch

- name: Perform action install_patch on bds_instance
  oci_bds_instance_actions:
    # required
    version: version_example
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: install_patch

- name: Perform action list_os_patches on bds_instance
  oci_bds_instance_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: list_os_patches

    # optional
    sort_by: timeCreated
    sort_order: ASC

- name: Perform action remove_cloud_sql on bds_instance
  oci_bds_instance_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: remove_cloud_sql

- name: Perform action remove_kafka on bds_instance
  oci_bds_instance_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: remove_kafka

- name: Perform action remove_node on bds_instance
  oci_bds_instance_actions:
    # required
    node_id: "ocid1.node.oc1..xxxxxxEXAMPLExxxxxx"
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: remove_node

    # optional
    is_force_remove_enabled: true

- name: Perform action renew_certificate on bds_instance
  oci_bds_instance_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: renew_certificate

    # optional
    services: [ "services_example" ]
    root_certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
    host_cert_details:
    - # required
      host_name: host_name_example
      certificate: "-----BEGIN CERTIFICATE----MIIBIjANBgkqhkiG9w0BA..-----END PUBLIC KEY-----"
      private_key: private_key_example
    server_key_password: example-password

- name: Perform action restart_node on bds_instance
  oci_bds_instance_actions:
    # required
    node_id: "ocid1.node.oc1..xxxxxxEXAMPLExxxxxx"
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: restart_node

- name: Perform action start on bds_instance
  oci_bds_instance_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: start

- name: Perform action stop on bds_instance
  oci_bds_instance_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    cluster_admin_password: example-password
    action: stop

    # optional
    is_force_stop_jobs: true

"""

RETURN = """
bds_instance:
    description:
        - Details of the BdsInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the Big Data Service resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the cluster.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The state of the cluster.
            returned: on success
            type: str
            sample: CREATING
        cluster_version:
            description:
                - Version of the Hadoop distribution.
            returned: on success
            type: str
            sample: CDH5
        is_high_availability:
            description:
                - Boolean flag specifying whether or not the cluster is highly available (HA)
            returned: on success
            type: bool
            sample: true
        is_secure:
            description:
                - Boolean flag specifying whether or not the cluster should be set up as secure.
            returned: on success
            type: bool
            sample: true
        is_cloud_sql_configured:
            description:
                - Boolean flag specifying whether or not Cloud SQL should be configured.
            returned: on success
            type: bool
            sample: true
        is_kafka_configured:
            description:
                - Boolean flag specifying whether or not Kafka should be configured.
            returned: on success
            type: bool
            sample: true
        network_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_nat_gateway_required:
                    description:
                        - A boolean flag whether to configure a NAT gateway.
                    returned: on success
                    type: bool
                    sample: true
                cidr_block:
                    description:
                        - The CIDR IP address block of the VCN.
                    returned: on success
                    type: str
                    sample: cidr_block_example
        cluster_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                bda_version:
                    description:
                        - BDA version installed in the cluster
                    returned: on success
                    type: str
                    sample: bda_version_example
                bdm_version:
                    description:
                        - Big Data Manager version installed in the cluster.
                    returned: on success
                    type: str
                    sample: bdm_version_example
                bds_version:
                    description:
                        - Big Data Service version installed in the cluster.
                    returned: on success
                    type: str
                    sample: bds_version_example
                os_version:
                    description:
                        - Oracle Linux version installed in the cluster.
                    returned: on success
                    type: str
                    sample: os_version_example
                db_version:
                    description:
                        - Cloud SQL query server database version.
                    returned: on success
                    type: str
                    sample: db_version_example
                bd_cell_version:
                    description:
                        - Cloud SQL cell version.
                    returned: on success
                    type: str
                    sample: bd_cell_version_example
                csql_cell_version:
                    description:
                        - Big Data SQL version.
                    returned: on success
                    type: str
                    sample: csql_cell_version_example
                time_created:
                    description:
                        - The time the cluster was created, shown as an RFC 3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_refreshed:
                    description:
                        - The time the cluster was automatically or manually refreshed, shown as an RFC 3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                cloudera_manager_url:
                    description:
                        - The URL of Cloudera Manager
                    returned: on success
                    type: str
                    sample: cloudera_manager_url_example
                ambari_url:
                    description:
                        - The URL of Ambari
                    returned: on success
                    type: str
                    sample: ambari_url_example
                big_data_manager_url:
                    description:
                        - The URL of Big Data Manager.
                    returned: on success
                    type: str
                    sample: big_data_manager_url_example
                hue_server_url:
                    description:
                        - The URL of the Hue server.
                    returned: on success
                    type: str
                    sample: hue_server_url_example
                odh_version:
                    description:
                        - Version of the ODH (Oracle Distribution including Apache Hadoop) installed on the cluster.
                    returned: on success
                    type: str
                    sample: odh_version_example
                jupyter_hub_url:
                    description:
                        - The URL of the Jupyterhub.
                    returned: on success
                    type: str
                    sample: jupyter_hub_url_example
        nodes:
            description:
                - The list of nodes in the cluster.
            returned: on success
            type: complex
            contains:
                instance_id:
                    description:
                        - The OCID of the underlying Oracle Cloud Infrastructure Compute instance.
                    returned: on success
                    type: str
                    sample: "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - The name of the node.
                    returned: on success
                    type: str
                    sample: display_name_example
                lifecycle_state:
                    description:
                        - The state of the node.
                    returned: on success
                    type: str
                    sample: CREATING
                node_type:
                    description:
                        - Cluster node type.
                    returned: on success
                    type: str
                    sample: MASTER
                shape:
                    description:
                        - Shape of the node.
                    returned: on success
                    type: str
                    sample: shape_example
                attached_block_volumes:
                    description:
                        - The list of block volumes attached to a given node.
                    returned: on success
                    type: complex
                    contains:
                        volume_attachment_id:
                            description:
                                - The OCID of the volume attachment.
                            returned: on success
                            type: str
                            sample: "ocid1.volumeattachment.oc1..xxxxxxEXAMPLExxxxxx"
                        volume_size_in_gbs:
                            description:
                                - The size of the volume in GBs.
                            returned: on success
                            type: int
                            sample: 56
                subnet_id:
                    description:
                        - The OCID of the subnet in which the node is to be created.
                    returned: on success
                    type: str
                    sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
                ip_address:
                    description:
                        - IP address of the node.
                    returned: on success
                    type: str
                    sample: ip_address_example
                hostname:
                    description:
                        - The fully-qualified hostname (FQDN) of the node.
                    returned: on success
                    type: str
                    sample: hostname_example
                image_id:
                    description:
                        - The OCID of the image from which the node was created.
                    returned: on success
                    type: str
                    sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
                ssh_fingerprint:
                    description:
                        - The fingerprint of the SSH key used for node access.
                    returned: on success
                    type: str
                    sample: ssh_fingerprint_example
                availability_domain:
                    description:
                        - The name of the availability domain in which the node is running.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                fault_domain:
                    description:
                        - The name of the fault domain in which the node is running.
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
                time_created:
                    description:
                        - The time the node was created, shown as an RFC 3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The time the cluster was updated, shown as an RFC 3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                ocpus:
                    description:
                        - The total number of OCPUs available to the node.
                    returned: on success
                    type: int
                    sample: 56
                memory_in_gbs:
                    description:
                        - The total amount of memory available to the node, in gigabytes.
                    returned: on success
                    type: int
                    sample: 56
                nvmes:
                    description:
                        - The number of NVMe drives to be used for storage. A single drive has 6.8 TB available.
                    returned: on success
                    type: int
                    sample: 56
                local_disks_total_size_in_gbs:
                    description:
                        - The aggregate size of all local disks, in gigabytes. If the instance does not have any local disks, this field is null.
                    returned: on success
                    type: float
                    sample: 1.2
                time_maintenance_reboot_due:
                    description:
                        - The date and time the instance is expected to be stopped / started, in the format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        cloud_sql_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - Shape of the node
                    returned: on success
                    type: str
                    sample: shape_example
                block_volume_size_in_gbs:
                    description:
                        - The size of block volume in GB that needs to be attached to a given node.
                          All the necessary details needed for attachment are managed by service itself.
                    returned: on success
                    type: int
                    sample: 56
                is_kerberos_mapped_to_database_users:
                    description:
                        - Boolean flag specifying whether or not Kerberos principals are mapped
                          to database users.
                    returned: on success
                    type: bool
                    sample: true
                ip_address:
                    description:
                        - IP address of the Cloud SQL node.
                    returned: on success
                    type: str
                    sample: ip_address_example
                kerberos_details:
                    description:
                        - Details about the Kerberos principals.
                    returned: on success
                    type: complex
                    contains:
                        principal_name:
                            description:
                                - Name of the Kerberos principal.
                            returned: on success
                            type: str
                            sample: principal_name_example
                        keytab_file:
                            description:
                                - Location of the keytab file
                            returned: on success
                            type: str
                            sample: keytab_file_example
        created_by:
            description:
                - The user who created the cluster.
            returned: on success
            type: str
            sample: created_by_example
        time_created:
            description:
                - The time the cluster was created, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the cluster was updated, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        number_of_nodes:
            description:
                - Number of nodes that forming the cluster
            returned: on success
            type: int
            sample: 56
        number_of_nodes_requiring_maintenance_reboot:
            description:
                - Number of nodes that require a maintenance reboot
            returned: on success
            type: int
            sample: 56
        bootstrap_script_url:
            description:
                - pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed.
            returned: on success
            type: str
            sample: bootstrap_script_url_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope.
                  Exists for cross-compatibility only. For example, `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For example, `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        kms_key_id:
            description:
                - The OCID of the Key Management master encryption key.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_profile:
            description:
                - Profile of the Big Data Service cluster.
            returned: on success
            type: str
            sample: HADOOP_EXTENDED
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "cluster_version": "CDH5",
        "is_high_availability": true,
        "is_secure": true,
        "is_cloud_sql_configured": true,
        "is_kafka_configured": true,
        "network_config": {
            "is_nat_gateway_required": true,
            "cidr_block": "cidr_block_example"
        },
        "cluster_details": {
            "bda_version": "bda_version_example",
            "bdm_version": "bdm_version_example",
            "bds_version": "bds_version_example",
            "os_version": "os_version_example",
            "db_version": "db_version_example",
            "bd_cell_version": "bd_cell_version_example",
            "csql_cell_version": "csql_cell_version_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_refreshed": "2013-10-20T19:20:30+01:00",
            "cloudera_manager_url": "cloudera_manager_url_example",
            "ambari_url": "ambari_url_example",
            "big_data_manager_url": "big_data_manager_url_example",
            "hue_server_url": "hue_server_url_example",
            "odh_version": "odh_version_example",
            "jupyter_hub_url": "jupyter_hub_url_example"
        },
        "nodes": [{
            "instance_id": "ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "lifecycle_state": "CREATING",
            "node_type": "MASTER",
            "shape": "shape_example",
            "attached_block_volumes": [{
                "volume_attachment_id": "ocid1.volumeattachment.oc1..xxxxxxEXAMPLExxxxxx",
                "volume_size_in_gbs": 56
            }],
            "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
            "ip_address": "ip_address_example",
            "hostname": "hostname_example",
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
            "ssh_fingerprint": "ssh_fingerprint_example",
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": "FAULT-DOMAIN-1",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "ocpus": 56,
            "memory_in_gbs": 56,
            "nvmes": 56,
            "local_disks_total_size_in_gbs": 1.2,
            "time_maintenance_reboot_due": "2013-10-20T19:20:30+01:00"
        }],
        "cloud_sql_details": {
            "shape": "shape_example",
            "block_volume_size_in_gbs": 56,
            "is_kerberos_mapped_to_database_users": true,
            "ip_address": "ip_address_example",
            "kerberos_details": [{
                "principal_name": "principal_name_example",
                "keytab_file": "keytab_file_example"
            }]
        },
        "created_by": "created_by_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "number_of_nodes": 56,
        "number_of_nodes_requiring_maintenance_reboot": 56,
        "bootstrap_script_url": "bootstrap_script_url_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "cluster_profile": "HADOOP_EXTENDED"
    }

certificate_service_info_summary:
    description:
        - Details of the BdsInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        service:
            description:
                - Name of the service
            returned: on success
            type: str
            sample: ZOOKEEPER
        service_certificate_status:
            description:
                - Whether certificate is enabled or disabled
            returned: on success
            type: str
            sample: ENABLED
        host_specific_certificate_details:
            description:
                - List of Host specific certificate details
            returned: on success
            type: complex
            contains:
                host_name:
                    description:
                        - Name of the host.
                    returned: on success
                    type: str
                    sample: host_name_example
                certificate_type:
                    description:
                        - Type of certificate self signed or CA signed
                    returned: on success
                    type: str
                    sample: CUSTOM_SIGNED
                time_expiry:
                    description:
                        - The time the certificate expires, shown as an RFC 3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "service": "ZOOKEEPER",
        "service_certificate_status": "ENABLED",
        "host_specific_certificate_details": [{
            "host_name": "host_name_example",
            "certificate_type": "CUSTOM_SIGNED",
            "time_expiry": "2013-10-20T19:20:30+01:00"
        }]
    }

os_patch_details:
    description:
        - Details of the BdsInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        os_patch_version:
            description:
                - Version of the os patch.
            returned: on success
            type: str
            sample: os_patch_version_example
        min_bds_version:
            description:
                - Minimum BDS version required to install current OS patch.
            returned: on success
            type: str
            sample: min_bds_version_example
        min_compatible_odh_version_map:
            description:
                - "Map of major ODH version to minimum ODH version required to install current OS patch. e.g. {ODH0.9: 0.9.1}"
            returned: on success
            type: dict
            sample: {}
        target_packages:
            description:
                - List of summaries of individual target packages.
            returned: on success
            type: complex
            contains:
                package_name:
                    description:
                        - The package's name.
                    returned: on success
                    type: str
                    sample: package_name_example
                target_version:
                    description:
                        - The target version of the package.
                    returned: on success
                    type: str
                    sample: target_version_example
                update_type:
                    description:
                        - The action that current package will be executed on the cluster.
                    returned: on success
                    type: str
                    sample: INSTALL
                related_cv_es:
                    description:
                        - Related CVEs of the package update.
                    returned: on success
                    type: list
                    sample: []
        release_date:
            description:
                - Released date of the OS patch.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        patch_type:
            description:
                - Type of a specific os patch.
                  REGULAR means standard released os patches.
                  CUSTOM means os patches with some customizations.
                  EMERGENT means os patches with some emergency fixes that should be prioritized.
            returned: on success
            type: str
            sample: REGULAR
    sample: {
        "os_patch_version": "os_patch_version_example",
        "min_bds_version": "min_bds_version_example",
        "min_compatible_odh_version_map": {},
        "target_packages": [{
            "package_name": "package_name_example",
            "target_version": "target_version_example",
            "update_type": "INSTALL",
            "related_cv_es": []
        }],
        "release_date": "2013-10-20T19:20:30+01:00",
        "patch_type": "REGULAR"
    }

os_patch_summary:
    description:
        - Details of the BdsInstance resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        os_patch_version:
            description:
                - Patch version of the os patch.
            returned: on success
            type: str
            sample: os_patch_version_example
        release_date:
            description:
                - The time when the OS patch was released.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "os_patch_version": "os_patch_version_example",
        "release_date": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.bds import BdsClient
    from oci.bds.models import AddBlockStorageDetails
    from oci.bds.models import AddCloudSqlDetails
    from oci.bds.models import AddKafkaDetails
    from oci.bds.models import AddMasterNodesDetails
    from oci.bds.models import AddUtilityNodesDetails
    from oci.bds.models import AddWorkerNodesDetails
    from oci.bds.models import CertificateServiceInfoDetails
    from oci.bds.models import ChangeBdsInstanceCompartmentDetails
    from oci.bds.models import ChangeShapeDetails
    from oci.bds.models import DisableCertificateDetails
    from oci.bds.models import EnableCertificateDetails
    from oci.bds.models import ExecuteBootstrapScriptDetails
    from oci.bds.models import InstallOsPatchDetails
    from oci.bds.models import InstallPatchDetails
    from oci.bds.models import RemoveCloudSqlDetails
    from oci.bds.models import RemoveKafkaDetails
    from oci.bds.models import RemoveNodeDetails
    from oci.bds.models import RenewCertificateDetails
    from oci.bds.models import RestartNodeDetails
    from oci.bds.models import StartBdsInstanceDetails
    from oci.bds.models import StopBdsInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_block_storage
        add_cloud_sql
        add_kafka
        add_master_nodes
        add_utility_nodes
        add_worker_nodes
        certificate_service_info
        change_compartment
        change_shape
        disable_certificate
        enable_certificate
        execute_bootstrap_script
        get_os_patch_details
        install_os_patch
        install_patch
        list_os_patches
        remove_cloud_sql
        remove_kafka
        remove_node
        renew_certificate
        restart_node
        start
        stop
    """

    @staticmethod
    def get_module_resource_id_param():
        return "bds_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("bds_instance_id")

    def get_get_fn(self):
        return self.client.get_bds_instance

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_instance,
            bds_instance_id=self.module.params.get("bds_instance_id"),
        )

    def get_response_field_name(self, action):
        response_fields = dict(
            stop="bds_instance",
            start="bds_instance",
            add_block_storage="bds_instance",
            add_cloud_sql="bds_instance",
            add_kafka="bds_instance",
            add_master_nodes="bds_instance",
            add_utility_nodes="bds_instance",
            add_worker_nodes="bds_instance",
            certificate_service_info="certificate_service_info_summary",
            change_shape="bds_instance",
            disable_certificate="bds_instance",
            enable_certificate="bds_instance",
            execute_bootstrap_script="bds_instance",
            get_os_patch_details="os_patch_details",
            install_os_patch="bds_instance",
            install_patch="bds_instance",
            list_os_patches="os_patch_summary",
            remove_cloud_sql="bds_instance",
            remove_kafka="bds_instance",
            remove_node="bds_instance",
            renew_certificate="bds_instance",
            restart_node="bds_instance",
            change_compartment="bds_instance",
        )
        return response_fields.get(action, "bds_instance")

    def add_block_storage(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddBlockStorageDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_block_storage,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_block_storage_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def add_cloud_sql(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddCloudSqlDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_cloud_sql,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_cloud_sql_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def add_kafka(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddKafkaDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_kafka,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_kafka_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def add_master_nodes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddMasterNodesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_master_nodes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_master_nodes_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def add_utility_nodes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddUtilityNodesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_utility_nodes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_utility_nodes_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def add_worker_nodes(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddWorkerNodesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_worker_nodes,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                add_worker_nodes_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def certificate_service_info(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CertificateServiceInfoDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.certificate_service_info,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                certificate_service_info_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeBdsInstanceCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_bds_instance_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                change_bds_instance_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_shape(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeShapeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_shape,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                change_shape_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def disable_certificate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DisableCertificateDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.disable_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                disable_certificate_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def enable_certificate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, EnableCertificateDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.enable_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                enable_certificate_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def execute_bootstrap_script(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ExecuteBootstrapScriptDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.execute_bootstrap_script,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                execute_bootstrap_script_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_os_patch_details(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.get_os_patch_details,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                os_patch_version=self.module.params.get("os_patch_version"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def install_os_patch(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstallOsPatchDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_os_patch,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                install_os_patch_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def install_patch(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, InstallPatchDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.install_patch,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                install_patch_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def list_os_patches(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.list_os_patches,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                sort_by=self.module.params.get("sort_by"),
                sort_order=self.module.params.get("sort_order"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def remove_cloud_sql(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveCloudSqlDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_cloud_sql,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                remove_cloud_sql_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_kafka(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveKafkaDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_kafka,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                remove_kafka_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def remove_node(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveNodeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_node,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                remove_node_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def renew_certificate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RenewCertificateDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.renew_certificate,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                renew_certificate_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def restart_node(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestartNodeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restart_node,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                restart_node_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def start(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StartBdsInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.start_bds_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                start_bds_instance_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def stop(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, StopBdsInstanceDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.stop_bds_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                stop_bds_instance_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BdsInstanceActionsHelperCustom = get_custom_class("BdsInstanceActionsHelperCustom")


class ResourceHelper(BdsInstanceActionsHelperCustom, BdsInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            number_of_kafka_nodes=dict(type="int"),
            number_of_master_nodes=dict(type="int"),
            number_of_utility_nodes=dict(type="int"),
            number_of_worker_nodes=dict(type="int"),
            node_type=dict(
                type="str",
                choices=["WORKER", "COMPUTE_ONLY_WORKER", "KAFKA_BROKER", "EDGE"],
            ),
            shape=dict(type="str"),
            block_volume_size_in_gbs=dict(type="int"),
            shape_config=dict(
                type="dict",
                options=dict(
                    ocpus=dict(type="int"),
                    memory_in_gbs=dict(type="int"),
                    nvmes=dict(type="int"),
                ),
            ),
            compartment_id=dict(type="str"),
            nodes=dict(
                type="dict",
                options=dict(
                    worker=dict(type="str"),
                    worker_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    compute_only_worker=dict(type="str"),
                    compute_only_worker_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    master=dict(type="str"),
                    master_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    utility=dict(type="str"),
                    utility_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    cloudsql=dict(type="str"),
                    cloudsql_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    edge=dict(type="str"),
                    edge_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                    kafka_broker=dict(type="str"),
                    kafka_broker_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"),
                            memory_in_gbs=dict(type="int"),
                            nvmes=dict(type="int"),
                        ),
                    ),
                ),
            ),
            bootstrap_script_url=dict(type="str"),
            os_patch_version=dict(type="str"),
            version=dict(type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            is_force_remove_enabled=dict(type="bool"),
            services=dict(type="list", elements="str"),
            root_certificate=dict(type="str"),
            host_cert_details=dict(
                type="list",
                elements="dict",
                options=dict(
                    host_name=dict(type="str", required=True),
                    certificate=dict(type="str", required=True),
                    private_key=dict(type="str", required=True, no_log=True),
                ),
            ),
            server_key_password=dict(type="str", no_log=True),
            node_id=dict(type="str"),
            bds_instance_id=dict(aliases=["id"], type="str", required=True),
            is_force_stop_jobs=dict(type="bool"),
            cluster_admin_password=dict(type="str", no_log=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_block_storage",
                    "add_cloud_sql",
                    "add_kafka",
                    "add_master_nodes",
                    "add_utility_nodes",
                    "add_worker_nodes",
                    "certificate_service_info",
                    "change_compartment",
                    "change_shape",
                    "disable_certificate",
                    "enable_certificate",
                    "execute_bootstrap_script",
                    "get_os_patch_details",
                    "install_os_patch",
                    "install_patch",
                    "list_os_patches",
                    "remove_cloud_sql",
                    "remove_kafka",
                    "remove_node",
                    "renew_certificate",
                    "restart_node",
                    "start",
                    "stop",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="bds_instance",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
