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
module: oci_opsi_configuration_items_facts
short_description: Fetches details about a ConfigurationItems resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ConfigurationItems resource in Oracle Cloud Infrastructure
    - Gets the applicable configuration items based on the query parameters specified. Configuration items for an opsiConfigType with respect to a compartmentId
      can be fetched.
      Values specified in configItemField param will determine what fields for each configuration items have to be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    opsi_config_type:
        description:
            - Filter to return configuration items based on configuration type of OPSI configuration.
        type: str
        choices:
            - "UX_CONFIGURATION"
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
            - "valueSourceConfig"
            - "metadata"
            - "applicableContexts"
    name:
        description:
            - A filter to return only configuration items that match the entire name.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific configuration_items
  oci_opsi_configuration_items_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    opsi_config_type: UX_CONFIGURATION
    config_items_applicable_context: [ "config_items_applicable_context_example" ]
    config_item_field: [ "name" ]
    name: name_example

"""

RETURN = """
configuration_items:
    description:
        - ConfigurationItems resource
    returned: on success
    type: complex
    contains:
        opsi_config_type:
            description:
                - OPSI configuration type.
            returned: on success
            type: str
            sample: UX_CONFIGURATION
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
                value_source_config:
                    description:
                        - Source configuration from where the value is taken for a configuration item.
                    returned: on success
                    type: str
                    sample: DEFAULT
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
        "opsi_config_type": "UX_CONFIGURATION",
        "config_items": [{
            "config_item_type": "BASIC",
            "name": "name_example",
            "value": "value_example",
            "value_source_config": "DEFAULT",
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


class ConfigurationItemsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return []

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
            "opsi_config_type",
            "config_items_applicable_context",
            "config_item_field",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_configuration_items, **optional_kwargs
        )


ConfigurationItemsFactsHelperCustom = get_custom_class(
    "ConfigurationItemsFactsHelperCustom"
)


class ResourceFactsHelper(
    ConfigurationItemsFactsHelperCustom, ConfigurationItemsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            opsi_config_type=dict(type="str", choices=["UX_CONFIGURATION"]),
            config_items_applicable_context=dict(type="list", elements="str"),
            config_item_field=dict(
                type="list",
                elements="str",
                choices=[
                    "name",
                    "value",
                    "defaultValue",
                    "valueSourceConfig",
                    "metadata",
                    "applicableContexts",
                ],
            ),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="configuration_items",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(configuration_items=result)


if __name__ == "__main__":
    main()
