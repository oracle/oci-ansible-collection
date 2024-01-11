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
module: oci_cloud_guard_responder_recipe
short_description: Manage a ResponderRecipe resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a ResponderRecipe resource in Oracle Cloud Infrastructure
    - For I(state=present), create a ResponderRecipe.
    - "This resource has the following action operations in the M(oracle.oci.oci_cloud_guard_responder_recipe_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    source_responder_recipe_id:
        description:
            - The id of the source responder recipe.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - Responder recipe display name.
            - Avoid entering confidential information.
            - Required for create using I(state=present), update using I(state=present) with responder_recipe_id present.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Responder recipe description.
            - Avoid entering confidential information.
            - This parameter is updatable.
        type: str
    responder_rules:
        description:
            - Responder Rules to override from source responder recipe
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            responder_rule_id:
                description:
                    - ResponderRecipeRule Identifier
                type: str
                required: true
            details:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    is_enabled:
                        description:
                            - Identifies state for ResponderRule
                        type: bool
                        required: true
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - Avoid entering confidential information.
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    responder_recipe_id:
        description:
            - OCID of ResponderRecipe
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ResponderRecipe.
            - Use I(state=present) to create or update a ResponderRecipe.
            - Use I(state=absent) to delete a ResponderRecipe.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create responder_recipe
  oci_cloud_guard_responder_recipe:
    # required
    source_responder_recipe_id: "ocid1.sourceresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    responder_rules:
    - # required
      responder_rule_id: "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx"
      details:
        # required
        is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update responder_recipe
  oci_cloud_guard_responder_recipe:
    # required
    display_name: display_name_example
    responder_recipe_id: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    responder_rules:
    - # required
      responder_rule_id: "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx"
      details:
        # required
        is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update responder_recipe using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_guard_responder_recipe:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    responder_rules:
    - # required
      responder_rule_id: "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx"
      details:
        # required
        is_enabled: true
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete responder_recipe
  oci_cloud_guard_responder_recipe:
    # required
    responder_recipe_id: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete responder_recipe using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_guard_responder_recipe:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
responder_recipe:
    description:
        - Details of the ResponderRecipe resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Identifier for ResponderRecipe.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
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
        responder_rules:
            description:
                - List of responder rules associated with the recipe
            returned: on success
            type: complex
            contains:
                responder_rule_id:
                    description:
                        - Identifier for ResponderRule.
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
                        - The date and time the responder recipe rule was created. Format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time the responder recipe rule was updated. Format defined by RFC3339.
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
                - List of responder rules associated with the recipe
            returned: on success
            type: complex
            contains:
                responder_rule_id:
                    description:
                        - Identifier for ResponderRule.
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
                        - The date and time the responder recipe rule was created. Format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time the responder recipe rule was updated. Format defined by RFC3339.
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
        source_responder_recipe_id:
            description:
                - The id of the source responder recipe.
            returned: on success
            type: str
            sample: "ocid1.sourceresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the responder recipe was created. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the responder recipe was updated. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Example.
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
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Avoid entering confidential information.
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
        "owner": "CUSTOMER",
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
        }],
        "source_responder_recipe_id": "ocid1.sourceresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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
    from oci.cloud_guard.models import CreateResponderRecipeDetails
    from oci.cloud_guard.models import UpdateResponderRecipeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResponderRecipeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ResponderRecipeHelperGen, self).get_possible_entity_types() + [
            "cloudguardresponderrecipe",
            "cloudguardresponderrecipes",
            "cloudGuardcloudguardresponderrecipe",
            "cloudGuardcloudguardresponderrecipes",
            "cloudguardresponderreciperesource",
            "cloudguardresponderrecipesresource",
            "responderrecipe",
            "responderrecipes",
            "cloudGuardresponderrecipe",
            "cloudGuardresponderrecipes",
            "responderreciperesource",
            "responderrecipesresource",
            "cloudguard",
        ]

    def get_module_resource_id_param(self):
        return "responder_recipe_id"

    def get_module_resource_id(self):
        return self.module.params.get("responder_recipe_id")

    def get_get_fn(self):
        return self.client.get_responder_recipe

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_responder_recipe, responder_recipe_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_responder_recipe,
            responder_recipe_id=self.module.params.get("responder_recipe_id"),
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
            self.client.list_responder_recipes, **kwargs
        )

    def get_create_model_class(self):
        return CreateResponderRecipeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_responder_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(create_responder_recipe_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateResponderRecipeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_responder_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                responder_recipe_id=self.module.params.get("responder_recipe_id"),
                update_responder_recipe_details=update_details,
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
            call_fn=self.client.delete_responder_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                responder_recipe_id=self.module.params.get("responder_recipe_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ResponderRecipeHelperCustom = get_custom_class("ResponderRecipeHelperCustom")


class ResourceHelper(ResponderRecipeHelperCustom, ResponderRecipeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            source_responder_recipe_id=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            responder_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    responder_rule_id=dict(type="str", required=True),
                    details=dict(
                        type="dict",
                        required=True,
                        options=dict(is_enabled=dict(type="bool", required=True)),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            responder_recipe_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="responder_recipe",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
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
