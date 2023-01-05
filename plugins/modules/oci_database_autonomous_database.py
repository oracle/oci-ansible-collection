#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_database_autonomous_database
short_description: Manage an AutonomousDatabase resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AutonomousDatabase resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Autonomous Database.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_autonomous_database_actions) module:
      autonomous_database_manual_refresh, change_compartment, configure_autonomous_database_vault_key, deregister_autonomous_database_data_safe,
      disable_autonomous_database_management, disable_autonomous_database_operations_insights, enable_autonomous_database_management,
      enable_autonomous_database_operations_insights, fail_over, generate_autonomous_database_wallet, register_autonomous_database_data_safe, restart, restore,
      rotate_autonomous_database_encryption_key, shrink, start, stop, switchover."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source_autonomous_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that you will clone to create
              a new Autonomous Database. Required when source is 'BACKUP_FROM_TIMESTAMP'
        type: str
    autonomous_database_backup_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database Backup that you will clone to
              create a new Autonomous Database.
            - Required when source is 'BACKUP_FROM_ID'
        type: str
    timestamp:
        description:
            - The timestamp specified for the point-in-time clone of the source Autonomous Database. The timestamp must be in the past.
            - Applicable when source is 'BACKUP_FROM_TIMESTAMP'
        type: str
    clone_type:
        description:
            - The Autonomous Database clone type.
            - Required when source is one of ['BACKUP_FROM_TIMESTAMP', 'DATABASE', 'BACKUP_FROM_ID']
        type: str
        choices:
            - "FULL"
            - "METADATA"
    use_latest_available_backup_time_stamp:
        description:
            - Clone from latest available backup timestamp.
            - Applicable when source is 'BACKUP_FROM_TIMESTAMP'
        type: bool
    source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that you will clone to create
              a new Autonomous Database.
            - Required when source is one of ['DATABASE', 'CLONE_TO_REFRESHABLE', 'CROSS_REGION_DATAGUARD']
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment of the Autonomous Database.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    character_set:
        description:
            - The character set for the autonomous database.  The default is AL32UTF8. Allowed values for an Autonomous Database on shared infrastructure as as
              returned by L(List Autonomous Database Character Sets,https://docs.cloud.oracle.com/autonomousDatabaseCharacterSets)
            - "For an Autonomous Database on dedicated infrastructure, the allowed values are:"
            - AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711, AR8NAFITHA721,
              AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII, CDN8PC863,
              CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES, EE8MACCROATIANS,
              EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII,
              IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS,
              KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4,
              RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8,
              VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850,
              WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS
        type: str
    ncharacter_set:
        description:
            - "The character set for the Autonomous Database.  The default is AL32UTF8. Use L(List Autonomous Database Character
              Sets,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/autonomousDatabaseCharacterSets/ListAutonomousDatabaseCharacterSets) to
              list the allowed values for an Autonomous Database on shared Exadata infrastructure.
              For an Autonomous Database on dedicated Exadata infrastructure, the allowed values are:
              AL16UTF16 or UTF8."
        type: str
    kms_key_id:
        description:
            - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
        type: str
    vault_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
              L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
        type: str
    is_preview_version_with_service_terms_accepted:
        description:
            - If set to `TRUE`, indicates that an Autonomous Database preview version is being provisioned, and that the preview version's terms of service have
              been accepted. Note that preview version software is only available for databases on L(shared Exadata
              infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).
        type: bool
    is_dedicated:
        description:
            - True if the database is on L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).
        type: bool
    autonomous_container_database_id:
        description:
            - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
    source:
        description:
            - "The source of the database: Use `NONE` for creating a new Autonomous Database. Use `DATABASE` for creating a new Autonomous Database by cloning
              an existing Autonomous Database. Use `CROSS_REGION_DATAGUARD` to create a standby Data Guard database in another region."
            - "For Autonomous Databases on L(shared Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html), the following
              cloning options are available: Use `BACKUP_FROM_ID` for creating a new Autonomous Database from a specified backup. Use `BACKUP_FROM_TIMESTAMP`
              for creating a point-in-time Autonomous Database clone using backups. For more information, see L(Cloning and Moving an Autonomous
              Database,https://docs.oracle.com/en/cloud/paas/autonomous-database/adbsa/clone-autonomous-
              database.html#GUID-D771796F-5081-4CFB-A7FF-0F893EABD7BC)."
        type: str
        choices:
            - "DATABASE"
            - "CLONE_TO_REFRESHABLE"
            - "BACKUP_FROM_ID"
            - "BACKUP_FROM_TIMESTAMP"
            - "CROSS_REGION_DATAGUARD"
            - "NONE"
        default: "NONE"
    autonomous_maintenance_schedule_type:
        description:
            - The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous
              Database
              follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the
              normal cycle.
        type: str
        choices:
            - "EARLY"
            - "REGULAR"
    cpu_core_count:
        description:
            - The number of OCPU cores to be made available to the database. For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of
              cores is determined by the infrastructure shape. See L(Characteristics of Infrastructure
              Shapes,https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1) for shape
              details.
            - "**Note:** This parameter cannot be used with the `ocpuCount` parameter."
            - This parameter is updatable.
        type: int
    ocpu_count:
        description:
            - The number of OCPU cores to be made available to the database.
            - "The following points apply:
              - For Autonomous Databases on dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of 0.1.
                For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous
                Databasese on shared Exadata infrastructure.)
              - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape. For
                example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated Exadata
                infrastructure."
            - For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See
              L(Characteristics of Infrastructure Shapes,https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-
              GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1) for shape details.
            - "**Note:** This parameter cannot be used with the `cpuCoreCount` parameter."
            - This parameter is updatable.
        type: float
    data_storage_size_in_tbs:
        description:
            - The size, in terabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. For
              Autonomous Databases on dedicated Exadata infrastructure, the maximum storage value is determined by the infrastructure shape. See
              L(Characteristics of Infrastructure Shapes,https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-
              GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1) for shape details.
            - "**Note:** This parameter cannot be used with the `dataStorageSizeInGBs` parameter."
            - This parameter is updatable.
        type: int
    data_storage_size_in_gbs:
        description:
            - The size, in gigabytes, of the data volume that will be created and attached to the database. This storage can later be scaled up if needed. The
              maximum storage value is determined by the infrastructure shape. See L(Characteristics of Infrastructure
              Shapes,https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1) for shape
              details.
            - "**Notes**
              - This parameter is only supported for dedicated Exadata infrastructure.
              - This parameter cannot be used with the `dataStorageSizeInTBs` parameter."
            - This parameter is updatable.
        type: int
    display_name:
        description:
            - The user-friendly name for the Autonomous Database. The name does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    is_free_tier:
        description:
            - Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of
              memory. For Always Free databases, memory and CPU cannot be scaled.
            - This parameter is updatable.
        type: bool
    admin_password:
        description:
            - "**Important** The `adminPassword` must be specified for all Autonomous Databases except for refreshable clones. The password must be between 12
              and 30 characters long, and must contain at least 1 uppercase, 1 lowercase, and 1 numeric character. It cannot contain the double quote symbol
              (\\") or the username \\"admin\\", regardless of casing."
            - This parameter is updatable.
        type: str
    db_name:
        description:
            - The database name. The name must begin with an alphabetic character and can contain a maximum of 14 alphanumeric characters. Special characters
              are not permitted. The database name must be unique in the tenancy.
            - This parameter is updatable.
        type: str
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
    db_workload:
        description:
            - "The Autonomous Database workload type. The following values are valid:"
            - "- OLTP - indicates an Autonomous Transaction Processing database
              - DW - indicates an Autonomous Data Warehouse database
              - AJD - indicates an Autonomous JSON Database
              - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type."
            - This parameter is updatable.
        type: str
        choices:
            - "OLTP"
            - "DW"
            - "AJD"
            - "APEX"
    license_model:
        description:
            - The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-
              premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
              License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
              Note that when provisioning an Autonomous Database on L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
              database/index.html), this attribute must be null because the attribute is already set at the
              Autonomous Exadata Infrastructure level. When using L(shared Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
              database/index.html), if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    is_access_control_enabled:
        description:
            - Indicates if the database-level access control is enabled.
              If disabled, database access is defined by the network security rules.
              If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While specifying
              `whitelistedIps` rules is optional,
               if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later using
               the `UpdateAutonomousDatabase` API operation or edit option in console.
              When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be disabled
              for the clone.
            - This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.
            - This parameter is updatable.
        type: bool
    whitelisted_ips:
        description:
            - The client IP access control list (ACL). This feature is available for autonomous databases on L(shared Exadata
              infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) and on Exadata Cloud@Customer.
              Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.
            - "For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
              Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
              Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"ocid1.vcn.oc1.sea.<unique_id>\\",\\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\\",\\"ocid1.vcn.oc1.sea.<u
              nique_id2>;1.1.0.0/16\\"]`
              For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
              Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"1.1.2.25\\"]`"
            - For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.
            - This parameter is updatable.
        type: list
        elements: str
    are_primary_whitelisted_ips_used:
        description:
            - This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
              It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses primary
              IP access control list (ACL) for standby.
              It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses
              different IP access control list (ACL) for standby compared to primary.
            - This parameter is updatable.
        type: bool
    standby_whitelisted_ips:
        description:
            - The client IP access control list (ACL). This feature is available for autonomous databases on L(shared Exadata
              infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) and on Exadata Cloud@Customer.
              Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.
            - "For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
              Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
              Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"ocid1.vcn.oc1.sea.<unique_id>\\",\\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\\",\\"ocid1.vcn.oc1.sea.<u
              nique_id2>;1.1.0.0/16\\"]`
              For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
              Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"1.1.2.25\\"]`"
            - For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.
            - This parameter is updatable.
        type: list
        elements: str
    is_auto_scaling_enabled:
        description:
            - Indicates if auto scaling is enabled for the Autonomous Database OCPU core count. The default value is `FALSE`.
            - This parameter is updatable.
        type: bool
    is_refreshable_clone:
        description:
            - Indicates whether the Autonomous Database is a refreshable clone.
            - This parameter is updatable.
        type: bool
    refreshable_mode:
        description:
            - The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous Database.
            - This parameter is updatable.
            - Applicable when source is 'CLONE_TO_REFRESHABLE'
        type: str
        choices:
            - "AUTOMATIC"
            - "MANUAL"
    is_local_data_guard_enabled:
        description:
            - Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard
              associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.
            - This parameter is updatable.
        type: bool
    is_data_guard_enabled:
        description:
            - "**Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous
              Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure."
            - This parameter is updatable.
        type: bool
    peer_db_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Data Guard standby database located in a
              different (remote) region from the source primary Autonomous Database.
            - To create or delete a local (in-region) standby, see the `isDataGuardEnabled` parameter.
            - This parameter is updatable.
        type: str
    db_version:
        description:
            - A valid Oracle Database version for Autonomous Database.
            - This parameter is updatable.
        type: str
    open_mode:
        description:
            - The `DATABASE OPEN` mode. You can open the database in `READ_ONLY` or `READ_WRITE` mode.
            - This parameter is updatable.
        type: str
        choices:
            - "READ_ONLY"
            - "READ_WRITE"
    permission_level:
        description:
            - The Autonomous Database permission level. Restricted mode allows access only to admin users.
            - This parameter is updatable.
        type: str
        choices:
            - "RESTRICTED"
            - "UNRESTRICTED"
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the resource is associated with.
            - "**Subnet Restrictions:**
              - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
              - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
              - For Autonomous Database, setting this will disable public secure access to the database."
            - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
              Specifying an overlapping subnet will cause the private interconnect to malfunction.
              This restriction applies to both the client subnet and the backup subnet.
            - This parameter is updatable.
        type: str
    private_endpoint_label:
        description:
            - The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change the
              same private endpoint database to the public endpoint database.
            - This parameter is updatable.
        type: str
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
    customer_contacts:
        description:
            - Customer Contacts.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            email:
                description:
                    - The email address used by Oracle to send notifications regarding databases and infrastructure.
                    - Applicable when source is 'DATABASE'
                type: str
    is_mtls_connection_required:
        description:
            - Indicates whether the Autonomous Database requires mTLS connections.
            - This parameter is updatable.
        type: bool
    scheduled_operations:
        description:
            - list of scheduled operations
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            day_of_week:
                description:
                    - ""
                    - Required when source is 'DATABASE'
                type: dict
                required: true
                suboptions:
                    name:
                        description:
                            - Name of the day of the week.
                            - Required when source is 'DATABASE'
                        type: str
                        choices:
                            - "MONDAY"
                            - "TUESDAY"
                            - "WEDNESDAY"
                            - "THURSDAY"
                            - "FRIDAY"
                            - "SATURDAY"
                            - "SUNDAY"
                        required: true
            scheduled_start_time:
                description:
                    - "auto start time. value must be of ISO-8601 format \\"HH:mm\\""
                    - Applicable when source is 'DATABASE'
                type: str
            scheduled_stop_time:
                description:
                    - "auto stop time. value must be of ISO-8601 format \\"HH:mm\\""
                    - Applicable when source is 'DATABASE'
                type: str
    is_auto_scaling_for_storage_enabled:
        description:
            - Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.
            - This parameter is updatable.
        type: bool
    max_cpu_core_count:
        description:
            - The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.
            - This parameter is updatable.
        type: int
    database_edition:
        description:
            - The Oracle Database Edition that applies to the Autonomous databases.
            - This parameter is updatable.
        type: str
    autonomous_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that you will clone to create
              a new Autonomous Database.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required when source is 'BACKUP_FROM_TIMESTAMP'
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AutonomousDatabase.
            - Use I(state=present) to create or update an AutonomousDatabase.
            - Use I(state=absent) to delete an AutonomousDatabase.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create autonomous_database with source = DATABASE
  oci_database_autonomous_database:
    # required
    clone_type: FULL
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source: DATABASE

    # optional
    character_set: character_set_example
    ncharacter_set: ncharacter_set_example
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    is_preview_version_with_service_terms_accepted: true
    is_dedicated: true
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_maintenance_schedule_type: EARLY
    cpu_core_count: 56
    ocpu_count: 3.4
    data_storage_size_in_tbs: 56
    data_storage_size_in_gbs: 56
    display_name: display_name_example
    is_free_tier: true
    admin_password: example-password
    db_name: db_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    db_workload: OLTP
    license_model: LICENSE_INCLUDED
    is_access_control_enabled: true
    whitelisted_ips: [ "whitelisted_ips_example" ]
    are_primary_whitelisted_ips_used: true
    standby_whitelisted_ips: [ "standby_whitelisted_ips_example" ]
    is_auto_scaling_enabled: true
    is_local_data_guard_enabled: true
    is_data_guard_enabled: true
    db_version: db_version_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_label: private_endpoint_label_example
    nsg_ids: [ "nsg_ids_example" ]
    customer_contacts:
    - # optional
      email: email_example
    is_mtls_connection_required: true
    scheduled_operations:
    - # required
      day_of_week:
        # required
        name: MONDAY

      # optional
      scheduled_start_time: scheduled_start_time_example
      scheduled_stop_time: scheduled_stop_time_example
    is_auto_scaling_for_storage_enabled: true
    max_cpu_core_count: 56
    database_edition: database_edition_example

- name: Create autonomous_database with source = CLONE_TO_REFRESHABLE
  oci_database_autonomous_database:
    # required
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source: CLONE_TO_REFRESHABLE

    # optional
    character_set: character_set_example
    ncharacter_set: ncharacter_set_example
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    is_preview_version_with_service_terms_accepted: true
    is_dedicated: true
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_maintenance_schedule_type: EARLY
    cpu_core_count: 56
    ocpu_count: 3.4
    data_storage_size_in_tbs: 56
    data_storage_size_in_gbs: 56
    display_name: display_name_example
    is_free_tier: true
    admin_password: example-password
    db_name: db_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    db_workload: OLTP
    license_model: LICENSE_INCLUDED
    is_access_control_enabled: true
    whitelisted_ips: [ "whitelisted_ips_example" ]
    are_primary_whitelisted_ips_used: true
    standby_whitelisted_ips: [ "standby_whitelisted_ips_example" ]
    is_auto_scaling_enabled: true
    refreshable_mode: AUTOMATIC
    is_local_data_guard_enabled: true
    is_data_guard_enabled: true
    db_version: db_version_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_label: private_endpoint_label_example
    nsg_ids: [ "nsg_ids_example" ]
    customer_contacts:
    - # optional
      email: email_example
    is_mtls_connection_required: true
    scheduled_operations:
    - # required
      day_of_week:
        # required
        name: MONDAY

      # optional
      scheduled_start_time: scheduled_start_time_example
      scheduled_stop_time: scheduled_stop_time_example
    is_auto_scaling_for_storage_enabled: true
    max_cpu_core_count: 56
    database_edition: database_edition_example

- name: Create autonomous_database with source = BACKUP_FROM_ID
  oci_database_autonomous_database:
    # required
    autonomous_database_backup_id: "ocid1.autonomousdatabasebackup.oc1..xxxxxxEXAMPLExxxxxx"
    clone_type: FULL
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source: BACKUP_FROM_ID

    # optional
    character_set: character_set_example
    ncharacter_set: ncharacter_set_example
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    is_preview_version_with_service_terms_accepted: true
    is_dedicated: true
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_maintenance_schedule_type: EARLY
    cpu_core_count: 56
    ocpu_count: 3.4
    data_storage_size_in_tbs: 56
    data_storage_size_in_gbs: 56
    display_name: display_name_example
    is_free_tier: true
    admin_password: example-password
    db_name: db_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    db_workload: OLTP
    license_model: LICENSE_INCLUDED
    is_access_control_enabled: true
    whitelisted_ips: [ "whitelisted_ips_example" ]
    are_primary_whitelisted_ips_used: true
    standby_whitelisted_ips: [ "standby_whitelisted_ips_example" ]
    is_auto_scaling_enabled: true
    is_local_data_guard_enabled: true
    is_data_guard_enabled: true
    db_version: db_version_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_label: private_endpoint_label_example
    nsg_ids: [ "nsg_ids_example" ]
    customer_contacts:
    - # optional
      email: email_example
    is_mtls_connection_required: true
    scheduled_operations:
    - # required
      day_of_week:
        # required
        name: MONDAY

      # optional
      scheduled_start_time: scheduled_start_time_example
      scheduled_stop_time: scheduled_stop_time_example
    is_auto_scaling_for_storage_enabled: true
    max_cpu_core_count: 56
    database_edition: database_edition_example

- name: Create autonomous_database with source = BACKUP_FROM_TIMESTAMP
  oci_database_autonomous_database:
    # required
    clone_type: FULL
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source: BACKUP_FROM_TIMESTAMP
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    timestamp: timestamp_example
    use_latest_available_backup_time_stamp: true
    character_set: character_set_example
    ncharacter_set: ncharacter_set_example
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    is_preview_version_with_service_terms_accepted: true
    is_dedicated: true
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_maintenance_schedule_type: EARLY
    cpu_core_count: 56
    ocpu_count: 3.4
    data_storage_size_in_tbs: 56
    data_storage_size_in_gbs: 56
    display_name: display_name_example
    is_free_tier: true
    admin_password: example-password
    db_name: db_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    db_workload: OLTP
    license_model: LICENSE_INCLUDED
    is_access_control_enabled: true
    whitelisted_ips: [ "whitelisted_ips_example" ]
    are_primary_whitelisted_ips_used: true
    standby_whitelisted_ips: [ "standby_whitelisted_ips_example" ]
    is_auto_scaling_enabled: true
    is_local_data_guard_enabled: true
    is_data_guard_enabled: true
    db_version: db_version_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_label: private_endpoint_label_example
    nsg_ids: [ "nsg_ids_example" ]
    customer_contacts:
    - # optional
      email: email_example
    is_mtls_connection_required: true
    scheduled_operations:
    - # required
      day_of_week:
        # required
        name: MONDAY

      # optional
      scheduled_start_time: scheduled_start_time_example
      scheduled_stop_time: scheduled_stop_time_example
    is_auto_scaling_for_storage_enabled: true
    max_cpu_core_count: 56
    database_edition: database_edition_example

- name: Create autonomous_database with source = CROSS_REGION_DATAGUARD
  oci_database_autonomous_database:
    # required
    source_id: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    source: CROSS_REGION_DATAGUARD

    # optional
    character_set: character_set_example
    ncharacter_set: ncharacter_set_example
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    is_preview_version_with_service_terms_accepted: true
    is_dedicated: true
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    autonomous_maintenance_schedule_type: EARLY
    cpu_core_count: 56
    ocpu_count: 3.4
    data_storage_size_in_tbs: 56
    data_storage_size_in_gbs: 56
    display_name: display_name_example
    is_free_tier: true
    admin_password: example-password
    db_name: db_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    db_workload: OLTP
    license_model: LICENSE_INCLUDED
    is_access_control_enabled: true
    whitelisted_ips: [ "whitelisted_ips_example" ]
    are_primary_whitelisted_ips_used: true
    standby_whitelisted_ips: [ "standby_whitelisted_ips_example" ]
    is_auto_scaling_enabled: true
    is_local_data_guard_enabled: true
    is_data_guard_enabled: true
    db_version: db_version_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_label: private_endpoint_label_example
    nsg_ids: [ "nsg_ids_example" ]
    customer_contacts:
    - # optional
      email: email_example
    is_mtls_connection_required: true
    scheduled_operations:
    - # required
      day_of_week:
        # required
        name: MONDAY

      # optional
      scheduled_start_time: scheduled_start_time_example
      scheduled_stop_time: scheduled_stop_time_example
    is_auto_scaling_for_storage_enabled: true
    max_cpu_core_count: 56
    database_edition: database_edition_example

- name: Create autonomous_database with source = NONE
  oci_database_autonomous_database:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    character_set: character_set_example
    ncharacter_set: ncharacter_set_example
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
    is_preview_version_with_service_terms_accepted: true
    is_dedicated: true
    autonomous_container_database_id: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    source: NONE
    autonomous_maintenance_schedule_type: EARLY
    cpu_core_count: 56
    ocpu_count: 3.4
    data_storage_size_in_tbs: 56
    data_storage_size_in_gbs: 56
    display_name: display_name_example
    is_free_tier: true
    admin_password: example-password
    db_name: db_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    db_workload: OLTP
    license_model: LICENSE_INCLUDED
    is_access_control_enabled: true
    whitelisted_ips: [ "whitelisted_ips_example" ]
    are_primary_whitelisted_ips_used: true
    standby_whitelisted_ips: [ "standby_whitelisted_ips_example" ]
    is_auto_scaling_enabled: true
    is_local_data_guard_enabled: true
    is_data_guard_enabled: true
    db_version: db_version_example
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_label: private_endpoint_label_example
    nsg_ids: [ "nsg_ids_example" ]
    customer_contacts:
    - # optional
      email: email_example
    is_mtls_connection_required: true
    scheduled_operations:
    - # required
      day_of_week:
        # required
        name: MONDAY

      # optional
      scheduled_start_time: scheduled_start_time_example
      scheduled_stop_time: scheduled_stop_time_example
    is_auto_scaling_for_storage_enabled: true
    max_cpu_core_count: 56
    database_edition: database_edition_example

- name: Update autonomous_database
  oci_database_autonomous_database:
    # required
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    cpu_core_count: 56
    ocpu_count: 3.4
    data_storage_size_in_tbs: 56
    data_storage_size_in_gbs: 56
    display_name: display_name_example
    is_free_tier: true
    admin_password: example-password
    db_name: db_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    db_workload: OLTP
    license_model: LICENSE_INCLUDED
    is_access_control_enabled: true
    whitelisted_ips: [ "whitelisted_ips_example" ]
    are_primary_whitelisted_ips_used: true
    standby_whitelisted_ips: [ "standby_whitelisted_ips_example" ]
    is_auto_scaling_enabled: true
    is_refreshable_clone: true
    refreshable_mode: AUTOMATIC
    is_local_data_guard_enabled: true
    is_data_guard_enabled: true
    peer_db_id: "ocid1.peerdb.oc1..xxxxxxEXAMPLExxxxxx"
    db_version: db_version_example
    open_mode: READ_ONLY
    permission_level: RESTRICTED
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_label: private_endpoint_label_example
    nsg_ids: [ "nsg_ids_example" ]
    customer_contacts:
    - # optional
      email: email_example
    is_mtls_connection_required: true
    scheduled_operations:
    - # required
      day_of_week:
        # required
        name: MONDAY

      # optional
      scheduled_start_time: scheduled_start_time_example
      scheduled_stop_time: scheduled_stop_time_example
    is_auto_scaling_for_storage_enabled: true
    max_cpu_core_count: 56
    database_edition: database_edition_example

- name: Update autonomous_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_database:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    cpu_core_count: 56
    ocpu_count: 3.4
    data_storage_size_in_tbs: 56
    data_storage_size_in_gbs: 56
    is_free_tier: true
    admin_password: example-password
    db_name: db_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    db_workload: OLTP
    license_model: LICENSE_INCLUDED
    is_access_control_enabled: true
    whitelisted_ips: [ "whitelisted_ips_example" ]
    are_primary_whitelisted_ips_used: true
    standby_whitelisted_ips: [ "standby_whitelisted_ips_example" ]
    is_auto_scaling_enabled: true
    is_refreshable_clone: true
    refreshable_mode: AUTOMATIC
    is_local_data_guard_enabled: true
    is_data_guard_enabled: true
    peer_db_id: "ocid1.peerdb.oc1..xxxxxxEXAMPLExxxxxx"
    db_version: db_version_example
    open_mode: READ_ONLY
    permission_level: RESTRICTED
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    private_endpoint_label: private_endpoint_label_example
    nsg_ids: [ "nsg_ids_example" ]
    customer_contacts:
    - # optional
      email: email_example
    is_mtls_connection_required: true
    scheduled_operations:
    - # required
      day_of_week:
        # required
        name: MONDAY

      # optional
      scheduled_start_time: scheduled_start_time_example
      scheduled_stop_time: scheduled_stop_time_example
    is_auto_scaling_for_storage_enabled: true
    max_cpu_core_count: 56
    database_edition: database_edition_example

- name: Delete autonomous_database
  oci_database_autonomous_database:
    # required
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete autonomous_database using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_autonomous_database:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
autonomous_database:
    description:
        - Details of the AutonomousDatabase resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Autonomous Database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the Autonomous Database.
            returned: on success
            type: str
            sample: PROVISIONING
        lifecycle_details:
            description:
                - Information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        vault_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                  L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
            returned: on success
            type: str
            sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_lifecycle_details:
            description:
                - KMS key lifecycle details.
            returned: on success
            type: str
            sample: kms_key_lifecycle_details_example
        kms_key_version_id:
            description:
                - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
                  versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
            returned: on success
            type: str
            sample: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
        db_name:
            description:
                - The database name.
            returned: on success
            type: str
            sample: db_name_example
        character_set:
            description:
                - "The character set for the autonomous database.  The default is AL32UTF8. Allowed values are:"
                - AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711,
                  AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775, BN8BSCII,
                  CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2, EE8MACCES,
                  EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869, ET8MSWIN923,
                  HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS, JA16SJISTILDE,
                  JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090,
                  N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS,
                  TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9,
                  WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC,
                  ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS
            returned: on success
            type: str
            sample: character_set_example
        ncharacter_set:
            description:
                - "The national character set for the autonomous database.  The default is AL16UTF16. Allowed values are:
                  AL16UTF16 or UTF8."
            returned: on success
            type: str
            sample: ncharacter_set_example
        is_free_tier:
            description:
                - Indicates if this is an Always Free resource. The default value is false. Note that Always Free Autonomous Databases have 1 CPU and 20GB of
                  memory. For Always Free databases, memory and CPU cannot be scaled.
            returned: on success
            type: bool
            sample: true
        system_tags:
            description:
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            returned: on success
            type: dict
            sample: {}
        time_reclamation_of_free_autonomous_database:
            description:
                - The date and time the Always Free database will be stopped because of inactivity. If this time is reached without any database activity, the
                  database will automatically be put into the STOPPED state.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_deletion_of_free_autonomous_database:
            description:
                - The date and time the Always Free database will be automatically deleted because of inactivity. If the database is in the STOPPED state and
                  without activity until this time, it will be deleted.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        backup_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                manual_backup_bucket_name:
                    description:
                        - Name of L(Object Storage,https://docs.cloud.oracle.com/Content/Object/Concepts/objectstorageoverview.htm) bucket to use for storing
                          manual backups.
                    returned: on success
                    type: str
                    sample: manual_backup_bucket_name_example
                manual_backup_type:
                    description:
                        - The manual backup destination type.
                    returned: on success
                    type: str
                    sample: NONE
        key_history_entry:
            description:
                - Key History Entry.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The id of the Autonomous Database L(Vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts)
                          service key management history entry.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                kms_key_version_id:
                    description:
                        - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple
                          key versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
                    returned: on success
                    type: str
                    sample: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
                vault_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                          L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
                    returned: on success
                    type: str
                    sample: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
                time_activated:
                    description:
                        - The date and time the kms key activated.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        cpu_core_count:
            description:
                - The number of OCPU cores to be made available to the database. When the ECPU is selected, the value for cpuCoreCount is 0. For Autonomous
                  Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See L(Characteristics of
                  Infrastructure Shapes,https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-
                  GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1) for shape details.
                - "**Note:** This parameter cannot be used with the `ocpuCount` parameter."
            returned: on success
            type: int
            sample: 56
        ocpu_count:
            description:
                - The number of OCPU cores to be made available to the database.
                - "The following points apply:
                  - For Autonomous Databases on dedicated Exadata infrastructure, to provision less than 1 core, enter a fractional value in an increment of
                    0.1. For example, you can provision 0.3 or 0.4 cores, but not 0.35 cores. (Note that fractional OCPU values are not supported for Autonomous
                    Databasese on shared Exadata infrastructure.)
                  - To provision 1 or more cores, you must enter an integer between 1 and the maximum number of cores available for the infrastructure shape.
                    For example, you can provision 2 cores or 3 cores, but not 2.5 cores. This applies to Autonomous Databases on both shared and dedicated
                    Exadata infrastructure."
                - For Autonomous Databases on dedicated Exadata infrastructure, the maximum number of cores is determined by the infrastructure shape. See
                  L(Characteristics of Infrastructure Shapes,https://www.oracle.com/pls/topic/lookup?ctx=en/cloud/paas/autonomous-database&id=ATPFG-
                  GUID-B0F033C1-CC5A-42F0-B2E7-3CECFEDA1FD1) for shape details.
                - "**Note:** This parameter cannot be used with the `cpuCoreCount` parameter."
            returned: on success
            type: float
            sample: 3.4
        provisionable_cpus:
            description:
                - An array of CPU values that an Autonomous Database can be scaled to.
            returned: on success
            type: list
            sample: []
        data_storage_size_in_tbs:
            description:
                - The quantity of data in the database, in terabytes.
            returned: on success
            type: int
            sample: 56
        memory_per_oracle_compute_unit_in_gbs:
            description:
                - The amount of memory (in GBs) enabled per each OCPU core in Autonomous VM Cluster.
            returned: on success
            type: int
            sample: 56
        data_storage_size_in_gbs:
            description:
                - The quantity of data in the database, in gigabytes.
            returned: on success
            type: int
            sample: 56
        infrastructure_type:
            description:
                - The infrastructure type this resource belongs to.
            returned: on success
            type: str
            sample: CLOUD
        is_dedicated:
            description:
                - True if the database uses L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html).
            returned: on success
            type: bool
            sample: true
        autonomous_container_database_id:
            description:
                - The Autonomous Container Database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the Autonomous Database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        display_name:
            description:
                - The user-friendly name for the Autonomous Database. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        service_console_url:
            description:
                - The URL of the Service Console for the Autonomous Database.
            returned: on success
            type: str
            sample: service_console_url_example
        connection_strings:
            description:
                - The connection string used to connect to the Autonomous Database. The username for the Service Console is ADMIN. Use the password you entered
                  when creating the Autonomous Database for the password value.
            returned: on success
            type: complex
            contains:
                high:
                    description:
                        - The High database service provides the highest level of resources to each SQL statement resulting in the highest performance, but
                          supports the fewest number of concurrent SQL statements.
                    returned: on success
                    type: str
                    sample: high_example
                medium:
                    description:
                        - The Medium database service provides a lower level of resources to each SQL statement potentially resulting a lower level of
                          performance, but supports more concurrent SQL statements.
                    returned: on success
                    type: str
                    sample: medium_example
                low:
                    description:
                        - The Low database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL
                          statements.
                    returned: on success
                    type: str
                    sample: low_example
                dedicated:
                    description:
                        - The database service provides the least level of resources to each SQL statement, but supports the most number of concurrent SQL
                          statements.
                    returned: on success
                    type: str
                    sample: dedicated_example
                all_connection_strings:
                    description:
                        - Returns all connection strings that can be used to connect to the Autonomous Database.
                          For more information, please see L(Predefined Database Service Names for Autonomous Transaction
                          Processing,https://docs.oracle.com/en/cloud/paas/atp-cloud/atpug/connect-predefined.html#GUID-9747539B-FD46-44F1-8FF8-F5AC650F15BE)
                    returned: on success
                    type: dict
                    sample: {}
                profiles:
                    description:
                        - A list of connection string profiles to allow clients to group, filter and select connection string values based on structured
                          metadata.
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - A user-friendly name for the connection.
                            returned: on success
                            type: str
                            sample: display_name_example
                        value:
                            description:
                                - Connection string value.
                            returned: on success
                            type: str
                            sample: value_example
                        consumer_group:
                            description:
                                - Consumer group used by the connection.
                            returned: on success
                            type: str
                            sample: HIGH
                        protocol:
                            description:
                                - Protocol used by the connection.
                            returned: on success
                            type: str
                            sample: TCP
                        tls_authentication:
                            description:
                                - Specifies whether the TLS handshake is using one-way (`SERVER`) or mutual (`MUTUAL`) authentication.
                            returned: on success
                            type: str
                            sample: SERVER
                        host_format:
                            description:
                                - Host format used in connection string.
                            returned: on success
                            type: str
                            sample: FQDN
                        session_mode:
                            description:
                                - Specifies whether the listener performs a direct hand-off of the session, or redirects the session. In RAC deployments where
                                  SCAN is used, sessions are redirected to a Node VIP. Use `DIRECT` for direct hand-offs. Use `REDIRECT` to redirect the
                                  session.
                            returned: on success
                            type: str
                            sample: DIRECT
                        syntax_format:
                            description:
                                - Specifies whether the connection string is using the long (`LONG`), Easy Connect (`EZCONNECT`), or Easy Connect Plus
                                  (`EZCONNECTPLUS`) format.
                                  Autonomous Databases on shared Exadata infrastructure always use the long format.
                            returned: on success
                            type: str
                            sample: LONG
        connection_urls:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                sql_dev_web_url:
                    description:
                        - Oracle SQL Developer Web URL.
                    returned: on success
                    type: str
                    sample: sql_dev_web_url_example
                apex_url:
                    description:
                        - Oracle Application Express (APEX) URL.
                    returned: on success
                    type: str
                    sample: apex_url_example
                machine_learning_user_management_url:
                    description:
                        - Oracle Machine Learning user management URL.
                    returned: on success
                    type: str
                    sample: machine_learning_user_management_url_example
                graph_studio_url:
                    description:
                        - The URL of the Graph Studio for the Autonomous Database.
                    returned: on success
                    type: str
                    sample: graph_studio_url_example
        license_model:
            description:
                - The Oracle license model that applies to the Oracle Autonomous Database. Bring your own license (BYOL) allows you to apply your current on-
                  premises Oracle software licenses to equivalent, highly automated Oracle PaaS and IaaS services in the cloud.
                  License Included allows you to subscribe to new Oracle Database software licenses and the Database service.
                  Note that when provisioning an Autonomous Database on L(dedicated Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
                  database/index.html), this attribute must be null because the attribute is already set at the
                  Autonomous Exadata Infrastructure level. When using L(shared Exadata infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-
                  database/index.html), if a value is not specified, the system will supply the value of `BRING_YOUR_OWN_LICENSE`.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        used_data_storage_size_in_tbs:
            description:
                - The amount of storage that has been used, in terabytes.
            returned: on success
            type: int
            sample: 56
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
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the resource is associated with.
                - "**Subnet Restrictions:**
                  - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
                  - For Exadata and virtual machine 2-node RAC systems, do not use a subnet that overlaps with 192.168.128.0/20.
                  - For Autonomous Database, setting this will disable public secure access to the database."
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and the backup subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
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
        private_endpoint:
            description:
                - The private endpoint for the resource.
            returned: on success
            type: str
            sample: private_endpoint_example
        private_endpoint_label:
            description:
                - The private endpoint label for the resource. Setting this to an empty string, after the private endpoint database gets created, will change
                  the same private endpoint database to the public endpoint database.
            returned: on success
            type: str
            sample: private_endpoint_label_example
        private_endpoint_ip:
            description:
                - The private endpoint Ip address for the resource.
            returned: on success
            type: str
            sample: private_endpoint_ip_example
        db_version:
            description:
                - A valid Oracle Database version for Autonomous Database.
            returned: on success
            type: str
            sample: db_version_example
        is_preview:
            description:
                - Indicates if the Autonomous Database version is a preview version.
            returned: on success
            type: bool
            sample: true
        db_workload:
            description:
                - "The Autonomous Database workload type. The following values are valid:"
                - "- OLTP - indicates an Autonomous Transaction Processing database
                  - DW - indicates an Autonomous Data Warehouse database
                  - AJD - indicates an Autonomous JSON Database
                  - APEX - indicates an Autonomous Database with the Oracle APEX Application Development workload type."
            returned: on success
            type: str
            sample: OLTP
        is_access_control_enabled:
            description:
                - Indicates if the database-level access control is enabled.
                  If disabled, database access is defined by the network security rules.
                  If enabled, database access is restricted to the IP addresses defined by the rules specified with the `whitelistedIps` property. While
                  specifying `whitelistedIps` rules is optional,
                   if database-level access control is enabled and no rules are specified, the database will become inaccessible. The rules can be added later
                   using the `UpdateAutonomousDatabase` API operation or edit option in console.
                  When creating a database clone, the desired access control setting should be specified. By default, database-level access control will be
                  disabled for the clone.
                - This property is applicable only to Autonomous Databases on the Exadata Cloud@Customer platform.
            returned: on success
            type: bool
            sample: true
        whitelisted_ips:
            description:
                - The client IP access control list (ACL). This feature is available for autonomous databases on L(shared Exadata
                  infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) and on Exadata Cloud@Customer.
                  Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.
                - "For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
                  Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"ocid1.vcn.oc1.sea.<unique_id>\\",\\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\\",\\"ocid1.vcn.oc1.se
                  a.<unique_id2>;1.1.0.0/16\\"]`
                  For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"1.1.2.25\\"]`"
                - For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.
            returned: on success
            type: list
            sample: []
        are_primary_whitelisted_ips_used:
            description:
                - This field will be null if the Autonomous Database is not Data Guard enabled or Access Control is disabled.
                  It's value would be `TRUE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses
                  primary IP access control list (ACL) for standby.
                  It's value would be `FALSE` if Autonomous Database is Data Guard enabled and Access Control is enabled and if the Autonomous Database uses
                  different IP access control list (ACL) for standby compared to primary.
            returned: on success
            type: bool
            sample: true
        standby_whitelisted_ips:
            description:
                - The client IP access control list (ACL). This feature is available for autonomous databases on L(shared Exadata
                  infrastructure,https://docs.oracle.com/en/cloud/paas/autonomous-database/index.html) and on Exadata Cloud@Customer.
                  Only clients connecting from an IP address included in the ACL may access the Autonomous Database instance.
                - "For shared Exadata infrastructure, this is an array of CIDR (Classless Inter-Domain Routing) notations for a subnet or VCN OCID.
                  Use a semicolon (;) as a deliminator between the VCN-specific subnets or IPs.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"ocid1.vcn.oc1.sea.<unique_id>\\",\\"ocid1.vcn.oc1.sea.<unique_id1>;1.1.1.1\\",\\"ocid1.vcn.oc1.se
                  a.<unique_id2>;1.1.0.0/16\\"]`
                  For Exadata Cloud@Customer, this is an array of IP addresses or CIDR (Classless Inter-Domain Routing) notations.
                  Example: `[\\"1.1.1.1\\",\\"1.1.1.0/24\\",\\"1.1.2.25\\"]`"
                - For an update operation, if you want to delete all the IPs in the ACL, use an array with a single empty string entry.
            returned: on success
            type: list
            sample: []
        apex_details:
            description:
                - Information about Oracle APEX Application Development.
            returned: on success
            type: complex
            contains:
                apex_version:
                    description:
                        - The Oracle APEX Application Development version.
                    returned: on success
                    type: str
                    sample: apex_version_example
                ords_version:
                    description:
                        - The Oracle REST Data Services (ORDS) version.
                    returned: on success
                    type: str
                    sample: ords_version_example
        is_auto_scaling_enabled:
            description:
                - Indicates if auto scaling is enabled for the Autonomous Database CPU core count.
            returned: on success
            type: bool
            sample: true
        data_safe_status:
            description:
                - Status of the Data Safe registration for this Autonomous Database.
            returned: on success
            type: str
            sample: REGISTERING
        operations_insights_status:
            description:
                - Status of Operations Insights for this Autonomous Database.
            returned: on success
            type: str
            sample: ENABLING
        database_management_status:
            description:
                - Status of Database Management for this Autonomous Database.
            returned: on success
            type: str
            sample: ENABLING
        time_maintenance_begin:
            description:
                - The date and time when maintenance will begin.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_maintenance_end:
            description:
                - The date and time when maintenance will end.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_refreshable_clone:
            description:
                - Indicates whether the Autonomous Database is a refreshable clone.
            returned: on success
            type: bool
            sample: true
        time_of_last_refresh:
            description:
                - The date and time when last refresh happened.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_last_refresh_point:
            description:
                - The refresh point timestamp (UTC). The refresh point is the time to which the database was most recently refreshed. Data created after the
                  refresh point is not included in the refresh.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_next_refresh:
            description:
                - The date and time of next refresh.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        open_mode:
            description:
                - The `DATABASE OPEN` mode. You can open the database in `READ_ONLY` or `READ_WRITE` mode.
            returned: on success
            type: str
            sample: READ_ONLY
        refreshable_status:
            description:
                - The refresh status of the clone. REFRESHING indicates that the clone is currently being refreshed with data from the source Autonomous
                  Database.
            returned: on success
            type: str
            sample: REFRESHING
        refreshable_mode:
            description:
                - The refresh mode of the clone. AUTOMATIC indicates that the clone is automatically being refreshed with data from the source Autonomous
                  Database.
            returned: on success
            type: str
            sample: AUTOMATIC
        source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source Autonomous Database that was cloned to create
                  the current Autonomous Database.
            returned: on success
            type: str
            sample: "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx"
        permission_level:
            description:
                - The Autonomous Database permission level. Restricted mode allows access only to admin users.
            returned: on success
            type: str
            sample: RESTRICTED
        time_of_last_switchover:
            description:
                - The timestamp of the last switchover operation for the Autonomous Database.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_of_last_failover:
            description:
                - The timestamp of the last failover operation.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_data_guard_enabled:
            description:
                - "**Deprecated.** Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous
                  Data Guard associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure."
            returned: on success
            type: bool
            sample: true
        failed_data_recovery_in_seconds:
            description:
                - Indicates the number of seconds of data loss for a Data Guard failover.
            returned: on success
            type: int
            sample: 56
        standby_db:
            description:
                - "**Deprecated** Autonomous Data Guard standby database details."
            returned: on success
            type: complex
            contains:
                lag_time_in_seconds:
                    description:
                        - The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine
                          the potential data loss in the event of a failover.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the Autonomous Database.
                    returned: on success
                    type: str
                    sample: PROVISIONING
                lifecycle_details:
                    description:
                        - Additional information about the current lifecycle state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                time_data_guard_role_changed:
                    description:
                        - The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        is_local_data_guard_enabled:
            description:
                - Indicates whether the Autonomous Database has local (in-region) Data Guard enabled. Not applicable to cross-region Autonomous Data Guard
                  associations, or to Autonomous Databases using dedicated Exadata infrastructure or Exadata Cloud@Customer infrastructure.
            returned: on success
            type: bool
            sample: true
        is_remote_data_guard_enabled:
            description:
                - Indicates whether the Autonomous Database has Cross Region Data Guard enabled. Not applicable to Autonomous Databases using dedicated Exadata
                  infrastructure or Exadata Cloud@Customer infrastructure.
            returned: on success
            type: bool
            sample: true
        local_standby_db:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                lag_time_in_seconds:
                    description:
                        - The amount of time, in seconds, that the data of the standby database lags the data of the primary database. Can be used to determine
                          the potential data loss in the event of a failover.
                    returned: on success
                    type: int
                    sample: 56
                lifecycle_state:
                    description:
                        - The current state of the Autonomous Database.
                    returned: on success
                    type: str
                    sample: PROVISIONING
                lifecycle_details:
                    description:
                        - Additional information about the current lifecycle state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                time_data_guard_role_changed:
                    description:
                        - The date and time the Autonomous Data Guard role was switched for the standby Autonomous Database.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
        role:
            description:
                - The Data Guard role of the Autonomous Container Database or Autonomous Database, if Autonomous Data Guard is enabled.
            returned: on success
            type: str
            sample: PRIMARY
        available_upgrade_versions:
            description:
                - List of Oracle Database versions available for a database upgrade. If there are no version upgrades available, this list is empty.
            returned: on success
            type: list
            sample: []
        key_store_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the key store.
            returned: on success
            type: str
            sample: "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx"
        key_store_wallet_name:
            description:
                - The wallet name for Oracle Key Vault.
            returned: on success
            type: str
            sample: key_store_wallet_name_example
        supported_regions_to_clone_to:
            description:
                - The list of regions that support the creation of an Autonomous Database clone or an Autonomous Data Guard standby database.
            returned: on success
            type: list
            sample: []
        customer_contacts:
            description:
                - Customer Contacts.
            returned: on success
            type: complex
            contains:
                email:
                    description:
                        - The email address used by Oracle to send notifications regarding databases and infrastructure.
                    returned: on success
                    type: str
                    sample: email_example
        time_local_data_guard_enabled:
            description:
                - The date and time that Autonomous Data Guard was enabled for an Autonomous Database where the standby was provisioned in the same region as
                  the primary database.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        dataguard_region_type:
            description:
                - "The Autonomous Data Guard region type of the Autonomous Database. For Autonomous Databases on shared Exadata infrastructure, Data Guard
                  associations have designated primary and standby regions, and these region types do not change when the database changes roles. The standby
                  regions in Data Guard associations can be the same region designated as the primary region, or they can be remote regions. Certain database
                  administrative operations may be available only in the primary region of the Data Guard association, and cannot be performed when the database
                  using the \\"primary\\" role is operating in a remote Data Guard standby region."
            returned: on success
            type: str
            sample: PRIMARY_DG_REGION
        time_data_guard_role_changed:
            description:
                - "The date and time the Autonomous Data Guard role was switched for the Autonomous Database. For databases that have standbys in both the
                  primary Data Guard region and a remote Data Guard standby region, this is the latest timestamp of either the database using the \\"primary\\"
                  role in the primary Data Guard region, or database located in the remote Data Guard standby region."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        peer_db_ids:
            description:
                - The list of L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of standby databases located in Autonomous Data
                  Guard remote regions that are associated with the source database. Note that for shared Exadata infrastructure, standby databases located in
                  the same region as the source primary database do not have OCIDs.
            returned: on success
            type: list
            sample: []
        is_mtls_connection_required:
            description:
                - Indicates whether the Autonomous Database requires mTLS connections.
            returned: on success
            type: bool
            sample: true
        is_reconnect_clone_enabled:
            description:
                - Indicates if the refreshable clone can be reconnected to its source database.
            returned: on success
            type: bool
            sample: true
        time_until_reconnect_clone_enabled:
            description:
                - The time and date as an RFC3339 formatted string, e.g., 2022-01-01T12:00:00.000Z, to set the limit for a refreshable clone to be reconnected
                  to its source database.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        autonomous_maintenance_schedule_type:
            description:
                - The maintenance schedule type of the Autonomous Database on shared Exadata infrastructure. The EARLY maintenance schedule of this Autonomous
                  Database
                  follows a schedule that applies patches prior to the REGULAR schedule.The REGULAR maintenance schedule of this Autonomous Database follows the
                  normal cycle.
            returned: on success
            type: str
            sample: EARLY
        scheduled_operations:
            description:
                - list of scheduled operations
            returned: on success
            type: complex
            contains:
                day_of_week:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the day of the week.
                            returned: on success
                            type: str
                            sample: MONDAY
                scheduled_start_time:
                    description:
                        - "auto start time. value must be of ISO-8601 format \\"HH:mm\\""
                    returned: on success
                    type: str
                    sample: scheduled_start_time_example
                scheduled_stop_time:
                    description:
                        - "auto stop time. value must be of ISO-8601 format \\"HH:mm\\""
                    returned: on success
                    type: str
                    sample: scheduled_stop_time_example
        is_auto_scaling_for_storage_enabled:
            description:
                - Indicates if auto scaling is enabled for the Autonomous Database storage. The default value is `FALSE`.
            returned: on success
            type: bool
            sample: true
        allocated_storage_size_in_tbs:
            description:
                - The amount of storage currently allocated for the database tables and billed for, rounded up. When auto-scaling is not enabled, this value is
                  equal to the `dataStorageSizeInTBs` value. You can compare this value to the `actualUsedDataStorageSizeInTBs` value to determine if a manual
                  shrink operation is appropriate for your allocated storage.
                - "**Note:** Auto-scaling does not automatically decrease allocated storage when data is deleted from the database."
            returned: on success
            type: float
            sample: 1.2
        actual_used_data_storage_size_in_tbs:
            description:
                - The current amount of storage in use for user and system data, in terabytes (TB).
            returned: on success
            type: float
            sample: 1.2
        max_cpu_core_count:
            description:
                - The number of Max OCPU cores to be made available to the autonomous database with auto scaling of cpu enabled.
            returned: on success
            type: int
            sample: 56
        database_edition:
            description:
                - The Oracle Database Edition that applies to the Autonomous databases.
            returned: on success
            type: str
            sample: STANDARD_EDITION
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "lifecycle_details": "lifecycle_details_example",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_lifecycle_details": "kms_key_lifecycle_details_example",
        "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx",
        "db_name": "db_name_example",
        "character_set": "character_set_example",
        "ncharacter_set": "ncharacter_set_example",
        "is_free_tier": true,
        "system_tags": {},
        "time_reclamation_of_free_autonomous_database": "2013-10-20T19:20:30+01:00",
        "time_deletion_of_free_autonomous_database": "2013-10-20T19:20:30+01:00",
        "backup_config": {
            "manual_backup_bucket_name": "manual_backup_bucket_name_example",
            "manual_backup_type": "NONE"
        },
        "key_history_entry": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx",
            "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
            "time_activated": "2013-10-20T19:20:30+01:00"
        }],
        "cpu_core_count": 56,
        "ocpu_count": 3.4,
        "provisionable_cpus": [],
        "data_storage_size_in_tbs": 56,
        "memory_per_oracle_compute_unit_in_gbs": 56,
        "data_storage_size_in_gbs": 56,
        "infrastructure_type": "CLOUD",
        "is_dedicated": true,
        "autonomous_container_database_id": "ocid1.autonomouscontainerdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "display_name": "display_name_example",
        "service_console_url": "service_console_url_example",
        "connection_strings": {
            "high": "high_example",
            "medium": "medium_example",
            "low": "low_example",
            "dedicated": "dedicated_example",
            "all_connection_strings": {},
            "profiles": [{
                "display_name": "display_name_example",
                "value": "value_example",
                "consumer_group": "HIGH",
                "protocol": "TCP",
                "tls_authentication": "SERVER",
                "host_format": "FQDN",
                "session_mode": "DIRECT",
                "syntax_format": "LONG"
            }]
        },
        "connection_urls": {
            "sql_dev_web_url": "sql_dev_web_url_example",
            "apex_url": "apex_url_example",
            "machine_learning_user_management_url": "machine_learning_user_management_url_example",
            "graph_studio_url": "graph_studio_url_example"
        },
        "license_model": "LICENSE_INCLUDED",
        "used_data_storage_size_in_tbs": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "private_endpoint": "private_endpoint_example",
        "private_endpoint_label": "private_endpoint_label_example",
        "private_endpoint_ip": "private_endpoint_ip_example",
        "db_version": "db_version_example",
        "is_preview": true,
        "db_workload": "OLTP",
        "is_access_control_enabled": true,
        "whitelisted_ips": [],
        "are_primary_whitelisted_ips_used": true,
        "standby_whitelisted_ips": [],
        "apex_details": {
            "apex_version": "apex_version_example",
            "ords_version": "ords_version_example"
        },
        "is_auto_scaling_enabled": true,
        "data_safe_status": "REGISTERING",
        "operations_insights_status": "ENABLING",
        "database_management_status": "ENABLING",
        "time_maintenance_begin": "2013-10-20T19:20:30+01:00",
        "time_maintenance_end": "2013-10-20T19:20:30+01:00",
        "is_refreshable_clone": true,
        "time_of_last_refresh": "2013-10-20T19:20:30+01:00",
        "time_of_last_refresh_point": "2013-10-20T19:20:30+01:00",
        "time_of_next_refresh": "2013-10-20T19:20:30+01:00",
        "open_mode": "READ_ONLY",
        "refreshable_status": "REFRESHING",
        "refreshable_mode": "AUTOMATIC",
        "source_id": "ocid1.source.oc1..xxxxxxEXAMPLExxxxxx",
        "permission_level": "RESTRICTED",
        "time_of_last_switchover": "2013-10-20T19:20:30+01:00",
        "time_of_last_failover": "2013-10-20T19:20:30+01:00",
        "is_data_guard_enabled": true,
        "failed_data_recovery_in_seconds": 56,
        "standby_db": {
            "lag_time_in_seconds": 56,
            "lifecycle_state": "PROVISIONING",
            "lifecycle_details": "lifecycle_details_example",
            "time_data_guard_role_changed": "2013-10-20T19:20:30+01:00"
        },
        "is_local_data_guard_enabled": true,
        "is_remote_data_guard_enabled": true,
        "local_standby_db": {
            "lag_time_in_seconds": 56,
            "lifecycle_state": "PROVISIONING",
            "lifecycle_details": "lifecycle_details_example",
            "time_data_guard_role_changed": "2013-10-20T19:20:30+01:00"
        },
        "role": "PRIMARY",
        "available_upgrade_versions": [],
        "key_store_id": "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx",
        "key_store_wallet_name": "key_store_wallet_name_example",
        "supported_regions_to_clone_to": [],
        "customer_contacts": [{
            "email": "email_example"
        }],
        "time_local_data_guard_enabled": "2013-10-20T19:20:30+01:00",
        "dataguard_region_type": "PRIMARY_DG_REGION",
        "time_data_guard_role_changed": "2013-10-20T19:20:30+01:00",
        "peer_db_ids": [],
        "is_mtls_connection_required": true,
        "is_reconnect_clone_enabled": true,
        "time_until_reconnect_clone_enabled": "2013-10-20T19:20:30+01:00",
        "autonomous_maintenance_schedule_type": "EARLY",
        "scheduled_operations": [{
            "day_of_week": {
                "name": "MONDAY"
            },
            "scheduled_start_time": "scheduled_start_time_example",
            "scheduled_stop_time": "scheduled_stop_time_example"
        }],
        "is_auto_scaling_for_storage_enabled": true,
        "allocated_storage_size_in_tbs": 1.2,
        "actual_used_data_storage_size_in_tbs": 1.2,
        "max_cpu_core_count": 56,
        "database_edition": "STANDARD_EDITION"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import CreateAutonomousDatabaseBase
    from oci.database.models import UpdateAutonomousDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(AutonomousDatabaseHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(AutonomousDatabaseHelperGen, self).get_possible_entity_types() + [
            "autonomousdatabase",
            "autonomousdatabases",
            "databaseautonomousdatabase",
            "databaseautonomousdatabases",
            "autonomousdatabaseresource",
            "autonomousdatabasesresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "autonomous_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("autonomous_database_id")

    def get_get_fn(self):
        return self.client.get_autonomous_database

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database,
            autonomous_database_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database,
            autonomous_database_id=self.module.params.get("autonomous_database_id"),
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
            ["autonomous_container_database_id", "display_name"]
            if self._use_name_as_identifier()
            else [
                "autonomous_container_database_id",
                "db_workload",
                "db_version",
                "is_free_tier",
                "display_name",
                "is_refreshable_clone",
                "is_data_guard_enabled",
            ]
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
            self.client.list_autonomous_databases, **kwargs
        )

    def get_create_model_class(self):
        return CreateAutonomousDatabaseBase

    def get_exclude_attributes(self):
        return [
            "use_latest_available_backup_time_stamp",
            "autonomous_database_backup_id",
            "source",
            "clone_type",
            "admin_password",
            "is_preview_version_with_service_terms_accepted",
            "autonomous_database_id",
            "timestamp",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(create_autonomous_database_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAutonomousDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
                update_autonomous_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_autonomous_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AutonomousDatabaseHelperCustom = get_custom_class("AutonomousDatabaseHelperCustom")


class ResourceHelper(AutonomousDatabaseHelperCustom, AutonomousDatabaseHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            source_autonomous_database_id=dict(type="str"),
            autonomous_database_backup_id=dict(type="str"),
            timestamp=dict(type="str"),
            clone_type=dict(type="str", choices=["FULL", "METADATA"]),
            use_latest_available_backup_time_stamp=dict(type="bool"),
            source_id=dict(type="str"),
            compartment_id=dict(type="str"),
            character_set=dict(type="str"),
            ncharacter_set=dict(type="str"),
            kms_key_id=dict(type="str"),
            vault_id=dict(type="str"),
            is_preview_version_with_service_terms_accepted=dict(type="bool"),
            is_dedicated=dict(type="bool"),
            autonomous_container_database_id=dict(type="str"),
            source=dict(
                type="str",
                default="NONE",
                choices=[
                    "DATABASE",
                    "CLONE_TO_REFRESHABLE",
                    "BACKUP_FROM_ID",
                    "BACKUP_FROM_TIMESTAMP",
                    "CROSS_REGION_DATAGUARD",
                    "NONE",
                ],
            ),
            autonomous_maintenance_schedule_type=dict(
                type="str", choices=["EARLY", "REGULAR"]
            ),
            cpu_core_count=dict(type="int"),
            ocpu_count=dict(type="float"),
            data_storage_size_in_tbs=dict(type="int"),
            data_storage_size_in_gbs=dict(type="int"),
            display_name=dict(aliases=["name"], type="str"),
            is_free_tier=dict(type="bool"),
            admin_password=dict(type="str", no_log=True),
            db_name=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            db_workload=dict(type="str", choices=["OLTP", "DW", "AJD", "APEX"]),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            is_access_control_enabled=dict(type="bool"),
            whitelisted_ips=dict(type="list", elements="str"),
            are_primary_whitelisted_ips_used=dict(type="bool"),
            standby_whitelisted_ips=dict(type="list", elements="str"),
            is_auto_scaling_enabled=dict(type="bool"),
            is_refreshable_clone=dict(type="bool"),
            refreshable_mode=dict(type="str", choices=["AUTOMATIC", "MANUAL"]),
            is_local_data_guard_enabled=dict(type="bool"),
            is_data_guard_enabled=dict(type="bool"),
            peer_db_id=dict(type="str"),
            db_version=dict(type="str"),
            open_mode=dict(type="str", choices=["READ_ONLY", "READ_WRITE"]),
            permission_level=dict(type="str", choices=["RESTRICTED", "UNRESTRICTED"]),
            subnet_id=dict(type="str"),
            private_endpoint_label=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            customer_contacts=dict(
                type="list", elements="dict", options=dict(email=dict(type="str"))
            ),
            is_mtls_connection_required=dict(type="bool"),
            scheduled_operations=dict(
                type="list",
                elements="dict",
                options=dict(
                    day_of_week=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "MONDAY",
                                    "TUESDAY",
                                    "WEDNESDAY",
                                    "THURSDAY",
                                    "FRIDAY",
                                    "SATURDAY",
                                    "SUNDAY",
                                ],
                            )
                        ),
                    ),
                    scheduled_start_time=dict(type="str"),
                    scheduled_stop_time=dict(type="str"),
                ),
            ),
            is_auto_scaling_for_storage_enabled=dict(type="bool"),
            max_cpu_core_count=dict(type="int"),
            database_edition=dict(type="str"),
            autonomous_database_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_database",
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
