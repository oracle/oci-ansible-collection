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
module: oci_cloud_guard_responder_recipe_facts
short_description: Fetches details about one or multiple ResponderRecipe resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ResponderRecipe resources in Oracle Cloud Infrastructure
    - Returns a list of all ResponderRecipes in a compartment
      The ListResponderRecipe operation returns only the targets in `compartmentId` passed.
      The list does not include any subcompartments of the compartmentId passed.
    - The parameter `accessLevel` specifies whether to return only those compartments for which the
      requestor has INSPECT permissions on at least one resource directly
      or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if
      Principal doesn't have access to even one of the child compartments. This is valid only when
      `compartmentIdInSubtree` is set to `true`.
    - The parameter `compartmentIdInSubtree` applies when you perform ListResponderRecipe on the
      `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned.
      To get a full list of all compartments and subcompartments in the tenancy (root compartment),
      set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.
    - If I(responder_recipe_id) is specified, the details of a single ResponderRecipe will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    responder_recipe_id:
        description:
            - OCID of ResponderRecipe
            - Required to get a specific responder_recipe.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple responder_recipes.
        type: str
    resource_metadata_only:
        description:
            - Default is false.
              When set to true, the list of all Oracle Managed Resources
              Metadata supported by Cloud Guard are returned.
        type: bool
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
    compartment_id_in_subtree:
        description:
            - Default is false.
              When set to true, the hierarchy of compartments is traversed
              and all compartments and subcompartments in the tenancy are
              returned depending on the the setting of `accessLevel`.
        type: bool
    access_level:
        description:
            - Valid values are `RESTRICTED` and `ACCESSIBLE`. Default is `RESTRICTED`.
              Setting this to `ACCESSIBLE` returns only those compartments for which the
              user has INSPECT permissions directly or indirectly (permissions can be on a
              resource in a subcompartment).
              When set to `RESTRICTED` permissions are checked and no partial results are displayed.
        type: str
        choices:
            - "RESTRICTED"
            - "ACCESSIBLE"
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
- name: Get a specific responder_recipe
  oci_cloud_guard_responder_recipe_facts:
    # required
    responder_recipe_id: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"

- name: List responder_recipes
  oci_cloud_guard_responder_recipe_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    resource_metadata_only: true
    display_name: display_name_example
    lifecycle_state: CREATING
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
responder_recipes:
    description:
        - List of ResponderRecipe resources
    returned: on success
    type: complex
    contains:
        effective_responder_rules:
            description:
                - List of responder rules associated with the recipe
                - Returned for get operation
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
    sample: [{
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
        "source_responder_recipe_id": "ocid1.sourceresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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


class ResponderRecipeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "responder_recipe_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_responder_recipe,
            responder_recipe_id=self.module.params.get("responder_recipe_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "resource_metadata_only",
            "display_name",
            "lifecycle_state",
            "compartment_id_in_subtree",
            "access_level",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_responder_recipes,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ResponderRecipeFactsHelperCustom = get_custom_class("ResponderRecipeFactsHelperCustom")


class ResourceFactsHelper(
    ResponderRecipeFactsHelperCustom, ResponderRecipeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            responder_recipe_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            resource_metadata_only=dict(type="bool"),
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
            compartment_id_in_subtree=dict(type="bool"),
            access_level=dict(type="str", choices=["RESTRICTED", "ACCESSIBLE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="responder_recipe",
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

    module.exit_json(responder_recipes=result)


if __name__ == "__main__":
    main()
