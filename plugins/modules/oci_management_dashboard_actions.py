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
module: oci_management_dashboard_actions
short_description: Perform actions on a ManagementDashboard resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagementDashboard resource in Oracle Cloud Infrastructure
    - For I(action=export_dashboard), exports an array of dashboards and their saved searches.
    - For I(action=import_dashboard), imports an array of dashboards and their saved searches.
version_added: "2.9"
author: Oracle (@oracle)
options:
    export_dashboard_id:
        description:
            - "{\\"dashboardIds\\":[\\"dashboardId1\\", \\"dashboardId2\\", ...]}"
            - Required for I(action=export_dashboard).
        type: str
    dashboards:
        description:
            - Array of dashboards.
            - Required for I(action=import_dashboard).
        type: list
        suboptions:
            dashboard_id:
                description:
                    - ID of the dashboard.
                type: str
                required: true
            provider_id:
                description:
                    - ID of the service (for example log-analytics) that owns the dashboard. Each service has a unique ID.
                type: str
                required: true
            provider_name:
                description:
                    - Name of the service (for example, Logging Analytics) that owns the dashboard.
                type: str
                required: true
            provider_version:
                description:
                    - Version of the service that owns the dashboard.
                type: str
                required: true
            tiles:
                description:
                    - Array of dashboard tiles.
                type: list
                required: true
                suboptions:
                    display_name:
                        description:
                            - Display name of the saved search.
                        type: str
                        aliases: ["name"]
                        required: true
                    saved_search_id:
                        description:
                            - ID of the saved search.
                        type: str
                        required: true
                    row:
                        description:
                            - Tile's row number.
                        type: int
                        required: true
                    column:
                        description:
                            - Tile's column number.
                        type: int
                        required: true
                    height:
                        description:
                            - The number of rows the tile occupies.
                        type: int
                        required: true
                    width:
                        description:
                            - The number of columns the tile occupies.
                        type: int
                        required: true
                    nls:
                        description:
                            - JSON that contains internationalization options.
                        type: dict
                        required: true
                    ui_config:
                        description:
                            - JSON that contains user interface options.
                        type: dict
                        required: true
                    data_config:
                        description:
                            - Array of JSON that contain data source options.
                        type: list
                        required: true
                    state:
                        description:
                            - Current state of the saved search.
                        type: str
                        choices:
                            - "DELETED"
                            - "UNAUTHORIZED"
                            - "DEFAULT"
                        required: true
                    drilldown_config:
                        description:
                            - Drill-down configuration to define the destination of a drill-down action.
                        type: dict
                        required: true
            display_name:
                description:
                    - Display name of the dashboard.
                type: str
                aliases: ["name"]
                required: true
            description:
                description:
                    - Description of the dashboard.
                type: str
                required: true
            compartment_id:
                description:
                    - OCID of the compartment in which the dashboard resides.
                type: str
                required: true
            is_oob_dashboard:
                description:
                    - Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be
                      modified.
                type: bool
                required: true
            is_show_in_home:
                description:
                    - Determines whether the dashboard will be displayed in Dashboard Home.
                type: bool
                required: true
            metadata_version:
                description:
                    - Version of the metadata.
                type: str
                required: true
            is_show_description:
                description:
                    - Determines whether the description of the dashboard is displayed.
                type: bool
                required: true
            screen_image:
                description:
                    - Screen image of the dashboard.
                type: str
                required: true
            nls:
                description:
                    - JSON that contains internationalization options.
                type: dict
                required: true
            ui_config:
                description:
                    - JSON that contains user interface options.
                type: dict
                required: true
            data_config:
                description:
                    - Array of JSON that contain data source options.
                type: list
                required: true
            type:
                description:
                    - Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.
                type: str
                required: true
            is_favorite:
                description:
                    - Determines whether the dashboard is set as favorite.
                type: bool
                required: true
            saved_searches:
                description:
                    - Array of saved searches in the dashboard.
                type: list
                required: true
                suboptions:
                    id:
                        description:
                            - ID of the saved search.
                        type: str
                        required: true
                    display_name:
                        description:
                            - Display name of the saved search.
                        type: str
                        aliases: ["name"]
                        required: true
                    provider_id:
                        description:
                            - ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.
                        type: str
                        required: true
                    provider_version:
                        description:
                            - Version of the service that owns this saved search.
                        type: str
                        required: true
                    provider_name:
                        description:
                            - Name of the service (for example, Logging Analytics) that owns the saved search.
                        type: str
                        required: true
                    compartment_id:
                        description:
                            - OCID of the compartment in which the saved search resides.
                        type: str
                        required: true
                    is_oob_saved_search:
                        description:
                            - Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by
                              Oracle and cannot be modified.
                        type: bool
                        required: true
                    description:
                        description:
                            - Description of the saved search.
                        type: str
                        required: true
                    nls:
                        description:
                            - JSON that contains internationalization options.
                        type: dict
                        required: true
                    type:
                        description:
                            - Determines how the saved search is displayed in a dashboard.
                        type: str
                        choices:
                            - "SEARCH_SHOW_IN_DASHBOARD"
                            - "SEARCH_DONT_SHOW_IN_DASHBOARD"
                            - "WIDGET_SHOW_IN_DASHBOARD"
                            - "WIDGET_DONT_SHOW_IN_DASHBOARD"
                        required: true
                    ui_config:
                        description:
                            - JSON that contains user interface options.
                        type: dict
                        required: true
                    data_config:
                        description:
                            - Array of JSON that contain data source options.
                        type: list
                        required: true
                    screen_image:
                        description:
                            - Screen image of the saved search.
                        type: str
                        required: true
                    metadata_version:
                        description:
                            - Version of the metadata.
                        type: str
                        required: true
                    widget_template:
                        description:
                            - Reference to the HTML file of the widget.
                        type: str
                        required: true
                    widget_vm:
                        description:
                            - Reference to the view model of the widget.
                        type: str
                        required: true
                    freeform_tags:
                        description:
                            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                              Example: `{\\"bar-key\\": \\"value\\"}`"
                        type: dict
                    defined_tags:
                        description:
                            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                        type: dict
            freeform_tags:
                description:
                    - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                      Example: `{\\"bar-key\\": \\"value\\"}`"
                type: dict
            defined_tags:
                description:
                    - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                      Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - Applicable only for I(action=import_dashboard).
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - Applicable only for I(action=import_dashboard).
        type: dict
    action:
        description:
            - The action to perform on the ManagementDashboard.
        type: str
        required: true
        choices:
            - "export_dashboard"
            - "import_dashboard"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action export_dashboard on management_dashboard
  oci_management_dashboard_actions:
    export_dashboard_id: "ocid1.exportdashboard.oc1..xxxxxxEXAMPLExxxxxx"
    action: export_dashboard

- name: Perform action import_dashboard on management_dashboard
  oci_management_dashboard_actions:
    dashboards:
    - dashboard_id: "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx"
      provider_id: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
      provider_name: provider_name_example
      provider_version: provider_version_example
      tiles:
      - display_name: display_name_example
        saved_search_id: "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx"
        row: 56
        column: 56
        height: 56
        width: 56
        state: DELETED
      display_name: display_name_example
      description: description_example
      compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
      is_oob_dashboard: true
      is_show_in_home: true
      metadata_version: metadata_version_example
      is_show_description: true
      screen_image: screen_image_example
      type: type_example
      is_favorite: true
      saved_searches:
      - id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name: display_name_example
        provider_id: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
        provider_version: provider_version_example
        provider_name: provider_name_example
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        is_oob_saved_search: true
        description: description_example
        type: SEARCH_SHOW_IN_DASHBOARD
        screen_image: screen_image_example
        metadata_version: metadata_version_example
        widget_template: widget_template_example
        widget_vm: widget_vm_example
    action: import_dashboard

"""

RETURN = """
management_dashboard:
    description:
        - Details of the ManagementDashboard resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        dashboards:
            description:
                - Array of dashboards.
            returned: on success
            type: complex
            contains:
                dashboard_id:
                    description:
                        - ID of the dashboard.
                    returned: on success
                    type: string
                    sample: "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx"
                provider_id:
                    description:
                        - ID of the service (for example log-analytics) that owns the dashboard. Each service has a unique ID.
                    returned: on success
                    type: string
                    sample: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
                provider_name:
                    description:
                        - Name of the service (for example, Logging Analytics) that owns the dashboard.
                    returned: on success
                    type: string
                    sample: provider_name_example
                provider_version:
                    description:
                        - Version of the service that owns the dashboard.
                    returned: on success
                    type: string
                    sample: provider_version_example
                tiles:
                    description:
                        - Array of dashboard tiles.
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - Display name of the saved search.
                            returned: on success
                            type: string
                            sample: display_name_example
                        saved_search_id:
                            description:
                                - ID of the saved search.
                            returned: on success
                            type: string
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
                                - JSON that contains user interface options.
                            returned: on success
                            type: dict
                            sample: {}
                        data_config:
                            description:
                                - Array of JSON that contain data source options.
                            returned: on success
                            type: list
                            sample: []
                        state:
                            description:
                                - Current state of the saved search.
                            returned: on success
                            type: string
                            sample: DELETED
                        drilldown_config:
                            description:
                                - Drill-down configuration to define the destination of a drill-down action.
                            returned: on success
                            type: dict
                            sample: {}
                display_name:
                    description:
                        - Display name of the dashboard.
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - Description of the dashboard.
                    returned: on success
                    type: string
                    sample: description_example
                compartment_id:
                    description:
                        - OCID of the compartment in which the dashboard resides.
                    returned: on success
                    type: string
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                is_oob_dashboard:
                    description:
                        - Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot
                          be modified.
                    returned: on success
                    type: bool
                    sample: true
                is_show_in_home:
                    description:
                        - Determines whether the dashboard will be displayed in Dashboard Home.
                    returned: on success
                    type: bool
                    sample: true
                metadata_version:
                    description:
                        - Version of the metadata.
                    returned: on success
                    type: string
                    sample: metadata_version_example
                is_show_description:
                    description:
                        - Determines whether the description of the dashboard is displayed.
                    returned: on success
                    type: bool
                    sample: true
                screen_image:
                    description:
                        - Screen image of the dashboard.
                    returned: on success
                    type: string
                    sample: screen_image_example
                nls:
                    description:
                        - JSON that contains internationalization options.
                    returned: on success
                    type: dict
                    sample: {}
                ui_config:
                    description:
                        - JSON that contains user interface options.
                    returned: on success
                    type: dict
                    sample: {}
                data_config:
                    description:
                        - Array of JSON that contain data source options.
                    returned: on success
                    type: list
                    sample: []
                type:
                    description:
                        - Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.
                    returned: on success
                    type: string
                    sample: type_example
                is_favorite:
                    description:
                        - Determines whether the dashboard is set as favorite.
                    returned: on success
                    type: bool
                    sample: true
                saved_searches:
                    description:
                        - Array of saved searches in the dashboard.
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - ID of the saved search.
                            returned: on success
                            type: string
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - Display name of the saved search.
                            returned: on success
                            type: string
                            sample: display_name_example
                        provider_id:
                            description:
                                - ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.
                            returned: on success
                            type: string
                            sample: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
                        provider_version:
                            description:
                                - Version of the service that owns this saved search.
                            returned: on success
                            type: string
                            sample: provider_version_example
                        provider_name:
                            description:
                                - Name of the service (for example, Logging Analytics) that owns the saved search.
                            returned: on success
                            type: string
                            sample: provider_name_example
                        compartment_id:
                            description:
                                - OCID of the compartment in which the saved search resides.
                            returned: on success
                            type: string
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        is_oob_saved_search:
                            description:
                                - Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by
                                  Oracle and cannot be modified.
                            returned: on success
                            type: bool
                            sample: true
                        description:
                            description:
                                - Description of the saved search.
                            returned: on success
                            type: string
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
                            type: string
                            sample: SEARCH_SHOW_IN_DASHBOARD
                        ui_config:
                            description:
                                - JSON that contains user interface options.
                            returned: on success
                            type: dict
                            sample: {}
                        data_config:
                            description:
                                - Array of JSON that contain data source options.
                            returned: on success
                            type: list
                            sample: []
                        screen_image:
                            description:
                                - Screen image of the saved search.
                            returned: on success
                            type: string
                            sample: screen_image_example
                        metadata_version:
                            description:
                                - Version of the metadata.
                            returned: on success
                            type: string
                            sample: metadata_version_example
                        widget_template:
                            description:
                                - Reference to the HTML file of the widget.
                            returned: on success
                            type: string
                            sample: widget_template_example
                        widget_vm:
                            description:
                                - Reference to the view model of the widget.
                            returned: on success
                            type: string
                            sample: widget_vm_example
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
    sample: {
        "dashboards": [{
            "dashboard_id": "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx",
            "provider_id": "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx",
            "provider_name": "provider_name_example",
            "provider_version": "provider_version_example",
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
                "drilldown_config": {}
            }],
            "display_name": "display_name_example",
            "description": "description_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "is_oob_dashboard": true,
            "is_show_in_home": true,
            "metadata_version": "metadata_version_example",
            "is_show_description": true,
            "screen_image": "screen_image_example",
            "nls": {},
            "ui_config": {},
            "data_config": [],
            "type": "type_example",
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
                "screen_image": "screen_image_example",
                "metadata_version": "metadata_version_example",
                "widget_template": "widget_template_example",
                "widget_vm": "widget_vm_example",
                "freeform_tags": {'Department': 'Finance'},
                "defined_tags": {'Operations': {'CostCenter': 'US'}}
            }],
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.management_dashboard import DashxApisClient
    from oci.management_dashboard.models import ManagementDashboardImportDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementDashboardActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        export_dashboard
        import_dashboard
    """

    def export_dashboard(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.export_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(
                export_dashboard_id=self.module.params.get("export_dashboard_id"),
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

    def import_dashboard(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ManagementDashboardImportDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(management_dashboard_import_details=action_details,),
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


ManagementDashboardActionsHelperCustom = get_custom_class(
    "ManagementDashboardActionsHelperCustom"
)


class ResourceHelper(
    ManagementDashboardActionsHelperCustom, ManagementDashboardActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            export_dashboard_id=dict(type="str"),
            dashboards=dict(
                type="list",
                elements="dict",
                options=dict(
                    dashboard_id=dict(type="str", required=True),
                    provider_id=dict(type="str", required=True),
                    provider_name=dict(type="str", required=True),
                    provider_version=dict(type="str", required=True),
                    tiles=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            display_name=dict(
                                aliases=["name"], type="str", required=True
                            ),
                            saved_search_id=dict(type="str", required=True),
                            row=dict(type="int", required=True),
                            column=dict(type="int", required=True),
                            height=dict(type="int", required=True),
                            width=dict(type="int", required=True),
                            nls=dict(type="dict", required=True),
                            ui_config=dict(type="dict", required=True),
                            data_config=dict(type="list", required=True),
                            state=dict(
                                type="str",
                                required=True,
                                choices=["DELETED", "UNAUTHORIZED", "DEFAULT"],
                            ),
                            drilldown_config=dict(type="dict", required=True),
                        ),
                    ),
                    display_name=dict(aliases=["name"], type="str", required=True),
                    description=dict(type="str", required=True),
                    compartment_id=dict(type="str", required=True),
                    is_oob_dashboard=dict(type="bool", required=True),
                    is_show_in_home=dict(type="bool", required=True),
                    metadata_version=dict(type="str", required=True),
                    is_show_description=dict(type="bool", required=True),
                    screen_image=dict(type="str", required=True),
                    nls=dict(type="dict", required=True),
                    ui_config=dict(type="dict", required=True),
                    data_config=dict(type="list", required=True),
                    type=dict(type="str", required=True),
                    is_favorite=dict(type="bool", required=True),
                    saved_searches=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            id=dict(type="str", required=True),
                            display_name=dict(
                                aliases=["name"], type="str", required=True
                            ),
                            provider_id=dict(type="str", required=True),
                            provider_version=dict(type="str", required=True),
                            provider_name=dict(type="str", required=True),
                            compartment_id=dict(type="str", required=True),
                            is_oob_saved_search=dict(type="bool", required=True),
                            description=dict(type="str", required=True),
                            nls=dict(type="dict", required=True),
                            type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "SEARCH_SHOW_IN_DASHBOARD",
                                    "SEARCH_DONT_SHOW_IN_DASHBOARD",
                                    "WIDGET_SHOW_IN_DASHBOARD",
                                    "WIDGET_DONT_SHOW_IN_DASHBOARD",
                                ],
                            ),
                            ui_config=dict(type="dict", required=True),
                            data_config=dict(type="list", required=True),
                            screen_image=dict(type="str", required=True),
                            metadata_version=dict(type="str", required=True),
                            widget_template=dict(type="str", required=True),
                            widget_vm=dict(type="str", required=True),
                            freeform_tags=dict(type="dict"),
                            defined_tags=dict(type="dict"),
                        ),
                    ),
                    freeform_tags=dict(type="dict"),
                    defined_tags=dict(type="dict"),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            action=dict(
                type="str",
                required=True,
                choices=["export_dashboard", "import_dashboard"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_dashboard",
        service_client_class=DashxApisClient,
        namespace="management_dashboard",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
