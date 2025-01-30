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
module: oci_cloud_guard_target_detector_recipe
short_description: Manage a TargetDetectorRecipe resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a TargetDetectorRecipe resource in Oracle Cloud Infrastructure
    - For I(state=present), attach a DetectorRecipe with the Target
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    detector_recipe_id:
        description:
            - DetectorRecipe Identifier
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    is_validation_only_query:
        description:
            - When enabled, validation is performed for attaching the detector recipe.
            - This parameter is updatable.
        type: bool
    detector_rules:
        description:
            - Update detector rules associated with detector recipe in a target.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            detector_rule_id:
                description:
                    - Identifier for DetectorRule.
                    - This parameter is updatable.
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
                                    - This parameter is updatable.
                                type: str
                                required: true
                            condition:
                                description:
                                    - ""
                                type: dict
                                required: true
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
    target_id:
        description:
            - OCID of target
        type: str
        required: true
    target_detector_recipe_id:
        description:
            - OCID of TargetDetectorRecipe
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
            - The state of the TargetDetectorRecipe.
            - Use I(state=present) to create or update a TargetDetectorRecipe.
            - Use I(state=absent) to delete a TargetDetectorRecipe.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create target_detector_recipe
  oci_cloud_guard_target_detector_recipe:
    # required
    detector_recipe_id: "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update target_detector_recipe
  oci_cloud_guard_target_detector_recipe:
    # required
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    target_detector_recipe_id: "ocid1.targetdetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    detector_recipe_id: "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    is_validation_only_query: true
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

- name: Delete target_detector_recipe
  oci_cloud_guard_target_detector_recipe:
    # required
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"
    target_detector_recipe_id: "ocid1.targetdetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
target_detector_recipe:
    description:
        - Details of the TargetDetectorRecipe resource acted upon by the current operation
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
                - Display name of detector recipe.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Detector recipe description.
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
                        - The unique identifier of the detector rule.
                    returned: on success
                    type: str
                    sample: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Display name for TargetDetectorRecipeDetectorRule. information.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description for TargetDetectorRecipeDetectorRule. information.
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
                        problem_threshold:
                            description:
                                - Cutover point for an elevated resource Risk Score to create a Problem
                            returned: on success
                            type: int
                            sample: 56
                        target_types:
                            description:
                                - List of target types for which the detector rule is applicable
                            returned: on success
                            type: list
                            sample: []
                        sighting_types:
                            description:
                                - List of sighting types
                            returned: on success
                            type: complex
                            contains:
                                id:
                                    description:
                                        - The unique identifier of sighting type
                                    returned: on success
                                    type: str
                                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                                display_name:
                                    description:
                                        - Name of the sighting type
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                description:
                                    description:
                                        - Description of the sighting type
                                    returned: on success
                                    type: str
                                    sample: description_example
                                mitre_link:
                                    description:
                                        - Link of the sighting type
                                    returned: on success
                                    type: str
                                    sample: mitre_link_example
                                tactic:
                                    description:
                                        - Mitre Att&ck tactic
                                    returned: on success
                                    type: str
                                    sample: tactic_example
                                techniques:
                                    description:
                                        - List of Mitre Att&ck Techniques
                                    returned: on success
                                    type: list
                                    sample: []
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
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                data_source_id:
                    description:
                        - The id of the attached DataSource.
                    returned: on success
                    type: str
                    sample: "ocid1.datasource.oc1..xxxxxxEXAMPLExxxxxx"
                entities_mappings:
                    description:
                        - Data Source entities mapping for a Detector Rule
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - The display name of entity
                            returned: on success
                            type: str
                            sample: display_name_example
                        query_field:
                            description:
                                - The entity value mapped to a data source query
                            returned: on success
                            type: str
                            sample: query_field_example
                        entity_type:
                            description:
                                - Possible type of entity
                            returned: on success
                            type: str
                            sample: EXTERNAL_IP
        effective_detector_rules:
            description:
                - List of effective detector rules for the detector type for recipe after applying defaults
            returned: on success
            type: complex
            contains:
                detector_rule_id:
                    description:
                        - The unique identifier of the detector rule.
                    returned: on success
                    type: str
                    sample: "ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - Display name for TargetDetectorRecipeDetectorRule. information.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description for TargetDetectorRecipeDetectorRule. information.
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
                        problem_threshold:
                            description:
                                - Cutover point for an elevated resource Risk Score to create a Problem
                            returned: on success
                            type: int
                            sample: 56
                        target_types:
                            description:
                                - List of target types for which the detector rule is applicable
                            returned: on success
                            type: list
                            sample: []
                        sighting_types:
                            description:
                                - List of sighting types
                            returned: on success
                            type: complex
                            contains:
                                id:
                                    description:
                                        - The unique identifier of sighting type
                                    returned: on success
                                    type: str
                                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                                display_name:
                                    description:
                                        - Name of the sighting type
                                    returned: on success
                                    type: str
                                    sample: display_name_example
                                description:
                                    description:
                                        - Description of the sighting type
                                    returned: on success
                                    type: str
                                    sample: description_example
                                mitre_link:
                                    description:
                                        - Link of the sighting type
                                    returned: on success
                                    type: str
                                    sample: mitre_link_example
                                tactic:
                                    description:
                                        - Mitre Att&ck tactic
                                    returned: on success
                                    type: str
                                    sample: tactic_example
                                techniques:
                                    description:
                                        - List of Mitre Att&ck Techniques
                                    returned: on success
                                    type: list
                                    sample: []
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
                        - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                data_source_id:
                    description:
                        - The id of the attached DataSource.
                    returned: on success
                    type: str
                    sample: "ocid1.datasource.oc1..xxxxxxEXAMPLExxxxxx"
                entities_mappings:
                    description:
                        - Data Source entities mapping for a Detector Rule
                    returned: on success
                    type: complex
                    contains:
                        display_name:
                            description:
                                - The display name of entity
                            returned: on success
                            type: str
                            sample: display_name_example
                        query_field:
                            description:
                                - The entity value mapped to a data source query
                            returned: on success
                            type: str
                            sample: query_field_example
                        entity_type:
                            description:
                                - Possible type of entity
                            returned: on success
                            type: str
                            sample: EXTERNAL_IP
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
        source_data_retention:
            description:
                - The number of days for which source data is retained
            returned: on success
            type: int
            sample: 56
    sample: {
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
                    }
                }],
                "labels": [],
                "is_configuration_allowed": true,
                "problem_threshold": 56,
                "target_types": [],
                "sighting_types": [{
                    "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                    "display_name": "display_name_example",
                    "description": "description_example",
                    "mitre_link": "mitre_link_example",
                    "tactic": "tactic_example",
                    "techniques": []
                }]
            },
            "managed_list_types": [],
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example",
            "data_source_id": "ocid1.datasource.oc1..xxxxxxEXAMPLExxxxxx",
            "entities_mappings": [{
                "display_name": "display_name_example",
                "query_field": "query_field_example",
                "entity_type": "EXTERNAL_IP"
            }]
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
                    }
                }],
                "labels": [],
                "is_configuration_allowed": true,
                "problem_threshold": 56,
                "target_types": [],
                "sighting_types": [{
                    "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                    "display_name": "display_name_example",
                    "description": "description_example",
                    "mitre_link": "mitre_link_example",
                    "tactic": "tactic_example",
                    "techniques": []
                }]
            },
            "managed_list_types": [],
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example",
            "data_source_id": "ocid1.datasource.oc1..xxxxxxEXAMPLExxxxxx",
            "entities_mappings": [{
                "display_name": "display_name_example",
                "query_field": "query_field_example",
                "entity_type": "EXTERNAL_IP"
            }]
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "source_data_retention": 56
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
    from oci.cloud_guard.models import AttachTargetDetectorRecipeDetails
    from oci.cloud_guard.models import UpdateTargetDetectorRecipeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetDetectorRecipeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            TargetDetectorRecipeHelperGen, self
        ).get_possible_entity_types() + [
            "cloudguardtarget",
            "cloudguardtargets",
            "cloudGuardcloudguardtarget",
            "cloudGuardcloudguardtargets",
            "cloudguardtargetresource",
            "cloudguardtargetsresource",
            "targetdetectorrecipe",
            "targetdetectorrecipes",
            "cloudGuardtargetdetectorrecipe",
            "cloudGuardtargetdetectorrecipes",
            "targetdetectorreciperesource",
            "targetdetectorrecipesresource",
            "cloudguard",
        ]

    def get_module_resource_id_param(self):
        return "target_detector_recipe_id"

    def get_module_resource_id(self):
        return self.module.params.get("target_detector_recipe_id")

    def get_get_fn(self):
        return self.client.get_target_detector_recipe

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_detector_recipe,
            target_detector_recipe_id=summary_model.id,
            target_id=self.module.params.get("target_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_detector_recipe,
            target_id=self.module.params.get("target_id"),
            target_detector_recipe_id=self.module.params.get(
                "target_detector_recipe_id"
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
            self.client.list_target_detector_recipes, **kwargs
        )

    def get_create_model_class(self):
        return AttachTargetDetectorRecipeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_target_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                attach_target_detector_recipe_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateTargetDetectorRecipeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_target_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                target_detector_recipe_id=self.module.params.get(
                    "target_detector_recipe_id"
                ),
                update_target_detector_recipe_details=update_details,
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
            call_fn=self.client.delete_target_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                target_id=self.module.params.get("target_id"),
                target_detector_recipe_id=self.module.params.get(
                    "target_detector_recipe_id"
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


TargetDetectorRecipeHelperCustom = get_custom_class("TargetDetectorRecipeHelperCustom")


class ResourceHelper(TargetDetectorRecipeHelperCustom, TargetDetectorRecipeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            detector_recipe_id=dict(type="str"),
            is_validation_only_query=dict(type="bool"),
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
                                    compartment_id=dict(type="str", required=True),
                                    condition=dict(
                                        type="dict",
                                        required=True,
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
                                                type="str",
                                                choices=["MANAGED", "CUSTOM"],
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
                                ),
                            )
                        ),
                    ),
                ),
            ),
            target_id=dict(type="str", required=True),
            target_detector_recipe_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="target_detector_recipe",
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
