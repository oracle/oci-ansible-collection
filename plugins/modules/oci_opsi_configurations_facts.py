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
module: oci_opsi_configurations_facts
short_description: Fetches details about one or multiple OpsiConfigurations resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OpsiConfigurations resources in Oracle Cloud Infrastructure
    - Gets a list of OPSI configuration resources based on the query parameters specified.
    - If I(opsi_configuration_id) is specified, the details of a single OpsiConfigurations will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    opsi_configuration_id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of OPSI configuration resource.
            - Required to get a specific opsi_configurations.
        type: str
        aliases: ["id"]
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
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple opsi_configurations.
        type: str
    display_name:
        description:
            - Filter to return based on resources that match the entire display name.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Filter to return based on Lifecycle state of OPSI configuration.
        type: list
        elements: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    opsi_config_type:
        description:
            - Filter to return based on configuration type of OPSI configuration.
        type: list
        elements: str
        choices:
            - "UX_CONFIGURATION"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - OPSI configurations list sort options.
        type: str
        choices:
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific opsi_configurations
  oci_opsi_configurations_facts:
    # required
    opsi_configuration_id: "ocid1.opsiconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    opsi_config_field: [ "configItems" ]
    config_item_custom_status: [ "customized" ]
    config_items_applicable_context: [ "config_items_applicable_context_example" ]
    config_item_field: [ "name" ]

- name: List opsi_configurations
  oci_opsi_configurations_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: [ "CREATING" ]
    opsi_config_type: [ "UX_CONFIGURATION" ]
    sort_order: ASC
    sort_by: displayName

"""

RETURN = """
opsi_configurations:
    description:
        - List of OpsiConfigurations resources
    returned: on success
    type: complex
    contains:
        config_items:
            description:
                - Array of configuration item summary objects.
                - Returned for get operation
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
    sample: [{
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
        }],
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
        "lifecycle_details": "lifecycle_details_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpsiConfigurationsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "opsi_configuration_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "opsi_config_field",
            "config_item_custom_status",
            "config_items_applicable_context",
            "config_item_field",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_opsi_configuration,
            opsi_configuration_id=self.module.params.get("opsi_configuration_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "opsi_config_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_opsi_configurations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OpsiConfigurationsFactsHelperCustom = get_custom_class(
    "OpsiConfigurationsFactsHelperCustom"
)


class ResourceFactsHelper(
    OpsiConfigurationsFactsHelperCustom, OpsiConfigurationsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            opsi_configuration_id=dict(aliases=["id"], type="str"),
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
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="list",
                elements="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            opsi_config_type=dict(
                type="list", elements="str", choices=["UX_CONFIGURATION"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="opsi_configurations",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(opsi_configurations=result)


if __name__ == "__main__":
    main()
