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
module: oci_cloud_guard_target_responder_recipe
short_description: Manage a TargetResponderRecipe resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a TargetResponderRecipe resource in Oracle Cloud Infrastructure
    - For I(state=present), attach a ResponderRecipe with the Target
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    responder_recipe_id:
        description:
            - ResponderRecipe Identifier
            - Required for create using I(state=present).
        type: str
    responder_rules:
        description:
            - Update responder rules associated with responder recipe in a target.
            - Required for update using I(state=present) with target_responder_recipe_id present.
        type: list
        elements: dict
        suboptions:
            responder_rule_id:
                description:
                    - Identifier for ResponderRule.
                    - This parameter is updatable.
                type: str
                required: true
            details:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    condition:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            parameter:
                                description:
                                    - parameter Key
                                    - This parameter is updatable.
                                    - Applicable when kind is 'SIMPLE'
                                type: str
                            operator:
                                description:
                                    - type of operator
                                    - This parameter is updatable.
                                    - Applicable when kind is 'SIMPLE'
                                type: str
                                choices:
                                    - "IN"
                                    - "NOT_IN"
                                    - "EQUALS"
                                    - "NOT_EQUALS"
                            value:
                                description:
                                    - type of operator
                                    - This parameter is updatable.
                                    - Applicable when kind is 'SIMPLE'
                                type: str
                            value_type:
                                description:
                                    - type of value
                                    - This parameter is updatable.
                                    - Applicable when kind is 'SIMPLE'
                                type: str
                                choices:
                                    - "MANAGED"
                                    - "CUSTOM"
                            kind:
                                description:
                                    - Type of condition object
                                    - This parameter is updatable.
                                type: str
                                choices:
                                    - "SIMPLE"
                                    - "COMPOSITE"
                                required: true
                            left_operand:
                                description:
                                    - ""
                                    - Applicable when kind is 'COMPOSITE'
                                type: dict
                                suboptions:
                                    kind:
                                        description:
                                            - Type of condition object
                                            - This parameter is updatable.
                                        type: str
                                        choices:
                                            - "COMPOSITE"
                                            - "SIMPLE"
                                        required: true
                            composite_operator:
                                description:
                                    - ""
                                    - This parameter is updatable.
                                    - Applicable when kind is 'COMPOSITE'
                                type: str
                                choices:
                                    - "AND"
                                    - "OR"
                            right_operand:
                                description:
                                    - ""
                                    - Applicable when kind is 'COMPOSITE'
                                type: dict
                                suboptions:
                                    kind:
                                        description:
                                            - Type of condition object
                                            - This parameter is updatable.
                                        type: str
                                        choices:
                                            - "COMPOSITE"
                                            - "SIMPLE"
                                        required: true
                    configurations:
                        description:
                            - Configurations associated with the ResponderRule
                        type: list
                        elements: dict
                        suboptions:
                            config_key:
                                description:
                                    - Unique name of the configuration
                                    - This parameter is updatable.
                                type: str
                                required: true
                            name:
                                description:
                                    - configuration name
                                    - This parameter is updatable.
                                type: str
                                required: true
                            value:
                                description:
                                    - configuration value
                                    - This parameter is updatable.
                                type: str
                                required: true
                    mode:
                        description:
                            - Execution Mode for ResponderRule
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "AUTOACTION"
                            - "USERACTION"
    target_id:
        description:
            - OCID of target
        type: str
        required: true
    target_responder_recipe_id:
        description:
            - OCID of TargetResponderRecipe
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required for create using I(state=present).
        type: str
    state:
        description:
            - The state of the TargetResponderRecipe.
            - Use I(state=present) to create or update a TargetResponderRecipe.
            - Use I(state=absent) to delete a TargetResponderRecipe.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create target_responder_recipe
  oci_cloud_guard_target_responder_recipe:
    # required
    responder_recipe_id: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update target_responder_recipe
  oci_cloud_guard_target_responder_recipe:
    # required
    responder_rules:
    - # required
      responder_rule_id: "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx"
      details:
        # optional
        condition:
          # required
          kind: SIMPLE

          # optional
          parameter: parameter_example
          operator: IN
          value: value_example
          value_type: MANAGED
        configurations:
        - # required
          config_key: config_key_example
          name: name_example
          value: value_example
        mode: AUTOACTION
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    target_responder_recipe_id: "ocid1.targetresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete target_responder_recipe
  oci_cloud_guard_target_responder_recipe:
    # required
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    target_responder_recipe_id: "ocid1.targetresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
target_responder_recipe:
    description:
        - Details of the TargetResponderRecipe resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier of TargetResponderRecipe that can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        responder_recipe_id:
            description:
                - Unique identifier for Responder Recipe of which this is an extension.
            returned: on success
            type: str
            sample: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - ResponderRecipe display name.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - ResponderRecipe description.
            returned: on success
            type: str
            sample: description_example
        owner:
            description:
                - Owner of ResponderRecipe
            returned: on success
            type: str
            sample: CUSTOMER
        time_created:
            description:
                - The date and time the target responder recipe rule was created. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the target responder recipe rule was updated. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        responder_rules:
            description:
                - "List of responder rules associated with the recipe - user input"
            returned: on success
            type: complex
            contains:
                responder_rule_id:
                    description:
                        - Unique ResponderRule identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - ResponderRule display name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - ResponderRule description.
                    returned: on success
                    type: str
                    sample: description_example
                type:
                    description:
                        - Type of Responder
                    returned: on success
                    type: str
                    sample: REMEDIATION
                policies:
                    description:
                        - List of Policy
                    returned: on success
                    type: list
                    sample: []
                supported_modes:
                    description:
                        - Supported Execution Modes
                    returned: on success
                    type: list
                    sample: []
                details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        condition:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
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
                                            type: str
                                            sample: COMPOSITE
                                composite_operator:
                                    description:
                                        - ""
                                    returned: on success
                                    type: str
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
                                            type: str
                                            sample: COMPOSITE
                                kind:
                                    description:
                                        - Type of condition object
                                    returned: on success
                                    type: str
                                    sample: COMPOSITE
                                parameter:
                                    description:
                                        - parameter Key
                                    returned: on success
                                    type: str
                                    sample: parameter_example
                                operator:
                                    description:
                                        - type of operator
                                    returned: on success
                                    type: str
                                    sample: IN
                                value:
                                    description:
                                        - type of operator
                                    returned: on success
                                    type: str
                                    sample: value_example
                                value_type:
                                    description:
                                        - type of value
                                    returned: on success
                                    type: str
                                    sample: MANAGED
                        configurations:
                            description:
                                - ResponderRule configurations
                            returned: on success
                            type: complex
                            contains:
                                config_key:
                                    description:
                                        - Unique name of the configuration
                                    returned: on success
                                    type: str
                                    sample: config_key_example
                                name:
                                    description:
                                        - configuration name
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - configuration value
                                    returned: on success
                                    type: str
                                    sample: value_example
                        is_enabled:
                            description:
                                - Identifies state for ResponderRule
                            returned: on success
                            type: bool
                            sample: true
                        mode:
                            description:
                                - Execution Mode for ResponderRule
                            returned: on success
                            type: str
                            sample: AUTOACTION
                compartment_id:
                    description:
                        - Compartment Identifier
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                time_created:
                    description:
                        - The date and time the target responder recipe rule was created. Format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time the target responder recipe rule was updated. Format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_state:
                    description:
                        - The current state of the ResponderRule.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
        effective_responder_rules:
            description:
                - List of responder rules associated with the recipe after applying all defaults
            returned: on success
            type: complex
            contains:
                responder_rule_id:
                    description:
                        - Unique ResponderRule identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - ResponderRule display name.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - ResponderRule description.
                    returned: on success
                    type: str
                    sample: description_example
                type:
                    description:
                        - Type of Responder
                    returned: on success
                    type: str
                    sample: REMEDIATION
                policies:
                    description:
                        - List of Policy
                    returned: on success
                    type: list
                    sample: []
                supported_modes:
                    description:
                        - Supported Execution Modes
                    returned: on success
                    type: list
                    sample: []
                details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        condition:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
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
                                            type: str
                                            sample: COMPOSITE
                                composite_operator:
                                    description:
                                        - ""
                                    returned: on success
                                    type: str
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
                                            type: str
                                            sample: COMPOSITE
                                kind:
                                    description:
                                        - Type of condition object
                                    returned: on success
                                    type: str
                                    sample: COMPOSITE
                                parameter:
                                    description:
                                        - parameter Key
                                    returned: on success
                                    type: str
                                    sample: parameter_example
                                operator:
                                    description:
                                        - type of operator
                                    returned: on success
                                    type: str
                                    sample: IN
                                value:
                                    description:
                                        - type of operator
                                    returned: on success
                                    type: str
                                    sample: value_example
                                value_type:
                                    description:
                                        - type of value
                                    returned: on success
                                    type: str
                                    sample: MANAGED
                        configurations:
                            description:
                                - ResponderRule configurations
                            returned: on success
                            type: complex
                            contains:
                                config_key:
                                    description:
                                        - Unique name of the configuration
                                    returned: on success
                                    type: str
                                    sample: config_key_example
                                name:
                                    description:
                                        - configuration name
                                    returned: on success
                                    type: str
                                    sample: name_example
                                value:
                                    description:
                                        - configuration value
                                    returned: on success
                                    type: str
                                    sample: value_example
                        is_enabled:
                            description:
                                - Identifies state for ResponderRule
                            returned: on success
                            type: bool
                            sample: true
                        mode:
                            description:
                                - Execution Mode for ResponderRule
                            returned: on success
                            type: str
                            sample: AUTOACTION
                compartment_id:
                    description:
                        - Compartment Identifier
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                time_created:
                    description:
                        - The date and time the target responder recipe rule was created. Format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time the target responder recipe rule was updated. Format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_state:
                    description:
                        - The current state of the ResponderRule.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "responder_recipe_id": "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "owner": "CUSTOMER",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "responder_rules": [{
            "responder_rule_id": "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "type": "REMEDIATION",
            "policies": [],
            "supported_modes": [],
            "details": {
                "condition": {
                    "left_operand": {
                        "kind": "COMPOSITE"
                    },
                    "composite_operator": "AND",
                    "right_operand": {
                        "kind": "COMPOSITE"
                    },
                    "kind": "COMPOSITE",
                    "parameter": "parameter_example",
                    "operator": "IN",
                    "value": "value_example",
                    "value_type": "MANAGED"
                },
                "configurations": [{
                    "config_key": "config_key_example",
                    "name": "name_example",
                    "value": "value_example"
                }],
                "is_enabled": true,
                "mode": "AUTOACTION"
            },
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example"
        }],
        "effective_responder_rules": [{
            "responder_rule_id": "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "type": "REMEDIATION",
            "policies": [],
            "supported_modes": [],
            "details": {
                "condition": {
                    "left_operand": {
                        "kind": "COMPOSITE"
                    },
                    "composite_operator": "AND",
                    "right_operand": {
                        "kind": "COMPOSITE"
                    },
                    "kind": "COMPOSITE",
                    "parameter": "parameter_example",
                    "operator": "IN",
                    "value": "value_example",
                    "value_type": "MANAGED"
                },
                "configurations": [{
                    "config_key": "config_key_example",
                    "name": "name_example",
                    "value": "value_example"
                }],
                "is_enabled": true,
                "mode": "AUTOACTION"
            },
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example"
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
    from oci.cloud_guard import CloudGuardClient
    from oci.cloud_guard.models import AttachTargetResponderRecipeDetails
    from oci.cloud_guard.models import UpdateTargetResponderRecipeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetResponderRecipeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            TargetResponderRecipeHelperGen, self
        ).get_possible_entity_types() + [
            "cloudguardtarget",
            "cloudguardtargets",
            "cloudGuardcloudguardtarget",
            "cloudGuardcloudguardtargets",
            "cloudguardtargetresource",
            "cloudguardtargetsresource",
            "targetresponderrecipe",
            "targetresponderrecipes",
            "cloudGuardtargetresponderrecipe",
            "cloudGuardtargetresponderrecipes",
            "targetresponderreciperesource",
            "targetresponderrecipesresource",
            "cloudguard",
        ]

    def get_module_resource_id_param(self):
        return "target_responder_recipe_id"

    def get_module_resource_id(self):
        return self.module.params.get("target_responder_recipe_id")

    def get_get_fn(self):
        return self.client.get_target_responder_recipe

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_responder_recipe,
            target_responder_recipe_id=summary_model.id,
            target_id=self.module.params.get("target_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_responder_recipe,
            target_id=self.module.params.get("target_id"),
            target_responder_recipe_id=self.module.params.get(
                "target_responder_recipe_id"
            ),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "target_id",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_target_responder_recipes, **kwargs
        )

    def get_create_model_class(self):
        return AttachTargetResponderRecipeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_target_responder_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                attach_target_responder_recipe_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTargetResponderRecipeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_target_responder_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                target_responder_recipe_id=self.module.params.get(
                    "target_responder_recipe_id"
                ),
                update_target_responder_recipe_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_target_responder_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                target_responder_recipe_id=self.module.params.get(
                    "target_responder_recipe_id"
                ),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TargetResponderRecipeHelperCustom = get_custom_class(
    "TargetResponderRecipeHelperCustom"
)


class ResourceHelper(TargetResponderRecipeHelperCustom, TargetResponderRecipeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            responder_recipe_id=dict(type="str"),
            responder_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    responder_rule_id=dict(type="str", required=True),
                    details=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            condition=dict(
                                type="dict",
                                options=dict(
                                    parameter=dict(type="str"),
                                    operator=dict(
                                        type="str",
                                        choices=[
                                            "IN",
                                            "NOT_IN",
                                            "EQUALS",
                                            "NOT_EQUALS",
                                        ],
                                    ),
                                    value=dict(type="str"),
                                    value_type=dict(
                                        type="str", choices=["MANAGED", "CUSTOM"]
                                    ),
                                    kind=dict(
                                        type="str",
                                        required=True,
                                        choices=["SIMPLE", "COMPOSITE"],
                                    ),
                                    left_operand=dict(
                                        type="dict",
                                        options=dict(
                                            kind=dict(
                                                type="str",
                                                required=True,
                                                choices=["COMPOSITE", "SIMPLE"],
                                            )
                                        ),
                                    ),
                                    composite_operator=dict(
                                        type="str", choices=["AND", "OR"]
                                    ),
                                    right_operand=dict(
                                        type="dict",
                                        options=dict(
                                            kind=dict(
                                                type="str",
                                                required=True,
                                                choices=["COMPOSITE", "SIMPLE"],
                                            )
                                        ),
                                    ),
                                ),
                            ),
                            configurations=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    config_key=dict(
                                        type="str", required=True, no_log=True
                                    ),
                                    name=dict(type="str", required=True),
                                    value=dict(type="str", required=True),
                                ),
                            ),
                            mode=dict(type="str", choices=["AUTOACTION", "USERACTION"]),
                        ),
                    ),
                ),
            ),
            target_id=dict(type="str", required=True),
            target_responder_recipe_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target_responder_recipe",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
