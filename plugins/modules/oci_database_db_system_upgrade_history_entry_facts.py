#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_database_db_system_upgrade_history_entry_facts
short_description: Fetches details about one or multiple DbSystemUpgradeHistoryEntry resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbSystemUpgradeHistoryEntry resources in Oracle Cloud Infrastructure
    - Gets the history of the upgrade actions performed on the specified DB system.
    - If I(upgrade_history_entry_id) is specified, the details of a single DbSystemUpgradeHistoryEntry will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    upgrade_history_entry_id:
        description:
            - The database/db system upgrade History L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific db_system_upgrade_history_entry.
        type: str
        aliases: ["id"]
    db_system_id:
        description:
            - The DB system L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIMECREATED is ascending.
        type: str
        choices:
            - "TIMESTARTED"
    upgrade_action:
        description:
            - A filter to return only upgradeHistoryEntries that match the specified Upgrade Action.
        type: str
        choices:
            - "PRECHECK"
            - "ROLLBACK"
            - "UPDATE_SNAPSHOT_RETENTION_DAYS"
            - "UPGRADE"
    lifecycle_state:
        description:
            - A filter to return only upgrade history entries that match the given lifecycle state exactly.
        type: str
        choices:
            - "IN_PROGRESS"
            - "SUCCEEDED"
            - "FAILED"
            - "NEEDS_ATTENTION"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific db_system_upgrade_history_entry
  oci_database_db_system_upgrade_history_entry_facts:
    # required
    upgrade_history_entry_id: "ocid1.upgradehistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

- name: List db_system_upgrade_history_entries
  oci_database_db_system_upgrade_history_entry_facts:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: TIMESTARTED
    upgrade_action: PRECHECK
    lifecycle_state: IN_PROGRESS

"""

RETURN = """
db_system_upgrade_history_entries:
    description:
        - List of DbSystemUpgradeHistoryEntry resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the upgrade history entry.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        action:
            description:
                - The operating system upgrade action.
            returned: on success
            type: str
            sample: PRECHECK
        new_gi_version:
            description:
                - A valid Oracle Grid Infrastructure (GI) software version.
            returned: on success
            type: str
            sample: new_gi_version_example
        old_gi_version:
            description:
                - A valid Oracle Grid Infrastructure (GI) software version.
            returned: on success
            type: str
            sample: old_gi_version_example
        snapshot_retention_period_in_days:
            description:
                - The retention period, in days, for the snapshot that allows you to perform a rollback of the upgrade operation. After this number of days
                  passes, you cannot roll back the upgrade.
            returned: on success
            type: int
            sample: 56
        lifecycle_state:
            description:
                - The current state of the action.
            returned: on success
            type: str
            sample: IN_PROGRESS
        lifecycle_details:
            description:
                - A descriptive text associated with the lifecycleState.
                  Typically contains additional displayable text.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_started:
            description:
                - The date and time when the upgrade action started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The date and time when the upgrade action completed
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "action": "PRECHECK",
        "new_gi_version": "new_gi_version_example",
        "old_gi_version": "old_gi_version_example",
        "snapshot_retention_period_in_days": 56,
        "lifecycle_state": "IN_PROGRESS",
        "lifecycle_details": "lifecycle_details_example",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00"
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


class DbSystemUpgradeHistoryEntryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_system_id",
            "upgrade_history_entry_id",
        ]

    def get_required_params_for_list(self):
        return [
            "db_system_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_system_upgrade_history_entry,
            db_system_id=self.module.params.get("db_system_id"),
            upgrade_history_entry_id=self.module.params.get("upgrade_history_entry_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "upgrade_action",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_system_upgrade_history_entries,
            db_system_id=self.module.params.get("db_system_id"),
            **optional_kwargs
        )


DbSystemUpgradeHistoryEntryFactsHelperCustom = get_custom_class(
    "DbSystemUpgradeHistoryEntryFactsHelperCustom"
)


class ResourceFactsHelper(
    DbSystemUpgradeHistoryEntryFactsHelperCustom,
    DbSystemUpgradeHistoryEntryFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            upgrade_history_entry_id=dict(aliases=["id"], type="str"),
            db_system_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMESTARTED"]),
            upgrade_action=dict(
                type="str",
                choices=[
                    "PRECHECK",
                    "ROLLBACK",
                    "UPDATE_SNAPSHOT_RETENTION_DAYS",
                    "UPGRADE",
                ],
            ),
            lifecycle_state=dict(
                type="str",
                choices=["IN_PROGRESS", "SUCCEEDED", "FAILED", "NEEDS_ATTENTION"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_system_upgrade_history_entry",
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

    module.exit_json(db_system_upgrade_history_entries=result)


if __name__ == "__main__":
    main()
