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
module: oci_management_dashboard_facts
short_description: Fetches details about one or multiple ManagementDashboard resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagementDashboard resources in Oracle Cloud Infrastructure
    - Gets the list of dashboards in a compartment with pagination.  Returned properties are the summary.
    - If I(management_dashboard_id) is specified, the details of a single ManagementDashboard will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    management_dashboard_id:
        description:
            - A unique dashboard identifier.
            - Required to get a specific management_dashboard.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple management_dashboards.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is the default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific management_dashboard
  oci_management_dashboard_facts:
    # required
    management_dashboard_id: "ocid1.managementdashboard.oc1..xxxxxxEXAMPLExxxxxx"

- name: List management_dashboards
  oci_management_dashboard_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
management_dashboards:
    description:
        - List of ManagementDashboard resources
    returned: on success
    type: complex
    contains:
        tiles:
            description:
                - Array of dashboard tiles.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - Display name of the saved search.
                    returned: on success
                    type: str
                    sample: display_name_example
                saved_search_id:
                    description:
                        - ID of the saved search.
                    returned: on success
                    type: str
                    sample: "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx"
                row:
                    description:
                        - Tile's row number.
                    returned: on success
                    type: int
                    sample: 56
                column:
                    description:
                        - Tile's column number.
                    returned: on success
                    type: int
                    sample: 56
                height:
                    description:
                        - The number of rows the tile occupies.
                    returned: on success
                    type: int
                    sample: 56
                width:
                    description:
                        - The number of columns the tile occupies.
                    returned: on success
                    type: int
                    sample: 56
                nls:
                    description:
                        - JSON that contains internationalization options.
                    returned: on success
                    type: dict
                    sample: {}
                ui_config:
                    description:
                        - It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the
                          visualization.
                    returned: on success
                    type: dict
                    sample: {}
                data_config:
                    description:
                        - It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for
                          various data sources.
                    returned: on success
                    type: list
                    sample: []
                state:
                    description:
                        - Current state of the saved search.
                    returned: on success
                    type: str
                    sample: DELETED
                drilldown_config:
                    description:
                        - Drill-down configuration to define the destination of a drill-down action.
                    returned: on success
                    type: list
                    sample: []
                parameters_map:
                    description:
                        - Specifies the saved search parameters values
                    returned: on success
                    type: dict
                    sample: {}
        is_show_in_home:
            description:
                - Determines whether the dashboard will be displayed in Dashboard Home.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        is_show_description:
            description:
                - Determines whether the description of the dashboard is displayed.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        ui_config:
            description:
                - JSON that contains user interface options.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        data_config:
            description:
                - Array of JSON that contain data source options.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        is_favorite:
            description:
                - Determines whether the dashboard is set as favorite.
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        saved_searches:
            description:
                - Array of saved searches in the dashboard.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - ID of the saved search.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Display name of the saved search.
                    returned: on success
                    type: str
                    sample: display_name_example
                provider_id:
                    description:
                        - ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.
                    returned: on success
                    type: str
                    sample: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
                provider_version:
                    description:
                        - Version of the service that owns this saved search.
                    returned: on success
                    type: str
                    sample: provider_version_example
                provider_name:
                    description:
                        - Name of the service (for example, Logging Analytics) that owns the saved search.
                    returned: on success
                    type: str
                    sample: provider_name_example
                compartment_id:
                    description:
                        - OCID of the compartment in which the saved search resides.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                is_oob_saved_search:
                    description:
                        - Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle
                          and cannot be modified.
                    returned: on success
                    type: bool
                    sample: true
                description:
                    description:
                        - Description of the saved search.
                    returned: on success
                    type: str
                    sample: description_example
                nls:
                    description:
                        - JSON that contains internationalization options.
                    returned: on success
                    type: dict
                    sample: {}
                type:
                    description:
                        - Determines how the saved search is displayed in a dashboard.
                    returned: on success
                    type: str
                    sample: SEARCH_SHOW_IN_DASHBOARD
                ui_config:
                    description:
                        - It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the
                          visualization.
                    returned: on success
                    type: dict
                    sample: {}
                data_config:
                    description:
                        - It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for
                          various data sources.
                    returned: on success
                    type: list
                    sample: []
                created_by:
                    description:
                        - The principle id of the user that created this saved search. This is automatically managed by the system. In OCI the value is ignored.
                          In EM it can skipped or otherwise it is ignored in both create and update API and system automatically sets its value.
                    returned: on success
                    type: str
                    sample: created_by_example
                updated_by:
                    description:
                        - The principle id of the user that updated this saved search.
                    returned: on success
                    type: str
                    sample: updated_by_example
                time_created:
                    description:
                        - Date and time the saved search was created.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - Date and time the saved search was updated.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                screen_image:
                    description:
                        - Screen image of the saved search.
                    returned: on success
                    type: str
                    sample: screen_image_example
                metadata_version:
                    description:
                        - The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.
                    returned: on success
                    type: str
                    sample: metadata_version_example
                widget_template:
                    description:
                        - The UI template that the saved search uses to render itself.
                    returned: on success
                    type: str
                    sample: widget_template_example
                widget_vm:
                    description:
                        - The View Model that the saved search uses to render itself.
                    returned: on success
                    type: str
                    sample: widget_vm_example
                lifecycle_state:
                    description:
                        - OCI lifecycle status. This is automatically managed by the system.
                    returned: on success
                    type: str
                    sample: ACTIVE
                parameters_config:
                    description:
                        - Defines parameters for the saved search.
                    returned: on success
                    type: list
                    sample: []
                features_config:
                    description:
                        - Contains configuration for enabling features.
                    returned: on success
                    type: dict
                    sample: {}
                drilldown_config:
                    description:
                        - Drill-down configuration to define the destination of a drill-down action.
                    returned: on success
                    type: list
                    sample: []
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
        parameters_config:
            description:
                - Defines parameters for the dashboard.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        drilldown_config:
            description:
                - Drill-down configuration to define the destination of a drill-down action.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        dashboard_id:
            description:
                - ID of the dashboard.  Same as id.
            returned: on success
            type: str
            sample: "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - ID of the dashboard.  Same as dashboardId.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Display name of the dashboard.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of the dashboard.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - OCID of the compartment in which the dashboard resides.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        provider_id:
            description:
                - ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.
            returned: on success
            type: str
            sample: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
        provider_name:
            description:
                - Name of the service (for example, Logging Analytics) that owns the dashboard.
            returned: on success
            type: str
            sample: provider_name_example
        provider_version:
            description:
                - Version of the service that owns the dashboard.
            returned: on success
            type: str
            sample: provider_version_example
        is_oob_dashboard:
            description:
                - Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be
                  modified.
            returned: on success
            type: bool
            sample: true
        created_by:
            description:
                - User who created the dashboard.
            returned: on success
            type: str
            sample: created_by_example
        time_created:
            description:
                - Date and time the dashboard was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        updated_by:
            description:
                - User who updated the dashboard.
            returned: on success
            type: str
            sample: updated_by_example
        time_updated:
            description:
                - Date and time the dashboard was updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        metadata_version:
            description:
                - The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.
            returned: on success
            type: str
            sample: metadata_version_example
        screen_image:
            description:
                - Screen image of the dashboard.
            returned: on success
            type: str
            sample: screen_image_example
        nls:
            description:
                - JSON that contains internationalization options.
            returned: on success
            type: dict
            sample: {}
        type:
            description:
                - Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.
            returned: on success
            type: str
            sample: type_example
        features_config:
            description:
                - Contains configuration for enabling features.
            returned: on success
            type: dict
            sample: {}
        lifecycle_state:
            description:
                - State of dashboard.
            returned: on success
            type: str
            sample: ACTIVE
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
    sample: [{
        "tiles": [{
            "display_name": "display_name_example",
            "saved_search_id": "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx",
            "row": 56,
            "column": 56,
            "height": 56,
            "width": 56,
            "nls": {},
            "ui_config": {},
            "data_config": [],
            "state": "DELETED",
            "drilldown_config": [],
            "parameters_map": {}
        }],
        "is_show_in_home": true,
        "is_show_description": true,
        "ui_config": {},
        "data_config": [],
        "is_favorite": true,
        "saved_searches": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "provider_id": "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx",
            "provider_version": "provider_version_example",
            "provider_name": "provider_name_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "is_oob_saved_search": true,
            "description": "description_example",
            "nls": {},
            "type": "SEARCH_SHOW_IN_DASHBOARD",
            "ui_config": {},
            "data_config": [],
            "created_by": "created_by_example",
            "updated_by": "updated_by_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "screen_image": "screen_image_example",
            "metadata_version": "metadata_version_example",
            "widget_template": "widget_template_example",
            "widget_vm": "widget_vm_example",
            "lifecycle_state": "ACTIVE",
            "parameters_config": [],
            "features_config": {},
            "drilldown_config": [],
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        }],
        "parameters_config": [],
        "drilldown_config": [],
        "dashboard_id": "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "provider_id": "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx",
        "provider_name": "provider_name_example",
        "provider_version": "provider_version_example",
        "is_oob_dashboard": true,
        "created_by": "created_by_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "updated_by": "updated_by_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "metadata_version": "metadata_version_example",
        "screen_image": "screen_image_example",
        "nls": {},
        "type": "type_example",
        "features_config": {},
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.management_dashboard import DashxApisClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementDashboardFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "management_dashboard_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_dashboard,
            management_dashboard_id=self.module.params.get("management_dashboard_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_management_dashboards,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ManagementDashboardFactsHelperCustom = get_custom_class(
    "ManagementDashboardFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagementDashboardFactsHelperCustom, ManagementDashboardFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            management_dashboard_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_dashboard",
        service_client_class=DashxApisClient,
        namespace="management_dashboard",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_dashboards=result)


if __name__ == "__main__":
    main()
