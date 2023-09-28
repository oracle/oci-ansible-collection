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
module: oci_database_database
short_description: Manage a Database resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Database resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new database in the specified Database Home. If the database version is provided, it must match the version of the
      Database Home. Applies to Exadata and Exadata Cloud@Customer systems.
    - "This resource has the following action operations in the M(oracle.oci.oci_database_database_actions) module: precheck, upgrade, rollback."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_version:
        description:
            - A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.
            - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel, adminPassword,
              whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable, dbName,
              scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
        type: str
    source:
        description:
            - "The source of the database:
              Use `NONE` for creating a new database.
              Use `DB_BACKUP` for creating a new database by restoring from a backup.
              The default is `NONE`."
            - Required for create using I(state=present).
        type: str
        choices:
            - "NONE"
            - "DB_BACKUP"
        default: "NONE"
    kms_key_id:
        description:
            - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
        type: str
    kms_key_version_id:
        description:
            - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
              versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
        type: str
    database:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            database_software_image_id:
                description:
                    - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
                    - Applicable when source is 'NONE'
                type: str
            pdb_name:
                description:
                    - The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric
                      characters. Special characters are not permitted. Pluggable database should not be same as database name.
                    - Applicable when source is 'NONE'
                type: str
            tde_wallet_password:
                description:
                    - "The optional password to open the TDE wallet. The password must be at least nine characters and contain at least two uppercase, two
                      lowercase, two numeric, and two special characters. The special characters must be _, #, or -."
                    - Applicable when source is 'NONE'
                type: str
            character_set:
                description:
                    - "The character set for the database.  The default is AL32UTF8. Allowed values are:"
                    - AL32UTF8, AR8ADOS710, AR8ADOS720, AR8APTEC715, AR8ARABICMACS, AR8ASMO8X, AR8ISO8859P6, AR8MSWIN1256, AR8MUSSAD768, AR8NAFITHA711,
                      AR8NAFITHA721, AR8SAKHR706, AR8SAKHR707, AZ8ISO8859P9E, BG8MSWIN, BG8PC437S, BLT8CP921, BLT8ISO8859P13, BLT8MSWIN1257, BLT8PC775,
                      BN8BSCII, CDN8PC863, CEL8ISO8859P14, CL8ISO8859P5, CL8ISOIR111, CL8KOI8R, CL8KOI8U, CL8MACCYRILLICS, CL8MSWIN1251, EE8ISO8859P2,
                      EE8MACCES, EE8MACCROATIANS, EE8MSWIN1250, EE8PC852, EL8DEC, EL8ISO8859P7, EL8MACGREEKS, EL8MSWIN1253, EL8PC437S, EL8PC851, EL8PC869,
                      ET8MSWIN923, HU8ABMOD, HU8CWI2, IN8ISCII, IS8PC861, IW8ISO8859P8, IW8MACHEBREWS, IW8MSWIN1255, IW8PC1507, JA16EUC, JA16EUCTILDE, JA16SJIS,
                      JA16SJISTILDE, JA16VMS, KO16KSC5601, KO16KSCCS, KO16MSWIN949, LA8ISO6937, LA8PASSPORT, LT8MSWIN921, LT8PC772, LT8PC774, LV8PC1117,
                      LV8PC8LR, LV8RST104090, N8PC865, NE8ISO8859P10, NEE8ISO8859P4, RU8BESTA, RU8PC855, RU8PC866, SE8ISO8859P3, TH8MACTHAIS, TH8TISASCII,
                      TR8DEC, TR8MACTURKISHS, TR8MSWIN1254, TR8PC857, US7ASCII, US8PC437, UTF8, VN8MSWIN1258, VN8VN3, WE8DEC, WE8DG, WE8ISO8859P1,
                      WE8ISO8859P15, WE8ISO8859P9, WE8MACROMAN8S, WE8MSWIN1252, WE8NCR4970, WE8NEXTSTEP, WE8PC850, WE8PC858, WE8PC860, WE8ROMAN8,
                      ZHS16CGB231280, ZHS16GBK, ZHT16BIG5, ZHT16CCDC, ZHT16DBT, ZHT16HKSCS, ZHT16MSWIN950, ZHT32EUC, ZHT32SOPS, ZHT32TRIS
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
                    - "**Deprecated.** The dbWorkload field has been deprecated for Exadata Database Service on Dedicated Infrastructure, Exadata Database
                      Service on Cloud@Customer, and Base Database Service.
                      Support for this attribute will end in November 2023. You may choose to update your custom scripts to exclude the dbWorkload attribute.
                      After November 2023 if you pass a value to the dbWorkload attribute, it will be ignored."
                    - The database workload type.
                    - Applicable when source is 'NONE'
                type: str
                choices:
                    - "OLTP"
                    - "DSS"
            db_backup_config:
                description:
                    - ""
                    - Applicable when source is 'NONE'
                type: dict
                suboptions:
                    auto_backup_enabled:
                        description:
                            - If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to
                              using the Console or the API for backups, a new backup configuration is created and associated with your database. This means that
                              you can no longer rely on your previously configured unmanaged backups to work.
                            - Applicable when source is 'NONE'
                        type: bool
                    recovery_window_in_days:
                        description:
                            - Number of days between the current and the earliest point of recoverability covered by automatic backups.
                              This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic backups
                              that are created before the window.
                              When the value is updated, it is applied to all existing automatic backups.
                            - Applicable when source is 'NONE'
                        type: int
                    auto_backup_window:
                        description:
                            - Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time windows. If
                              no option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For
                              example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to
                              4:00 AM (exclusive).
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
                    auto_full_backup_window:
                        description:
                            - Time window selected for initiating full backup for the database system. There are twelve available two-hour time windows. If no
                              option is selected, the value is null and a start time between 12:00 AM to 7:00 AM in the region of the database is automatically
                              chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM
                              (inclusive) to 4:00 AM (exclusive).
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
                    auto_full_backup_day:
                        description:
                            - Day of the week the full backup should be applied on the database system. If no option is selected, the value is null and we will
                              default to Sunday.
                            - Applicable when source is 'NONE'
                        type: str
                        choices:
                            - "SUNDAY"
                            - "MONDAY"
                            - "TUESDAY"
                            - "WEDNESDAY"
                            - "THURSDAY"
                            - "FRIDAY"
                            - "SATURDAY"
                    run_immediate_full_backup:
                        description:
                            - If set to true, configures automatic full backups in the local region (the region of the DB system) for the first backup run
                              immediately.
                            - Applicable when source is 'NONE'
                        type: bool
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
                                    - "DBRS"
                                required: true
                            id:
                                description:
                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                                    - Applicable when source is 'NONE'
                                type: str
                            vpc_user:
                                description:
                                    - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery
                                      Appliance.
                                    - Applicable when source is 'NONE'
                                type: str
                            vpc_password:
                                description:
                                    - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                                    - Applicable when source is 'NONE'
                                type: str
                            internet_proxy:
                                description:
                                    - Proxy URL to connect to object store.
                                    - Applicable when source is 'NONE'
                                type: str
                            dbrs_policy_id:
                                description:
                                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DBRS policy used for backup.
                                    - Applicable when source is 'NONE'
                                type: str
                    backup_deletion_policy:
                        description:
                            - "This defines when the backups will be deleted. - IMMEDIATE option keep the backup for predefined time i.e 72 hours and then
                              delete permanently... - RETAIN will keep the backups as per the policy defined for database backups."
                            - Applicable when source is 'NONE'
                        type: str
                        choices:
                            - "DELETE_IMMEDIATELY"
                            - "DELETE_AFTER_RETENTION_PERIOD"
            freeform_tags:
                description:
                    - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    - Applicable when source is 'NONE'
                type: dict
            defined_tags:
                description:
                    - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                    - Applicable when source is 'NONE'
                type: dict
            kms_key_id:
                description:
                    - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
                    - Applicable when source is 'NONE'
                type: str
            kms_key_version_id:
                description:
                    - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
                      versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
                    - Applicable when source is 'NONE'
                type: str
            vault_id:
                description:
                    - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Oracle Cloud Infrastructure
                      L(vault,https://docs.cloud.oracle.com/Content/KeyManagement/Concepts/keyoverview.htm#concepts).
                    - Applicable when source is 'NONE'
                type: str
            backup_id:
                description:
                    - The backup L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    - Required when source is 'DB_BACKUP'
                type: str
            backup_tde_password:
                description:
                    - The password to open the TDE wallet.
                    - Applicable when source is 'DB_BACKUP'
                type: str
            admin_password:
                description:
                    - "A strong password for SYS, SYSTEM, and PDB Admin. The password must be at least nine characters and contain at least two uppercase, two
                      lowercase, two numbers, and two special characters. The special characters must be _, #, or -."
                type: str
                required: true
            db_unique_name:
                description:
                    - The `DB_UNIQUE_NAME` of the Oracle Database being backed up.
                type: str
            db_name:
                description:
                    - The database name. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric characters. Special
                      characters are not permitted.
                    - Required when source is 'NONE'
                type: str
            sid_prefix:
                description:
                    - Specifies a prefix for the `Oracle SID` of the database to be created.
                type: str
    db_backup_config:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            auto_backup_enabled:
                description:
                    - If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using the
                      Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can no longer
                      rely on your previously configured unmanaged backups to work.
                    - This parameter is updatable.
                type: bool
            recovery_window_in_days:
                description:
                    - Number of days between the current and the earliest point of recoverability covered by automatic backups.
                      This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic backups that are
                      created before the window.
                      When the value is updated, it is applied to all existing automatic backups.
                    - This parameter is updatable.
                type: int
            auto_backup_window:
                description:
                    - Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time windows. If no
                      option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if the
                      user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM (exclusive).
                    - "Example: `SLOT_TWO`"
                    - This parameter is updatable.
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
            auto_full_backup_window:
                description:
                    - Time window selected for initiating full backup for the database system. There are twelve available two-hour time windows. If no option is
                      selected, the value is null and a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For
                      example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM
                      (exclusive).
                    - "Example: `SLOT_TWO`"
                    - This parameter is updatable.
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
            auto_full_backup_day:
                description:
                    - Day of the week the full backup should be applied on the database system. If no option is selected, the value is null and we will default
                      to Sunday.
                    - This parameter is updatable.
                type: str
                choices:
                    - "SUNDAY"
                    - "MONDAY"
                    - "TUESDAY"
                    - "WEDNESDAY"
                    - "THURSDAY"
                    - "FRIDAY"
                    - "SATURDAY"
            run_immediate_full_backup:
                description:
                    - If set to true, configures automatic full backups in the local region (the region of the DB system) for the first backup run immediately.
                    - This parameter is updatable.
                type: bool
            backup_destination_details:
                description:
                    - Backup destination details.
                type: list
                elements: dict
                suboptions:
                    type:
                        description:
                            - Type of the database backup destination.
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "NFS"
                            - "RECOVERY_APPLIANCE"
                            - "OBJECT_STORE"
                            - "LOCAL"
                            - "DBRS"
                        required: true
                    id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                            - This parameter is updatable.
                        type: str
                    vpc_user:
                        description:
                            - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery Appliance.
                            - This parameter is updatable.
                        type: str
                    vpc_password:
                        description:
                            - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                            - This parameter is updatable.
                        type: str
                    internet_proxy:
                        description:
                            - Proxy URL to connect to object store.
                            - This parameter is updatable.
                        type: str
                    dbrs_policy_id:
                        description:
                            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DBRS policy used for backup.
                            - This parameter is updatable.
                        type: str
            backup_deletion_policy:
                description:
                    - "This defines when the backups will be deleted. - IMMEDIATE option keep the backup for predefined time i.e 72 hours and then delete
                      permanently... - RETAIN will keep the backups as per the policy defined for database backups."
                    - This parameter is updatable.
                type: str
                choices:
                    - "DELETE_IMMEDIATELY"
                    - "DELETE_AFTER_RETENTION_PERIOD"
    db_home_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    new_admin_password:
        description:
            - "A new strong password for SYS, SYSTEM, and the plugbable database ADMIN user. The password must be at least nine characters and contain at least
              two uppercase, two lowercase, two numeric, and two special characters. The special characters must be _, #, or -."
            - This parameter is updatable.
        type: str
    old_tde_wallet_password:
        description:
            - The existing TDE wallet password. You must provide the existing password in order to set a new TDE wallet password.
            - This parameter is updatable.
        type: str
    new_tde_wallet_password:
        description:
            - "The new password to open the TDE wallet. The password must be at least nine characters and contain at least two uppercase, two lowercase, two
              numeric, and two special characters. The special characters must be _, #, or -."
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
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    perform_final_backup:
        description:
            - Whether to perform a final backup of the database or not. Default is false.
            - If you previously used RMAN or dbcli to configure backups and then you switch to using the Console or the API for backups, a new backup
              configuration is created and associated with your database. This means that you can no longer rely on your previously configured unmanaged backups
              to work.
            - This parameter is used in multiple APIs. Refer to the API description for details on how the operation uses it.
        type: bool
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the Database.
            - Use I(state=present) to create or update a Database.
            - Use I(state=absent) to delete a Database.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create database with source = NONE
  oci_database_database:
    # required
    database:
      # required
      admin_password: example-password

      # optional
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
        auto_full_backup_window: SLOT_ONE
        auto_full_backup_day: SUNDAY
        run_immediate_full_backup: true
        backup_destination_details:
        - # required
          type: NFS

          # optional
          id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
          vpc_user: vpc_user_example
          vpc_password: example-password
          internet_proxy: internet_proxy_example
          dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
        backup_deletion_policy: DELETE_IMMEDIATELY
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
      kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
      backup_tde_password: example-password
      db_unique_name: db_unique_name_example
      db_name: db_name_example
      sid_prefix: sid_prefix_example
    db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_version: db_version_example
    source: NONE
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create database with source = DB_BACKUP
  oci_database_database:
    # required
    source: DB_BACKUP
    database:
      # required
      admin_password: example-password

      # optional
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
        auto_full_backup_window: SLOT_ONE
        auto_full_backup_day: SUNDAY
        run_immediate_full_backup: true
        backup_destination_details:
        - # required
          type: NFS

          # optional
          id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
          vpc_user: vpc_user_example
          vpc_password: example-password
          internet_proxy: internet_proxy_example
          dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
        backup_deletion_policy: DELETE_IMMEDIATELY
      freeform_tags: {'Department': 'Finance'}
      defined_tags: {'Operations': {'CostCenter': 'US'}}
      kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
      kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"
      vault_id: "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx"
      backup_id: "ocid1.backup.oc1..xxxxxxEXAMPLExxxxxx"
      backup_tde_password: example-password
      db_unique_name: db_unique_name_example
      db_name: db_name_example
      sid_prefix: sid_prefix_example
    db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_version: db_version_example
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    kms_key_version_id: "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update database
  oci_database_database:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    db_backup_config:
      # optional
      auto_backup_enabled: true
      recovery_window_in_days: 56
      auto_backup_window: SLOT_ONE
      auto_full_backup_window: SLOT_ONE
      auto_full_backup_day: SUNDAY
      run_immediate_full_backup: true
      backup_destination_details:
      - # required
        type: NFS

        # optional
        id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        vpc_user: vpc_user_example
        vpc_password: example-password
        internet_proxy: internet_proxy_example
        dbrs_policy_id: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
      backup_deletion_policy: DELETE_IMMEDIATELY
    db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"
    new_admin_password: example-password
    old_tde_wallet_password: example-password
    new_tde_wallet_password: example-password
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete database
  oci_database_database:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

    # optional
    perform_final_backup: true

"""

RETURN = """
database:
    description:
        - Details of the Database resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        character_set:
            description:
                - The character set for the database.
            returned: on success
            type: str
            sample: character_set_example
        ncharacter_set:
            description:
                - The national character set for the database.
            returned: on success
            type: str
            sample: ncharacter_set_example
        db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
            returned: on success
            type: str
            sample: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster.
            returned: on success
            type: str
            sample: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
        db_name:
            description:
                - The database name.
            returned: on success
            type: str
            sample: db_name_example
        pdb_name:
            description:
                - The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of thirty alphanumeric
                  characters. Special characters are not permitted. Pluggable database should not be same as database name.
            returned: on success
            type: str
            sample: pdb_name_example
        db_workload:
            description:
                - "**Deprecated.** The dbWorkload field has been deprecated for Exadata Database Service on Dedicated Infrastructure, Exadata Database Service
                  on Cloud@Customer, and Base Database Service.
                  Support for this attribute will end in November 2023. You may choose to update your custom scripts to exclude the dbWorkload attribute. After
                  November 2023 if you pass a value to the dbWorkload attribute, it will be ignored."
                - The database workload type.
            returned: on success
            type: str
            sample: db_workload_example
        db_unique_name:
            description:
                - A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby
                  databases). The unique name cannot be changed.
            returned: on success
            type: str
            sample: db_unique_name_example
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the database.
            returned: on success
            type: str
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the database was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        last_backup_timestamp:
            description:
                - The date and time when the latest database backup was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        last_backup_duration_in_seconds:
            description:
                - The duration when the latest database backup created.
            returned: on success
            type: int
            sample: 56
        last_failed_backup_timestamp:
            description:
                - The date and time when the latest database backup failed.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        db_backup_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                auto_backup_enabled:
                    description:
                        - If set to true, configures automatic backups. If you previously used RMAN or dbcli to configure backups and then you switch to using
                          the Console or the API for backups, a new backup configuration is created and associated with your database. This means that you can
                          no longer rely on your previously configured unmanaged backups to work.
                    returned: on success
                    type: bool
                    sample: true
                recovery_window_in_days:
                    description:
                        - Number of days between the current and the earliest point of recoverability covered by automatic backups.
                          This value applies to automatic backups only. After a new automatic backup has been created, Oracle removes old automatic backups that
                          are created before the window.
                          When the value is updated, it is applied to all existing automatic backups.
                    returned: on success
                    type: int
                    sample: 56
                auto_backup_window:
                    description:
                        - Time window selected for initiating automatic backup for the database system. There are twelve available two-hour time windows. If no
                          option is selected, a start time between 12:00 AM to 7:00 AM in the region of the database is automatically chosen. For example, if
                          the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM (inclusive) to 4:00 AM
                          (exclusive).
                        - "Example: `SLOT_TWO`"
                    returned: on success
                    type: str
                    sample: SLOT_ONE
                auto_full_backup_window:
                    description:
                        - Time window selected for initiating full backup for the database system. There are twelve available two-hour time windows. If no
                          option is selected, the value is null and a start time between 12:00 AM to 7:00 AM in the region of the database is automatically
                          chosen. For example, if the user selects SLOT_TWO from the enum list, the automatic backup job will start in between 2:00 AM
                          (inclusive) to 4:00 AM (exclusive).
                        - "Example: `SLOT_TWO`"
                    returned: on success
                    type: str
                    sample: SLOT_ONE
                auto_full_backup_day:
                    description:
                        - Day of the week the full backup should be applied on the database system. If no option is selected, the value is null and we will
                          default to Sunday.
                    returned: on success
                    type: str
                    sample: SUNDAY
                run_immediate_full_backup:
                    description:
                        - If set to true, configures automatic full backups in the local region (the region of the DB system) for the first backup run
                          immediately.
                    returned: on success
                    type: bool
                    sample: true
                backup_destination_details:
                    description:
                        - Backup destination details.
                    returned: on success
                    type: complex
                    contains:
                        type:
                            description:
                                - Type of the database backup destination.
                            returned: on success
                            type: str
                            sample: NFS
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the backup destination.
                            returned: on success
                            type: str
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        vpc_user:
                            description:
                                - For a RECOVERY_APPLIANCE backup destination, the Virtual Private Catalog (VPC) user that is used to access the Recovery
                                  Appliance.
                            returned: on success
                            type: str
                            sample: vpc_user_example
                        vpc_password:
                            description:
                                - For a RECOVERY_APPLIANCE backup destination, the password for the VPC user that is used to access the Recovery Appliance.
                            returned: on success
                            type: str
                            sample: example-password
                        internet_proxy:
                            description:
                                - Proxy URL to connect to object store.
                            returned: on success
                            type: str
                            sample: internet_proxy_example
                        dbrs_policy_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DBRS policy used for backup.
                            returned: on success
                            type: str
                            sample: "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
                backup_deletion_policy:
                    description:
                        - "This defines when the backups will be deleted. - IMMEDIATE option keep the backup for predefined time i.e 72 hours and then delete
                          permanently... - RETAIN will keep the backups as per the policy defined for database backups."
                    returned: on success
                    type: str
                    sample: DELETE_IMMEDIATELY
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
        connection_strings:
            description:
                - The Connection strings used to connect to the Oracle Database.
            returned: on success
            type: complex
            contains:
                cdb_default:
                    description:
                        - Host name based CDB Connection String.
                    returned: on success
                    type: str
                    sample: cdb_default_example
                cdb_ip_default:
                    description:
                        - IP based CDB Connection String.
                    returned: on success
                    type: str
                    sample: cdb_ip_default_example
                all_connection_strings:
                    description:
                        - All connection strings to use to connect to the Database.
                    returned: on success
                    type: dict
                    sample: {}
        kms_key_id:
            description:
                - The OCID of the key container that is used as the master encryption key in database transparent data encryption (TDE) operations.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        kms_key_version_id:
            description:
                - The OCID of the key container version that is used in database transparent data encryption (TDE) operations KMS Key can have multiple key
                  versions. If none is specified, the current key version (latest) of the Key Id is used for the operation.
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
        source_database_point_in_time_recovery_timestamp:
            description:
                - Point in time recovery timeStamp of the source database at which cloned database system is cloned from the source database system, as
                  described in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339)
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        database_software_image_id:
            description:
                - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            returned: on success
            type: str
            sample: "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        is_cdb:
            description:
                - True if the database is a container database.
            returned: on success
            type: bool
            sample: true
        database_management_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                management_status:
                    description:
                        - The status of the Database Management service.
                    returned: on success
                    type: str
                    sample: ENABLING
                management_type:
                    description:
                        - The Database Management type.
                    returned: on success
                    type: str
                    sample: BASIC
        sid_prefix:
            description:
                - Specifies a prefix for the `Oracle SID` of the database to be created.
            returned: on success
            type: str
            sample: sid_prefix_example
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "character_set": "character_set_example",
        "ncharacter_set": "ncharacter_set_example",
        "db_home_id": "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "vm_cluster_id": "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "db_name": "db_name_example",
        "pdb_name": "pdb_name_example",
        "db_workload": "db_workload_example",
        "db_unique_name": "db_unique_name_example",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "last_backup_timestamp": "2013-10-20T19:20:30+01:00",
        "last_backup_duration_in_seconds": 56,
        "last_failed_backup_timestamp": "2013-10-20T19:20:30+01:00",
        "db_backup_config": {
            "auto_backup_enabled": true,
            "recovery_window_in_days": 56,
            "auto_backup_window": "SLOT_ONE",
            "auto_full_backup_window": "SLOT_ONE",
            "auto_full_backup_day": "SUNDAY",
            "run_immediate_full_backup": true,
            "backup_destination_details": [{
                "type": "NFS",
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "vpc_user": "vpc_user_example",
                "vpc_password": "example-password",
                "internet_proxy": "internet_proxy_example",
                "dbrs_policy_id": "ocid1.dbrspolicy.oc1..xxxxxxEXAMPLExxxxxx"
            }],
            "backup_deletion_policy": "DELETE_IMMEDIATELY"
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "connection_strings": {
            "cdb_default": "cdb_default_example",
            "cdb_ip_default": "cdb_ip_default_example",
            "all_connection_strings": {}
        },
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "kms_key_version_id": "ocid1.kmskeyversion.oc1..xxxxxxEXAMPLExxxxxx",
        "vault_id": "ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx",
        "source_database_point_in_time_recovery_timestamp": "2013-10-20T19:20:30+01:00",
        "database_software_image_id": "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx",
        "is_cdb": true,
        "database_management_config": {
            "management_status": "ENABLING",
            "management_type": "BASIC"
        },
        "sid_prefix": "sid_prefix_example",
        "key_store_id": "ocid1.keystore.oc1..xxxxxxEXAMPLExxxxxx",
        "key_store_wallet_name": "key_store_wallet_name_example"
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
    from oci.database.models import CreateDatabaseBase
    from oci.database.models import UpdateDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(DatabaseHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(DatabaseHelperGen, self).get_possible_entity_types() + [
            "database",
            "databases",
            "databasedatabase",
            "databasedatabases",
            "databaseresource",
            "databasesresource",
        ]

    def get_module_resource_id_param(self):
        return "database_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_id")

    def get_get_fn(self):
        return self.client.get_database

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_database, database_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database, database_id=self.module.params.get("database_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["db_home_id"]

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
        return oci_common_utils.list_all_resources(self.client.list_databases, **kwargs)

    def get_create_model_class(self):
        return CreateDatabaseBase

    def get_exclude_attributes(self):
        return ["db_version", "database", "source"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_database,
            call_fn_args=(),
            call_fn_kwargs=dict(create_new_database_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDatabaseDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                update_database_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                perform_final_backup=self.module.params.get("perform_final_backup"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseHelperCustom = get_custom_class("DatabaseHelperCustom")


class ResourceHelper(DatabaseHelperCustom, DatabaseHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            db_version=dict(type="str"),
            source=dict(type="str", default="NONE", choices=["NONE", "DB_BACKUP"]),
            kms_key_id=dict(type="str"),
            kms_key_version_id=dict(type="str"),
            database=dict(
                type="dict",
                options=dict(
                    database_software_image_id=dict(type="str"),
                    pdb_name=dict(type="str"),
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
                            auto_full_backup_window=dict(
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
                            auto_full_backup_day=dict(
                                type="str",
                                choices=[
                                    "SUNDAY",
                                    "MONDAY",
                                    "TUESDAY",
                                    "WEDNESDAY",
                                    "THURSDAY",
                                    "FRIDAY",
                                    "SATURDAY",
                                ],
                            ),
                            run_immediate_full_backup=dict(type="bool"),
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
                                            "DBRS",
                                        ],
                                    ),
                                    id=dict(type="str"),
                                    vpc_user=dict(type="str"),
                                    vpc_password=dict(type="str", no_log=True),
                                    internet_proxy=dict(type="str"),
                                    dbrs_policy_id=dict(type="str"),
                                ),
                            ),
                            backup_deletion_policy=dict(
                                type="str",
                                choices=[
                                    "DELETE_IMMEDIATELY",
                                    "DELETE_AFTER_RETENTION_PERIOD",
                                ],
                            ),
                        ),
                    ),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                    kms_key_id=dict(type="str"),
                    kms_key_version_id=dict(type="str"),
                    vault_id=dict(type="str"),
                    backup_id=dict(type="str"),
                    backup_tde_password=dict(type="str", no_log=True),
                    admin_password=dict(type="str", required=True, no_log=True),
                    db_unique_name=dict(type="str"),
                    db_name=dict(type="str"),
                    sid_prefix=dict(type="str"),
                ),
            ),
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
                    auto_full_backup_window=dict(
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
                    auto_full_backup_day=dict(
                        type="str",
                        choices=[
                            "SUNDAY",
                            "MONDAY",
                            "TUESDAY",
                            "WEDNESDAY",
                            "THURSDAY",
                            "FRIDAY",
                            "SATURDAY",
                        ],
                    ),
                    run_immediate_full_backup=dict(type="bool"),
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
                                    "DBRS",
                                ],
                            ),
                            id=dict(type="str"),
                            vpc_user=dict(type="str"),
                            vpc_password=dict(type="str", no_log=True),
                            internet_proxy=dict(type="str"),
                            dbrs_policy_id=dict(type="str"),
                        ),
                    ),
                    backup_deletion_policy=dict(
                        type="str",
                        choices=["DELETE_IMMEDIATELY", "DELETE_AFTER_RETENTION_PERIOD"],
                    ),
                ),
            ),
            db_home_id=dict(type="str"),
            new_admin_password=dict(type="str", no_log=True),
            old_tde_wallet_password=dict(type="str", no_log=True),
            new_tde_wallet_password=dict(type="str", no_log=True),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            database_id=dict(aliases=["id"], type="str"),
            perform_final_backup=dict(type="bool"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
