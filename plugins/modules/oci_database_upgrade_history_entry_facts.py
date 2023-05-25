#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_database_upgrade_history_entry_facts
short_description: Fetches details about one or multiple DatabaseUpgradeHistoryEntry resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DatabaseUpgradeHistoryEntry resources in Oracle Cloud Infrastructure
    - Gets the upgrade history for a specified database in a bare metal or virtual machine DB system.
    - If I(upgrade_history_entry_id) is specified, the details of a single DatabaseUpgradeHistoryEntry will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    upgrade_history_entry_id:
        description:
            - The database/db system upgrade History L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific database_upgrade_history_entry.
        type: str
        aliases: ["id"]
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    upgrade_action:
        description:
            - A filter to return only upgradeHistoryEntries that match the specified Upgrade Action.
        type: str
        choices:
            - "PRECHECK"
            - "UPGRADE"
            - "ROLLBACK"
    lifecycle_state:
        description:
            - A filter to return only upgradeHistoryEntries that match the given lifecycle state exactly.
        type: str
        choices:
            - "SUCCEEDED"
            - "FAILED"
            - "IN_PROGRESS"
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is ascending.
        type: str
        choices:
            - "TIMESTARTED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific database_upgrade_history_entry
  oci_database_upgrade_history_entry_facts:
    # required
    upgrade_history_entry_id: "ocid1.upgradehistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"

- name: List database_upgrade_history_entries
  oci_database_upgrade_history_entry_facts:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    upgrade_action: PRECHECK
    lifecycle_state: SUCCEEDED
    sort_by: TIMESTARTED
    sort_order: ASC

"""

RETURN = """
database_upgrade_history_entries:
    description:
        - List of DatabaseUpgradeHistoryEntry resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database upgrade history.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        action:
            description:
                - The database upgrade action.
            returned: on success
            type: str
            sample: PRECHECK
        source:
            description:
                - "The source of the Oracle Database software to be used for the upgrade.
                   - Use `DB_HOME` to specify an existing Database Home to upgrade the database. The database is moved to the target Database Home and makes use
                     of the Oracle Database software version of the target Database Home.
                   - Use `DB_VERSION` to specify a generally-available Oracle Database software version to upgrade the database.
                   - Use `DB_SOFTWARE_IMAGE` to specify a L(database software
                     image,https://docs.cloud.oracle.com/iaas/Content/Database/Concepts/databasesoftwareimage.htm) to upgrade the database."
            returned: on success
            type: str
            sample: DB_HOME
        lifecycle_state:
            description:
                - Status of database upgrade history SUCCEEDED|IN_PROGRESS|FAILED.
            returned: on success
            type: str
            sample: SUCCEEDED
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        target_db_version:
            description:
                - A valid Oracle Database version. For a list of supported versions, use the ListDbVersions operation.
                - "This cannot be updated in parallel with any of the following: licenseModel, dbEdition, cpuCoreCount, computeCount, computeModel,
                  adminPassword, whitelistedIps, isMTLSConnectionRequired, openMode, permissionLevel, dbWorkload, privateEndpointLabel, nsgIds, isRefreshable,
                  dbName, scheduledOperations, dbToolsDetails, isLocalDataGuardEnabled, or isFreeTier."
            returned: on success
            type: str
            sample: target_db_version_example
        target_database_software_image_id:
            description:
                - the database software image used for upgrading database.
            returned: on success
            type: str
            sample: "ocid1.targetdatabasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx"
        target_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
            returned: on success
            type: str
            sample: "ocid1.targetdbhome.oc1..xxxxxxEXAMPLExxxxxx"
        source_db_home_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Database Home.
            returned: on success
            type: str
            sample: "ocid1.sourcedbhome.oc1..xxxxxxEXAMPLExxxxxx"
        time_started:
            description:
                - The date and time when the database upgrade started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The date and time when the database upgrade ended.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        options:
            description:
                - "Additional upgrade options supported by DBUA(Database Upgrade Assistant).
                  Example: \\"-upgradeTimezone false -keepEvents\\""
            returned: on success
            type: str
            sample: options_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "action": "PRECHECK",
        "source": "DB_HOME",
        "lifecycle_state": "SUCCEEDED",
        "lifecycle_details": "lifecycle_details_example",
        "target_db_version": "target_db_version_example",
        "target_database_software_image_id": "ocid1.targetdatabasesoftwareimage.oc1..xxxxxxEXAMPLExxxxxx",
        "target_db_home_id": "ocid1.targetdbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "source_db_home_id": "ocid1.sourcedbhome.oc1..xxxxxxEXAMPLExxxxxx",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "options": "options_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseUpgradeHistoryEntryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_id",
            "upgrade_history_entry_id",
        ]

    def get_required_params_for_list(self):
        return [
            "database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_database_upgrade_history_entry,
            database_id=self.module.params.get("database_id"),
            upgrade_history_entry_id=self.module.params.get("upgrade_history_entry_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "upgrade_action",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_database_upgrade_history_entries,
            database_id=self.module.params.get("database_id"),
            **optional_kwargs
        )


DatabaseUpgradeHistoryEntryFactsHelperCustom = get_custom_class(
    "DatabaseUpgradeHistoryEntryFactsHelperCustom"
)


class ResourceFactsHelper(
    DatabaseUpgradeHistoryEntryFactsHelperCustom,
    DatabaseUpgradeHistoryEntryFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            upgrade_history_entry_id=dict(aliases=["id"], type="str"),
            database_id=dict(type="str", required=True),
            upgrade_action=dict(
                type="str", choices=["PRECHECK", "UPGRADE", "ROLLBACK"]
            ),
            lifecycle_state=dict(
                type="str", choices=["SUCCEEDED", "FAILED", "IN_PROGRESS"]
            ),
            sort_by=dict(type="str", choices=["TIMESTARTED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="database_upgrade_history_entry",
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

    module.exit_json(database_upgrade_history_entries=result)


if __name__ == "__main__":
    main()
