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
module: oci_cloud_guard_target_responder_recipe_facts
short_description: Fetches details about one or multiple TargetResponderRecipe resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TargetResponderRecipe resources in Oracle Cloud Infrastructure
    - Returns a list of all responder recipes associated with the target identified by targetId
    - If I(target_responder_recipe_id) is specified, the details of a single TargetResponderRecipe will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    target_responder_recipe_id:
        description:
            - OCID of TargetResponderRecipe
            - Required to get a specific target_responder_recipe.
        type: str
        aliases: ["id"]
    target_id:
        description:
            - OCID of target
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple target_responder_recipes.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - The field life cycle state. Only one state can be provided. Default value for state is active. If no value is specified state is active.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific target_responder_recipe
  oci_cloud_guard_target_responder_recipe_facts:
    # required
    target_responder_recipe_id: "ocid1.targetresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

- name: List target_responder_recipes
  oci_cloud_guard_target_responder_recipe_facts:
    # required
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
target_responder_recipes:
    description:
        - List of TargetResponderRecipe resources
    returned: on success
    type: complex
    contains:
        responder_rules:
            description:
                - "List of responder rules associated with the recipe - user input"
                - Returned for get operation
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
                - Returned for get operation
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
        id:
            description:
                - Unique identifier of TargetResponderRecipe that can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        responder_recipe_id:
            description:
                - Unique identifier for Responder Recipe of which this is an extension.
            returned: on success
            type: str
            sample: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
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
        lifecycle_state:
            description:
                - The current state of the Example.
                - Returned for list operation
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "responder_recipe_id": "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "owner": "CUSTOMER",
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
    from oci.cloud_guard import CloudGuardClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetResponderRecipeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "target_id",
            "target_responder_recipe_id",
        ]

    def get_required_params_for_list(self):
        return [
            "target_id",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_responder_recipe,
            target_id=self.module.params.get("target_id"),
            target_responder_recipe_id=self.module.params.get(
                "target_responder_recipe_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_target_responder_recipes,
            target_id=self.module.params.get("target_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TargetResponderRecipeFactsHelperCustom = get_custom_class(
    "TargetResponderRecipeFactsHelperCustom"
)


class ResourceFactsHelper(
    TargetResponderRecipeFactsHelperCustom, TargetResponderRecipeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            target_responder_recipe_id=dict(aliases=["id"], type="str"),
            target_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="target_responder_recipe",
        service_client_class=CloudGuardClient,
        namespace="cloud_guard",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(target_responder_recipes=result)


if __name__ == "__main__":
    main()
