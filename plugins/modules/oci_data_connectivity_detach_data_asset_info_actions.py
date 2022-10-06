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
module: oci_data_connectivity_detach_data_asset_info_actions
short_description: Perform actions on a DetachDataAssetInfo resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DetachDataAssetInfo resource in Oracle Cloud Infrastructure
    - For I(action=create_detach_data_asset), detaches a list of data assets to the given endpoint.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry OCID.
        type: str
        required: true
    endpoint_id:
        description:
            - DCMS endpoint ID.
        type: str
        aliases: ["id"]
        required: true
    data_assets:
        description:
            - The array of DataAsset keys.
        type: list
        elements: dict
        required: true
        suboptions:
            key:
                description:
                    - Currently not used while creating a data asset. Reserved for future.
                type: str
                required: true
            model_version:
                description:
                    - The model version of an object.
                type: str
            model_type:
                description:
                    - The type of the object.
                type: str
            name:
                description:
                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                type: str
                required: true
            description:
                description:
                    - User-defined description of the data asset.
                type: str
            object_status:
                description:
                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                type: int
            object_version:
                description:
                    - The version of the object that is used to track changes in the object instance.
                type: int
            identifier:
                description:
                    - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can
                      be modified.
                type: str
                required: true
            external_key:
                description:
                    - The external key of the object.
                type: str
            asset_properties:
                description:
                    - Additional properties for the data asset.
                type: dict
            properties:
                description:
                    - All the properties for the data asset in a key-value map format.
                type: dict
            type:
                description:
                    - Specific DataAsset Type
                type: str
            native_type_system:
                description:
                    - ""
                type: dict
                suboptions:
                    key:
                        description:
                            - The key of the object.
                        type: str
                    model_type:
                        description:
                            - The type of the object.
                        type: str
                    model_version:
                        description:
                            - The model version of an object.
                        type: str
                    parent_ref:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                        type: str
                    description:
                        description:
                            - A user-defined description for the object.
                        type: str
                    object_version:
                        description:
                            - The version of the object that is used to track changes in the object instance.
                        type: int
                    type_mapping_to:
                        description:
                            - The type system to map to.
                        type: dict
                    type_mapping_from:
                        description:
                            - The type system to map from.
                        type: dict
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                        type: int
                    identifier:
                        description:
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The
                              value can be modified.
                        type: str
                    types:
                        description:
                            - An array of types.
                        type: list
                        elements: dict
                        suboptions:
                            model_type:
                                description:
                                    - The property which differentiates the subtypes.
                                type: str
                                choices:
                                    - "STRUCTURED_TYPE"
                                    - "DATA_TYPE"
                                    - "CONFIGURED_TYPE"
                                    - "COMPOSITE_TYPE"
                                    - "DERIVED_TYPE"
                                required: true
                            key:
                                description:
                                    - The key of the object.
                                type: str
                            model_version:
                                description:
                                    - The model version of an object.
                                type: str
                            parent_ref:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    parent:
                                        description:
                                            - Key of the parent object.
                                        type: str
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            description:
                                description:
                                    - A user-defined description for the object.
                                type: str
                            dt_type:
                                description:
                                    - The data type.
                                type: str
                                choices:
                                    - "PRIMITIVE"
                                    - "STRUCTURED"
                            type_system_name:
                                description:
                                    - The data type system name.
                                type: str
                            config_definition:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    key:
                                        description:
                                            - The key of the object.
                                        type: str
                                    model_type:
                                        description:
                                            - The type of the object.
                                        type: str
                                    model_version:
                                        description:
                                            - The model version of an object.
                                        type: str
                                    parent_ref:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                type: str
                                    name:
                                        description:
                                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    is_contained:
                                        description:
                                            - Specifies whether the configuration is contained.
                                        type: bool
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                        type: int
                                    config_parameter_definitions:
                                        description:
                                            - The parameter configuration details.
                                        type: dict
                                        suboptions:
                                            parameter_type:
                                                description:
                                                    - ""
                                                type: dict
                                                suboptions:
                                                    wrapped_type:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            model_type:
                                                                description:
                                                                    - The property which differentiates the subtypes.
                                                                type: str
                                                                choices:
                                                                    - "STRUCTURED_TYPE"
                                                                    - "DATA_TYPE"
                                                                    - "CONFIGURED_TYPE"
                                                                    - "COMPOSITE_TYPE"
                                                                    - "DERIVED_TYPE"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            description:
                                                                description:
                                                                    - A user-defined description for the object.
                                                                type: str
                                                    config_values:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            config_param_values:
                                                                description:
                                                                    - The configuration parameter values.
                                                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                type: dict
                                                                suboptions:
                                                                    string_value:
                                                                        description:
                                                                            - A string value of the parameter.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: str
                                                                    int_value:
                                                                        description:
                                                                            - An integer value of the parameter.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: int
                                                                    object_value:
                                                                        description:
                                                                            - An object value of the parameter.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: dict
                                                                    ref_value:
                                                                        description:
                                                                            - The root object reference value.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: dict
                                                                    parameter_value:
                                                                        description:
                                                                            - Reference to the parameter by its key.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                type: dict
                                                                suboptions:
                                                                    parent:
                                                                        description:
                                                                            - Key of the parent object.
                                                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                        type: str
                                                    dt_type:
                                                        description:
                                                            - The data type.
                                                            - Applicable when model_type is 'DATA_TYPE'
                                                        type: str
                                                        choices:
                                                            - "PRIMITIVE"
                                                            - "STRUCTURED"
                                                    type_system_name:
                                                        description:
                                                            - The data type system name.
                                                            - Applicable when model_type is 'DATA_TYPE'
                                                        type: str
                                                    schema:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'STRUCTURED_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            model_type:
                                                                description:
                                                                    - The property which differentiates the subtypes.
                                                                type: str
                                                                choices:
                                                                    - "STRUCTURED_TYPE"
                                                                    - "DATA_TYPE"
                                                                    - "CONFIGURED_TYPE"
                                                                    - "COMPOSITE_TYPE"
                                                                    - "DERIVED_TYPE"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            description:
                                                                description:
                                                                    - A user-defined description for the object.
                                                                type: str
                                                    model_type:
                                                        description:
                                                            - The property which differentiates the subtypes.
                                                        type: str
                                                        choices:
                                                            - "CONFIGURED_TYPE"
                                                            - "DERIVED_TYPE"
                                                            - "DATA_TYPE"
                                                            - "STRUCTURED_TYPE"
                                                            - "COMPOSITE_TYPE"
                                                        required: true
                                                    key:
                                                        description:
                                                            - The key of the object.
                                                        type: str
                                                    model_version:
                                                        description:
                                                            - The model version of an object.
                                                        type: str
                                                    parent_ref:
                                                        description:
                                                            - ""
                                                        type: dict
                                                        suboptions:
                                                            parent:
                                                                description:
                                                                    - Key of the parent object.
                                                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                                                type: str
                                                    name:
                                                        description:
                                                            - Free form text without any restriction on the permitted characters. Name can have letters,
                                                              numbers, and special characters. The value is editable and is restricted to 1000 characters.
                                                        type: str
                                                    object_status:
                                                        description:
                                                            - The status of an object that can be set to value 1 for shallow references across objects, other
                                                              values reserved.
                                                        type: int
                                                    description:
                                                        description:
                                                            - A user-defined description for the object.
                                                        type: str
                                                    parent_type:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'COMPOSITE_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            model_type:
                                                                description:
                                                                    - The property which differentiates the subtypes.
                                                                type: str
                                                                choices:
                                                                    - "STRUCTURED_TYPE"
                                                                    - "DATA_TYPE"
                                                                    - "CONFIGURED_TYPE"
                                                                    - "COMPOSITE_TYPE"
                                                                    - "DERIVED_TYPE"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            description:
                                                                description:
                                                                    - A user-defined description for the object.
                                                                type: str
                                                            parent_type:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            elements:
                                                                description:
                                                                    - An array of elements.
                                                                type: list
                                                                elements: dict
                                                            config_definition:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                    elements:
                                                        description:
                                                            - An array of elements.
                                                            - Applicable when model_type is 'COMPOSITE_TYPE'
                                                        type: list
                                                        elements: dict
                                                        suboptions:
                                                            labels:
                                                                description:
                                                                    - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You
                                                                      can define your own labels and use them to categorize content.
                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                type: list
                                                                elements: str
                                                            native_shape_field:
                                                                description:
                                                                    - ""
                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                type: dict
                                                                suboptions:
                                                                    model_type:
                                                                        description:
                                                                            - The type of the types object.
                                                                            - Required when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                        choices:
                                                                            - "SHAPE"
                                                                            - "SHAPE_FIELD"
                                                                            - "NATIVE_SHAPE_FIELD"
                                                                        required: true
                                                                    key:
                                                                        description:
                                                                            - The key of the object.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    model_version:
                                                                        description:
                                                                            - The model version of an object.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    parent_ref:
                                                                        description:
                                                                            - ""
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: dict
                                                                        suboptions:
                                                                            parent:
                                                                                description:
                                                                                    - Key of the parent object.
                                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                                type: str
                                                                    config_values:
                                                                        description:
                                                                            - ""
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: dict
                                                                        suboptions:
                                                                            config_param_values:
                                                                                description:
                                                                                    - The configuration parameter values.
                                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                                type: dict
                                                                                suboptions:
                                                                                    string_value:
                                                                                        description:
                                                                                            - A string value of the parameter.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: str
                                                                                    int_value:
                                                                                        description:
                                                                                            - An integer value of the parameter.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: int
                                                                                    object_value:
                                                                                        description:
                                                                                            - An object value of the parameter.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: dict
                                                                                    ref_value:
                                                                                        description:
                                                                                            - The root object reference value.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: dict
                                                                                    parameter_value:
                                                                                        description:
                                                                                            - Reference to the parameter by its key.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: str
                                                                            parent_ref:
                                                                                description:
                                                                                    - ""
                                                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                                                type: dict
                                                                                suboptions:
                                                                                    parent:
                                                                                        description:
                                                                                            - Key of the parent object.
                                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                                        type: str
                                                                    object_status:
                                                                        description:
                                                                            - The status of an object that can be set to value 1 for shallow references across
                                                                              objects, other values reserved.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: int
                                                                    name:
                                                                        description:
                                                                            - Free form text without any restriction on the permitted characters. Name can have
                                                                              letters, numbers, and special characters. The value is editable and is restricted
                                                                              to 1000 characters.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    description:
                                                                        description:
                                                                            - A detailed description of the object.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    type:
                                                                        description:
                                                                            - The type reference.
                                                                            - Required when model_type is 'SHAPE_FIELD'
                                                                        type: dict
                                                                        required: true
                                                                    position:
                                                                        description:
                                                                            - The position of the attribute.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: int
                                                                    default_value_string:
                                                                        description:
                                                                            - The default value.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    is_mandatory:
                                                                        description:
                                                                            - Specifies whether the field is mandatory.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: bool
                                                            port_type:
                                                                description:
                                                                    - The port details of the data asset type.
                                                                    - Applicable when model_type is one of ['INPUT_PORT', 'OUTPUT_PORT']
                                                                type: str
                                                                choices:
                                                                    - "DATA"
                                                                    - "CONTROL"
                                                                    - "MODEL"
                                                            fields:
                                                                description:
                                                                    - An array of fields.
                                                                    - Applicable when model_type is one of ['INPUT_PORT', 'OUTPUT_PORT']
                                                                type: list
                                                                elements: dict
                                                                suboptions:
                                                                    model_type:
                                                                        description:
                                                                            - The type of the types object.
                                                                        type: str
                                                                        choices:
                                                                            - "SHAPE"
                                                                            - "SHAPE_FIELD"
                                                                            - "NATIVE_SHAPE_FIELD"
                                                                        required: true
                                                                    key:
                                                                        description:
                                                                            - The key of the object.
                                                                        type: str
                                                                    model_version:
                                                                        description:
                                                                            - The model version of an object.
                                                                        type: str
                                                                    parent_ref:
                                                                        description:
                                                                            - ""
                                                                        type: dict
                                                                    config_values:
                                                                        description:
                                                                            - ""
                                                                        type: dict
                                                                    object_status:
                                                                        description:
                                                                            - The status of an object that can be set to value 1 for shallow references across
                                                                              objects, other values reserved.
                                                                        type: int
                                                                    name:
                                                                        description:
                                                                            - Free form text without any restriction on the permitted characters. Name can have
                                                                              letters, numbers, and special characters. The value is editable and is restricted
                                                                              to 1000 characters.
                                                                        type: str
                                                                    description:
                                                                        description:
                                                                            - A detailed description of the object.
                                                                        type: str
                                                            default_value:
                                                                description:
                                                                    - The default value of the parameter.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: dict
                                                            root_object_default_value:
                                                                description:
                                                                    - The default value of the parameter, which can be an object in DIS, such as a data entity.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: dict
                                                            is_input:
                                                                description:
                                                                    - Specifies whether the parameter is an input value.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: bool
                                                            is_output:
                                                                description:
                                                                    - Specifies whether the parameter is an output value.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: bool
                                                            output_aggregation_type:
                                                                description:
                                                                    - The output aggregation type.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: str
                                                                choices:
                                                                    - "MIN"
                                                                    - "MAX"
                                                                    - "COUNT"
                                                                    - "SUM"
                                                            type_name:
                                                                description:
                                                                    - The type of value the parameter was created for.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: str
                                                            model_type:
                                                                description:
                                                                    - The type of the types object.
                                                                type: str
                                                                choices:
                                                                    - "OUTPUT_PORT"
                                                                    - "SHAPE"
                                                                    - "SHAPE_FIELD"
                                                                    - "INPUT_PORT"
                                                                    - "PARAMETER"
                                                                    - "NATIVE_SHAPE_FIELD"
                                                                required: true
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                                suboptions:
                                                                    parent:
                                                                        description:
                                                                            - Key of the parent object.
                                                                            - Applicable when model_type is 'OUTPUT_PORT'
                                                                        type: str
                                                            config_values:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                                suboptions:
                                                                    config_param_values:
                                                                        description:
                                                                            - The configuration parameter values.
                                                                            - Applicable when model_type is 'OUTPUT_PORT'
                                                                        type: dict
                                                                        suboptions:
                                                                            string_value:
                                                                                description:
                                                                                    - A string value of the parameter.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: str
                                                                            int_value:
                                                                                description:
                                                                                    - An integer value of the parameter.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: int
                                                                            object_value:
                                                                                description:
                                                                                    - An object value of the parameter.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: dict
                                                                            ref_value:
                                                                                description:
                                                                                    - The root object reference value.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: dict
                                                                            parameter_value:
                                                                                description:
                                                                                    - Reference to the parameter by its key.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: str
                                                                    parent_ref:
                                                                        description:
                                                                            - ""
                                                                            - Applicable when model_type is 'OUTPUT_PORT'
                                                                        type: dict
                                                                        suboptions:
                                                                            parent:
                                                                                description:
                                                                                    - Key of the parent object.
                                                                                    - Applicable when model_type is 'OUTPUT_PORT'
                                                                                type: str
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            description:
                                                                description:
                                                                    - A detailed description of the object.
                                                                type: str
                                                            type:
                                                                description:
                                                                    - ""
                                                                    - Applicable when model_type is one of ['SHAPE', 'SHAPE_FIELD', 'PARAMETER']
                                                                    - Required when model_type is 'NATIVE_SHAPE_FIELD'
                                                                type: dict
                                                                suboptions:
                                                                    model_type:
                                                                        description:
                                                                            - The property which differentiates the subtypes.
                                                                        type: str
                                                                        choices:
                                                                            - "STRUCTURED_TYPE"
                                                                            - "DATA_TYPE"
                                                                            - "CONFIGURED_TYPE"
                                                                            - "COMPOSITE_TYPE"
                                                                            - "DERIVED_TYPE"
                                                                    key:
                                                                        description:
                                                                            - The key of the object.
                                                                        type: str
                                                                    model_version:
                                                                        description:
                                                                            - The model version of an object.
                                                                        type: str
                                                                    parent_ref:
                                                                        description:
                                                                            - ""
                                                                        type: dict
                                                                    name:
                                                                        description:
                                                                            - Free form text without any restriction on the permitted characters. Name can have
                                                                              letters, numbers, and special characters. The value is editable and is restricted
                                                                              to 1000 characters.
                                                                        type: str
                                                                    object_status:
                                                                        description:
                                                                            - The status of an object that can be set to value 1 for shallow references across
                                                                              objects, other values reserved.
                                                                        type: int
                                                                    description:
                                                                        description:
                                                                            - A user-defined description for the object.
                                                                        type: str
                                                            position:
                                                                description:
                                                                    - The position of the attribute.
                                                                    - Applicable when model_type is 'NATIVE_SHAPE_FIELD'
                                                                type: int
                                                            default_value_string:
                                                                description:
                                                                    - The default value.
                                                                    - Applicable when model_type is 'NATIVE_SHAPE_FIELD'
                                                                type: str
                                                            is_mandatory:
                                                                description:
                                                                    - Specifies whether the field is mandatory.
                                                                    - Applicable when model_type is 'NATIVE_SHAPE_FIELD'
                                                                type: bool
                                                    config_definition:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is one of ['DATA_TYPE', 'CONFIGURED_TYPE', 'COMPOSITE_TYPE']
                                                        type: dict
                                                        suboptions:
                                                            key:
                                                                description:
                                                                    - The key of the object.
                                                                type: str
                                                            model_type:
                                                                description:
                                                                    - The type of the object.
                                                                type: str
                                                            model_version:
                                                                description:
                                                                    - The model version of an object.
                                                                type: str
                                                            parent_ref:
                                                                description:
                                                                    - ""
                                                                type: dict
                                                            name:
                                                                description:
                                                                    - Free form text without any restriction on the permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            is_contained:
                                                                description:
                                                                    - Specifies whether the configuration is contained.
                                                                type: bool
                                                            object_status:
                                                                description:
                                                                    - The status of an object that can be set to value 1 for shallow references across objects,
                                                                      other values reserved.
                                                                type: int
                                                            config_parameter_definitions:
                                                                description:
                                                                    - The parameter configuration details.
                                                                type: dict
                                            parameter_name:
                                                description:
                                                    - This object represents the configurable properties for an object type.
                                                type: str
                                            description:
                                                description:
                                                    - A user-defined description for the object.
                                                type: str
                                            default_value:
                                                description:
                                                    - The default value for the parameter.
                                                type: dict
                                            class_field_name:
                                                description:
                                                    - The parameter class field name.
                                                type: str
                                            is_static:
                                                description:
                                                    - Specifies whether the parameter is static.
                                                type: bool
                                            is_class_field_value:
                                                description:
                                                    - Specifies whether the parameter is a class field.
                                                type: bool
            registry_metadata:
                description:
                    - ""
                type: dict
                suboptions:
                    aggregator_key:
                        description:
                            - The owning object's key for this object.
                        type: str
                    labels:
                        description:
                            - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them
                              to categorize content.
                        type: list
                        elements: str
                    registry_version:
                        description:
                            - The registry version.
                        type: int
                    key:
                        description:
                            - The identifying key for the object.
                        type: str
                    is_favorite:
                        description:
                            - Specifies whether the object is a favorite.
                        type: bool
                    created_by_user_id:
                        description:
                            - The ID of the user who created the object.
                        type: str
                    created_by_user_name:
                        description:
                            - The name of the user who created the object.
                        type: str
                    updated_by_user_id:
                        description:
                            - The ID of the user who updated the object.
                        type: str
                    updated_by_user_name:
                        description:
                            - The name of the user who updated the object.
                        type: str
                    time_created:
                        description:
                            - The date and time that the object was created.
                        type: str
                    time_updated:
                        description:
                            - The date and time that the object was updated.
                        type: str
            metadata:
                description:
                    - ""
                type: dict
                suboptions:
                    created_by:
                        description:
                            - The user that created the object.
                        type: str
                    created_by_name:
                        description:
                            - The user that created the object.
                        type: str
                    updated_by:
                        description:
                            - The user that updated the object.
                        type: str
                    updated_by_name:
                        description:
                            - The user that updated the object.
                        type: str
                    time_created:
                        description:
                            - The date and time that the object was created.
                        type: str
                    time_updated:
                        description:
                            - The date and time that the object was updated.
                        type: str
                    aggregator_key:
                        description:
                            - The owning object key for this object.
                        type: str
                    aggregator:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            type:
                                description:
                                    - The type of the aggregator.
                                type: str
                            key:
                                description:
                                    - The key of the aggregator object.
                                type: str
                            name:
                                description:
                                    - The name of the aggregator.
                                type: str
                            identifier:
                                description:
                                    - The identifier of the aggregator.
                                type: str
                            description:
                                description:
                                    - The description of the aggregator.
                                type: str
                    identifier_path:
                        description:
                            - The full path to identify the object.
                        type: str
                    info_fields:
                        description:
                            - Information property fields.
                        type: dict
                    registry_version:
                        description:
                            - The registry version of the object.
                        type: int
                    labels:
                        description:
                            - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                              categorize content.
                        type: list
                        elements: str
                    is_favorite:
                        description:
                            - Specifies whether this object is a favorite.
                        type: bool
            default_connection:
                description:
                    - ""
                type: dict
                suboptions:
                    key:
                        description:
                            - Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is
                              required, a value can be passed in create.
                        type: str
                        required: true
                    model_version:
                        description:
                            - The model version of an object.
                        type: str
                    model_type:
                        description:
                            - The type of the object.
                        type: str
                    name:
                        description:
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                        type: str
                        required: true
                    description:
                        description:
                            - User-defined description for the connection.
                        type: str
                    object_version:
                        description:
                            - The version of the object that is used to track changes in the object instance.
                        type: int
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                        type: int
                    identifier:
                        description:
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The
                              value can be modified.
                        type: str
                        required: true
                    primary_schema:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            key:
                                description:
                                    - The object key.
                                type: str
                                required: true
                            model_type:
                                description:
                                    - The object type.
                                type: str
                                required: true
                            model_version:
                                description:
                                    - The model version of the object.
                                type: str
                            parent_ref:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    parent:
                                        description:
                                            - Key of the parent object.
                                        type: str
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                                required: true
                            resource_name:
                                description:
                                    - A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000
                                      characters.
                                type: str
                            description:
                                description:
                                    - User-defined description for the schema.
                                type: str
                            object_version:
                                description:
                                    - The version of the object that is used to track changes in the object instance.
                                type: int
                            external_key:
                                description:
                                    - The external key of the object.
                                type: str
                            is_has_containers:
                                description:
                                    - Specifies whether the schema has containers.
                                type: bool
                            default_connection:
                                description:
                                    - The default connection key.
                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            identifier:
                                description:
                                    - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or
                                      underscore. The value can be modified.
                                type: str
                                required: true
                            metadata:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    created_by:
                                        description:
                                            - The user that created the object.
                                        type: str
                                    created_by_name:
                                        description:
                                            - The user that created the object.
                                        type: str
                                    updated_by:
                                        description:
                                            - The user that updated the object.
                                        type: str
                                    updated_by_name:
                                        description:
                                            - The user that updated the object.
                                        type: str
                                    time_created:
                                        description:
                                            - The date and time that the object was created.
                                        type: str
                                    time_updated:
                                        description:
                                            - The date and time that the object was updated.
                                        type: str
                                    aggregator_key:
                                        description:
                                            - The owning object key for this object.
                                        type: str
                                    aggregator:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            type:
                                                description:
                                                    - The type of the aggregator.
                                                type: str
                                            key:
                                                description:
                                                    - The key of the aggregator object.
                                                type: str
                                            name:
                                                description:
                                                    - The name of the aggregator.
                                                type: str
                                            identifier:
                                                description:
                                                    - The identifier of the aggregator.
                                                type: str
                                            description:
                                                description:
                                                    - The description of the aggregator.
                                                type: str
                                    identifier_path:
                                        description:
                                            - The full path to identify the object.
                                        type: str
                                    info_fields:
                                        description:
                                            - Information property fields.
                                        type: dict
                                    registry_version:
                                        description:
                                            - The registry version of the object.
                                        type: int
                                    labels:
                                        description:
                                            - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels
                                              and use them to categorize content.
                                        type: list
                                        elements: str
                                    is_favorite:
                                        description:
                                            - Specifies whether this object is a favorite.
                                        type: bool
                    connection_properties:
                        description:
                            - The properties of the connection.
                        type: list
                        elements: dict
                        suboptions:
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                            value:
                                description:
                                    - The value for the connection name property.
                                type: str
                    properties:
                        description:
                            - All the properties of the connection in a key-value map format.
                        type: dict
                    type:
                        description:
                            - Specific Connection Type
                        type: str
                    is_default:
                        description:
                            - The default property of the connection.
                        type: bool
                    metadata:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            created_by:
                                description:
                                    - The user that created the object.
                                type: str
                            created_by_name:
                                description:
                                    - The user that created the object.
                                type: str
                            updated_by:
                                description:
                                    - The user that updated the object.
                                type: str
                            updated_by_name:
                                description:
                                    - The user that updated the object.
                                type: str
                            time_created:
                                description:
                                    - The date and time that the object was created.
                                type: str
                            time_updated:
                                description:
                                    - The date and time that the object was updated.
                                type: str
                            aggregator_key:
                                description:
                                    - The owning object key for this object.
                                type: str
                            aggregator:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    type:
                                        description:
                                            - The type of the aggregator.
                                        type: str
                                    key:
                                        description:
                                            - The key of the aggregator object.
                                        type: str
                                    name:
                                        description:
                                            - The name of the aggregator.
                                        type: str
                                    identifier:
                                        description:
                                            - The identifier of the aggregator.
                                        type: str
                                    description:
                                        description:
                                            - The description of the aggregator.
                                        type: str
                            identifier_path:
                                description:
                                    - The full path to identify the object.
                                type: str
                            info_fields:
                                description:
                                    - Information property fields.
                                type: dict
                            registry_version:
                                description:
                                    - The registry version of the object.
                                type: int
                            labels:
                                description:
                                    - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use
                                      them to categorize content.
                                type: list
                                elements: str
                            is_favorite:
                                description:
                                    - Specifies whether this object is a favorite.
                                type: bool
                    registry_metadata:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            aggregator_key:
                                description:
                                    - The owning object's key for this object.
                                type: str
                            labels:
                                description:
                                    - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and
                                      use them to categorize content.
                                type: list
                                elements: str
                            registry_version:
                                description:
                                    - The registry version.
                                type: int
                            key:
                                description:
                                    - The identifying key for the object.
                                type: str
                            is_favorite:
                                description:
                                    - Specifies whether the object is a favorite.
                                type: bool
                            created_by_user_id:
                                description:
                                    - The ID of the user who created the object.
                                type: str
                            created_by_user_name:
                                description:
                                    - The name of the user who created the object.
                                type: str
                            updated_by_user_id:
                                description:
                                    - The ID of the user who updated the object.
                                type: str
                            updated_by_user_name:
                                description:
                                    - The name of the user who updated the object.
                                type: str
                            time_created:
                                description:
                                    - The date and time that the object was created.
                                type: str
                            time_updated:
                                description:
                                    - The date and time that the object was updated.
                                type: str
            end_points:
                description:
                    - The list of endpoints with which this data asset is associated.
                type: list
                elements: dict
                suboptions:
                    dcms_endpoint_id:
                        description:
                            - The endpoint ID provided by control plane.
                            - Required when model_type is 'PRIVATE_END_POINT'
                        type: str
                    pe_id:
                        description:
                            - The OCID of the private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    compartment_id:
                        description:
                            - The compartmentId of the private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    dns_proxy_ip:
                        description:
                            - The IP address of the DNS proxy.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    private_endpoint_ip:
                        description:
                            - The OCID of the private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    dns_zones:
                        description:
                            - Array of DNS zones to be used during the private endpoint resolution.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: list
                        elements: str
                    state:
                        description:
                            - Specifies the private endpoint state.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                        choices:
                            - "ACTIVE"
                            - "INACTIVE"
                    model_type:
                        description:
                            - The type of the endpoint.
                        type: str
                        choices:
                            - "PRIVATE_END_POINT"
                            - "PUBLIC_END_POINT"
                        required: true
                    key:
                        description:
                            - Generated key that can be used in API calls to identify the endpoint. In scenarios where reference to the endpoint is required, a
                              value can be passed in create.
                        type: str
                    model_version:
                        description:
                            - The model version of an object.
                        type: str
                    parent_ref:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                    - Applicable when model_type is 'PRIVATE_END_POINT'
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                        type: str
                    description:
                        description:
                            - User-defined description of the endpoint.
                        type: str
                    object_version:
                        description:
                            - The version of the object that is used to track changes in the object instance.
                        type: int
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                        type: int
                    identifier:
                        description:
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The
                              value can be modified.
                        type: str
                    data_assets:
                        description:
                            - The list of data assets that belong to the endpoint.
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                    - Currently not used while creating a data asset. Reserved for future.
                                type: str
                                required: true
                            model_version:
                                description:
                                    - The model version of an object.
                                type: str
                            model_type:
                                description:
                                    - The type of the object.
                                type: str
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                                required: true
                            description:
                                description:
                                    - User-defined description of the data asset.
                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            object_version:
                                description:
                                    - The version of the object that is used to track changes in the object instance.
                                type: int
                            identifier:
                                description:
                                    - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or
                                      underscore. The value can be modified.
                                type: str
                                required: true
                            external_key:
                                description:
                                    - The external key of the object.
                                type: str
                            asset_properties:
                                description:
                                    - Additional properties for the data asset.
                                type: dict
                            properties:
                                description:
                                    - All the properties for the data asset in a key-value map format.
                                type: dict
                            type:
                                description:
                                    - Specific DataAsset Type
                                type: str
                            native_type_system:
                                description:
                                    - ""
                                type: dict
                            registry_metadata:
                                description:
                                    - ""
                                type: dict
                            metadata:
                                description:
                                    - ""
                                type: dict
                            default_connection:
                                description:
                                    - ""
                                type: dict
                            end_points:
                                description:
                                    - The list of endpoints with which this data asset is associated.
                                type: list
                                elements: dict
    action:
        description:
            - The action to perform on the DetachDataAssetInfo.
        type: str
        required: true
        choices:
            - "create_detach_data_asset"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action create_detach_data_asset on detach_data_asset_info
  oci_data_connectivity_detach_data_asset_info_actions:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"
    data_assets:
    - # required
      key: key_example
      name: name_example
      identifier: identifier_example

      # optional
      model_version: model_version_example
      model_type: model_type_example
      description: description_example
      object_status: 56
      object_version: 56
      external_key: external_key_example
      asset_properties: null
      properties: null
      type: type_example
      native_type_system:
        # optional
        key: key_example
        model_type: model_type_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        description: description_example
        object_version: 56
        type_mapping_to: null
        type_mapping_from: null
        object_status: 56
        identifier: identifier_example
        types:
        - # required
          model_type: STRUCTURED_TYPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          name: name_example
          object_status: 56
          description: description_example
          dt_type: PRIMITIVE
          type_system_name: type_system_name_example
          config_definition:
            # optional
            key: key_example
            model_type: model_type_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
            name: name_example
            is_contained: true
            object_status: 56
            config_parameter_definitions:
              # optional
              parameter_type:
                # required
                model_type: CONFIGURED_TYPE

                # optional
                wrapped_type:
                  # required
                  model_type: STRUCTURED_TYPE

                  # optional
                  key: key_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  object_status: 56
                  description: description_example
                config_values:
                  # optional
                  config_param_values:
                    # optional
                    string_value: string_value_example
                    int_value: 56
                    object_value: null
                    ref_value: null
                    parameter_value: parameter_value_example
                  parent_ref:
                    # optional
                    parent: parent_example
                key: key_example
                model_version: model_version_example
                parent_ref:
                  # optional
                  parent: parent_example
                name: name_example
                object_status: 56
                description: description_example
                config_definition:
                  # optional
                  key: key_example
                  model_type: model_type_example
                  model_version: model_version_example
                  parent_ref: null
                  name: name_example
                  is_contained: true
                  object_status: 56
                  config_parameter_definitions: null
              parameter_name: parameter_name_example
              description: description_example
              default_value: null
              class_field_name: class_field_name_example
              is_static: true
              is_class_field_value: true
      registry_metadata:
        # optional
        aggregator_key: aggregator_key_example
        labels: [ "labels_example" ]
        registry_version: 56
        key: key_example
        is_favorite: true
        created_by_user_id: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
        created_by_user_name: created_by_user_name_example
        updated_by_user_id: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_user_name: updated_by_user_name_example
        time_created: time_created_example
        time_updated: time_updated_example
      metadata:
        # optional
        created_by: created_by_example
        created_by_name: created_by_name_example
        updated_by: updated_by_example
        updated_by_name: updated_by_name_example
        time_created: time_created_example
        time_updated: time_updated_example
        aggregator_key: aggregator_key_example
        aggregator:
          # optional
          type: type_example
          key: key_example
          name: name_example
          identifier: identifier_example
          description: description_example
        identifier_path: identifier_path_example
        info_fields: null
        registry_version: 56
        labels: [ "labels_example" ]
        is_favorite: true
      default_connection:
        # required
        key: key_example
        name: name_example
        identifier: identifier_example

        # optional
        model_version: model_version_example
        model_type: model_type_example
        description: description_example
        object_version: 56
        object_status: 56
        primary_schema:
          # required
          key: key_example
          model_type: model_type_example
          name: name_example
          identifier: identifier_example

          # optional
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
          resource_name: resource_name_example
          description: description_example
          object_version: 56
          external_key: external_key_example
          is_has_containers: true
          default_connection: default_connection_example
          object_status: 56
          metadata:
            # optional
            created_by: created_by_example
            created_by_name: created_by_name_example
            updated_by: updated_by_example
            updated_by_name: updated_by_name_example
            time_created: time_created_example
            time_updated: time_updated_example
            aggregator_key: aggregator_key_example
            aggregator:
              # optional
              type: type_example
              key: key_example
              name: name_example
              identifier: identifier_example
              description: description_example
            identifier_path: identifier_path_example
            info_fields: null
            registry_version: 56
            labels: [ "labels_example" ]
            is_favorite: true
        connection_properties:
        - # optional
          name: name_example
          value: value_example
        properties: null
        type: type_example
        is_default: true
        metadata:
          # optional
          created_by: created_by_example
          created_by_name: created_by_name_example
          updated_by: updated_by_example
          updated_by_name: updated_by_name_example
          time_created: time_created_example
          time_updated: time_updated_example
          aggregator_key: aggregator_key_example
          aggregator:
            # optional
            type: type_example
            key: key_example
            name: name_example
            identifier: identifier_example
            description: description_example
          identifier_path: identifier_path_example
          info_fields: null
          registry_version: 56
          labels: [ "labels_example" ]
          is_favorite: true
        registry_metadata:
          # optional
          aggregator_key: aggregator_key_example
          labels: [ "labels_example" ]
          registry_version: 56
          key: key_example
          is_favorite: true
          created_by_user_id: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
          created_by_user_name: created_by_user_name_example
          updated_by_user_id: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
          updated_by_user_name: updated_by_user_name_example
          time_created: time_created_example
          time_updated: time_updated_example
      end_points:
      - # required
        dcms_endpoint_id: "ocid1.dcmsendpoint.oc1..xxxxxxEXAMPLExxxxxx"
        model_type: PRIVATE_END_POINT

        # optional
        pe_id: "ocid1.pe.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dns_proxy_ip: dns_proxy_ip_example
        private_endpoint_ip: private_endpoint_ip_example
        dns_zones: [ "dns_zones_example" ]
        state: ACTIVE
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        description: description_example
        object_version: 56
        object_status: 56
        identifier: identifier_example
        data_assets:
        - # required
          key: key_example
          name: name_example
          identifier: identifier_example

          # optional
          model_version: model_version_example
          model_type: model_type_example
          description: description_example
          object_status: 56
          object_version: 56
          external_key: external_key_example
          asset_properties: null
          properties: null
          type: type_example
          native_type_system: null
          registry_metadata: null
          metadata: null
          default_connection: null
          end_points: [ "end_points_example" ]
    action: create_detach_data_asset

"""

RETURN = """
detach_data_asset_info:
    description:
        - Details of the DetachDataAssetInfo resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        reference_info:
            description:
                - Mapping the DataAsset name as the key to the results as the value.
            returned: on success
            type: complex
            contains:
                error_msg:
                    description:
                        - Error text for validation failure.
                    returned: on success
                    type: str
                    sample: error_msg_example
                status:
                    description:
                        - Status of the validation result execution.
                    returned: on success
                    type: str
                    sample: ERROR
    sample: {
        "reference_info": {
            "error_msg": "error_msg_example",
            "status": "ERROR"
        }
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient
    from oci.data_connectivity.models import CreateDetachDataAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DetachDataAssetInfoActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        create_detach_data_asset
    """

    @staticmethod
    def get_module_resource_id_param():
        return "endpoint_id"

    def get_module_resource_id(self):
        return self.module.params.get("endpoint_id")

    def create_detach_data_asset(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CreateDetachDataAssetDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_detach_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                endpoint_id=self.module.params.get("endpoint_id"),
                create_detach_data_asset_details=action_details,
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


DetachDataAssetInfoActionsHelperCustom = get_custom_class(
    "DetachDataAssetInfoActionsHelperCustom"
)


class ResourceHelper(
    DetachDataAssetInfoActionsHelperCustom, DetachDataAssetInfoActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            registry_id=dict(type="str", required=True),
            endpoint_id=dict(aliases=["id"], type="str", required=True),
            data_assets=dict(
                type="list",
                elements="dict",
                required=True,
                options=dict(
                    key=dict(type="str", required=True, no_log=True),
                    model_version=dict(type="str"),
                    model_type=dict(type="str"),
                    name=dict(type="str", required=True),
                    description=dict(type="str"),
                    object_status=dict(type="int"),
                    object_version=dict(type="int"),
                    identifier=dict(type="str", required=True),
                    external_key=dict(type="str", no_log=True),
                    asset_properties=dict(type="dict"),
                    properties=dict(type="dict"),
                    type=dict(type="str"),
                    native_type_system=dict(
                        type="dict",
                        options=dict(
                            key=dict(type="str", no_log=True),
                            model_type=dict(type="str"),
                            model_version=dict(type="str"),
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
                            ),
                            name=dict(type="str"),
                            description=dict(type="str"),
                            object_version=dict(type="int"),
                            type_mapping_to=dict(type="dict"),
                            type_mapping_from=dict(type="dict"),
                            object_status=dict(type="int"),
                            identifier=dict(type="str"),
                            types=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "STRUCTURED_TYPE",
                                            "DATA_TYPE",
                                            "CONFIGURED_TYPE",
                                            "COMPOSITE_TYPE",
                                            "DERIVED_TYPE",
                                        ],
                                    ),
                                    key=dict(type="str", no_log=True),
                                    model_version=dict(type="str"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
                                    ),
                                    name=dict(type="str"),
                                    object_status=dict(type="int"),
                                    description=dict(type="str"),
                                    dt_type=dict(
                                        type="str", choices=["PRIMITIVE", "STRUCTURED"]
                                    ),
                                    type_system_name=dict(type="str"),
                                    config_definition=dict(
                                        type="dict",
                                        options=dict(
                                            key=dict(type="str", no_log=True),
                                            model_type=dict(type="str"),
                                            model_version=dict(type="str"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                            name=dict(type="str"),
                                            is_contained=dict(type="bool"),
                                            object_status=dict(type="int"),
                                            config_parameter_definitions=dict(
                                                type="dict"
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    registry_metadata=dict(
                        type="dict",
                        options=dict(
                            aggregator_key=dict(type="str", no_log=True),
                            labels=dict(type="list", elements="str"),
                            registry_version=dict(type="int"),
                            key=dict(type="str", no_log=True),
                            is_favorite=dict(type="bool"),
                            created_by_user_id=dict(type="str"),
                            created_by_user_name=dict(type="str"),
                            updated_by_user_id=dict(type="str"),
                            updated_by_user_name=dict(type="str"),
                            time_created=dict(type="str"),
                            time_updated=dict(type="str"),
                        ),
                    ),
                    metadata=dict(
                        type="dict",
                        options=dict(
                            created_by=dict(type="str"),
                            created_by_name=dict(type="str"),
                            updated_by=dict(type="str"),
                            updated_by_name=dict(type="str"),
                            time_created=dict(type="str"),
                            time_updated=dict(type="str"),
                            aggregator_key=dict(type="str", no_log=True),
                            aggregator=dict(
                                type="dict",
                                options=dict(
                                    type=dict(type="str"),
                                    key=dict(type="str", no_log=True),
                                    name=dict(type="str"),
                                    identifier=dict(type="str"),
                                    description=dict(type="str"),
                                ),
                            ),
                            identifier_path=dict(type="str"),
                            info_fields=dict(type="dict"),
                            registry_version=dict(type="int"),
                            labels=dict(type="list", elements="str"),
                            is_favorite=dict(type="bool"),
                        ),
                    ),
                    default_connection=dict(
                        type="dict",
                        options=dict(
                            key=dict(type="str", required=True, no_log=True),
                            model_version=dict(type="str"),
                            model_type=dict(type="str"),
                            name=dict(type="str", required=True),
                            description=dict(type="str"),
                            object_version=dict(type="int"),
                            object_status=dict(type="int"),
                            identifier=dict(type="str", required=True),
                            primary_schema=dict(
                                type="dict",
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    model_type=dict(type="str", required=True),
                                    model_version=dict(type="str"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
                                    ),
                                    name=dict(type="str", required=True),
                                    resource_name=dict(type="str"),
                                    description=dict(type="str"),
                                    object_version=dict(type="int"),
                                    external_key=dict(type="str", no_log=True),
                                    is_has_containers=dict(type="bool"),
                                    default_connection=dict(type="str"),
                                    object_status=dict(type="int"),
                                    identifier=dict(type="str", required=True),
                                    metadata=dict(
                                        type="dict",
                                        options=dict(
                                            created_by=dict(type="str"),
                                            created_by_name=dict(type="str"),
                                            updated_by=dict(type="str"),
                                            updated_by_name=dict(type="str"),
                                            time_created=dict(type="str"),
                                            time_updated=dict(type="str"),
                                            aggregator_key=dict(
                                                type="str", no_log=True
                                            ),
                                            aggregator=dict(
                                                type="dict",
                                                options=dict(
                                                    type=dict(type="str"),
                                                    key=dict(type="str", no_log=True),
                                                    name=dict(type="str"),
                                                    identifier=dict(type="str"),
                                                    description=dict(type="str"),
                                                ),
                                            ),
                                            identifier_path=dict(type="str"),
                                            info_fields=dict(type="dict"),
                                            registry_version=dict(type="int"),
                                            labels=dict(type="list", elements="str"),
                                            is_favorite=dict(type="bool"),
                                        ),
                                    ),
                                ),
                            ),
                            connection_properties=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    name=dict(type="str"), value=dict(type="str")
                                ),
                            ),
                            properties=dict(type="dict"),
                            type=dict(type="str"),
                            is_default=dict(type="bool"),
                            metadata=dict(
                                type="dict",
                                options=dict(
                                    created_by=dict(type="str"),
                                    created_by_name=dict(type="str"),
                                    updated_by=dict(type="str"),
                                    updated_by_name=dict(type="str"),
                                    time_created=dict(type="str"),
                                    time_updated=dict(type="str"),
                                    aggregator_key=dict(type="str", no_log=True),
                                    aggregator=dict(
                                        type="dict",
                                        options=dict(
                                            type=dict(type="str"),
                                            key=dict(type="str", no_log=True),
                                            name=dict(type="str"),
                                            identifier=dict(type="str"),
                                            description=dict(type="str"),
                                        ),
                                    ),
                                    identifier_path=dict(type="str"),
                                    info_fields=dict(type="dict"),
                                    registry_version=dict(type="int"),
                                    labels=dict(type="list", elements="str"),
                                    is_favorite=dict(type="bool"),
                                ),
                            ),
                            registry_metadata=dict(
                                type="dict",
                                options=dict(
                                    aggregator_key=dict(type="str", no_log=True),
                                    labels=dict(type="list", elements="str"),
                                    registry_version=dict(type="int"),
                                    key=dict(type="str", no_log=True),
                                    is_favorite=dict(type="bool"),
                                    created_by_user_id=dict(type="str"),
                                    created_by_user_name=dict(type="str"),
                                    updated_by_user_id=dict(type="str"),
                                    updated_by_user_name=dict(type="str"),
                                    time_created=dict(type="str"),
                                    time_updated=dict(type="str"),
                                ),
                            ),
                        ),
                    ),
                    end_points=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            dcms_endpoint_id=dict(type="str"),
                            pe_id=dict(type="str"),
                            compartment_id=dict(type="str"),
                            dns_proxy_ip=dict(type="str"),
                            private_endpoint_ip=dict(type="str"),
                            dns_zones=dict(type="list", elements="str"),
                            state=dict(type="str", choices=["ACTIVE", "INACTIVE"]),
                            model_type=dict(
                                type="str",
                                required=True,
                                choices=["PRIVATE_END_POINT", "PUBLIC_END_POINT"],
                            ),
                            key=dict(type="str", no_log=True),
                            model_version=dict(type="str"),
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
                            ),
                            name=dict(type="str"),
                            description=dict(type="str"),
                            object_version=dict(type="int"),
                            object_status=dict(type="int"),
                            identifier=dict(type="str"),
                            data_assets=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    key=dict(type="str", required=True, no_log=True),
                                    model_version=dict(type="str"),
                                    model_type=dict(type="str"),
                                    name=dict(type="str", required=True),
                                    description=dict(type="str"),
                                    object_status=dict(type="int"),
                                    object_version=dict(type="int"),
                                    identifier=dict(type="str", required=True),
                                    external_key=dict(type="str", no_log=True),
                                    asset_properties=dict(type="dict"),
                                    properties=dict(type="dict"),
                                    type=dict(type="str"),
                                    native_type_system=dict(type="TypeSystem"),
                                    registry_metadata=dict(type="RegistryMetadata"),
                                    metadata=dict(type="ObjectMetadata"),
                                    default_connection=dict(type="Connection"),
                                    end_points=dict(type="list", elements="dict"),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            action=dict(
                type="str", required=True, choices=["create_detach_data_asset"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="detach_data_asset_info",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
