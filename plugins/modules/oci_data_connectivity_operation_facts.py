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
module: oci_data_connectivity_operation_facts
short_description: Fetches details about one or multiple Operation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Operation resources in Oracle Cloud Infrastructure
    - Lists the summary of operations that are present in the schema, identified by the schema name.
    - If I(operation_resource_name) is specified, the details of a single Operation will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operation_resource_name:
        description:
            - The operation resource name used for retrieving the details of operation.
            - Required to get a specific operation.
        type: str
    registry_id:
        description:
            - The registry OCID.
        type: str
        required: true
    connection_key:
        description:
            - The connection key.
        type: str
        required: true
    schema_resource_name:
        description:
            - The schema resource name used for retrieving schemas.
        type: str
        required: true
    name:
        description:
            - Used to filter by the name of the object.
        type: str
    sort_by:
        description:
            - Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other
              fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order
              are by relevance score in descending order).
        type: str
        choices:
            - "id"
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - Specifies sort order to use, either `ASC` (ascending) or `DESC` (descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
    endpoint_id:
        description:
            - Endpoint ID used for getDataAssetFullDetails.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific operation
  oci_data_connectivity_operation_facts:
    # required
    operation_resource_name: operation_resource_name_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    connection_key: connection_key_example
    schema_resource_name: schema_resource_name_example

    # optional
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: List operations
  oci_data_connectivity_operation_facts:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    connection_key: connection_key_example
    schema_resource_name: schema_resource_name_example

    # optional
    name: name_example
    sort_by: id
    sort_order: ASC
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
operations:
    description:
        - List of Operation resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The object key.
                - Returned for get operation
            returned: on success
            type: str
            sample: key_example
        model_version:
            description:
                - The model version of the object.
                - Returned for get operation
            returned: on success
            type: str
            sample: model_version_example
        parent_ref:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                parent:
                    description:
                        - Key of the parent object.
                    returned: on success
                    type: str
                    sample: parent_example
        shape:
            description:
                - ""
                - Returned for get operation
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
                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value
                          is editable and is restricted to 1000 characters.
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
                                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                    returned: on success
                                    type: int
                                    sample: 56
                                name:
                                    description:
                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                          characters. The value is editable and is restricted to 1000 characters.
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
                                        - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels
                                          and use them to categorize content.
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
                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                          characters. The value is editable and is restricted to 1000 characters.
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
                                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
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
                                                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers,
                                                          and special characters. The value is editable and is restricted to 1000 characters.
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
                                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters.
                                  The value is editable and is restricted to 1000 characters.
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
        name:
            description:
                - The operation name.
                - Returned for get operation
            returned: on success
            type: str
            sample: name_example
        object_version:
            description:
                - The version of the object that is used to track changes in the object instance.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        external_key:
            description:
                - The external key of the object.
                - Returned for get operation
            returned: on success
            type: str
            sample: external_key_example
        resource_name:
            description:
                - The resource name.
                - Returned for get operation
            returned: on success
            type: str
            sample: resource_name_example
        object_status:
            description:
                - The status of an object that can be set to value 1 for shallow reference across objects, other values reserved.
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        model_type:
            description:
                - The operation type.
            returned: on success
            type: str
            sample: PROCEDURE
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
                        - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                          categorize content.
                    returned: on success
                    type: list
                    sample: []
                is_favorite:
                    description:
                        - Specifies whether this object is a favorite.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
        "key": "key_example",
        "model_version": "model_version_example",
        "parent_ref": {
            "parent": "parent_example"
        },
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
        "name": "name_example",
        "object_version": 56,
        "external_key": "external_key_example",
        "resource_name": "resource_name_example",
        "object_status": 56,
        "model_type": "PROCEDURE",
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
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_connectivity import DataConnectivityManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "registry_id",
            "connection_key",
            "schema_resource_name",
            "operation_resource_name",
        ]

    def get_required_params_for_list(self):
        return [
            "registry_id",
            "connection_key",
            "schema_resource_name",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "endpoint_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_operation,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
            schema_resource_name=self.module.params.get("schema_resource_name"),
            operation_resource_name=self.module.params.get("operation_resource_name"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_by",
            "sort_order",
            "endpoint_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_operations,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
            schema_resource_name=self.module.params.get("schema_resource_name"),
            **optional_kwargs
        )


OperationFactsHelperCustom = get_custom_class("OperationFactsHelperCustom")


class ResourceFactsHelper(OperationFactsHelperCustom, OperationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            operation_resource_name=dict(type="str"),
            registry_id=dict(type="str", required=True),
            connection_key=dict(type="str", required=True, no_log=True),
            schema_resource_name=dict(type="str", required=True),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["id", "timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            endpoint_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="operation",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(operations=result)


if __name__ == "__main__":
    main()
