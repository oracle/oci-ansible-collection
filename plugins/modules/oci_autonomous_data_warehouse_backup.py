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
module: oci_autonomous_data_warehouse_backup
short_description: Create a new Autonomous Data Warehouse Backup in OCI Database Cloud Service.
description:
    - Create a new Autonomous Data Warehouse Backup in OCI Database Cloud Service.
    - Since all the operations of this module takes a long time, it is recommended to set the C(wait) parameter to
      False. Use M(oci_autonomous_data_warehouse_backup_facts) to check the status of the operation as a separate task.
version_added: "2.5"
options:
    autonomous_data_warehouse_id:
        description: Identifier of the  Autonomous Data Warehouse whose backup has to be created. Mandatory for create.
        required: false
        aliases: ['id']
    display_name:
        description: The user-friendly name for the Autonomous Data Warehouse Backup. It does not have to be unique.
                     Mandatory for create.
        required: false
    state:
        description: Decides whether to create Autonomous Data Warehouse Backup. For I(state=present), if the backup
                     does not exists, it gets created.
        required: false
        choices: ['present']
        default: 'present'
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Autonomous Data Warehouse Backup
- name: Create Autonomous Data Warehouse Backup
  oci_autonomous_data_warehouse_backup:
      autonomous_data_warehouse_id: 'ocid1.autonomousdwdatabase.xxxxxEXAMPLExxxxx'
      display_name: 'ansible-data-warehouse-backup'
      wait: False
      state: 'present'
"""

RETURN = """
    autonomous_data_warehouse_backup:
        description: Attributes of the Autonomous Data Warehouse Backup.
        returned: success
        type: complex
        contains:
            compartment_id:
                description: The identifier of the compartment containing the
                             Autonomous Data Warehouse, whose backup has to be created.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xxxxxEXAMPLExxxxx
            autonomous_data_warehouse_id:
                description: The identifier of the Autonomous Data Warehouse whose backup
                             has to be created.
                returned: always
                type: string
                sample: ocid1.autonomousdwdatabase.oc1.iad.xxxxxEXAMPLExxxxx
            display_name:
                description: The user-friendly name for the Autonomous Data Warehouse Backup.
                returned: always
                type: string
                sample: manual-backup
            id:
                description: Identifier of the Autonomous Data Warehouse Backup.
                returned: always
                type: string
                sample: ocid1.autonomousdwbackup.oc1.iad.xxxxxEXAMPLExxxxx
            is_automatic:
                description: Indicates whether the backup is user-initiated or automatic.
                returned: always
                type: string
                sample: False
            time_ended:
                description: The date and time the Autonomous Data Warehouse Backup was completed.
                returned: always
                type: string
                sample: 2018-02-23T13:50:57.211000+00:00
            time_started:
                description: The date and time the Autonomous Data Warehouse Backup starts.
                returned: always
                type: string
                sample: 2018-02-23T06:37:58.669000+00:00
            type:
                description: The type of Autonomous Data Warehouse Backup.
                returned: always
                type: string
                sample: FULL
            lifecycle_state:
                description: The current state of the Data Warehouse Backup.
                returned: always
                type: string
                sample: ACTIVE
            lifecycle_details:
                description: Additional information about the current lifecycle_state
                             of the Data Warehouse Backup.
                returned: always
                type: string
                sample: The backup operation cannot run successfully because the node
                        is STOPPING or STOPPED
        sample: {
                  "autonomous_data_warehouse_id":"ocid1.autonomousdwdatabase.oc1.iad.xxxxxEXAMPLExxxxx",
                  "compartment_id":"ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                  "display_name":"autodbwarehousebackup",
                  "id":"ocid1.autonomousdwbackup.oc1.iad.xxxxxEXAMPLExxxxx",
                  "is_automatic":false,
                  "lifecycle_details": null,
                  "lifecycle_state":"AVAILABLE",
                  "time_ended":null,
                  "time_started":"2018-09-22T16:38:30.558000+00:00",
                  "type":"FULL"
                }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.database.database_client import DatabaseClient
    from oci.database.models import CreateAutonomousDataWarehouseBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = None


def create_autonomous_data_warehouse_backup(db_client, module):
    result = dict(changed=False, autonomous_data_warehouse_backup="")
    create_autonomous_data_warehouse_backup_details = (
        CreateAutonomousDataWarehouseBackupDetails()
    )
    for attribute in create_autonomous_data_warehouse_backup_details.attribute_map:
        create_autonomous_data_warehouse_backup_details.__setattr__(
            attribute, module.params.get(attribute)
        )

    result = oci_utils.create_and_wait(
        resource_type="autonomous_data_warehouse_backup",
        create_fn=db_client.create_autonomous_data_warehouse_backup,
        kwargs_create={
            "create_autonomous_data_warehouse_backup_details": create_autonomous_data_warehouse_backup_details
        },
        client=db_client,
        get_fn=db_client.get_autonomous_data_warehouse_backup,
        get_param="autonomous_data_warehouse_backup_id",
        module=module,
        states=["ACTIVE", "FAILED"],
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_autonomous_data_warehouse_backup")
    set_logger(logger)

    module_args = oci_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            autonomous_data_warehouse_id=dict(
                type="str", required=False, aliases=["id"]
            ),
            display_name=dict(type="str", required=False),
            state=dict(
                type="str", required=False, default="present", choices=["present"]
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
            resource_type="autonomous_data_warehouse_backup",
            create_fn=create_autonomous_data_warehouse_backup,
            kwargs_create={"db_client": db_client, "module": module},
            list_fn=db_client.list_autonomous_data_warehouse_backups,
            kwargs_list={
                "autonomous_data_warehouse_id": module.params.get(
                    "autonomous_data_warehouse_id"
                )
            },
            module=module,
            model=CreateAutonomousDataWarehouseBackupDetails(),
        )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
