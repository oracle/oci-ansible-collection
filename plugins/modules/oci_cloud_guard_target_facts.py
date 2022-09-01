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
module: oci_cloud_guard_target_facts
short_description: Fetches details about one or multiple Target resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Target resources in Oracle Cloud Infrastructure
    - Returns a list of all Targets in a compartment
      The ListTargets operation returns only the targets in `compartmentId` passed.
      The list does not include any subcompartments of the compartmentId passed.
    - The parameter `accessLevel` specifies whether to return only those compartments for which the
      requestor has INSPECT permissions on at least one resource directly
      or indirectly (ACCESSIBLE) (the resource can be in a subcompartment) or to return Not Authorized if
      Principal doesn't have access to even one of the child compartments. This is valid only when
      `compartmentIdInSubtree` is set to `true`.
    - The parameter `compartmentIdInSubtree` applies when you perform ListTargets on the
      `compartmentId` passed and when it is set to true, the entire hierarchy of compartments can be returned.
      To get a full list of all compartments and subcompartments in the tenancy (root compartment),
      set the parameter `compartmentIdInSubtree` to true and `accessLevel` to ACCESSIBLE.
    - If I(target_id) is specified, the details of a single Target will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    target_id:
        description:
            - OCID of target
            - Required to get a specific target.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple targets.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    is_non_security_zone_targets_only_query:
        description:
            - Default is false.
              When set to true, only the targets that would be deleted as part of
              security zone creation will be returned.
        type: bool
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
- name: Get a specific target
  oci_cloud_guard_target_facts:
    # required
    target_id: "ocid1.target.oc1..xxxxxxEXAMPLExxxxxx"

- name: List targets
  oci_cloud_guard_target_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    is_non_security_zone_targets_only_query: true
    lifecycle_state: CREATING
    compartment_id_in_subtree: true
    access_level: RESTRICTED
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
targets:
    description:
        - List of Target resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - The target description.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        target_detector_recipes:
            description:
                - List of detector recipes associated with target
                - Returned for get operation
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
                                - A message describing the current state in more detail. For example, can be used to provide actionable information for a
                                  resource in Failed state.
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
                                - A message describing the current state in more detail. For example, can be used to provide actionable information for a
                                  resource in Failed state.
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
        target_responder_recipes:
            description:
                - List of responder recipes associated with target
                - Returned for get operation
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
                                - A message describing the current state in more detail. For example, can be used to provide actionable information for a
                                  resource in Failed state.
                            returned: on success
                            type: str
                            sample: lifecycle_details_example
        target_details:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                target_resource_type:
                    description:
                        - Possible type of targets.
                    returned: on success
                    type: str
                    sample: COMPARTMENT
                security_zone_id:
                    description:
                        - The OCID of the security zone to associate this compartment with.
                    returned: on success
                    type: str
                    sample: "ocid1.securityzone.oc1..xxxxxxEXAMPLExxxxxx"
                security_zone_display_name:
                    description:
                        - The name of the security zone to associate this compartment with.
                    returned: on success
                    type: str
                    sample: security_zone_display_name_example
                target_security_zone_recipes:
                    description:
                        - The list of security zone recipes to associate this compartment with.
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
                                - The recipe's name
                            returned: on success
                            type: str
                            sample: display_name_example
                        description:
                            description:
                                - The recipe's description
                            returned: on success
                            type: str
                            sample: description_example
                        compartment_id:
                            description:
                                - The id of the compartment that contains the recipe
                            returned: on success
                            type: str
                            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                        owner:
                            description:
                                - The owner of the recipe
                            returned: on success
                            type: str
                            sample: CUSTOMER
                        security_policies:
                            description:
                                - The list of `SecurityPolicy` ids that are included in the recipe
                            returned: on success
                            type: list
                            sample: []
                        time_created:
                            description:
                                - The time the recipe was created. An RFC3339 formatted datetime string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_updated:
                            description:
                                - The time the recipe was last updated. An RFC3339 formatted datetime string.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        lifecycle_state:
                            description:
                                - The current state of the recipe
                            returned: on success
                            type: str
                            sample: CREATING
                        lifecycle_details:
                            description:
                                - A message describing the current state in more detail. For example, this can be used to provide actionable information for a
                                  recipe in the `Failed` state.
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
        inherited_by_compartments:
            description:
                - List of inherited compartments
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Target display name, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier where the resource is created
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
        "description": "description_example",
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
        }],
        "target_details": {
            "target_resource_type": "COMPARTMENT",
            "security_zone_id": "ocid1.securityzone.oc1..xxxxxxEXAMPLExxxxxx",
            "security_zone_display_name": "security_zone_display_name_example",
            "target_security_zone_recipes": [{
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "display_name": "display_name_example",
                "description": "description_example",
                "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
                "owner": "CUSTOMER",
                "security_policies": [],
                "time_created": "2013-10-20T19:20:30+01:00",
                "time_updated": "2013-10-20T19:20:30+01:00",
                "lifecycle_state": "CREATING",
                "lifecycle_details": "lifecycle_details_example",
                "freeform_tags": {'Department': 'Finance'},
                "defined_tags": {'Operations': {'CostCenter': 'US'}},
                "system_tags": {}
            }]
        },
        "inherited_by_compartments": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "target_resource_type": "COMPARTMENT",
        "target_resource_id": "ocid1.targetresource.oc1..xxxxxxEXAMPLExxxxxx",
        "recipe_count": 56,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecyle_details": "lifecyle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.cloud_guard import CloudGuardClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TargetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "target_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_target, target_id=self.module.params.get("target_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "is_non_security_zone_targets_only_query",
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
            self.client.list_targets,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TargetFactsHelperCustom = get_custom_class("TargetFactsHelperCustom")


class ResourceFactsHelper(TargetFactsHelperCustom, TargetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            target_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            is_non_security_zone_targets_only_query=dict(type="bool"),
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

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="target",
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

    module.exit_json(targets=result)


if __name__ == "__main__":
    main()
