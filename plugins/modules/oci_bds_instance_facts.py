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
module: oci_bds_instance_facts
short_description: Fetches details about one or multiple BdsInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BdsInstance resources in Oracle Cloud Infrastructure
    - Returns a list of BDS instances.
    - If I(bds_instance_id) is specified, the details of a single BdsInstance will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the BDS instance
            - Required to get a specific bds_instance.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment.
            - Required to list multiple bds_instances.
        type: str
    lifecycle_state:
        description:
            - The state of the BDS instance.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
            - "UPDATING_INFRA"
            - "SUSPENDING"
            - "SUSPENDED"
            - "RESUMING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List bds_instances
  oci_bds_instance_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific bds_instance
  oci_bds_instance_facts:
    bds_instance_id: ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
bds_instances:
    description:
        - List of BdsInstance resources
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
                        - Big Data Manager version installed in the cluster
                    returned: on success
                    type: string
                    sample: bdm_version_example
                bds_version:
                    description:
                        - Big Data Service version installed in the cluster
                    returned: on success
                    type: string
                    sample: bds_version_example
                os_version:
                    description:
                        - Oracle Linux version installed in the cluster
                    returned: on success
                    type: string
                    sample: os_version_example
                db_version:
                    description:
                        - Query Server Database version
                    returned: on success
                    type: string
                    sample: db_version_example
                bd_cell_version:
                    description:
                        - Cloud SQL cell version
                    returned: on success
                    type: string
                    sample: bd_cell_version_example
                csql_cell_version:
                    description:
                        - Big Data SQL version
                    returned: on success
                    type: string
                    sample: csql_cell_version_example
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
                hostname:
                    description:
                        - The fully-qualified hostname (FQDN) of the node
                    returned: on success
                    type: string
                    sample: hostname_example
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
    sample: [{
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
            "bds_version": "bds_version_example",
            "os_version": "os_version_example",
            "db_version": "db_version_example",
            "bd_cell_version": "bd_cell_version_example",
            "csql_cell_version": "csql_cell_version_example",
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
            "hostname": "hostname_example",
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.bds import BdsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BdsInstanceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "bds_instance_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_bds_instance,
            bds_instance_id=self.module.params.get("bds_instance_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_bds_instances,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


BdsInstanceFactsHelperCustom = get_custom_class("BdsInstanceFactsHelperCustom")


class ResourceFactsHelper(BdsInstanceFactsHelperCustom, BdsInstanceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            bds_instance_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "UPDATING",
                    "UPDATING_INFRA",
                    "SUSPENDING",
                    "SUSPENDED",
                    "RESUMING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bds_instance",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(bds_instances=result)


if __name__ == "__main__":
    main()
