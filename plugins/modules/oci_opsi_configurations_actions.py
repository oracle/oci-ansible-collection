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
module: oci_opsi_configurations_actions
short_description: Perform actions on an OpsiConfigurations resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an OpsiConfigurations resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an OpsiConfiguration resource from one compartment to another.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    opsi_configuration_id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of OPSI configuration resource.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the OpsiConfigurations.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on opsi_configurations
  oci_opsi_configurations_actions:
    # required
    opsi_configuration_id: "ocid1.opsiconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import ChangeOpsiConfigurationCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OpsiConfigurationsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "opsi_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("opsi_configuration_id")

    def get_get_fn(self):
        return self.client.get_opsi_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_opsi_configuration,
            opsi_configuration_id=self.module.params.get("opsi_configuration_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeOpsiConfigurationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_opsi_configuration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                opsi_configuration_id=self.module.params.get("opsi_configuration_id"),
                change_opsi_configuration_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OpsiConfigurationsActionsHelperCustom = get_custom_class(
    "OpsiConfigurationsActionsHelperCustom"
)


class ResourceHelper(
    OpsiConfigurationsActionsHelperCustom, OpsiConfigurationsActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            opsi_configuration_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
