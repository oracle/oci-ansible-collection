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
module: oci_database_maintenance_run_facts
short_description: Fetches details about one or multiple MaintenanceRun resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MaintenanceRun resources in Oracle Cloud Infrastructure
    - Gets a list of the maintenance runs in the specified compartment.
    - If I(maintenance_run_id) is specified, the details of a single MaintenanceRun will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    maintenance_run_id:
        description:
            - The maintenance run OCID.
            - Required to get a specific maintenance_run.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
            - Required to list multiple maintenance_runs.
        type: str
    target_resource_id:
        description:
            - The target resource ID.
        type: str
    target_resource_type:
        description:
            - The type of the target resource.
        type: str
        choices:
            - "AUTONOMOUS_EXADATA_INFRASTRUCTURE"
            - "AUTONOMOUS_CONTAINER_DATABASE"
            - "EXADATA_DB_SYSTEM"
            - "CLOUD_EXADATA_INFRASTRUCTURE"
    maintenance_type:
        description:
            - The maintenance type.
        type: str
        choices:
            - "PLANNED"
            - "UNPLANNED"
    sort_by:
        description:
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for TIME_SCHEDULED and TIME_ENDED is descending. Default order
              for DISPLAYNAME is ascending. The DISPLAYNAME sort order is case sensitive.
            - "**Note:** If you do not include the availability domain filter, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIME_SCHEDULED"
            - "TIME_ENDED"
            - "DISPLAYNAME"
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
            - "SCHEDULED"
            - "IN_PROGRESS"
            - "SUCCEEDED"
            - "SKIPPED"
            - "FAILED"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
    availability_domain:
        description:
            - A filter to return only resources that match the given availability domain exactly.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List maintenance_runs
  oci_database_maintenance_run_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific maintenance_run
  oci_database_maintenance_run_facts:
    maintenance_run_id: ocid1.maintenancerun.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
maintenance_runs:
    description:
        - List of MaintenanceRun resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the maintenance run.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        compartment_id:
            description:
                - The OCID of the compartment.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
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
                - The current state of the maintenance run.
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
            sample: ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx
        maintenance_type:
            description:
                - Maintenance type.
            returned: on success
            type: string
            sample: PLANNED
        patch_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch to be applied in the maintenance run.
            returned: on success
            type: string
            sample: ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx
        maintenance_subtype:
            description:
                - Maintenance sub-type.
            returned: on success
            type: string
            sample: QUARTERLY
    sample: [{
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
        "maintenance_subtype": "QUARTERLY"
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


class MaintenanceRunFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "maintenance_run_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_maintenance_run,
            maintenance_run_id=self.module.params.get("maintenance_run_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "target_resource_id",
            "target_resource_type",
            "maintenance_type",
            "sort_by",
            "sort_order",
            "lifecycle_state",
            "availability_domain",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_maintenance_runs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


MaintenanceRunFactsHelperCustom = get_custom_class("MaintenanceRunFactsHelperCustom")


class ResourceFactsHelper(
    MaintenanceRunFactsHelperCustom, MaintenanceRunFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            maintenance_run_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            target_resource_id=dict(type="str"),
            target_resource_type=dict(
                type="str",
                choices=[
                    "AUTONOMOUS_EXADATA_INFRASTRUCTURE",
                    "AUTONOMOUS_CONTAINER_DATABASE",
                    "EXADATA_DB_SYSTEM",
                    "CLOUD_EXADATA_INFRASTRUCTURE",
                ],
            ),
            maintenance_type=dict(type="str", choices=["PLANNED", "UNPLANNED"]),
            sort_by=dict(
                type="str", choices=["TIME_SCHEDULED", "TIME_ENDED", "DISPLAYNAME"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "SCHEDULED",
                    "IN_PROGRESS",
                    "SUCCEEDED",
                    "SKIPPED",
                    "FAILED",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                ],
            ),
            availability_domain=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="maintenance_run",
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

    module.exit_json(maintenance_runs=result)


if __name__ == "__main__":
    main()
