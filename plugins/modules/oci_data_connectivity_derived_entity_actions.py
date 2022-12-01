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
module: oci_data_connectivity_derived_entity_actions
short_description: Perform actions on a DerivedEntity resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DerivedEntity resource in Oracle Cloud Infrastructure
    - For I(action=derive_entities), get the Derived Entities from the EntityFlowMode and reference key of DataObject
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry OCID.
        type: str
        aliases: ["id"]
        required: true
    items:
        description:
            - The array of DeriveEntitiesRequestItem
        type: list
        elements: dict
        required: true
        suboptions:
            model_type:
                description:
                    - The model type of DeriveEntitiesRequestItem
                type: str
                required: true
            mode:
                description:
                    - Determines whether derived entity is treated as source or target
                type: str
                choices:
                    - "IN"
                    - "OUT"
                required: true
            referenced_data_object:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    model_type:
                        description:
                            - The input Operation type.
                        type: str
                        choices:
                            - "API"
                            - "PROCEDURE"
                        required: true
                    model_version:
                        description:
                            - The object's model version.
                        type: str
                    parent_ref:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                    - Applicable when model_type is 'API'
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is unique, editable and is restricted to 1000 characters.
                        type: str
                    object_version:
                        description:
                            - The version of the object that is used to track changes in the object instance.
                        type: int
                    resource_name:
                        description:
                            - The resource name.
                        type: str
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.
                        type: int
                    external_key:
                        description:
                            - The external key for the object.
                        type: str
                    key:
                        description:
                            - The object key.
                        type: str
    action:
        description:
            - The action to perform on the DerivedEntity.
        type: str
        required: true
        choices:
            - "derive_entities"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action derive_entities on derived_entity
  oci_data_connectivity_derived_entity_actions:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    items:
    - # required
      model_type: model_type_example
      mode: IN
      referenced_data_object:
        # required
        model_type: API

        # optional
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        object_version: 56
        resource_name: resource_name_example
        object_status: 56
        external_key: external_key_example
        key: key_example
    action: derive_entities

"""

RETURN = """
derive_entities:
    description:
        - Details of the DerivedEntity resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        items:
            description:
                - The array of DerivedEntity
            returned: on success
            type: complex
            contains:
                entity_properties:
                    description:
                        - Map<String, String> for entity properties
                    returned: on success
                    type: dict
                    sample: {}
                model_type:
                    description:
                        - The data entity type.
                    returned: on success
                    type: str
                    sample: VIEW_ENTITY
                metadata:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        created_by:
                            description:
                                - The user that created the object.
                            returned: on success
                            type: str
                            sample: created_by_example
                        created_by_name:
                            description:
                                - The user that created the object.
                            returned: on success
                            type: str
                            sample: created_by_name_example
                        updated_by:
                            description:
                                - The user that updated the object.
                            returned: on success
                            type: str
                            sample: updated_by_example
                        updated_by_name:
                            description:
                                - The user that updated the object.
                            returned: on success
                            type: str
                            sample: updated_by_name_example
                        time_created:
                            description:
                                - The date and time that the object was created.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_updated:
                            description:
                                - The date and time that the object was updated.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        aggregator_key:
                            description:
                                - The owning object key for this object.
                            returned: on success
                            type: str
                            sample: aggregator_key_example
                        aggregator:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                type:
                                    description:
                                        - The type of the aggregator.
                                    returned: on success
                                    type: str
                                    sample: type_example
                                key:
                                    description:
                                        - The key of the aggregator object.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                name:
                                    description:
                                        - The name of the aggregator.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                identifier:
                                    description:
                                        - The identifier of the aggregator.
                                    returned: on success
                                    type: str
                                    sample: identifier_example
                                description:
                                    description:
                                        - The description of the aggregator.
                                    returned: on success
                                    type: str
                                    sample: description_example
                        identifier_path:
                            description:
                                - The full path to identify the object.
                            returned: on success
                            type: str
                            sample: identifier_path_example
                        info_fields:
                            description:
                                - Information property fields.
                            returned: on success
                            type: dict
                            sample: {}
                        registry_version:
                            description:
                                - The registry version of the object.
                            returned: on success
                            type: int
                            sample: 56
                        labels:
                            description:
                                - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them
                                  to categorize content.
                            returned: on success
                            type: list
                            sample: []
                        is_favorite:
                            description:
                                - Specifies whether this object is a favorite.
                            returned: on success
                            type: bool
                            sample: true
                key:
                    description:
                        - The object key.
                    returned: on success
                    type: str
                    sample: key_example
                model_version:
                    description:
                        - The object's model version.
                    returned: on success
                    type: str
                    sample: model_version_example
                parent_ref:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        parent:
                            description:
                                - Key of the parent object.
                            returned: on success
                            type: str
                            sample: parent_example
                name:
                    description:
                        - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is
                          unique, editable and is restricted to 1000 characters.
                    returned: on success
                    type: str
                    sample: name_example
                object_version:
                    description:
                        - The version of the object that is used to track changes in the object instance.
                    returned: on success
                    type: int
                    sample: 56
                shape:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        model_type:
                            description:
                                - The type of the types object.
                            returned: on success
                            type: str
                            sample: SHAPE
                        key:
                            description:
                                - The key of the object.
                            returned: on success
                            type: str
                            sample: key_example
                        model_version:
                            description:
                                - The model version of an object.
                            returned: on success
                            type: str
                            sample: model_version_example
                        parent_ref:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                parent:
                                    description:
                                        - Key of the parent object.
                                    returned: on success
                                    type: str
                                    sample: parent_example
                        config_values:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                config_param_values:
                                    description:
                                        - The configuration parameter values.
                                    returned: on success
                                    type: complex
                                    contains:
                                        string_value:
                                            description:
                                                - A string value of the parameter.
                                            returned: on success
                                            type: str
                                            sample: string_value_example
                                        int_value:
                                            description:
                                                - An integer value of the parameter.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        object_value:
                                            description:
                                                - An object value of the parameter.
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        ref_value:
                                            description:
                                                - The root object reference value.
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        parameter_value:
                                            description:
                                                - Reference to the parameter by its key.
                                            returned: on success
                                            type: str
                                            sample: parameter_value_example
                                parent_ref:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        parent:
                                            description:
                                                - Key of the parent object.
                                            returned: on success
                                            type: str
                                            sample: parent_example
                        object_status:
                            description:
                                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                            returned: on success
                            type: int
                            sample: 56
                        name:
                            description:
                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters.
                                  The value is editable and is restricted to 1000 characters.
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - A detailed description of the object.
                            returned: on success
                            type: str
                            sample: description_example
                        type:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                parent_type:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        model_type:
                                            description:
                                                - The property which differentiates the subtypes.
                                            returned: on success
                                            type: str
                                            sample: STRUCTURED_TYPE
                                        key:
                                            description:
                                                - The key of the object.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        model_version:
                                            description:
                                                - The model version of an object.
                                            returned: on success
                                            type: str
                                            sample: model_version_example
                                        parent_ref:
                                            description:
                                                - ""
                                            returned: on success
                                            type: ParentReference
                                            sample: "null"

                                        name:
                                            description:
                                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and
                                                  special characters. The value is editable and is restricted to 1000 characters.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        object_status:
                                            description:
                                                - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                  reserved.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        description:
                                            description:
                                                - A user-defined description for the object.
                                            returned: on success
                                            type: str
                                            sample: description_example
                                        parent_type:
                                            description:
                                                - ""
                                            returned: on success
                                            type: CompositeType
                                            sample: "null"

                                        elements:
                                            description:
                                                - An array of elements.
                                            returned: on success
                                            type: list
                                            sample: []
                                        config_definition:
                                            description:
                                                - ""
                                            returned: on success
                                            type: ConfigDefinition
                                            sample: "null"

                                elements:
                                    description:
                                        - An array of elements.
                                    returned: on success
                                    type: complex
                                    contains:
                                        position:
                                            description:
                                                - The position of the attribute.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        default_value_string:
                                            description:
                                                - The default value.
                                            returned: on success
                                            type: str
                                            sample: default_value_string_example
                                        is_mandatory:
                                            description:
                                                - Specifies whether the field is mandatory.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        port_type:
                                            description:
                                                - The port details of the data asset type.
                                            returned: on success
                                            type: str
                                            sample: DATA
                                        fields:
                                            description:
                                                - An array of fields.
                                            returned: on success
                                            type: complex
                                            contains:
                                                model_type:
                                                    description:
                                                        - The type of the types object.
                                                    returned: on success
                                                    type: str
                                                    sample: SHAPE
                                                key:
                                                    description:
                                                        - The key of the object.
                                                    returned: on success
                                                    type: str
                                                    sample: key_example
                                                model_version:
                                                    description:
                                                        - The model version of an object.
                                                    returned: on success
                                                    type: str
                                                    sample: model_version_example
                                                parent_ref:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: ParentReference
                                                    sample: "null"

                                                config_values:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: ConfigValues
                                                    sample: "null"

                                                object_status:
                                                    description:
                                                        - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                          reserved.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                                name:
                                                    description:
                                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers,
                                                          and special characters. The value is editable and is restricted to 1000 characters.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                description:
                                                    description:
                                                        - A detailed description of the object.
                                                    returned: on success
                                                    type: str
                                                    sample: description_example
                                        default_value:
                                            description:
                                                - The default value of the parameter.
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        root_object_default_value:
                                            description:
                                                - The default value of the parameter, which can be an object in DIS, such as a data entity.
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        is_input:
                                            description:
                                                - Specifies whether the parameter is an input value.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        is_output:
                                            description:
                                                - Specifies whether the parameter is an output value.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        output_aggregation_type:
                                            description:
                                                - The output aggregation type.
                                            returned: on success
                                            type: str
                                            sample: MIN
                                        type_name:
                                            description:
                                                - The type of value the parameter was created for.
                                            returned: on success
                                            type: str
                                            sample: type_name_example
                                        model_type:
                                            description:
                                                - The type of the types object.
                                            returned: on success
                                            type: str
                                            sample: SHAPE
                                        key:
                                            description:
                                                - The key of the object.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        model_version:
                                            description:
                                                - The model version of an object.
                                            returned: on success
                                            type: str
                                            sample: model_version_example
                                        parent_ref:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                parent:
                                                    description:
                                                        - Key of the parent object.
                                                    returned: on success
                                                    type: str
                                                    sample: parent_example
                                        config_values:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                config_param_values:
                                                    description:
                                                        - The configuration parameter values.
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        string_value:
                                                            description:
                                                                - A string value of the parameter.
                                                            returned: on success
                                                            type: str
                                                            sample: string_value_example
                                                        int_value:
                                                            description:
                                                                - An integer value of the parameter.
                                                            returned: on success
                                                            type: int
                                                            sample: 56
                                                        object_value:
                                                            description:
                                                                - An object value of the parameter.
                                                            returned: on success
                                                            type: dict
                                                            sample: {}
                                                        ref_value:
                                                            description:
                                                                - The root object reference value.
                                                            returned: on success
                                                            type: dict
                                                            sample: {}
                                                        parameter_value:
                                                            description:
                                                                - Reference to the parameter by its key.
                                                            returned: on success
                                                            type: str
                                                            sample: parameter_value_example
                                                parent_ref:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        parent:
                                                            description:
                                                                - Key of the parent object.
                                                            returned: on success
                                                            type: str
                                                            sample: parent_example
                                        object_status:
                                            description:
                                                - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                  reserved.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        name:
                                            description:
                                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and
                                                  special characters. The value is editable and is restricted to 1000 characters.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        description:
                                            description:
                                                - A detailed description of the object.
                                            returned: on success
                                            type: str
                                            sample: description_example
                                        type:
                                            description:
                                                - The type reference.
                                            returned: on success
                                            type: dict
                                            sample: {}
                                        labels:
                                            description:
                                                - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own
                                                  labels and use them to categorize content.
                                            returned: on success
                                            type: list
                                            sample: []
                                        native_shape_field:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                model_type:
                                                    description:
                                                        - The type of the types object.
                                                    returned: on success
                                                    type: str
                                                    sample: SHAPE
                                                key:
                                                    description:
                                                        - The key of the object.
                                                    returned: on success
                                                    type: str
                                                    sample: key_example
                                                model_version:
                                                    description:
                                                        - The model version of an object.
                                                    returned: on success
                                                    type: str
                                                    sample: model_version_example
                                                parent_ref:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        parent:
                                                            description:
                                                                - Key of the parent object.
                                                            returned: on success
                                                            type: str
                                                            sample: parent_example
                                                config_values:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        config_param_values:
                                                            description:
                                                                - The configuration parameter values.
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                string_value:
                                                                    description:
                                                                        - A string value of the parameter.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: string_value_example
                                                                int_value:
                                                                    description:
                                                                        - An integer value of the parameter.
                                                                    returned: on success
                                                                    type: int
                                                                    sample: 56
                                                                object_value:
                                                                    description:
                                                                        - An object value of the parameter.
                                                                    returned: on success
                                                                    type: dict
                                                                    sample: {}
                                                                ref_value:
                                                                    description:
                                                                        - The root object reference value.
                                                                    returned: on success
                                                                    type: dict
                                                                    sample: {}
                                                                parameter_value:
                                                                    description:
                                                                        - Reference to the parameter by its key.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: parameter_value_example
                                                        parent_ref:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: complex
                                                            contains:
                                                                parent:
                                                                    description:
                                                                        - Key of the parent object.
                                                                    returned: on success
                                                                    type: str
                                                                    sample: parent_example
                                                object_status:
                                                    description:
                                                        - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                          reserved.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                                name:
                                                    description:
                                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers,
                                                          and special characters. The value is editable and is restricted to 1000 characters.
                                                    returned: on success
                                                    type: str
                                                    sample: name_example
                                                description:
                                                    description:
                                                        - A detailed description of the object.
                                                    returned: on success
                                                    type: str
                                                    sample: description_example
                                                type:
                                                    description:
                                                        - The type reference.
                                                    returned: on success
                                                    type: dict
                                                    sample: {}
                                                position:
                                                    description:
                                                        - The position of the attribute.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                                default_value_string:
                                                    description:
                                                        - The default value.
                                                    returned: on success
                                                    type: str
                                                    sample: default_value_string_example
                                                is_mandatory:
                                                    description:
                                                        - Specifies whether the field is mandatory.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                wrapped_type:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        model_type:
                                            description:
                                                - The property which differentiates the subtypes.
                                            returned: on success
                                            type: str
                                            sample: STRUCTURED_TYPE
                                        key:
                                            description:
                                                - The key of the object.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        model_version:
                                            description:
                                                - The model version of an object.
                                            returned: on success
                                            type: str
                                            sample: model_version_example
                                        parent_ref:
                                            description:
                                                - ""
                                            returned: on success
                                            type: ParentReference
                                            sample: "null"

                                        name:
                                            description:
                                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and
                                                  special characters. The value is editable and is restricted to 1000 characters.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        object_status:
                                            description:
                                                - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                  reserved.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        description:
                                            description:
                                                - A user-defined description for the object.
                                            returned: on success
                                            type: str
                                            sample: description_example
                                config_values:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        config_param_values:
                                            description:
                                                - The configuration parameter values.
                                            returned: on success
                                            type: complex
                                            contains:
                                                string_value:
                                                    description:
                                                        - A string value of the parameter.
                                                    returned: on success
                                                    type: str
                                                    sample: string_value_example
                                                int_value:
                                                    description:
                                                        - An integer value of the parameter.
                                                    returned: on success
                                                    type: int
                                                    sample: 56
                                                object_value:
                                                    description:
                                                        - An object value of the parameter.
                                                    returned: on success
                                                    type: dict
                                                    sample: {}
                                                ref_value:
                                                    description:
                                                        - The root object reference value.
                                                    returned: on success
                                                    type: dict
                                                    sample: {}
                                                parameter_value:
                                                    description:
                                                        - Reference to the parameter by its key.
                                                    returned: on success
                                                    type: str
                                                    sample: parameter_value_example
                                        parent_ref:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                parent:
                                                    description:
                                                        - Key of the parent object.
                                                    returned: on success
                                                    type: str
                                                    sample: parent_example
                                dt_type:
                                    description:
                                        - The data type.
                                    returned: on success
                                    type: str
                                    sample: PRIMITIVE
                                type_system_name:
                                    description:
                                        - The data type system name.
                                    returned: on success
                                    type: str
                                    sample: type_system_name_example
                                config_definition:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        key:
                                            description:
                                                - The key of the object.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        model_type:
                                            description:
                                                - The type of the object.
                                            returned: on success
                                            type: str
                                            sample: model_type_example
                                        model_version:
                                            description:
                                                - The model version of an object.
                                            returned: on success
                                            type: str
                                            sample: model_version_example
                                        parent_ref:
                                            description:
                                                - ""
                                            returned: on success
                                            type: complex
                                            contains:
                                                parent:
                                                    description:
                                                        - Key of the parent object.
                                                    returned: on success
                                                    type: str
                                                    sample: parent_example
                                        name:
                                            description:
                                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and
                                                  special characters. The value is editable and is restricted to 1000 characters.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        is_contained:
                                            description:
                                                - Specifies whether the configuration is contained.
                                            returned: on success
                                            type: bool
                                            sample: true
                                        object_status:
                                            description:
                                                - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                  reserved.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        config_parameter_definitions:
                                            description:
                                                - The parameter configuration details.
                                            returned: on success
                                            type: complex
                                            contains:
                                                parameter_type:
                                                    description:
                                                        - ""
                                                    returned: on success
                                                    type: complex
                                                    contains:
                                                        model_type:
                                                            description:
                                                                - The property which differentiates the subtypes.
                                                            returned: on success
                                                            type: str
                                                            sample: STRUCTURED_TYPE
                                                        key:
                                                            description:
                                                                - The key of the object.
                                                            returned: on success
                                                            type: str
                                                            sample: key_example
                                                        model_version:
                                                            description:
                                                                - The model version of an object.
                                                            returned: on success
                                                            type: str
                                                            sample: model_version_example
                                                        parent_ref:
                                                            description:
                                                                - ""
                                                            returned: on success
                                                            type: ParentReference
                                                            sample: "null"

                                                        name:
                                                            description:
                                                                - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                  numbers, and special characters. The value is editable and is restricted to 1000 characters.
                                                            returned: on success
                                                            type: str
                                                            sample: name_example
                                                        object_status:
                                                            description:
                                                                - The status of an object that can be set to value 1 for shallow references across objects,
                                                                  other values reserved.
                                                            returned: on success
                                                            type: int
                                                            sample: 56
                                                        description:
                                                            description:
                                                                - A user-defined description for the object.
                                                            returned: on success
                                                            type: str
                                                            sample: description_example
                                                parameter_name:
                                                    description:
                                                        - This object represents the configurable properties for an object type.
                                                    returned: on success
                                                    type: str
                                                    sample: parameter_name_example
                                                description:
                                                    description:
                                                        - A user-defined description for the object.
                                                    returned: on success
                                                    type: str
                                                    sample: description_example
                                                default_value:
                                                    description:
                                                        - The default value for the parameter.
                                                    returned: on success
                                                    type: dict
                                                    sample: {}
                                                class_field_name:
                                                    description:
                                                        - The parameter class field name.
                                                    returned: on success
                                                    type: str
                                                    sample: class_field_name_example
                                                is_static:
                                                    description:
                                                        - Specifies whether the parameter is static.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                                is_class_field_value:
                                                    description:
                                                        - Specifies whether the parameter is a class field.
                                                    returned: on success
                                                    type: bool
                                                    sample: true
                                model_type:
                                    description:
                                        - The property which differentiates the subtypes.
                                    returned: on success
                                    type: str
                                    sample: STRUCTURED_TYPE
                                key:
                                    description:
                                        - The key of the object.
                                    returned: on success
                                    type: str
                                    sample: key_example
                                model_version:
                                    description:
                                        - The model version of an object.
                                    returned: on success
                                    type: str
                                    sample: model_version_example
                                parent_ref:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        parent:
                                            description:
                                                - Key of the parent object.
                                            returned: on success
                                            type: str
                                            sample: parent_example
                                name:
                                    description:
                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                          characters. The value is editable and is restricted to 1000 characters.
                                    returned: on success
                                    type: str
                                    sample: name_example
                                object_status:
                                    description:
                                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                    returned: on success
                                    type: int
                                    sample: 56
                                description:
                                    description:
                                        - A user-defined description for the object.
                                    returned: on success
                                    type: str
                                    sample: description_example
                                schema:
                                    description:
                                        - ""
                                    returned: on success
                                    type: complex
                                    contains:
                                        model_type:
                                            description:
                                                - The property which differentiates the subtypes.
                                            returned: on success
                                            type: str
                                            sample: STRUCTURED_TYPE
                                        key:
                                            description:
                                                - The key of the object.
                                            returned: on success
                                            type: str
                                            sample: key_example
                                        model_version:
                                            description:
                                                - The model version of an object.
                                            returned: on success
                                            type: str
                                            sample: model_version_example
                                        parent_ref:
                                            description:
                                                - ""
                                            returned: on success
                                            type: ParentReference
                                            sample: "null"

                                        name:
                                            description:
                                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and
                                                  special characters. The value is editable and is restricted to 1000 characters.
                                            returned: on success
                                            type: str
                                            sample: name_example
                                        object_status:
                                            description:
                                                - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                  reserved.
                                            returned: on success
                                            type: int
                                            sample: 56
                                        description:
                                            description:
                                                - A user-defined description for the object.
                                            returned: on success
                                            type: str
                                            sample: description_example
                shape_id:
                    description:
                        - The shape ID.
                    returned: on success
                    type: str
                    sample: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
                resource_name:
                    description:
                        - The resource name.
                    returned: on success
                    type: str
                    sample: resource_name_example
                object_status:
                    description:
                        - The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.
                    returned: on success
                    type: int
                    sample: 56
                identifier:
                    description:
                        - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value
                          can be modified.
                    returned: on success
                    type: str
                    sample: identifier_example
                ref_data_object:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        model_type:
                            description:
                                - The input Operation type.
                            returned: on success
                            type: str
                            sample: PROCEDURE
                        model_version:
                            description:
                                - The object's model version.
                            returned: on success
                            type: str
                            sample: model_version_example
                        parent_ref:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                parent:
                                    description:
                                        - Key of the parent object.
                                    returned: on success
                                    type: str
                                    sample: parent_example
                        name:
                            description:
                                - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The
                                  value is unique, editable and is restricted to 1000 characters.
                            returned: on success
                            type: str
                            sample: name_example
                        object_version:
                            description:
                                - The version of the object that is used to track changes in the object instance.
                            returned: on success
                            type: int
                            sample: 56
                        resource_name:
                            description:
                                - The resource name.
                            returned: on success
                            type: str
                            sample: resource_name_example
                        object_status:
                            description:
                                - The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.
                            returned: on success
                            type: int
                            sample: 56
                        external_key:
                            description:
                                - The external key for the object.
                            returned: on success
                            type: str
                            sample: external_key_example
                        key:
                            description:
                                - The object key.
                            returned: on success
                            type: str
                            sample: key_example
                mode:
                    description:
                        - Determines whether entity is treated as source or target
                    returned: on success
                    type: str
                    sample: IN
                derived_properties:
                    description:
                        - Property-bag (key-value pairs where key is Shape Field resource name and value is object)
                    returned: on success
                    type: dict
                    sample: {}
    sample: {
        "items": [{
            "entity_properties": {},
            "model_type": "VIEW_ENTITY",
            "metadata": {
                "created_by": "created_by_example",
                "created_by_name": "created_by_name_example",
                "updated_by": "updated_by_example",
                "updated_by_name": "updated_by_name_example",
                "time_created": "2013-10-20T19:20:30+01:00",
                "time_updated": "2013-10-20T19:20:30+01:00",
                "aggregator_key": "aggregator_key_example",
                "aggregator": {
                    "type": "type_example",
                    "key": "key_example",
                    "name": "name_example",
                    "identifier": "identifier_example",
                    "description": "description_example"
                },
                "identifier_path": "identifier_path_example",
                "info_fields": {},
                "registry_version": 56,
                "labels": [],
                "is_favorite": true
            },
            "key": "key_example",
            "model_version": "model_version_example",
            "parent_ref": {
                "parent": "parent_example"
            },
            "name": "name_example",
            "object_version": 56,
            "shape": {
                "model_type": "SHAPE",
                "key": "key_example",
                "model_version": "model_version_example",
                "parent_ref": {
                    "parent": "parent_example"
                },
                "config_values": {
                    "config_param_values": {
                        "string_value": "string_value_example",
                        "int_value": 56,
                        "object_value": {},
                        "ref_value": {},
                        "parameter_value": "parameter_value_example"
                    },
                    "parent_ref": {
                        "parent": "parent_example"
                    }
                },
                "object_status": 56,
                "name": "name_example",
                "description": "description_example",
                "type": {
                    "parent_type": {
                        "model_type": "STRUCTURED_TYPE",
                        "key": "key_example",
                        "model_version": "model_version_example",
                        "parent_ref": null,
                        "name": "name_example",
                        "object_status": 56,
                        "description": "description_example",
                        "parent_type": null,
                        "elements": [],
                        "config_definition": null
                    },
                    "elements": [{
                        "position": 56,
                        "default_value_string": "default_value_string_example",
                        "is_mandatory": true,
                        "port_type": "DATA",
                        "fields": [{
                            "model_type": "SHAPE",
                            "key": "key_example",
                            "model_version": "model_version_example",
                            "parent_ref": null,
                            "config_values": null,
                            "object_status": 56,
                            "name": "name_example",
                            "description": "description_example"
                        }],
                        "default_value": {},
                        "root_object_default_value": {},
                        "is_input": true,
                        "is_output": true,
                        "output_aggregation_type": "MIN",
                        "type_name": "type_name_example",
                        "model_type": "SHAPE",
                        "key": "key_example",
                        "model_version": "model_version_example",
                        "parent_ref": {
                            "parent": "parent_example"
                        },
                        "config_values": {
                            "config_param_values": {
                                "string_value": "string_value_example",
                                "int_value": 56,
                                "object_value": {},
                                "ref_value": {},
                                "parameter_value": "parameter_value_example"
                            },
                            "parent_ref": {
                                "parent": "parent_example"
                            }
                        },
                        "object_status": 56,
                        "name": "name_example",
                        "description": "description_example",
                        "type": {},
                        "labels": [],
                        "native_shape_field": {
                            "model_type": "SHAPE",
                            "key": "key_example",
                            "model_version": "model_version_example",
                            "parent_ref": {
                                "parent": "parent_example"
                            },
                            "config_values": {
                                "config_param_values": {
                                    "string_value": "string_value_example",
                                    "int_value": 56,
                                    "object_value": {},
                                    "ref_value": {},
                                    "parameter_value": "parameter_value_example"
                                },
                                "parent_ref": {
                                    "parent": "parent_example"
                                }
                            },
                            "object_status": 56,
                            "name": "name_example",
                            "description": "description_example",
                            "type": {},
                            "position": 56,
                            "default_value_string": "default_value_string_example",
                            "is_mandatory": true
                        }
                    }],
                    "wrapped_type": {
                        "model_type": "STRUCTURED_TYPE",
                        "key": "key_example",
                        "model_version": "model_version_example",
                        "parent_ref": null,
                        "name": "name_example",
                        "object_status": 56,
                        "description": "description_example"
                    },
                    "config_values": {
                        "config_param_values": {
                            "string_value": "string_value_example",
                            "int_value": 56,
                            "object_value": {},
                            "ref_value": {},
                            "parameter_value": "parameter_value_example"
                        },
                        "parent_ref": {
                            "parent": "parent_example"
                        }
                    },
                    "dt_type": "PRIMITIVE",
                    "type_system_name": "type_system_name_example",
                    "config_definition": {
                        "key": "key_example",
                        "model_type": "model_type_example",
                        "model_version": "model_version_example",
                        "parent_ref": {
                            "parent": "parent_example"
                        },
                        "name": "name_example",
                        "is_contained": true,
                        "object_status": 56,
                        "config_parameter_definitions": {
                            "parameter_type": {
                                "model_type": "STRUCTURED_TYPE",
                                "key": "key_example",
                                "model_version": "model_version_example",
                                "parent_ref": null,
                                "name": "name_example",
                                "object_status": 56,
                                "description": "description_example"
                            },
                            "parameter_name": "parameter_name_example",
                            "description": "description_example",
                            "default_value": {},
                            "class_field_name": "class_field_name_example",
                            "is_static": true,
                            "is_class_field_value": true
                        }
                    },
                    "model_type": "STRUCTURED_TYPE",
                    "key": "key_example",
                    "model_version": "model_version_example",
                    "parent_ref": {
                        "parent": "parent_example"
                    },
                    "name": "name_example",
                    "object_status": 56,
                    "description": "description_example",
                    "schema": {
                        "model_type": "STRUCTURED_TYPE",
                        "key": "key_example",
                        "model_version": "model_version_example",
                        "parent_ref": null,
                        "name": "name_example",
                        "object_status": 56,
                        "description": "description_example"
                    }
                }
            },
            "shape_id": "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx",
            "resource_name": "resource_name_example",
            "object_status": 56,
            "identifier": "identifier_example",
            "ref_data_object": {
                "model_type": "PROCEDURE",
                "model_version": "model_version_example",
                "parent_ref": {
                    "parent": "parent_example"
                },
                "name": "name_example",
                "object_version": 56,
                "resource_name": "resource_name_example",
                "object_status": 56,
                "external_key": "external_key_example",
                "key": "key_example"
            },
            "mode": "IN",
            "derived_properties": {}
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient
    from oci.data_connectivity.models import DeriveEntitiesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DerivedEntityActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        derive_entities
    """

    @staticmethod
    def get_module_resource_id_param():
        return "registry_id"

    def get_module_resource_id(self):
        return self.module.params.get("registry_id")

    def derive_entities(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DeriveEntitiesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.derive_entities,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                derive_entities_details=action_details,
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


DerivedEntityActionsHelperCustom = get_custom_class("DerivedEntityActionsHelperCustom")


class ResourceHelper(DerivedEntityActionsHelperCustom, DerivedEntityActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            registry_id=dict(aliases=["id"], type="str", required=True),
            items=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    model_type=dict(type="str", required=True),
                    mode=dict(type="str", required=True, choices=["IN", "OUT"]),
                    referenced_data_object=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            model_type=dict(
                                type="str", required=True, choices=["API", "PROCEDURE"]
                            ),
                            model_version=dict(type="str"),
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
                            ),
                            name=dict(type="str"),
                            object_version=dict(type="int"),
                            resource_name=dict(type="str"),
                            object_status=dict(type="int"),
                            external_key=dict(type="str", no_log=True),
                            key=dict(type="str", no_log=True),
                        ),
                    ),
                ),
            ),
            action=dict(type="str", required=True, choices=["derive_entities"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="derived_entity",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
