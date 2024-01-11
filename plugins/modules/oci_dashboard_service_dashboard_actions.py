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
module: oci_dashboard_service_dashboard_actions
short_description: Perform actions on a Dashboard resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Dashboard resource in Oracle Cloud Infrastructure
    - For I(action=change_dashboard_group), moves a Dashboard resource from one dashboardGroup identifier to another. When provided, If-Match is checked against
      ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dashboard_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard.
        type: str
        aliases: ["id"]
        required: true
    dashboard_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the dashboardGroup
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Dashboard.
        type: str
        required: true
        choices:
            - "change_dashboard_group"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_dashboard_group on dashboard
  oci_dashboard_service_dashboard_actions:
    # required
    dashboard_id: "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx"
    dashboard_group_id: "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_dashboard_group

"""

RETURN = """
dashboard:
    description:
        - Details of the Dashboard resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        dashboard_group_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard group that the dashboard belongs to.
            returned: on success
            type: str
            sample: "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "A user-friendly name for the dashboard. Does not have to be unique, and it can be changed. Avoid entering confidential information.
                  Leading and trailing spaces and the following special characters are not allowed: <>()=/'\\"&\\\\"
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - "A short description of the dashboard. It can be changed. Avoid entering confidential information.
                  The following special characters are not allowed: <>()=/'\\"&\\\\"
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment containing the dashboard. A
                  dashboard is always in the same compartment as its dashboard group.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        schema_version:
            description:
                - The schema describing how to interpret the dashboard configuration and widgets.
            returned: on success
            type: str
            sample: V1
        time_created:
            description:
                - The date and time the dashboard was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the dashboard was updated, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the dashboard.
            returned: on success
            type: str
            sample: CREATING
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        config:
            description:
                - The dashboard configuration. For example, the layout and widget placement.
            returned: on success
            type: dict
            sample: {}
        widgets:
            description:
                - The visualization building blocks of the dashboard.
            returned: on success
            type: list
            sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "dashboard_group_id": "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "schema_version": "V1",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "config": {},
        "widgets": []
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
    from oci.dashboard_service import DashboardClient
    from oci.dashboard_service.models import ChangeDashboardGroupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DashboardActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_dashboard_group
    """

    @staticmethod
    def get_module_resource_id_param():
        return "dashboard_id"

    def get_module_resource_id(self):
        return self.module.params.get("dashboard_id")

    def get_get_fn(self):
        return self.client.get_dashboard

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_dashboard,
            dashboard_id=self.module.params.get("dashboard_id"),
        )

    def change_dashboard_group(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDashboardGroupDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_dashboard_group,
            call_fn_args=(),
            call_fn_kwargs=dict(
                dashboard_id=self.module.params.get("dashboard_id"),
                change_dashboard_group_details=action_details,
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


DashboardActionsHelperCustom = get_custom_class("DashboardActionsHelperCustom")


class ResourceHelper(DashboardActionsHelperCustom, DashboardActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            dashboard_id=dict(aliases=["id"], type="str", required=True),
            dashboard_group_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_dashboard_group"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="dashboard",
        service_client_class=DashboardClient,
        namespace="dashboard_service",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
