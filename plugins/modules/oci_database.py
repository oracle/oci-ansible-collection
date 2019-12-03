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
module: oci_database
short_description: Restore or Update a Database in OCI Database Cloud Service.
description:
    - Restore a Database. Note that this operation is not idempotent and any existing data in the database would be
      overwritten by this operation.
    - Update a Database.
    - Since all operations of this module takes a long time, it is recommended to set the C(wait) to False. Use
      M(oci_database_facts) to check the status of the operation as a separate task.
version_added: "2.5"
options:
    database_id:
        description: Identifier of the  Database that is required to be restored or updated.
        required: true
        aliases: ['id']
    database_scn:
        description: System Change Number of the backup which should be used to
                     restore the Database.
        required: false
    latest:
        description: If I(latest=True), the Database is restored to the last known good state
                     with the least possible data loss.
        required: false
    timestamp:
        description: The timestamp to which Database gets restored.
        required: false
    db_backup_config:
        description: Determines whether to configure automatic backups for the Database.
        suboptions:
            auto_backup_enabled:
                description: Configures automatic backup if I(auto_backup_enabled=True)
                required: false
        required: false
    state:
        description: Desired action to be performed on Database
        required: true
        default: 'update'
        choices: ['restore', 'update']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Update Database Backup Configuration
- name: Enable automatic Database Backups for a Database
  oci_database:
      database_id: 'ocid1.database.aaaa'
      db_backup_config:
          auto_backup_enabled: True
      state: 'update'
#Restore Database from latest backup
- name: Restore Database from latest backup
  oci_database:
      database_id: 'ocid1.database.aaaa'
      latest: True
      wait: False
      state: 'restore'
"""

RETURN = """
    database:
        description: Attributes of the Database.
        returned: success
        type: complex
        contains:
            character_set:
                description: The character set for the database.
                returned: always
                type: string
                sample: AL32UTF8
            compartment_id:
                description: The identifier of the compartment containing the
                             DB System where the Database resides.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            db_backup_config:
                description: Determines whether to configure automatic backup
                             of the Database.
                returned: always
                type: string
                sample: db_backup_config:{
                            auto_backup_enabled:false
                        }
            db_home_id:
                description: The identifier of the DB Home containing the
                             Database.
                returned: always
                type: string
                sample: ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx
            db_name:
                description: The database name.
                returned: always
                type: string
                sample: ansibledb
            db_unique_name:
                description: A system-generated name for the database to
                             ensure uniqueness within an Oracle Data Guard group
                             (a primary database and its standby databases). The
                             unique name cannot be changed.
                returned: always
                type: string
                sample: ansibledb_iad7b
            db_workload:
                description: Database workload type.
                returned: always
                type: string
                sample: OLTP
            id:
                description: Identifier of the Database.
                returned: always
                type: string
                sample: ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx
            time_created:
                description: Date and time when the DB Node was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            software_storage_size_in_gb:
                description: Storage size, in GBs, of the software volume that
                             is allocated to the DB system. This is applicable
                             only for VM-based DBs.
                returned: always
                type: string
                sample: 1024
            ncharacter_set:
                description: The national character set for the database.
                returned: always
                type: string
                sample: AL16UTF16
            pdb_name:
                description: Pluggable database name. It must begin with an
                             alphabetic character and can contain a maximum
                             of eight alphanumeric characters. Special characters
                             are not permitted. Pluggable database should not be
                             same as database name.
                returned: always
                type: string
                sample: ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the Database.
                returned: always
                type: string
                sample: AVAILABLE
            lifecycle_details:
                description: Additional information about the current lifecycle_state
                             of the Database.
                returned: always
                type: string
                sample: AVAILABLE
        sample: {
                   "character_set":"AL32UTF8",
                   "compartment_id":"ocid1.compartment.aaaa",
                   "freeform_tags":{"deployment":"test"},
                   "defined_tags":{"target_users":{"division":"design"}},
                   "db_backup_config":{
                            "auto_backup_enabled":false
                    },
                   "db_home_id":"ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx",
                   "db_name":"ansibledb",
                   "db_unique_name":"ansibledb_iad2cj",
                   "db_workload":"OLTP",
                   "id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_details":null,
                   "lifecycle_state":"BACKUP_IN_PROGRESS",
                   "ncharacter_set":"AL16UTF16",
                   "pdb_name":null,
                   "time_created":"2018-02-22T08:42:26.060000+00:00"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils, oci_db_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.database.models import (
        RestoreDatabaseDetails,
        UpdateDatabaseDetails,
        DbBackupConfig,
    )
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None


def restore_database(db_client, module):
    result = dict(changed=True, database="")
    database_id = module.params.get("database_id")
    restore_database_details = RestoreDatabaseDetails()
    for attribute in restore_database_details.attribute_map:
        restore_database_details.__setattr__(attribute, module.params.get(attribute))

    result = oci_db_utils.execute_function_and_wait(
        resource_type="database",
        function=db_client.restore_database,
        kwargs_function={
            "database_id": database_id,
            "restore_database_details": restore_database_details,
        },
        client=db_client,
        get_fn=db_client.get_database,
        get_param="database_id",
        module=module,
    )
    return result


def update_database(db_client, module):
    database_id = module.params.get("database_id")
    input_auto_backup_enabled = False
    existing_database = oci_utils.get_existing_resource(
        db_client.get_database, module, database_id=module.params.get("database_id")
    )
    if existing_database is None:
        module.fail_json(
            msg="No Database with id " + database_id + "is found for update."
        )
    result = dict(database=to_dict(existing_database), changed=False)
    update_database_details = UpdateDatabaseDetails()
    changed = False
    db_backup_config_changed = False
    attributes_to_compare = ["freeform_tags", "defined_tags"]
    for attribute in attributes_to_compare:
        changed = oci_utils.check_and_update_attributes(
            update_database_details,
            attribute,
            module.params.get(attribute),
            getattr(existing_database, attribute),
            changed,
        )
    input_db_backup_config = module.params.get("db_backup_config")
    if input_db_backup_config is not None:
        input_auto_backup_enabled = input_db_backup_config.get(
            "auto_backup_enabled", False
        )
    if (
        existing_database.db_backup_config.auto_backup_enabled
        != input_auto_backup_enabled
    ):
        db_backup_config = DbBackupConfig()
        db_backup_config.auto_backup_enabled = input_auto_backup_enabled
        update_database_details.db_backup_config = db_backup_config
        db_backup_config_changed = True
    if changed or db_backup_config_changed:
        db_backup_config = DbBackupConfig()
        db_backup_config.auto_backup_enabled = input_auto_backup_enabled
        update_database_details.db_backup_config = db_backup_config
        result = oci_utils.update_and_wait(
            resource_type="database",
            update_fn=db_client.update_database,
            kwargs_update={
                "database_id": database_id,
                "update_database_details": update_database_details,
            },
            client=db_client,
            get_fn=db_client.get_database,
            get_param="database_id",
            module=module,
        )
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_database")
    set_logger(logger)
    module_args = oci_utils.get_taggable_arg_spec(supports_wait=True)
    module_args.update(
        dict(
            database_id=dict(type="str", required=True, aliases=["id"]),
            database_scn=dict(type="str", required=False),
            latest=dict(type=bool, required=False),
            timestamp=dict(type="str", required=False),
            db_backup_config=dict(type=dict, required=False),
            state=dict(
                type="str",
                required=False,
                default="update",
                choices=["restore", "update"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    state = module.params["state"]
    if state == "restore":
        result = restore_database(db_client, module)
    elif state == "update":
        result = update_database(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
