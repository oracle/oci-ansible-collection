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
module: oci_database_db_home_patch_history_entry_facts
short_description: Fetches details about one or multiple DbHomePatchHistoryEntry resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DbHomePatchHistoryEntry resources in Oracle Cloud Infrastructure
    - Lists the history of patch operations on the specified Database Home.
    - If I(patch_history_entry_id) is specified, the details of a single DbHomePatchHistoryEntry will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    patch_history_entry_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch history entry.
            - Required to get a specific db_home_patch_history_entry.
        type: str
        aliases: ["id"]
    db_home_id:
        description:
            - The Database Home L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific db_home_patch_history_entry
  oci_database_db_home_patch_history_entry_facts:
    # required
    patch_history_entry_id: "ocid1.patchhistoryentry.oc1..xxxxxxEXAMPLExxxxxx"
    db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

- name: List db_home_patch_history_entries
  oci_database_db_home_patch_history_entry_facts:
    # required
    db_home_id: "ocid1.dbhome.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
db_home_patch_history_entries:
    description:
        - List of DbHomePatchHistoryEntry resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch history entry.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        patch_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch.
            returned: on success
            type: str
            sample: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
        action:
            description:
                - The action being performed or was completed.
            returned: on success
            type: str
            sample: APPLY
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
                - The date and time when the patch action started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The date and time when the patch action completed
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "patch_id": "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx",
        "action": "APPLY",
        "lifecycle_state": "IN_PROGRESS",
        "lifecycle_details": "lifecycle_details_example",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00"
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


class DbHomePatchHistoryEntryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "db_home_id",
            "patch_history_entry_id",
        ]

    def get_required_params_for_list(self):
        return [
            "db_home_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_db_home_patch_history_entry,
            db_home_id=self.module.params.get("db_home_id"),
            patch_history_entry_id=self.module.params.get("patch_history_entry_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_db_home_patch_history_entries,
            db_home_id=self.module.params.get("db_home_id"),
            **optional_kwargs
        )


DbHomePatchHistoryEntryFactsHelperCustom = get_custom_class(
    "DbHomePatchHistoryEntryFactsHelperCustom"
)


class ResourceFactsHelper(
    DbHomePatchHistoryEntryFactsHelperCustom, DbHomePatchHistoryEntryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            patch_history_entry_id=dict(aliases=["id"], type="str"),
            db_home_id=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="db_home_patch_history_entry",
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

    module.exit_json(db_home_patch_history_entries=result)


if __name__ == "__main__":
    main()
