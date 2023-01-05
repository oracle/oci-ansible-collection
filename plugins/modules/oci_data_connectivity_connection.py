#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_data_connectivity_connection
short_description: Manage a Connection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Connection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a connection under an existing data asset.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    key:
        description:
            - Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is required, a value can be
              passed in create.
        type: str
    model_version:
        description:
            - The model version of an object.
            - This parameter is updatable.
        type: str
    model_type:
        description:
            - The type of the object.
            - This parameter is updatable.
        type: str
    name:
        description:
            - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable
              and is restricted to 1000 characters.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    description:
        description:
            - User-defined description of the connection.
            - This parameter is updatable.
        type: str
    object_version:
        description:
            - The version of the object that is used to track changes in the object instance.
            - This parameter is updatable.
        type: int
    object_status:
        description:
            - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
            - This parameter is updatable.
        type: int
    identifier:
        description:
            - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can be
              modified.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    primary_schema:
        description:
            - ""
            - This parameter is updatable.
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
                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
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
                    - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value can
                      be modified.
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
                            - Labels are keywords or tags that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                              categorize content.
                        type: list
                        elements: str
                    is_favorite:
                        description:
                            - Specifies whether this object is a favorite.
                        type: bool
    connection_properties:
        description:
            - The properties of the connection.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            name:
                description:
                    - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                      editable and is restricted to 1000 characters.
                type: str
            value:
                description:
                    - The value for the connection name property.
                type: str
    properties:
        description:
            - All the properties of the connection in a key-value map format.
            - Required for create using I(state=present), update using I(state=present) with connection_key present.
        type: dict
    type:
        description:
            - Specific Connection Type
            - Required for create using I(state=present), update using I(state=present) with connection_key present.
        type: str
    is_default:
        description:
            - The default property of the connection.
            - This parameter is updatable.
        type: bool
    metadata:
        description:
            - ""
            - This parameter is updatable.
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
    registry_metadata:
        description:
            - ""
            - This parameter is updatable.
        type: dict
        suboptions:
            aggregator_key:
                description:
                    - The owning object's key for this object.
                type: str
            labels:
                description:
                    - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
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
    registry_id:
        description:
            - The registry OCID.
        type: str
        required: true
    connection_key:
        description:
            - The connection key.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    data_asset_key:
        description:
            - Used to filter by the data asset key of the object.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the Connection.
            - Use I(state=present) to create or update a Connection.
            - Use I(state=absent) to delete a Connection.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create connection
  oci_data_connectivity_connection:
    # required
    name: name_example
    identifier: identifier_example
    properties: null
    type: type_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    key: key_example
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

- name: Update connection
  oci_data_connectivity_connection:
    # required
    properties: null
    type: type_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    connection_key: connection_key_example

    # optional
    model_version: model_version_example
    model_type: model_type_example
    name: name_example
    description: description_example
    object_version: 56
    object_status: 56
    identifier: identifier_example
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

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_connectivity_connection:
    # required
    name: name_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example

    # optional
    model_version: model_version_example
    model_type: model_type_example
    description: description_example
    object_version: 56
    object_status: 56
    identifier: identifier_example
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

- name: Delete connection
  oci_data_connectivity_connection:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    connection_key: connection_key_example
    state: absent

- name: Delete connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_connectivity_connection:
    # required
    name: name_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    state: absent

"""

RETURN = """
connection:
    description:
        - Details of the Connection resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Generated key that can be used in API calls to identify the connection. In scenarios where reference to the connection is required, a value
                  can be passed in create.
            returned: on success
            type: str
            sample: key_example
        model_version:
            description:
                - The model version of an object.
            returned: on success
            type: str
            sample: model_version_example
        model_type:
            description:
                - The type of the object.
            returned: on success
            type: str
            sample: model_type_example
        name:
            description:
                - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is
                  editable and is restricted to 1000 characters.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - User-defined description for the connection.
            returned: on success
            type: str
            sample: description_example
        object_version:
            description:
                - The version of the object that is used to track changes in the object instance.
            returned: on success
            type: int
            sample: 56
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
        primary_schema:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - The object key.
                    returned: on success
                    type: str
                    sample: key_example
                model_type:
                    description:
                        - The object type.
                    returned: on success
                    type: str
                    sample: model_type_example
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
                resource_name:
                    description:
                        - A resource name can have letters, numbers, and special characters. The value is editable and is restricted to 4000 characters.
                    returned: on success
                    type: str
                    sample: resource_name_example
                description:
                    description:
                        - User-defined description for the schema.
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
                is_has_containers:
                    description:
                        - Specifies whether the schema has containers.
                    returned: on success
                    type: bool
                    sample: true
                default_connection:
                    description:
                        - The default connection key.
                    returned: on success
                    type: str
                    sample: default_connection_example
                object_status:
                    description:
                        - The status of an object that can be set to value 1 for shallow references across objects, other values reserved.
                    returned: on success
                    type: int
                    sample: 56
                identifier:
                    description:
                        - Value can only contain upper case letters, underscore, and numbers. It should begin with an upper case letter or underscore. The value
                          can be modified.
                    returned: on success
                    type: str
                    sample: identifier_example
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
        connection_properties:
            description:
                - The properties of the connection.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value
                          is editable and is restricted to 1000 characters.
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - The value for the connection name property.
                    returned: on success
                    type: str
                    sample: value_example
        properties:
            description:
                - All the properties of the connection in a key-value map format.
            returned: on success
            type: dict
            sample: {}
        type:
            description:
                - Specific Connection Type
            returned: on success
            type: str
            sample: type_example
        is_default:
            description:
                - The default property of the connection.
            returned: on success
            type: bool
            sample: true
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
        registry_metadata:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                aggregator_key:
                    description:
                        - The owning object's key for this object.
                    returned: on success
                    type: str
                    sample: aggregator_key_example
                labels:
                    description:
                        - Labels are keywords or labels that you can add to data assets, dataflows, and so on. You can define your own labels and use them to
                          categorize content.
                    returned: on success
                    type: list
                    sample: []
                registry_version:
                    description:
                        - The registry version.
                    returned: on success
                    type: int
                    sample: 56
                key:
                    description:
                        - The identifying key for the object.
                    returned: on success
                    type: str
                    sample: key_example
                is_favorite:
                    description:
                        - Specifies whether the object is a favorite.
                    returned: on success
                    type: bool
                    sample: true
                created_by_user_id:
                    description:
                        - The ID of the user who created the object.
                    returned: on success
                    type: str
                    sample: "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                created_by_user_name:
                    description:
                        - The name of the user who created the object.
                    returned: on success
                    type: str
                    sample: created_by_user_name_example
                updated_by_user_id:
                    description:
                        - The ID of the user who updated the object.
                    returned: on success
                    type: str
                    sample: "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx"
                updated_by_user_name:
                    description:
                        - The name of the user who updated the object.
                    returned: on success
                    type: str
                    sample: updated_by_user_name_example
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
    sample: {
        "key": "key_example",
        "model_version": "model_version_example",
        "model_type": "model_type_example",
        "name": "name_example",
        "description": "description_example",
        "object_version": 56,
        "object_status": 56,
        "identifier": "identifier_example",
        "primary_schema": {
            "key": "key_example",
            "model_type": "model_type_example",
            "model_version": "model_version_example",
            "parent_ref": {
                "parent": "parent_example"
            },
            "name": "name_example",
            "resource_name": "resource_name_example",
            "description": "description_example",
            "object_version": 56,
            "external_key": "external_key_example",
            "is_has_containers": true,
            "default_connection": "default_connection_example",
            "object_status": 56,
            "identifier": "identifier_example",
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
        },
        "connection_properties": [{
            "name": "name_example",
            "value": "value_example"
        }],
        "properties": {},
        "type": "type_example",
        "is_default": true,
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
        "registry_metadata": {
            "aggregator_key": "aggregator_key_example",
            "labels": [],
            "registry_version": 56,
            "key": "key_example",
            "is_favorite": true,
            "created_by_user_id": "ocid1.createdbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "created_by_user_name": "created_by_user_name_example",
            "updated_by_user_id": "ocid1.updatedbyuser.oc1..xxxxxxEXAMPLExxxxxx",
            "updated_by_user_name": "updated_by_user_name_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00"
        }
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
    from oci.data_connectivity import DataConnectivityManagementClient
    from oci.data_connectivity.models import CreateConnectionDetails
    from oci.data_connectivity.models import UpdateConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ConnectionHelperGen, self).get_possible_entity_types() + [
            "connection",
            "connections",
            "dataConnectivityconnection",
            "dataConnectivityconnections",
            "connectionresource",
            "connectionsresource",
            "dataconnectivity",
        ]

    def get_module_resource_id_param(self):
        return "connection_key"

    def get_module_resource_id(self):
        return self.module.params.get("connection_key")

    def get_get_fn(self):
        return self.client.get_connection

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            connection_key=summary_model.key,
            registry_id=self.module.params.get("registry_id"),
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "registry_id",
            "data_asset_key",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["name"] if self._use_name_as_identifier() else ["name", "type"]
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
        return oci_common_utils.list_all_resources(
            self.client.list_connections, **kwargs
        )

    def get_create_model_class(self):
        return CreateConnectionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                create_connection_details=create_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                connection_key=self.module.params.get("connection_key"),
                update_connection_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                registry_id=self.module.params.get("registry_id"),
                connection_key=self.module.params.get("connection_key"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ConnectionHelperCustom = get_custom_class("ConnectionHelperCustom")


class ResourceHelper(ConnectionHelperCustom, ConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            key=dict(type="str", no_log=True),
            model_version=dict(type="str"),
            model_type=dict(type="str"),
            name=dict(type="str"),
            description=dict(type="str"),
            object_version=dict(type="int"),
            object_status=dict(type="int"),
            identifier=dict(type="str"),
            primary_schema=dict(
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
            registry_id=dict(type="str", required=True),
            connection_key=dict(type="str", no_log=True),
            data_asset_key=dict(type="str", no_log=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection",
        service_client_class=DataConnectivityManagementClient,
        namespace="data_connectivity",
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
