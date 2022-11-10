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
module: oci_bds_instance_facts
short_description: Fetches details about one or multiple BdsInstance resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BdsInstance resources in Oracle Cloud Infrastructure
    - Returns a list of all Big Data Service clusters in a compartment.
    - If I(bds_instance_id) is specified, the details of a single BdsInstance will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the cluster.
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
            - The state of the cluster.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "UPDATING"
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
- name: Get a specific bds_instance
  oci_bds_instance_facts:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

- name: List bds_instances
  oci_bds_instance_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    sort_by: timeCreated
    sort_order: ASC
    display_name: display_name_example

"""

RETURN = """
bds_instances:
    description:
        - List of BdsInstance resources
    returned: on success
    type: complex
    contains:
        network_config:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: str
            sample: created_by_example
        time_updated:
            description:
                - The time the cluster was updated, shown as an RFC 3339 formatted datetime string.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        bootstrap_script_url:
            description:
                - pre-authenticated URL of the bootstrap script in Object Store that can be downloaded and executed.
                - Returned for get operation
            returned: on success
            type: str
            sample: bootstrap_script_url_example
        kms_key_id:
            description:
                - The OCID of the Key Management master encryption key.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
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
        number_of_nodes:
            description:
                - Number of nodes that forming the cluster
            returned: on success
            type: int
            sample: 56
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
        time_created:
            description:
                - The time the cluster was created, shown as an RFC 3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
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
        "time_updated": "2013-10-20T19:20:30+01:00",
        "bootstrap_script_url": "bootstrap_script_url_example",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "CREATING",
        "number_of_nodes": 56,
        "cluster_version": "CDH5",
        "is_high_availability": true,
        "is_secure": true,
        "is_cloud_sql_configured": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
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

    module = OCIAnsibleModule(argument_spec=module_args)

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
