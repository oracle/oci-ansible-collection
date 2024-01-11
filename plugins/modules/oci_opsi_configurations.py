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
module: oci_opsi_configurations
short_description: Manage an OpsiConfigurations resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an OpsiConfigurations resource in Oracle Cloud Infrastructure
    - For I(state=present), create an OPSI configuration resource.
    - "This resource has the following action operations in the M(oracle.oci.oci_opsi_configurations_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    opsi_config_field:
        description:
            - Optional fields to return as part of OpsiConfiguration object. Unless requested, these fields will not be returned by default.
        type: list
        elements: str
        choices:
            - "configItems"
    config_item_custom_status:
        description:
            - Specifies whether only customized configuration items or only non-customized configuration items or both have to be returned.
              By default only customized configuration items are returned.
        type: list
        elements: str
        choices:
            - "customized"
            - "nonCustomized"
    config_items_applicable_context:
        description:
            - Returns the configuration items filtered by applicable contexts sent in this param. By default configuration items of all applicable contexts are
              returned.
        type: list
        elements: str
    config_item_field:
        description:
            - Specifies the fields to return in a config item summary.
        type: list
        elements: str
        choices:
            - "name"
            - "value"
            - "defaultValue"
            - "metadata"
            - "applicableContexts"
    opsi_config_type:
        description:
            - OPSI configuration type.
            - Required for create using I(state=present), update using I(state=present) with opsi_configuration_id present.
        type: str
        choices:
            - "UX_CONFIGURATION"
    display_name:
        description:
            - User-friendly display name for the OPSI configuration. The name does not have to be unique.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Description of OPSI configuration.
            - This parameter is updatable.
        type: str
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
    system_tags:
        description:
            - "System tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            - This parameter is updatable.
        type: dict
    config_items:
        description:
            - Array of configuration items with custom values. All and only configuration items requiring custom values should be part of this array.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            config_item_type:
                description:
                    - Type of configuration item.
                    - This parameter is updatable.
                type: str
                choices:
                    - "BASIC"
                required: true
            name:
                description:
                    - Name of configuration item.
                    - This parameter is updatable.
                type: str
            value:
                description:
                    - Value of configuration item.
                    - This parameter is updatable.
                type: str
    opsi_configuration_id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of OPSI configuration resource.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the OpsiConfigurations.
            - Use I(state=present) to create or update an OpsiConfigurations.
            - Use I(state=absent) to delete an OpsiConfigurations.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create opsi_configurations with opsi_config_type = UX_CONFIGURATION
  oci_opsi_configurations:
    # required
    opsi_config_type: UX_CONFIGURATION

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    config_items:
    - # required
      config_item_type: BASIC

      # optional
      name: name_example
      value: value_example

- name: Update opsi_configurations with opsi_config_type = UX_CONFIGURATION
  oci_opsi_configurations:
    # required
    opsi_config_type: UX_CONFIGURATION

    # optional
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    config_items:
    - # required
      config_item_type: BASIC

      # optional
      name: name_example
      value: value_example

- name: Update opsi_configurations using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with opsi_config_type = UX_CONFIGURATION
  oci_opsi_configurations:
    # required
    opsi_config_type: UX_CONFIGURATION

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null
    config_items:
    - # required
      config_item_type: BASIC

      # optional
      name: name_example
      value: value_example

- name: Delete opsi_configurations
  oci_opsi_configurations:
    # required
    opsi_configuration_id: "ocid1.opsiconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete opsi_configurations using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_opsi_configurations:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
opsi_configurations:
    description:
        - Details of the OpsiConfigurations resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of OPSI configuration resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        opsi_config_type:
            description:
                - OPSI configuration type.
            returned: on success
            type: str
            sample: UX_CONFIGURATION
        display_name:
            description:
                - User-friendly display name for the OPSI configuration. The name does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description of OPSI configuration.
            returned: on success
            type: str
            sample: description_example
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
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time at which the resource was first created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time at which the resource was last updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - OPSI configuration resource lifecycle state.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        config_items:
            description:
                - Array of configuration item summary objects.
            returned: on success
            type: complex
            contains:
                config_item_type:
                    description:
                        - Type of configuration item.
                    returned: on success
                    type: str
                    sample: BASIC
                name:
                    description:
                        - Name of configuration item.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - Value of configuration item.
                    returned: on success
                    type: str
                    sample: value_example
                default_value:
                    description:
                        - Value of configuration item.
                    returned: on success
                    type: str
                    sample: default_value_example
                applicable_contexts:
                    description:
                        - List of contexts in Operations Insights where this configuration item is applicable.
                    returned: on success
                    type: list
                    sample: []
                metadata:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        config_item_type:
                            description:
                                - Type of configuration item.
                            returned: on success
                            type: str
                            sample: BASIC
                        display_name:
                            description:
                                - User-friendly display name for the configuration item.
                            returned: on success
                            type: str
                            sample: display_name_example
                        description:
                            description:
                                - Description of configuration item .
                            returned: on success
                            type: str
                            sample: description_example
                        data_type:
                            description:
                                - "Data type of configuration item.
                                  Examples: STRING, BOOLEAN, NUMBER"
                            returned: on success
                            type: str
                            sample: data_type_example
                        unit_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                unit:
                                    description:
                                        - Unit of configuration item.
                                    returned: on success
                                    type: str
                                    sample: unit_example
                                display_name:
                                    description:
                                        - User-friendly display name for the configuration item unit.
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                        value_input_details:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                min_value:
                                    description:
                                        - Minimum value limit for the configuration item.
                                    returned: on success
                                    type: str
                                    sample: min_value_example
                                max_value:
                                    description:
                                        - Maximum value limit for the configuration item.
                                    returned: on success
                                    type: str
                                    sample: max_value_example
                                allowed_value_type:
                                    description:
                                        - Allowed value type of configuration item.
                                    returned: on success
                                    type: str
                                    sample: LIMIT
                                possible_values:
                                    description:
                                        - Allowed values to pick for the configuration item.
                                    returned: on success
                                    type: list
                                    sample: []
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "opsi_config_type": "UX_CONFIGURATION",
        "display_name": "display_name_example",
        "description": "description_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "config_items": [{
            "config_item_type": "BASIC",
            "name": "name_example",
            "value": "value_example",
            "default_value": "default_value_example",
            "applicable_contexts": [],
            "metadata": {
                "config_item_type": "BASIC",
                "display_name": "display_name_example",
                "description": "description_example",
                "data_type": "data_type_example",
                "unit_details": {
                    "unit": "unit_example",
                    "display_name": "display_name_example"
                },
                "value_input_details": {
                    "min_value": "min_value_example",
                    "max_value": "max_value_example",
                    "allowed_value_type": "LIMIT",
                    "possible_values": []
                }
            }
        }]
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
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import CreateOpsiConfigurationDetails
    from oci.opsi.models import UpdateOpsiConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpsiConfigurationsHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(OpsiConfigurationsHelperGen, self).get_possible_entity_types() + [
            "opsiconfigurations",
            "opsiconfiguration",
            "opsiopsiconfigurations",
            "opsiopsiconfiguration",
            "opsiconfigurationsresource",
            "opsiconfigurationresource",
            "opsi",
        ]

    def get_module_resource_id_param(self):
        return "opsi_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("opsi_configuration_id")

    def get_get_fn(self):
        return self.client.get_opsi_configuration

    def get_resource(self):
        optional_params = [
            "opsi_config_field",
            "config_item_custom_status",
            "config_items_applicable_context",
            "config_item_field",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_opsi_configuration,
            opsi_configuration_id=self.module.params.get("opsi_configuration_id"),
            **optional_kwargs
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
            self.client.list_opsi_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateOpsiConfigurationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        optional_enum_params = [
            "opsi_config_field",
            "config_item_custom_status",
            "config_item_field",
        ]
        optional_enum_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_enum_params
            if self.module.params.get(param) is not None
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_opsi_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_opsi_configuration_details=create_details,
                config_items_applicable_context=self.module.params.get(
                    "config_items_applicable_context"
                ),
                **optional_enum_kwargs
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateOpsiConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_opsi_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opsi_configuration_id=self.module.params.get("opsi_configuration_id"),
                update_opsi_configuration_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_opsi_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opsi_configuration_id=self.module.params.get("opsi_configuration_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OpsiConfigurationsHelperCustom = get_custom_class("OpsiConfigurationsHelperCustom")


class ResourceHelper(OpsiConfigurationsHelperCustom, OpsiConfigurationsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            opsi_config_field=dict(
                type="list", elements="str", choices=["configItems"]
            ),
            config_item_custom_status=dict(
                type="list", elements="str", choices=["customized", "nonCustomized"]
            ),
            config_items_applicable_context=dict(type="list", elements="str"),
            config_item_field=dict(
                type="list",
                elements="str",
                choices=[
                    "name",
                    "value",
                    "defaultValue",
                    "metadata",
                    "applicableContexts",
                ],
            ),
            opsi_config_type=dict(type="str", choices=["UX_CONFIGURATION"]),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            config_items=dict(
                type="list",
                elements="dict",
                options=dict(
                    config_item_type=dict(type="str", required=True, choices=["BASIC"]),
                    name=dict(type="str"),
                    value=dict(type="str"),
                ),
            ),
            opsi_configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="opsi_configurations",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
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
