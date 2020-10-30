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
module: oci_database_db_home
short_description: Manage a DbHome resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DbHome resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Database Home in the specified database system based on the request parameters you provide. Applies to bare metal DB
      systems, Exadata systems, and Exadata Cloud@Customer systems.
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - The user-provided name of the Database Home.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    database_software_image_id:
        description:
            - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
        type: str
    source:
        description:
            - "The source of database: NONE for creating a new database. DB_BACKUP for creating a new database by restoring from a database backup."
        type: str
        choices:
            - "DATABASE"
            - "DB_BACKUP"
            - "VM_CLUSTER_BACKUP"
            - "NONE"
            - "VM_CLUSTER_NEW"
        default: "NONE"
    db_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            - Required when source is one of ['DATABASE', 'NONE', 'DB_BACKUP']
        type: str
    database:
        description:
            - ""
            - Required when source is one of ['VM_CLUSTER_BACKUP', 'DATABASE', 'DB_BACKUP']
        type: dict
        suboptions:
            database_id:
                description:
                    - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    - Required when source is 'DATABASE'
                type: str
            backup_tde_password:
                description:
                    - The password to open the TDE wallet.
                    - Required when source is one of ['VM_CLUSTER_BACKUP', 'DATABASE', 'DB_BACKUP']
                type: str
            admin_password:
                description:
                    - "A strong password for SYS, SYSTEM, PDB Admin and TDE Wallet. The password must be at least nine characters and contain at least two
                      uppercase, two lowercase, two numbers, and two special characters. The special characters must be _, #, or -."
                type: str
                required: true
            db_unique_name:
                description:
                    - The `DB_UNIQUE_NAME` of the Oracle Database being backed up.
                type: str
            db_name:
                description:
                    - The display name of the database to be created from the backup. It must begin with an alphabetic character and can contain a maximum of
                      eight alphanumeric characters. Special characters are not permitted.
                    - Required when source is one of ['VM_CLUSTER_NEW', 'NONE']
                type: str
            time_stamp_for_point_in_time_recovery:
                description:
                    - The point in time of the original database from which the new database is created. If not specifed, the latest backup is used to create
                      the database.
                    - Applicable when source is 'DATABASE'
                type: str
            backup_id:
                description:
                    - The backup L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
                    - Required when source is one of ['VM_CLUSTER_BACKUP', 'DB_BACKUP']
                type: str
            database_software_image_id:
                description:
                    - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
                    - Applicable when source is one of ['VM_CLUSTER_NEW', 'NONE']
                type: str
            pdb_name:
                description:
                    - The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric
                      characters. Special characters are not permitted. Pluggable database should not be same as database name.
                    - Applicable when source is one of ['VM_CLUSTER_NEW', 'NONE']
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
                    - Applicable when source is one of ['VM_CLUSTER_NEW', 'NONE']
                type: str
            ncharacter_set:
                description:
                    - "The national character set for the database.  The default is AL16UTF16. Allowed values are:
                      AL16UTF16 or UTF8."
                    - Applicable when source is one of ['VM_CLUSTER_NEW', 'NONE']
                type: str
            db_workload:
                description:
                    - The database workload type.
                    - Applicable when source is one of ['VM_CLUSTER_NEW', 'NONE']
                type: str
                choices:
                    - "OLTP"
                    - "DSS"
            db_backup_config:
                description:
                    - ""
                    - Applicable when source is one of ['VM_CLUSTER_NEW', 'NONE']
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
                    backup_destination_details:
                        description:
                            - Backup destination details.
                            - Applicable when source is 'NONE'
                        type: list
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
            freeform_tags:
                description:
                    - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                    - "Example: `{\\"Department\\": \\"Finance\\"}`"
                    - Applicable when source is one of ['VM_CLUSTER_NEW', 'NONE']
                type: dict
            defined_tags:
                description:
                    - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                    - Applicable when source is one of ['VM_CLUSTER_NEW', 'NONE']
                type: dict
    vm_cluster_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster.
            - Required when source is one of ['VM_CLUSTER_BACKUP', 'VM_CLUSTER_NEW']
        type: str
    db_version:
        description:
            - A valid Oracle Database version. To get a list of supported versions, use the L(ListDbVersions,https://docs.cloud.oracle.com/en-
              us/iaas/api/#/en/database/20160918/DbVersionSummary/ListDbVersions) operation.
            - Required when source is one of ['VM_CLUSTER_NEW', 'NONE']
        type: str
    db_home_id:
        description:
            - The Database Home L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    patch_details:
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
    one_off_patches:
        description:
            - List of one-off patches for Database Homes.
            - This parameter is updatable.
        type: list
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
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the DbHome.
            - Use I(state=present) to create or update a DbHome.
            - Use I(state=absent) to delete a DbHome.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create db_home
  oci_database_db_home:
    db_system_id: ocid1.dbsystem.oc1.phx.unique_ID
    display_name: createdDbHome
    source: NONE
    db_version: 12.1.0.2
    database:
      admin_password: password
      db_name: myTestDb
      db_unique_name: myTestDb_phx1cs
      db_backup_config:
        recovery_window_in_days: 30
        auto_backup_enabled: true

- name: Update db_home using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_db_home:
    display_name: createdDbHome
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update db_home
  oci_database_db_home:
    db_home_id: ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete db_home
  oci_database_db_home:
    db_home_id: ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete db_home using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_database_db_home:
    display_name: createdDbHome
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

"""

RETURN = """
db_home:
    description:
        - Details of the DbHome resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - The user-provided name for the Database Home. The name does not need to be unique.
            returned: on success
            type: string
            sample: display_name_example
        last_patch_history_entry_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the last patch history. This value is updated as soon as
                  a patch operation is started.
            returned: on success
            type: string
            sample: ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx
        lifecycle_state:
            description:
                - The current state of the Database Home.
            returned: on success
            type: string
            sample: PROVISIONING
        db_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the DB system.
            returned: on success
            type: string
            sample: ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx
        vm_cluster_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the VM cluster.
            returned: on success
            type: string
            sample: ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx
        db_version:
            description:
                - The Oracle Database version.
            returned: on success
            type: string
            sample: db_version_example
        db_home_location:
            description:
                - The location of the Oracle Database Home.
            returned: on success
            type: string
            sample: db_home_location_example
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the Database Home was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        one_off_patches:
            description:
                - List of one-off patches for Database Homes.
            returned: on success
            type: list
            sample: []
        database_software_image_id:
            description:
                - The database software image L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)
            returned: on success
            type: string
            sample: ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "last_patch_history_entry_id": "ocid1.lastpatchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "PROVISIONING",
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "vm_cluster_id": "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx",
        "db_version": "db_version_example",
        "db_home_location": "db_home_location_example",
        "lifecycle_details": "lifecycle_details_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "one_off_patches": [],
        "database_software_image_id": "ocid1.databasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.database.models import CreateDbHomeBase
    from oci.database.models import UpdateDbHomeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DbHomeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def __init__(self, *args, **kwargs):
        super(DbHomeHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_module_resource_id_param(self):
        return "db_home_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_home_id")

    def get_get_fn(self):
        return self.client.get_db_home

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_home, db_home_id=self.module.params.get("db_home_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["db_system_id", "vm_cluster_id", "display_name"]

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
        return oci_common_utils.list_all_resources(self.client.list_db_homes, **kwargs)

    def get_create_model_class(self):
        return CreateDbHomeBase

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_db_home,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_db_home_with_db_system_id_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDbHomeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_db_home,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_home_id=self.module.params.get("db_home_id"),
                update_db_home_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_db_home,
            call_fn_args=(),
            call_fn_kwargs=dict(
                db_home_id=self.module.params.get("db_home_id"),
                perform_final_backup=self.module.params.get("perform_final_backup"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DbHomeHelperCustom = get_custom_class("DbHomeHelperCustom")


class ResourceHelper(DbHomeHelperCustom, DbHomeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            database_software_image_id=dict(type="str"),
            source=dict(
                type="str",
                default="NONE",
                choices=[
                    "DATABASE",
                    "DB_BACKUP",
                    "VM_CLUSTER_BACKUP",
                    "NONE",
                    "VM_CLUSTER_NEW",
                ],
            ),
            db_system_id=dict(type="str"),
            database=dict(
                type="dict",
                options=dict(
                    database_id=dict(type="str"),
                    backup_tde_password=dict(type="str", no_log=True),
                    admin_password=dict(type="str", required=True, no_log=True),
                    db_unique_name=dict(type="str"),
                    db_name=dict(type="str"),
                    time_stamp_for_point_in_time_recovery=dict(type="str"),
                    backup_id=dict(type="str"),
                    database_software_image_id=dict(type="str"),
                    pdb_name=dict(type="str"),
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
                ),
            ),
            vm_cluster_id=dict(type="str"),
            db_version=dict(type="str"),
            db_home_id=dict(aliases=["id"], type="str"),
            patch_details=dict(
                type="dict",
                options=dict(
                    patch_id=dict(type="str"),
                    database_software_image_id=dict(type="str"),
                    action=dict(type="str", choices=["APPLY", "PRECHECK"]),
                ),
            ),
            one_off_patches=dict(type="list"),
            perform_final_backup=dict(type="bool"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="db_home",
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
