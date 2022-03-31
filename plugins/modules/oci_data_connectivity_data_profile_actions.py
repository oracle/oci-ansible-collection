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
module: oci_data_connectivity_data_profile_actions
short_description: Perform actions on a DataProfile resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DataProfile resource in Oracle Cloud Infrastructure
    - For I(action=create), execute data profiling on live schema
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    registry_id:
        description:
            - The registry Ocid.
        type: str
        aliases: ["id"]
        required: true
    read_operation_config:
        description:
            - ""
        type: dict
        suboptions:
            model_type:
                description:
                    - The type of data operation.
                type: str
                choices:
                    - "READ_OPERATION_CONFIG"
                    - "WRITE_OPERATION_CONFIG"
                required: true
            key:
                description:
                    - The object key.
                type: str
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
                        type: str
            operations:
                description:
                    - An array of operations.
                type: list
                elements: dict
                suboptions:
                    query:
                        description:
                            - A query string.
                            - Required when model_type is 'QUERY'
                        type: str
                    is_distinct:
                        description:
                            - Specifies whether the object is distinct.
                            - Applicable when model_type is 'SELECT'
                        type: bool
                    select_columns:
                        description:
                            - An array of selected columns.
                            - Required when model_type is 'SELECT'
                        type: list
                        elements: dict
                        suboptions:
                            model_type:
                                description:
                                    - The type of the types object.
                                    - Required when model_type is 'SELECT'
                                type: str
                                choices:
                                    - "SHAPE"
                                    - "SHAPE_FIELD"
                                    - "NATIVE_SHAPE_FIELD"
                                required: true
                            key:
                                description:
                                    - The key of the object.
                                    - Applicable when model_type is 'SELECT'
                                type: str
                            model_version:
                                description:
                                    - The model version of an object.
                                    - Applicable when model_type is 'SELECT'
                                type: str
                            parent_ref:
                                description:
                                    - ""
                                    - Applicable when model_type is 'SELECT'
                                type: dict
                                suboptions:
                                    parent:
                                        description:
                                            - Key of the parent object.
                                            - Applicable when model_type is 'SELECT'
                                        type: str
                            config_values:
                                description:
                                    - ""
                                    - Applicable when model_type is 'SELECT'
                                type: dict
                                suboptions:
                                    config_param_values:
                                        description:
                                            - The configuration parameter values.
                                            - Applicable when model_type is 'SELECT'
                                        type: dict
                                        suboptions:
                                            string_value:
                                                description:
                                                    - A string value of the parameter.
                                                    - Applicable when model_type is 'SELECT'
                                                type: str
                                            int_value:
                                                description:
                                                    - An integer value of the parameter.
                                                    - Applicable when model_type is 'SELECT'
                                                type: int
                                            object_value:
                                                description:
                                                    - An object value of the parameter.
                                                    - Applicable when model_type is 'SELECT'
                                                type: dict
                                            ref_value:
                                                description:
                                                    - The root object reference value.
                                                    - Applicable when model_type is 'SELECT'
                                                type: dict
                                            parameter_value:
                                                description:
                                                    - Reference to the parameter by its key.
                                                    - Applicable when model_type is 'SELECT'
                                                type: str
                                    parent_ref:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'SELECT'
                                        type: dict
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                    - Applicable when model_type is 'SELECT'
                                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                    - Applicable when model_type is 'SELECT'
                                type: int
                            name:
                                description:
                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters.
                                      The value is editable and is restricted to 1000 characters.
                                    - Applicable when model_type is 'SELECT'
                                type: str
                            description:
                                description:
                                    - Detailed description for the object.
                                    - Applicable when model_type is 'SELECT'
                                type: str
                            type:
                                description:
                                    - The type reference.
                                    - Applicable when model_type is 'SELECT'
                                type: dict
                            labels:
                                description:
                                    - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them
                                      to categorize content.
                                    - Applicable when model_type is 'SELECT'
                                type: list
                                elements: str
                            native_shape_field:
                                description:
                                    - ""
                                    - Applicable when model_type is 'SELECT'
                                type: dict
                                suboptions:
                                    model_type:
                                        description:
                                            - The type of the types object.
                                            - Required when model_type is 'SELECT'
                                        type: str
                                        choices:
                                            - "SHAPE"
                                            - "SHAPE_FIELD"
                                            - "NATIVE_SHAPE_FIELD"
                                        required: true
                                    key:
                                        description:
                                            - The key of the object.
                                            - Applicable when model_type is 'SELECT'
                                        type: str
                                    model_version:
                                        description:
                                            - The model version of an object.
                                            - Applicable when model_type is 'SELECT'
                                        type: str
                                    parent_ref:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'SELECT'
                                        type: dict
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                    - Applicable when model_type is 'SELECT'
                                                type: str
                                    config_values:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'SELECT'
                                        type: dict
                                        suboptions:
                                            config_param_values:
                                                description:
                                                    - The configuration parameter values.
                                                    - Applicable when model_type is 'SELECT'
                                                type: dict
                                                suboptions:
                                                    string_value:
                                                        description:
                                                            - A string value of the parameter.
                                                            - Applicable when model_type is 'SELECT'
                                                        type: str
                                                    int_value:
                                                        description:
                                                            - An integer value of the parameter.
                                                            - Applicable when model_type is 'SELECT'
                                                        type: int
                                                    object_value:
                                                        description:
                                                            - An object value of the parameter.
                                                            - Applicable when model_type is 'SELECT'
                                                        type: dict
                                                    ref_value:
                                                        description:
                                                            - The root object reference value.
                                                            - Applicable when model_type is 'SELECT'
                                                        type: dict
                                                    parameter_value:
                                                        description:
                                                            - Reference to the parameter by its key.
                                                            - Applicable when model_type is 'SELECT'
                                                        type: str
                                            parent_ref:
                                                description:
                                                    - ""
                                                    - Applicable when model_type is 'SELECT'
                                                type: dict
                                                suboptions:
                                                    parent:
                                                        description:
                                                            - Key of the parent object.
                                                            - Applicable when model_type is 'SELECT'
                                                        type: str
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                            - Applicable when model_type is 'SELECT'
                                        type: int
                                    name:
                                        description:
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                            - Applicable when model_type is 'SELECT'
                                        type: str
                                    description:
                                        description:
                                            - Detailed description for the object.
                                            - Applicable when model_type is 'SELECT'
                                        type: str
                                    type:
                                        description:
                                            - The type reference.
                                            - Required when model_type is 'SELECT'
                                        type: dict
                                        required: true
                                    position:
                                        description:
                                            - The position of the attribute.
                                            - Applicable when model_type is 'SELECT'
                                        type: int
                                    default_value_string:
                                        description:
                                            - The default value.
                                            - Applicable when model_type is 'SELECT'
                                        type: str
                                    is_mandatory:
                                        description:
                                            - Specifies whether the field is mandatory.
                                            - Applicable when model_type is 'SELECT'
                                        type: bool
                    condition:
                        description:
                            - The join condition.
                            - Required when model_type is 'JOIN'
                        type: str
                    policy:
                        description:
                            - The type of join.
                            - Required when model_type is 'JOIN'
                        type: str
                        choices:
                            - "INNER_JOIN"
                            - "LEFT_JOIN"
                            - "RIGHT_JOIN"
                            - "FULL_JOIN"
                    sort_clauses:
                        description:
                            - The sort clause.
                            - Required when model_type is 'SORT'
                        type: list
                        elements: dict
                        suboptions:
                            field:
                                description:
                                    - ""
                                    - Applicable when model_type is 'SORT'
                                type: dict
                                suboptions:
                                    model_type:
                                        description:
                                            - The type of the types object.
                                            - Required when model_type is 'SORT'
                                        type: str
                                        choices:
                                            - "SHAPE"
                                            - "SHAPE_FIELD"
                                            - "NATIVE_SHAPE_FIELD"
                                        required: true
                                    key:
                                        description:
                                            - The key of the object.
                                            - Applicable when model_type is 'SORT'
                                        type: str
                                    model_version:
                                        description:
                                            - The model version of an object.
                                            - Applicable when model_type is 'SORT'
                                        type: str
                                    parent_ref:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'SORT'
                                        type: dict
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                    - Applicable when model_type is 'SORT'
                                                type: str
                                    config_values:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'SORT'
                                        type: dict
                                        suboptions:
                                            config_param_values:
                                                description:
                                                    - The configuration parameter values.
                                                    - Applicable when model_type is 'SORT'
                                                type: dict
                                                suboptions:
                                                    string_value:
                                                        description:
                                                            - A string value of the parameter.
                                                            - Applicable when model_type is 'SORT'
                                                        type: str
                                                    int_value:
                                                        description:
                                                            - An integer value of the parameter.
                                                            - Applicable when model_type is 'SORT'
                                                        type: int
                                                    object_value:
                                                        description:
                                                            - An object value of the parameter.
                                                            - Applicable when model_type is 'SORT'
                                                        type: dict
                                                    ref_value:
                                                        description:
                                                            - The root object reference value.
                                                            - Applicable when model_type is 'SORT'
                                                        type: dict
                                                    parameter_value:
                                                        description:
                                                            - Reference to the parameter by its key.
                                                            - Applicable when model_type is 'SORT'
                                                        type: str
                                            parent_ref:
                                                description:
                                                    - ""
                                                    - Applicable when model_type is 'SORT'
                                                type: dict
                                                suboptions:
                                                    parent:
                                                        description:
                                                            - Key of the parent object.
                                                            - Applicable when model_type is 'SORT'
                                                        type: str
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                            - Applicable when model_type is 'SORT'
                                        type: int
                                    name:
                                        description:
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                            - Applicable when model_type is 'SORT'
                                        type: str
                                    description:
                                        description:
                                            - Detailed description for the object.
                                            - Applicable when model_type is 'SORT'
                                        type: str
                                    type:
                                        description:
                                            - The type reference.
                                            - Applicable when model_type is 'SORT'
                                        type: dict
                                    labels:
                                        description:
                                            - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and
                                              use them to categorize content.
                                            - Applicable when model_type is 'SORT'
                                        type: list
                                        elements: str
                                    native_shape_field:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'SORT'
                                        type: dict
                                        suboptions:
                                            model_type:
                                                description:
                                                    - The type of the types object.
                                                    - Required when model_type is 'SORT'
                                                type: str
                                                choices:
                                                    - "SHAPE"
                                                    - "SHAPE_FIELD"
                                                    - "NATIVE_SHAPE_FIELD"
                                                required: true
                                            key:
                                                description:
                                                    - The key of the object.
                                                    - Applicable when model_type is 'SORT'
                                                type: str
                                            model_version:
                                                description:
                                                    - The model version of an object.
                                                    - Applicable when model_type is 'SORT'
                                                type: str
                                            parent_ref:
                                                description:
                                                    - ""
                                                    - Applicable when model_type is 'SORT'
                                                type: dict
                                                suboptions:
                                                    parent:
                                                        description:
                                                            - Key of the parent object.
                                                            - Applicable when model_type is 'SORT'
                                                        type: str
                                            config_values:
                                                description:
                                                    - ""
                                                    - Applicable when model_type is 'SORT'
                                                type: dict
                                                suboptions:
                                                    config_param_values:
                                                        description:
                                                            - The configuration parameter values.
                                                            - Applicable when model_type is 'SORT'
                                                        type: dict
                                                        suboptions:
                                                            string_value:
                                                                description:
                                                                    - A string value of the parameter.
                                                                    - Applicable when model_type is 'SORT'
                                                                type: str
                                                            int_value:
                                                                description:
                                                                    - An integer value of the parameter.
                                                                    - Applicable when model_type is 'SORT'
                                                                type: int
                                                            object_value:
                                                                description:
                                                                    - An object value of the parameter.
                                                                    - Applicable when model_type is 'SORT'
                                                                type: dict
                                                            ref_value:
                                                                description:
                                                                    - The root object reference value.
                                                                    - Applicable when model_type is 'SORT'
                                                                type: dict
                                                            parameter_value:
                                                                description:
                                                                    - Reference to the parameter by its key.
                                                                    - Applicable when model_type is 'SORT'
                                                                type: str
                                                    parent_ref:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'SORT'
                                                        type: dict
                                                        suboptions:
                                                            parent:
                                                                description:
                                                                    - Key of the parent object.
                                                                    - Applicable when model_type is 'SORT'
                                                                type: str
                                            object_status:
                                                description:
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                    - Applicable when model_type is 'SORT'
                                                type: int
                                            name:
                                                description:
                                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                    - Applicable when model_type is 'SORT'
                                                type: str
                                            description:
                                                description:
                                                    - Detailed description for the object.
                                                    - Applicable when model_type is 'SORT'
                                                type: str
                                            type:
                                                description:
                                                    - The type reference.
                                                    - Required when model_type is 'SORT'
                                                type: dict
                                                required: true
                                            position:
                                                description:
                                                    - The position of the attribute.
                                                    - Applicable when model_type is 'SORT'
                                                type: int
                                            default_value_string:
                                                description:
                                                    - The default value.
                                                    - Applicable when model_type is 'SORT'
                                                type: str
                                            is_mandatory:
                                                description:
                                                    - Specifies whether the field is mandatory.
                                                    - Applicable when model_type is 'SORT'
                                                type: bool
                            order:
                                description:
                                    - The sort order.
                                    - Applicable when model_type is 'SORT'
                                type: str
                                choices:
                                    - "ASC"
                                    - "DESC"
                    model_type:
                        description:
                            - The type of operation.
                        type: str
                        choices:
                            - "QUERY"
                            - "SELECT"
                            - "JOIN"
                            - "SORT"
                            - "FILTER"
                        required: true
                    filter_condition:
                        description:
                            - The filter condition.
                            - Applicable when model_type is 'FILTER'
                        type: str
            data_format:
                description:
                    - ""
                type: dict
                suboptions:
                    format_attribute:
                        description:
                            - ""
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
                            model_type:
                                description:
                                    - The type of the format attribute.
                                type: str
                                choices:
                                    - "AVRO_FORMAT"
                                    - "JSON_FORMAT"
                                    - "CSV_FORMAT"
                                    - "PARQUET_FORMAT"
                                required: true
                            compression:
                                description:
                                    - The compression for the file.
                                    - Applicable when model_type is one of ['PARQUET_FORMAT', 'AVRO_FORMAT']
                                type: str
                    type:
                        description:
                            - type
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
                        type: dict
                        suboptions:
                            codec:
                                description:
                                    - Compression algorithm
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
            partition_config:
                description:
                    - ""
                type: dict
                suboptions:
                    model_type:
                        description:
                            - The type of partition configuration.
                        type: str
                        choices:
                            - "KEYRANGEPARTITIONCONFIG"
                        required: true
                    partition_number:
                        description:
                            - The partition number for the key range.
                        type: int
                    key_range:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            key:
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
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    description:
                                        description:
                                            - Detailed description for the object.
                                        type: str
                                    type:
                                        description:
                                            - The type reference.
                                        type: dict
                                    labels:
                                        description:
                                            - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and
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
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                type: int
                                            name:
                                                description:
                                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                type: str
                                            description:
                                                description:
                                                    - Detailed description for the object.
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
                            range:
                                description:
                                    - The key range.
                                type: list
                                elements: str
            read_attribute:
                description:
                    - ""
                type: dict
                suboptions:
                    extract_strategy:
                        description:
                            - "Extraction Strategy - FULL|INCREMENTAL"
                            - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                        type: str
                        choices:
                            - "FULL"
                            - "INCREMENTAL"
                    external_storage:
                        description:
                            - ""
                            - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                        type: dict
                        suboptions:
                            model_type:
                                description:
                                    - The type of the abstract read attribute.
                                    - Required when model_type is 'BICC_READ_ATTRIBUTE'
                                type: str
                                choices:
                                    - "EXTERNAL_STORAGE"
                                required: true
                            storage_id:
                                description:
                                    - Id of the external stoarge configured in BICC console. Usually its numeric.
                                    - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                                type: str
                            storage_name:
                                description:
                                    - Name of the external storage configured in BICC console
                                    - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                                type: str
                            host:
                                description:
                                    - Object Storage host Url. DO not give http/https.
                                    - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                                type: str
                            tenancy_id:
                                description:
                                    - Tenancy OCID for the OOS bucket
                                    - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                                type: str
                            namespace:
                                description:
                                    - Namespace for the OOS bucket
                                    - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                                type: str
                            bucket:
                                description:
                                    - Bucket Name where BICC extracts stores the files
                                    - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                                type: str
                    initial_extract_date:
                        description:
                            - Date from where extract should start
                            - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                        type: str
                    last_extract_date:
                        description:
                            - Date last extracted
                            - Applicable when model_type is 'BICC_READ_ATTRIBUTE'
                        type: str
                    model_type:
                        description:
                            - The type of the abstract read attribute.
                        type: str
                        choices:
                            - "ORACLE_READ_ATTRIBUTE"
                            - "BICC_READ_ATTRIBUTE"
                            - "ORACLEREADATTRIBUTE"
                        required: true
                    fetch_size:
                        description:
                            - The fetch size for reading.
                        type: int
            object_status:
                description:
                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                type: int
            read_raw_data:
                description:
                    - Specifies if this readOperationConfig operation should trigger raw data preview flow.
                type: bool
    data_asset:
        description:
            - ""
        type: dict
        suboptions:
            key:
                description:
                    - Currently not used on data asset creation. Reserved for future.
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
                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is
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
                    - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be
                      modified.
                type: str
                required: true
            external_key:
                description:
                    - The external key for the object.
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
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is editable and is restricted to 1000 characters.
                        type: str
                    description:
                        description:
                            - A user defined description for the object.
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
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The
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
                                    - The property which disciminates the subtypes.
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
                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters.
                                      The value is editable and is restricted to 1000 characters.
                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            description:
                                description:
                                    - A user defined description for the object.
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
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    is_contained:
                                        description:
                                            - Specifies whether the configuration is contained or not.
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
                                                                    - The property which disciminates the subtypes.
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
                                                                    - Free form text without any restriction on permitted characters. Name can have letters,
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
                                                                    - A user defined description for the object.
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
                                                                    - The property which disciminates the subtypes.
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
                                                                    - Free form text without any restriction on permitted characters. Name can have letters,
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
                                                                    - A user defined description for the object.
                                                                type: str
                                                    model_type:
                                                        description:
                                                            - The property which disciminates the subtypes.
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
                                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers,
                                                              and special characters. The value is editable and is restricted to 1000 characters.
                                                        type: str
                                                    object_status:
                                                        description:
                                                            - The status of an object that can be set to value 1 for shallow references across objects, other
                                                              values reserved.
                                                        type: int
                                                    description:
                                                        description:
                                                            - A user defined description for the object.
                                                        type: str
                                                    parent_type:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'COMPOSITE_TYPE'
                                                        type: dict
                                                        suboptions:
                                                            model_type:
                                                                description:
                                                                    - The property which disciminates the subtypes.
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
                                                                    - Free form text without any restriction on permitted characters. Name can have letters,
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
                                                                    - A user defined description for the object.
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
                                                                    - Labels are keywords or labels that you can add to data assets, dataflows etc. You can
                                                                      define your own labels and use them to categorize content.
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
                                                                            - Free form text without any restriction on permitted characters. Name can have
                                                                              letters, numbers, and special characters. The value is editable and is restricted
                                                                              to 1000 characters.
                                                                            - Applicable when model_type is 'SHAPE_FIELD'
                                                                        type: str
                                                                    description:
                                                                        description:
                                                                            - Detailed description for the object.
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
                                                                    - The port details for the data asset.Type.
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
                                                                            - Free form text without any restriction on permitted characters. Name can have
                                                                              letters, numbers, and special characters. The value is editable and is restricted
                                                                              to 1000 characters.
                                                                        type: str
                                                                    description:
                                                                        description:
                                                                            - Detailed description for the object.
                                                                        type: str
                                                            default_value:
                                                                description:
                                                                    - The default value of the parameter.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: dict
                                                            root_object_default_value:
                                                                description:
                                                                    - The default value of the parameter which can be an object in DIS, such as a data entity.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: dict
                                                            is_input:
                                                                description:
                                                                    - Specifies whether the parameter is input value.
                                                                    - Applicable when model_type is 'PARAMETER'
                                                                type: bool
                                                            is_output:
                                                                description:
                                                                    - Specifies whether the parameter is output value.
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
                                                                    - Free form text without any restriction on permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            description:
                                                                description:
                                                                    - Detailed description for the object.
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
                                                                            - The property which disciminates the subtypes.
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
                                                                            - Free form text without any restriction on permitted characters. Name can have
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
                                                                            - A user defined description for the object.
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
                                                                    - Free form text without any restriction on permitted characters. Name can have letters,
                                                                      numbers, and special characters. The value is editable and is restricted to 1000
                                                                      characters.
                                                                type: str
                                                            is_contained:
                                                                description:
                                                                    - Specifies whether the configuration is contained or not.
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
                                                    - A user defined description for the object.
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
                                                    - Specifies whether the parameter is static or not.
                                                type: bool
                                            is_class_field_value:
                                                description:
                                                    - Specifies whether the parameter is a class field or not.
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
                            - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to
                              categorize content.
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
                            - Specifies whether this object is a favorite or not.
                        type: bool
                    created_by_user_id:
                        description:
                            - The id of the user who created the object.
                        type: str
                    created_by_user_name:
                        description:
                            - The name of the user who created the object.
                        type: str
                    updated_by_user_id:
                        description:
                            - The id of the user who updated the object.
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
                            - The full path to identify this object.
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
                            - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to
                              categorize content.
                        type: list
                        elements: str
                    is_favorite:
                        description:
                            - Specifies whether this object is a favorite or not.
                        type: bool
            default_connection:
                description:
                    - ""
                type: dict
                suboptions:
                    key:
                        description:
                            - Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a
                              value can be passed in create.
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
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is editable and is restricted to 1000 characters.
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
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The
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
                                    - The object's type.
                                type: str
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
                                        type: str
                            name:
                                description:
                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters.
                                      The value is editable and is restricted to 1000 characters.
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
                                    - The external key for the object.
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
                                    - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore.
                                      The value can be modified.
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
                                            - The full path to identify this object.
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
                                            - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels
                                              and use them to categorize content.
                                        type: list
                                        elements: str
                                    is_favorite:
                                        description:
                                            - Specifies whether this object is a favorite or not.
                                        type: bool
                    connection_properties:
                        description:
                            - The properties for the connection.
                        type: list
                        elements: dict
                        suboptions:
                            name:
                                description:
                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters.
                                      The value is editable and is restricted to 1000 characters.
                                type: str
                            value:
                                description:
                                    - The value for the connection name property.
                                type: str
                    properties:
                        description:
                            - All the properties for the connection in a key-value map format.
                        type: dict
                    type:
                        description:
                            - Specific Connection Type
                        type: str
                    is_default:
                        description:
                            - The default property for the connection.
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
                                    - The full path to identify this object.
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
                                    - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use
                                      them to categorize content.
                                type: list
                                elements: str
                            is_favorite:
                                description:
                                    - Specifies whether this object is a favorite or not.
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
                                    - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them
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
                                    - Specifies whether this object is a favorite or not.
                                type: bool
                            created_by_user_id:
                                description:
                                    - The id of the user who created the object.
                                type: str
                            created_by_user_name:
                                description:
                                    - The name of the user who created the object.
                                type: str
                            updated_by_user_id:
                                description:
                                    - The id of the user who updated the object.
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
                            - The ocid of private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    compartment_id:
                        description:
                            - The compartmentId of private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    dns_proxy_ip:
                        description:
                            - The IP address of dns proxy.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    private_endpoint_ip:
                        description:
                            - The ocid of private endpoint resource.
                            - Applicable when model_type is 'PRIVATE_END_POINT'
                        type: str
                    dns_zones:
                        description:
                            - Array of dns zones to be use during private endpoint resolution.
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
                            - Generated key that can be used in API calls to identify endpoint. On scenarios where reference to the endpoint is needed, a value
                              can be passed in create.
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
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is editable and is restricted to 1000 characters.
                        type: str
                    description:
                        description:
                            - User-defined description for the endpoint.
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
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The
                              value can be modified.
                        type: str
                    data_assets:
                        description:
                            - List of data assets which belongs to this endpoint
                        type: list
                        elements: dict
                        suboptions:
                            key:
                                description:
                                    - Currently not used on data asset creation. Reserved for future.
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
                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters.
                                      The value is editable and is restricted to 1000 characters.
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
                                    - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore.
                                      The value can be modified.
                                type: str
                                required: true
                            external_key:
                                description:
                                    - The external key for the object.
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
    connection:
        description:
            - ""
        type: dict
        suboptions:
            key:
                description:
                    - Generated key that can be used in API calls to identify connection. On scenarios where reference to the connection is needed, a value can
                      be passed in create.
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
                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
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
                    - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be
                      modified.
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
                            - The object's type.
                        type: str
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
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is editable and is restricted to 1000 characters.
                        type: str
                        required: true
                    resource_name:
                        description:
                            - A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000 characters.
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
                            - The external key for the object.
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
                            - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The
                              value can be modified.
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
                                    - The full path to identify this object.
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
                                    - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use
                                      them to categorize content.
                                type: list
                                elements: str
                            is_favorite:
                                description:
                                    - Specifies whether this object is a favorite or not.
                                type: bool
            connection_properties:
                description:
                    - The properties for the connection.
                type: list
                elements: dict
                suboptions:
                    name:
                        description:
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is editable and is restricted to 1000 characters.
                        type: str
                    value:
                        description:
                            - The value for the connection name property.
                        type: str
            properties:
                description:
                    - All the properties for the connection in a key-value map format.
                type: dict
            type:
                description:
                    - Specific Connection Type
                type: str
            is_default:
                description:
                    - The default property for the connection.
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
                            - The full path to identify this object.
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
                            - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to
                              categorize content.
                        type: list
                        elements: str
                    is_favorite:
                        description:
                            - Specifies whether this object is a favorite or not.
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
                            - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and use them to
                              categorize content.
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
                            - Specifies whether this object is a favorite or not.
                        type: bool
                    created_by_user_id:
                        description:
                            - The id of the user who created the object.
                        type: str
                    created_by_user_name:
                        description:
                            - The name of the user who created the object.
                        type: str
                    updated_by_user_id:
                        description:
                            - The id of the user who updated the object.
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
    schema:
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
                    - The object's type.
                type: str
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
                        type: str
            name:
                description:
                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                type: str
                required: true
            resource_name:
                description:
                    - A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000 characters.
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
                    - The external key for the object.
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
                    - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be
                      modified.
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
                            - The full path to identify this object.
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
                            - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to
                              categorize content.
                        type: list
                        elements: str
                    is_favorite:
                        description:
                            - Specifies whether this object is a favorite or not.
                        type: bool
    data_entity:
        description:
            - ""
        type: dict
        suboptions:
            filters:
                description:
                    - Filters present in the Datastore. It can be Null.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: str
            is_effective_date_disabled:
                description:
                    - It shows whether or not effective date is disabled
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: bool
            is_flex_data_store:
                description:
                    - It shows whether the datastore is of flex type
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: bool
            is_silent_error:
                description:
                    - It shows whether the extraction of this datastore will stop on error
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: bool
            supports_incremental:
                description:
                    - It shows whether the datastore supports Incremental Extract or not.
                    - Applicable when model_type is 'DATA_STORE_ENTITY'
                type: bool
            sql_query:
                description:
                    - sqlQuery
                    - Applicable when model_type is 'SQL_ENTITY'
                type: str
            model_type:
                description:
                    - The data entity type.
                type: str
                choices:
                    - "TABLE_ENTITY"
                    - "DATA_STORE_ENTITY"
                    - "VIEW_ENTITY"
                    - "SQL_ENTITY"
                    - "FILE_ENTITY"
                required: true
            metadata:
                description:
                    - ""
                type: dict
                suboptions:
                    created_by:
                        description:
                            - The user that created the object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    created_by_name:
                        description:
                            - The user that created the object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    updated_by:
                        description:
                            - The user that updated the object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    updated_by_name:
                        description:
                            - The user that updated the object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    time_created:
                        description:
                            - The date and time that the object was created.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    time_updated:
                        description:
                            - The date and time that the object was updated.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    aggregator_key:
                        description:
                            - The owning object key for this object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    aggregator:
                        description:
                            - ""
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: dict
                        suboptions:
                            type:
                                description:
                                    - The type of the aggregator.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: str
                            key:
                                description:
                                    - The key of the aggregator object.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: str
                            name:
                                description:
                                    - The name of the aggregator.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: str
                            identifier:
                                description:
                                    - The identifier of the aggregator.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: str
                            description:
                                description:
                                    - The description of the aggregator.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: str
                    identifier_path:
                        description:
                            - The full path to identify this object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    info_fields:
                        description:
                            - Information property fields.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: dict
                    registry_version:
                        description:
                            - The registry version of the object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: int
                    labels:
                        description:
                            - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to
                              categorize content.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: list
                        elements: str
                    is_favorite:
                        description:
                            - Specifies whether this object is a favorite or not.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: bool
            key:
                description:
                    - The object key.
                type: str
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
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
            name:
                description:
                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                type: str
            description:
                description:
                    - Detailed description for the object.
                type: str
            object_version:
                description:
                    - The version of the object that is used to track changes in the object instance.
                type: int
            external_key:
                description:
                    - The external key for the object.
                type: str
            shape:
                description:
                    - ""
                type: dict
                suboptions:
                    model_type:
                        description:
                            - The type of the types object.
                            - Required when model_type is 'TABLE_ENTITY'
                        type: str
                        choices:
                            - "SHAPE"
                            - "SHAPE_FIELD"
                            - "NATIVE_SHAPE_FIELD"
                        required: true
                    key:
                        description:
                            - The key of the object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    model_version:
                        description:
                            - The model version of an object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    parent_ref:
                        description:
                            - ""
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: str
                    config_values:
                        description:
                            - ""
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: dict
                        suboptions:
                            config_param_values:
                                description:
                                    - The configuration parameter values.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: dict
                                suboptions:
                                    string_value:
                                        description:
                                            - A string value of the parameter.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: str
                                    int_value:
                                        description:
                                            - An integer value of the parameter.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: int
                                    object_value:
                                        description:
                                            - An object value of the parameter.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: dict
                                    ref_value:
                                        description:
                                            - The root object reference value.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: dict
                                    parameter_value:
                                        description:
                                            - Reference to the parameter by its key.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: str
                            parent_ref:
                                description:
                                    - ""
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: dict
                                suboptions:
                                    parent:
                                        description:
                                            - Key of the parent object.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: str
                    object_status:
                        description:
                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: int
                    name:
                        description:
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is editable and is restricted to 1000 characters.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    description:
                        description:
                            - Detailed description for the object.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    type:
                        description:
                            - ""
                            - Applicable when model_type is 'TABLE_ENTITY'
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
                                            - The property which disciminates the subtypes.
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
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                        type: int
                                    description:
                                        description:
                                            - A user defined description for the object.
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
                                            - The property which disciminates the subtypes.
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
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                        type: int
                                    description:
                                        description:
                                            - A user defined description for the object.
                                        type: str
                            model_type:
                                description:
                                    - The property which disciminates the subtypes.
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
                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters.
                                      The value is editable and is restricted to 1000 characters.
                                type: str
                            object_status:
                                description:
                                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                type: int
                            description:
                                description:
                                    - A user defined description for the object.
                                type: str
                            parent_type:
                                description:
                                    - ""
                                    - Applicable when model_type is 'COMPOSITE_TYPE'
                                type: dict
                                suboptions:
                                    model_type:
                                        description:
                                            - The property which disciminates the subtypes.
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
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                        type: int
                                    description:
                                        description:
                                            - A user defined description for the object.
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
                                            - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and
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
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                type: int
                                            name:
                                                description:
                                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                    - Applicable when model_type is 'SHAPE_FIELD'
                                                type: str
                                            description:
                                                description:
                                                    - Detailed description for the object.
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
                                            - The port details for the data asset.Type.
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
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                type: int
                                            name:
                                                description:
                                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                type: str
                                            description:
                                                description:
                                                    - Detailed description for the object.
                                                type: str
                                    default_value:
                                        description:
                                            - The default value of the parameter.
                                            - Applicable when model_type is 'PARAMETER'
                                        type: dict
                                    root_object_default_value:
                                        description:
                                            - The default value of the parameter which can be an object in DIS, such as a data entity.
                                            - Applicable when model_type is 'PARAMETER'
                                        type: dict
                                    is_input:
                                        description:
                                            - Specifies whether the parameter is input value.
                                            - Applicable when model_type is 'PARAMETER'
                                        type: bool
                                    is_output:
                                        description:
                                            - Specifies whether the parameter is output value.
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
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    description:
                                        description:
                                            - Detailed description for the object.
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
                                                    - The property which disciminates the subtypes.
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
                                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                type: str
                                            object_status:
                                                description:
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                type: int
                                            description:
                                                description:
                                                    - A user defined description for the object.
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
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                            - Applicable when model_type is 'CONFIGURED_TYPE'
                                        type: str
                                    is_contained:
                                        description:
                                            - Specifies whether the configuration is contained or not.
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
                                                            - The property which disciminates the subtypes.
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
                                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers,
                                                              and special characters. The value is editable and is restricted to 1000 characters.
                                                        type: str
                                                    object_status:
                                                        description:
                                                            - The status of an object that can be set to value 1 for shallow references across objects, other
                                                              values reserved.
                                                        type: int
                                                    description:
                                                        description:
                                                            - A user defined description for the object.
                                                        type: str
                                            parameter_name:
                                                description:
                                                    - This object represents the configurable properties for an object type.
                                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                                type: str
                                            description:
                                                description:
                                                    - A user defined description for the object.
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
                                                    - Specifies whether the parameter is static or not.
                                                    - Applicable when model_type is 'CONFIGURED_TYPE'
                                                type: bool
                                            is_class_field_value:
                                                description:
                                                    - Specifies whether the parameter is a class field or not.
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
                    - "DATA_STORE"
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
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is editable and is restricted to 1000 characters.
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
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                        type: str
                                    description:
                                        description:
                                            - Detailed description for the object.
                                        type: str
                                    type:
                                        description:
                                            - The type reference.
                                        type: dict
                                    labels:
                                        description:
                                            - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and
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
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                type: int
                                            name:
                                                description:
                                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                type: str
                                            description:
                                                description:
                                                    - Detailed description for the object.
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
                            - Required when model_type is 'TABLE_ENTITY'
                        type: str
                        choices:
                            - "FOREIGN_KEY"
                        required: true
                    key:
                        description:
                            - The object key.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    model_version:
                        description:
                            - The object's model version.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    parent_ref:
                        description:
                            - ""
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: dict
                        suboptions:
                            parent:
                                description:
                                    - Key of the parent object.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: str
                    name:
                        description:
                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value
                              is editable and is restricted to 1000 characters.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: str
                    attribute_refs:
                        description:
                            - An array of attribute references.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: list
                        elements: dict
                        suboptions:
                            position:
                                description:
                                    - The position of the attribute.
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: int
                            attribute:
                                description:
                                    - ""
                                    - Applicable when model_type is 'TABLE_ENTITY'
                                type: dict
                                suboptions:
                                    model_type:
                                        description:
                                            - The type of the types object.
                                            - Required when model_type is 'TABLE_ENTITY'
                                        type: str
                                        choices:
                                            - "SHAPE"
                                            - "SHAPE_FIELD"
                                            - "NATIVE_SHAPE_FIELD"
                                        required: true
                                    key:
                                        description:
                                            - The key of the object.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: str
                                    model_version:
                                        description:
                                            - The model version of an object.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: str
                                    parent_ref:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: dict
                                        suboptions:
                                            parent:
                                                description:
                                                    - Key of the parent object.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: str
                                    config_values:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: dict
                                        suboptions:
                                            config_param_values:
                                                description:
                                                    - The configuration parameter values.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: dict
                                                suboptions:
                                                    string_value:
                                                        description:
                                                            - A string value of the parameter.
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: str
                                                    int_value:
                                                        description:
                                                            - An integer value of the parameter.
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: int
                                                    object_value:
                                                        description:
                                                            - An object value of the parameter.
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: dict
                                                    ref_value:
                                                        description:
                                                            - The root object reference value.
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: dict
                                                    parameter_value:
                                                        description:
                                                            - Reference to the parameter by its key.
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: str
                                            parent_ref:
                                                description:
                                                    - ""
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: dict
                                                suboptions:
                                                    parent:
                                                        description:
                                                            - Key of the parent object.
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: str
                                    object_status:
                                        description:
                                            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: int
                                    name:
                                        description:
                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special
                                              characters. The value is editable and is restricted to 1000 characters.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: str
                                    description:
                                        description:
                                            - Detailed description for the object.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: str
                                    type:
                                        description:
                                            - The type reference.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: dict
                                    labels:
                                        description:
                                            - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own labels and
                                              use them to categorize content.
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: list
                                        elements: str
                                    native_shape_field:
                                        description:
                                            - ""
                                            - Applicable when model_type is 'TABLE_ENTITY'
                                        type: dict
                                        suboptions:
                                            model_type:
                                                description:
                                                    - The type of the types object.
                                                    - Required when model_type is 'TABLE_ENTITY'
                                                type: str
                                                choices:
                                                    - "SHAPE"
                                                    - "SHAPE_FIELD"
                                                    - "NATIVE_SHAPE_FIELD"
                                                required: true
                                            key:
                                                description:
                                                    - The key of the object.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: str
                                            model_version:
                                                description:
                                                    - The model version of an object.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: str
                                            parent_ref:
                                                description:
                                                    - ""
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: dict
                                                suboptions:
                                                    parent:
                                                        description:
                                                            - Key of the parent object.
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: str
                                            config_values:
                                                description:
                                                    - ""
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: dict
                                                suboptions:
                                                    config_param_values:
                                                        description:
                                                            - The configuration parameter values.
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: dict
                                                        suboptions:
                                                            string_value:
                                                                description:
                                                                    - A string value of the parameter.
                                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                                type: str
                                                            int_value:
                                                                description:
                                                                    - An integer value of the parameter.
                                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                                type: int
                                                            object_value:
                                                                description:
                                                                    - An object value of the parameter.
                                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                                type: dict
                                                            ref_value:
                                                                description:
                                                                    - The root object reference value.
                                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                                type: dict
                                                            parameter_value:
                                                                description:
                                                                    - Reference to the parameter by its key.
                                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                                type: str
                                                    parent_ref:
                                                        description:
                                                            - ""
                                                            - Applicable when model_type is 'TABLE_ENTITY'
                                                        type: dict
                                                        suboptions:
                                                            parent:
                                                                description:
                                                                    - Key of the parent object.
                                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                                type: str
                                            object_status:
                                                description:
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: int
                                            name:
                                                description:
                                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: str
                                            description:
                                                description:
                                                    - Detailed description for the object.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: str
                                            type:
                                                description:
                                                    - The type reference.
                                                    - Required when model_type is 'TABLE_ENTITY'
                                                type: dict
                                                required: true
                                            position:
                                                description:
                                                    - The position of the attribute.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: int
                                            default_value_string:
                                                description:
                                                    - The default value.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: str
                                            is_mandatory:
                                                description:
                                                    - Specifies whether the field is mandatory.
                                                    - Applicable when model_type is 'TABLE_ENTITY'
                                                type: bool
                    update_rule:
                        description:
                            - The update rule.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: int
                    delete_rule:
                        description:
                            - The delete rule.
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: int
                    reference_unique_key:
                        description:
                            - ""
                            - Applicable when model_type is 'TABLE_ENTITY'
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
                                        type: str
                            name:
                                description:
                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters.
                                      The value is editable and is restricted to 1000 characters.
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
                                                    - The status of an object that can be set to value 1 for shallow references across objects, other values
                                                      reserved.
                                                type: int
                                            name:
                                                description:
                                                    - Free form text without any restriction on permitted characters. Name can have letters, numbers, and
                                                      special characters. The value is editable and is restricted to 1000 characters.
                                                type: str
                                            description:
                                                description:
                                                    - Detailed description for the object.
                                                type: str
                                            type:
                                                description:
                                                    - The type reference.
                                                type: dict
                                            labels:
                                                description:
                                                    - Labels are keywords or labels that you can add to data assets, dataflows etc. You can define your own
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
                                                            - The status of an object that can be set to value 1 for shallow references across objects, other
                                                              values reserved.
                                                        type: int
                                                    name:
                                                        description:
                                                            - Free form text without any restriction on permitted characters. Name can have letters, numbers,
                                                              and special characters. The value is editable and is restricted to 1000 characters.
                                                        type: str
                                                    description:
                                                        description:
                                                            - Detailed description for the object.
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
                            - Applicable when model_type is 'TABLE_ENTITY'
                        type: int
            resource_name:
                description:
                    - The resource name.
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
                            model_type:
                                description:
                                    - The type of the format attribute.
                                type: str
                                choices:
                                    - "AVRO_FORMAT"
                                    - "JSON_FORMAT"
                                    - "CSV_FORMAT"
                                    - "PARQUET_FORMAT"
                                required: true
                            compression:
                                description:
                                    - The compression for the file.
                                    - Applicable when model_type is one of ['PARQUET_FORMAT', 'AVRO_FORMAT']
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
            object_status:
                description:
                    - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                type: int
            identifier:
                description:
                    - Value can only contain upper case letters, underscore and numbers. It should begin with upper case letter or underscore. The value can be
                      modified.
                type: str
    profile_config:
        description:
            - ""
        type: dict
        suboptions:
            attributes:
                description:
                    - Array of column names to profile. If empty all columns in the entity are profiled.
                type: list
                elements: str
            functions:
                description:
                    - Array of enum Strings basically what all profile functions to run. If empty, all supported functions are run.
                type: list
                elements: str
                choices:
                    - "ATTRIBUTE_COUNT"
                    - "ROW_COUNT"
                    - "DATA_TYPE"
                    - "DISTINCT_COUNT"
                    - "DUPLICATE_COUNT"
                    - "HISTOGRAM"
                    - "MAX"
                    - "MAX_LENGTH"
                    - "MEAN"
                    - "MEAN_LENGTH"
                    - "MEDIAN"
                    - "MIN"
                    - "MIN_LENGTH"
                    - "NULL_COUNT"
                    - "OUTLIER"
                    - "PATTERN"
                    - "STANDARD_DEVIATION"
                    - "UNIQUE_COUNT"
                    - "VARIANCE"
                    - "VALUE_FREQUENCY"
            top_n_val_freq:
                description:
                    - The maximum number of value frequencies to return per column. The VFs are sorted descending on frequency and ascending on value and then
                      topN are returned and rest discarded.
                type: int
            pattern_threshold:
                description:
                    - A pattern has to qualify minumum this percentage threshold to be considered a legitimate pattern on its own. All patterns which does not
                      qualify this will be clubbed together into a single 'Others' pattern.
                type: int
            data_type_threshold:
                description:
                    - A data type has to qualify minimum this percentage threshold to be considered an infrred data type for a column.
                type: int
    endpoint_id:
        description:
            - Endpoint Id used for getDataAssetFullDetails.
        type: str
    action:
        description:
            - The action to perform on the DataProfile.
        type: str
        required: true
        choices:
            - "create"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action create on data_profile
  oci_data_connectivity_data_profile_actions:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    action: create

    # optional
    read_operation_config:
      # required
      model_type: READ_OPERATION_CONFIG

      # optional
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      operations:
      - # required
        query: query_example
        model_type: QUERY
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
      partition_config:
        # required
        model_type: KEYRANGEPARTITIONCONFIG

        # optional
        partition_number: 56
        key_range:
          # optional
          key:
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
          range: [ "range_example" ]
      read_attribute:
        # required
        model_type: ORACLE_READ_ATTRIBUTE

        # optional
        fetch_size: 56
      object_status: 56
      read_raw_data: true
    data_asset:
      # required
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
    connection:
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
    schema:
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
    data_entity:
      # required
      model_type: TABLE_ENTITY

      # optional
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
      key: key_example
      model_version: model_version_example
      parent_ref:
        # optional
        parent: parent_example
      name: name_example
      description: description_example
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
    profile_config:
      # optional
      attributes: [ "attributes_example" ]
      functions: [ "ATTRIBUTE_COUNT" ]
      top_n_val_freq: 56
      pattern_threshold: 56
      data_type_threshold: 56
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
data_profile:
    description:
        - Details of the DataProfile resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        entity_name:
            description:
                - Entity name for which prodilig is requested.
            returned: on success
            type: str
            sample: entity_name_example
        entity_profile_result:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                attribute_count:
                    description:
                        - Number of columns in the DataFrame (arrow buffer) sent from Java layer. This value is not impacted by the List of attributes to
                          profile as being passed via configuration.
                    returned: on success
                    type: int
                    sample: 56
                sampled_row_count:
                    description:
                        - Number of rows were that were sampled
                    returned: on success
                    type: int
                    sample: 56
                estimated_row_count:
                    description:
                        - The estimated row count in the source.
                    returned: on success
                    type: int
                    sample: 56
        attribute_profile_results:
            description:
                - Array of profiling results
            returned: on success
            type: complex
            contains:
                mean:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                median:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                standard_deviation:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                variance:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                outlier:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        low:
                            description:
                                - low value of outlier
                            returned: on success
                            type: str
                            sample: low_example
                        high:
                            description:
                                - high value of outlier
                            returned: on success
                            type: str
                            sample: high_example
                        low_count:
                            description:
                                - lowCount value of outlier
                            returned: on success
                            type: str
                            sample: low_count_example
                        high_count:
                            description:
                                - highCount value of outlier
                            returned: on success
                            type: str
                            sample: high_count_example
                histogram:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        ranges:
                            description:
                                - Range of values
                            returned: on success
                            type: list
                            sample: []
                        counts:
                            description:
                                - Count of each ranges.
                            returned: on success
                            type: list
                            sample: []
                type:
                    description:
                        - Type of attribute
                    returned: on success
                    type: dict
                    sample: {}
                name:
                    description:
                        - Name of attribute
                    returned: on success
                    type: str
                    sample: name_example
                min:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                max:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                null_count:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                distinct_count:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                unique_count:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                duplicate_count:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                value_frequencies:
                    description:
                        - Top N value frequencies for the column as described already in profile config topNValueFrequency property.
                    returned: on success
                    type: complex
                    contains:
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        freq:
                            description:
                                - How many times that value occurred.
                            returned: on success
                            type: int
                            sample: 56
                        freq_percentage:
                            description:
                                - Frequency percentage across the sampled row counts (excluding nulls).
                            returned: on success
                            type: float
                            sample: 1.2
                min_length:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                max_length:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                mean_length:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                pattern_frequencies:
                    description:
                        - Pattern frequencies for the column as described already in profile config.
                    returned: on success
                    type: complex
                    contains:
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        freq:
                            description:
                                - How many times that value occurred.
                            returned: on success
                            type: int
                            sample: 56
                        freq_percentage:
                            description:
                                - Frequency percentage across the sampled row counts (excluding nulls).
                            returned: on success
                            type: float
                            sample: 1.2
                inferred_data_types:
                    description:
                        - Inferred DataType for the column.
                    returned: on success
                    type: complex
                    contains:
                        value:
                            description:
                                - Value of the confidence of the profile result
                            returned: on success
                            type: str
                            sample: value_example
                        confidence:
                            description:
                                - Placeholder for now, in future we will return the confidence of the profile result (because we are using sampled data and not
                                  whole data)
                            returned: on success
                            type: int
                            sample: 56
                        freq:
                            description:
                                - How many times that value occurred.
                            returned: on success
                            type: int
                            sample: 56
                        freq_percentage:
                            description:
                                - Frequency percentage across the sampled row counts (excluding nulls).
                            returned: on success
                            type: float
                            sample: 1.2
    sample: {
        "entity_name": "entity_name_example",
        "entity_profile_result": {
            "attribute_count": 56,
            "sampled_row_count": 56,
            "estimated_row_count": 56
        },
        "attribute_profile_results": [{
            "mean": {
                "confidence": 56,
                "value": "value_example"
            },
            "median": {
                "confidence": 56,
                "value": "value_example"
            },
            "standard_deviation": {
                "confidence": 56,
                "value": "value_example"
            },
            "variance": {
                "confidence": 56,
                "value": "value_example"
            },
            "outlier": {
                "low": "low_example",
                "high": "high_example",
                "low_count": "low_count_example",
                "high_count": "high_count_example"
            },
            "histogram": {
                "ranges": [],
                "counts": []
            },
            "type": {},
            "name": "name_example",
            "min": {
                "confidence": 56,
                "value": "value_example"
            },
            "max": {
                "confidence": 56,
                "value": "value_example"
            },
            "null_count": {
                "confidence": 56,
                "value": "value_example"
            },
            "distinct_count": {
                "confidence": 56,
                "value": "value_example"
            },
            "unique_count": {
                "confidence": 56,
                "value": "value_example"
            },
            "duplicate_count": {
                "confidence": 56,
                "value": "value_example"
            },
            "value_frequencies": [{
                "value": "value_example",
                "confidence": 56,
                "freq": 56,
                "freq_percentage": 1.2
            }],
            "min_length": {
                "confidence": 56,
                "value": "value_example"
            },
            "max_length": {
                "confidence": 56,
                "value": "value_example"
            },
            "mean_length": {
                "confidence": 56,
                "value": "value_example"
            },
            "pattern_frequencies": [{
                "value": "value_example",
                "confidence": 56,
                "freq": 56,
                "freq_percentage": 1.2
            }],
            "inferred_data_types": [{
                "value": "value_example",
                "confidence": 56,
                "freq": 56,
                "freq_percentage": 1.2
            }]
        }]
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
    from oci.data_connectivity.models import CreateDataProfileDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataProfileActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        create
    """

    @staticmethod
    def get_module_resource_id_param():
        return "registry_id"

    def get_module_resource_id(self):
        return self.module.params.get("registry_id")

    def create(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, CreateDataProfileDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_data_profile,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                create_data_profile_details=action_details,
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


DataProfileActionsHelperCustom = get_custom_class("DataProfileActionsHelperCustom")


class ResourceHelper(DataProfileActionsHelperCustom, DataProfileActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            registry_id=dict(aliases=["id"], type="str", required=True),
            read_operation_config=dict(
                type="dict",
                options=dict(
                    model_type=dict(
                        type="str",
                        required=True,
                        choices=["READ_OPERATION_CONFIG", "WRITE_OPERATION_CONFIG"],
                    ),
                    key=dict(type="str", no_log=True),
                    model_version=dict(type="str"),
                    parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
                    operations=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            query=dict(type="str"),
                            is_distinct=dict(type="bool"),
                            select_columns=dict(
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
                            condition=dict(type="str"),
                            policy=dict(
                                type="str",
                                choices=[
                                    "INNER_JOIN",
                                    "LEFT_JOIN",
                                    "RIGHT_JOIN",
                                    "FULL_JOIN",
                                ],
                            ),
                            sort_clauses=dict(
                                type="list",
                                elements="dict",
                                options=dict(
                                    field=dict(
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
                                    order=dict(type="str", choices=["ASC", "DESC"]),
                                ),
                            ),
                            model_type=dict(
                                type="str",
                                required=True,
                                choices=["QUERY", "SELECT", "JOIN", "SORT", "FILTER"],
                            ),
                            filter_condition=dict(type="str"),
                        ),
                    ),
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
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "AVRO_FORMAT",
                                            "JSON_FORMAT",
                                            "CSV_FORMAT",
                                            "PARQUET_FORMAT",
                                        ],
                                    ),
                                    compression=dict(type="str"),
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
                    partition_config=dict(
                        type="dict",
                        options=dict(
                            model_type=dict(
                                type="str",
                                required=True,
                                choices=["KEYRANGEPARTITIONCONFIG"],
                            ),
                            partition_number=dict(type="int"),
                            key_range=dict(
                                type="dict",
                                no_log=False,
                                options=dict(
                                    key=dict(
                                        type="dict",
                                        no_log=False,
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
                                    range=dict(type="list", elements="str"),
                                ),
                            ),
                        ),
                    ),
                    read_attribute=dict(
                        type="dict",
                        options=dict(
                            extract_strategy=dict(
                                type="str", choices=["FULL", "INCREMENTAL"]
                            ),
                            external_storage=dict(
                                type="dict",
                                options=dict(
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["EXTERNAL_STORAGE"],
                                    ),
                                    storage_id=dict(type="str"),
                                    storage_name=dict(type="str"),
                                    host=dict(type="str"),
                                    tenancy_id=dict(type="str"),
                                    namespace=dict(type="str"),
                                    bucket=dict(type="str"),
                                ),
                            ),
                            initial_extract_date=dict(type="str"),
                            last_extract_date=dict(type="str"),
                            model_type=dict(
                                type="str",
                                required=True,
                                choices=[
                                    "ORACLE_READ_ATTRIBUTE",
                                    "BICC_READ_ATTRIBUTE",
                                    "ORACLEREADATTRIBUTE",
                                ],
                            ),
                            fetch_size=dict(type="int"),
                        ),
                    ),
                    object_status=dict(type="int"),
                    read_raw_data=dict(type="bool"),
                ),
            ),
            data_asset=dict(
                type="dict",
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
            connection=dict(
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
                                type="dict", options=dict(parent=dict(type="str"))
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
                        ),
                    ),
                    connection_properties=dict(
                        type="list",
                        elements="dict",
                        options=dict(name=dict(type="str"), value=dict(type="str")),
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
            schema=dict(
                type="dict",
                options=dict(
                    key=dict(type="str", required=True, no_log=True),
                    model_type=dict(type="str", required=True),
                    model_version=dict(type="str"),
                    parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
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
                ),
            ),
            data_entity=dict(
                type="dict",
                options=dict(
                    filters=dict(type="str"),
                    is_effective_date_disabled=dict(type="bool"),
                    is_flex_data_store=dict(type="bool"),
                    is_silent_error=dict(type="bool"),
                    supports_incremental=dict(type="bool"),
                    sql_query=dict(type="str"),
                    model_type=dict(
                        type="str",
                        required=True,
                        choices=[
                            "TABLE_ENTITY",
                            "DATA_STORE_ENTITY",
                            "VIEW_ENTITY",
                            "SQL_ENTITY",
                            "FILE_ENTITY",
                        ],
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
                    key=dict(type="str", no_log=True),
                    model_version=dict(type="str"),
                    parent_ref=dict(type="dict", options=dict(parent=dict(type="str"))),
                    name=dict(type="str"),
                    description=dict(type="str"),
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
                            parent_ref=dict(
                                type="dict", options=dict(parent=dict(type="str"))
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
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
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
                                            config_definition=dict(
                                                type="ConfigDefinition"
                                            ),
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
                                            port_type=dict(
                                                type="str",
                                                choices=["DATA", "CONTROL", "MODEL"],
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
                                                    parent_ref=dict(
                                                        type="ParentReference"
                                                    ),
                                                    config_values=dict(
                                                        type="ConfigValues"
                                                    ),
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
                                                    parent_ref=dict(
                                                        type="ParentReference"
                                                    ),
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
                                            config_parameter_definitions=dict(
                                                type="dict"
                                            ),
                                        ),
                                    ),
                                ),
                            ),
                        ),
                    ),
                    shape_id=dict(type="str"),
                    entity_type=dict(
                        type="str",
                        choices=["TABLE", "VIEW", "FILE", "SQL", "DATA_STORE"],
                    ),
                    other_type_label=dict(type="str"),
                    unique_keys=dict(
                        type="list",
                        elements="dict",
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
                    foreign_keys=dict(
                        type="list",
                        elements="dict",
                        no_log=False,
                        options=dict(
                            model_type=dict(
                                type="str", required=True, choices=["FOREIGN_KEY"]
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
                            update_rule=dict(type="int"),
                            delete_rule=dict(type="int"),
                            reference_unique_key=dict(
                                type="dict",
                                no_log=False,
                                options=dict(
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=["PRIMARY_KEY"],
                                    ),
                                    key=dict(type="str", no_log=True),
                                    model_version=dict(type="str"),
                                    parent_ref=dict(
                                        type="dict",
                                        options=dict(parent=dict(type="str")),
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
                                                    type=dict(type="dict"),
                                                    labels=dict(
                                                        type="list", elements="str"
                                                    ),
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
                                                            key=dict(
                                                                type="str", no_log=True
                                                            ),
                                                            model_version=dict(
                                                                type="str"
                                                            ),
                                                            parent_ref=dict(
                                                                type="dict",
                                                                options=dict(
                                                                    parent=dict(
                                                                        type="str"
                                                                    )
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
                                                            object_status=dict(
                                                                type="int"
                                                            ),
                                                            name=dict(type="str"),
                                                            description=dict(
                                                                type="str"
                                                            ),
                                                            type=dict(
                                                                type="dict",
                                                                required=True,
                                                            ),
                                                            position=dict(type="int"),
                                                            default_value_string=dict(
                                                                type="str"
                                                            ),
                                                            is_mandatory=dict(
                                                                type="bool"
                                                            ),
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
                                    model_type=dict(
                                        type="str",
                                        required=True,
                                        choices=[
                                            "AVRO_FORMAT",
                                            "JSON_FORMAT",
                                            "CSV_FORMAT",
                                            "PARQUET_FORMAT",
                                        ],
                                    ),
                                    compression=dict(type="str"),
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
                    object_status=dict(type="int"),
                    identifier=dict(type="str"),
                ),
            ),
            profile_config=dict(
                type="dict",
                options=dict(
                    attributes=dict(type="list", elements="str"),
                    functions=dict(
                        type="list",
                        elements="str",
                        choices=[
                            "ATTRIBUTE_COUNT",
                            "ROW_COUNT",
                            "DATA_TYPE",
                            "DISTINCT_COUNT",
                            "DUPLICATE_COUNT",
                            "HISTOGRAM",
                            "MAX",
                            "MAX_LENGTH",
                            "MEAN",
                            "MEAN_LENGTH",
                            "MEDIAN",
                            "MIN",
                            "MIN_LENGTH",
                            "NULL_COUNT",
                            "OUTLIER",
                            "PATTERN",
                            "STANDARD_DEVIATION",
                            "UNIQUE_COUNT",
                            "VARIANCE",
                            "VALUE_FREQUENCY",
                        ],
                    ),
                    top_n_val_freq=dict(type="int"),
                    pattern_threshold=dict(type="int"),
                    data_type_threshold=dict(type="int"),
                ),
            ),
            endpoint_id=dict(type="str"),
            action=dict(type="str", required=True, choices=["create"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_profile",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
