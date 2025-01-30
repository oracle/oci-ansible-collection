#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_management_dashboard_management_saved_search
short_description: Manage a ManagementSavedSearch resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ManagementSavedSearch resource in Oracle Cloud Infrastructure
    - "For I(state=present), creates a new saved search.
      Here's an example of how you can use CLI to create a saved search. For information on the details that must be passed to CREATE, you can use the GET API
      to obtain the Create.json file:
      `oci management-dashboard saved-search get --management-saved-search-id ocid1.managementsavedsearch.oc1..savedsearchId1 --query data > Create.json`.
      You can then modify the Create.json file by removing the `id` attribute and making other required changes, and use the `oci management-dashboard saved-
      search create` command."
    - "This resource has the following action operations in the M(oracle.oci.oci_management_dashboard_management_saved_search_actions) module:
      change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    id:
        description:
            - ID of the saved search, which must only be provided for Out-of-the-Box (OOB) saved search.
        type: str
    display_name:
        description:
            - Display name of the saved search.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    provider_id:
        description:
            - ID of the service (for example log-analytics) that owns the saved search. Each service has a unique ID.
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
    provider_name:
        description:
            - The user friendly name of the service (for example, Logging Analytics) that owns the saved search.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    compartment_id:
        description:
            - OCID of the compartment in which the saved search resides.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable.
        type: str
    is_oob_saved_search:
        description:
            - Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and cannot
              be modified.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: bool
    description:
        description:
            - Description of the saved search.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    nls:
        description:
            - JSON that contains internationalization options.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
    type:
        description:
            - Determines how the saved search is displayed in a dashboard.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
        choices:
            - "SEARCH_SHOW_IN_DASHBOARD"
            - "SEARCH_DONT_SHOW_IN_DASHBOARD"
            - "WIDGET_SHOW_IN_DASHBOARD"
            - "WIDGET_DONT_SHOW_IN_DASHBOARD"
            - "FILTER_SHOW_IN_DASHBOARD"
            - "FILTER_DONT_SHOW_IN_DASHBOARD"
    ui_config:
        description:
            - It defines the visualization type of the widget saved search, the UI options of that visualization type, the binding of data to the visualization.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
    data_config:
        description:
            - It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data
              sources.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: list
        elements: dict
    screen_image:
        description:
            - Screen image of the saved search.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    metadata_version:
        description:
            - The version of the metadata defined in the API. This is maintained and enforced by dashboard server. Currently it is 2.0.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    widget_template:
        description:
            - The UI template that the saved search uses to render itself.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    widget_vm:
        description:
            - The View Model that the saved search uses to render itself.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    parameters_config:
        description:
            - Defines parameters for the saved search.
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
    management_saved_search_id:
        description:
            - A unique saved search identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ManagementSavedSearch.
            - Use I(state=present) to create or update a ManagementSavedSearch.
            - Use I(state=absent) to delete a ManagementSavedSearch.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create management_saved_search
  oci_management_dashboard_management_saved_search:
    # required
    display_name: display_name_example
    provider_id: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
    provider_version: provider_version_example
    provider_name: provider_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_oob_saved_search: true
    description: description_example
    nls: null
    type: SEARCH_SHOW_IN_DASHBOARD
    ui_config: null
    data_config: [ "data_config_example" ]
    screen_image: screen_image_example
    metadata_version: metadata_version_example
    widget_template: widget_template_example
    widget_vm: widget_vm_example

    # optional
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    parameters_config: [ "parameters_config_example" ]
    features_config: null
    drilldown_config: [ "drilldown_config_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update management_saved_search
  oci_management_dashboard_management_saved_search:
    # required
    management_saved_search_id: "ocid1.managementsavedsearch.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    provider_id: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
    provider_version: provider_version_example
    provider_name: provider_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_oob_saved_search: true
    description: description_example
    nls: null
    type: SEARCH_SHOW_IN_DASHBOARD
    ui_config: null
    data_config: [ "data_config_example" ]
    screen_image: screen_image_example
    metadata_version: metadata_version_example
    widget_template: widget_template_example
    widget_vm: widget_vm_example
    parameters_config: [ "parameters_config_example" ]
    features_config: null
    drilldown_config: [ "drilldown_config_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update management_saved_search using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_management_dashboard_management_saved_search:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    provider_id: "ocid1.provider.oc1..xxxxxxEXAMPLExxxxxx"
    provider_version: provider_version_example
    provider_name: provider_name_example
    is_oob_saved_search: true
    description: description_example
    nls: null
    type: SEARCH_SHOW_IN_DASHBOARD
    ui_config: null
    data_config: [ "data_config_example" ]
    screen_image: screen_image_example
    metadata_version: metadata_version_example
    widget_template: widget_template_example
    widget_vm: widget_vm_example
    parameters_config: [ "parameters_config_example" ]
    features_config: null
    drilldown_config: [ "drilldown_config_example" ]
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete management_saved_search
  oci_management_dashboard_management_saved_search:
    # required
    management_saved_search_id: "ocid1.managementsavedsearch.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete management_saved_search using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_management_dashboard_management_saved_search:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
management_saved_search:
    description:
        - Details of the ManagementSavedSearch resource acted upon by the current operation
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
                - Determines whether the saved search is an Out-of-the-Box (OOB) saved search. Note that OOB saved searches are only provided by Oracle and
                  cannot be modified.
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
                - It defines how data is fetched. A functional saved search needs a valid dataConfig. See examples on how it can be constructed for various data
                  sources.
            returned: on success
            type: list
            sample: []
        created_by:
            description:
                - The principle id of the user that created this saved search. This is automatically managed by the system. In OCI the value is ignored. In EM
                  it can skipped or otherwise it is ignored in both create and update API and system automatically sets its value.
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
    sample: {
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
    from oci.management_dashboard.models import CreateManagementSavedSearchDetails
    from oci.management_dashboard.models import UpdateManagementSavedSearchDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementSavedSearchHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            ManagementSavedSearchHelperGen, self
        ).get_possible_entity_types() + [
            "managementsavedsearch",
            "managementsavedsearches",
            "managementDashboardmanagementsavedsearch",
            "managementDashboardmanagementsavedsearches",
            "managementsavedsearchresource",
            "managementsavedsearchesresource",
            "managementdashboard",
        ]

    def get_module_resource_id_param(self):
        return "management_saved_search_id"

    def get_module_resource_id(self):
        return self.module.params.get("management_saved_search_id")

    def get_get_fn(self):
        return self.client.get_management_saved_search

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_saved_search,
            management_saved_search_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_saved_search,
            management_saved_search_id=self.module.params.get(
                "management_saved_search_id"
            ),
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
            self.client.list_management_saved_searches, **kwargs
        )

    def get_create_model_class(self):
        return CreateManagementSavedSearchDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_management_saved_search,
            call_fn_args=(),
            call_fn_kwargs=dict(create_management_saved_search_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateManagementSavedSearchDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_management_saved_search,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_saved_search_id=self.module.params.get(
                    "management_saved_search_id"
                ),
                update_management_saved_search_details=update_details,
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
            call_fn=self.client.delete_management_saved_search,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_saved_search_id=self.module.params.get(
                    "management_saved_search_id"
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


ManagementSavedSearchHelperCustom = get_custom_class(
    "ManagementSavedSearchHelperCustom"
)


class ResourceHelper(ManagementSavedSearchHelperCustom, ManagementSavedSearchHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            provider_id=dict(type="str"),
            provider_version=dict(type="str"),
            provider_name=dict(type="str"),
            compartment_id=dict(type="str"),
            is_oob_saved_search=dict(type="bool"),
            description=dict(type="str"),
            nls=dict(type="dict"),
            type=dict(
                type="str",
                choices=[
                    "SEARCH_SHOW_IN_DASHBOARD",
                    "SEARCH_DONT_SHOW_IN_DASHBOARD",
                    "WIDGET_SHOW_IN_DASHBOARD",
                    "WIDGET_DONT_SHOW_IN_DASHBOARD",
                    "FILTER_SHOW_IN_DASHBOARD",
                    "FILTER_DONT_SHOW_IN_DASHBOARD",
                ],
            ),
            ui_config=dict(type="dict"),
            data_config=dict(type="list", elements="dict"),
            screen_image=dict(type="str"),
            metadata_version=dict(type="str"),
            widget_template=dict(type="str"),
            widget_vm=dict(type="str"),
            parameters_config=dict(type="list", elements="dict"),
            features_config=dict(type="dict"),
            drilldown_config=dict(type="list", elements="dict"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            management_saved_search_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_saved_search",
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
