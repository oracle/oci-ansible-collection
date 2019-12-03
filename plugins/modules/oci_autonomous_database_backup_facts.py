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
module: oci_autonomous_database_backup_facts
short_description: Fetches details of one or more Autonomous Database Backups
description:
    - Fetches details of one or more Autonomous Database Backups.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment from which the details of the Autonomous Database Backups should be
                     fetched
        required: false
    autonomous_database_backup_id:
        description: Identifier of the Autonomous Database Backup whose details needs to be fetched.
        required: false
        aliases: ['id']
    autonomous_database_id:
        description: Identifier of the Autonomous Database whose Backup details needs to be fetched.
        required: false
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""
EXAMPLES = """
#Fetch Autonomous Database Backup for a Compartment
- name: List all Autonomous Database Backups in a Compartment
  oci_autonomous_database_backup_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'

#Fetch Autonomous Database Backup for a Compartment Filtered by Display Name
- name: List all Autonomous Database Backups in a Compartment
  oci_autonomous_database_backup_facts:
      compartment_id: 'ocid1.compartment..xxxxxEXAMPLExxxxx'
      display_name: 'ansibleautodbbackup'

#Fetch Autonomous Database Backups for an Autonomous Database
- name: List all Database Backups of an Autonomous Database filtered by Display Name
  oci_autonomous_database_facts:
      autonomous_database_id: 'ocid1.autonomousdatabase..xxxxxEXAMPLExxxxx'

#Fetch Autonomous Database Backups for an Autonomous Database filtered by Display Name
- name: List all Database Backups of an Autonomous Database filtered by Display Name
  oci_autonomous_database_facts:
      autonomous_database_id: 'ocid1.autonomousdatabase..xxxxxEXAMPLExxxxx'
      display_name: 'ansibleautodbbackup'

#Fetch a specific Autonomous Database Backup
- name: List a specific Autonomous Database Backup
  oci_database_facts:
      autonomous_database_backup_id: 'ocid1.autonomousdatabasebackup..xxxxxEXAMPLExxxxx'
"""

RETURN = """
    autonomous_database_backups:
        description: Attributes of the Fetched Autonomous Database Backup.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the
                             Autonomous Database, whose backup has to be created.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xxxxxEXAMPLExxxxx
            autonomous_database_id:
                description: The identifier of the Autonomous Database whose backup
                             has to be created.
                returned: always
                type: string
                sample: ocid1.autonomousdatabase.oc1.iad.xxxxxEXAMPLExxxxx
            display_name:
                description: The user-friendly name for the Autonomous Database Backup.
                returned: always
                type: string
                sample: manual-backup
            id:
                description: Identifier of the Autonomous Database Backup.
                returned: always
                type: string
                sample: ocid1.autonomousdatabasebackup.oc1.iad.xxxxxEXAMPLExxxxx
            is_automatic:
                description: Indicates whether the backup is user-initiated or automatic.
                returned: always
                type: string
                sample: False
            time_ended:
                description: The date and time the Autonomous Database Backup was completed.
                returned: always
                type: string
                sample: 2018-02-23T13:50:57.211000+00:00
            time_started:
                description: The date and time the Autonomous Database Backup starts.
                returned: always
                type: string
                sample: 2018-02-23T06:37:58.669000+00:00
            type:
                description: The type of Autonomous Database Backup.
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
                  "autonomous_database_id":"ocid1.autonomousdatabase.oc1.iad.xxxxxEXAMPLExxxxx",
                  "compartment_id":"ocid1.compartment.oc1.xxxxxEXAMPLExxxxx",
                  "display_name":"autonomous_db_backup_test",
                  "id":"ocid1.autonomousdatabasebackup.oc1.iad.xxxxxEXAMPLExxxxx",
                  "is_automatic":false,
                  "lifecycle_details": null,
                  "time_ended":"2018-09-20T09:12:45.502000+00:00",
                  "time_started":"2018-09-20T09:07:34.482000+00:00",
                  "type":"FULL"
               },
               {
                  "autonomous_database_id":"ocid1.autonomousdatabase.oc1.iad.xxxxxEXAMPLExxxxx",
                  "compartment_id":"ocid1.compartment.oc1.xxxxxEXAMPLExxxxx",
                  "display_name":"autonomous_db_backup_prod",
                  "id":"ocid1.autonomousdatabasebackup.oc1.iad.xxxxxEXAMPLExxxxx",
                  "is_automatic":false,
                  "lifecycle_details": null,
                  "time_ended":"2018-09-20T09:15:45.502000+00:00",
                  "time_started":"2018-09-20T09:08:00.482000+00:00",
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


def list_autonomous_database_backups(db_client, module):
    result = dict(autonomous_database_backups="")

    compartment_id = module.params.get("compartment_id")
    autonomous_database_backup_id = module.params.get("autonomous_database_backup_id")
    autonomous_database_id = module.params.get("autonomous_database_id")
    try:
        if compartment_id:
            get_logger().debug(
                "Listing all Autonomous Database Backups under compartment %s",
                compartment_id,
            )
            autonomous_database_backups = oci_utils.list_all_resources(
                db_client.list_autonomous_database_backups,
                compartment_id=compartment_id,
                display_name=module.params.get("display_name"),
            )
        elif autonomous_database_id:
            get_logger().debug(
                "Listing all Autonomous Database Backups for Autonomous Database Id %s",
                compartment_id,
            )
            autonomous_database_backups = oci_utils.list_all_resources(
                db_client.list_autonomous_database_backups,
                autonomous_database_id=autonomous_database_id,
                display_name=module.params.get("display_name"),
            )
        elif autonomous_database_backup_id:
            get_logger().debug(
                "Listing Autonomous Database Backup %s", autonomous_database_backup_id
            )
            response = oci_utils.call_with_backoff(
                db_client.get_autonomous_database_backup,
                autonomous_database_backup_id=autonomous_database_backup_id,
            )
            autonomous_database_backups = [response.data]
    except ServiceError as ex:
        get_logger().error(
            "Unable to list Autonomous Database Backups due to %s", ex.message
        )
        module.fail_json(msg=ex.message)
    result["autonomous_database_backups"] = to_dict(autonomous_database_backups)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_autonomous_database_backup_facts")
    set_logger(logger)

    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            autonomous_database_id=dict(type="str", required=False),
            autonomous_database_backup_id=dict(
                type="str", required=False, aliases=["id"]
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["compartment_id", "autonomous_database_backup_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_autonomous_database_backups(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
