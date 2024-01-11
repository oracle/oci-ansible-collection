#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_db_node_facts
short_description: Fetches details about one or multiple DbNode resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbNode resources in Oracle Cloud Infrastructure
    - Lists the database nodes in the specified DB system and compartment. A database node is a server running database software.
    - If I(db_node_id) is specified, the details of a single DbNode will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_node_id:
        description:
            - The database node L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific db_node.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple db_nodes.
        type: str
    db_system_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm). If provided, filters the results to the set of
              database versions which are supported for the DB system.
        type: str
    vm_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster.
        type: str
    sort_by:
        description:
            - Sort by TIMECREATED.  Default order for TIMECREATED is descending.
        type: str
        choices:
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "STOPPING"
            - "STOPPED"
            - "STARTING"
            - "TERMINATING"
            - "TERMINATED"
            - "FAILED"
    db_server_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exacc Db server.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific db_node
  oci_database_db_node_facts:
    # required
    db_node_id: "ocid1.dbnode.oc1..xxxxxxEXAMPLExxxxxx"

- name: List db_nodes
  oci_database_db_node_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: PROVISIONING
    db_server_id: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
db_nodes:
    description:
        - List of DbNode resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database node.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        vnic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VNIC.
            returned: on success
            type: str
            sample: "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx"
        backup_vnic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup VNIC.
            returned: on success
            type: str
            sample: "ocid1.backupvnic.oc1..xxxxxxEXAMPLExxxxxx"
        host_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the host IP address associated with the database node.
                  Use this OCID with either the
                  L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/GetPrivateIp) or the
                  L(GetPublicIpByPrivateIpId,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PublicIp/GetPublicIpByPrivateIpId) API to get the
                  IP address
                  needed to make a database connection.
                - "**Note:** Applies only to Exadata Cloud Service."
            returned: on success
            type: str
            sample: "ocid1.hostip.oc1..xxxxxxEXAMPLExxxxxx"
        backup_ip_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup IP address associated with the database node.
                  Use this OCID with either the
                  L(GetPrivateIp,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PrivateIp/GetPrivateIp) or the
                  L(GetPublicIpByPrivateIpId,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/20160918/PublicIp/GetPublicIpByPrivateIpId) API to get the
                  IP address
                  needed to make a database connection.
                - "**Note:** Applies only to Exadata Cloud Service."
            returned: on success
            type: str
            sample: "ocid1.backupip.oc1..xxxxxxEXAMPLExxxxxx"
        vnic2_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the second VNIC.
                - "**Note:** Applies only to Exadata Cloud Service."
            returned: on success
            type: str
            sample: "ocid1.vnic2.oc1..xxxxxxEXAMPLExxxxxx"
        backup_vnic2_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the second backup VNIC.
                - "**Note:** Applies only to Exadata Cloud Service."
            returned: on success
            type: str
            sample: "ocid1.backupvnic2.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the database node.
            returned: on success
            type: str
            sample: PROVISIONING
        hostname:
            description:
                - The host name for the database node.
            returned: on success
            type: str
            sample: hostname_example
        fault_domain:
            description:
                - The name of the Fault Domain the instance is contained in.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        time_created:
            description:
                - The date and time that the database node was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        software_storage_size_in_gb:
            description:
                - The size (in GB) of the block storage volume allocation for the DB system. This attribute applies only for virtual machine DB systems.
            returned: on success
            type: int
            sample: 56
        maintenance_type:
            description:
                - The type of database node maintenance.
            returned: on success
            type: str
            sample: VMDB_REBOOT_MIGRATION
        time_maintenance_window_start:
            description:
                - Start date and time of maintenance window.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_maintenance_window_end:
            description:
                - End date and time of maintenance window.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        additional_details:
            description:
                - Additional information about the planned maintenance.
            returned: on success
            type: str
            sample: additional_details_example
        cpu_core_count:
            description:
                - The number of CPU cores enabled on the Db node.
            returned: on success
            type: int
            sample: 56
        memory_size_in_gbs:
            description:
                - The allocated memory in GBs on the Db node.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The allocated local node storage in GBs on the Db node.
            returned: on success
            type: int
            sample: 56
        db_server_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exacc Db server associated with the database node.
            returned: on success
            type: str
            sample: "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx"
        primary_private_ip:
            description:
                - The private IP of the primary VNIC attached to this db node
            returned: on success
            type: str
            sample: 10.0.0.10
        primary_public_ip:
            description:
                - The public IP of the primary VNIC attached to this db node
            returned: on success
            type: str
            sample: 140.34.93.209
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "vnic_id": "ocid1.vnic.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_vnic_id": "ocid1.backupvnic.oc1..xxxxxxEXAMPLExxxxxx",
        "host_ip_id": "ocid1.hostip.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_ip_id": "ocid1.backupip.oc1..xxxxxxEXAMPLExxxxxx",
        "vnic2_id": "ocid1.vnic2.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_vnic2_id": "ocid1.backupvnic2.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "hostname": "hostname_example",
        "fault_domain": "FAULT-DOMAIN-1",
        "time_created": "2013-10-20T19:20:30+01:00",
        "software_storage_size_in_gb": 56,
        "maintenance_type": "VMDB_REBOOT_MIGRATION",
        "time_maintenance_window_start": "2013-10-20T19:20:30+01:00",
        "time_maintenance_window_end": "2013-10-20T19:20:30+01:00",
        "additional_details": "additional_details_example",
        "cpu_core_count": 56,
        "memory_size_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "db_server_id": "ocid1.dbserver.oc1..xxxxxxEXAMPLExxxxxx",
        "primary_private_ip": "10.0.0.10",
        "primary_public_ip": "140.34.93.209"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbNodeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_node_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_node, db_node_id=self.module.params.get("db_node_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "db_system_id",
            "vm_cluster_id",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "db_server_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_nodes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DbNodeFactsHelperCustom = get_custom_class("DbNodeFactsHelperCustom")


class ResourceFactsHelper(DbNodeFactsHelperCustom, DbNodeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            db_node_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            db_system_id=dict(type="str"),
            vm_cluster_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "STOPPING",
                    "STOPPED",
                    "STARTING",
                    "TERMINATING",
                    "TERMINATED",
                    "FAILED",
                ],
            ),
            db_server_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_node",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_nodes=result)


if __name__ == "__main__":
    main()
