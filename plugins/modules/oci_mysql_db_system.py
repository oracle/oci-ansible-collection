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
module: oci_mysql_db_system
short_description: Manage a DbSystem resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DbSystem resource in Oracle Cloud Infrastructure
    - For I(state=present), creates and launches a DB System.
    - "This resource has the following action operations in the M(oracle.oci.oci_mysql_db_system_actions) module: restart, start, stop."
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
    source:
        description:
            - ""
        type: dict
        suboptions:
            backup_id:
                description:
                    - The OCID of the backup to be used as the source for the new DB System.
                    - Required when source_type is 'BACKUP'
                type: str
            source_url:
                description:
                    - "The Pre-Authenticated Request (PAR) of a bucket/prefix or PAR of a @.manifest.json object from the Object Storage.
                      Check L(Using Pre-Authenticated Requests,https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests.htm)
                      for information related to PAR creation.
                      Please create PAR with \\"Permit object reads\\" access type and \\"Enable Object Listing\\" permission when using a bucket/prefix PAR.
                      Please create PAR with \\"Permit object reads\\" access type when using a @.manifest.json object PAR."
                    - Required when source_type is 'IMPORTURL'
                type: str
            source_type:
                description:
                    - The specific source identifier.
                type: str
                choices:
                    - "BACKUP"
                    - "NONE"
                    - "IMPORTURL"
                    - "PITR"
                default: "NONE"
            db_system_id:
                description:
                    - The OCID of the DB System from which a backup shall be selected to be
                      restored when creating the new DB System. Use this together with
                      recovery point to perform a point in time recovery operation.
                    - Required when source_type is 'PITR'
                type: str
            recovery_point:
                description:
                    - The date and time, as per RFC 3339, of the change up to which the
                      new DB System shall be restored to, using a backup and logs from the
                      original DB System. In case no point in time is specified, then this
                      new DB System shall be restored up to the latest change recorded for
                      the original DB System.
                    - Applicable when source_type is 'PITR'
                type: str
    display_name:
        description:
            - The user-friendly name for the DB System. It does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - User-provided data about the DB System.
            - This parameter is updatable.
        type: str
    subnet_id:
        description:
            - The OCID of the subnet the DB System is associated with.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_highly_available:
        description:
            - Specifies if the DB System is highly available.
            - "When creating a DB System with High Availability, three instances
              are created and placed according to your region- and
              subnet-type. The secondaries are placed automatically in the other
              two availability or fault domains.  You can choose the preferred
              location of your primary instance, only."
            - This parameter is updatable.
        type: bool
    availability_domain:
        description:
            - The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.
            - In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains
              and the MySQL instance in that domain is promoted to the primary instance.
              This redirection does not affect the IP address of the DB System in any way.
            - For a standalone DB System, this defines the availability domain in which the DB System is placed.
            - This parameter is updatable.
        type: str
    fault_domain:
        description:
            - The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.
            - In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains
              and the MySQL instance in that domain is promoted to the primary instance.
              This redirection does not affect the IP address of the DB System in any way.
            - For a standalone DB System, this defines the fault domain in which the DB System is placed.
            - This parameter is updatable.
        type: str
    shape_name:
        description:
            - "The name of the shape. The shape determines the resources allocated
              - CPU cores and memory for VM shapes; CPU cores, memory and storage
              for non-VM (or bare metal) shapes. To get a list of shapes, use the
              L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/mysql/20190415/ShapeSummary/ListShapes) operation."
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    mysql_version:
        description:
            - The specific MySQL version identifier.
            - This parameter is updatable.
        type: str
    configuration_id:
        description:
            - The OCID of the Configuration to be used for this DB System.
            - This parameter is updatable.
        type: str
    admin_username:
        description:
            - The username for the administrative user.
            - This parameter is updatable.
        type: str
    admin_password:
        description:
            - The password for the administrative user. The password must be
              between 8 and 32 characters long, and must contain at least 1
              numeric character, 1 lowercase character, 1 uppercase character, and
              1 special (nonalphanumeric) character.
            - This parameter is updatable.
        type: str
    data_storage_size_in_gbs:
        description:
            - Initial size of the data volume in GBs that will be created and attached.
              Keep in mind that this only specifies the size of the database data volume,
              the log volume for the database will be scaled appropriately with its shape.
            - This parameter is updatable.
        type: int
    hostname_label:
        description:
            - The hostname for the primary endpoint of the DB System. Used for DNS.
            - "The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
              (for example, \\"dbsystem-1\\" in FQDN \\"dbsystem-1.subnet123.vcn1.oraclevcn.com\\")."
            - Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123.
            - This parameter is updatable.
        type: str
    ip_address:
        description:
            - "The IP address the DB System is configured to listen on.
              A private IP address of your choice to assign to the primary endpoint of the DB System.
              Must be an available IP address within the subnet's CIDR. If you don't specify a value,
              Oracle automatically assigns a private IP address from the subnet. This should be a
              \\"dotted-quad\\" style IPv4 address."
            - This parameter is updatable.
        type: str
    port:
        description:
            - The port for primary endpoint of the DB System to listen on.
            - This parameter is updatable.
        type: int
    port_x:
        description:
            - The TCP network port on which X Plugin listens for connections. This is the X Plugin equivalent of port.
            - This parameter is updatable.
        type: int
    backup_policy:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            is_enabled:
                description:
                    - Specifies if automatic backups are enabled.
                    - This parameter is updatable.
                type: bool
            window_start_time:
                description:
                    - The start of a 30-minute window of time in which daily, automated backups occur.
                    - "This should be in the format of the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be
                      truncated to zero."
                    - At some point in the window, the system may incur a brief service disruption as the backup is performed.
                    - This parameter is updatable.
                type: str
            retention_in_days:
                description:
                    - Number of days to retain an automatic backup.
                    - This parameter is updatable.
                type: int
            freeform_tags:
                description:
                    - Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                    - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                    - "Example: `{\\"bar-key\\": \\"value\\"}`"
                    - This parameter is updatable.
                type: dict
            defined_tags:
                description:
                    - Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                    - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                    - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                    - This parameter is updatable.
                type: dict
            pitr_policy:
                description:
                    - ""
                type: dict
                suboptions:
                    is_enabled:
                        description:
                            - Specifies if PITR is enabled or disabled.
                        type: bool
                        required: true
    maintenance:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            window_start_time:
                description:
                    - The start of the 2 hour maintenance window.
                    - "This string is of the format: \\"{day-of-week} {time-of-day}\\"."
                    - "\\"{day-of-week}\\" is a case-insensitive string like \\"mon\\", \\"tue\\", &c."
                    - "\\"{time-of-day}\\" is the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated to
                      zero."
                    - This parameter is updatable.
                type: str
    freeform_tags:
        description:
            - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    deletion_policy:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            automatic_backup_retention:
                description:
                    - Specifies if any automatic backups created for a DB System should be retained or deleted when the DB System is deleted.
                    - This parameter is updatable.
                type: str
                choices:
                    - "DELETE"
                    - "RETAIN"
            final_backup:
                description:
                    - "Specifies whether or not a backup is taken when the DB System is deleted.
                        REQUIRE_FINAL_BACKUP: a backup is taken if the DB System is deleted.
                        SKIP_FINAL_BACKUP: a backup is not taken if the DB System is deleted."
                    - This parameter is updatable.
                type: str
                choices:
                    - "SKIP_FINAL_BACKUP"
                    - "REQUIRE_FINAL_BACKUP"
            is_delete_protected:
                description:
                    - Specifies whether the DB System can be deleted. Set to true to prevent deletion, false (default) to allow.
                    - This parameter is updatable.
                type: bool
    crash_recovery:
        description:
            - Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled,
              and whether to enable or disable syncing of the Binary Logs.
            - This parameter is updatable.
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DbSystem.
            - Use I(state=present) to create or update a DbSystem.
            - Use I(state=absent) to delete a DbSystem.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create db_system
  oci_mysql_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    shape_name: shape_name_example

    # optional
    source:
      # required
      backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
      source_type: BACKUP
    display_name: display_name_example
    description: description_example
    is_highly_available: true
    availability_domain: Uocm:PHX-AD-1
    fault_domain: FAULT-DOMAIN-1
    mysql_version: mysql_version_example
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    admin_username: admin_username_example
    admin_password: example-password
    data_storage_size_in_gbs: 56
    hostname_label: hostname_label_example
    ip_address: ip_address_example
    port: 56
    port_x: 56
    backup_policy:
      # optional
      is_enabled: true
      window_start_time: window_start_time_example
      retention_in_days: 56
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      pitr_policy:
        # required
        is_enabled: true
    maintenance:
      # optional
      window_start_time: window_start_time_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    deletion_policy:
      # optional
      automatic_backup_retention: DELETE
      final_backup: SKIP_FINAL_BACKUP
      is_delete_protected: true
    crash_recovery: ENABLED

- name: Update db_system
  oci_mysql_db_system:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_highly_available: true
    availability_domain: Uocm:PHX-AD-1
    fault_domain: FAULT-DOMAIN-1
    shape_name: shape_name_example
    mysql_version: mysql_version_example
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    admin_username: admin_username_example
    admin_password: example-password
    data_storage_size_in_gbs: 56
    hostname_label: hostname_label_example
    ip_address: ip_address_example
    port: 56
    port_x: 56
    backup_policy:
      # optional
      is_enabled: true
      window_start_time: window_start_time_example
      retention_in_days: 56
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      pitr_policy:
        # required
        is_enabled: true
    maintenance:
      # optional
      window_start_time: window_start_time_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    deletion_policy:
      # optional
      automatic_backup_retention: DELETE
      final_backup: SKIP_FINAL_BACKUP
      is_delete_protected: true
    crash_recovery: ENABLED

- name: Update db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    is_highly_available: true
    availability_domain: Uocm:PHX-AD-1
    fault_domain: FAULT-DOMAIN-1
    shape_name: shape_name_example
    mysql_version: mysql_version_example
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    admin_username: admin_username_example
    admin_password: example-password
    data_storage_size_in_gbs: 56
    hostname_label: hostname_label_example
    ip_address: ip_address_example
    port: 56
    port_x: 56
    backup_policy:
      # optional
      is_enabled: true
      window_start_time: window_start_time_example
      retention_in_days: 56
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      pitr_policy:
        # required
        is_enabled: true
    maintenance:
      # optional
      window_start_time: window_start_time_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    deletion_policy:
      # optional
      automatic_backup_retention: DELETE
      final_backup: SKIP_FINAL_BACKUP
      is_delete_protected: true
    crash_recovery: ENABLED

- name: Delete db_system
  oci_mysql_db_system:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_mysql_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
db_system:
    description:
        - Details of the DbSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the DB System.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the DB System. It does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-provided data about the DB System.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment the DB System belongs in.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        subnet_id:
            description:
                - The OCID of the subnet the DB System is associated with.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        is_highly_available:
            description:
                - Specifies if the DB System is highly available.
            returned: on success
            type: bool
            sample: true
        current_placement:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                availability_domain:
                    description:
                        - The availability domain in which the DB System is placed.
                    returned: on success
                    type: str
                    sample: Uocm:PHX-AD-1
                fault_domain:
                    description:
                        - The fault domain in which the DB System is placed.
                    returned: on success
                    type: str
                    sample: FAULT-DOMAIN-1
        is_analytics_cluster_attached:
            description:
                - "DEPRECATED -- please use `isHeatWaveClusterAttached` instead.
                  If the DB System has an Analytics Cluster attached."
            returned: on success
            type: bool
            sample: true
        analytics_cluster:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape_name:
                    description:
                        - "The shape determines resources to allocate to the Analytics
                          Cluster nodes - CPU cores, memory."
                    returned: on success
                    type: str
                    sample: shape_name_example
                cluster_size:
                    description:
                        - The number of analytics-processing compute instances, of the
                          specified shape, in the Analytics Cluster.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the MySQL Analytics Cluster.
                    returned: on success
                    type: str
                    sample: lifecycle_state_example
                time_created:
                    description:
                        - The date and time the Analytics Cluster was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The time the Analytics Cluster was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        is_heat_wave_cluster_attached:
            description:
                - If the DB System has a HeatWave Cluster attached.
            returned: on success
            type: bool
            sample: true
        heat_wave_cluster:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                shape_name:
                    description:
                        - "The shape determines resources to allocate to the HeatWave
                          nodes - CPU cores, memory."
                    returned: on success
                    type: str
                    sample: shape_name_example
                cluster_size:
                    description:
                        - The number of analytics-processing compute instances, of the
                          specified shape, in the HeatWave cluster.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the MySQL HeatWave cluster.
                    returned: on success
                    type: str
                    sample: lifecycle_state_example
                time_created:
                    description:
                        - The date and time the HeatWave cluster was created,
                          as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The time the HeatWave cluster was last updated,
                          as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        availability_domain:
            description:
                - The availability domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.
                - In a failover scenario, the Read/Write endpoint is redirected to one of the other availability domains
                  and the MySQL instance in that domain is promoted to the primary instance.
                  This redirection does not affect the IP address of the DB System in any way.
                - For a standalone DB System, this defines the availability domain in which the DB System is placed.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        fault_domain:
            description:
                - The fault domain on which to deploy the Read/Write endpoint. This defines the preferred primary instance.
                - In a failover scenario, the Read/Write endpoint is redirected to one of the other fault domains
                  and the MySQL instance in that domain is promoted to the primary instance.
                  This redirection does not affect the IP address of the DB System in any way.
                - For a standalone DB System, this defines the fault domain in which the DB System is placed.
            returned: on success
            type: str
            sample: FAULT-DOMAIN-1
        shape_name:
            description:
                - "The shape of the primary instances of the DB System. The shape
                  determines resources allocated to a DB System - CPU cores
                  and memory for VM shapes; CPU cores, memory and storage for non-VM
                  (or bare metal) shapes. To get a list of shapes, use (the
                  L(ListShapes,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/mysql/20181021/ShapeSummary/ListShapes) operation."
            returned: on success
            type: str
            sample: shape_name_example
        mysql_version:
            description:
                - Name of the MySQL Version in use for the DB System.
            returned: on success
            type: str
            sample: mysql_version_example
        backup_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - If automated backups are enabled or disabled.
                    returned: on success
                    type: bool
                    sample: true
                window_start_time:
                    description:
                        - The start of a 30-minute window of time in which daily, automated backups occur.
                        - "This should be in the format of the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be
                          truncated to zero."
                        - At some point in the window, the system may incur a brief service disruption as the backup is performed.
                        - "If not defined, a window is selected from the following Region-based time-spans:
                          - eu-frankfurt-1: 20:00 - 04:00 UTC
                          - us-ashburn-1: 03:00 - 11:00 UTC
                          - uk-london-1: 06:00 - 14:00 UTC
                          - ap-tokyo-1: 13:00 - 21:00
                          - us-phoenix-1: 06:00 - 14:00"
                    returned: on success
                    type: str
                    sample: window_start_time_example
                retention_in_days:
                    description:
                        - The number of days automated backups are retained.
                    returned: on success
                    type: int
                    sample: 56
                freeform_tags:
                    description:
                        - Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                        - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                        - "Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                        - Tags defined here will be copied verbatim as tags on the Backup resource created by this BackupPolicy.
                        - "Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
                pitr_policy:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Specifies if PITR is enabled or disabled.
                            returned: on success
                            type: bool
                            sample: true
        source:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backup_id:
                    description:
                        - The OCID of the backup to be used as the source for the new DB System.
                    returned: on success
                    type: str
                    sample: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
                source_type:
                    description:
                        - The specific source identifier.
                    returned: on success
                    type: str
                    sample: NONE
                db_system_id:
                    description:
                        - The OCID of the DB System from which a backup shall be selected to be
                          restored when creating the new DB System. Use this together with
                          recovery point to perform a point in time recovery operation.
                    returned: on success
                    type: str
                    sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
                recovery_point:
                    description:
                        - The date and time, as per RFC 3339, of the change up to which the
                          new DB System shall be restored to, using a backup and logs from the
                          original DB System. In case no point in time is specified, then this
                          new DB System shall be restored up to the latest change recorded for
                          the original DB System.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        configuration_id:
            description:
                - The OCID of the Configuration to be used for Instances in this DB System.
            returned: on success
            type: str
            sample: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
        data_storage_size_in_gbs:
            description:
                - Initial size of the data volume in GiBs that will be created and attached.
            returned: on success
            type: int
            sample: 56
        hostname_label:
            description:
                - "The hostname for the primary endpoint of the DB System. Used for DNS.
                  The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
                  (for example, \\"dbsystem-1\\" in FQDN \\"dbsystem-1.subnet123.vcn1.oraclevcn.com\\").
                  Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123."
            returned: on success
            type: str
            sample: hostname_label_example
        ip_address:
            description:
                - "The IP address the DB System is configured to listen on. A private
                  IP address of the primary endpoint of the DB System. Must be an
                  available IP address within the subnet's CIDR. This will be a
                  \\"dotted-quad\\" style IPv4 address."
            returned: on success
            type: str
            sample: ip_address_example
        port:
            description:
                - The port for primary endpoint of the DB System to listen on.
            returned: on success
            type: int
            sample: 56
        port_x:
            description:
                - The network port on which X Plugin listens for TCP/IP connections. This is the X Plugin equivalent of port.
            returned: on success
            type: int
            sample: 56
        endpoints:
            description:
                - The network endpoints available for this DB System.
            returned: on success
            type: complex
            contains:
                hostname:
                    description:
                        - The network address of the DB System.
                    returned: on success
                    type: str
                    sample: hostname_example
                ip_address:
                    description:
                        - The IP address the DB System is configured to listen on.
                    returned: on success
                    type: str
                    sample: ip_address_example
                port:
                    description:
                        - The port the MySQL instance listens on.
                    returned: on success
                    type: int
                    sample: 56
                port_x:
                    description:
                        - The network port where to connect to use this endpoint using the X protocol.
                    returned: on success
                    type: int
                    sample: 56
                modes:
                    description:
                        - The access modes from the client that this endpoint supports.
                    returned: on success
                    type: list
                    sample: []
                status:
                    description:
                        - The state of the endpoints, as far as it can seen from the DB System.
                          There may be some inconsistency with the actual state of the MySQL service.
                    returned: on success
                    type: str
                    sample: ACTIVE
                status_details:
                    description:
                        - Additional information about the current endpoint status.
                    returned: on success
                    type: str
                    sample: status_details_example
        channels:
            description:
                - A list with a summary of all the Channels attached to the DB System.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The OCID of the Channel.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The OCID of the compartment.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                is_enabled:
                    description:
                        - Whether the Channel has been enabled by the user.
                    returned: on success
                    type: bool
                    sample: true
                source:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        source_type:
                            description:
                                - The specific source identifier.
                            returned: on success
                            type: str
                            sample: MYSQL
                        hostname:
                            description:
                                - The network address of the MySQL instance.
                            returned: on success
                            type: str
                            sample: hostname_example
                        port:
                            description:
                                - The port the source MySQL instance listens on.
                            returned: on success
                            type: int
                            sample: 56
                        username:
                            description:
                                - The name of the replication user on the source MySQL instance.
                                  The username has a maximum length of 96 characters. For more information,
                                  please see the L(MySQL documentation,https://dev.mysql.com/doc/refman/8.0/en/change-master-to.html)
                            returned: on success
                            type: str
                            sample: username_example
                        ssl_mode:
                            description:
                                - The SSL mode of the Channel.
                            returned: on success
                            type: str
                            sample: VERIFY_IDENTITY
                        ssl_ca_certificate:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                certificate_type:
                                    description:
                                        - The type of CA certificate.
                                    returned: on success
                                    type: str
                                    sample: PEM
                                contents:
                                    description:
                                        - The string containing the CA certificate in PEM format.
                                    returned: on success
                                    type: str
                                    sample: contents_example
                target:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        target_type:
                            description:
                                - The specific target identifier.
                            returned: on success
                            type: str
                            sample: DBSYSTEM
                        db_system_id:
                            description:
                                - The OCID of the source DB System.
                            returned: on success
                            type: str
                            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
                        channel_name:
                            description:
                                - The case-insensitive name that identifies the replication channel. Channel names
                                  must follow the rules defined for L(MySQL identifiers,https://dev.mysql.com/doc/refman/8.0/en/identifiers.html).
                                  The names of non-Deleted Channels must be unique for each DB System.
                            returned: on success
                            type: str
                            sample: channel_name_example
                        applier_username:
                            description:
                                - The username for the replication applier of the target MySQL DB System.
                            returned: on success
                            type: str
                            sample: applier_username_example
                lifecycle_state:
                    description:
                        - The state of the Channel.
                    returned: on success
                    type: str
                    sample: lifecycle_state_example
                lifecycle_details:
                    description:
                        - A message describing the state of the Channel.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                display_name:
                    description:
                        - The user-friendly name for the Channel. It does not have to be unique.
                    returned: on success
                    type: str
                    sample: display_name_example
                time_created:
                    description:
                        - The date and time the Channel was created, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The time the Channel was last updated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                freeform_tags:
                    description:
                        - "Simple key-value pair applied without any predefined name, type or scope. Exists for cross-compatibility only.
                          Example: `{\\"bar-key\\": \\"value\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - "Usage of predefined tag keys. These predefined keys are scoped to namespaces.
                          Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
        lifecycle_state:
            description:
                - The current state of the DB System.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: str
            sample: lifecycle_details_example
        maintenance:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                window_start_time:
                    description:
                        - The start time of the maintenance window.
                        - "This string is of the format: \\"{day-of-week} {time-of-day}\\"."
                        - "\\"{day-of-week}\\" is a case-insensitive string like \\"mon\\", \\"tue\\", &c."
                        - "\\"{time-of-day}\\" is the \\"Time\\" portion of an RFC3339-formatted timestamp. Any second or sub-second time data will be truncated
                          to zero."
                    returned: on success
                    type: str
                    sample: window_start_time_example
        deletion_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                automatic_backup_retention:
                    description:
                        - Specifies if any automatic backups created for a DB System should be retained or deleted when the DB System is deleted.
                    returned: on success
                    type: str
                    sample: DELETE
                final_backup:
                    description:
                        - "Specifies whether or not a backup is taken when the DB System is deleted.
                            REQUIRE_FINAL_BACKUP: a backup is taken if the DB System is deleted.
                            SKIP_FINAL_BACKUP: a backup is not taken if the DB System is deleted."
                    returned: on success
                    type: str
                    sample: SKIP_FINAL_BACKUP
                is_delete_protected:
                    description:
                        - Specifies whether the DB System can be deleted. Set to true to prevent deletion, false (default) to allow.
                    returned: on success
                    type: bool
                    sample: true
        time_created:
            description:
                - The date and time the DB System was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the DB System was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        crash_recovery:
            description:
                - Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled,
                  and whether to enable or disable syncing of the Binary Logs.
            returned: on success
            type: str
            sample: ENABLED
        point_in_time_recovery_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                time_earliest_recovery_point:
                    description:
                        - Earliest recovery time point for the DB System, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_latest_recovery_point:
                    description:
                        - Latest recovery time point for the DB System, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc3339).
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "is_highly_available": true,
        "current_placement": {
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": "FAULT-DOMAIN-1"
        },
        "is_analytics_cluster_attached": true,
        "analytics_cluster": {
            "shape_name": "shape_name_example",
            "cluster_size": 56,
            "lifecycle_state": "lifecycle_state_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        },
        "is_heat_wave_cluster_attached": true,
        "heat_wave_cluster": {
            "shape_name": "shape_name_example",
            "cluster_size": 56,
            "lifecycle_state": "lifecycle_state_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        },
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domain": "FAULT-DOMAIN-1",
        "shape_name": "shape_name_example",
        "mysql_version": "mysql_version_example",
        "backup_policy": {
            "is_enabled": true,
            "window_start_time": "window_start_time_example",
            "retention_in_days": 56,
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}},
            "pitr_policy": {
                "is_enabled": true
            }
        },
        "source": {
            "backup_id": "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx",
            "source_type": "NONE",
            "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
            "recovery_point": "2013-10-20T19:20:30+01:00"
        },
        "configuration_id": "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx",
        "data_storage_size_in_gbs": 56,
        "hostname_label": "hostname_label_example",
        "ip_address": "ip_address_example",
        "port": 56,
        "port_x": 56,
        "endpoints": [{
            "hostname": "hostname_example",
            "ip_address": "ip_address_example",
            "port": 56,
            "port_x": 56,
            "modes": [],
            "status": "ACTIVE",
            "status_details": "status_details_example"
        }],
        "channels": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "is_enabled": true,
            "source": {
                "source_type": "MYSQL",
                "hostname": "hostname_example",
                "port": 56,
                "username": "username_example",
                "ssl_mode": "VERIFY_IDENTITY",
                "ssl_ca_certificate": {
                    "certificate_type": "PEM",
                    "contents": "contents_example"
                }
            },
            "target": {
                "target_type": "DBSYSTEM",
                "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
                "channel_name": "channel_name_example",
                "applier_username": "applier_username_example"
            },
            "lifecycle_state": "lifecycle_state_example",
            "lifecycle_details": "lifecycle_details_example",
            "display_name": "display_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        }],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "maintenance": {
            "window_start_time": "window_start_time_example"
        },
        "deletion_policy": {
            "automatic_backup_retention": "DELETE",
            "final_backup": "SKIP_FINAL_BACKUP",
            "is_delete_protected": true
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "crash_recovery": "ENABLED",
        "point_in_time_recovery_details": {
            "time_earliest_recovery_point": "2013-10-20T19:20:30+01:00",
            "time_latest_recovery_point": "2013-10-20T19:20:30+01:00"
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
    from oci.mysql import WorkRequestsClient
    from oci.mysql import DbSystemClient
    from oci.mysql.models import CreateDbSystemDetails
    from oci.mysql.models import UpdateDbSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlDbSystemHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    def get_possible_entity_types(self):
        return super(MysqlDbSystemHelperGen, self).get_possible_entity_types() + [
            "dbsystem",
            "dbsystems",
            "mysqldbsystem",
            "mysqldbsystems",
            "dbsystemresource",
            "dbsystemsresource",
            "mysql",
        ]

    def get_module_resource_id_param(self):
        return "db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_system_id")

    def get_get_fn(self):
        return self.client.get_db_system

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system, db_system_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["db_system_id", "display_name"]
            if self._use_name_as_identifier()
            else ["db_system_id", "display_name", "configuration_id"]
        )

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
            self.client.list_db_systems, **kwargs
        )

    def get_create_model_class(self):
        return CreateDbSystemDetails

    def get_exclude_attributes(self):
        return ["admin_username", "source.source_url", "admin_password"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(create_db_system_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDbSystemDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_system_id=self.module.params.get("db_system_id"),
                update_db_system_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(db_system_id=self.module.params.get("db_system_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlDbSystemHelperCustom = get_custom_class("MysqlDbSystemHelperCustom")


class ResourceHelper(MysqlDbSystemHelperCustom, MysqlDbSystemHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            source=dict(
                type="dict",
                options=dict(
                    backup_id=dict(type="str"),
                    source_url=dict(type="str"),
                    source_type=dict(
                        type="str",
                        default="NONE",
                        choices=["BACKUP", "NONE", "IMPORTURL", "PITR"],
                    ),
                    db_system_id=dict(type="str"),
                    recovery_point=dict(type="str"),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            subnet_id=dict(type="str"),
            is_highly_available=dict(type="bool"),
            availability_domain=dict(type="str"),
            fault_domain=dict(type="str"),
            shape_name=dict(type="str"),
            mysql_version=dict(type="str"),
            configuration_id=dict(type="str"),
            admin_username=dict(type="str"),
            admin_password=dict(type="str", no_log=True),
            data_storage_size_in_gbs=dict(type="int"),
            hostname_label=dict(type="str"),
            ip_address=dict(type="str"),
            port=dict(type="int"),
            port_x=dict(type="int"),
            backup_policy=dict(
                type="dict",
                options=dict(
                    is_enabled=dict(type="bool"),
                    window_start_time=dict(type="str"),
                    retention_in_days=dict(type="int"),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                    pitr_policy=dict(
                        type="dict",
                        options=dict(is_enabled=dict(type="bool", required=True)),
                    ),
                ),
            ),
            maintenance=dict(
                type="dict", options=dict(window_start_time=dict(type="str"))
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            deletion_policy=dict(
                type="dict",
                options=dict(
                    automatic_backup_retention=dict(
                        type="str", choices=["DELETE", "RETAIN"]
                    ),
                    final_backup=dict(
                        type="str",
                        choices=["SKIP_FINAL_BACKUP", "REQUIRE_FINAL_BACKUP"],
                    ),
                    is_delete_protected=dict(type="bool"),
                ),
            ),
            crash_recovery=dict(type="str", choices=["ENABLED", "DISABLED"]),
            db_system_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_system",
        service_client_class=DbSystemClient,
        namespace="mysql",
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
