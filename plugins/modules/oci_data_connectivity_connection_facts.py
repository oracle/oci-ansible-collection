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
module: oci_data_connectivity_connection_facts
short_description: Fetches details about one or multiple Connection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Connection resources in Oracle Cloud Infrastructure
    - Retrieves a list of all connections.
    - If I(connection_key) is specified, the details of a single Connection will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_key:
        description:
            - The connection key.
            - Required to get a specific connection.
        type: str
    registry_id:
        description:
            - The registry OCID.
        type: str
        required: true
    data_asset_key:
        description:
            - Used to filter by the data asset key of the object.
            - Required to list multiple connections.
        type: str
    name:
        description:
            - Used to filter by the name of the object.
        type: str
    fields:
        description:
            - Specifies the fields to get for an object.
        type: list
        elements: str
    type:
        description:
            - Type of the object to filter the results with.
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
    favorites_query_param:
        description:
            - If value is FAVORITES_ONLY, then only objects marked as favorite by the requesting user will be included in result. If value is
              NON_FAVORITES_ONLY, then objects marked as favorites by the requesting user will be skipped. If value is ALL or if not specified, all objects,
              irrespective of favorites or not will be returned. Default is ALL.
        type: str
        choices:
            - "FAVORITES_ONLY"
            - "NON_FAVORITES_ONLY"
            - "ALL"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific connection
  oci_data_connectivity_connection_facts:
    # required
    connection_key: connection_key_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"

- name: List connections
  oci_data_connectivity_connection_facts:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example

    # optional
    name: name_example
    fields: [ "fields_example" ]
    type: type_example
    sort_by: id
    sort_order: ASC
    favorites_query_param: FAVORITES_ONLY

"""

RETURN = """
connections:
    description:
        - List of Connection resources
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
    sample: [{
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


class ConnectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "registry_id",
            "connection_key",
        ]

    def get_required_params_for_list(self):
        return [
            "registry_id",
            "data_asset_key",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "fields",
            "type",
            "sort_by",
            "sort_order",
            "favorites_query_param",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_connections,
            registry_id=self.module.params.get("registry_id"),
            data_asset_key=self.module.params.get("data_asset_key"),
            **optional_kwargs
        )


ConnectionFactsHelperCustom = get_custom_class("ConnectionFactsHelperCustom")


class ResourceFactsHelper(ConnectionFactsHelperCustom, ConnectionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            connection_key=dict(type="str", no_log=True),
            registry_id=dict(type="str", required=True),
            data_asset_key=dict(type="str", no_log=True),
            name=dict(type="str"),
            fields=dict(type="list", elements="str"),
            type=dict(type="str"),
            sort_by=dict(type="str", choices=["id", "timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            favorites_query_param=dict(
                type="str", choices=["FAVORITES_ONLY", "NON_FAVORITES_ONLY", "ALL"]
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="connection",
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

    module.exit_json(connections=result)


if __name__ == "__main__":
    main()
