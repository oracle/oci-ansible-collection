#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_db_system
short_description: Manage a DbSystem resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DbSystem resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new DB system in the specified compartment and availability domain. The Oracle
      Database edition that you specify applies to all the databases on that DB system. The selected edition cannot be changed.
    - An initial database is created on the DB system based on the request parameters you provide and some default
      options. For detailed information about default options, see L(Bare metal and virtual machine DB system default
      options.,https://docs.cloud.oracle.com/Content/Database/Tasks/creatingDBsystem.htm#Default)
    - "**Note:** Deprecated for Exadata Cloud Service systems. Use the L(new resource model
      APIs,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem.htm#exaflexsystem_topic-resource_model) instead."
    - For Exadata Cloud Service instances, support for this API will end on May 15th, 2021. See L(Switching an Exadata DB System to the New Resource Model and
      APIs,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/exaflexsystem_topic-resource_model_conversion.htm) for details on converting existing
      Exadata DB systems to the new resource model.
    - Use the L(CreateCloudExadataInfrastructure,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/database/latest/CloudExadataInfrastructure/CreateCloudExadataInfrastructure/) and
      L(CreateCloudVmCluster,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/database/latest/CloudVmCluster/CreateCloudVmCluster/) APIs to provision a new
      Exadata Cloud Service instance.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_db_system_actions) module: change_compartment,
      migrate_exadata_db_system_resource_model."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment the DB system  belongs in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    fault_domains:
        description:
            - A Fault Domain is a grouping of hardware and infrastructure within an availability domain.
              Fault Domains let you distribute your instances so that they are not on the same physical
              hardware within a single availability domain. A hardware failure or maintenance
              that affects one Fault Domain does not affect DB systems in other Fault Domains.
            - If you do not specify the Fault Domain, the system selects one for you. To change the Fault
              Domain for a DB system, terminate it and launch a new DB system in the preferred Fault Domain.
            - If the node count is greater than 1, you can specify which Fault Domains these nodes will be distributed into.
              The system assigns your nodes automatically to the Fault Domains you specify so that
              no Fault Domain contains more than one node.
            - To get a list of Fault Domains, use the
              L(ListFaultDomains,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/latest/FaultDomain/ListFaultDomains) operation in the
              Identity and Access Management Service API.
            - "Example: `FAULT-DOMAIN-1`"
        type: list
        elements: str
    display_name:
        description:
            - The user-friendly name for the DB system. The name does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    availability_domain:
        description:
            - The availability domain where the DB system is located.
            - Required for create using I(state=present).
        type: str
    subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the DB system is associated with.
            - "**Subnet Restrictions:**
              - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
              - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20."
            - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
              Specifying an overlapping subnet will cause the private interconnect to malfunction.
              This restriction applies to both the client subnet and the backup subnet.
            - Required for create using I(state=present).
        type: str
    backup_subnet_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup network subnet the DB system is associated with.
              Applicable only to Exadata DB systems.
            - "**Subnet Restrictions:** See the subnet restrictions information for **subnetId**."
        type: str
    nsg_ids:
        description:
            - "A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this
              resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about NSGs,
              see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
              **NsgIds restrictions:**
              - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty."
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
    shape:
        description:
            - "The shape of the DB system. The shape determines resources allocated to the DB system.
              - For virtual machine shapes, the number of CPU cores and memory
              - For bare metal and Exadata shapes, the number of CPU cores, memory, and storage"
            - To get a list of shapes, use the L(ListDbSystemShapes,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/latest/DbSystemShapeSummary/ListDbSystemShapes) operation.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    time_zone:
        description:
            - The time zone to use for the DB system. For details, see L(DB System Time
              Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
        type: str
    db_system_options:
        description:
            - ""
        type: dict
        suboptions:
            storage_management:
                description:
                    - "The storage option used in DB system.
                      ASM - Automatic storage management
                      LVM - Logical Volume management"
                    - Applicable when source is 'NONE'
                type: str
                choices:
                    - "ASM"
                    - "LVM"
    sparse_diskgroup:
        description:
            - If true, Sparse Diskgroup is configured for Exadata dbsystem. If False, Sparse diskgroup is not configured.
        type: bool
    ssh_public_keys:
        description:
            - The public key portion of the key pair to use for SSH access to the DB system. Multiple public keys can be provided. The length of the combined
              keys cannot exceed 40,000 characters.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: str
    hostname:
        description:
            - The hostname for the DB system. The hostname must begin with an alphabetic character, and
              can contain alphanumeric characters and hyphens (-). The maximum length of the hostname is 16 characters for bare metal and virtual machine DB
              systems, and 12 characters for Exadata DB systems.
            - The maximum length of the combined hostname and domain is 63 characters.
            - "**Note:** The hostname must be unique within the subnet. If it is not unique,
              the DB system will fail to provision."
            - Required for create using I(state=present).
        type: str
    domain:
        description:
            - A domain name used for the DB system. If the Oracle-provided Internet and VCN
              Resolver is enabled for the specified subnet, the domain name for the subnet is used
              (do not provide one). Otherwise, provide a valid DNS domain name. Hyphens (-) are not permitted.
        type: str
    cpu_core_count:
        description:
            - "The number of CPU cores to enable for a bare metal or Exadata DB system. The valid values depend on the specified shape:"
            - "- BM.DenseIO1.36 - Specify a multiple of 2, from 2 to 36.
              - BM.DenseIO2.52 - Specify a multiple of 2, from 2 to 52.
              - Exadata.Base.48 - Specify a multiple of 2, from 0 to 48.
              - Exadata.Quarter1.84 - Specify a multiple of 2, from 22 to 84.
              - Exadata.Half1.168 - Specify a multiple of 4, from 44 to 168.
              - Exadata.Full1.336 - Specify a multiple of 8, from 88 to 336.
              - Exadata.Quarter2.92 - Specify a multiple of 2, from 0 to 92.
              - Exadata.Half2.184 - Specify a multiple of 4, from 0 to 184.
              - Exadata.Full2.368 - Specify a multiple of 8, from 0 to 368."
            - This parameter is not used for virtual machine DB systems because virtual machine DB systems have a set number of cores for each shape.
              For information about the number of cores for a virtual machine DB system shape, see L(Virtual Machine DB
              Systems,https://docs.cloud.oracle.com/Content/Database/Concepts/overview.htm#virtualmachine)
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: int
    cluster_name:
        description:
            - The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may contain
              hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.
        type: str
    data_storage_percentage:
        description:
            - The percentage assigned to DATA storage (user data and database files).
              The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups).
              Specify 80 or 40. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.
        type: int
    data_storage_size_in_gbs:
        description:
            - Size (in GB) of the initial data volume that will be created and attached to a virtual machine DB system. You can scale up storage after
              provisioning, as needed. Note that the total storage size attached will be more than the amount you specify to allow for REDO/RECO space and
              software volume.
            - This parameter is updatable.
        type: int
        aliases: ["initial_data_storage_size_in_gb"]
    kms_key_id:
        description:
            - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
        type: str
    kms_key_version_id:
        description:
            - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
              versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
        type: str
    node_count:
        description:
            - The number of nodes to launch for a 2-node RAC virtual machine DB system. Specify either 1 or 2.
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
    source:
        description:
            - "The source of the database:
              Use `NONE` for creating a new database. Use `DB_BACKUP` for creating a new database by restoring from a backup. Use `DATABASE` for creating
              a new database from an existing database, including archive redo log data. The default is `NONE`."
        type: str
        choices:
            - "NONE"
            - "DB_SYSTEM"
            - "DATABASE"
            - "DB_BACKUP"
        default: "NONE"
    private_ip:
        description:
            - A private IP address of your choice. Must be an available IP address within the subnet's CIDR.
              If you don't specify a value, Oracle automatically assigns a private IP address from the subnet.
        type: str
    db_home:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            display_name:
                description:
                    - The user-provided name of the Database Home.
                type: str
                aliases: ["name"]
            db_version:
                description:
                    - A valid Oracle Database version. To get a list of supported versions, use the L(ListDbVersions,https://docs.cloud.oracle.com/en-
                      us/iaas/api/#/en/database/latest/DbVersionSummary/ListDbVersions) operation.
                    - Required when source is 'NONE'
                type: str
            database_software_image_id:
                description:
                    - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    - Applicable when source is one of ['NONE', 'DB_BACKUP']
                type: str
            database:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    db_name:
                        description:
                            - The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters.
                              Special characters are not permitted.
                            - Required when source is 'NONE'
                        type: str
                    db_unique_name:
                        description:
                            - The `DB_UNIQUE_NAME` of the Oracle Database being backed up.
                        type: str
                    database_software_image_id:
                        description:
                            - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
                            - Applicable when source is 'NONE'
                        type: str
                    pdb_name:
                        description:
                            - The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty
                              alphanumeric characters. Special characters are not permitted. Pluggable database should not be same as database name.
                            - Applicable when source is 'NONE'
                        type: str
                    admin_password:
                        description:
                            - "A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two
                              uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -."
                        type: str
                        required: true
                    tde_wallet_password:
                        description:
                            - "The optional password to open the TDE wallet. The password must be at least nine characters and contain at least two uppercase,
                              two lowercase, two numeric, and two special characters. The special characters must be _, #, or -."
                            - Applicable when source is 'NONE'
                        type: str
                    character_set:
                        description:
                            - "The character set for the database.  The default is AL32UTF8. Allowed values are:"
                            - AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711,
                              AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775,
                              BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2,
                              EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851,
                              EL8PC869, ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC,
                              JA16EUCTILDE, JA16SJIS, JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921,
                              LT8PC772, LT8PC774, LV8PC1117, LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866,
                              SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII, TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258,
                              VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1, WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850,
                              WE8PC858, WE8PC860, WE8ROMAN8, ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC,
                              ZHT32SOPS, ZHT32TRIS
                            - Applicable when source is 'NONE'
                        type: str
                    ncharacter_set:
                        description:
                            - "The national character set for the database.  The default is AL16UTF16. Allowed values are:
                              AL16UTF16 or UTF8."
                            - Applicable when source is 'NONE'
                        type: str
                    db_workload:
                        description:
                            - The database workload type.
                            - Applicable when source is 'NONE'
                        type: str
                        choices:
                            - "OLTP"
                            - "DSS"
                    db_backup_config:
                        description:
                            - ""
                            - Applicable when source is one of ['DB_SYSTEM', 'NONE']
                        type: dict
                        suboptions:
                            auto_backup_enabled:
                                description:
                                    - If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you
                                      switch to using the Console or the API for backups, a new backup configuration is created and associated with your
                                      database. This means that you can no longer rely on your previously configured unmanaged backups to work.
                                    - Applicable when source is 'NONE'
                                type: bool
                            recovery_window_in_days:
                                description:
                                    - Number of days between the current and the earliest point of recoverability covered by automatic backups.
                                      This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic
                                      backups that are created before the window.
                                      When the value is updated, it is applied to all existing automatic backups.
                                    - Applicable when source is 'NONE'
                                type: int
                            auto_backup_window:
                                description:
                                    - Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time
                                      windows. If no option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically
                                      chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00
                                      AM (inclusive) to 4:00 AM (exclusive).
                                    - "Example: `SLOT_TWO`"
                                    - Applicable when source is 'NONE'
                                type: str
                                choices:
                                    - "SLOT_ONE"
                                    - "SLOT_TWO"
                                    - "SLOT_THREE"
                                    - "SLOT_FOUR"
                                    - "SLOT_FIVE"
                                    - "SLOT_SIX"
                                    - "SLOT_SEVEN"
                                    - "SLOT_EIGHT"
                                    - "SLOT_NINE"
                                    - "SLOT_TEN"
                                    - "SLOT_ELEVEN"
                                    - "SLOT_TWELVE"
                            backup_destination_details:
                                description:
                                    - Backup destination details.
                                    - Applicable when source is 'NONE'
                                type: list
                                elements: dict
                                suboptions:
                                    type:
                                        description:
                                            - Type of the database backup destination.
                                            - Required when source is 'NONE'
                                        type: str
                                        choices:
                                            - "NFS"
                                            - "RECOVERY_APPLIANCE"
                                            - "OBJECT_STORE"
                                            - "LOCAL"
                                        required: true
                                    id:
                                        description:
                                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                                            - Applicable when source is 'NONE'
                                        type: str
                                    vpc_user:
                                        description:
                                            - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the
                                              Recovery Appliance.
                                            - Applicable when source is 'NONE'
                                        type: str
                                    vpc_password:
                                        description:
                                            - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery
                                              Appliance.
                                            - Applicable when source is 'NONE'
                                        type: str
                                    internet_proxy:
                                        description:
                                            - Proxy URL to connect to object store.
                                            - Applicable when source is 'NONE'
                                        type: str
                    freeform_tags:
                        description:
                            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                            - "Example: `{\\"Department\\": \\"Finance\\"}`"
                            - Applicable when source is one of ['DB_SYSTEM', 'NONE']
                        type: dict
                    defined_tags:
                        description:
                            - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                            - Applicable when source is one of ['DB_SYSTEM', 'NONE']
                        type: dict
                    sid_prefix:
                        description:
                            - Specifies a prefix for the `Oracle SID` of the database to be created.
                            - Applicable when source is one of ['NONE', 'DB_BACKUP']
                        type: str
                    db_domain:
                        description:
                            - The database domain. In a distributed database system, DB_DOMAIN specifies the logical location of the database within the network
                              structure.
                            - Applicable when source is 'DB_SYSTEM'
                        type: str
                    database_id:
                        description:
                            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                            - Required when source is 'DATABASE'
                        type: str
                    backup_tde_password:
                        description:
                            - The password to open the TDE wallet.
                            - Applicable when source is one of ['DATABASE', 'DB_BACKUP']
                        type: str
                    time_stamp_for_point_in_time_recovery:
                        description:
                            - The point in time of the original database from which the new database is created. If not specifed, the latest backup is used to
                              create the database.
                            - Applicable when source is 'DATABASE'
                        type: str
                    backup_id:
                        description:
                            - The backup L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                            - Required when source is 'DB_BACKUP'
                        type: str
            freeform_tags:
                description:
                    - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    - Applicable when source is 'DB_SYSTEM'
                type: dict
            defined_tags:
                description:
                    - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                    - Applicable when source is 'DB_SYSTEM'
                type: dict
    database_edition:
        description:
            - The Oracle Database Edition that applies to all the databases on the DB system.
              Exadata DB systems and 2-node RAC DB systems require ENTERPRISE_EDITION_EXTREME_PERFORMANCE.
            - Required when source is one of ['DATABASE', 'NONE', 'DB_BACKUP']
        type: str
        choices:
            - "STANDARD_EDITION"
            - "ENTERPRISE_EDITION"
            - "ENTERPRISE_EDITION_HIGH_PERFORMANCE"
            - "ENTERPRISE_EDITION_EXTREME_PERFORMANCE"
    disk_redundancy:
        description:
            - The type of redundancy configured for the DB system.
              Normal is 2-way redundancy, recommended for test and development systems.
              High is 3-way redundancy, recommended for production systems.
            - Applicable when source is one of ['DATABASE', 'NONE', 'DB_BACKUP']
        type: str
        choices:
            - "HIGH"
            - "NORMAL"
    license_model:
        description:
            - The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.
            - This parameter is updatable.
        type: str
        choices:
            - "LICENSE_INCLUDED"
            - "BRING_YOUR_OWN_LICENSE"
    maintenance_window_details:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when source is 'NONE'
        type: dict
        suboptions:
            preference:
                description:
                    - The maintenance window scheduling preference.
                    - Required when source is 'NONE'
                type: str
                choices:
                    - "NO_PREFERENCE"
                    - "CUSTOM_PREFERENCE"
                required: true
            months:
                description:
                    - Months during the year when maintenance should be performed.
                    - Applicable when source is 'NONE'
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - Name of the month of the year.
                            - Required when source is 'NONE'
                        type: str
                        choices:
                            - "JANUARY"
                            - "FEBRUARY"
                            - "MARCH"
                            - "APRIL"
                            - "MAY"
                            - "JUNE"
                            - "JULY"
                            - "AUGUST"
                            - "SEPTEMBER"
                            - "OCTOBER"
                            - "NOVEMBER"
                            - "DECEMBER"
                        required: true
            weeks_of_month:
                description:
                    - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                      duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                      For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                      Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                      Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of the
                      week and hours that maintenance will be performed.
                    - Applicable when source is 'NONE'
                type: list
                elements: int
            days_of_week:
                description:
                    - Days during the week when maintenance should be performed.
                    - Applicable when source is 'NONE'
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - Name of the day of the week.
                            - Required when source is 'NONE'
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
            hours_of_day:
                description:
                    - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                      - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12 -
                        represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59 UTC"
                    - Applicable when source is 'NONE'
                type: list
                elements: int
            lead_time_in_weeks:
                description:
                    - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to 4.
                    - Applicable when source is 'NONE'
                type: int
    source_db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            - Required when source is 'DB_SYSTEM'
        type: str
    db_system_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    version:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            patch_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch.
                    - This parameter is updatable.
                type: str
            database_software_image_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database software image.
                    - This parameter is updatable.
                type: str
            action:
                description:
                    - The action to perform on the patch.
                    - This parameter is updatable.
                type: str
                choices:
                    - "APPLY"
                    - "PRECHECK"
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
- name: Create db_system with source = NONE
  oci_database_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    shape: shape_example
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    hostname: hostname_example
    cpu_core_count: 56
    db_home:
      # required
      database:
        # required
        admin_password: example-password

        # optional
        db_name: db_name_example
        db_unique_name: db_unique_name_example
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        pdb_name: pdb_name_example
        tde_wallet_password: example-password
        character_set: character_set_example
        ncharacter_set: ncharacter_set_example
        db_workload: OLTP
        db_backup_config:
          # optional
          auto_backup_enabled: true
          recovery_window_in_days: 56
          auto_backup_window: SLOT_ONE
          backup_destination_details:
          - # required
            type: NFS

            # optional
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            vpc_user: vpc_user_example
            vpc_password: example-password
            internet_proxy: internet_proxy_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        sid_prefix: sid_prefix_example
        db_domain: db_domain_example
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        backup_tde_password: example-password
        time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
        backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"

            # optional
      display_name: display_name_example
      db_version: db_version_example
      database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
    database_edition: STANDARD_EDITION

    # optional
    fault_domains: [ "fault_domains_example" ]
    display_name: display_name_example
    backup_subnet_id: "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    time_zone: time_zone_example
    db_system_options:
      # optional
      storage_management: ASM
    sparse_diskgroup: true
    domain: domain_example
    cluster_name: cluster_name_example
    data_storage_percentage: 56
    data_storage_size_in_gbs: 56
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
    node_count: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    source: NONE
    private_ip: private_ip_example
    disk_redundancy: HIGH
    license_model: LICENSE_INCLUDED
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56

- name: Create db_system with source = DB_SYSTEM
  oci_database_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    shape: shape_example
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    hostname: hostname_example
    cpu_core_count: 56
    source: DB_SYSTEM
    db_home:
      # required
      database:
        # required
        admin_password: example-password

        # optional
        db_name: db_name_example
        db_unique_name: db_unique_name_example
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        pdb_name: pdb_name_example
        tde_wallet_password: example-password
        character_set: character_set_example
        ncharacter_set: ncharacter_set_example
        db_workload: OLTP
        db_backup_config:
          # optional
          auto_backup_enabled: true
          recovery_window_in_days: 56
          auto_backup_window: SLOT_ONE
          backup_destination_details:
          - # required
            type: NFS

            # optional
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            vpc_user: vpc_user_example
            vpc_password: example-password
            internet_proxy: internet_proxy_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        sid_prefix: sid_prefix_example
        db_domain: db_domain_example
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        backup_tde_password: example-password
        time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
        backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"

            # optional
      display_name: display_name_example
      db_version: db_version_example
      database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
    source_db_system_id: "ocid1.sourcedbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    fault_domains: [ "fault_domains_example" ]
    display_name: display_name_example
    backup_subnet_id: "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    time_zone: time_zone_example
    db_system_options:
      # optional
      storage_management: ASM
    sparse_diskgroup: true
    domain: domain_example
    cluster_name: cluster_name_example
    data_storage_percentage: 56
    data_storage_size_in_gbs: 56
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
    node_count: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    private_ip: private_ip_example
    license_model: LICENSE_INCLUDED

- name: Create db_system with source = DATABASE
  oci_database_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    shape: shape_example
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    hostname: hostname_example
    cpu_core_count: 56
    source: DATABASE
    db_home:
      # required
      database:
        # required
        admin_password: example-password

        # optional
        db_name: db_name_example
        db_unique_name: db_unique_name_example
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        pdb_name: pdb_name_example
        tde_wallet_password: example-password
        character_set: character_set_example
        ncharacter_set: ncharacter_set_example
        db_workload: OLTP
        db_backup_config:
          # optional
          auto_backup_enabled: true
          recovery_window_in_days: 56
          auto_backup_window: SLOT_ONE
          backup_destination_details:
          - # required
            type: NFS

            # optional
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            vpc_user: vpc_user_example
            vpc_password: example-password
            internet_proxy: internet_proxy_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        sid_prefix: sid_prefix_example
        db_domain: db_domain_example
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        backup_tde_password: example-password
        time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
        backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"

            # optional
      display_name: display_name_example
      db_version: db_version_example
      database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
    database_edition: STANDARD_EDITION

    # optional
    fault_domains: [ "fault_domains_example" ]
    display_name: display_name_example
    backup_subnet_id: "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    time_zone: time_zone_example
    db_system_options:
      # optional
      storage_management: ASM
    sparse_diskgroup: true
    domain: domain_example
    cluster_name: cluster_name_example
    data_storage_percentage: 56
    data_storage_size_in_gbs: 56
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
    node_count: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    private_ip: private_ip_example
    disk_redundancy: HIGH
    license_model: LICENSE_INCLUDED

- name: Create db_system with source = DB_BACKUP
  oci_database_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1
    subnet_id: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
    shape: shape_example
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    hostname: hostname_example
    cpu_core_count: 56
    source: DB_BACKUP
    db_home:
      # required
      database:
        # required
        admin_password: example-password

        # optional
        db_name: db_name_example
        db_unique_name: db_unique_name_example
        database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        pdb_name: pdb_name_example
        tde_wallet_password: example-password
        character_set: character_set_example
        ncharacter_set: ncharacter_set_example
        db_workload: OLTP
        db_backup_config:
          # optional
          auto_backup_enabled: true
          recovery_window_in_days: 56
          auto_backup_window: SLOT_ONE
          backup_destination_details:
          - # required
            type: NFS

            # optional
            id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
            vpc_user: vpc_user_example
            vpc_password: example-password
            internet_proxy: internet_proxy_example
        freeform_tags: {'Department': 'Finance'}
        defined_tags: {'Operations': {'CostCenter': 'US'}}
        sid_prefix: sid_prefix_example
        db_domain: db_domain_example
        database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
        backup_tde_password: example-password
        time_stamp_for_point_in_time_recovery: time_stamp_for_point_in_time_recovery_example
        backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"

            # optional
      display_name: display_name_example
      db_version: db_version_example
      database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
    database_edition: STANDARD_EDITION

    # optional
    fault_domains: [ "fault_domains_example" ]
    display_name: display_name_example
    backup_subnet_id: "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx"
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    time_zone: time_zone_example
    db_system_options:
      # optional
      storage_management: ASM
    sparse_diskgroup: true
    domain: domain_example
    cluster_name: cluster_name_example
    data_storage_percentage: 56
    data_storage_size_in_gbs: 56
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
    node_count: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    private_ip: private_ip_example
    disk_redundancy: HIGH
    license_model: LICENSE_INCLUDED

- name: Update db_system
  oci_database_db_system:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    shape: shape_example
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    cpu_core_count: 56
    data_storage_size_in_gbs: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    license_model: LICENSE_INCLUDED
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    version:
      # optional
      patch_id: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
      database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
      action: APPLY

- name: Update db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_db_system:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    nsg_ids: [ "nsg_ids_example" ]
    backup_network_nsg_ids: [ "backup_network_nsg_ids_example" ]
    shape: shape_example
    ssh_public_keys: [ "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz..." ]
    cpu_core_count: 56
    data_storage_size_in_gbs: 56
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    license_model: LICENSE_INCLUDED
    maintenance_window_details:
      # required
      preference: NO_PREFERENCE

      # optional
      months:
      - # required
        name: JANUARY
      weeks_of_month: [ "weeks_of_month_example" ]
      days_of_week:
      - # required
        name: MONDAY
      hours_of_day: [ "hours_of_day_example" ]
      lead_time_in_weeks: 56
    version:
      # optional
      patch_id: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
      database_software_image_id: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
      action: APPLY

- name: Delete db_system
  oci_database_db_system:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete db_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_db_system:
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
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the DB system. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        availability_domain:
            description:
                - The name of the availability domain that the DB system is located in.
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        fault_domains:
            description:
                - List of the Fault Domains in which this DB system is provisioned.
            returned: on success
            type: list
            sample: []
        subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the subnet the DB system is associated with.
                - "**Subnet Restrictions:**
                  - For bare metal DB systems and for single node virtual machine DB systems, do not use a subnet that overlaps with 192.168.16.16/28.
                  - For Exadata and virtual machine 2-node RAC DB systems, do not use a subnet that overlaps with 192.168.128.0/20."
                - These subnets are used by the Oracle Clusterware private interconnect on the database instance.
                  Specifying an overlapping subnet will cause the private interconnect to malfunction.
                  This restriction applies to both the client subnet and backup subnet.
            returned: on success
            type: str
            sample: "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx"
        backup_subnet_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup network subnet the DB system is associated
                  with. Applicable only to Exadata DB systems.
                - "**Subnet Restriction:** See the subnet restrictions information for **subnetId**."
            returned: on success
            type: str
            sample: "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx"
        nsg_ids:
            description:
                - "A list of the L(OCIDs,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the network security groups (NSGs) that this
                  resource belongs to. Setting this to an empty array after the list is created removes the resource from all NSGs. For more information about
                  NSGs, see L(Security Rules,https://docs.cloud.oracle.com/Content/Network/Concepts/securityrules.htm).
                  **NsgIds restrictions:**
                  - Autonomous Databases with private access require at least 1 Network Security Group (NSG). The nsgIds array cannot be empty."
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
        shape:
            description:
                - "The shape of the DB system. The shape determines resources to allocate to the DB system.
                  - For virtual machine shapes, the number of CPU cores and memory
                  - For bare metal and Exadata shapes, the number of CPU cores, storage, and memory"
            returned: on success
            type: str
            sample: shape_example
        db_system_options:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                storage_management:
                    description:
                        - "The storage option used in DB system.
                          ASM - Automatic storage management
                          LVM - Logical Volume management"
                    returned: on success
                    type: str
                    sample: ASM
        ssh_public_keys:
            description:
                - The public key portion of one or more key pairs used for SSH access to the DB system.
            returned: on success
            type: list
            sample: [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ]
        time_zone:
            description:
                - The time zone of the DB system. For details, see L(DB System Time
                  Zones,https://docs.cloud.oracle.com/Content/Database/References/timezones.htm).
            returned: on success
            type: str
            sample: time_zone_example
        hostname:
            description:
                - The hostname for the DB system.
            returned: on success
            type: str
            sample: hostname_example
        domain:
            description:
                - The domain name for the DB system.
            returned: on success
            type: str
            sample: domain_example
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        version:
            description:
                - The Oracle Database version of the DB system.
            returned: on success
            type: str
            sample: version_example
        cpu_core_count:
            description:
                - The number of CPU cores enabled on the DB system.
            returned: on success
            type: int
            sample: 56
        cluster_name:
            description:
                - The cluster name for Exadata and 2-node RAC virtual machine DB systems. The cluster name must begin with an alphabetic character, and may
                  contain hyphens (-). Underscores (_) are not permitted. The cluster name can be no longer than 11 characters and is not case sensitive.
            returned: on success
            type: str
            sample: cluster_name_example
        data_storage_percentage:
            description:
                - The percentage assigned to DATA storage (user data and database files).
                  The remaining percentage is assigned to RECO storage (database redo logs, archive logs, and recovery manager backups). Accepted values are 40
                  and 80. The default is 80 percent assigned to DATA storage. Not applicable for virtual machine DB systems.
            returned: on success
            type: int
            sample: 56
        database_edition:
            description:
                - The Oracle Database edition that applies to all the databases on the DB system.
            returned: on success
            type: str
            sample: STANDARD_EDITION
        last_patch_history_entry_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last patch history. This value is updated as soon as
                  a patch operation starts.
            returned: on success
            type: str
            sample: "ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
        listener_port:
            description:
                - The port number configured for the listener on the DB system.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the DB system.
            returned: on success
            type: str
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the DB system was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        disk_redundancy:
            description:
                - The type of redundancy configured for the DB system.
                  NORMAL is 2-way redundancy.
                  HIGH is 3-way redundancy.
            returned: on success
            type: str
            sample: HIGH
        sparse_diskgroup:
            description:
                - True, if Sparse Diskgroup is configured for Exadata dbsystem, False, if Sparse diskgroup was not configured.
            returned: on success
            type: bool
            sample: true
        scan_ip_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Single Client Access Name (SCAN) IP addresses
                  associated with the DB system.
                  SCAN IP addresses are typically used for load balancing and are not assigned to any interface.
                  Oracle Clusterware directs the requests to the appropriate nodes in the cluster.
                - "**Note:** For a single-node DB system, this list is empty."
            returned: on success
            type: list
            sample: []
        vip_ids:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the virtual IP (VIP) addresses associated with the DB
                  system.
                  The Cluster Ready Services (CRS) creates and maintains one VIP address for each node in the DB system to
                  enable failover. If one node fails, the VIP is reassigned to another active node in the cluster.
                - "**Note:** For a single-node DB system, this list is empty."
            returned: on success
            type: list
            sample: []
        scan_dns_record_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DNS record for the SCAN IP addresses that are
                  associated with the DB system.
            returned: on success
            type: str
            sample: "ocid1.scandnsrecord.oc1..xxxxxxEXAMPLExxxxxx"
        scan_dns_name:
            description:
                - The FQDN of the DNS record for the SCAN IP addresses that are associated with the DB system.
            returned: on success
            type: str
            sample: scan_dns_name_example
        zone_id:
            description:
                - The OCID of the zone the DB system is associated with.
            returned: on success
            type: str
            sample: "ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx"
        data_storage_size_in_gbs:
            description:
                - The data storage size, in gigabytes, that is currently available to the DB system. Applies only for virtual machine DB systems.
            returned: on success
            type: int
            sample: 56
        reco_storage_size_in_gb:
            description:
                - The RECO/REDO storage size, in gigabytes, that is currently allocated to the DB system. Applies only for virtual machine DB systems.
            returned: on success
            type: int
            sample: 56
        node_count:
            description:
                - The number of nodes in the DB system. For RAC DB systems, the value is greater than 1.
            returned: on success
            type: int
            sample: 56
        license_model:
            description:
                - The Oracle license model that applies to all the databases on the DB system. The default is LICENSE_INCLUDED.
            returned: on success
            type: str
            sample: LICENSE_INCLUDED
        maintenance_window:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                preference:
                    description:
                        - The maintenance window scheduling preference.
                    returned: on success
                    type: str
                    sample: NO_PREFERENCE
                months:
                    description:
                        - Months during the year when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the month of the year.
                            returned: on success
                            type: str
                            sample: JANUARY
                weeks_of_month:
                    description:
                        - Weeks during the month when maintenance should be performed. Weeks start on the 1st, 8th, 15th, and 22nd days of the month, and have a
                          duration of 7 days. Weeks start and end based on calendar dates, not days of the week.
                          For example, to allow maintenance during the 2nd week of the month (from the 8th day to the 14th day of the month), use the value 2.
                          Maintenance cannot be scheduled for the fifth week of months that contain more than 28 days.
                          Note that this parameter works in conjunction with the  daysOfWeek and hoursOfDay parameters to allow you to specify specific days of
                          the week and hours that maintenance will be performed.
                    returned: on success
                    type: list
                    sample: []
                days_of_week:
                    description:
                        - Days during the week when maintenance should be performed.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - Name of the day of the week.
                            returned: on success
                            type: str
                            sample: MONDAY
                hours_of_day:
                    description:
                        - "The window of hours during the day when maintenance should be performed. The window is a 4 hour slot. Valid values are
                          - 0 - represents time slot 0:00 - 3:59 UTC - 4 - represents time slot 4:00 - 7:59 UTC - 8 - represents time slot 8:00 - 11:59 UTC - 12
                            - represents time slot 12:00 - 15:59 UTC - 16 - represents time slot 16:00 - 19:59 UTC - 20 - represents time slot 20:00 - 23:59
                            UTC"
                    returned: on success
                    type: list
                    sample: []
                lead_time_in_weeks:
                    description:
                        - Lead time window allows user to set a lead time to prepare for a down time. The lead time is in weeks and valid value is between 1 to
                          4.
                    returned: on success
                    type: int
                    sample: 56
        last_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last maintenance run.
            returned: on success
            type: str
            sample: "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        next_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the next maintenance run.
            returned: on success
            type: str
            sample: "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
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
        source_db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: str
            sample: "ocid1.sourcedbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        point_in_time_data_disk_clone_timestamp:
            description:
                - The point in time for a cloned database system when the data disks were cloned from the source database system, as described in L(RFC
                  3339,https://tools.ietf.org/rfc/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "display_name": "display_name_example",
        "availability_domain": "Uocm:PHX-AD-1",
        "fault_domains": [],
        "subnet_id": "ocid1.subnet.oc1..xxxxxxEXAMPLExxxxxx",
        "backup_subnet_id": "ocid1.backupsubnet.oc1..xxxxxxEXAMPLExxxxxx",
        "nsg_ids": [],
        "backup_network_nsg_ids": [],
        "shape": "shape_example",
        "db_system_options": {
            "storage_management": "ASM"
        },
        "ssh_public_keys": [ ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEAz... ],
        "time_zone": "time_zone_example",
        "hostname": "hostname_example",
        "domain": "domain_example",
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "version": "version_example",
        "cpu_core_count": 56,
        "cluster_name": "cluster_name_example",
        "data_storage_percentage": 56,
        "database_edition": "STANDARD_EDITION",
        "last_patch_history_entry_id": "ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx",
        "listener_port": 56,
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "disk_redundancy": "HIGH",
        "sparse_diskgroup": true,
        "scan_ip_ids": [],
        "vip_ids": [],
        "scan_dns_record_id": "ocid1.scandnsrecord.oc1..xxxxxxEXAMPLExxxxxx",
        "scan_dns_name": "scan_dns_name_example",
        "zone_id": "ocid1.zone.oc1..xxxxxxEXAMPLExxxxxx",
        "data_storage_size_in_gbs": 56,
        "reco_storage_size_in_gb": 56,
        "node_count": 56,
        "license_model": "LICENSE_INCLUDED",
        "maintenance_window": {
            "preference": "NO_PREFERENCE",
            "months": [{
                "name": "JANUARY"
            }],
            "weeks_of_month": [],
            "days_of_week": [{
                "name": "MONDAY"
            }],
            "hours_of_day": [],
            "lead_time_in_weeks": 56
        },
        "last_maintenance_run_id": "ocid1.lastmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "next_maintenance_run_id": "ocid1.nextmaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "source_db_system_id": "ocid1.sourcedbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "point_in_time_data_disk_clone_timestamp": "2013-10-20T19:20:30+01:00"
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
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import LaunchDbSystemBase
    from oci.database.models import UpdateDbSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbSystemHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(DbSystemHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
        return "db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_system_id")

    def get_get_fn(self):
        return self.client.get_db_system

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
        optional_list_method_params = ["availability_domain", "display_name"]

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
        return LaunchDbSystemBase

    def get_exclude_attributes(self):
        return [
            "data_storage_size_in_gbs",
            "kms_key_version_id",
            "source",
            "private_ip",
            "db_home",
            "maintenance_window_details",
        ]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.launch_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(launch_db_system_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
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
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.terminate_db_system,
            call_fn_args=(),
            call_fn_kwargs=dict(db_system_id=self.module.params.get("db_system_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DbSystemHelperCustom = get_custom_class("DbSystemHelperCustom")


class ResourceHelper(DbSystemHelperCustom, DbSystemHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            fault_domains=dict(type="list", elements="str"),
            display_name=dict(aliases=["name"], type="str"),
            availability_domain=dict(type="str"),
            subnet_id=dict(type="str"),
            backup_subnet_id=dict(type="str"),
            nsg_ids=dict(type="list", elements="str"),
            backup_network_nsg_ids=dict(type="list", elements="str"),
            shape=dict(type="str"),
            time_zone=dict(type="str"),
            db_system_options=dict(
                type="dict",
                options=dict(
                    storage_management=dict(type="str", choices=["ASM", "LVM"])
                ),
            ),
            sparse_diskgroup=dict(type="bool"),
            ssh_public_keys=dict(type="list", elements="str", no_log=True),
            hostname=dict(type="str"),
            domain=dict(type="str"),
            cpu_core_count=dict(type="int"),
            cluster_name=dict(type="str"),
            data_storage_percentage=dict(type="int"),
            data_storage_size_in_gbs=dict(
                aliases=["initial_data_storage_size_in_gb"], type="int"
            ),
            kms_key_id=dict(type="str"),
            kms_key_version_id=dict(type="str"),
            node_count=dict(type="int"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            source=dict(
                type="str",
                default="NONE",
                choices=["NONE", "DB_SYSTEM", "DATABASE", "DB_BACKUP"],
            ),
            private_ip=dict(type="str"),
            db_home=dict(
                type="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str"),
                    db_version=dict(type="str"),
                    database_software_image_id=dict(type="str"),
                    database=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            db_name=dict(type="str"),
                            db_unique_name=dict(type="str"),
                            database_software_image_id=dict(type="str"),
                            pdb_name=dict(type="str"),
                            admin_password=dict(type="str", required=True, no_log=True),
                            tde_wallet_password=dict(type="str", no_log=True),
                            character_set=dict(type="str"),
                            ncharacter_set=dict(type="str"),
                            db_workload=dict(type="str", choices=["OLTP", "DSS"]),
                            db_backup_config=dict(
                                type="dict",
                                options=dict(
                                    auto_backup_enabled=dict(type="bool"),
                                    recovery_window_in_days=dict(type="int"),
                                    auto_backup_window=dict(
                                        type="str",
                                        choices=[
                                            "SLOT_ONE",
                                            "SLOT_TWO",
                                            "SLOT_THREE",
                                            "SLOT_FOUR",
                                            "SLOT_FIVE",
                                            "SLOT_SIX",
                                            "SLOT_SEVEN",
                                            "SLOT_EIGHT",
                                            "SLOT_NINE",
                                            "SLOT_TEN",
                                            "SLOT_ELEVEN",
                                            "SLOT_TWELVE",
                                        ],
                                    ),
                                    backup_destination_details=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "NFS",
                                                    "RECOVERY_APPLIANCE",
                                                    "OBJECT_STORE",
                                                    "LOCAL",
                                                ],
                                            ),
                                            id=dict(type="str"),
                                            vpc_user=dict(type="str"),
                                            vpc_password=dict(type="str", no_log=True),
                                            internet_proxy=dict(type="str"),
                                        ),
                                    ),
                                ),
                            ),
                            freeform_tags=dict(type="dict"),
                            defined_tags=dict(type="dict"),
                            sid_prefix=dict(type="str"),
                            db_domain=dict(type="str"),
                            database_id=dict(type="str"),
                            backup_tde_password=dict(type="str", no_log=True),
                            time_stamp_for_point_in_time_recovery=dict(type="str"),
                            backup_id=dict(type="str"),
                        ),
                    ),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            database_edition=dict(
                type="str",
                choices=[
                    "STANDARD_EDITION",
                    "ENTERPRISE_EDITION",
                    "ENTERPRISE_EDITION_HIGH_PERFORMANCE",
                    "ENTERPRISE_EDITION_EXTREME_PERFORMANCE",
                ],
            ),
            disk_redundancy=dict(type="str", choices=["HIGH", "NORMAL"]),
            license_model=dict(
                type="str", choices=["LICENSE_INCLUDED", "BRING_YOUR_OWN_LICENSE"]
            ),
            maintenance_window_details=dict(
                type="dict",
                options=dict(
                    preference=dict(
                        type="str",
                        required=True,
                        choices=["NO_PREFERENCE", "CUSTOM_PREFERENCE"],
                    ),
                    months=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            name=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "JANUARY",
                                    "FEBRUARY",
                                    "MARCH",
                                    "APRIL",
                                    "MAY",
                                    "JUNE",
                                    "JULY",
                                    "AUGUST",
                                    "SEPTEMBER",
                                    "OCTOBER",
                                    "NOVEMBER",
                                    "DECEMBER",
                                ],
                            )
                        ),
                    ),
                    weeks_of_month=dict(type="list", elements="int"),
                    days_of_week=dict(
                        type="list",
                        elements="dict",
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
                    hours_of_day=dict(type="list", elements="int"),
                    lead_time_in_weeks=dict(type="int"),
                ),
            ),
            source_db_system_id=dict(type="str"),
            db_system_id=dict(aliases=["id"], type="str"),
            version=dict(
                type="dict",
                options=dict(
                    patch_id=dict(type="str"),
                    database_software_image_id=dict(type="str"),
                    action=dict(type="str", choices=["APPLY", "PRECHECK"]),
                ),
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_system",
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
