#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_pdb_conversion_history_entry_facts
short_description: Fetches details about one or multiple PdbConversionHistoryEntry resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PdbConversionHistoryEntry resources in Oracle Cloud Infrastructure
    - Gets the pluggable database conversion history for a specified database in a bare metal or virtual machine DB system.
    - If I(pdb_conversion_history_entry_id) is specified, the details of a single PdbConversionHistoryEntry will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    pdb_conversion_history_entry_id:
        description:
            - The database conversion history L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to get a specific pdb_conversion_history_entry.
        type: str
        aliases: ["id"]
    pdb_conversion_action:
        description:
            - A filter to return only the pluggable database conversion history entries that match the specified conversion action. For example, you can use
              this filter to return only entries for the precheck operation.
        type: str
        choices:
            - "PRECHECK"
            - "CONVERT"
            - "SYNC"
            - "SYNC_ROLLBACK"
    lifecycle_state:
        description:
            - "A filter to return only the pluggable database conversion history entries that match the specified lifecycle state. For example, you can use this
              filter to return only entries in the \\"failed\\" lifecycle state."
        type: str
        choices:
            - "SUCCEEDED"
            - "FAILED"
            - "IN_PROGRESS"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). The default order for `TIMECREATED` is ascending.
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
- name: Get a specific pdb_conversion_history_entry
  oci_database_pdb_conversion_history_entry_facts:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    pdb_conversion_history_entry_id: "ocid1.pdbconversionhistoryentry.oc1..xxxxxxEXAMPLExxxxxx"

- name: List pdb_conversion_history_entries
  oci_database_pdb_conversion_history_entry_facts:
    # required
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    pdb_conversion_action: pdb_conversion_action_example
    lifecycle_state: lifecycle_state_example
    sort_by: TIMESTARTED
    sort_order: ASC

"""

RETURN = """
pdb_conversion_history_entries:
    description:
        - List of PdbConversionHistoryEntry resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database conversion history.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        action:
            description:
                - "The operations used to convert a non-container database to a pluggable database.
                  - Use `PRECHECK` to run a pre-check operation on non-container database prior to converting it into a pluggable database.
                  - Use `CONVERT` to convert a non-container database into a pluggable database.
                  - Use `SYNC` if the non-container database was manually converted into a pluggable database using the dbcli command-line utility. Databases
                    may need to be converted manually if the CONVERT action fails when converting a non-container database using the API.
                  - Use `SYNC_ROLLBACK` if the conversion of a non-container database into a pluggable database was manually rolled back using the dbcli command
                    line utility. Conversions may need to be manually rolled back if the CONVERT action fails when converting a non-container database using the
                    API."
            returned: on success
            type: str
            sample: PRECHECK
        target:
            description:
                - "The target container database of the pluggable database created by the database conversion operation. Currently, the database conversion
                  operation only supports creating the pluggable database in a new container database.
                   - Use `NEW_DATABASE` to specify that the pluggable database be created within a new container database in the same database home."
            returned: on success
            type: str
            sample: NEW_DATABASE
        source_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: str
            sample: "ocid1.sourcedatabase.oc1..xxxxxxEXAMPLExxxxxx"
        target_database_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the database.
            returned: on success
            type: str
            sample: "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx"
        cdb_name:
            description:
                - The database name. The name must begin with an alphabetic character and can contain a maximum of 8 alphanumeric characters. Special characters
                  are not permitted. The database name must be unique in the tenancy.
            returned: on success
            type: str
            sample: cdb_name_example
        lifecycle_state:
            description:
                - Status of an operation performed during the conversion of a non-container database to a pluggable database.
            returned: on success
            type: str
            sample: SUCCEEDED
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state for the conversion operation.
            returned: on success
            type: str
            sample: lifecycle_details_example
        time_started:
            description:
                - The date and time when the database conversion operation started.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - The date and time when the database conversion operation ended.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        additional_cdb_params:
            description:
                - Additional container database parameter.
            returned: on success
            type: str
            sample: additional_cdb_params_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "action": "PRECHECK",
        "target": "NEW_DATABASE",
        "source_database_id": "ocid1.sourcedatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "target_database_id": "ocid1.targetdatabase.oc1..xxxxxxEXAMPLExxxxxx",
        "cdb_name": "cdb_name_example",
        "lifecycle_state": "SUCCEEDED",
        "lifecycle_details": "lifecycle_details_example",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "additional_cdb_params": "additional_cdb_params_example"
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


class PdbConversionHistoryEntryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "database_id",
            "pdb_conversion_history_entry_id",
        ]

    def get_required_params_for_list(self):
        return [
            "database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pdb_conversion_history_entry,
            database_id=self.module.params.get("database_id"),
            pdb_conversion_history_entry_id=self.module.params.get(
                "pdb_conversion_history_entry_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "pdb_conversion_action",
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
            self.client.list_pdb_conversion_history_entries,
            database_id=self.module.params.get("database_id"),
            **optional_kwargs
        )


PdbConversionHistoryEntryFactsHelperCustom = get_custom_class(
    "PdbConversionHistoryEntryFactsHelperCustom"
)


class ResourceFactsHelper(
    PdbConversionHistoryEntryFactsHelperCustom, PdbConversionHistoryEntryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            database_id=dict(type="str", required=True),
            pdb_conversion_history_entry_id=dict(aliases=["id"], type="str"),
            pdb_conversion_action=dict(
                type="str", choices=["PRECHECK", "CONVERT", "SYNC", "SYNC_ROLLBACK"]
            ),
            lifecycle_state=dict(
                type="str", choices=["SUCCEEDED", "FAILED", "IN_PROGRESS"]
            ),
            sort_by=dict(type="str", choices=["TIMESTARTED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="pdb_conversion_history_entry",
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

    module.exit_json(pdb_conversion_history_entries=result)


if __name__ == "__main__":
    main()
