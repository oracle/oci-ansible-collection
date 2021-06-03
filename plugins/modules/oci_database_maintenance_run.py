#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_database_maintenance_run
short_description: Manage a MaintenanceRun resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a MaintenanceRun resource in Oracle Cloud Infrastructure
version_added: "2.9"
author: Oracle (@oracle)
options:
    maintenance_run_id:
        description:
            - The maintenance run OCID.
        type: str
        aliases: ["id"]
        required: true
    is_enabled:
        description:
            - If `FALSE`, skips the maintenance run.
            - This parameter is updatable.
        type: bool
    time_scheduled:
        description:
            - The scheduled date and time of the maintenance run to update.
            - This parameter is updatable.
        type: str
    is_patch_now_enabled:
        description:
            - If set to `TRUE`, starts patching immediately.
            - This parameter is updatable.
        type: bool
    patch_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch to be applied in the maintenance run.
            - This parameter is updatable.
        type: str
    patching_mode:
        description:
            - "Maintenance method, it will be either \\"ROLLING\\" or \\"NONROLLING\\". Default value is ROLLING."
            - This parameter is updatable.
        type: str
        choices:
            - "ROLLING"
            - "NONROLLING"
    state:
        description:
            - The state of the MaintenanceRun.
            - Use I(state=present) to update an existing a MaintenanceRun.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update maintenance_run
  oci_database_maintenance_run:
    is_enabled: false
    maintenance_run_id: "ocid1.maintenancerun.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
maintenance_run:
    description:
        - Details of the MaintenanceRun resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the maintenance run.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The user-friendly name for the maintenance run.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Description of the maintenance run.
            returned: on success
            type: string
            sample: description_example
        lifecycle_state:
            description:
                - The current state of the maintenance run. For Autonomous Database on shared Exadata infrastructure, valid states are IN_PROGRESS, SUCCEEDED
                  and FAILED.
            returned: on success
            type: string
            sample: SCHEDULED
        lifecycle_details:
            description:
                - Additional information about the current lifecycle state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        time_scheduled:
            description:
                - The date and time the maintenance run is scheduled to occur.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_started:
            description:
                - The date and time the maintenance run starts.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_ended:
            description:
                - The date and time the maintenance run was completed.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        target_resource_type:
            description:
                - The type of the target resource on which the maintenance run occurs.
            returned: on success
            type: string
            sample: AUTONOMOUS_EXADATA_INFRASTRUCTURE
        target_resource_id:
            description:
                - The ID of the target resource on which the maintenance run occurs.
            returned: on success
            type: string
            sample: "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx"
        maintenance_type:
            description:
                - Maintenance type.
            returned: on success
            type: string
            sample: PLANNED
        patch_id:
            description:
                - The unique identifier of the patch. The identifier string includes the patch type, the Oracle Database version, and the patch creation date
                  (using the format YYMMDD). For example, the identifier `ru_patch_19.9.0.0_201030` is used for an RU patch for Oracle Database 19.9.0.0 that
                  was released October 30, 2020.
            returned: on success
            type: string
            sample: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"
        maintenance_subtype:
            description:
                - Maintenance sub-type.
            returned: on success
            type: string
            sample: QUARTERLY
        peer_maintenance_run_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the maintenance run for the Autonomous Data Guard
                  association's peer container database.
            returned: on success
            type: string
            sample: "ocid1.peermaintenancerun.oc1..xxxxxxEXAMPLExxxxxx"
        patching_mode:
            description:
                - "Maintenance method, it will be either \\"ROLLING\\" or \\"NONROLLING\\". Default value is ROLLING."
            returned: on success
            type: string
            sample: ROLLING
        patch_failure_count:
            description:
                - Contain the patch failure count.
            returned: on success
            type: int
            sample: 56
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "lifecycle_state": "SCHEDULED",
        "lifecycle_details": "lifecycle_details_example",
        "time_scheduled": "2013-10-20T19:20:30+01:00",
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "target_resource_type": "AUTONOMOUS_EXADATA_INFRASTRUCTURE",
        "target_resource_id": "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx",
        "maintenance_type": "PLANNED",
        "patch_id": "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx",
        "maintenance_subtype": "QUARTERLY",
        "peer_maintenance_run_id": "ocid1.peermaintenancerun.oc1..xxxxxxEXAMPLExxxxxx",
        "patching_mode": "ROLLING",
        "patch_failure_count": 56
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient
    from oci.database.models import UpdateMaintenanceRunDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MaintenanceRunHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_module_resource_id_param(self):
        return "maintenance_run_id"

    def get_module_resource_id(self):
        return self.module.params.get("maintenance_run_id")

    def get_get_fn(self):
        return self.client.get_maintenance_run

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_maintenance_run,
            maintenance_run_id=self.module.params.get("maintenance_run_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_maintenance_runs, **kwargs
        )

    def get_update_model_class(self):
        return UpdateMaintenanceRunDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_maintenance_run,
            call_fn_args=(),
            call_fn_kwargs=dict(
                maintenance_run_id=self.module.params.get("maintenance_run_id"),
                update_maintenance_run_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


MaintenanceRunHelperCustom = get_custom_class("MaintenanceRunHelperCustom")


class ResourceHelper(MaintenanceRunHelperCustom, MaintenanceRunHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            maintenance_run_id=dict(aliases=["id"], type="str", required=True),
            is_enabled=dict(type="bool"),
            time_scheduled=dict(type="str"),
            is_patch_now_enabled=dict(type="bool"),
            patch_id=dict(type="str"),
            patching_mode=dict(type="str", choices=["ROLLING", "NONROLLING"]),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="maintenance_run",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
