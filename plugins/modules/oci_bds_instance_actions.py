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
module: oci_bds_instance_actions
short_description: Perform actions on a BdsInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BdsInstance resource in Oracle Cloud Infrastructure
    - For I(action=add_block_storage), adds block storage to existing worker/compute only worker nodes. The same amount of  storage will be added to all
      worker/compute only worker nodes. No change will be made to storage that is already attached. Block storage cannot be removed.
    - For I(action=add_cloud_sql), adds Cloud SQL to your cluster. You can use Cloud SQL to query against non-relational data stored in multiple big data
      sources, including Apache Hive, HDFS, Oracle NoSQL Database, and Apache HBase. Adding Cloud SQL adds a query server node to the cluster and creates cell
      servers on all the worker nodes in the cluster.
    - For I(action=add_worker_nodes), increases the size (scales out) a cluster by adding worker nodes(data/compute). The added worker nodes will have the same
      shape and will have the same amount of attached block storage as other worker nodes in the cluster.
    - For I(action=change_compartment), moves a Big Data Service cluster into a different compartment.
    - For I(action=change_shape), changes the size of a cluster by scaling up or scaling down the nodes. Nodes are scaled up or down by changing the shapes of
      all the nodes of the same type to the next larger or smaller shape. The node types are master, utility, worker, and Cloud SQL. Only nodes with VM-STANDARD
      shapes can be scaled.
    - For I(action=install_patch), install the specified patch to this cluster.
    - For I(action=remove_cloud_sql), removes Cloud SQL from the cluster.
    - For I(action=remove_node), remove a single node of a Big Data Service cluster
    - For I(action=restart_node), restarts a single node of a Big Data Service cluster
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    number_of_worker_nodes:
        description:
            - Number of additional worker nodes for the cluster.
            - Required for I(action=add_worker_nodes).
        type: int
    node_type:
        description:
            - Worker node types, can either be Worker Data node or Compute only worker node.
            - Required for I(action=add_block_storage), I(action=add_worker_nodes).
        type: str
        choices:
            - "WORKER"
            - "COMPUTE_ONLY_WORKER"
    shape:
        description:
            - Shape of the node.
            - Required for I(action=add_cloud_sql).
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
            - Applicable only for I(action=add_cloud_sql)I(action=add_worker_nodes).
        type: dict
        suboptions:
            ocpus:
                description:
                    - The total number of OCPUs available to the node.
                type: int
            memory_in_gbs:
                description:
                    - The total amount of memory available to the node, in gigabytes
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
                            - The total amount of memory available to the node, in gigabytes
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
                            - The total amount of memory available to the node, in gigabytes
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
                            - The total amount of memory available to the node, in gigabytes
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
                            - The total amount of memory available to the node, in gigabytes
                        type: int
            cloudsql:
                description:
                    - Change shape of the Cloud SQL node to the desired target shape. Only VM_STANDARD shapes are allowed here.
                type: str
    version:
        description:
            - The version of the patch to be installed.
            - Required for I(action=install_patch).
        type: str
    cluster_admin_password:
        description:
            - Base-64 encoded password for the cluster (and Cloudera Manager) admin user.
            - Required for I(action=add_block_storage), I(action=add_cloud_sql), I(action=add_worker_nodes), I(action=change_shape), I(action=install_patch),
              I(action=remove_cloud_sql), I(action=remove_node).
        type: str
    is_force_remove_enabled:
        description:
            - Boolean flag specifying whether or not to force remove node if graceful
              removal fails.
            - Applicable only for I(action=remove_node).
        type: bool
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        aliases: ["id"]
        required: true
    node_id:
        description:
            - OCID of the node to be removed.
            - Required for I(action=remove_node), I(action=restart_node).
        type: str
    action:
        description:
            - The action to perform on the BdsInstance.
        type: str
        required: true
        choices:
            - "add_block_storage"
            - "add_cloud_sql"
            - "add_worker_nodes"
            - "change_compartment"
            - "change_shape"
            - "install_patch"
            - "remove_cloud_sql"
            - "remove_node"
            - "restart_node"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_block_storage on bds_instance
  oci_bds_instance_actions:
    # required
    node_type: WORKER
    block_volume_size_in_gbs: 56
    cluster_admin_password: example-password
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_block_storage

- name: Perform action add_cloud_sql on bds_instance
  oci_bds_instance_actions:
    # required
    shape: shape_example
    cluster_admin_password: example-password
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_cloud_sql

    # optional
    block_volume_size_in_gbs: 56
    shape_config:
      # optional
      ocpus: 56
      memory_in_gbs: 56

- name: Perform action add_worker_nodes on bds_instance
  oci_bds_instance_actions:
    # required
    number_of_worker_nodes: 56
    node_type: WORKER
    cluster_admin_password: example-password
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_worker_nodes

    # optional
    shape: shape_example
    block_volume_size_in_gbs: 56
    shape_config:
      # optional
      ocpus: 56
      memory_in_gbs: 56

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
      compute_only_worker: compute_only_worker_example
      compute_only_worker_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
      master: master_example
      master_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
      utility: utility_example
      utility_shape_config:
        # optional
        ocpus: 56
        memory_in_gbs: 56
      cloudsql: cloudsql_example
    cluster_admin_password: example-password
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_shape

- name: Perform action install_patch on bds_instance
  oci_bds_instance_actions:
    # required
    version: version_example
    cluster_admin_password: example-password
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: install_patch

- name: Perform action remove_cloud_sql on bds_instance
  oci_bds_instance_actions:
    # required
    cluster_admin_password: example-password
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_cloud_sql

- name: Perform action remove_node on bds_instance
  oci_bds_instance_actions:
    # required
    cluster_admin_password: example-password
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    node_id: "ocid1.node.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_node

    # optional
    is_force_remove_enabled: true

- name: Perform action restart_node on bds_instance
  oci_bds_instance_actions:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    node_id: "ocid1.node.oc1..xxxxxxEXAMPLExxxxxx"
    action: restart_node

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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "cluster_version": "CDH5",
        "is_high_availability": true,
        "is_secure": true,
        "is_cloud_sql_configured": true,
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
            "memory_in_gbs": 56
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
        "bootstrap_script_url": "bootstrap_script_url_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.bds.models import AddWorkerNodesDetails
    from oci.bds.models import ChangeBdsInstanceCompartmentDetails
    from oci.bds.models import ChangeShapeDetails
    from oci.bds.models import InstallPatchDetails
    from oci.bds.models import RemoveCloudSqlDetails
    from oci.bds.models import RemoveNodeDetails
    from oci.bds.models import RestartNodeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_block_storage
        add_cloud_sql
        add_worker_nodes
        change_compartment
        change_shape
        install_patch
        remove_cloud_sql
        remove_node
        restart_node
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


BdsInstanceActionsHelperCustom = get_custom_class("BdsInstanceActionsHelperCustom")


class ResourceHelper(BdsInstanceActionsHelperCustom, BdsInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            number_of_worker_nodes=dict(type="int"),
            node_type=dict(type="str", choices=["WORKER", "COMPUTE_ONLY_WORKER"]),
            shape=dict(type="str"),
            block_volume_size_in_gbs=dict(type="int"),
            shape_config=dict(
                type="dict",
                options=dict(ocpus=dict(type="int"), memory_in_gbs=dict(type="int")),
            ),
            compartment_id=dict(type="str"),
            nodes=dict(
                type="dict",
                options=dict(
                    worker=dict(type="str"),
                    worker_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"), memory_in_gbs=dict(type="int")
                        ),
                    ),
                    compute_only_worker=dict(type="str"),
                    compute_only_worker_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"), memory_in_gbs=dict(type="int")
                        ),
                    ),
                    master=dict(type="str"),
                    master_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"), memory_in_gbs=dict(type="int")
                        ),
                    ),
                    utility=dict(type="str"),
                    utility_shape_config=dict(
                        type="dict",
                        options=dict(
                            ocpus=dict(type="int"), memory_in_gbs=dict(type="int")
                        ),
                    ),
                    cloudsql=dict(type="str"),
                ),
            ),
            version=dict(type="str"),
            cluster_admin_password=dict(type="str", no_log=True),
            is_force_remove_enabled=dict(type="bool"),
            bds_instance_id=dict(aliases=["id"], type="str", required=True),
            node_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_block_storage",
                    "add_cloud_sql",
                    "add_worker_nodes",
                    "change_compartment",
                    "change_shape",
                    "install_patch",
                    "remove_cloud_sql",
                    "remove_node",
                    "restart_node",
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
