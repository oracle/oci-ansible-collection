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
module: oci_data_catalog_custom_property_facts
short_description: Fetches details about one or multiple CustomProperty resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple CustomProperty resources in Oracle Cloud Infrastructure
    - Returns a list of custom properties within a data catalog.
    - If I(custom_property_key) is specified, the details of a single CustomProperty will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        required: true
    namespace_id:
        description:
            - Unique namespace identifier.
        type: str
        required: true
    custom_property_key:
        description:
            - Unique Custom Property key
            - Required to get a specific custom_property.
        type: str
    fields:
        description:
            - Specifies the fields to return in a custom property response.
        type: list
        choices:
            - "key"
            - "displayName"
            - "description"
            - "dataType"
            - "namespaceName"
            - "lifecycleState"
            - "timeCreated"
            - "timeUpdated"
            - "createdById"
            - "updatedById"
            - "properties"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given. The match is not case sensitive.
        type: str
        aliases: ["name"]
    display_name_contains:
        description:
            - "A filter to return only resources that match display name pattern given. The match is not case sensitive.
              For Example : /folders?displayNameContains=Cu.*
              The above would match all folders with display name that starts with \\"Cu\\"."
        type: str
    data_types:
        description:
            - Return the custom properties which has specified data types
        type: list
        choices:
            - "TEXT"
            - "RICH_TEXT"
            - "BOOLEAN"
            - "NUMBER"
            - "DATE"
    type_name:
        description:
            - A filter to return only resources that match the entire type name given. The match is not case sensitive
        type: list
        choices:
            - "DATA_ASSET"
            - "AUTONOMOUS_DATA_WAREHOUSE"
            - "HIVE"
            - "KAFKA"
            - "MYSQL"
            - "ORACLE_OBJECT_STORAGE"
            - "AUTONOMOUS_TRANSACTION_PROCESSING"
            - "ORACLE"
            - "POSTGRESQL"
            - "MICROSOFT_AZURE_SQL_DATABASE"
            - "MICROSOFT_SQL_SERVER"
            - "IBM_DB2"
            - "DATA_ENTITY"
            - "LOGICAL_ENTITY"
            - "TABLE"
            - "VIEW"
            - "ATTRIBUTE"
            - "FOLDER"
            - "ORACLE_ANALYTICS_SUBJECT_AREA_COLUMN"
            - "ORACLE_ANALYTICS_LOGICAL_COLUMN"
            - "ORACLE_ANALYTICS_PHYSICAL_COLUMN"
            - "ORACLE_ANALYTICS_ANALYSIS_COLUMN"
            - "ORACLE_ANALYTICS_SERVER"
            - "ORACLE_ANALYTICS_CLOUD"
            - "ORACLE_ANALYTICS_SUBJECT_AREA"
            - "ORACLE_ANALYTICS_DASHBOARD"
            - "ORACLE_ANALYTICS_BUSINESS_MODEL"
            - "ORACLE_ANALYTICS_PHYSICAL_DATABASE"
            - "ORACLE_ANALYTICS_PHYSICAL_SCHEMA"
            - "ORACLE_ANALYTICS_PRESENTATION_TABLE"
            - "ORACLE_ANALYTICS_LOGICAL_TABLE"
            - "ORACLE_ANALYTICS_PHYSICAL_TABLE"
            - "ORACLE_ANALYTICS_ANALYSIS"
            - "DATABASE_SCHEMA"
            - "TOPIC"
            - "CONNECTION"
            - "GLOSSARY"
            - "TERM"
            - "CATEGORY"
            - "FILE"
            - "BUCKET"
            - "MESSAGE"
            - "UNRECOGNIZED_FILE"
    lifecycle_state:
        description:
            - A filter to return only resources that match the specified lifecycle state. The value is case insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "MOVING"
    time_created:
        description:
            - Time that the resource was created. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
        type: str
    time_updated:
        description:
            - Time that the resource was updated. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
        type: str
    created_by_id:
        description:
            - OCID of the user who created the resource.
        type: str
    updated_by_id:
        description:
            - OCID of the user who updated the resource.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for USAGECOUNT and DISPLAYNAME is Ascending
        type: str
        choices:
            - "DISPLAYNAME"
            - "USAGECOUNT"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List custom_properties
  oci_data_catalog_custom_property_facts:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific custom_property
  oci_data_catalog_custom_property_facts:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"
    custom_property_key: custom_property_key_example

"""

RETURN = """
custom_properties:
    description:
        - List of CustomProperty resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique data asset key that is immutable.
            returned: on success
            type: string
            sample: key_example
        display_name:
            description:
                - Display name of the custom property
            returned: on success
            type: string
            sample: display_name_example
        data_type:
            description:
                - Data type of the custom property
            returned: on success
            type: string
            sample: TEXT
        description:
            description:
                - Description for the custom property
            returned: on success
            type: string
            sample: description_example
        namespace_name:
            description:
                - Namespace name of the custom property
            returned: on success
            type: string
            sample: namespace_name_example
        is_list_type:
            description:
                - Is this property allowed to have list of values
            returned: on success
            type: bool
            sample: true
        is_sortable:
            description:
                - If this field allows to sort from UI
            returned: on success
            type: bool
            sample: true
        is_filterable:
            description:
                - If this field allows to filter or create facets from UI
            returned: on success
            type: bool
            sample: true
        is_multi_valued:
            description:
                - If this field allows multiple values to be set
            returned: on success
            type: bool
            sample: true
        is_hidden:
            description:
                - If this field is a hidden field
            returned: on success
            type: bool
            sample: true
        is_editable:
            description:
                - If this field is a editable field
            returned: on success
            type: bool
            sample: true
        is_shown_in_list:
            description:
                - If this field is displayed in a list view of applicable objects.
            returned: on success
            type: bool
            sample: true
        is_service_defined:
            description:
                - If this field is defined by service or by a user
            returned: on success
            type: bool
            sample: true
        is_hidden_in_search:
            description:
                - If this field is allowed to pop in search results
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of the custom property.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - "The date and time the custom property was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2019-03-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-03-25T21:10:29.600Z
        time_updated:
            description:
                - The last time that any change was made to the custom property. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        created_by_id:
            description:
                - OCID of the user who created the custom property.
            returned: on success
            type: string
            sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_id:
            description:
                - OCID of the user who last modified the custom property.
            returned: on success
            type: string
            sample: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
        usage_count:
            description:
                - Total number of first class objects using this custom property
            returned: on success
            type: int
            sample: 56
        is_event_enabled:
            description:
                - If an OCI Event will be emitted when the custom property is modified.
            returned: on success
            type: bool
            sample: true
        scope:
            description:
                - The set of object types to which the custom property applies.
            returned: on success
            type: complex
            contains:
                type_id:
                    description:
                        - Unique type key identifier
                    returned: on success
                    type: string
                    sample: "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx"
                type_name:
                    description:
                        - Name of the type associated with
                    returned: on success
                    type: string
                    sample: type_name_example
                count:
                    description:
                        - Number of objects associated with this type
                    returned: on success
                    type: int
                    sample: 56
                is_event_enabled:
                    description:
                        - If an OCI Event will be emitted when the custom property is modified.
                    returned: on success
                    type: bool
                    sample: true
        allowed_values:
            description:
                - Allowed values for the custom property if any
            returned: on success
            type: list
            sample: []
        events:
            description:
                - Event configuration for this custom property, against the desired subset of object types to which the property applies.
            returned: on success
            type: complex
            contains:
                type_id:
                    description:
                        - Unique type key identifier.
                    returned: on success
                    type: string
                    sample: "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx"
                type_name:
                    description:
                        - Name of the type.
                    returned: on success
                    type: string
                    sample: type_name_example
                property_id:
                    description:
                        - Unique property key identifier.
                    returned: on success
                    type: string
                    sample: "ocid1.property.oc1..xxxxxxEXAMPLExxxxxx"
                property_name:
                    description:
                        - Name of the property.
                    returned: on success
                    type: string
                    sample: property_name_example
                event_config_status:
                    description:
                        - Status of the configuration.
                    returned: on success
                    type: string
                    sample: ENABLED
                time_created:
                    description:
                        - "The date and time the event was configured, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2019-03-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2019-03-25T21:10:29.600Z
                time_updated:
                    description:
                        - The last time that any change was made to the configuration. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime
                          string.
                    returned: on success
                    type: string
                    sample: 2013-10-20T19:20:30+01:00
                created_by_id:
                    description:
                        - OCID of the user who created the configuration.
                    returned: on success
                    type: string
                    sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
                updated_by_id:
                    description:
                        - OCID of the user who last modified the configuration.
                    returned: on success
                    type: string
                    sample: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
        properties:
            description:
                - "A map of maps that contains the properties which are specific to the asset type. Each data asset type
                  definition defines it's set of required and optional properties. The map keys are category names and the
                  values are maps of property name to property value. Every property is contained inside of a category. Most
                  data assets have required properties within the \\"default\\" category.
                  Example: `{\\"properties\\": { \\"default\\": { \\"host\\": \\"host1\\", \\"port\\": \\"1521\\", \\"database\\": \\"orcl\\"}}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "key": "key_example",
        "display_name": "display_name_example",
        "data_type": "TEXT",
        "description": "description_example",
        "namespace_name": "namespace_name_example",
        "is_list_type": true,
        "is_sortable": true,
        "is_filterable": true,
        "is_multi_valued": true,
        "is_hidden": true,
        "is_editable": true,
        "is_shown_in_list": true,
        "is_service_defined": true,
        "is_hidden_in_search": true,
        "lifecycle_state": "CREATING",
        "time_created": "2019-03-25T21:10:29.600Z",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
        "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx",
        "usage_count": 56,
        "is_event_enabled": true,
        "scope": [{
            "type_id": "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx",
            "type_name": "type_name_example",
            "count": 56,
            "is_event_enabled": true
        }],
        "allowed_values": [],
        "events": [{
            "type_id": "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx",
            "type_name": "type_name_example",
            "property_id": "ocid1.property.oc1..xxxxxxEXAMPLExxxxxx",
            "property_name": "property_name_example",
            "event_config_status": "ENABLED",
            "time_created": "2019-03-25T21:10:29.600Z",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
            "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "properties": {}
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.data_catalog import DataCatalogClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogCustomPropertyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "catalog_id",
            "namespace_id",
            "custom_property_key",
        ]

    def get_required_params_for_list(self):
        return [
            "catalog_id",
            "namespace_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_property,
            catalog_id=self.module.params.get("catalog_id"),
            namespace_id=self.module.params.get("namespace_id"),
            custom_property_key=self.module.params.get("custom_property_key"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "display_name_contains",
            "data_types",
            "type_name",
            "lifecycle_state",
            "time_created",
            "time_updated",
            "created_by_id",
            "updated_by_id",
            "fields",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_custom_properties,
            catalog_id=self.module.params.get("catalog_id"),
            namespace_id=self.module.params.get("namespace_id"),
            **optional_kwargs
        )


DataCatalogCustomPropertyFactsHelperCustom = get_custom_class(
    "DataCatalogCustomPropertyFactsHelperCustom"
)


class ResourceFactsHelper(
    DataCatalogCustomPropertyFactsHelperCustom, DataCatalogCustomPropertyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            catalog_id=dict(type="str", required=True),
            namespace_id=dict(type="str", required=True),
            custom_property_key=dict(type="str"),
            fields=dict(
                type="list",
                choices=[
                    "key",
                    "displayName",
                    "description",
                    "dataType",
                    "namespaceName",
                    "lifecycleState",
                    "timeCreated",
                    "timeUpdated",
                    "createdById",
                    "updatedById",
                    "properties",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            display_name_contains=dict(type="str"),
            data_types=dict(
                type="list", choices=["TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE"]
            ),
            type_name=dict(
                type="list",
                choices=[
                    "DATA_ASSET",
                    "AUTONOMOUS_DATA_WAREHOUSE",
                    "HIVE",
                    "KAFKA",
                    "MYSQL",
                    "ORACLE_OBJECT_STORAGE",
                    "AUTONOMOUS_TRANSACTION_PROCESSING",
                    "ORACLE",
                    "POSTGRESQL",
                    "MICROSOFT_AZURE_SQL_DATABASE",
                    "MICROSOFT_SQL_SERVER",
                    "IBM_DB2",
                    "DATA_ENTITY",
                    "LOGICAL_ENTITY",
                    "TABLE",
                    "VIEW",
                    "ATTRIBUTE",
                    "FOLDER",
                    "ORACLE_ANALYTICS_SUBJECT_AREA_COLUMN",
                    "ORACLE_ANALYTICS_LOGICAL_COLUMN",
                    "ORACLE_ANALYTICS_PHYSICAL_COLUMN",
                    "ORACLE_ANALYTICS_ANALYSIS_COLUMN",
                    "ORACLE_ANALYTICS_SERVER",
                    "ORACLE_ANALYTICS_CLOUD",
                    "ORACLE_ANALYTICS_SUBJECT_AREA",
                    "ORACLE_ANALYTICS_DASHBOARD",
                    "ORACLE_ANALYTICS_BUSINESS_MODEL",
                    "ORACLE_ANALYTICS_PHYSICAL_DATABASE",
                    "ORACLE_ANALYTICS_PHYSICAL_SCHEMA",
                    "ORACLE_ANALYTICS_PRESENTATION_TABLE",
                    "ORACLE_ANALYTICS_LOGICAL_TABLE",
                    "ORACLE_ANALYTICS_PHYSICAL_TABLE",
                    "ORACLE_ANALYTICS_ANALYSIS",
                    "DATABASE_SCHEMA",
                    "TOPIC",
                    "CONNECTION",
                    "GLOSSARY",
                    "TERM",
                    "CATEGORY",
                    "FILE",
                    "BUCKET",
                    "MESSAGE",
                    "UNRECOGNIZED_FILE",
                ],
            ),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "MOVING",
                ],
            ),
            time_created=dict(type="str"),
            time_updated=dict(type="str"),
            created_by_id=dict(type="str"),
            updated_by_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["DISPLAYNAME", "USAGECOUNT"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="custom_property",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(custom_properties=result)


if __name__ == "__main__":
    main()
