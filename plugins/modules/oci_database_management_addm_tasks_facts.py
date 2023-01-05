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
module: oci_database_management_addm_tasks_facts
short_description: Fetches details about one or multiple AddmTasks resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AddmTasks resources in Oracle Cloud Infrastructure
    - Lists the metadata for each ADDM task who's end snapshot time falls within the provided start and end time. Details include
      the name of the ADDM task, description, user, status and creation date time.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    time_start:
        description:
            - The beginning of the time range to search for ADDM tasks as defined by date-time RFC3339 format.
        type: str
        required: true
    time_end:
        description:
            - The end of the time range to search for ADDM tasks as defined by date-time RFC3339 format.
        type: str
        required: true
    sort_by:
        description:
            - The option to sort the list of ADDM tasks.
        type: str
        choices:
            - "TASK_NAME"
            - "TASK_ID"
            - "DESCRIPTION"
            - "DB_USER"
            - "STATUS"
            - "TIME_CREATED"
            - "BEGIN_TIME"
            - "END_TIME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Descending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List addm_tasks
  oci_database_management_addm_tasks_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    time_start: 2013-10-20T19:20:30+01:00
    time_end: 2013-10-20T19:20:30+01:00

    # optional
    sort_by: TASK_NAME
    sort_order: ASC

"""

RETURN = """
addm_tasks:
    description:
        - List of AddmTasks resources
    returned: on success
    type: complex
    contains:
        task_name:
            description:
                - The name of the ADDM task.
            returned: on success
            type: str
            sample: task_name_example
        task_id:
            description:
                - The ID number of the ADDM task.
            returned: on success
            type: int
            sample: 56
        description:
            description:
                - The description of the ADDM task.
            returned: on success
            type: str
            sample: description_example
        db_user:
            description:
                - The database user who owns the ADDM task.
            returned: on success
            type: str
            sample: db_user_example
        status:
            description:
                - The status of the ADDM task.
            returned: on success
            type: str
            sample: INITIAL
        time_created:
            description:
                - The creation date of the ADDM task.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        how_created:
            description:
                - A description of how the task was created.
            returned: on success
            type: str
            sample: AUTO
        start_snapshot_time:
            description:
                - The timestamp of the beginning AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        end_snapshot_time:
            description:
                - The timestamp of the ending AWR snapshot used in the ADDM task as defined by date-time RFC3339 format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        begin_snapshot_id:
            description:
                - The ID number of the beginning AWR snapshot.
            returned: on success
            type: int
            sample: 56
        end_snapshot_id:
            description:
                - The ID number of the ending AWR snapshot.
            returned: on success
            type: int
            sample: 56
        findings:
            description:
                - The number of ADDM findings.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "task_name": "task_name_example",
        "task_id": 56,
        "description": "description_example",
        "db_user": "db_user_example",
        "status": "INITIAL",
        "time_created": "2013-10-20T19:20:30+01:00",
        "how_created": "AUTO",
        "start_snapshot_time": "2013-10-20T19:20:30+01:00",
        "end_snapshot_time": "2013-10-20T19:20:30+01:00",
        "begin_snapshot_id": 56,
        "end_snapshot_id": 56,
        "findings": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AddmTasksFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
            "time_start",
            "time_end",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.addm_tasks,
            managed_database_id=self.module.params.get("managed_database_id"),
            time_start=self.module.params.get("time_start"),
            time_end=self.module.params.get("time_end"),
            **optional_kwargs
        )


AddmTasksFactsHelperCustom = get_custom_class("AddmTasksFactsHelperCustom")


class ResourceFactsHelper(AddmTasksFactsHelperCustom, AddmTasksFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            time_start=dict(type="str", required=True),
            time_end=dict(type="str", required=True),
            sort_by=dict(
                type="str",
                choices=[
                    "TASK_NAME",
                    "TASK_ID",
                    "DESCRIPTION",
                    "DB_USER",
                    "STATUS",
                    "TIME_CREATED",
                    "BEGIN_TIME",
                    "END_TIME",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="addm_tasks",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(addm_tasks=result)


if __name__ == "__main__":
    main()
