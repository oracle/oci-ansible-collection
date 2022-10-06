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
module: oci_data_connectivity_data_entity_actions
short_description: Perform actions on a DataEntity resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DataEntity resource in Oracle Cloud Infrastructure
    - For I(action=create_entity_shape), creates the data entity shape using the shape from the data asset.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
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
    sql_query:
        description:
            - sqlQuery
            - Applicable when model_type is 'SQL_ENTITY'
        type: str
    data_format:
        description:
            - ""
            - Applicable when model_type is 'FILE_ENTITY'
        type: dict
        suboptions:
            format_attribute:
                description:
                    - ""
                    - Applicable when model_type is 'FILE_ENTITY'
                type: dict
                suboptions:
                    encoding:
                        description:
                            - The encoding for the file.
                            - Applicable when model_type is one of ['CSV_FORMAT', 'JSON_FORMAT']
                        type: str
                    escape_character:
                        description:
                            - The escape character for the CSV format.
                            - Applicable when model_type is 'CSV_FORMAT'
                        type: str
                    delimiter:
                        description:
                            - The delimiter for the CSV format.
                            - Applicable when model_type is 'CSV_FORMAT'
                        type: str
                    quote_character:
                        description:
                            - The quote character for the CSV format.
                            - Applicable when model_type is 'CSV_FORMAT'
                        type: str
                    has_header:
                        description:
                            - Defines whether the file has a header row.
                            - Applicable when model_type is 'CSV_FORMAT'
                        type: bool
                    is_file_pattern:
                        description:
                            - Defines whether a file pattern is supported.
                            - Applicable when model_type is 'CSV_FORMAT'
                        type: bool
                    timestamp_format:
                        description:
                            - Format for timestamp information.
                            - Applicable when model_type is 'CSV_FORMAT'
                        type: str
                    compression:
                        description:
                            - The compression for the file.
                            - Applicable when model_type is one of ['PARQUET_FORMAT', 'AVRO_FORMAT']
                        type: str
                    model_type:
                        description:
                            - The type of the format attribute.
                        type: str
                        choices:
                            - "AVRO_FORMAT"
                            - "JSON_FORMAT"
                            - "CSV_FORMAT"
                            - "PARQUET_FORMAT"
                            - "EXCEL_FORMAT"
                        required: true
                    data_address:
                        description:
                            - "Range of the data. For example, \\"'My Sheet'!B3:C35\\""
                            - Applicable when model_type is 'EXCEL_FORMAT'
                        type: str
                    header:
                        description:
                            - "Whether the dataAddress contains the header with column names. If false - column names fill be generated."
                            - Applicable when model_type is 'EXCEL_FORMAT'
                        type: bool
                    password:
                        description:
                            - Workbook password if it is password protected.
                            - Applicable when model_type is 'EXCEL_FORMAT'
                        type: str
            type:
                description:
                    - type
                    - Required when model_type is 'FILE_ENTITY'
                type: str
                choices:
                    - "JSON"
                    - "CSV"
                    - "PARQUET"
                    - "AVRO"
                required: true
            compression_config:
                description:
                    - ""
                    - Applicable when model_type is 'FILE_ENTITY'
                type: dict
                suboptions:
                    codec:
                        description:
                            - Compression algorithm
                            - Required when model_type is 'FILE_ENTITY'
                        type: str
                        choices:
                            - "NONE"
                            - "AUTO"
                            - "GZIP"
                            - "BZIP2"
                            - "DEFLATE"
                            - "LZ4"
                            - "SNAPPY"
                        required: true
    model_type:
        description:
            - The data entity type.
        type: str
        choices:
            - "DATA_STORE_ENTITY"
            - "TABLE_ENTITY"
            - "SQL_ENTITY"
            - "FILE_ENTITY"
            - "VIEW_ENTITY"
        required: true
    key:
        description:
            - The object key.
        type: str
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
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
    name:
        description:
            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable
              and is restricted to 1000 characters.
        type: str
        required: true
    object_version:
        description:
            - The version of the object that is used to track changes in the object instance.
        type: int
    external_key:
        description:
            - The external key of the object.
        type: str
    shape:
        description:
            - ""
        type: dict
        suboptions:
            model_type:
                description:
                    - The type of the types object.
                    - Required when model_type is 'DATA_STORE_ENTITY'
                type: str
                choices:
                    - "SHAPE"
                    - "SHAPE_FIELD"
                    - "NATIVE_SHAPE_FIELD"
                required: true
            key:
                description:
                    - The key of the object.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            model_version:
                description:
                    - The model version of an object.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            parent_ref:
                description:
                    - ""
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: dict
                suboptions:
                    parent:
                        description:
                            - Key of the parent object.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: str
            config_values:
                description:
                    - ""
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: dict
                suboptions:
                    config_param_values:
                        description:
                            - The configuration parameter values.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: dict
                        suboptions:
                            string_value:
                                description:
                                    - A string value of the parameter.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: str
                            int_value:
                                description:
                                    - An integer value of the parameter.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: int
                            object_value:
                                description:
                                    - An object value of the parameter.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: dict
                            ref_value:
                                description:
                                    - The root object reference value.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: dict
                            parameter_value:
                                description:
                                    - Reference to the parameter by its key.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: str
                    parent_ref:
                        description:
                            - ""
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: str
            object_status:
                description:
                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: int
            name:
                description:
                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            description:
                description:
                    - A detailed description of the object.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            type:
                description:
                    - ""
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
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
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                        type: str
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
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
                                    - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and
                                      use them to categorize content.
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
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                            - Applicable when model_type is 'SHAPE_FIELD'
                                        type: int
                                    name:
                                        description:
                                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
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
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                        type: int
                                    name:
                                        description:
                                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
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
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
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
                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                type: str
                            model_type:
                                description:
                                    - The type of the object.
                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                type: str
                            model_version:
                                description:
                                    - The model version of an object.
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
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                type: str
                            is_contained:
                                description:
                                    - Specifies whether the configuration is contained.
                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                type: bool
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                type: int
                            config_parameter_definitions:
                                description:
                                    - The parameter configuration details.
                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                type: dict
                                suboptions:
                                    parameter_type:
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
                                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                type: str
                                            object_status:
                                                description:
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                type: int
                                            description:
                                                description:
                                                    - A user-defined description for the object.
                                                type: str
                                    parameter_name:
                                        description:
                                            - This object represents the configurable properties for an object type.
                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                        type: str
                                    description:
                                        description:
                                            - A user-defined description for the object.
                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                        type: str
                                    default_value:
                                        description:
                                            - The default value for the parameter.
                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                        type: dict
                                    class_field_name:
                                        description:
                                            - The parameter class field name.
                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                        type: str
                                    is_static:
                                        description:
                                            - Specifies whether the parameter is static.
                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                        type: bool
                                    is_class_field_value:
                                        description:
                                            - Specifies whether the parameter is a class field.
                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                        type: bool
    shape_id:
        description:
            - The shape ID.
        type: str
    entity_type:
        description:
            - The entity type.
        type: str
        choices:
            - "TABLE"
            - "VIEW"
            - "FILE"
            - "SQL"
    other_type_label:
        description:
            - Specifies other type label.
        type: str
    unique_keys:
        description:
            - An array of unique keys.
        type: list
        elements: dict
        suboptions:
            model_type:
                description:
                    - The key type.
                type: str
                choices:
                    - "PRIMARY_KEY"
                required: true
            key:
                description:
                    - The object key.
                type: str
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
                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                type: str
            attribute_refs:
                description:
                    - An array of attribute references.
                type: list
                elements: dict
                suboptions:
                    position:
                        description:
                            - The position of the attribute.
                        type: int
                    attribute:
                        description:
                            - ""
                        type: dict
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
                                suboptions:
                                    parent:
                                        description:
                                            - Key of the parent object.
                                        type: str
                            config_values:
                                description:
                                    - ""
                                type: dict
                                suboptions:
                                    config_param_values:
                                        description:
                                            - The configuration parameter values.
                                        type: dict
                                        suboptions:
                                            string_value:
                                                description:
                                                    - A string value of the parameter.
                                                type: str
                                            int_value:
                                                description:
                                                    - An integer value of the parameter.
                                                type: int
                                            object_value:
                                                description:
                                                    - An object value of the parameter.
                                                type: dict
                                            ref_value:
                                                description:
                                                    - The root object reference value.
                                                type: dict
                                            parameter_value:
                                                description:
                                                    - Reference to the parameter by its key.
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
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                type: str
                            description:
                                description:
                                    - A detailed description of the object.
                                type: str
                            type:
                                description:
                                    - The type reference.
                                type: dict
                            labels:
                                description:
                                    - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and
                                      use them to categorize content.
                                type: list
                                elements: str
                            native_shape_field:
                                description:
                                    - ""
                                type: dict
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
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                type: str
                                    config_values:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            config_param_values:
                                                description:
                                                    - The configuration parameter values.
                                                type: dict
                                                suboptions:
                                                    string_value:
                                                        description:
                                                            - A string value of the parameter.
                                                        type: str
                                                    int_value:
                                                        description:
                                                            - An integer value of the parameter.
                                                        type: int
                                                    object_value:
                                                        description:
                                                            - An object value of the parameter.
                                                        type: dict
                                                    ref_value:
                                                        description:
                                                            - The root object reference value.
                                                        type: dict
                                                    parameter_value:
                                                        description:
                                                            - Reference to the parameter by its key.
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
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                        type: int
                                    name:
                                        description:
                                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    description:
                                        description:
                                            - A detailed description of the object.
                                        type: str
                                    type:
                                        description:
                                            - The type reference.
                                        type: dict
                                        required: true
                                    position:
                                        description:
                                            - The position of the attribute.
                                        type: int
                                    default_value_string:
                                        description:
                                            - The default value.
                                        type: str
                                    is_mandatory:
                                        description:
                                            - Specifies whether the field is mandatory.
                                        type: bool
            object_status:
                description:
                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                type: int
    foreign_keys:
        description:
            - An array of foreign keys.
        type: list
        elements: dict
        suboptions:
            model_type:
                description:
                    - The key type.
                    - Required when model_type is 'DATA_STORE_ENTITY'
                type: str
                choices:
                    - "FOREIGN_KEY"
                required: true
            key:
                description:
                    - The object key.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            model_version:
                description:
                    - The model version of the object.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            parent_ref:
                description:
                    - ""
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: dict
                suboptions:
                    parent:
                        description:
                            - Key of the parent object.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: str
            name:
                description:
                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            attribute_refs:
                description:
                    - An array of attribute references.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: list
                elements: dict
                suboptions:
                    position:
                        description:
                            - The position of the attribute.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: int
                    attribute:
                        description:
                            - ""
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: dict
                        suboptions:
                            model_type:
                                description:
                                    - The type of the types object.
                                    - Required when model_type is 'DATA_STORE_ENTITY'
                                type: str
                                choices:
                                    - "SHAPE"
                                    - "SHAPE_FIELD"
                                    - "NATIVE_SHAPE_FIELD"
                                required: true
                            key:
                                description:
                                    - The key of the object.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: str
                            model_version:
                                description:
                                    - The model version of an object.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: str
                            parent_ref:
                                description:
                                    - ""
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: dict
                                suboptions:
                                    parent:
                                        description:
                                            - Key of the parent object.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: str
                            config_values:
                                description:
                                    - ""
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: dict
                                suboptions:
                                    config_param_values:
                                        description:
                                            - The configuration parameter values.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: dict
                                        suboptions:
                                            string_value:
                                                description:
                                                    - A string value of the parameter.
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: str
                                            int_value:
                                                description:
                                                    - An integer value of the parameter.
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: int
                                            object_value:
                                                description:
                                                    - An object value of the parameter.
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: dict
                                            ref_value:
                                                description:
                                                    - The root object reference value.
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: dict
                                            parameter_value:
                                                description:
                                                    - Reference to the parameter by its key.
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: str
                                    parent_ref:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: dict
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: int
                            name:
                                description:
                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                      characters. The value is editable and is restricted to 1000 characters.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: str
                            description:
                                description:
                                    - A detailed description of the object.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: str
                            type:
                                description:
                                    - The type reference.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: dict
                            labels:
                                description:
                                    - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and
                                      use them to categorize content.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: list
                                elements: str
                            native_shape_field:
                                description:
                                    - ""
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: dict
                                suboptions:
                                    model_type:
                                        description:
                                            - The type of the types object.
                                            - Required when model_type is 'DATA_STORE_ENTITY'
                                        type: str
                                        choices:
                                            - "SHAPE"
                                            - "SHAPE_FIELD"
                                            - "NATIVE_SHAPE_FIELD"
                                        required: true
                                    key:
                                        description:
                                            - The key of the object.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: str
                                    model_version:
                                        description:
                                            - The model version of an object.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: str
                                    parent_ref:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: dict
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: str
                                    config_values:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: dict
                                        suboptions:
                                            config_param_values:
                                                description:
                                                    - The configuration parameter values.
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: dict
                                                suboptions:
                                                    string_value:
                                                        description:
                                                            - A string value of the parameter.
                                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                        type: str
                                                    int_value:
                                                        description:
                                                            - An integer value of the parameter.
                                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                        type: int
                                                    object_value:
                                                        description:
                                                            - An object value of the parameter.
                                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                        type: dict
                                                    ref_value:
                                                        description:
                                                            - The root object reference value.
                                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                        type: dict
                                                    parameter_value:
                                                        description:
                                                            - Reference to the parameter by its key.
                                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                        type: str
                                            parent_ref:
                                                description:
                                                    - ""
                                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                type: dict
                                                suboptions:
                                                    parent:
                                                        description:
                                                            - Key of the parent object.
                                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                                        type: str
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: int
                                    name:
                                        description:
                                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: str
                                    description:
                                        description:
                                            - A detailed description of the object.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: str
                                    type:
                                        description:
                                            - The type reference.
                                            - Required when model_type is 'DATA_STORE_ENTITY'
                                        type: dict
                                        required: true
                                    position:
                                        description:
                                            - The position of the attribute.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: int
                                    default_value_string:
                                        description:
                                            - The default value.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: str
                                    is_mandatory:
                                        description:
                                            - Specifies whether the field is mandatory.
                                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                                        type: bool
            update_rule:
                description:
                    - The update rule.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: int
            delete_rule:
                description:
                    - The delete rule.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: int
            reference_unique_key:
                description:
                    - ""
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: dict
                suboptions:
                    model_type:
                        description:
                            - The key type.
                        type: str
                        choices:
                            - "PRIMARY_KEY"
                        required: true
                    key:
                        description:
                            - The object key.
                        type: str
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
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                        type: str
                    attribute_refs:
                        description:
                            - An array of attribute references.
                        type: list
                        elements: dict
                        suboptions:
                            position:
                                description:
                                    - The position of the attribute.
                                type: int
                            attribute:
                                description:
                                    - ""
                                type: dict
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
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                type: str
                                    config_values:
                                        description:
                                            - ""
                                        type: dict
                                        suboptions:
                                            config_param_values:
                                                description:
                                                    - The configuration parameter values.
                                                type: dict
                                                suboptions:
                                                    string_value:
                                                        description:
                                                            - A string value of the parameter.
                                                        type: str
                                                    int_value:
                                                        description:
                                                            - An integer value of the parameter.
                                                        type: int
                                                    object_value:
                                                        description:
                                                            - An object value of the parameter.
                                                        type: dict
                                                    ref_value:
                                                        description:
                                                            - The root object reference value.
                                                        type: dict
                                                    parameter_value:
                                                        description:
                                                            - Reference to the parameter by its key.
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
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                        type: int
                                    name:
                                        description:
                                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    description:
                                        description:
                                            - A detailed description of the object.
                                        type: str
                                    type:
                                        description:
                                            - The type reference.
                                        type: dict
                                    labels:
                                        description:
                                            - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own
                                              labels and use them to categorize content.
                                        type: list
                                        elements: str
                                    native_shape_field:
                                        description:
                                            - ""
                                        type: dict
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
                                                suboptions:
                                                    parent:
                                                        description:
                                                            - Key of the parent object.
                                                        type: str
                                            config_values:
                                                description:
                                                    - ""
                                                type: dict
                                                suboptions:
                                                    config_param_values:
                                                        description:
                                                            - The configuration parameter values.
                                                        type: dict
                                                        suboptions:
                                                            string_value:
                                                                description:
                                                                    - A string value of the parameter.
                                                                type: str
                                                            int_value:
                                                                description:
                                                                    - An integer value of the parameter.
                                                                type: int
                                                            object_value:
                                                                description:
                                                                    - An object value of the parameter.
                                                                type: dict
                                                            ref_value:
                                                                description:
                                                                    - The root object reference value.
                                                                type: dict
                                                            parameter_value:
                                                                description:
                                                                    - Reference to the parameter by its key.
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
                                            object_status:
                                                description:
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                type: int
                                            name:
                                                description:
                                                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                type: str
                                            description:
                                                description:
                                                    - A detailed description of the object.
                                                type: str
                                            type:
                                                description:
                                                    - The type reference.
                                                type: dict
                                                required: true
                                            position:
                                                description:
                                                    - The position of the attribute.
                                                type: int
                                            default_value_string:
                                                description:
                                                    - The default value.
                                                type: str
                                            is_mandatory:
                                                description:
                                                    - Specifies whether the field is mandatory.
                                                type: bool
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                        type: int
            object_status:
                description:
                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: int
    resource_name:
        description:
            - The resource name.
        type: str
    object_status:
        description:
            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
        type: int
    identifier:
        description:
            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be
              modified.
        type: str
    types:
        description:
            - ""
        type: dict
        suboptions:
            key:
                description:
                    - The key of the object.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            model_type:
                description:
                    - The type of the object.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            model_version:
                description:
                    - The model version of an object.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            parent_ref:
                description:
                    - ""
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: dict
                suboptions:
                    parent:
                        description:
                            - Key of the parent object.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: str
            name:
                description:
                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            description:
                description:
                    - A user defined description for the object.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            object_version:
                description:
                    - The version of the object that is used to track changes in the object instance.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: int
            types:
                description:
                    - types
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: dict
                suboptions:
                    model_type:
                        description:
                            - The property which differentiates the subtypes.
                            - Required when model_type is 'DATA_STORE_ENTITY'
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
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: str
                    model_version:
                        description:
                            - The model version of an object.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: str
                    parent_ref:
                        description:
                            - ""
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The
                              value is editable and is restricted to 1000 characters.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: str
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: int
                    description:
                        description:
                            - A user-defined description for the object.
                            - Applicable when model_type is 'DATA_STORE_ENTITY'
                        type: str
            object_status:
                description:
                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: int
            identifier:
                description:
                    - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can
                      be modified.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
    entity_properties:
        description:
            - Map<String, String> for entity properties
        type: dict
    authorization_mode:
        description:
            - Authorization mode for communicating with another OCI service relevant for the API.
        type: str
        choices:
            - "OBO"
            - "USER_PRINCIPAL"
            - "RESOURCE_PRINCIPAL"
            - "INSTANCE_PRINCIPAL"
            - "UNDEFINED"
    endpoint_id:
        description:
            - Endpoint ID used for getDataAssetFullDetails.
        type: str
    action:
        description:
            - The action to perform on the DataEntity.
        type: str
        required: true
        choices:
            - "create_entity_shape"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action create_entity_shape on data_entity with model_type = DATA_STORE_ENTITY
  oci_data_connectivity_data_entity_actions:
    # required
    model_type: DATA_STORE_ENTITY
    name: name_example

    # optional
    key: key_example
    model_version: model_version_example
    parent_ref:
      # optional
      parent: parent_example
    object_version: 56
    external_key: external_key_example
    shape:
      # required
      model_type: SHAPE

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
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
      object_status: 56
      name: name_example
      description: description_example
      type:
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
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            parameter_name: parameter_name_example
            description: description_example
            default_value: null
            class_field_name: class_field_name_example
            is_static: true
            is_class_field_value: true
    shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
    entity_type: TABLE
    other_type_label: other_type_label_example
    unique_keys:
    - # required
      model_type: PRIMARY_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      object_status: 56
    foreign_keys:
    - # required
      model_type: FOREIGN_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      update_rule: 56
      delete_rule: 56
      reference_unique_key:
        # required
        model_type: PRIMARY_KEY

        # optional
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        attribute_refs:
        - # optional
          position: 56
          attribute:
            # required
            model_type: SHAPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            type: null
            labels: [ "labels_example" ]
            native_shape_field:
              # required
              model_type: SHAPE
              type: null

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
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
              object_status: 56
              name: name_example
              description: description_example
              position: 56
              default_value_string: default_value_string_example
              is_mandatory: true
        object_status: 56
      object_status: 56
    resource_name: resource_name_example
    object_status: 56
    identifier: identifier_example
    types:
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
      types:
        # required
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
      object_status: 56
      identifier: identifier_example
    entity_properties: null

- name: Perform action create_entity_shape on data_entity with model_type = TABLE_ENTITY
  oci_data_connectivity_data_entity_actions:
    # required
    model_type: TABLE_ENTITY
    name: name_example

    # optional
    key: key_example
    model_version: model_version_example
    parent_ref:
      # optional
      parent: parent_example
    object_version: 56
    external_key: external_key_example
    shape:
      # required
      model_type: SHAPE

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
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
      object_status: 56
      name: name_example
      description: description_example
      type:
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
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            parameter_name: parameter_name_example
            description: description_example
            default_value: null
            class_field_name: class_field_name_example
            is_static: true
            is_class_field_value: true
    shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
    entity_type: TABLE
    other_type_label: other_type_label_example
    unique_keys:
    - # required
      model_type: PRIMARY_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      object_status: 56
    foreign_keys:
    - # required
      model_type: FOREIGN_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      update_rule: 56
      delete_rule: 56
      reference_unique_key:
        # required
        model_type: PRIMARY_KEY

        # optional
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        attribute_refs:
        - # optional
          position: 56
          attribute:
            # required
            model_type: SHAPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            type: null
            labels: [ "labels_example" ]
            native_shape_field:
              # required
              model_type: SHAPE
              type: null

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
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
              object_status: 56
              name: name_example
              description: description_example
              position: 56
              default_value_string: default_value_string_example
              is_mandatory: true
        object_status: 56
      object_status: 56
    resource_name: resource_name_example
    object_status: 56
    identifier: identifier_example
    types:
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
      types:
        # required
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
      object_status: 56
      identifier: identifier_example
    entity_properties: null

- name: Perform action create_entity_shape on data_entity with model_type = SQL_ENTITY
  oci_data_connectivity_data_entity_actions:
    # required
    model_type: SQL_ENTITY
    name: name_example

    # optional
    sql_query: sql_query_example
    key: key_example
    model_version: model_version_example
    parent_ref:
      # optional
      parent: parent_example
    object_version: 56
    external_key: external_key_example
    shape:
      # required
      model_type: SHAPE

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
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
      object_status: 56
      name: name_example
      description: description_example
      type:
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
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            parameter_name: parameter_name_example
            description: description_example
            default_value: null
            class_field_name: class_field_name_example
            is_static: true
            is_class_field_value: true
    shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
    entity_type: TABLE
    other_type_label: other_type_label_example
    unique_keys:
    - # required
      model_type: PRIMARY_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      object_status: 56
    foreign_keys:
    - # required
      model_type: FOREIGN_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      update_rule: 56
      delete_rule: 56
      reference_unique_key:
        # required
        model_type: PRIMARY_KEY

        # optional
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        attribute_refs:
        - # optional
          position: 56
          attribute:
            # required
            model_type: SHAPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            type: null
            labels: [ "labels_example" ]
            native_shape_field:
              # required
              model_type: SHAPE
              type: null

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
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
              object_status: 56
              name: name_example
              description: description_example
              position: 56
              default_value_string: default_value_string_example
              is_mandatory: true
        object_status: 56
      object_status: 56
    resource_name: resource_name_example
    object_status: 56
    identifier: identifier_example
    types:
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
      types:
        # required
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
      object_status: 56
      identifier: identifier_example
    entity_properties: null

- name: Perform action create_entity_shape on data_entity with model_type = FILE_ENTITY
  oci_data_connectivity_data_entity_actions:
    # required
    model_type: FILE_ENTITY
    name: name_example

    # optional
    data_format:
      # required
      type: JSON

      # optional
      format_attribute:
        # required
        model_type: AVRO_FORMAT

        # optional
        compression: compression_example
      compression_config:
        # required
        codec: NONE
    key: key_example
    model_version: model_version_example
    parent_ref:
      # optional
      parent: parent_example
    object_version: 56
    external_key: external_key_example
    shape:
      # required
      model_type: SHAPE

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
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
      object_status: 56
      name: name_example
      description: description_example
      type:
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
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            parameter_name: parameter_name_example
            description: description_example
            default_value: null
            class_field_name: class_field_name_example
            is_static: true
            is_class_field_value: true
    shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
    entity_type: TABLE
    other_type_label: other_type_label_example
    unique_keys:
    - # required
      model_type: PRIMARY_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      object_status: 56
    foreign_keys:
    - # required
      model_type: FOREIGN_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      update_rule: 56
      delete_rule: 56
      reference_unique_key:
        # required
        model_type: PRIMARY_KEY

        # optional
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        attribute_refs:
        - # optional
          position: 56
          attribute:
            # required
            model_type: SHAPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            type: null
            labels: [ "labels_example" ]
            native_shape_field:
              # required
              model_type: SHAPE
              type: null

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
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
              object_status: 56
              name: name_example
              description: description_example
              position: 56
              default_value_string: default_value_string_example
              is_mandatory: true
        object_status: 56
      object_status: 56
    resource_name: resource_name_example
    object_status: 56
    identifier: identifier_example
    types:
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
      types:
        # required
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
      object_status: 56
      identifier: identifier_example
    entity_properties: null

- name: Perform action create_entity_shape on data_entity with model_type = VIEW_ENTITY
  oci_data_connectivity_data_entity_actions:
    # required
    model_type: VIEW_ENTITY
    name: name_example

    # optional
    key: key_example
    model_version: model_version_example
    parent_ref:
      # optional
      parent: parent_example
    object_version: 56
    external_key: external_key_example
    shape:
      # required
      model_type: SHAPE

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
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
      object_status: 56
      name: name_example
      description: description_example
      type:
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
              model_type: STRUCTURED_TYPE

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref: null
              name: name_example
              object_status: 56
              description: description_example
            parameter_name: parameter_name_example
            description: description_example
            default_value: null
            class_field_name: class_field_name_example
            is_static: true
            is_class_field_value: true
    shape_id: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
    entity_type: TABLE
    other_type_label: other_type_label_example
    unique_keys:
    - # required
      model_type: PRIMARY_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      object_status: 56
    foreign_keys:
    - # required
      model_type: FOREIGN_KEY

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      attribute_refs:
      - # optional
        position: 56
        attribute:
          # required
          model_type: SHAPE

          # optional
          key: key_example
          model_version: model_version_example
          parent_ref:
            # optional
            parent: parent_example
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
          object_status: 56
          name: name_example
          description: description_example
          type: null
          labels: [ "labels_example" ]
          native_shape_field:
            # required
            model_type: SHAPE
            type: null

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            position: 56
            default_value_string: default_value_string_example
            is_mandatory: true
      update_rule: 56
      delete_rule: 56
      reference_unique_key:
        # required
        model_type: PRIMARY_KEY

        # optional
        key: key_example
        model_version: model_version_example
        parent_ref:
          # optional
          parent: parent_example
        name: name_example
        attribute_refs:
        - # optional
          position: 56
          attribute:
            # required
            model_type: SHAPE

            # optional
            key: key_example
            model_version: model_version_example
            parent_ref:
              # optional
              parent: parent_example
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
            object_status: 56
            name: name_example
            description: description_example
            type: null
            labels: [ "labels_example" ]
            native_shape_field:
              # required
              model_type: SHAPE
              type: null

              # optional
              key: key_example
              model_version: model_version_example
              parent_ref:
                # optional
                parent: parent_example
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
              object_status: 56
              name: name_example
              description: description_example
              position: 56
              default_value_string: default_value_string_example
              is_mandatory: true
        object_status: 56
      object_status: 56
    resource_name: resource_name_example
    object_status: 56
    identifier: identifier_example
    types:
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
      types:
        # required
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
      object_status: 56
      identifier: identifier_example
    entity_properties: null

"""

RETURN = """
data_entity:
    description:
        - Details of the DataEntity resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        filters:
            description:
                - Filters present in the datastore. It can be null.
            returned: on success
            type: str
            sample: filters_example
        is_effective_date_disabled:
            description:
                - It shows whether the effective date is disabled.
            returned: on success
            type: bool
            sample: true
        is_flex_data_store:
            description:
                - It shows whether the datastore is of flex type.
            returned: on success
            type: bool
            sample: true
        is_silent_error:
            description:
                - It shows whether the extraction of this datastore will stop when an error occurs.
            returned: on success
            type: bool
            sample: true
        supports_incremental:
            description:
                - It shows whether the datastore supports incremental extract.
            returned: on success
            type: bool
            sample: true
        data_format:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                format_attribute:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        escape_character:
                            description:
                                - The escape character for the CSV format.
                            returned: on success
                            type: str
                            sample: escape_character_example
                        delimiter:
                            description:
                                - The delimiter for the CSV format.
                            returned: on success
                            type: str
                            sample: delimiter_example
                        quote_character:
                            description:
                                - The quote character for the CSV format.
                            returned: on success
                            type: str
                            sample: quote_character_example
                        has_header:
                            description:
                                - Defines whether the file has a header row.
                            returned: on success
                            type: bool
                            sample: true
                        is_file_pattern:
                            description:
                                - Defines whether a file pattern is supported.
                            returned: on success
                            type: bool
                            sample: true
                        timestamp_format:
                            description:
                                - Format for timestamp information.
                            returned: on success
                            type: str
                            sample: timestamp_format_example
                        data_address:
                            description:
                                - "Range of the data. For example, \\"'My Sheet'!B3:C35\\""
                            returned: on success
                            type: str
                            sample: data_address_example
                        header:
                            description:
                                - "Whether the dataAddress contains the header with column names. If false - column names fill be generated."
                            returned: on success
                            type: bool
                            sample: true
                        password:
                            description:
                                - Workbook password if it is password protected.
                            returned: on success
                            type: str
                            sample: example-password
                        encoding:
                            description:
                                - The encoding for the file.
                            returned: on success
                            type: str
                            sample: encoding_example
                        model_type:
                            description:
                                - The type of the format attribute.
                            returned: on success
                            type: str
                            sample: JSON_FORMAT
                        compression:
                            description:
                                - The compression for the file.
                            returned: on success
                            type: str
                            sample: compression_example
                type:
                    description:
                        - type
                    returned: on success
                    type: str
                    sample: JSON
                compression_config:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        codec:
                            description:
                                - Compression algorithm
                            returned: on success
                            type: str
                            sample: NONE
        sql_query:
            description:
                - sqlQuery
            returned: on success
            type: str
            sample: sql_query_example
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
        key:
            description:
                - The object key.
            returned: on success
            type: str
            sample: key_example
        model_version:
            description:
                - The model version of the object.
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
                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                  editable and is restricted to 1000 characters.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Detailed description of the object.
            returned: on success
            type: str
            sample: description_example
        object_version:
            description:
                - The version of the object that is used to track changes in the object instance.
            returned: on success
            type: int
            sample: 56
        external_key:
            description:
                - The external key of the object.
            returned: on success
            type: str
            sample: external_key_example
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
        shape_id:
            description:
                - The shape ID.
            returned: on success
            type: str
            sample: "ocid1.shape.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type:
            description:
                - The entity type.
            returned: on success
            type: str
            sample: TABLE
        other_type_label:
            description:
                - Specifies other type label.
            returned: on success
            type: str
            sample: other_type_label_example
        unique_keys:
            description:
                - An array of unique keys.
            returned: on success
            type: complex
            contains:
                model_type:
                    description:
                        - The key type.
                    returned: on success
                    type: str
                    sample: PRIMARY_KEY
                key:
                    description:
                        - The object key.
                    returned: on success
                    type: str
                    sample: key_example
                model_version:
                    description:
                        - The model version of the object.
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
                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value
                          is editable and is restricted to 1000 characters.
                    returned: on success
                    type: str
                    sample: name_example
                attribute_refs:
                    description:
                        - An array of attribute references.
                    returned: on success
                    type: complex
                    contains:
                        position:
                            description:
                                - The position of the attribute.
                            returned: on success
                            type: int
                            sample: 56
                        attribute:
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
                object_status:
                    description:
                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                    returned: on success
                    type: int
                    sample: 56
        foreign_keys:
            description:
                - An array of foreign keys.
            returned: on success
            type: complex
            contains:
                model_type:
                    description:
                        - The key type.
                    returned: on success
                    type: str
                    sample: FOREIGN_KEY
                key:
                    description:
                        - The object key.
                    returned: on success
                    type: str
                    sample: key_example
                model_version:
                    description:
                        - The model version of the object.
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
                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value
                          is editable and is restricted to 1000 characters.
                    returned: on success
                    type: str
                    sample: name_example
                attribute_refs:
                    description:
                        - An array of attribute references.
                    returned: on success
                    type: complex
                    contains:
                        position:
                            description:
                                - The position of the attribute.
                            returned: on success
                            type: int
                            sample: 56
                        attribute:
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
                update_rule:
                    description:
                        - The update rule.
                    returned: on success
                    type: int
                    sample: 56
                delete_rule:
                    description:
                        - The delete rule.
                    returned: on success
                    type: int
                    sample: 56
                reference_unique_key:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        model_type:
                            description:
                                - The key type.
                            returned: on success
                            type: str
                            sample: PRIMARY_KEY
                        key:
                            description:
                                - The object key.
                            returned: on success
                            type: str
                            sample: key_example
                        model_version:
                            description:
                                - The model version of the object.
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
                        attribute_refs:
                            description:
                                - An array of attribute references.
                            returned: on success
                            type: complex
                            contains:
                                position:
                                    description:
                                        - The position of the attribute.
                                    returned: on success
                                    type: int
                                    sample: 56
                                attribute:
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
                        object_status:
                            description:
                                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                            returned: on success
                            type: int
                            sample: 56
                object_status:
                    description:
                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
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
                - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
            returned: on success
            type: int
            sample: 56
        identifier:
            description:
                - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be
                  modified.
            returned: on success
            type: str
            sample: identifier_example
    sample: {
        "filters": "filters_example",
        "is_effective_date_disabled": true,
        "is_flex_data_store": true,
        "is_silent_error": true,
        "supports_incremental": true,
        "data_format": {
            "format_attribute": {
                "escape_character": "escape_character_example",
                "delimiter": "delimiter_example",
                "quote_character": "quote_character_example",
                "has_header": true,
                "is_file_pattern": true,
                "timestamp_format": "timestamp_format_example",
                "data_address": "data_address_example",
                "header": true,
                "password": "example-password",
                "encoding": "encoding_example",
                "model_type": "JSON_FORMAT",
                "compression": "compression_example"
            },
            "type": "JSON",
            "compression_config": {
                "codec": "NONE"
            }
        },
        "sql_query": "sql_query_example",
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
        "description": "description_example",
        "object_version": 56,
        "external_key": "external_key_example",
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
        "entity_type": "TABLE",
        "other_type_label": "other_type_label_example",
        "unique_keys": [{
            "model_type": "PRIMARY_KEY",
            "key": "key_example",
            "model_version": "model_version_example",
            "parent_ref": {
                "parent": "parent_example"
            },
            "name": "name_example",
            "attribute_refs": [{
                "position": 56,
                "attribute": {
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
                }
            }],
            "object_status": 56
        }],
        "foreign_keys": [{
            "model_type": "FOREIGN_KEY",
            "key": "key_example",
            "model_version": "model_version_example",
            "parent_ref": {
                "parent": "parent_example"
            },
            "name": "name_example",
            "attribute_refs": [{
                "position": 56,
                "attribute": {
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
                }
            }],
            "update_rule": 56,
            "delete_rule": 56,
            "reference_unique_key": {
                "model_type": "PRIMARY_KEY",
                "key": "key_example",
                "model_version": "model_version_example",
                "parent_ref": {
                    "parent": "parent_example"
                },
                "name": "name_example",
                "attribute_refs": [{
                    "position": 56,
                    "attribute": {
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
                    }
                }],
                "object_status": 56
            },
            "object_status": 56
        }],
        "resource_name": "resource_name_example",
        "object_status": 56,
        "identifier": "identifier_example"
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
    from oci.data_connectivity.models import CreateEntityShapeDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataEntityActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        create_entity_shape
    """

    @staticmethod
    def get_module_resource_id_param():
        return "schema_resource_name"

    def get_module_resource_id(self):
        return self.module.params.get("schema_resource_name")

    def get_get_fn(self):
        return self.client.get_data_entity

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_entity,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
            schema_resource_name=self.module.params.get("schema_resource_name"),
            data_entity_key=self.module.params.get("data_entity_key"),
        )

    def create_entity_shape(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CreateEntityShapeDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_entity_shape,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                connection_key=self.module.params.get("connection_key"),
                schema_resource_name=self.module.params.get("schema_resource_name"),
                create_entity_shape_details=action_details,
                authorization_mode=self.module.params.get("authorization_mode"),
                endpoint_id=self.module.params.get("endpoint_id"),
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


DataEntityActionsHelperCustom = get_custom_class("DataEntityActionsHelperCustom")


class ResourceHelper(DataEntityActionsHelperCustom, DataEntityActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            registry_id=dict(type="str", required=True),
            connection_key=dict(type="str", required=True, no_log=True),
            schema_resource_name=dict(type="str", required=True),
            sql_query=dict(type="str"),
            data_format=dict(
                type="dict",
                options=dict(
                    format_attribute=dict(
                        type="dict",
                        options=dict(
                            encoding=dict(type="str"),
                            escape_character=dict(type="str"),
                            delimiter=dict(type="str"),
                            quote_character=dict(type="str"),
                            has_header=dict(type="bool"),
                            is_file_pattern=dict(type="bool"),
                            timestamp_format=dict(type="str"),
                            compression=dict(type="str"),
                            model_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "AVRO_FORMAT",
                                    "JSON_FORMAT",
                                    "CSV_FORMAT",
                                    "PARQUET_FORMAT",
                                    "EXCEL_FORMAT",
                                ],
                            ),
                            data_address=dict(type="str"),
                            header=dict(type="bool"),
                            password=dict(type="str", no_log=True),
                        ),
                    ),
                    type=dict(
                        type="str",
                        required=True,
                        choices=["JSON", "CSV", "PARQUET", "AVRO"],
                    ),
                    compression_config=dict(
                        type="dict",
                        options=dict(
                            codec=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "NONE",
                                    "AUTO",
                                    "GZIP",
                                    "BZIP2",
                                    "DEFLATE",
                                    "LZ4",
                                    "SNAPPY",
                                ],
                            )
                        ),
                    ),
                ),
            ),
            model_type=dict(
                type="str",
                required=True,
                choices=[
                    "DATA_STORE_ENTITY",
                    "TABLE_ENTITY",
                    "SQL_ENTITY",
                    "FILE_ENTITY",
                    "VIEW_ENTITY",
                ],
            ),
            key=dict(type="str", no_log=True),
            model_version=dict(type="str"),
            parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
            name=dict(type="str", required=True),
            object_version=dict(type="int"),
            external_key=dict(type="str", no_log=True),
            shape=dict(
                type="dict",
                options=dict(
                    model_type=dict(
                        type="str",
                        required=True,
                        choices=["SHAPE", "SHAPE_FIELD", "NATIVE_SHAPE_FIELD"],
                    ),
                    key=dict(type="str", no_log=True),
                    model_version=dict(type="str"),
                    parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
                    config_values=dict(
                        type="dict",
                        options=dict(
                            config_param_values=dict(type="dict"),
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
                            ),
                        ),
                    ),
                    object_status=dict(type="int"),
                    name=dict(type="str"),
                    description=dict(type="str"),
                    type=dict(
                        type="dict",
                        options=dict(
                            wrapped_type=dict(
                                type="dict",
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
                                    parent_ref=dict(type="ParentReference"),
                                    name=dict(type="str"),
                                    object_status=dict(type="int"),
                                    description=dict(type="str"),
                                ),
                            ),
                            config_values=dict(
                                type="dict",
                                options=dict(
                                    config_param_values=dict(type="dict"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
                                    ),
                                ),
                            ),
                            dt_type=dict(
                                type="str", choices=["PRIMITIVE", "STRUCTURED"]
                            ),
                            type_system_name=dict(type="str"),
                            schema=dict(
                                type="dict",
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
                                    parent_ref=dict(type="ParentReference"),
                                    name=dict(type="str"),
                                    object_status=dict(type="int"),
                                    description=dict(type="str"),
                                ),
                            ),
                            model_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "CONFIGURED_TYPE",
                                    "DERIVED_TYPE",
                                    "DATA_TYPE",
                                    "STRUCTURED_TYPE",
                                    "COMPOSITE_TYPE",
                                ],
                            ),
                            key=dict(type="str", no_log=True),
                            model_version=dict(type="str"),
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
                            ),
                            name=dict(type="str"),
                            object_status=dict(type="int"),
                            description=dict(type="str"),
                            parent_type=dict(
                                type="dict",
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
                                    parent_ref=dict(type="ParentReference"),
                                    name=dict(type="str"),
                                    object_status=dict(type="int"),
                                    description=dict(type="str"),
                                    parent_type=dict(type="CompositeType"),
                                    elements=dict(type="list", elements="dict"),
                                    config_definition=dict(type="ConfigDefinition"),
                                ),
                            ),
                            elements=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    labels=dict(type="list", elements="str"),
                                    native_shape_field=dict(
                                        type="dict",
                                        options=dict(
                                            model_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "SHAPE",
                                                    "SHAPE_FIELD",
                                                    "NATIVE_SHAPE_FIELD",
                                                ],
                                            ),
                                            key=dict(type="str", no_log=True),
                                            model_version=dict(type="str"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                            config_values=dict(
                                                type="dict",
                                                options=dict(
                                                    config_param_values=dict(
                                                        type="dict"
                                                    ),
                                                    parent_ref=dict(
                                                        type="dict",
                                                        options=dict(
                                                            parent=dict(type="str")
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            object_status=dict(type="int"),
                                            name=dict(type="str"),
                                            description=dict(type="str"),
                                            type=dict(type="dict", required=True),
                                            position=dict(type="int"),
                                            default_value_string=dict(type="str"),
                                            is_mandatory=dict(type="bool"),
                                        ),
                                    ),
                                    port_type=dict(
                                        type="str", choices=["DATA", "CONTROL", "MODEL"]
                                    ),
                                    fields=dict(
                                        type="list",
                                        elements="dict",
                                        options=dict(
                                            model_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "SHAPE",
                                                    "SHAPE_FIELD",
                                                    "NATIVE_SHAPE_FIELD",
                                                ],
                                            ),
                                            key=dict(type="str", no_log=True),
                                            model_version=dict(type="str"),
                                            parent_ref=dict(type="ParentReference"),
                                            config_values=dict(type="ConfigValues"),
                                            object_status=dict(type="int"),
                                            name=dict(type="str"),
                                            description=dict(type="str"),
                                        ),
                                    ),
                                    default_value=dict(type="dict"),
                                    root_object_default_value=dict(type="dict"),
                                    is_input=dict(type="bool"),
                                    is_output=dict(type="bool"),
                                    output_aggregation_type=dict(
                                        type="str",
                                        choices=["MIN", "MAX", "COUNT", "SUM"],
                                    ),
                                    type_name=dict(type="str"),
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "OUTPUT_PORT",
                                            "SHAPE",
                                            "SHAPE_FIELD",
                                            "INPUT_PORT",
                                            "PARAMETER",
                                            "NATIVE_SHAPE_FIELD",
                                        ],
                                    ),
                                    key=dict(type="str", no_log=True),
                                    model_version=dict(type="str"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
                                    ),
                                    config_values=dict(
                                        type="dict",
                                        options=dict(
                                            config_param_values=dict(type="dict"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                        ),
                                    ),
                                    object_status=dict(type="int"),
                                    name=dict(type="str"),
                                    description=dict(type="str"),
                                    type=dict(
                                        type="dict",
                                        options=dict(
                                            model_type=dict(
                                                type="str",
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
                                            parent_ref=dict(type="ParentReference"),
                                            name=dict(type="str"),
                                            object_status=dict(type="int"),
                                            description=dict(type="str"),
                                        ),
                                    ),
                                    position=dict(type="int"),
                                    default_value_string=dict(type="str"),
                                    is_mandatory=dict(type="bool"),
                                ),
                            ),
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
                                    config_parameter_definitions=dict(type="dict"),
                                ),
                            ),
                        ),
                    ),
                ),
            ),
            shape_id=dict(type="str"),
            entity_type=dict(type="str", choices=["TABLE", "VIEW", "FILE", "SQL"]),
            other_type_label=dict(type="str"),
            unique_keys=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(
                    model_type=dict(type="str", required=True, choices=["PRIMARY_KEY"]),
                    key=dict(type="str", no_log=True),
                    model_version=dict(type="str"),
                    parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
                    name=dict(type="str"),
                    attribute_refs=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            position=dict(type="int"),
                            attribute=dict(
                                type="dict",
                                options=dict(
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "SHAPE",
                                            "SHAPE_FIELD",
                                            "NATIVE_SHAPE_FIELD",
                                        ],
                                    ),
                                    key=dict(type="str", no_log=True),
                                    model_version=dict(type="str"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
                                    ),
                                    config_values=dict(
                                        type="dict",
                                        options=dict(
                                            config_param_values=dict(type="dict"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                        ),
                                    ),
                                    object_status=dict(type="int"),
                                    name=dict(type="str"),
                                    description=dict(type="str"),
                                    type=dict(type="dict"),
                                    labels=dict(type="list", elements="str"),
                                    native_shape_field=dict(
                                        type="dict",
                                        options=dict(
                                            model_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "SHAPE",
                                                    "SHAPE_FIELD",
                                                    "NATIVE_SHAPE_FIELD",
                                                ],
                                            ),
                                            key=dict(type="str", no_log=True),
                                            model_version=dict(type="str"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                            config_values=dict(
                                                type="dict",
                                                options=dict(
                                                    config_param_values=dict(
                                                        type="dict"
                                                    ),
                                                    parent_ref=dict(
                                                        type="dict",
                                                        options=dict(
                                                            parent=dict(type="str")
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            object_status=dict(type="int"),
                                            name=dict(type="str"),
                                            description=dict(type="str"),
                                            type=dict(type="dict", required=True),
                                            position=dict(type="int"),
                                            default_value_string=dict(type="str"),
                                            is_mandatory=dict(type="bool"),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    object_status=dict(type="int"),
                ),
            ),
            foreign_keys=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(
                    model_type=dict(type="str", required=True, choices=["FOREIGN_KEY"]),
                    key=dict(type="str", no_log=True),
                    model_version=dict(type="str"),
                    parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
                    name=dict(type="str"),
                    attribute_refs=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            position=dict(type="int"),
                            attribute=dict(
                                type="dict",
                                options=dict(
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "SHAPE",
                                            "SHAPE_FIELD",
                                            "NATIVE_SHAPE_FIELD",
                                        ],
                                    ),
                                    key=dict(type="str", no_log=True),
                                    model_version=dict(type="str"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
                                    ),
                                    config_values=dict(
                                        type="dict",
                                        options=dict(
                                            config_param_values=dict(type="dict"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                        ),
                                    ),
                                    object_status=dict(type="int"),
                                    name=dict(type="str"),
                                    description=dict(type="str"),
                                    type=dict(type="dict"),
                                    labels=dict(type="list", elements="str"),
                                    native_shape_field=dict(
                                        type="dict",
                                        options=dict(
                                            model_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "SHAPE",
                                                    "SHAPE_FIELD",
                                                    "NATIVE_SHAPE_FIELD",
                                                ],
                                            ),
                                            key=dict(type="str", no_log=True),
                                            model_version=dict(type="str"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                            config_values=dict(
                                                type="dict",
                                                options=dict(
                                                    config_param_values=dict(
                                                        type="dict"
                                                    ),
                                                    parent_ref=dict(
                                                        type="dict",
                                                        options=dict(
                                                            parent=dict(type="str")
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            object_status=dict(type="int"),
                                            name=dict(type="str"),
                                            description=dict(type="str"),
                                            type=dict(type="dict", required=True),
                                            position=dict(type="int"),
                                            default_value_string=dict(type="str"),
                                            is_mandatory=dict(type="bool"),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    update_rule=dict(type="int"),
                    delete_rule=dict(type="int"),
                    reference_unique_key=dict(
                        type="dict",
                        no_log=False,
                        options=dict(
                            model_type=dict(
                                type="str", required=True, choices=["PRIMARY_KEY"]
                            ),
                            key=dict(type="str", no_log=True),
                            model_version=dict(type="str"),
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
                            ),
                            name=dict(type="str"),
                            attribute_refs=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    position=dict(type="int"),
                                    attribute=dict(
                                        type="dict",
                                        options=dict(
                                            model_type=dict(
                                                type="str",
                                                required=True,
                                                choices=[
                                                    "SHAPE",
                                                    "SHAPE_FIELD",
                                                    "NATIVE_SHAPE_FIELD",
                                                ],
                                            ),
                                            key=dict(type="str", no_log=True),
                                            model_version=dict(type="str"),
                                            parent_ref=dict(
                                                type="dict",
                                                options=dict(parent=dict(type="str")),
                                            ),
                                            config_values=dict(
                                                type="dict",
                                                options=dict(
                                                    config_param_values=dict(
                                                        type="dict"
                                                    ),
                                                    parent_ref=dict(
                                                        type="dict",
                                                        options=dict(
                                                            parent=dict(type="str")
                                                        ),
                                                    ),
                                                ),
                                            ),
                                            object_status=dict(type="int"),
                                            name=dict(type="str"),
                                            description=dict(type="str"),
                                            type=dict(type="dict"),
                                            labels=dict(type="list", elements="str"),
                                            native_shape_field=dict(
                                                type="dict",
                                                options=dict(
                                                    model_type=dict(
                                                        type="str",
                                                        required=True,
                                                        choices=[
                                                            "SHAPE",
                                                            "SHAPE_FIELD",
                                                            "NATIVE_SHAPE_FIELD",
                                                        ],
                                                    ),
                                                    key=dict(type="str", no_log=True),
                                                    model_version=dict(type="str"),
                                                    parent_ref=dict(
                                                        type="dict",
                                                        options=dict(
                                                            parent=dict(type="str")
                                                        ),
                                                    ),
                                                    config_values=dict(
                                                        type="dict",
                                                        options=dict(
                                                            config_param_values=dict(
                                                                type="dict"
                                                            ),
                                                            parent_ref=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    parent=dict(
                                                                        type="str"
                                                                    )
                                                                ),
                                                            ),
                                                        ),
                                                    ),
                                                    object_status=dict(type="int"),
                                                    name=dict(type="str"),
                                                    description=dict(type="str"),
                                                    type=dict(
                                                        type="dict", required=True
                                                    ),
                                                    position=dict(type="int"),
                                                    default_value_string=dict(
                                                        type="str"
                                                    ),
                                                    is_mandatory=dict(type="bool"),
                                                ),
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                            object_status=dict(type="int"),
                        ),
                    ),
                    object_status=dict(type="int"),
                ),
            ),
            resource_name=dict(type="str"),
            object_status=dict(type="int"),
            identifier=dict(type="str"),
            types=dict(
                type="dict",
                options=dict(
                    key=dict(type="str", no_log=True),
                    model_type=dict(type="str"),
                    model_version=dict(type="str"),
                    parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
                    name=dict(type="str"),
                    description=dict(type="str"),
                    object_version=dict(type="int"),
                    types=dict(type="dict"),
                    object_status=dict(type="int"),
                    identifier=dict(type="str"),
                ),
            ),
            entity_properties=dict(type="dict"),
            authorization_mode=dict(
                type="str",
                choices=[
                    "OBO",
                    "USER_PRINCIPAL",
                    "RESOURCE_PRINCIPAL",
                    "INSTANCE_PRINCIPAL",
                    "UNDEFINED",
                ],
            ),
            endpoint_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["create_entity_shape"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_entity",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
