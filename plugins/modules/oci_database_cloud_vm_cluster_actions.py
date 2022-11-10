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
module: oci_database_cloud_vm_cluster_actions
short_description: Perform actions on a CloudVmCluster resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a CloudVmCluster resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a cloud VM cluster and its dependent resources to another compartment. Applies to Exadata Cloud Service instances
      and Autonomous Database on dedicated Exadata infrastructure only.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    cloud_vm_cluster_id:
        description:
            - The cloud VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the CloudVmCluster.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on cloud_vm_cluster
  oci_database_cloud_vm_cluster_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
cloud_vm_cluster:
    description:
        - Details of the CloudVmCluster resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        iorm_config_cache:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                lifecycle_state:
                    description:
                        - The current state of IORM configuration for the Exadata DB system.
                    returned: on success
                    type: str
                    sample: BOOTSTRAPPING
                lifecycle_details:
                    description:
                        - Additional information about the current `lifecycleState`.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                objective:
                    description:
                        - The current value for the IORM objective.
                          The default is `AUTO`.
                    returned: on success
                    type: str
                    sample: LOW_LATENCY
                db_plans:
                    description:
                        - An array of IORM settings for all the database in
                          the Exadata DB system.
                    returned: on success
                    type: complex
                    contains:
                        db_name:
                            description:
                                - The database name. For the default `DbPlan`, the `dbName` is `default`.
                            returned: on success
                            type: str
                            sample: db_name_example
                        share:
                            description:
                                - The relative priority of this database.
                            returned: on success
                            type: int
                            sample: 56
                        flash_cache_limit:
                            description:
                                - The flash cache limit for this database. This value is internally configured based on the share value assigned to the
                                  database.
                            returned: on success
                            type: str
                            sample: flash_cache_limit_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud VM cluster.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        availability_domain:
            description:
                - The name of the availability domain that the cloud Exadata infrastructure resource is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet associated with the cloud VM cluster.
                - "**Subnet Restrictions:**
                  - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20."
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and backup subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        backup_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup network subnet associated with the cloud VM
                  cluster.
                - "**Subnet Restriction:** See the subnet restrictions information for **subnetId**."
            returned: on success
            type: str
            sample: "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - "The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the network security groups (NSGs) to which
                  this resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see L(Security
                  Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
                  **NsgIds restrictions:**
                  - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty."
            returned: on success
            type: list
            sample: []
        backup_network_nsg_ids:
            description:
                - A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that the
                  backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For
                  more information about NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm). Applicable only
                  to Exadata systems.
            returned: on success
            type: list
            sample: []
        last_update_history_entry_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance update history entry. This value is
                  updated when a maintenance update starts.
            returned: on success
            type: str
            sample: "ocid1.lastupdatehistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
        shape:
            description:
                - The model name of the Exadata hardware running the cloud VM cluster.
            returned: on success
            type: str
            sample: shape_example
        listener_port:
            description:
                - The port number configured for the listener on the cloud VM cluster.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the cloud VM cluster.
            returned: on success
            type: str
            sample: PROVISIONING
        node_count:
            description:
                - The number of nodes in the cloud VM cluster.
            returned: on success
            type: int
            sample: 56
        storage_size_in_gbs:
            description:
                - The storage allocation for the disk group, in gigabytes (GB).
            returned: on success
            type: int
            sample: 56
        display_name:
            description:
                - The user-friendly name for the cloud VM cluster. The name does not need to be unique.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time that the cloud VM cluster was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_zone:
            description:
                - The time zone of the cloud VM cluster. For details, see L(Exadata Infrastructure Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: str
            sample: time_zone_example
        hostname:
            description:
                - The hostname for the cloud VM cluster.
            returned: on success
            type: str
            sample: hostname_example
        domain:
            description:
                - The domain name for the cloud VM cluster.
            returned: on success
            type: str
            sample: domain_example
        cpu_core_count:
            description:
                - The number of CPU cores enabled on the cloud VM cluster.
            returned: on success
            type: int
            sample: 56
        ocpu_count:
            description:
                - The number of OCPU cores to enable on the cloud VM cluster. Only 1 decimal place is allowed for the fractional part.
            returned: on success
            type: float
            sample: 3.4
        cluster_name:
            description:
                - The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_)
                  are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.
            returned: on success
            type: str
            sample: cluster_name_example
        data_storage_percentage:
            description:
                - The percentage assigned to DATA storage (user data and database files).
                  The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35,
                  40, 60 and 80. The default is 80 percent assigned to DATA storage. See L(Storage
                  Configuration,https://docs.cloud.oracle.com/Content/Database/Concepts/exaoverview.htm#Exadata) in the Exadata documentation for details on the
                  impact of the configuration settings on storage.
            returned: on success
            type: int
            sample: 56
        is_local_backup_enabled:
            description:
                - If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage
                  is not available in the cloud VM cluster.
            returned: on success
            type: bool
            sample: true
        cloud_exadata_infrastructure_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud Exadata infrastructure.
            returned: on success
            type: str
            sample: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
        is_sparse_diskgroup_enabled:
            description:
                - If true, sparse disk group is configured for the cloud VM cluster. If false, sparse disk group is not created.
            returned: on success
            type: bool
            sample: true
        gi_version:
            description:
                - A valid Oracle Grid Infrastructure (GI) software version.
            returned: on success
            type: str
            sample: gi_version_example
        system_version:
            description:
                - Operating system version of the image.
            returned: on success
            type: str
            sample: system_version_example
        ssh_public_keys:
            description:
                - The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.
            returned: on success
            type: list
            sample: [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ]
        license_model:
            description:
                - The Oracle license model that applies to the cloud VM cluster. The default is LICENSE_INCLUDED.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        disk_redundancy:
            description:
                - The type of redundancy configured for the cloud Vm cluster.
                  NORMAL is 2-way redundancy.
                  HIGH is 3-way redundancy.
            returned: on success
            type: str
            sample: HIGH
        scan_ip_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Single Client Access Name (SCAN) IP addresses
                  associated with the cloud VM cluster.
                  SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
                  Oracle Clusterware directs the requests to the appropriate nodes in the cluster.
                - "**Note:** For a single-node DB system, this list is empty."
            returned: on success
            type: list
            sample: []
        vip_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the virtual IP (VIP) addresses associated with the cloud
                  VM cluster.
                  The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the Exadata Cloud Service instance to
                  enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.
                - "**Note:** For a single-node DB system, this list is empty."
            returned: on success
            type: list
            sample: []
        scan_dns_record_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DNS record for the SCAN IP addresses that are
                  associated with the cloud VM cluster.
            returned: on success
            type: str
            sample: "ocid1.scandnsrecord.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        scan_dns_name:
            description:
                - The FQDN of the DNS record for the SCAN IP addresses that are associated with the cloud VM cluster.
            returned: on success
            type: str
            sample: scan_dns_name_example
        zone_id:
            description:
                - The OCID of the zone the cloud VM cluster is associated with.
            returned: on success
            type: str
            sample: "ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx"
        scan_listener_port_tcp:
            description:
                - The TCP Single Client Access Name (SCAN) port. The default port is 1521.
            returned: on success
            type: int
            sample: 56
        scan_listener_port_tcp_ssl:
            description:
                - The TCPS Single Client Access Name (SCAN) port. The default port is 2484.
            returned: on success
            type: int
            sample: 56
        data_collection_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_diagnostics_events_enabled:
                    description:
                        - Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS. Enabling diagnostic collection
                          allows you to receive Events service notifications for guest VM issues. Diagnostic collection also allows Oracle to provide enhanced
                          service and proactive support for your Exadata system. You can enable diagnostic collection during VM cluster/Cloud VM cluster
                          provisioning. You can also disable or enable it at any time using the `UpdateVmCluster` or `updateCloudVmCluster` API.
                    returned: on success
                    type: bool
                    sample: true
                is_health_monitoring_enabled:
                    description:
                        - Indicates whether health monitoring is enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling health monitoring allows
                          Oracle to collect diagnostic data and share it with its operations and support personnel. You may also receive notifications for some
                          events. Collecting health diagnostics enables Oracle to provide proactive support and enhanced service for your system.
                          Optionally enable health monitoring while provisioning a system. You can also disable or enable health monitoring anytime using the
                          `UpdateVmCluster`, `UpdateCloudVmCluster` or `updateDbsystem` API.
                    returned: on success
                    type: bool
                    sample: true
                is_incident_logs_enabled:
                    description:
                        - Indicates whether incident logs and trace collection are enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling incident
                          logs collection allows Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces, and use
                          them to diagnose issues and resolve them.
                          Optionally enable incident logs collection while provisioning a system. You can also disable or enable incident logs collection
                          anytime using the `UpdateVmCluster`, `updateCloudVmCluster` or `updateDbsystem` API.
                    returned: on success
                    type: bool
                    sample: true
    sample: {
        "iorm_config_cache": {
            "lifecycle_state": "BOOTSTRAPPING",
            "lifecycle_details": "lifecycle_details_example",
            "objective": "LOW_LATENCY",
            "db_plans": [{
                "db_name": "db_name_example",
                "share": 56,
                "flash_cache_limit": "flash_cache_limit_example"
            }]
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "availability_domain": "Uocm:PHX-AD-1",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_subnet_id": "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "backup_network_nsg_ids": [],
        "last_update_history_entry_id": "ocid1.lastupdatehistoryentry.oc1..xxxxxxEXAMPLExxxxxx",
        "shape": "shape_example",
        "listener_port": 56,
        "lifecycle_state": "PROVISIONING",
        "node_count": 56,
        "storage_size_in_gbs": 56,
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "time_zone": "time_zone_example",
        "hostname": "hostname_example",
        "domain": "domain_example",
        "cpu_core_count": 56,
        "ocpu_count": 3.4,
        "cluster_name": "cluster_name_example",
        "data_storage_percentage": 56,
        "is_local_backup_enabled": true,
        "cloud_exadata_infrastructure_id": "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx",
        "is_sparse_diskgroup_enabled": true,
        "gi_version": "gi_version_example",
        "system_version": "system_version_example",
        "ssh_public_keys": [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ],
        "license_model": "LICENSE_INCLUDED",
        "disk_redundancy": "HIGH",
        "scan_ip_ids": [],
        "vip_ids": [],
        "scan_dns_record_id": "ocid1.scandnsrecord.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "scan_dns_name": "scan_dns_name_example",
        "zone_id": "ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx",
        "scan_listener_port_tcp": 56,
        "scan_listener_port_tcp_ssl": 56,
        "data_collection_options": {
            "is_diagnostics_events_enabled": true,
            "is_health_monitoring_enabled": true,
            "is_incident_logs_enabled": true
        }
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import ChangeCloudVmClusterCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CloudVmClusterActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    def __init__(self, *args, **kwargs):
        super(CloudVmClusterActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "cloud_vm_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cloud_vm_cluster_id")

    def get_get_fn(self):
        return self.client.get_cloud_vm_cluster

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_vm_cluster,
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeCloudVmClusterCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_cloud_vm_cluster_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                change_cloud_vm_cluster_compartment_details=action_details,
                cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


CloudVmClusterActionsHelperCustom = get_custom_class(
    "CloudVmClusterActionsHelperCustom"
)


class ResourceHelper(CloudVmClusterActionsHelperCustom, CloudVmClusterActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            cloud_vm_cluster_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="cloud_vm_cluster",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
