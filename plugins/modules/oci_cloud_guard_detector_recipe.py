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
module: oci_cloud_guard_detector_recipe
short_description: Manage a DetectorRecipe resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DetectorRecipe resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a DetectorRecipe
version_added: "2.9"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - DetectorRecipe Display Name
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - DetectorRecipe Description
            - This parameter is updatable.
        type: str
    source_detector_recipe_id:
        description:
            - The id of the source detector recipe.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    detector_rules:
        description:
            - Detector Rules to override from source detector recipe
            - This parameter is updatable.
        type: list
        suboptions:
            detector_rule_id:
                description:
                    - DetectorRecipeRule Identifier
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
                            - Enables the control
                        type: bool
                        required: true
                    risk_level:
                        description:
                            - The Risk Level
                        type: str
                        choices:
                            - "CRITICAL"
                            - "HIGH"
                            - "MEDIUM"
                            - "LOW"
                            - "MINOR"
                        required: true
                    configurations:
                        description:
                            - Configuration details
                        type: list
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
                            data_type:
                                description:
                                    - configuration data type
                                type: str
                            values:
                                description:
                                    - List of configuration values
                                type: list
                                suboptions:
                                    list_type:
                                        description:
                                            - configuration list item type, either CUSTOM or MANAGED
                                        type: str
                                        choices:
                                            - "MANAGED"
                                            - "CUSTOM"
                                        required: true
                                    managed_list_type:
                                        description:
                                            - type of the managed list
                                        type: str
                                        required: true
                                    value:
                                        description:
                                            - configuration value
                                        type: str
                                        required: true
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
                    labels:
                        description:
                            - user defined labels for a detector rule
                        type: list
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
    detector_recipe_id:
        description:
            - DetectorRecipe OCID
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DetectorRecipe.
            - Use I(state=present) to create or update a DetectorRecipe.
            - Use I(state=absent) to delete a DetectorRecipe.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create detector_recipe
  oci_cloud_guard_detector_recipe:
    display_name: display_name_example
    source_detector_recipe_id: ocid1.sourcedetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Update detector_recipe using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_guard_detector_recipe:
    display_name: display_name_example
    description: description_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    detector_rules:
    - detector_rule_id: ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx
      details:
        is_enabled: true
        risk_level: CRITICAL
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update detector_recipe
  oci_cloud_guard_detector_recipe:
    display_name: display_name_example
    description: description_example
    detector_recipe_id: ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete detector_recipe
  oci_cloud_guard_detector_recipe:
    detector_recipe_id: ocid1.detectorrecipe.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

- name: Delete detector_recipe using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_guard_detector_recipe:
    display_name: display_name_example
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

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
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        source_detector_recipe_id:
            description:
                - Recipe Ocid of the Source Recipe to be cloned
            returned: on success
            type: string
            sample: ocid1.sourcedetectorrecipe.oc1..xxxxxxEXAMPLExxxxxx
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
                - List of detetor rules for the detector type for recipe
            returned: on success
            type: complex
            contains:
                detector_rule_id:
                    description:
                        - The unique identifier of the detector rule
                    returned: on success
                    type: string
                    sample: ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx
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
                                            type: dict
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
                                            type: dict
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
                            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
                - List of detetor rules for the detector type for recipe
            returned: on success
            type: complex
            contains:
                detector_rule_id:
                    description:
                        - The unique identifier of the detector rule
                    returned: on success
                    type: string
                    sample: ocid1.detectorrule.oc1..xxxxxxEXAMPLExxxxxx
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
                                            type: dict
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
                                            type: dict
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
                            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.cloud_guard import CloudGuardClient
    from oci.cloud_guard.models import CreateDetectorRecipeDetails
    from oci.cloud_guard.models import UpdateDetectorRecipeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetectorRecipeHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
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
            self.client.list_detector_recipes, **kwargs
        )

    def get_create_model_class(self):
        return CreateDetectorRecipeDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(create_detector_recipe_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDetectorRecipeDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detector_recipe_id=self.module.params.get("detector_recipe_id"),
                update_detector_recipe_details=update_details,
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
            call_fn=self.client.delete_detector_recipe,
            call_fn_args=(),
            call_fn_kwargs=dict(
                detector_recipe_id=self.module.params.get("detector_recipe_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DetectorRecipeHelperCustom = get_custom_class("DetectorRecipeHelperCustom")


class ResourceHelper(DetectorRecipeHelperCustom, DetectorRecipeHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            source_detector_recipe_id=dict(type="str"),
            compartment_id=dict(type="str"),
            detector_rules=dict(
                type="list",
                elements="dict",
                options=dict(
                    detector_rule_id=dict(type="str", required=True),
                    details=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            is_enabled=dict(type="bool", required=True),
                            risk_level=dict(
                                type="str",
                                required=True,
                                choices=["CRITICAL", "HIGH", "MEDIUM", "LOW", "MINOR"],
                            ),
                            configurations=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    config_key=dict(type="str", required=True),
                                    name=dict(type="str", required=True),
                                    value=dict(type="str"),
                                    data_type=dict(type="str"),
                                    values=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            list_type=dict(
                                                type="str",
                                                required=True,
                                                choices=["MANAGED", "CUSTOM"],
                                            ),
                                            managed_list_type=dict(
                                                type="str", required=True
                                            ),
                                            value=dict(type="str", required=True),
                                        ),
                                    ),
                                ),
                            ),
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
                                        type="str", choices=["MANAGED", "CUSTOM"]
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
                            labels=dict(type="list"),
                        ),
                    ),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            detector_recipe_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
