#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_cloud_guard_target
short_description: Manage a Target resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Target resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Target
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - DetectorTemplate Identifier
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    compartment_id:
        description:
            - Compartment Identifier where the resource is created
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    description:
        description:
            - The target description.
        type: str
    target_resource_type:
        description:
            - possible type of targets(compartment/HCMCloud/ERPCloud)
            - Required for create using I(state=present).
        type: str
        choices:
            - "COMPARTMENT"
            - "ERPCLOUD"
            - "HCMCLOUD"
    target_resource_id:
        description:
            - Resource ID which the target uses to monitor
            - Required for create using I(state=present).
        type: str
    target_detector_recipes:
        description:
            - List of detector recipes to associate with target
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            detector_recipe_id:
                description:
                    - Identifier for DetectorRecipe.
                type: str
            detector_rules:
                description:
                    - Overrides to be applied to Detector Rule associated with the target
                type: list
                elements: dict
                suboptions:
                    detector_rule_id:
                        description:
                            - Identifier for DetectorRule.
                        type: str
                        required: true
                    details:
                        description:
                            - ""
                        type: dict
                        required: true
                        suboptions:
                            condition_groups:
                                description:
                                    - Condition group corresponding to each compartment
                                type: list
                                elements: dict
                                suboptions:
                                    compartment_id:
                                        description:
                                            - compartment associated with condition
                                        type: str
                                        required: true
                                    condition:
                                        description:
                                            - ""
                                        type: dict
                                        required: true
                                        suboptions:
                                            kind:
                                                description:
                                                    - Type of condition object
                                                type: str
                                                choices:
                                                    - "SIMPLE"
                                                    - "COMPOSITE"
                                                required: true
                                            parameter:
                                                description:
                                                    - parameter Key
                                                    - Applicable when kind is 'SIMPLE'
                                                type: str
                                            operator:
                                                description:
                                                    - type of operator
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
                                                    - Applicable when kind is 'SIMPLE'
                                                type: str
                                            value_type:
                                                description:
                                                    - type of value
                                                    - Applicable when kind is 'SIMPLE'
                                                type: str
                                                choices:
                                                    - "MANAGED"
                                                    - "CUSTOM"
                                            left_operand:
                                                description:
                                                    - ""
                                                    - Applicable when kind is 'COMPOSITE'
                                                type: dict
                                                suboptions:
                                                    kind:
                                                        description:
                                                            - Type of condition object
                                                        type: str
                                                        choices:
                                                            - "COMPOSITE"
                                                            - "SIMPLE"
                                                        required: true
                                            composite_operator:
                                                description:
                                                    - ""
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
                                                        type: str
                                                        choices:
                                                            - "COMPOSITE"
                                                            - "SIMPLE"
                                                        required: true
            target_detector_recipe_id:
                description:
                    - Identifier for DetectorRecipe.
                    - This parameter is updatable.
                type: str
    target_responder_recipes:
        description:
            - List of responder recipes to associate with target
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            responder_recipe_id:
                description:
                    - Identifier for ResponderRecipe.
                type: str
            responder_rules:
                description:
                    - Override responder rules associated with reponder recipe in a target.
                type: list
                elements: dict
                suboptions:
                    responder_rule_id:
                        description:
                            - Identifier for ResponderRule.
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
                                    kind:
                                        description:
                                            - Type of condition object
                                        type: str
                                        choices:
                                            - "SIMPLE"
                                            - "COMPOSITE"
                                        required: true
                                    parameter:
                                        description:
                                            - parameter Key
                                            - Applicable when kind is 'SIMPLE'
                                        type: str
                                    operator:
                                        description:
                                            - type of operator
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
                                            - Applicable when kind is 'SIMPLE'
                                        type: str
                                    value_type:
                                        description:
                                            - type of value
                                            - Applicable when kind is 'SIMPLE'
                                        type: str
                                        choices:
                                            - "MANAGED"
                                            - "CUSTOM"
                                    left_operand:
                                        description:
                                            - ""
                                            - Applicable when kind is 'COMPOSITE'
                                        type: dict
                                        suboptions:
                                            kind:
                                                description:
                                                    - Type of condition object
                                                type: str
                                                choices:
                                                    - "COMPOSITE"
                                                    - "SIMPLE"
                                                required: true
                                    composite_operator:
                                        description:
                                            - ""
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
                                        type: str
                                        required: true
                                    name:
                                        description:
                                            - configuration name
                                        type: str
                                        required: true
                                    value:
                                        description:
                                            - configuration value
                                        type: str
                                        required: true
                            mode:
                                description:
                                    - Execution Mode for ResponderRule
                                type: str
                                choices:
                                    - "AUTOACTION"
                                    - "USERACTION"
            target_responder_recipe_id:
                description:
                    - Identifier for ResponderRecipe.
                    - This parameter is updatable.
                type: str
    lifecycle_state:
        description:
            - The current state of the DetectorRule.
            - This parameter is updatable.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
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
    target_id:
        description:
            - OCID of target
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Target.
            - Use I(state=present) to create or update a Target.
            - Use I(state=absent) to delete a Target.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create target
  oci_cloud_guard_target:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    target_resource_type: COMPARTMENT
    target_resource_id: "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    target_detector_recipes:
    - # optional
      detector_recipe_id: "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
      detector_rules:
      - # required
        detector_rule_id: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
        details:
          # optional
          condition_groups:
          - # required
            compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
            condition:
              # required
              kind: SIMPLE

              # optional
              parameter: parameter_example
              operator: IN
              value: value_example
              value_type: MANAGED
      target_detector_recipe_id: "ocid1.targetdetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    target_responder_recipes:
    - # optional
      responder_recipe_id: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
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
      target_responder_recipe_id: "ocid1.targetresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update target
  oci_cloud_guard_target:
    # required
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    target_detector_recipes:
    - # optional
      detector_recipe_id: "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
      detector_rules:
      - # required
        detector_rule_id: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
        details:
          # optional
          condition_groups:
          - # required
            compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
            condition:
              # required
              kind: SIMPLE

              # optional
              parameter: parameter_example
              operator: IN
              value: value_example
              value_type: MANAGED
      target_detector_recipe_id: "ocid1.targetdetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    target_responder_recipes:
    - # optional
      responder_recipe_id: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
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
      target_responder_recipe_id: "ocid1.targetresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update target using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_guard_target:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    target_detector_recipes:
    - # optional
      detector_recipe_id: "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
      detector_rules:
      - # required
        detector_rule_id: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
        details:
          # optional
          condition_groups:
          - # required
            compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
            condition:
              # required
              kind: SIMPLE

              # optional
              parameter: parameter_example
              operator: IN
              value: value_example
              value_type: MANAGED
      target_detector_recipe_id: "ocid1.targetdetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    target_responder_recipes:
    - # optional
      responder_recipe_id: "ocid1.responderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
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
      target_responder_recipe_id: "ocid1.targetresponderrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete target
  oci_cloud_guard_target:
    # required
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete target using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_guard_target:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
target:
    description:
        - Details of the Target resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Target Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier where the resource is created
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The target description.
            returned: on success
            type: str
            sample: description_example
        target_resource_type:
            description:
                - possible type of targets
            returned: on success
            type: str
            sample: COMPARTMENT
        target_resource_id:
            description:
                - Resource ID which the target uses to monitor
            returned: on success
            type: str
            sample: "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx"
        recipe_count:
            description:
                - Total number of recipes attached to target
            returned: on success
            type: int
            sample: 56
        target_detector_recipes:
            description:
                - List of detector recipes associated with target
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - Ocid for detector recipe
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - DisplayName of detector recipe
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Detector recipe description
                    returned: on success
                    type: str
                    sample: description_example
                compartment_id:
                    description:
                        - compartmentId of detector recipe
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                detector_recipe_id:
                    description:
                        - Unique identifier for Detector Recipe of which this is an extension
                    returned: on success
                    type: str
                    sample: "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
                owner:
                    description:
                        - Owner of detector recipe
                    returned: on success
                    type: str
                    sample: CUSTOMER
                detector:
                    description:
                        - Type of detector
                    returned: on success
                    type: str
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
                            type: str
                            sample: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - displayName
                            returned: on success
                            type: str
                            sample: display_name_example
                        description:
                            description:
                                - Description for TargetDetectorRecipeDetectorRule
                            returned: on success
                            type: str
                            sample: description_example
                        recommendation:
                            description:
                                - Recommendation for TargetDetectorRecipeDetectorRule
                            returned: on success
                            type: str
                            sample: recommendation_example
                        detector:
                            description:
                                - detector for the rule
                            returned: on success
                            type: str
                            sample: IAAS_ACTIVITY_DETECTOR
                        service_type:
                            description:
                                - service type of the configuration to which the rule is applied
                            returned: on success
                            type: str
                            sample: service_type_example
                        resource_type:
                            description:
                                - resource type of the configuration to which the rule is applied
                            returned: on success
                            type: str
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
                                    type: str
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
                                        data_type:
                                            description:
                                                - configuration data type
                                            returned: on success
                                            type: str
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
                                                    type: str
                                                    sample: MANAGED
                                                managed_list_type:
                                                    description:
                                                        - type of the managed list
                                                    returned: on success
                                                    type: str
                                                    sample: managed_list_type_example
                                                value:
                                                    description:
                                                        - configuration value
                                                    returned: on success
                                                    type: str
                                                    sample: value_example
                                condition_groups:
                                    description:
                                        - Condition group corresponding to each compartment
                                    returned: on success
                                    type: complex
                                    contains:
                                        compartment_id:
                                            description:
                                                - compartment associated with condition
                                            returned: on success
                                            type: str
                                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                                                    type: str
                                                    sample: COMPOSITE
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
                        time_created:
                            description:
                                - The date and time the target detector recipe rule was created. Format defined by RFC3339.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_updated:
                            description:
                                - The date and time the target detector recipe rule was updated. Format defined by RFC3339.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        lifecycle_state:
                            description:
                                - The current state of the DetectorRule.
                            returned: on success
                            type: str
                            sample: CREATING
                        lifecycle_details:
                            description:
                                - A message describing the current state in more detail. For example, can be used to provide actionable information for a
                                  resource in Failed state.
                            returned: on success
                            type: str
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
                            type: str
                            sample: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - displayName
                            returned: on success
                            type: str
                            sample: display_name_example
                        description:
                            description:
                                - Description for TargetDetectorRecipeDetectorRule
                            returned: on success
                            type: str
                            sample: description_example
                        recommendation:
                            description:
                                - Recommendation for TargetDetectorRecipeDetectorRule
                            returned: on success
                            type: str
                            sample: recommendation_example
                        detector:
                            description:
                                - detector for the rule
                            returned: on success
                            type: str
                            sample: IAAS_ACTIVITY_DETECTOR
                        service_type:
                            description:
                                - service type of the configuration to which the rule is applied
                            returned: on success
                            type: str
                            sample: service_type_example
                        resource_type:
                            description:
                                - resource type of the configuration to which the rule is applied
                            returned: on success
                            type: str
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
                                    type: str
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
                                        data_type:
                                            description:
                                                - configuration data type
                                            returned: on success
                                            type: str
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
                                                    type: str
                                                    sample: MANAGED
                                                managed_list_type:
                                                    description:
                                                        - type of the managed list
                                                    returned: on success
                                                    type: str
                                                    sample: managed_list_type_example
                                                value:
                                                    description:
                                                        - configuration value
                                                    returned: on success
                                                    type: str
                                                    sample: value_example
                                condition_groups:
                                    description:
                                        - Condition group corresponding to each compartment
                                    returned: on success
                                    type: complex
                                    contains:
                                        compartment_id:
                                            description:
                                                - compartment associated with condition
                                            returned: on success
                                            type: str
                                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
                                                    type: str
                                                    sample: COMPOSITE
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
                        time_created:
                            description:
                                - The date and time the target detector recipe rule was created. Format defined by RFC3339.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_updated:
                            description:
                                - The date and time the target detector recipe rule was updated. Format defined by RFC3339.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        lifecycle_state:
                            description:
                                - The current state of the DetectorRule.
                            returned: on success
                            type: str
                            sample: CREATING
                        lifecycle_details:
                            description:
                                - A message describing the current state in more detail. For example, can be used to provide actionable information for a
                                  resource in Failed state.
                            returned: on success
                            type: str
                            sample: lifecycle_details_example
                time_created:
                    description:
                        - The date and time the target detector recipe was created. Format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The date and time the target detector recipe was updated. Format defined by RFC3339.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_state:
                    description:
                        - The current state of the resource.
                    returned: on success
                    type: str
                    sample: CREATING
        target_responder_recipes:
            description:
                - List of responder recipes associated with target
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - Unique identifier of TargetResponderRecipe that is immutable on creation
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                responder_recipe_id:
                    description:
                        - Unique identifier for Responder Recipe of which this is an extension
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
                        - ResponderRecipe Identifier Name
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - ResponderRecipe Description
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
                                - Identifier for ResponderRule.
                            returned: on success
                            type: str
                            sample: "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - ResponderRule Display Name
                            returned: on success
                            type: str
                            sample: display_name_example
                        description:
                            description:
                                - ResponderRule Description
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
                                        kind:
                                            description:
                                                - Type of condition object
                                            returned: on success
                                            type: str
                                            sample: COMPOSITE
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
                                - A message describing the current state in more detail. For example, can be used to provide actionable information for a
                                  resource in Failed state.
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
                                - Identifier for ResponderRule.
                            returned: on success
                            type: str
                            sample: "ocid1.responderrule.oc1..xxxxxxEXAMPLExxxxxx"
                        display_name:
                            description:
                                - ResponderRule Display Name
                            returned: on success
                            type: str
                            sample: display_name_example
                        description:
                            description:
                                - ResponderRule Description
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
                                        kind:
                                            description:
                                                - Type of condition object
                                            returned: on success
                                            type: str
                                            sample: COMPOSITE
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
                                - A message describing the current state in more detail. For example, can be used to provide actionable information for a
                                  resource in Failed state.
                            returned: on success
                            type: str
                            sample: lifecycle_details_example
        inherited_by_compartments:
            description:
                - List of inherited compartments
            returned: on success
            type: list
            sample: []
        time_created:
            description:
                - The date and time the target was created. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the target was updated. Format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Target.
            returned: on success
            type: str
            sample: CREATING
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecyle_details_example
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "target_resource_type": "COMPARTMENT",
        "target_resource_id": "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx",
        "recipe_count": 56,
        "target_detector_recipes": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example",
            "description": "description_example",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "detector_recipe_id": "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx",
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
                    "condition_groups": [{
                        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                        "condition": {
                            "kind": "COMPOSITE",
                            "left_operand": {
                                "kind": "COMPOSITE"
                            },
                            "composite_operator": "AND",
                            "right_operand": {
                                "kind": "COMPOSITE"
                            },
                            "parameter": "parameter_example",
                            "operator": "IN",
                            "value": "value_example",
                            "value_type": "MANAGED"
                        }
                    }],
                    "labels": [],
                    "is_configuration_allowed": true
                },
                "managed_list_types": [],
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
                    "condition_groups": [{
                        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                        "condition": {
                            "kind": "COMPOSITE",
                            "left_operand": {
                                "kind": "COMPOSITE"
                            },
                            "composite_operator": "AND",
                            "right_operand": {
                                "kind": "COMPOSITE"
                            },
                            "parameter": "parameter_example",
                            "operator": "IN",
                            "value": "value_example",
                            "value_type": "MANAGED"
                        }
                    }],
                    "labels": [],
                    "is_configuration_allowed": true
                },
                "managed_list_types": [],
                "time_created": "2013-10-20T19:20:30+01:00",
                "time_updated": "2013-10-20T19:20:30+01:00",
                "lifecycle_state": "CREATING",
                "lifecycle_details": "lifecycle_details_example"
            }],
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING"
        }],
        "target_responder_recipes": [{
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
                        "kind": "COMPOSITE",
                        "left_operand": {
                            "kind": "COMPOSITE"
                        },
                        "composite_operator": "AND",
                        "right_operand": {
                            "kind": "COMPOSITE"
                        },
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
                        "kind": "COMPOSITE",
                        "left_operand": {
                            "kind": "COMPOSITE"
                        },
                        "composite_operator": "AND",
                        "right_operand": {
                            "kind": "COMPOSITE"
                        },
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
        }],
        "inherited_by_compartments": [],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.cloud_guard import CloudGuardClient
    from oci.cloud_guard.models import CreateTargetDetails
    from oci.cloud_guard.models import UpdateTargetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(TargetHelperGen, self).get_possible_entity_types() + [
            "cloudguardtarget",
            "cloudguardtargets",
            "cloudGuardcloudguardtarget",
            "cloudGuardcloudguardtargets",
            "cloudguardtargetresource",
            "cloudguardtargetsresource",
            "target",
            "targets",
            "cloudGuardtarget",
            "cloudGuardtargets",
            "targetresource",
            "targetsresource",
            "cloudguard",
        ]

    def get_module_resource_id_param(self):
        return "target_id"

    def get_module_resource_id(self):
        return self.module.params.get("target_id")

    def get_get_fn(self):
        return self.client.get_target

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_target, target_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target, target_id=self.module.params.get("target_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "lifecycle_state"]
        )

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
        return oci_common_utils.list_all_resources(self.client.list_targets, **kwargs)

    def get_create_model_class(self):
        return CreateTargetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_target,
            call_fn_args=(),
            call_fn_kwargs=dict(create_target_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTargetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_target,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                update_target_details=update_details,
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
            call_fn=self.client.delete_target,
            call_fn_args=(),
            call_fn_kwargs=dict(target_id=self.module.params.get("target_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


TargetHelperCustom = get_custom_class("TargetHelperCustom")


class ResourceHelper(TargetHelperCustom, TargetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            description=dict(type="str"),
            target_resource_type=dict(
                type="str", choices=["COMPARTMENT", "ERPCLOUD", "HCMCLOUD"]
            ),
            target_resource_id=dict(type="str"),
            target_detector_recipes=dict(
                type="list",
                elements="dict",
                options=dict(
                    detector_recipe_id=dict(type="str"),
                    detector_rules=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            detector_rule_id=dict(type="str", required=True),
                            details=dict(
                                type="dict",
                                required=True,
                                options=dict(
                                    condition_groups=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            compartment_id=dict(
                                                type="str", required=True
                                            ),
                                            condition=dict(
                                                type="dict",
                                                required=True,
                                                options=dict(
                                                    kind=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=["SIMPLE", "COMPOSITE"],
                                                    ),
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
                                                        type="str",
                                                        choices=["MANAGED", "CUSTOM"],
                                                    ),
                                                    left_operand=dict(
                                                        type="dict",
                                                        options=dict(
                                                            kind=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "COMPOSITE",
                                                                    "SIMPLE",
                                                                ],
                                                            )
                                                        ),
                                                    ),
                                                    composite_operator=dict(
                                                        type="str",
                                                        choices=["AND", "OR"],
                                                    ),
                                                    right_operand=dict(
                                                        type="dict",
                                                        options=dict(
                                                            kind=dict(
                                                                type="str",
                                                                required=True,
                                                                choices=[
                                                                    "COMPOSITE",
                                                                    "SIMPLE",
                                                                ],
                                                            )
                                                        ),
                                                    ),
                                                ),
                                            ),
                                        ),
                                    )
                                ),
                            ),
                        ),
                    ),
                    target_detector_recipe_id=dict(type="str"),
                ),
            ),
            target_responder_recipes=dict(
                type="list",
                elements="dict",
                options=dict(
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
                                            kind=dict(
                                                type="str",
                                                required=True,
                                                choices=["SIMPLE", "COMPOSITE"],
                                            ),
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
                                                type="str",
                                                choices=["MANAGED", "CUSTOM"],
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
                                    mode=dict(
                                        type="str", choices=["AUTOACTION", "USERACTION"]
                                    ),
                                ),
                            ),
                        ),
                    ),
                    target_responder_recipe_id=dict(type="str"),
                ),
            ),
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
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            target_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target",
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
