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
module: oci_bds_instance_actions
short_description: Perform actions on a BdsInstance resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a BdsInstance resource in Oracle Cloud Infrastructure
    - For I(action=add_block_storage), adds storage to existing worker nodes. The same amount of storage will be added to all workers.
      No change will be made to already attached storage. Block Storage once added cannot be removed.
    - For I(action=add_cloud_sql), adds Cloud SQL to your cluster. This will add a query server node to the cluster
      and create cell servers on all your worker nodes.
    - For I(action=add_worker_nodes), add worker nodes to an existing cluster. The worker nodes added will be based on an identical shape
      and have the same amount of attached block storage as other worker nodes in the cluster.
    - For I(action=remove_cloud_sql), remove Cloud SQL capability.
version_added: "2.9"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the BDS instance
        type: str
        aliases: ["id"]
        required: true
    cluster_admin_password:
        description:
            - Base-64 encoded password for Cloudera Manager admin user
        type: str
        required: true
    block_volume_size_in_gbs:
        description:
            - The size of block volume in GB that needs to be added to each worker node.
              All the necessary details needed for attachment are managed by service itself.
            - Required for I(action=add_block_storage).
        type: int
    shape:
        description:
            - Shape of the node
            - Required for I(action=add_cloud_sql).
        type: str
    number_of_worker_nodes:
        description:
            - Number of additional worker nodes for the BDS instance
            - Required for I(action=add_worker_nodes).
        type: int
    action:
        description:
            - The action to perform on the BdsInstance.
        type: str
        required: true
        choices:
            - "add_block_storage"
            - "add_cloud_sql"
            - "add_worker_nodes"
            - "remove_cloud_sql"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_block_storage on bds_instance
  oci_bds_instance_actions:
    bds_instance_id: ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx
    cluster_admin_password: cluster_admin_password_example
    block_volume_size_in_gbs: 56
    action: add_block_storage

- name: Perform action add_cloud_sql on bds_instance
  oci_bds_instance_actions:
    bds_instance_id: ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx
    cluster_admin_password: cluster_admin_password_example
    shape: shape_example
    action: add_cloud_sql

- name: Perform action add_worker_nodes on bds_instance
  oci_bds_instance_actions:
    bds_instance_id: ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx
    cluster_admin_password: cluster_admin_password_example
    number_of_worker_nodes: 56
    action: add_worker_nodes

- name: Perform action remove_cloud_sql on bds_instance
  oci_bds_instance_actions:
    bds_instance_id: ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx
    cluster_admin_password: cluster_admin_password_example
    action: remove_cloud_sql

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
                - The OCID of the BDS resource
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - Name of the BDS instance
            returned: on success
            type: string
            sample: display_name_example
        lifecycle_state:
            description:
                - The state of the BDS instance
            returned: on success
            type: string
            sample: CREATING
        cluster_version:
            description:
                - Version of the Hadoop distribution
            returned: on success
            type: string
            sample: CDH5
        is_high_availability:
            description:
                - Boolean flag specifying whether or not the cluster is HA
            returned: on success
            type: bool
            sample: true
        is_secure:
            description:
                - Boolean flag specifying whether or not the cluster should be setup as secure.
            returned: on success
            type: bool
            sample: true
        is_cloud_sql_configured:
            description:
                - Boolean flag specifying whether we configure Cloud SQL or not
            returned: on success
            type: bool
            sample: true
        network_config:
            description:
                - Additional configuration of customer's network.
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
                    type: string
                    sample: 172.16.0.0/16
        cluster_details:
            description:
                - Specific info about a Hadoop cluster
            returned: on success
            type: complex
            contains:
                bda_version:
                    description:
                        - BDA version installed in the cluster
                    returned: on success
                    type: string
                    sample: bda_version_example
                bdm_version:
                    description:
                        - BDM version installed in the cluster
                    returned: on success
                    type: string
                    sample: bdm_version_example
                time_created:
                    description:
                        - The time the cluster was created. An RFC3339 formatted datetime string
                    returned: on success
                    type: string
                    sample: 2019-03-29T09:36:42.000+0000
                time_refreshed:
                    description:
                        - The time the BDS instance was automatically, or manually refreshed.
                          An RFC3339 formatted datetime string
                    returned: on success
                    type: string
                    sample: 2019-03-29T09:36:42.000+0000
                cloudera_manager_url:
                    description:
                        - The URL of a Cloudera Manager
                    returned: on success
                    type: string
                    sample: cloudera_manager_url_example
                big_data_manager_url:
                    description:
                        - The URL of a Big Data Manager
                    returned: on success
                    type: string
                    sample: big_data_manager_url_example
                hue_server_url:
                    description:
                        - The URL of a Hue Server
                    returned: on success
                    type: string
                    sample: hue_server_url_example
        nodes:
            description:
                - The list of nodes in the BDS instance
            returned: on success
            type: complex
            contains:
                instance_id:
                    description:
                        - The OCID of the underlying compute instance
                    returned: on success
                    type: string
                    sample: ocid1.instance.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - The name of the node
                    returned: on success
                    type: string
                    sample: display_name_example
                lifecycle_state:
                    description:
                        - The state of the node
                    returned: on success
                    type: string
                    sample: CREATING
                node_type:
                    description:
                        - BDS instance node type
                    returned: on success
                    type: string
                    sample: MASTER
                shape:
                    description:
                        - Shape of the node
                    returned: on success
                    type: string
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
                            type: string
                            sample: ocid1.volumeattachment.oc1..xxxxxxEXAMPLExxxxxx
                        volume_size_in_gbs:
                            description:
                                - The size of the volume in GBs.
                            returned: on success
                            type: int
                            sample: 56
                subnet_id:
                    description:
                        - The OCID of the subnet in which the node should be created
                    returned: on success
                    type: string
                    sample: ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx
                ip_address:
                    description:
                        - IP address of the node
                    returned: on success
                    type: string
                    sample: ip_address_example
                image_id:
                    description:
                        - The OCID of the image from which the node was created
                    returned: on success
                    type: string
                    sample: ocid1.image.oc1..xxxxxxEXAMPLExxxxxx
                ssh_fingerprint:
                    description:
                        - The fingerprint of the SSH key used for node access
                    returned: on success
                    type: string
                    sample: ssh_fingerprint_example
                availability_domain:
                    description:
                        - The name of the availability domain the node is running in
                    returned: on success
                    type: string
                    sample: Uocm:PHX-AD-1
                fault_domain:
                    description:
                        - The name of the fault domain the node is running in
                    returned: on success
                    type: string
                    sample: fault_domain_example
                time_created:
                    description:
                        - The time the node was created. An RFC3339 formatted datetime string
                    returned: on success
                    type: string
                    sample: 2019-03-29T09:36:42.000+0000
                time_updated:
                    description:
                        - The time the BDS instance was updated. An RFC3339 formatted datetime string
                    returned: on success
                    type: string
                    sample: 2019-03-29T09:36:42.000+0000
        cloud_sql_details:
            description:
                - The information about added Cloud SQL capability
            returned: on success
            type: complex
            contains:
                shape:
                    description:
                        - Shape of the node
                    returned: on success
                    type: string
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
                        - Boolean flag specifying whether or not are Kerberos principals mapped
                          to database users.
                    returned: on success
                    type: bool
                    sample: true
                ip_address:
                    description:
                        - IP address of the Cloud SQL node
                    returned: on success
                    type: string
                    sample: ip_address_example
                kerberos_details:
                    description:
                        - Details about Kerberos principals
                    returned: on success
                    type: complex
                    contains:
                        principal_name:
                            description:
                                - Name of the Kerberos principal
                            returned: on success
                            type: string
                            sample: principal_name_example
                        keytab_file:
                            description:
                                - Location of the keytab file
                            returned: on success
                            type: string
                            sample: keytab_file_example
        created_by:
            description:
                - The user who created the BDS instance.
            returned: on success
            type: string
            sample: created_by_example
        time_created:
            description:
                - The time the BDS instance was created. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2019-03-29T09:36:42.000+0000
        time_updated:
            description:
                - The time the BDS instance was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2019-03-29T09:36:42.000+0000
        number_of_nodes:
            description:
                - Number of nodes that forming the cluster
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
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
            "cidr_block": "172.16.0.0/16"
        },
        "cluster_details": {
            "bda_version": "bda_version_example",
            "bdm_version": "bdm_version_example",
            "time_created": "2019-03-29T09:36:42.000+0000",
            "time_refreshed": "2019-03-29T09:36:42.000+0000",
            "cloudera_manager_url": "cloudera_manager_url_example",
            "big_data_manager_url": "big_data_manager_url_example",
            "hue_server_url": "hue_server_url_example"
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
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
            "ssh_fingerprint": "ssh_fingerprint_example",
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": "fault_domain_example",
            "time_created": "2019-03-29T09:36:42.000+0000",
            "time_updated": "2019-03-29T09:36:42.000+0000"
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
        "time_created": "2019-03-29T09:36:42.000+0000",
        "time_updated": "2019-03-29T09:36:42.000+0000",
        "number_of_nodes": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.bds import BdsClient
    from oci.bds.models import AddBlockStorageDetails
    from oci.bds.models import AddCloudSqlDetails
    from oci.bds.models import AddWorkerNodesDetails
    from oci.bds.models import RemoveCloudSqlDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsInstanceActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_block_storage
        add_cloud_sql
        add_worker_nodes
        remove_cloud_sql
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


BdsInstanceActionsHelperCustom = get_custom_class("BdsInstanceActionsHelperCustom")


class ResourceHelper(BdsInstanceActionsHelperCustom, BdsInstanceActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            bds_instance_id=dict(aliases=["id"], type="str", required=True),
            cluster_admin_password=dict(type="str", required=True, no_log=True),
            block_volume_size_in_gbs=dict(type="int"),
            shape=dict(type="str"),
            number_of_worker_nodes=dict(type="int"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_block_storage",
                    "add_cloud_sql",
                    "add_worker_nodes",
                    "remove_cloud_sql",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

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
