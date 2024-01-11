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
module: oci_mysql_db_system_facts
short_description: Fetches details about one or multiple DbSystem resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbSystem resources in Oracle Cloud Infrastructure
    - Get a list of DB Systems in the specified compartment.
      The default sort order is by timeUpdated, descending.
    - If I(db_system_id) is specified, the details of a single DbSystem will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple db_systems.
        type: str
    is_heat_wave_cluster_attached:
        description:
            - If true, return only DB Systems with a HeatWave cluster attached, if false
              return only DB Systems with no HeatWave cluster attached. If not
              present, return all DB Systems.
        type: bool
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific db_system.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A filter to return only the resource matching the given display name exactly.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - DbSystem Lifecycle State
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    configuration_id:
        description:
            - The requested Configuration instance.
        type: str
    is_up_to_date:
        description:
            - Filter instances if they are using the latest revision of the
              Configuration they are associated with.
        type: bool
    database_management:
        description:
            - Filter DB Systems by their Database Management configuration.
        type: list
        elements: str
        choices:
            - "ENABLED"
            - "DISABLED"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Time fields are default ordered as descending. Display name is default ordered as
              ascending.
        type: str
        choices:
            - "displayName"
            - "timeCreated"
    sort_order:
        description:
            - The sort order to use (ASC or DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific db_system
  oci_mysql_db_system_facts:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

- name: List db_systems
  oci_mysql_db_system_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_heat_wave_cluster_attached: true
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: CREATING
    configuration_id: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
    is_up_to_date: true
    database_management: [ "ENABLED" ]
    sort_by: displayName
    sort_order: ASC

"""

RETURN = """
db_systems:
    description:
        - List of DbSystem resources
    returned: on success
    type: complex
    contains:
        subnet_id:
            description:
                - The OCID of the subnet the DB System is associated with.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        source:
            description:
                - ""
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.configuration.oc1..xxxxxxEXAMPLExxxxxx"
        data_storage_size_in_gbs:
            description:
                - Initial size of the data volume in GiBs that will be created and attached.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        hostname_label:
            description:
                - "The hostname for the primary endpoint of the DB System. Used for DNS.
                  The value is the hostname portion of the primary private IP's fully qualified domain name (FQDN)
                  (for example, \\"dbsystem-1\\" in FQDN \\"dbsystem-1.subnet123.vcn1.oraclevcn.com\\").
                  Must be unique across all VNICs in the subnet and comply with RFC 952 and RFC 1123."
                - Returned for get operation
            returned: on success
            type: str
            sample: hostname_label_example
        ip_address:
            description:
                - "The IP address the DB System is configured to listen on. A private
                  IP address of the primary endpoint of the DB System. Must be an
                  available IP address within the subnet's CIDR. This will be a
                  \\"dotted-quad\\" style IPv4 address."
                - Returned for get operation
            returned: on success
            type: str
            sample: ip_address_example
        port:
            description:
                - The port for primary endpoint of the DB System to listen on.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        port_x:
            description:
                - The network port on which X Plugin listens for TCP/IP connections. This is the X Plugin equivalent of port.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        channels:
            description:
                - A list with a summary of all the Channels attached to the DB System.
                - Returned for get operation
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
                        anonymous_transactions_handling:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                uuid:
                                    description:
                                        - The UUID that is used as a prefix when generating transaction identifiers for anonymous transactions
                                          coming from the source. You can change the UUID later.
                                    returned: on success
                                    type: str
                                    sample: "null"

                                last_configured_log_filename:
                                    description:
                                        - Specifies one of the coordinates (file) at which the replica should begin
                                          reading the source's log. As this value specifies the point where replication
                                          starts from, it is only used once, when it starts. It is never used again,
                                          unless a new UpdateChannel operation modifies it.
                                    returned: on success
                                    type: str
                                    sample: last_configured_log_filename_example
                                last_configured_log_offset:
                                    description:
                                        - Specifies one of the coordinates (offset) at which the replica should begin
                                          reading the source's log. As this value specifies the point where replication
                                          starts from, it is only used once, when it starts. It is never used again,
                                          unless a new UpdateChannel operation modifies it.
                                    returned: on success
                                    type: int
                                    sample: 56
                                policy:
                                    description:
                                        - Specifies how the replication channel handles anonymous transactions.
                                    returned: on success
                                    type: str
                                    sample: ERROR_ON_ANONYMOUS
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
                        filters:
                            description:
                                - Replication filter rules to be applied at the DB System Channel target.
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - The type of the filter rule.
                                        - For details on each type, see
                                          L(Replication Filtering Rules,https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html)
                                    returned: on success
                                    type: str
                                    sample: REPLICATE_DO_DB
                                value:
                                    description:
                                        - "The body of the filter rule. This can represent a database, a table, or a database pair (represented as
                                          \\"db1->db2\\"). For more information, see
                                          L(Replication Filtering Rules,https://dev.mysql.com/doc/refman/8.0/en/replication-rules.html)."
                                    returned: on success
                                    type: str
                                    sample: value_example
                        tables_without_primary_key_handling:
                            description:
                                - Specifies how a replication channel handles the creation and alteration of tables
                                  that do not have a primary key.
                            returned: on success
                            type: str
                            sample: RAISE_ERROR
                        delay_in_seconds:
                            description:
                                - Specifies the amount of time, in seconds, that the channel waits before
                                  applying a transaction received from the source.
                            returned: on success
                            type: int
                            sample: 56
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
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        maintenance:
            description:
                - ""
                - Returned for get operation
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
                        - "If you set the read replica maintenance window to \\"\\" or if not specified, the read replica is set same as the DB system
                          maintenance window."
                    returned: on success
                    type: str
                    sample: window_start_time_example
        point_in_time_recovery_details:
            description:
                - ""
                - Returned for get operation
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
                is_lakehouse_enabled:
                    description:
                        - Lakehouse enabled status for the HeatWave cluster.
                    returned: on success
                    type: bool
                    sample: true
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
                resource_type:
                    description:
                        - The type of endpoint that clients and connectors can connect to.
                    returned: on success
                    type: str
                    sample: DBSYSTEM
                resource_id:
                    description:
                        - The OCID of the resource that this endpoint is attached to.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the DB System.
            returned: on success
            type: str
            sample: CREATING
        mysql_version:
            description:
                - Name of the MySQL Version in use for the DB System.
            returned: on success
            type: str
            sample: mysql_version_example
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
        crash_recovery:
            description:
                - Whether to run the DB System with InnoDB Redo Logs and the Double Write Buffer enabled or disabled,
                  and whether to enable or disable syncing of the Binary Logs.
            returned: on success
            type: str
            sample: ENABLED
        database_management:
            description:
                - Whether to enable monitoring via the Database Management service.
            returned: on success
            type: str
            sample: ENABLED
    sample: [{
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
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
                },
                "anonymous_transactions_handling": {
                    "uuid": null,
                    "last_configured_log_filename": "last_configured_log_filename_example",
                    "last_configured_log_offset": 56,
                    "policy": "ERROR_ON_ANONYMOUS"
                }
            },
            "target": {
                "target_type": "DBSYSTEM",
                "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
                "channel_name": "channel_name_example",
                "applier_username": "applier_username_example",
                "filters": [{
                    "type": "REPLICATE_DO_DB",
                    "value": "value_example"
                }],
                "tables_without_primary_key_handling": "RAISE_ERROR",
                "delay_in_seconds": 56
            },
            "lifecycle_state": "lifecycle_state_example",
            "lifecycle_details": "lifecycle_details_example",
            "display_name": "display_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        }],
        "lifecycle_details": "lifecycle_details_example",
        "maintenance": {
            "window_start_time": "window_start_time_example"
        },
        "point_in_time_recovery_details": {
            "time_earliest_recovery_point": "2013-10-20T19:20:30+01:00",
            "time_latest_recovery_point": "2013-10-20T19:20:30+01:00"
        },
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_highly_available": true,
        "current_placement": {
            "availability_domain": "Uocm:PHX-AD-1",
            "fault_domain": "FAULT-DOMAIN-1"
        },
        "is_heat_wave_cluster_attached": true,
        "heat_wave_cluster": {
            "shape_name": "shape_name_example",
            "cluster_size": 56,
            "is_lakehouse_enabled": true,
            "lifecycle_state": "lifecycle_state_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        },
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domain": "FAULT-DOMAIN-1",
        "endpoints": [{
            "hostname": "hostname_example",
            "ip_address": "ip_address_example",
            "port": 56,
            "port_x": 56,
            "modes": [],
            "status": "ACTIVE",
            "status_details": "status_details_example",
            "resource_type": "DBSYSTEM",
            "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "lifecycle_state": "CREATING",
        "mysql_version": "mysql_version_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "deletion_policy": {
            "automatic_backup_retention": "DELETE",
            "final_backup": "SKIP_FINAL_BACKUP",
            "is_delete_protected": true
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
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
        "shape_name": "shape_name_example",
        "crash_recovery": "ENABLED",
        "database_management": "ENABLED"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.mysql import DbSystemClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlDbSystemFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "is_heat_wave_cluster_attached",
            "db_system_id",
            "display_name",
            "lifecycle_state",
            "configuration_id",
            "is_up_to_date",
            "database_management",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_systems,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MysqlDbSystemFactsHelperCustom = get_custom_class("MysqlDbSystemFactsHelperCustom")


class ResourceFactsHelper(MysqlDbSystemFactsHelperCustom, MysqlDbSystemFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            is_heat_wave_cluster_attached=dict(type="bool"),
            db_system_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            configuration_id=dict(type="str"),
            is_up_to_date=dict(type="bool"),
            database_management=dict(
                type="list", elements="str", choices=["ENABLED", "DISABLED"]
            ),
            sort_by=dict(type="str", choices=["displayName", "timeCreated"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_system",
        service_client_class=DbSystemClient,
        namespace="mysql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(db_systems=result)


if __name__ == "__main__":
    main()
