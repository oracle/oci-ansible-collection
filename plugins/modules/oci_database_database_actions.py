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
module: oci_database_database_actions
short_description: Perform actions on a Database resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Database resource in Oracle Cloud Infrastructure
    - For I(action=restore), restore a Database based on the request parameters you provide.
version_added: "2.9"
author: Oracle (@oracle)
options:
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    database_scn:
        description:
            - Restores using the backup with the System Change Number (SCN) specified.
        type: str
    timestamp:
        description:
            - Restores to the timestamp specified.
        type: str
    latest:
        description:
            - Restores to the last known good state with the least possible data loss.
        type: bool
    action:
        description:
            - The action to perform on the Database.
        type: str
        required: true
        choices:
            - "restore"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action restore on database
  oci_database_database_actions:
    database_id: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx
    action: restore

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
    sample: {
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
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import RestoreDatabaseDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        restore
    """

    def __init__(self, *args, **kwargs):
        super(DatabaseActionsHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    @staticmethod
    def get_module_resource_id_param():
        return "database_id"

    def get_module_resource_id(self):
        return self.module.params.get("database_id")

    def get_get_fn(self):
        return self.client.get_database

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database, database_id=self.module.params.get("database_id"),
        )

    def restore(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RestoreDatabaseDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.restore_database,
            call_fn_args=(),
            call_fn_kwargs=dict(
                database_id=self.module.params.get("database_id"),
                restore_database_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DatabaseActionsHelperCustom = get_custom_class("DatabaseActionsHelperCustom")


class ResourceHelper(DatabaseActionsHelperCustom, DatabaseActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            database_id=dict(aliases=["id"], type="str", required=True),
            database_scn=dict(type="str"),
            timestamp=dict(type="str"),
            latest=dict(type="bool"),
            action=dict(type="str", required=True, choices=["restore"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
