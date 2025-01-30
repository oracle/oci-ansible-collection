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
module: oci_cloud_guard_target_detector_recipe_facts
short_description: Fetches details about one or multiple TargetDetectorRecipe resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TargetDetectorRecipe resources in Oracle Cloud Infrastructure
    - Returns a list of all detector recipes associated with the target identified by targetId
    - If I(target_detector_recipe_id) is specified, the details of a single TargetDetectorRecipe will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    target_detector_recipe_id:
        description:
            - OCID of TargetDetectorRecipe
            - Required to get a specific target_detector_recipe.
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
            - Required to list multiple target_detector_recipes.
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
- name: Get a specific target_detector_recipe
  oci_cloud_guard_target_detector_recipe_facts:
    # required
    target_detector_recipe_id: "ocid1.targetdetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

- name: List target_detector_recipes
  oci_cloud_guard_target_detector_recipe_facts:
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
target_detector_recipes:
    description:
        - List of TargetDetectorRecipe resources
    returned: on success
    type: complex
    contains:
        detector_rules:
            description:
                - "List of detector rules for the detector type for recipe - user input"
                - Returned for get operation
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
                - Returned for get operation
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
        id:
            description:
                - Ocid for detector recipe
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - compartmentId of detector recipe
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        owner:
            description:
                - Owner of detector recipe
            returned: on success
            type: str
            sample: CUSTOMER
        detector_recipe_id:
            description:
                - Unique identifier for Detector Recipe of which this is an extension
            returned: on success
            type: str
            sample: "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx"
        detector:
            description:
                - Type of detector
            returned: on success
            type: str
            sample: IAAS_ACTIVITY_DETECTOR
        lifecycle_state:
            description:
                - The current state of the resource.
            returned: on success
            type: str
            sample: CREATING
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
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        source_data_retention:
            description:
                - The number of days for which source data is retained
            returned: on success
            type: int
            sample: 56
    sample: [{
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "owner": "CUSTOMER",
        "detector_recipe_id": "ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx",
        "detector": "IAAS_ACTIVITY_DETECTOR",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "source_data_retention": 56
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


class TargetDetectorRecipeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "target_id",
            "target_detector_recipe_id",
        ]

    def get_required_params_for_list(self):
        return [
            "target_id",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target_detector_recipe,
            target_id=self.module.params.get("target_id"),
            target_detector_recipe_id=self.module.params.get(
                "target_detector_recipe_id"
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
            self.client.list_target_detector_recipes,
            target_id=self.module.params.get("target_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TargetDetectorRecipeFactsHelperCustom = get_custom_class(
    "TargetDetectorRecipeFactsHelperCustom"
)


class ResourceFactsHelper(
    TargetDetectorRecipeFactsHelperCustom, TargetDetectorRecipeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            target_detector_recipe_id=dict(aliases=["id"], type="str"),
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
        resource_type="target_detector_recipe",
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

    module.exit_json(target_detector_recipes=result)


if __name__ == "__main__":
    main()
