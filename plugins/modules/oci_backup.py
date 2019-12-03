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
module: oci_backup
short_description: Create and Delete a Database Backup in OCI Database Cloud Service.
description:
    - Create and Delete a Database Backup in OCI Database Cloud Service.
    - Since all the operations of this module takes a long time, it is recommended to set the C(wait) parameter to
      False. Use M(oci_backup_facts) to check the status of the operation as a separate task.
version_added: "2.5"
options:
    database_id:
        description: Identifier of the  Database whose backup has to be created.
                     Mandatory for create.
        required: false
        aliases: ['id']
    display_name:
        description: The user-friendly name for the Database Backup. It does not have to be unique.
                     Mandatory for create.
        required: false
    backup_id:
        description: Identifier of the  Database Backup. Mandatory for delete.
        required: false
    state:
        description: Decides whether to create or delete Database Backup. For I(state=present),
                     if the backup does not exists, it gets created.For I(state=absent),
                     backup gets deleted.
        required: true
        choices: ['present', 'absent']
        default: 'present'
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Database Backup
- name: Create Database Backup
  oci_backup:
      database_id: 'ocid1.database.aaaa'
      display_name: 'ansible-backup'
      wait: False
      state: 'present'
# Delete Database Backup
- name: Delete Database Backup
  oci_backup:
      backup_id: 'ocid1.backup.aaaa'
      state: 'absent'
"""

RETURN = """
    backup:
        description: Attributes of the Database Backup.
        returned: success
        type: complex
        contains:
            availability_domain:
                description: The name of the Availability Domain that the Database Backup is located in.
                returned: always
                type: string
                sample: IwGV:US-ABC-AD-1
            compartment_id:
                description: The identifier of the compartment containing the
                             DB System where the Database resides, whose backup
                             has to be created.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            database_id:
                description: The identifier of the Database whose backup
                             has to be created.
                returned: always
                type: string
                sample: ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx
            display_name:
                description: The user-friendly name for the Database Backup.
                returned: always
                type: string
                sample: ansible-backup
            id:
                description: Identifier of the Database Backup.
                returned: always
                type: string
                sample: ocid1.backup.oc1.iad.xxxxxEXAMPLExxxxx
            time_ended:
                description: The date and time the Database Backup was completed.
                returned: always
                type: string
                sample: 2018-02-23T13:50:57.211000+00:00
            time_started:
                description: The date and time the Database Backup starts.
                returned: always
                type: string
                sample: 2018-02-23T06:37:58.669000+00:00
            type:
                description: The type of Database Backup.
                returned: always
                type: string
                sample: FULL
            lifecycle_state:
                description: The current state of the Database Backup.
                returned: always
                type: string
                sample: ACTIVE
            lifecycle_details:
                description: Additional information about the current lifecycle_state
                             of the Database Backup.
                returned: always
                type: string
                sample: The backup operation cannot run successfully because the node
                        is STOPPING or STOPPED
        sample: {
                    "availability_domain":"IwGV:US-ABC-AD-1",
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "database_id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"ansible-backup",
                    "id":"ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_details":"The backup operation  run successfully.",
                    "lifecycle_state":"AVAILABLE",
                    "time_ended":"2018-02-23T13:50:57.211000+00:00",
                    "time_started":"2018-02-23T06:37:58.669000+00:00",
                    "type":"FULL"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.database.models import CreateBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None


def create_backup(db_client, module):
    result = dict(changed=False, backup="")
    create_backup_details = CreateBackupDetails()
    for attribute in create_backup_details.attribute_map:
        create_backup_details.__setattr__(attribute, module.params.get(attribute))
    result = oci_utils.create_and_wait(
        resource_type="backup",
        create_fn=db_client.create_backup,
        kwargs_create={"create_backup_details": create_backup_details},
        client=db_client,
        get_fn=db_client.get_backup,
        get_param="backup_id",
        module=module,
    )

    return result


def delete_backup(db_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="backup",
        client=db_client,
        get_fn=db_client.get_backup,
        kwargs_get={"backup_id": module.params["backup_id"]},
        delete_fn=db_client.delete_backup,
        kwargs_delete={"backup_id": module.params["backup_id"]},
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_backup")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            backup_id=dict(type="str", required=False, aliases=["id"]),
            database_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False),
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
    state = module.params["state"]
    if state == "present":
        result = oci_utils.check_and_create_resource(
            resource_type="backup",
            create_fn=create_backup,
            kwargs_create={"db_client": db_client, "module": module},
            list_fn=db_client.list_backups,
            kwargs_list={"database_id": module.params.get("database_id")},
            module=module,
            model=CreateBackupDetails(),
        )
    elif state == "absent":
        result = delete_backup(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
