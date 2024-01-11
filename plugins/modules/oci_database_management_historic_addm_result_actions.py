#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_management_historic_addm_result_actions
short_description: Perform actions on a HistoricAddmResult resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a HistoricAddmResult resource in Oracle Cloud Infrastructure
    - For I(action=run_historic_addm), creates and executes a historic ADDM task using the specified AWR snapshot IDs. If an existing ADDM task
      uses the provided awr snapshot IDs, the existing task will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        aliases: ["id"]
        required: true
    start_snapshot_id:
        description:
            - The ID number of the beginning AWR snapshot.
        type: int
        required: true
    end_snapshot_id:
        description:
            - The ID of the ending AWR snapshot.
        type: int
        required: true
    action:
        description:
            - The action to perform on the HistoricAddmResult.
        type: str
        required: true
        choices:
            - "run_historic_addm"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action run_historic_addm on historic_addm_result
  oci_database_management_historic_addm_result_actions:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    start_snapshot_id: 56
    end_snapshot_id: 56
    action: run_historic_addm

"""

RETURN = """
historic_addm_result:
    description:
        - Details of the HistoricAddmResult resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        is_newly_created:
            description:
                - Specifies whether the ADDM task returned had already existed or was newly created by the api call.
            returned: on success
            type: bool
            sample: true
        task_name:
            description:
                - The name of the historic ADDM task.
            returned: on success
            type: str
            sample: task_name_example
        task_id:
            description:
                - The ID of the historic ADDM task.
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
                - The database user who owns the historic ADDM task.
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
    sample: {
        "is_newly_created": true,
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
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient
    from oci.database_management.models import RunHistoricAddmDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HistoricAddmResultActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        run_historic_addm
    """

    @staticmethod
    def get_module_resource_id_param():
        return "managed_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_database_id")

    def run_historic_addm(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RunHistoricAddmDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.run_historic_addm,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                run_historic_addm_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


HistoricAddmResultActionsHelperCustom = get_custom_class(
    "HistoricAddmResultActionsHelperCustom"
)


class ResourceHelper(
    HistoricAddmResultActionsHelperCustom, HistoricAddmResultActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            managed_database_id=dict(aliases=["id"], type="str", required=True),
            start_snapshot_id=dict(type="int", required=True),
            end_snapshot_id=dict(type="int", required=True),
            action=dict(type="str", required=True, choices=["run_historic_addm"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="historic_addm_result",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
