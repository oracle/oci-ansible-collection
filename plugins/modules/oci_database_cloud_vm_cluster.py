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
module: oci_database_cloud_vm_cluster
short_description: Manage a CloudVmCluster resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CloudVmCluster resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a cloud VM cluster.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_cloud_vm_cluster_actions) module: add_virtual_machine,
      change_compartment, remove_virtual_machine."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet associated with the cloud VM cluster.
            - Required for create using I(state=present).
        type: str
    backup_subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup network subnet associated with the cloud VM
              cluster.
            - Required for create using I(state=present).
        type: str
    db_servers:
        description:
            - The list of DB servers.
        type: list
        elements: str
    cluster_name:
        description:
            - The cluster name for cloud VM cluster. The cluster name must begin with an alphabetic character, and may contain hyphens (-). Underscores (_) are
              not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.
        type: str
    data_storage_percentage:
        description:
            - The percentage assigned to DATA storage (user data and database files).
              The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 35, 40,
              60 and 80. The default is 80 percent assigned to DATA storage. See L(Storage
              Configuration,https://docs.cloud.oracle.com/Content/Database/Concepts/exaoverview.htm#Exadata) in the Exadata documentation for details on the
              impact of the configuration settings on storage.
        type: int
    cloud_exadata_infrastructure_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the cloud Exadata infrastructure resource.
            - Required for create using I(state=present).
        type: str
    hostname:
        description:
            - The hostname for the cloud VM cluster. The hostname must begin with an alphabetic character, and
              can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB
              systems, and 12 characters for Exadata systems.
            - The maximum length of the combined hostname and domain is 63 characters.
            - "**Note:** The hostname must be unique within the subnet. If it is not unique,
              the cloud VM Cluster will fail to provision."
            - Required for create using I(state=present).
        type: str
    domain:
        description:
            - A domain name used for the cloud VM cluster. If the Oracle-provided internet and VCN
              resolver is enabled for the specified subnet, the domain name for the subnet is used
              (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.
              Applies to Exadata Cloud Service instances only.
        type: str
    is_sparse_diskgroup_enabled:
        description:
            - If true, the sparse disk group is configured for the cloud VM cluster. If false, the sparse disk group is not created.
        type: bool
    is_local_backup_enabled:
        description:
            - If true, database backup on local Exadata storage is configured for the cloud VM cluster. If false, database backup on local Exadata storage is
              not available in the cloud VM cluster.
        type: bool
    time_zone:
        description:
            - The time zone to use for the cloud VM cluster. For details, see L(Time
              Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
        type: str
    scan_listener_port_tcp:
        description:
            - The TCP Single Client Access Name (SCAN) port. The default port is 1521.
        type: int
    scan_listener_port_tcp_ssl:
        description:
            - The TCPS Single Client Access Name (SCAN) port. The default port is 2484.
        type: int
    private_zone_id:
        description:
            - The private zone id in which DNS records need to be created.
        type: str
    gi_version:
        description:
            - A valid Oracle Grid Infrastructure (GI) software version.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - The user-friendly name for the cloud VM cluster. The name does not need to be unique.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    cpu_core_count:
        description:
            - "The number of CPU cores to enable for a cloud VM cluster. Valid values depend on the specified shape:"
            - "- Exadata.Base.48 - Specify a multiple of 2, from 0 to 48.
              - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84.
              - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168.
              - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.
              - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92.
              - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184.
              - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    ocpu_count:
        description:
            - The number of OCPU cores to enable for a cloud VM cluster. Only 1 decimal place is allowed for the fractional part.
            - This parameter is updatable.
        type: float
    memory_size_in_gbs:
        description:
            - The memory to be allocated in GBs.
            - This parameter is updatable.
        type: int
    db_node_storage_size_in_gbs:
        description:
            - The local node storage to be allocated in GBs.
            - This parameter is updatable.
        type: int
    data_storage_size_in_tbs:
        description:
            - The data disk group size to be allocated in TBs.
            - This parameter is updatable.
        type: float
    license_model:
        description:
            - The Oracle license model that applies to the cloud VM cluster. The default is BRING_YOUR_OWN_LICENSE.
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    ssh_public_keys:
        description:
            - The public key portion of one or more key pairs used for SSH access to the cloud VM cluster.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    update_details:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            update_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the maintenance update.
                    - This parameter is updatable.
                type: str
            update_action:
                description:
                    - The update action.
                    - This parameter is updatable.
                type: str
                choices:
                    - "ROLLING_APPLY"
                    - "NON_ROLLING_APPLY"
                    - "PRECHECK"
                    - "ROLLBACK"
    nsg_ids:
        description:
            - "The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) for the network security groups (NSGs) to which this
              resource belongs. Setting this to an empty list removes all resources from all NSGs. For more information about NSGs, see L(Security
              Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
              **NsgIds restrictions:**
              - A network security group (NSG) is optional for Autonomous Databases with private access. The nsgIds list can be empty."
            - This parameter is updatable.
        type: list
        elements: str
    backup_network_nsg_ids:
        description:
            - A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that the
              backup network of this DB system belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more
              information about NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm). Applicable only to Exadata
              systems.
            - This parameter is updatable.
        type: list
        elements: str
    compute_nodes:
        description:
            - The list of compute servers to be added to the cloud VM cluster.
            - This parameter is updatable.
        type: list
        elements: str
    storage_size_in_gbs:
        description:
            - The disk group size to be allocated in GBs.
            - This parameter is updatable.
        type: int
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - This parameter is updatable.
        type: dict
    data_collection_options:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_diagnostics_events_enabled:
                description:
                    - Indicates whether diagnostic collection is enabled for the VM cluster/Cloud VM cluster/VMBM DBCS. Enabling diagnostic collection allows
                      you to receive Events service notifications for guest VM issues. Diagnostic collection also allows Oracle to provide enhanced service and
                      proactive support for your Exadata system. You can enable diagnostic collection during VM cluster/Cloud VM cluster provisioning. You can
                      also disable or enable it at any time using the `UpdateVmCluster` or `updateCloudVmCluster` API.
                type: bool
            is_health_monitoring_enabled:
                description:
                    - Indicates whether health monitoring is enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling health monitoring allows Oracle
                      to collect diagnostic data and share it with its operations and support personnel. You may also receive notifications for some events.
                      Collecting health diagnostics enables Oracle to provide proactive support and enhanced service for your system.
                      Optionally enable health monitoring while provisioning a system. You can also disable or enable health monitoring anytime using the
                      `UpdateVmCluster`, `UpdateCloudVmCluster` or `updateDbsystem` API.
                type: bool
            is_incident_logs_enabled:
                description:
                    - Indicates whether incident logs and trace collection are enabled for the VM cluster / Cloud VM cluster / VMBM DBCS. Enabling incident logs
                      collection allows Oracle to receive Events service notifications for guest VM issues, collect incident logs and traces, and use them to
                      diagnose issues and resolve them.
                      Optionally enable incident logs collection while provisioning a system. You can also disable or enable incident logs collection anytime
                      using the `UpdateVmCluster`, `updateCloudVmCluster` or `updateDbsystem` API.
                type: bool
    cloud_vm_cluster_id:
        description:
            - The cloud VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the CloudVmCluster.
            - Use I(state=present) to create or update a CloudVmCluster.
            - Use I(state=absent) to delete a CloudVmCluster.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create cloud_vm_cluster
  oci_database_cloud_vm_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    backup_subnet_id: "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    cloud_exadata_infrastructure_id: "ocid1.cloudexadatainfrastructure.oc1..xxxxxxEXAMPLExxxxxx"
    hostname: hostname_example
    gi_version: gi_version_example
    display_name: display_name_example
    cpu_core_count: 56
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]

    # optional
    db_servers: [ "db_servers_example" ]
    cluster_name: cluster_name_example
    data_storage_percentage: 56
    domain: domain_example
    is_sparse_diskgroup_enabled: true
    is_local_backup_enabled: true
    time_zone: time_zone_example
    scan_listener_port_tcp: 56
    scan_listener_port_tcp_ssl: 56
    private_zone_id: "ocid1.privatezone.oc1..xxxxxxEXAMPLExxxxxx"
    ocpu_count: 3.4
    memory_size_in_gbs: 56
    db_node_storage_size_in_gbs: 56
    data_storage_size_in_tbs: 3.4
    license_model: LICENSE_INCLUDED
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_collection_options:
      # optional
      is_diagnostics_events_enabled: true
      is_health_monitoring_enabled: true
      is_incident_logs_enabled: true

- name: Update cloud_vm_cluster
  oci_database_cloud_vm_cluster:
    # required
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    cpu_core_count: 56
    ocpu_count: 3.4
    memory_size_in_gbs: 56
    db_node_storage_size_in_gbs: 56
    data_storage_size_in_tbs: 3.4
    license_model: LICENSE_INCLUDED
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    update_details:
      # optional
      update_id: "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx"
      update_action: ROLLING_APPLY
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    compute_nodes: [ "compute_nodes_example" ]
    storage_size_in_gbs: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_collection_options:
      # optional
      is_diagnostics_events_enabled: true
      is_health_monitoring_enabled: true
      is_incident_logs_enabled: true

- name: Update cloud_vm_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_cloud_vm_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    cpu_core_count: 56
    ocpu_count: 3.4
    memory_size_in_gbs: 56
    db_node_storage_size_in_gbs: 56
    data_storage_size_in_tbs: 3.4
    license_model: LICENSE_INCLUDED
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    update_details:
      # optional
      update_id: "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx"
      update_action: ROLLING_APPLY
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    compute_nodes: [ "compute_nodes_example" ]
    storage_size_in_gbs: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    data_collection_options:
      # optional
      is_diagnostics_events_enabled: true
      is_health_monitoring_enabled: true
      is_incident_logs_enabled: true

- name: Delete cloud_vm_cluster
  oci_database_cloud_vm_cluster:
    # required
    cloud_vm_cluster_id: "ocid1.cloudvmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete cloud_vm_cluster using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_cloud_vm_cluster:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
        memory_size_in_gbs:
            description:
                - The memory to be allocated in GBs.
            returned: on success
            type: int
            sample: 56
        db_node_storage_size_in_gbs:
            description:
                - The local node storage to be allocated in GBs.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_tbs:
            description:
                - The data disk group size to be allocated in TBs.
            returned: on success
            type: float
            sample: 1.2
        db_servers:
            description:
                - The list of DB servers.
            returned: on success
            type: list
            sample: []
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
        "memory_size_in_gbs": 56,
        "db_node_storage_size_in_gbs": 56,
        "data_storage_size_in_tbs": 1.2,
        "db_servers": [],
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
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateCloudVmClusterDetails
    from oci.database.models import UpdateCloudVmClusterDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CloudVmClusterHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(CloudVmClusterHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = oci_config_utils.create_service_client(
            self.module, WorkRequestClient
        )

    def get_possible_entity_types(self):
        return super(CloudVmClusterHelperGen, self).get_possible_entity_types() + [
            "cloudvmcluster",
            "cloudvmclusters",
            "databasecloudvmcluster",
            "databasecloudvmclusters",
            "cloudvmclusterresource",
            "cloudvmclustersresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "cloud_vm_cluster_id"

    def get_module_resource_id(self):
        return self.module.params.get("cloud_vm_cluster_id")

    def get_get_fn(self):
        return self.client.get_cloud_vm_cluster

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_vm_cluster, cloud_vm_cluster_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cloud_vm_cluster,
            cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "cloud_exadata_infrastructure_id",
            "display_name",
        ]

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
            self.client.list_cloud_vm_clusters, **kwargs
        )

    def get_create_model_class(self):
        return CreateCloudVmClusterDetails

    def get_exclude_attributes(self):
        return ["private_zone_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_cloud_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(create_cloud_vm_cluster_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateCloudVmClusterDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_cloud_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
                update_cloud_vm_cluster_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_cloud_vm_cluster,
            call_fn_args=(),
            call_fn_kwargs=dict(
                cloud_vm_cluster_id=self.module.params.get("cloud_vm_cluster_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


CloudVmClusterHelperCustom = get_custom_class("CloudVmClusterHelperCustom")


class ResourceHelper(CloudVmClusterHelperCustom, CloudVmClusterHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            subnet_id=dict(type="str"),
            backup_subnet_id=dict(type="str"),
            db_servers=dict(type="list", elements="str"),
            cluster_name=dict(type="str"),
            data_storage_percentage=dict(type="int"),
            cloud_exadata_infrastructure_id=dict(type="str"),
            hostname=dict(type="str"),
            domain=dict(type="str"),
            is_sparse_diskgroup_enabled=dict(type="bool"),
            is_local_backup_enabled=dict(type="bool"),
            time_zone=dict(type="str"),
            scan_listener_port_tcp=dict(type="int"),
            scan_listener_port_tcp_ssl=dict(type="int"),
            private_zone_id=dict(type="str"),
            gi_version=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            cpu_core_count=dict(type="int"),
            ocpu_count=dict(type="float"),
            memory_size_in_gbs=dict(type="int"),
            db_node_storage_size_in_gbs=dict(type="int"),
            data_storage_size_in_tbs=dict(type="float"),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            ssh_public_keys=dict(type="list", elements="str", no_log=True),
            update_details=dict(
                type="dict",
                options=dict(
                    update_id=dict(type="str"),
                    update_action=dict(
                        type="str",
                        choices=[
                            "ROLLING_APPLY",
                            "NON_ROLLING_APPLY",
                            "PRECHECK",
                            "ROLLBACK",
                        ],
                    ),
                ),
            ),
            nsg_ids=dict(type="list", elements="str"),
            backup_network_nsg_ids=dict(type="list", elements="str"),
            compute_nodes=dict(type="list", elements="str"),
            storage_size_in_gbs=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            data_collection_options=dict(
                type="dict",
                options=dict(
                    is_diagnostics_events_enabled=dict(type="bool"),
                    is_health_monitoring_enabled=dict(type="bool"),
                    is_incident_logs_enabled=dict(type="bool"),
                ),
            ),
            cloud_vm_cluster_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
