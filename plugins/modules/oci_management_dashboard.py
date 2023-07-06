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
module: oci_management_dashboard
short_description: Manage a ManagementDashboard resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ManagementDashboard resource in Oracle Cloud Infrastructure
    - "For I(state=present), creates a new dashboard. Limit for number of saved searches in a dashboard is 20.
      Here's an example of how you can use CLI to create a dashboard. For information on the details that must be passed to CREATE, you can use the GET API to
      obtain the Create.json file:
      `oci management-dashboard dashboard get --management-dashboard-id  \\"ocid1.managementdashboard.oc1..dashboardId1\\" --query data > Create.json.`
      You can then modify the Create.json file by removing the `id` attribute and making other required changes, and use the `oci management-dashboard dashboard
      create` command."
    - "This resource has the following action operations in the M(oracle.oci.oci_management_dashboard_actions) module: export_dashboard, import_dashboard."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    dashboard_id:
        description:
            - ID of the dashboard, which must only be provided for Out-of-the-Box (OOB) dashboards.
        type: str
    provider_id:
        description:
            - ID of the service (for example, log-analytics) that owns the dashboard. Each service has a unique ID.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    provider_name:
        description:
            - The user friendly name of the service (for example, Logging Analytics) that owns the dashboard.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    provider_version:
        description:
            - The version of the metadata of the provider. This is useful for provider to version its features and metadata. Any newly created saved search (or
              dashboard) should use providerVersion 3.0.0.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    tiles:
        description:
            - Array of dashboard tiles.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
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
                    - It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the
                      visualization.
                type: dict
                required: true
            data_config:
                description:
                    - It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various
                      data sources.
                type: list
                elements: dict
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
                type: list
                required: true
            parameters_map:
                description:
                    - Specifies the saved search parameters values
                type: dict
    display_name:
        description:
            - Display name of the dashboard.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of the dashboard.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - OCID of the compartment in which the dashboard resides.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable.
        type: str
    is_oob_dashboard:
        description:
            - Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be
              modified.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    is_show_in_home:
        description:
            - Determines whether the dashboard will be displayed in Dashboard Home.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    metadata_version:
        description:
            - The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_show_description:
        description:
            - Determines whether the description of the dashboard is displayed.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    screen_image:
        description:
            - Screen image of the dashboard.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    nls:
        description:
            - JSON that contains internationalization options.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
    ui_config:
        description:
            - JSON that contains user interface options.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
    data_config:
        description:
            - Array of JSON that contain data source options.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
    type:
        description:
            - Type of dashboard. NORMAL denotes a single dashboard and SET denotes a dashboard set.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_favorite:
        description:
            - Determines whether the dashboard is set as favorite.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    parameters_config:
        description:
            - Defines parameters for the dashboard.
            - This parameter is updatable.
        type: list
        elements: dict
    features_config:
        description:
            - Contains configuration for enabling features.
            - This parameter is updatable.
        type: dict
    drilldown_config:
        description:
            - Drill-down configuration to define the destination of a drill-down action.
            - This parameter is updatable.
        type: list
        elements: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    management_dashboard_id:
        description:
            - A unique dashboard identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ManagementDashboard.
            - Use I(state=present) to create or update a ManagementDashboard.
            - Use I(state=absent) to delete a ManagementDashboard.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create management_dashboard
  oci_management_dashboard:
    # required
    provider_id: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
    provider_name: provider_name_example
    provider_version: provider_version_example
    tiles:
    - # required
      display_name: display_name_example
      saved_search_id: "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx"
      row: 56
      column: 56
      height: 56
      width: 56
      nls: null
      ui_config: null
      data_config: [ "data_config_example" ]
      state: DELETED
      drilldown_config: []

      # optional
      parameters_map: null
    display_name: display_name_example
    description: description_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_oob_dashboard: true
    is_show_in_home: true
    metadata_version: metadata_version_example
    is_show_description: true
    screen_image: screen_image_example
    nls: null
    ui_config: null
    data_config: [ "data_config_example" ]
    type: type_example
    is_favorite: true

    # optional
    dashboard_id: "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx"
    parameters_config: [ "parameters_config_example" ]
    features_config: null
    drilldown_config: [ "drilldown_config_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update management_dashboard
  oci_management_dashboard:
    # required
    management_dashboard_id: "ocid1.managementdashboard.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    provider_id: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
    provider_name: provider_name_example
    provider_version: provider_version_example
    tiles:
    - # required
      display_name: display_name_example
      saved_search_id: "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx"
      row: 56
      column: 56
      height: 56
      width: 56
      nls: null
      ui_config: null
      data_config: [ "data_config_example" ]
      state: DELETED
      drilldown_config: []

      # optional
      parameters_map: null
    display_name: display_name_example
    description: description_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_oob_dashboard: true
    is_show_in_home: true
    metadata_version: metadata_version_example
    is_show_description: true
    screen_image: screen_image_example
    nls: null
    ui_config: null
    data_config: [ "data_config_example" ]
    type: type_example
    is_favorite: true
    parameters_config: [ "parameters_config_example" ]
    features_config: null
    drilldown_config: [ "drilldown_config_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update management_dashboard using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_management_dashboard:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    provider_id: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
    provider_name: provider_name_example
    provider_version: provider_version_example
    tiles:
    - # required
      display_name: display_name_example
      saved_search_id: "ocid1.savedsearch.oc1..xxxxxxEXAMPLExxxxxx"
      row: 56
      column: 56
      height: 56
      width: 56
      nls: null
      ui_config: null
      data_config: [ "data_config_example" ]
      state: DELETED
      drilldown_config: []

      # optional
      parameters_map: null
    description: description_example
    is_oob_dashboard: true
    is_show_in_home: true
    metadata_version: metadata_version_example
    is_show_description: true
    screen_image: screen_image_example
    nls: null
    ui_config: null
    data_config: [ "data_config_example" ]
    type: type_example
    is_favorite: true
    parameters_config: [ "parameters_config_example" ]
    features_config: null
    drilldown_config: [ "drilldown_config_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete management_dashboard
  oci_management_dashboard:
    # required
    management_dashboard_id: "ocid1.managementdashboard.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete management_dashboard using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_management_dashboard:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
management_dashboard:
    description:
        - Details of the ManagementDashboard resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
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
        is_oob_dashboard:
            description:
                - Determines whether the dashboard is an Out-of-the-Box (OOB) dashboard. Note that OOB dashboards are only provided by Oracle and cannot be
                  modified.
            returned: on success
            type: bool
            sample: true
        is_show_in_home:
            description:
                - Determines whether the dashboard will be displayed in Dashboard Home.
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
            type: str
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
            type: str
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
        lifecycle_state:
            description:
                - State of dashboard.
            returned: on success
            type: str
            sample: ACTIVE
        parameters_config:
            description:
                - Defines parameters for the dashboard.
            returned: on success
            type: list
            sample: []
        drilldown_config:
            description:
                - Drill-down configuration to define the destination of a drill-down action.
            returned: on success
            type: list
            sample: []
        features_config:
            description:
                - Contains configuration for enabling features.
            returned: on success
            type: dict
            sample: {}
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
        "dashboard_id": "ocid1.dashboard.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
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
            "drilldown_config": [],
            "parameters_map": {}
        }],
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_oob_dashboard": true,
        "is_show_in_home": true,
        "created_by": "created_by_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "updated_by": "updated_by_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
        "lifecycle_state": "ACTIVE",
        "parameters_config": [],
        "drilldown_config": [],
        "features_config": {},
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.management_dashboard import DashxApisClient
    from oci.management_dashboard.models import CreateManagementDashboardDetails
    from oci.management_dashboard.models import UpdateManagementDashboardDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementDashboardHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ManagementDashboardHelperGen, self).get_possible_entity_types() + [
            "managementdashboard",
            "managementdashboards",
            "managementDashboardmanagementdashboard",
            "managementDashboardmanagementdashboards",
            "managementdashboardresource",
            "managementdashboardsresource",
        ]

    def get_module_resource_id_param(self):
        return "management_dashboard_id"

    def get_module_resource_id(self):
        return self.module.params.get("management_dashboard_id")

    def get_get_fn(self):
        return self.client.get_management_dashboard

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_dashboard,
            management_dashboard_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_dashboard,
            management_dashboard_id=self.module.params.get("management_dashboard_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_management_dashboards, **kwargs
        )

    def get_create_model_class(self):
        return CreateManagementDashboardDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_management_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(create_management_dashboard_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateManagementDashboardDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_management_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_dashboard_id=self.module.params.get(
                    "management_dashboard_id"
                ),
                update_management_dashboard_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_management_dashboard,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_dashboard_id=self.module.params.get(
                    "management_dashboard_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ManagementDashboardHelperCustom = get_custom_class("ManagementDashboardHelperCustom")


class ResourceHelper(ManagementDashboardHelperCustom, ManagementDashboardHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            dashboard_id=dict(type="str"),
            provider_id=dict(type="str"),
            provider_name=dict(type="str"),
            provider_version=dict(type="str"),
            tiles=dict(
                type="list",
                elements="dict",
                options=dict(
                    display_name=dict(aliases=["name"], type="str", required=True),
                    saved_search_id=dict(type="str", required=True),
                    row=dict(type="int", required=True),
                    column=dict(type="int", required=True),
                    height=dict(type="int", required=True),
                    width=dict(type="int", required=True),
                    nls=dict(type="dict", required=True),
                    ui_config=dict(type="dict", required=True),
                    data_config=dict(type="list", elements="dict", required=True),
                    state=dict(
                        type="str",
                        required=True,
                        choices=["DELETED", "UNAUTHORIZED", "DEFAULT"],
                    ),
                    drilldown_config=dict(type="list", required=True),
                    parameters_map=dict(type="dict"),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            compartment_id=dict(type="str"),
            is_oob_dashboard=dict(type="bool"),
            is_show_in_home=dict(type="bool"),
            metadata_version=dict(type="str"),
            is_show_description=dict(type="bool"),
            screen_image=dict(type="str"),
            nls=dict(type="dict"),
            ui_config=dict(type="dict"),
            data_config=dict(type="list", elements="dict"),
            type=dict(type="str"),
            is_favorite=dict(type="bool"),
            parameters_config=dict(type="list", elements="dict"),
            features_config=dict(type="dict"),
            drilldown_config=dict(type="list", elements="dict"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            management_dashboard_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_dashboard",
        service_client_class=DashxApisClient,
        namespace="management_dashboard",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
