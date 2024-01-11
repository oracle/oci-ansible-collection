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
module: oci_dashboard_service_dashboard_facts
short_description: Fetches details about one or multiple Dashboard resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Dashboard resources in Oracle Cloud Infrastructure
    - Returns a list of dashboards with a specific dashboard group ID.
    - If I(dashboard_id) is specified, the details of a single Dashboard will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dashboard_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard.
            - Required to get a specific dashboard.
        type: str
        aliases: ["id"]
    dashboard_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the dashboard group that the dashboard belongs to.
            - Required to list multiple dashboards.
        type: str
    lifecycle_state:
        description:
            - A filter that returns dashboard resources that match the lifecycle state specified.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A case-sensitive filter that returns resources that match the entire display name specified.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
              Default order for TIMECREATED is descending.
              Default order for DISPLAYNAME is ascending.
              The DISPLAYNAME sort order is case sensitive.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    opc_cross_region:
        description:
            - "To identify if the call is cross-regional. In CRUD calls for a resource, to
              identify that the call originates from different region, set the
              `CrossRegionIdentifierHeader` parameter to a region name (ex - `US-ASHBURN-1`)
              The call will be served from a Replicated bucket.
              For same-region calls, the value is unassigned."
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific dashboard
  oci_dashboard_service_dashboard_facts:
    # required
    dashboard_id: "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    opc_cross_region: us-phoenix-1

- name: List dashboards
  oci_dashboard_service_dashboard_facts:
    # required
    dashboard_group_id: "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated
    opc_cross_region: us-phoenix-1

"""

RETURN = """
dashboards:
    description:
        - List of Dashboard resources
    returned: on success
    type: complex
    contains:
        schema_version:
            description:
                - The schema describing how to interpret the dashboard configuration and widgets.
                - Returned for get operation
            returned: on success
            type: str
            sample: V1
        config:
            description:
                - The dashboard configuration. For example, the layout and widget placement.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        widgets:
            description:
                - The visualization building blocks of the dashboard.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
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
    sample: [{
        "schema_version": "V1",
        "config": {},
        "widgets": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "dashboard_group_id": "ocid1.dashboardgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.dashboard_service import DashboardClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DashboardFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "dashboard_id",
        ]

    def get_required_params_for_list(self):
        return [
            "dashboard_group_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "opc_cross_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_dashboard,
            dashboard_id=self.module.params.get("dashboard_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
            "opc_cross_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_dashboards,
            dashboard_group_id=self.module.params.get("dashboard_group_id"),
            **optional_kwargs
        )


DashboardFactsHelperCustom = get_custom_class("DashboardFactsHelperCustom")


class ResourceFactsHelper(DashboardFactsHelperCustom, DashboardFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            dashboard_id=dict(aliases=["id"], type="str"),
            dashboard_group_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            opc_cross_region=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="dashboard",
        service_client_class=DashboardClient,
        namespace="dashboard_service",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(dashboards=result)


if __name__ == "__main__":
    main()
