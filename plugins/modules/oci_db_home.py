#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_db_home
short_description: Create,update and delete a DB Home in OCI Database Cloud Service.
description:
    - Create an OCI DB Home
    - Update an OCI DB Home, if present
    - Delete an OCI DB Home, if present.
    - Since all operations of this module takes a long time, it is recommended to set the C(wait) to False. Use
      M(oci_db_home_facts) to check the status of the operation as a separate task.
version_added: "2.5"
options:
    db_system_id:
        description: Identifier of the  DB System under which the DB Home should exist.
                     Mandatory for create.
        required: false
    db_home_id:
        description: The identifier of the db home. Mandatory for update and delete.
        required: false
        aliases: ['id']
    source:
        description: Source of database. I(source=NONE) for creating a new database
                     I(source=DB_BACKUP) for creating a new database by restoring a
                     backup.
        required: false
        default: 'NONE'
        choices: ['NONE', 'DB_BACKUP']
    database:
        description: The details of the databse to be created under the db home. Mandatory
                     for create operation.
        suboptions:
            admin_password:
               description: A strong password for SYS, SYSTEM, and PDB Admin. The password
                            must be at least nine characters and contain at least two
                            uppercase,two lowercase, two numbers, and two special characters.
                            This parameter valid for I(source=NONE) and I(source=DB_BACKUP).
               required: true
            character_set:
               description: The character set for the database. The default
                            is AL32UTF8. This parameter only valid for I(source=NONE).
               required: false
            db_backup_config:
               description: Consists of the option 'auto_backup_enabled' to determine whether
                            to configures automatic backups of the databse. This parameter only
                            valid for I(source=NONE).
               required: false
            db_name:
               description: The name of the database name. It must begin with an alphabetic character
                            and can contain a maximum of eight alphanumeric characters. Special characters
                            are not permitted. This parameter only valid for I(source=NONE).
               required: true
            db_workload:
               description: Database workload type with allowed values OLTP and DSS. This parameter only
                            valid for I(source=NONE).
               required: false
            ncharacter_set:
               description: National character set for the database.The default is AL16UTF16.
                            Allowed values are AL16UTF16 or UTF8. This parameter only valid for
                            I(source=NONE).
               required: false
            pdb_name:
               description: pluggable database name.It must begin with an alphabetic character
                            and can contain a maximum of eight alphanumeric characters. Special
                            characters are not permitted. Pluggable database should not be same
                            as database name. This parameter only valid for I(source=NONE).
               required: false
            backup_id:
               description: The backup OCID. This parameter only valid for I(source=DB_BACKUP).
               required: true
            backup_tde_password:
               description: The password to open the TDE wallet. This parameter only valid for I(source=DB_BACKUP).
               required: true
        required: false
    display_name:
        description: The user-provided name of the database home.
        required: false
    db_version:
        description: A valid Oracle database version. Mandatory for create.
        required: false
    patch_details:
        description: The patch version and what actions to perform with that, on specified DB
                     Home. This is required only for the update use case.
        suboptions:
            action:
               description: The action to perform on the patch.
               required: true
               choices: ['APPLY', 'PRECHECK']
            patch_id:
               description: The OCID of the patch.
               required: true
        required: false
    state:
        description: Create,update or delete DB Home. For I(state=present), if it
                     does not exists, it gets created. If exists, it gets updated.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.

# Create DB Home from No Source
- name: Create DB Home From No Source
  oci_db_home:
    db_system_id: "ocid1.dbsystem.aaaa"
    display_name: "db50"
    source: "NONE"
    database:
      admin_password: 'BEstr0ng_#1'
      character_set: 'AL32UTF8'
      db_backup_config:
        auto_backup_enabled: False
      db_name: 'dbone{{random_suffix_1024}}'
      db_workload: 'OLTP'
      ncharacter_set: 'AL16UTF16'
    db_version: "12.2.0.1"
    wait: False
    state: 'present'

# Create DB Home from DB Backup
- name: Create DB Home From DB Backup
  oci_db_home:
    db_system_id: "ocid1.dbsystem.aaaa"
    display_name: "db50"
    source: "DB_BACKUP"
    database:
       backup_id: 'ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx'
       backup_tde_password: 'BEstr0ng_#1'
       admin_password: 'BEstr0ng_#1'
    state: 'present'

# Precheck a patch on DB Home
- name: Precheck a patch on DB Home
  oci_db_home:
    db_home_id: "ocid1.dbhome.aaaa"
    patch_details:
       patch_id: "ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx"
       action: 'PRECHECK'
    state: 'present'

# Apply a patch on DB Home
- name: Apply a patch on DB Home
  oci_db_home:
    db_home_id: "ocid1.dbhome.aaaa"
    patch_details:
       patch_id: "ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx"
       action: 'APPLY'
    state: 'present'

# Delete DB Home
- name: Delete DB Home
  oci_db_home:
    db_home_id: "ocid1.dbhome.aaaa"
    state: 'absent'
"""

RETURN = """
    db_home:
        description: Attributes of the created/updated DB Home.
                    For delete, deleted DB Home description will
                    be returned.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the DB Home
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            db_system_id:
                description: Identifier of the  DB System under which the DB Home should exists.
                returned: always
                type: string
                sample: ocid1.dbsystem.oc1.iad.xxxxxEXAMPLExxxxx
            db_version:
                description: Oracle database version.
                returned: always
                type: string
                sample: 12.2.0.1.1
            display_name:
                description: The user-friendly name for the DB Home.
                returned: always
                type: string
                sample: ansible-db-home
            id:
                description: Identifier of the DB Home.
                returned: always
                type: string
                sample: ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the DB System was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            last_patch_history_entry_id:
                description: The OCID of the last patch history. This is updated
                             as soon as a patch operation is started.
                returned: always
                type: string
                sample: ocid1.lastpatchhistory.aaaa
            lifecycle_state:
                description: The current state of the DB System.
                returned: always
                type: string
                sample: AVAILABLE
        sample: {
                   "compartment_id":"ocid1.compartment.aaaa",
                   "db_system_id":"ocid1.dbsystem.aaaa",
                   "db_version":"12.2.0.1.1",
                   "display_name":"ansible-db",
                   "id":"ocid1.dbhome.aaaa",
                   "last_patch_history_entry_id":"ocid1.dbpatchhistory.aaaa",
                   "lifecycle_state":"AVAILABLE",
                   "time_created":"2018-02-16T08:44:32.779000+00:00"
              }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle import oci_db_utils
import os

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError, ClientError
    from oci.util import to_dict
    from oci.database.models import (
        CreateDbHomeWithDbSystemIdDetails,
        CreateDbHomeWithDbSystemIdFromBackupDetails,
        UpdateDbHomeDetails,
        CreateDatabaseFromBackupDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_db_home(db_client, module):
    result = dict(changed=False, db_home="")
    db_home_id = module.params.get("db_home_id")
    try:
        if db_home_id:
            result = update_db_home(db_client, module, db_home_id)
        else:
            db_system = oci_utils.get_existing_resource(
                db_client.get_db_system,
                module,
                db_system_id=module.params.get("db_system_id"),
            )
            db_home_model = None
            source = module.params.get("source")
            if source == "NONE":
                db_home_model = CreateDbHomeWithDbSystemIdDetails()
            elif source == "DB_BACKUP":
                db_home_model = CreateDbHomeWithDbSystemIdFromBackupDetails()
            result = oci_utils.check_and_create_resource(
                resource_type="db_home",
                create_fn=create_db_home,
                kwargs_create={"db_client": db_client, "module": module},
                list_fn=db_client.list_db_homes,
                kwargs_list={
                    "compartment_id": db_system.compartment_id,
                    "db_system_id": module.params.get("db_system_id"),
                },
                module=module,
                model=db_home_model,
            )
    except ServiceError as ex:
        get_logger().error(
            "Unable to create/update database home due to: %s", ex.message
        )
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to launch/update database home due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_db_home(db_client, module):
    create_db_home_details = None
    source = module.params.get("source")
    if source == "NONE":
        create_db_home_details = CreateDbHomeWithDbSystemIdDetails()
        create_db_home_details.database = oci_db_utils.create_database_details(
            module.params.get("database", None)
        )
        create_db_home_details.source = source
    elif source == "DB_BACKUP":
        create_db_home_details = CreateDbHomeWithDbSystemIdFromBackupDetails()
        create_db_home_details.database = create_database_from_backup_details(
            module.params.get("database", None)
        )
        create_db_home_details.source = source

    for attribute in create_db_home_details.attribute_map.keys():
        if attribute not in ("database", "source"):
            create_db_home_details.__setattr__(attribute, module.params.get(attribute))
    result = oci_utils.create_and_wait(
        resource_type="db_home",
        create_fn=db_client.create_db_home,
        kwargs_create={
            "create_db_home_with_db_system_id_details": create_db_home_details
        },
        client=db_client,
        get_fn=db_client.get_db_home,
        get_param="db_home_id",
        module=module,
    )
    return result


def create_database_from_backup_details(database_dict):
    create_database_from_backup_details = CreateDatabaseFromBackupDetails()
    for attribute in create_database_from_backup_details.attribute_map.keys():
        create_database_from_backup_details.__setattr__(
            attribute, database_dict.get(attribute, None)
        )
    return create_database_from_backup_details


def update_db_home(db_client, module, db_home_id):
    result = dict()
    db_home = oci_utils.get_existing_resource(
        db_client.get_db_home, module, db_home_id=db_home_id
    )
    if db_home is None:
        raise ClientError(
            Exception("No DB Home with id " + db_home_id + " is found for update")
        )
    last_patch_history_entry_id = db_home.last_patch_history_entry_id
    input_version_dict = module.params.get("patch_details", None)
    update_db_home_details = UpdateDbHomeDetails()
    version_changed, patch_details = oci_db_utils.is_version_changed(
        db_client.get_db_home_patch_history_entry,
        db_client.get_db_home_patch,
        db_home.db_version,
        input_version_dict,
        last_patch_history_entry_id,
        db_home_id=db_home_id,
    )
    if version_changed:
        update_db_home_details.db_version = patch_details
        result = oci_utils.update_and_wait(
            resource_type="db_home",
            update_fn=db_client.update_db_home,
            kwargs_update={
                "db_home_id": db_home_id,
                "update_db_home_details": update_db_home_details,
            },
            client=db_client,
            get_fn=db_client.get_db_home,
            get_param="db_home_id",
            module=module,
        )
    else:
        result["db_home"] = to_dict(db_home)
        result["changed"] = False
    return result


def delete_db_home(db_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="db_home",
        client=db_client,
        get_fn=db_client.get_db_home,
        kwargs_get={"db_home_id": module.params["db_home_id"]},
        delete_fn=db_client.delete_db_home,
        kwargs_delete={"db_home_id": module.params["db_home_id"]},
        module=module,
    )
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_db_home")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            db_system_id=dict(type="str", required=False),
            db_home_id=dict(type="str", required=False, aliases=["id"]),
            display_name=dict(type="str", required=False),
            source=dict(
                type="str",
                required=False,
                choices=["DB_BACKUP", "NONE"],
                default="NONE",
            ),
            database=dict(type=dict, required=False),
            db_version=dict(type="str", required=False),
            patch_details=dict(type=dict, required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    if os.environ.get("OCI_DB_MOCK") is not None:
        db_client.base_client.session.headers.update(
            {"opc-host-serial": "FakeHostSerial"}
        )
    state = module.params["state"]

    if state == "present":
        result = create_or_update_db_home(db_client, module)
    elif state == "absent":
        result = delete_db_home(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
