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
module: oci_cloud_guard_detector_recipe_actions
short_description: Perform actions on a DetectorRecipe resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DetectorRecipe resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves the DetectorRecipe from current compartment to another.
version_added: "2.9"
author: Oracle (@oracle)
options:
    detector_recipe_id:
        description:
            - DetectorRecipe OCID
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The OCID of the compartment into which the DetectorRecipe should be moved
        type: str
        required: true
    action:
        description:
            - The action to perform on the DetectorRecipe.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on detector_recipe
  oci_cloud_guard_detector_recipe_actions:
    detector_recipe_id: "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
detector_recipe:
    description:
        - Details of the DetectorRecipe resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Ocid for detector recipe
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - DisplayName of detector recipe
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Detector recipe description
            returned: on success
            type: string
            sample: description_example
        compartment_id:
            description:
                - compartmentId of detector recipe
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        source_detector_recipe_id:
            description:
                - Recipe Ocid of the Source Recipe to be cloned
            returned: on success
            type: string
            sample: "ocid1.sourcedetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
        owner:
            description:
                - Owner of detector recipe
            returned: on success
            type: string
            sample: CUSTOMER
        detector:
            description:
                - Type of detector
            returned: on success
            type: string
            sample: IAAS_ACTIVITY_DETECTOR
        detector_rules:
            description:
                - "List of detector rules for the detector type for recipe - user input"
            returned: on success
            type: complex
            contains:
                detector_rule_id:
                    description:
                        - The unique identifier of the detector rule
                    returned: on success
                    type: string
                    sample: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - displayName
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - Description for DetectorRecipeDetectorRule
                    returned: on success
                    type: string
                    sample: description_example
                recommendation:
                    description:
                        - Recommendation for DetectorRecipeDetectorRule
                    returned: on success
                    type: string
                    sample: recommendation_example
                detector:
                    description:
                        - detector for the rule
                    returned: on success
                    type: string
                    sample: IAAS_ACTIVITY_DETECTOR
                service_type:
                    description:
                        - service type of the configuration to which the rule is applied
                    returned: on success
                    type: string
                    sample: service_type_example
                resource_type:
                    description:
                        - resource type of the configuration to which the rule is applied
                    returned: on success
                    type: string
                    sample: resource_type_example
                details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables the control
                            returned: on success
                            type: bool
                            sample: true
                        risk_level:
                            description:
                                - The Risk Level
                            returned: on success
                            type: string
                            sample: CRITICAL
                        configurations:
                            description:
                                - Configuration details
                            returned: on success
                            type: complex
                            contains:
                                config_key:
                                    description:
                                        - Unique name of the configuration
                                    returned: on success
                                    type: string
                                    sample: config_key_example
                                name:
                                    description:
                                        - configuration name
                                    returned: on success
                                    type: string
                                    sample: name_example
                                value:
                                    description:
                                        - configuration value
                                    returned: on success
                                    type: string
                                    sample: value_example
                                data_type:
                                    description:
                                        - configuration data type
                                    returned: on success
                                    type: string
                                    sample: data_type_example
                                values:
                                    description:
                                        - List of configuration values
                                    returned: on success
                                    type: complex
                                    contains:
                                        list_type:
                                            description:
                                                - configuration list item type, either CUSTOM or MANAGED
                                            returned: on success
                                            type: string
                                            sample: MANAGED
                                        managed_list_type:
                                            description:
                                                - type of the managed list
                                            returned: on success
                                            type: string
                                            sample: managed_list_type_example
                                        value:
                                            description:
                                                - configuration value
                                            returned: on success
                                            type: string
                                            sample: value_example
                        condition:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                kind:
                                    description:
                                        - Type of condition object
                                    returned: on success
                                    type: string
                                    sample: SIMPLE
                                parameter:
                                    description:
                                        - parameter Key
                                    returned: on success
                                    type: string
                                    sample: parameter_example
                                operator:
                                    description:
                                        - type of operator
                                    returned: on success
                                    type: string
                                    sample: IN
                                value:
                                    description:
                                        - type of operator
                                    returned: on success
                                    type: string
                                    sample: value_example
                                value_type:
                                    description:
                                        - type of value
                                    returned: on success
                                    type: string
                                    sample: MANAGED
                                left_operand:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        kind:
                                            description:
                                                - Type of condition object
                                            returned: on success
                                            type: string
                                            sample: COMPOSITE
                                composite_operator:
                                    description:
                                        - ""
                                    returned: on success
                                    type: string
                                    sample: AND
                                right_operand:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        kind:
                                            description:
                                                - Type of condition object
                                            returned: on success
                                            type: string
                                            sample: COMPOSITE
                        labels:
                            description:
                                - user defined labels for a detector rule
                            returned: on success
                            type: list
                            sample: []
                        is_configuration_allowed:
                            description:
                                - configuration allowed or not
                            returned: on success
                            type: bool
                            sample: true
                managed_list_types:
                    description:
                        - List of cloudguard managed list types related to this rule
                    returned: on success
                    type: list
                    sample: []
                candidate_responder_rules:
                    description:
                        - List of CandidateResponderRule related to this rule
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The unique identifier of the Responder rule
                            returned: on success
                            type: string
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - The display name of the Responder rule
                            returned: on success
                            type: string
                            sample: display_name_example
                        is_preferred:
                            description:
                                - Preferred state
                            returned: on success
                            type: bool
                            sample: true
                time_created:
                    description:
                        - The date and time the detector recipe rule was created. Format defined by RFC3339.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_updated:
                    description:
                        - The date and time the detector recipe rule was updated. Format defined by RFC3339.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                lifecycle_state:
                    description:
                        - The current state of the DetectorRule.
                    returned: on success
                    type: string
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: string
                    sample: lifecycle_details_example
        effective_detector_rules:
            description:
                - List of effective detector rules for the detector type for recipe after applying defaults
            returned: on success
            type: complex
            contains:
                detector_rule_id:
                    description:
                        - The unique identifier of the detector rule
                    returned: on success
                    type: string
                    sample: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - displayName
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - Description for DetectorRecipeDetectorRule
                    returned: on success
                    type: string
                    sample: description_example
                recommendation:
                    description:
                        - Recommendation for DetectorRecipeDetectorRule
                    returned: on success
                    type: string
                    sample: recommendation_example
                detector:
                    description:
                        - detector for the rule
                    returned: on success
                    type: string
                    sample: IAAS_ACTIVITY_DETECTOR
                service_type:
                    description:
                        - service type of the configuration to which the rule is applied
                    returned: on success
                    type: string
                    sample: service_type_example
                resource_type:
                    description:
                        - resource type of the configuration to which the rule is applied
                    returned: on success
                    type: string
                    sample: resource_type_example
                details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        is_enabled:
                            description:
                                - Enables the control
                            returned: on success
                            type: bool
                            sample: true
                        risk_level:
                            description:
                                - The Risk Level
                            returned: on success
                            type: string
                            sample: CRITICAL
                        configurations:
                            description:
                                - Configuration details
                            returned: on success
                            type: complex
                            contains:
                                config_key:
                                    description:
                                        - Unique name of the configuration
                                    returned: on success
                                    type: string
                                    sample: config_key_example
                                name:
                                    description:
                                        - configuration name
                                    returned: on success
                                    type: string
                                    sample: name_example
                                value:
                                    description:
                                        - configuration value
                                    returned: on success
                                    type: string
                                    sample: value_example
                                data_type:
                                    description:
                                        - configuration data type
                                    returned: on success
                                    type: string
                                    sample: data_type_example
                                values:
                                    description:
                                        - List of configuration values
                                    returned: on success
                                    type: complex
                                    contains:
                                        list_type:
                                            description:
                                                - configuration list item type, either CUSTOM or MANAGED
                                            returned: on success
                                            type: string
                                            sample: MANAGED
                                        managed_list_type:
                                            description:
                                                - type of the managed list
                                            returned: on success
                                            type: string
                                            sample: managed_list_type_example
                                        value:
                                            description:
                                                - configuration value
                                            returned: on success
                                            type: string
                                            sample: value_example
                        condition:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                kind:
                                    description:
                                        - Type of condition object
                                    returned: on success
                                    type: string
                                    sample: SIMPLE
                                parameter:
                                    description:
                                        - parameter Key
                                    returned: on success
                                    type: string
                                    sample: parameter_example
                                operator:
                                    description:
                                        - type of operator
                                    returned: on success
                                    type: string
                                    sample: IN
                                value:
                                    description:
                                        - type of operator
                                    returned: on success
                                    type: string
                                    sample: value_example
                                value_type:
                                    description:
                                        - type of value
                                    returned: on success
                                    type: string
                                    sample: MANAGED
                                left_operand:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        kind:
                                            description:
                                                - Type of condition object
                                            returned: on success
                                            type: string
                                            sample: COMPOSITE
                                composite_operator:
                                    description:
                                        - ""
                                    returned: on success
                                    type: string
                                    sample: AND
                                right_operand:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        kind:
                                            description:
                                                - Type of condition object
                                            returned: on success
                                            type: string
                                            sample: COMPOSITE
                        labels:
                            description:
                                - user defined labels for a detector rule
                            returned: on success
                            type: list
                            sample: []
                        is_configuration_allowed:
                            description:
                                - configuration allowed or not
                            returned: on success
                            type: bool
                            sample: true
                managed_list_types:
                    description:
                        - List of cloudguard managed list types related to this rule
                    returned: on success
                    type: list
                    sample: []
                candidate_responder_rules:
                    description:
                        - List of CandidateResponderRule related to this rule
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The unique identifier of the Responder rule
                            returned: on success
                            type: string
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - The display name of the Responder rule
                            returned: on success
                            type: string
                            sample: display_name_example
                        is_preferred:
                            description:
                                - Preferred state
                            returned: on success
                            type: bool
                            sample: true
                time_created:
                    description:
                        - The date and time the detector recipe rule was created. Format defined by RFC3339.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                time_updated:
                    description:
                        - The date and time the detector recipe rule was updated. Format defined by RFC3339.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                lifecycle_state:
                    description:
                        - The current state of the DetectorRule.
                    returned: on success
                    type: string
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: string
                    sample: lifecycle_details_example
        time_created:
            description:
                - The date and time the detector recipe was created. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The date and time the detector recipe was updated. Format defined by RFC3339.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: string
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
                - System tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  System tags can be viewed by users, but can only be created by the system.
                - "Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "source_detector_recipe_id": "ocid1.sourcedetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx",
        "owner": "CUSTOMER",
        "detector": "IAAS_ACTIVITY_DETECTOR",
        "detector_rules": [{
            "detector_rule_id": "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "recommendation": "recommendation_example",
            "detector": "IAAS_ACTIVITY_DETECTOR",
            "service_type": "service_type_example",
            "resource_type": "resource_type_example",
            "details": {
                "is_enabled": true,
                "risk_level": "CRITICAL",
                "configurations": [{
                    "config_key": "config_key_example",
                    "name": "name_example",
                    "value": "value_example",
                    "data_type": "data_type_example",
                    "values": [{
                        "list_type": "MANAGED",
                        "managed_list_type": "managed_list_type_example",
                        "value": "value_example"
                    }]
                }],
                "condition": {
                    "kind": "SIMPLE",
                    "parameter": "parameter_example",
                    "operator": "IN",
                    "value": "value_example",
                    "value_type": "MANAGED",
                    "left_operand": {
                        "kind": "COMPOSITE"
                    },
                    "composite_operator": "AND",
                    "right_operand": {
                        "kind": "COMPOSITE"
                    }
                },
                "labels": [],
                "is_configuration_allowed": true
            },
            "managed_list_types": [],
            "candidate_responder_rules": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "is_preferred": true
            }],
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example"
        }],
        "effective_detector_rules": [{
            "detector_rule_id": "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "recommendation": "recommendation_example",
            "detector": "IAAS_ACTIVITY_DETECTOR",
            "service_type": "service_type_example",
            "resource_type": "resource_type_example",
            "details": {
                "is_enabled": true,
                "risk_level": "CRITICAL",
                "configurations": [{
                    "config_key": "config_key_example",
                    "name": "name_example",
                    "value": "value_example",
                    "data_type": "data_type_example",
                    "values": [{
                        "list_type": "MANAGED",
                        "managed_list_type": "managed_list_type_example",
                        "value": "value_example"
                    }]
                }],
                "condition": {
                    "kind": "SIMPLE",
                    "parameter": "parameter_example",
                    "operator": "IN",
                    "value": "value_example",
                    "value_type": "MANAGED",
                    "left_operand": {
                        "kind": "COMPOSITE"
                    },
                    "composite_operator": "AND",
                    "right_operand": {
                        "kind": "COMPOSITE"
                    }
                },
                "labels": [],
                "is_configuration_allowed": true
            },
            "managed_list_types": [],
            "candidate_responder_rules": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "is_preferred": true
            }],
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.cloud_guard import CloudGuardClient
    from oci.cloud_guard.models import ChangeDetectorRecipeCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetectorRecipeActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "detector_recipe_id"

    def get_module_resource_id(self):
        return self.module.params.get("detector_recipe_id")

    def get_get_fn(self):
        return self.client.get_detector_recipe

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_detector_recipe,
            detector_recipe_id=self.module.params.get("detector_recipe_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeDetectorRecipeCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_detector_recipe_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detector_recipe_id=self.module.params.get("detector_recipe_id"),
                change_detector_recipe_compartment_details=action_details,
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


DetectorRecipeActionsHelperCustom = get_custom_class(
    "DetectorRecipeActionsHelperCustom"
)


class ResourceHelper(DetectorRecipeActionsHelperCustom, DetectorRecipeActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            detector_recipe_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="detector_recipe",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
