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
module: oci_database_facts
short_description: Fetches details of one or more Databases
description:
    - Fetches details of one or more OCI Databases.
version_added: "2.5"
options:
    compartment_id:
        description: Identifier of the compartment in which the specified Database exists
        required: false
    db_home_id:
        description: Identifier of the DB Home under which the Database is available.
        required: false
    database_id:
        description: Identifier of the Database whose details needs to be fetched.
        required: false
        aliases: ['id']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: oracle
"""
EXAMPLES = """
#Fetch Databases
- name: Fetch all Databases under a DB Home
  oci_database_facts:
    compartment_id: 'ocid1.compartment.aaaa'
    db_home_id: "ocid1.dbhome.aaaa"
#Fetch a specific Database
- name: List a specific DB Node
  oci_database_facts:
      database_id: 'ocid1.database..xcds'
"""

RETURN = """
    databases:
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
                description: The identifier of the compartment containing the DB System where the Database resides.
                returned: always
                type: string
                sample: ocid1.compartment.oc1.xzvf..oifds
            db_backup_config:
                description: Determines whether to configure automatic backup of the Database.
                returned: always
                type: string
                sample: db_backup_config:{
                            auto_backup_enabled:false
                        }
            db_home_id:
                description: The identifier of the DB Home containing the Database.
                returned: always
                type: string
                sample: ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx
            db_name:
                description: The database name.
                returned: always
                type: string
                sample: ansibledb
            db_unique_name:
                description: A system-generated name for the database to ensure uniqueness within an Oracle Data Guard
                             group (a primary database and its standby databases). The unique name cannot be changed.
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
                description: Date and time when the DB Node was created, in the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2016-08-25T21:10:29.600Z
            software_storage_size_in_gb:
                description: Storage size, in GBs, of the software volume that is allocated to the DB system. This is
                             applicable only for VM-based DBs.
                returned: always
                type: string
                sample: 1024
            ncharacter_set:
                description: The national character set for the database.
                returned: always
                type: string
                sample: AL16UTF16
            pdb_name:
                description: Pluggable database name. It must begin with an alphabetic character and can contain a
                             maximum of eight alphanumeric characters. Special characters are not permitted. Pluggable
                             database should not be same as database name.
                returned: always
                type: string
                sample: ocid1.vnic.oc1.iad.xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the Database.
                returned: always
                type: string
                sample: AVAILABLE
            lifecycle_details:
                description: Additional information about the current lifecycle_state of the Database.
                returned: always
                type: string
                sample: AVAILABLE
        sample: [{
                   "character_set":"AL32UTF8",
                   "compartment_id":"ocid1.compartment.aaaa",
                   "freeform_tags":{"deployment":"test"},
                   "defined_tags":{"target_users":{"division":"design"}},
                   "db_backup_config":{
                            "auto_backup_enabled":false
                    },
                   "db_home_id":"ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx",
                   "db_name":"ansibledbone",
                   "db_unique_name":"ansibledbone_iad2cj",
                   "db_workload":"OLTP",
                   "id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_details":null,
                   "lifecycle_state":"BACKUP_IN_PROGRESS",
                   "ncharacter_set":"AL16UTF16",
                   "pdb_name":null,
                   "time_created":"2018-02-22T08:42:26.060000+00:00"
                },
                {
                   "character_set":"AL32UTF8",
                   "compartment_id":"ocid1.compartment.aaaa",
                   "freeform_tags":{"deployment":"production"},
                   "defined_tags":{"target_users":{"division":"development"}},
                   "db_backup_config":{
                            "auto_backup_enabled":true
                    },
                   "db_home_id":"ocid1.dbhome.oc1.iad.xxxxxEXAMPLExxxxx",
                   "db_name":"ansibledbtwo",
                   "db_unique_name":"ansibledbtwo_iad2cj",
                   "db_workload":"OLTP",
                   "id":"ocid1.database.oc1.iad.xxxxxEXAMPLExxxxx",
                   "lifecycle_details":null,
                   "lifecycle_state":"AVAILABLE",
                   "ncharacter_set":"AL16UTF16",
                   "pdb_name":null,
                   "time_created":"2018-02-20T08:42:26.060000+00:00"
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


def list_databases(db_client, module):
    result = dict(databases="")
    compartment_id = module.params.get("compartment_id")
    db_home_id = module.params.get("db_home_id")
    database_id = module.params.get("database_id")
    try:
        if database_id:
            get_logger().debug("Listing Databases %s", database_id)
            response = oci_utils.call_with_backoff(
                db_client.get_database, database_id=database_id
            )
            existing_databases = [response.data]
        elif compartment_id and db_home_id:
            get_logger().debug(
                "Listing all Databases under compartment %s and DB Home %s",
                compartment_id,
                db_home_id,
            )
            existing_databases = oci_utils.list_all_resources(
                db_client.list_databases,
                compartment_id=compartment_id,
                db_home_id=db_home_id,
            )
    except ServiceError as ex:
        get_logger().error("Unable to list Databases due to %s", ex.message)
        module.fail_json(msg=ex.message)

    result["databases"] = to_dict(existing_databases)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_database_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            db_home_id=dict(type="str", required=False),
            database_id=dict(type="str", required=False, aliases=["id"]),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[
            ["compartment_id", "database_id"],
            ["db_home_id", "database_id"],
        ],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    db_client = oci_utils.create_service_client(module, DatabaseClient)
    result = list_databases(db_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
