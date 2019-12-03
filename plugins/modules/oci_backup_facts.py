#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_backup_facts
short_description: Fetches details of one or more Database Backups
description:
    - Fetches details of the Database Backups.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which the
                     details of the Database Backups should be fetched
        required: false
    database_id:
        description: Identifier of the Database whose Backups should be fetched.
        required: false
        aliases: ['id']
    backup_id:
        description: Identifier of the Database Backup whose details needs to be fetched.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""
EXAMPLES = """
#Fetch Database Backup for a Compartment
- name: List all Database Backups in a Compartment
  oci_backup_facts:
      compartment_id: 'ocid1.compartment..xcds'
#Fetch Database Backup for a Database
- name: List all Database Backups of a Database
  oci_database_facts:
      database_id: 'ocid1.database..xcds'
#Fetch a specific Database Backup
- name: List a specific Database Backup
  oci_database_facts:
      backup_id: 'ocid1.backup..xcds'
"""

RETURN = """
    backups:
        description: Attributes of the Fetched Database Backup.
        returned: success
        type: complex
        contains:
            availability_domain:
                description: The name of the Availability Domain that the backup is located in.
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
        sample: [{
                    "availability_domain":"IwGV:US-ABC-AD-1",
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "database_id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"ansible-backup-one",
                    "id":"ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_details":"The backup operation  run successfully.",
                    "lifecycle_state":"AVAILABLE",
                    "time_ended":"2018-02-23T13:50:57.211000+00:00",
                    "time_started":"2018-02-23T06:37:58.669000+00:00",
                    "type":"FULL"
                },
                {
                    "availability_domain":"IwGV:US-ABC-AD-1",
                    "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                    "database_id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                    "display_name":"ansible-backup-two",
                    "id":"ocid1.dbbackup.oc1.iad.xxxxxEXAMPLExxxxx",
                    "lifecycle_details":"The backup operation  run successfully.",
                    "lifecycle_state":"AVAILABLE",
                    "time_ended":"2018-02-24T13:50:57.211000+00:00",
                    "time_started":"2018-02-24T06:37:58.669000+00:00",
                    "type":"FULL"
                }]
"""
from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_backups(db_client, module):
    result = dict(backups="")
    compartment_id = module.params.get("compartment_id")
    backup_id = module.params.get("backup_id")
    database_id = module.params.get("database_id")
    try:
        if backup_id:
            get_logger().debug("Listing Database Backup %s", backup_id)
            response = oci_utils.call_with_backoff(
                db_client.get_backup, backup_id=backup_id
            )
            existing_backups = [response.data]
        elif database_id:
            get_logger().debug(
                "Listing all Database Backups for Database %s", database_id
            )
            existing_backups = oci_utils.list_all_resources(
                db_client.list_backups,
                database_id=database_id,
                display_name=module.params.get("display_name"),
            )
        elif compartment_id:
            get_logger().debug(
                "Listing all Database Backups under compartment %s", compartment_id
            )
            existing_backups = oci_utils.list_all_resources(
                db_client.list_backups,
                compartment_id=compartment_id,
                display_name=module.params.get("display_name"),
            )
    except ServiceError as ex:
        get_logger().error("Unable to list Database Backups due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["backups"] = to_dict(existing_backups)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_backup_facts")
    set_logger(logger)
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            backup_id=dict(type="str", required=False, aliases=["id"]),
            database_id=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[
            ["compartment_id", "database_id"],
            ["compartment_id", "backup_id"],
            ["database_id", "backup_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)

    result = list_backups(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
