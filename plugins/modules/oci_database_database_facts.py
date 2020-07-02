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
module: oci_database_database_facts
short_description: Fetches details about one or multiple Database resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Database resources in Oracle Cloud Infrastructure
    - Gets a list of the databases in the specified Database Home.
    - If I(database_id) is specified, the details of a single Database will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific database.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple databases.
        type: str
    db_home_id:
        description:
            - A Database Home L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple databases.
        type: str
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is descending.  Default order for DBNAME is
              ascending. The DBNAME sort order is case sensitive.
        type: str
        choices:
            - "DBNAME"
            - "TIMECREATED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to return only resources that match the given lifecycle state exactly.
        type: str
        choices:
            - "PROVISIONING"
            - "AVAILABLE"
            - "UPDATING"
            - "BACKUP_IN_PROGRESS"
            - "TERMINATING"
            - "TERMINATED"
            - "RESTORE_FAILED"
            - "FAILED"
    db_name:
        description:
            - A filter to return only resources that match the entire database name given. The match is not case sensitive.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List databases
  oci_database_database_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    db_home_id: ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific database
  oci_database_database_facts:
    database_id: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
databases:
    description:
        - List of Database resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        character_set:
            description:
                - The character set for the database.
            returned: on success
            type: string
            sample: character_set_example
        ncharacter_set:
            description:
                - The national character set for the database.
            returned: on success
            type: string
            sample: ncharacter_set_example
        db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
            returned: on success
            type: string
            sample: ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx
        db_name:
            description:
                - The database name.
            returned: on success
            type: string
            sample: db_name_example
        pdb_name:
            description:
                - The name of the pluggable database. The name must begin with an alphabetic character and can contain a maximum of eight alphanumeric
                  characters. Special characters are not permitted. Pluggable database should not be same as database name.
            returned: on success
            type: string
            sample: pdb_name_example
        db_workload:
            description:
                - The database workload type.
            returned: on success
            type: string
            sample: db_workload_example
        db_unique_name:
            description:
                - A system-generated name for the database to ensure uniqueness within an Oracle Data Guard group (a primary database and its standby
                  databases). The unique name cannot be changed.
            returned: on success
            type: string
            sample: db_unique_name_example
        lifecycle_details:
            description:
                - Additional information about the current lifecycleState.
            returned: on success
            type: string
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the database.
            returned: on success
            type: string
            sample: PROVISIONING
        time_created:
            description:
                - The date and time the database was created.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
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
                    type: string
                    sample: cdb_default_example
                cdb_ip_default:
                    description:
                        - IP based CDB Connection String.
                    returned: on success
                    type: string
                    sample: cdb_ip_default_example
                all_connection_strings:
                    description:
                        - All connection strings to use to connect to the Database.
                    returned: on success
                    type: dict
                    sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "character_set": "character_set_example",
        "ncharacter_set": "ncharacter_set_example",
        "db_home_id": "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "db_name": "db_name_example",
        "pdb_name": "pdb_name_example",
        "db_workload": "db_workload_example",
        "db_unique_name": "db_unique_name_example",
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "PROVISIONING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "db_backup_config": {
            "auto_backup_enabled": true,
            "recovery_window_in_days": 56
        },
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "connection_strings": {
            "cdb_default": "cdb_default_example",
            "cdb_ip_default": "cdb_ip_default_example",
            "all_connection_strings": {}
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "db_home_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database, database_id=self.module.params.get("database_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "db_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_databases,
            compartment_id=self.module.params.get("compartment_id"),
            db_home_id=self.module.params.get("db_home_id"),
            **optional_kwargs
        )


DatabaseFactsHelperCustom = get_custom_class("DatabaseFactsHelperCustom")


class ResourceFactsHelper(DatabaseFactsHelperCustom, DatabaseFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            db_home_id=dict(type="str"),
            sort_by=dict(type="str", choices=["DBNAME", "TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "PROVISIONING",
                    "AVAILABLE",
                    "UPDATING",
                    "BACKUP_IN_PROGRESS",
                    "TERMINATING",
                    "TERMINATED",
                    "RESTORE_FAILED",
                    "FAILED",
                ],
            ),
            db_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(databases=result)


if __name__ == "__main__":
    main()
