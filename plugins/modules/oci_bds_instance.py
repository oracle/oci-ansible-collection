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
module: oci_bds_instance
short_description: Manage a BdsInstance resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a BdsInstance resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a Big Data Service cluster.
    - "This resource has the following action operations in the M(oracle.oci.oci_bds_instance_actions) module: add_block_storage, add_cloud_sql,
      add_worker_nodes, change_compartment, change_shape, remove_cloud_sql, restart_node."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - Name of the Big Data Service cluster.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    cluster_version:
        description:
            - Version of the Hadoop distribution.
            - Required for create using I(state=present).
        type: str
    cluster_public_key:
        description:
            - The SSH public key used to authenticate the cluster connection.
            - Required for create using I(state=present).
        type: str
    cluster_admin_password:
        description:
            - Base-64 encoded password for the cluster (and Cloudera Manager) admin user.
            - Required for create using I(state=present).
        type: str
    is_high_availability:
        description:
            - Boolean flag specifying whether or not the cluster is highly available (HA).
            - Required for create using I(state=present).
        type: bool
    is_secure:
        description:
            - Boolean flag specifying whether or not the cluster should be set up as secure.
            - Required for create using I(state=present).
        type: bool
    network_config:
        description:
            - ""
        type: dict
        suboptions:
            is_nat_gateway_required:
                description:
                    - A boolean flag whether to configure a NAT gateway.
                type: bool
            cidr_block:
                description:
                    - The CIDR IP address block of the VCN.
                type: str
    nodes:
        description:
            - The list of nodes in the Big Data Service cluster.
            - Required for create using I(state=present).
        type: list
        elements: dict
        suboptions:
            node_type:
                description:
                    - The Big Data Service cluster node type.
                type: str
                required: true
            shape:
                description:
                    - Shape of the node.
                type: str
                required: true
            block_volume_size_in_gbs:
                description:
                    - The size of block volume in GB to be attached to a given node. All the
                      details needed for attaching the block volume are managed by service itself.
                type: int
                required: true
            subnet_id:
                description:
                    - The OCID of the subnet in which the node will be created.
                type: str
                required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type, or scope.
              Exists for cross-compatibility only. For example, `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For example, `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    bds_instance_id:
        description:
            - The OCID of the cluster.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the BdsInstance.
            - Use I(state=present) to create or update a BdsInstance.
            - Use I(state=absent) to delete a BdsInstance.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create bds_instance
  oci_bds_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    cluster_version: cluster_version_example
    cluster_public_key: "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..."
    cluster_admin_password: example-password
    is_high_availability: true
    is_secure: true
    nodes:
    - # required
      node_type: node_type_example
      shape: shape_example
      block_volume_size_in_gbs: 56
      subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    network_config:
      # optional
      is_nat_gateway_required: true
      cidr_block: cidr_block_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update bds_instance
  oci_bds_instance:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update bds_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bds_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete bds_instance
  oci_bds_instance:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete bds_instance using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_bds_instance:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
            "hostname": "hostname_example",
            "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
            "ssh_fingerprint": "ssh_fingerprint_example",
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": "FAULT-DOMAIN-1",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.bds import BdsClient
    from oci.bds.models import CreateBdsInstanceDetails
    from oci.bds.models import UpdateBdsInstanceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsInstanceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(BdsInstanceHelperGen, self).get_possible_entity_types() + [
            "bdsinstance",
            "bdsinstances",
            "bdsbdsinstance",
            "bdsbdsinstances",
            "bdsinstanceresource",
            "bdsinstancesresource",
            "bds",
        ]

    def get_module_resource_id_param(self):
        return "bds_instance_id"

    def get_module_resource_id(self):
        return self.module.params.get("bds_instance_id")

    def get_get_fn(self):
        return self.client.get_bds_instance

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_instance, bds_instance_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_instance,
            bds_instance_id=self.module.params.get("bds_instance_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_bds_instances, **kwargs
        )

    def get_create_model_class(self):
        return CreateBdsInstanceDetails

    def get_exclude_attributes(self):
        return ["cluster_public_key", "cluster_admin_password"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_bds_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(create_bds_instance_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateBdsInstanceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_bds_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                update_bds_instance_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_bds_instance,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


BdsInstanceHelperCustom = get_custom_class("BdsInstanceHelperCustom")


class ResourceHelper(BdsInstanceHelperCustom, BdsInstanceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            cluster_version=dict(type="str"),
            cluster_public_key=dict(type="str", no_log=True),
            cluster_admin_password=dict(type="str", no_log=True),
            is_high_availability=dict(type="bool"),
            is_secure=dict(type="bool"),
            network_config=dict(
                type="dict",
                options=dict(
                    is_nat_gateway_required=dict(type="bool"),
                    cidr_block=dict(type="str"),
                ),
            ),
            nodes=dict(
                type="list",
                elements="dict",
                options=dict(
                    node_type=dict(type="str", required=True),
                    shape=dict(type="str", required=True),
                    block_volume_size_in_gbs=dict(type="int", required=True),
                    subnet_id=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            bds_instance_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
