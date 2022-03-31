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
module: oci_data_connectivity_schema_facts
short_description: Fetches details about one or multiple Schema resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Schema resources in Oracle Cloud Infrastructure
    - Retrieves a list of all the schemas that can be accessed using the specified connection.
    - If I(schema_resource_name) is specified, the details of a single Schema will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    schema_resource_name:
        description:
            - The schema resource name used for retrieving schemas.
            - Required to get a specific schema.
        type: str
    registry_id:
        description:
            - The registry Ocid.
        type: str
        required: true
    connection_key:
        description:
            - The connection key.
        type: str
        required: true
    fields:
        description:
            - Specifies the fields to get for an object.
        type: list
        elements: str
    sort_by:
        description:
            - Specifies the field to sort by. Accepts only one field. By default, when you sort by time fields, results are shown in descending order. All other
              fields default to ascending order. Sorting related parameters are ignored when parameter `query` is present (search operation and sorting order is
              by relevance score in descending order).
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
    schema_resource_key:
        description:
            - Schema resource name used for retrieving schemas.
        type: str
    name:
        description:
            - Used to filter by the name of the object.
        type: str
    name_list:
        description:
            - Used to filter by the name of the object.
        type: list
        elements: str
    endpoint_id:
        description:
            - Endpoint Id used for getDataAssetFullDetails.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific schema
  oci_data_connectivity_schema_facts:
    # required
    schema_resource_name: schema_resource_name_example
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    connection_key: connection_key_example

    # optional
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

- name: List schemas
  oci_data_connectivity_schema_facts:
    # required
    registry_id: "ocid1.registry.oc1..xxxxxxEXAMPLExxxxxx"
    connection_key: connection_key_example

    # optional
    fields: [ "fields_example" ]
    sort_by: id
    sort_order: ASC
    schema_resource_key: schema_resource_key_example
    name: name_example
    name_list: [ "name_list_example" ]
    endpoint_id: "ocid1.endpoint.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
schemas:
    description:
        - List of Schema resources
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
                - The object's type.
            returned: on success
            type: str
            sample: model_type_example
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
                - Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable
                  and is restricted to 1000 characters.
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
                - The external key for the object.
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
                - Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be
                  modified.
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
                        - The full path to identify this object.
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
                        - Labels are keywords or tags that you can add to data assets, dataflows and so on. You can define your own labels and use them to
                          categorize content.
                    returned: on success
                    type: list
                    sample: []
                is_favorite:
                    description:
                        - Specifies whether this object is a favorite or not.
                    returned: on success
                    type: bool
                    sample: true
    sample: [{
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


class SchemaFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "registry_id",
            "connection_key",
            "schema_resource_name",
        ]

    def get_required_params_for_list(self):
        return [
            "registry_id",
            "connection_key",
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
            self.client.get_schema,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
            schema_resource_name=self.module.params.get("schema_resource_name"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "fields",
            "sort_by",
            "sort_order",
            "schema_resource_key",
            "name",
            "name_list",
            "endpoint_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_schemas,
            registry_id=self.module.params.get("registry_id"),
            connection_key=self.module.params.get("connection_key"),
            **optional_kwargs
        )


SchemaFactsHelperCustom = get_custom_class("SchemaFactsHelperCustom")


class ResourceFactsHelper(SchemaFactsHelperCustom, SchemaFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            schema_resource_name=dict(type="str"),
            registry_id=dict(type="str", required=True),
            connection_key=dict(type="str", required=True, no_log=True),
            fields=dict(type="list", elements="str"),
            sort_by=dict(type="str", choices=["id", "timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            schema_resource_key=dict(type="str", no_log=True),
            name=dict(type="str"),
            name_list=dict(type="list", elements="str"),
            endpoint_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="schema",
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

    module.exit_json(schemas=result)


if __name__ == "__main__":
    main()
