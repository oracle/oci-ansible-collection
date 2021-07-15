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
module: oci_data_catalog_data_asset_actions
short_description: Perform actions on a DataAsset resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DataAsset resource in Oracle Cloud Infrastructure
    - For I(action=add_data_selector_patterns), add data selector pattern to the data asset.
    - For I(action=import_connection), import new connection for this data asset.
    - For I(action=import_data_asset), import technical objects to a Data Asset
    - For I(action=parse_connection), parse data asset references through connections from this data asset.
    - For I(action=remove_data_selector_patterns), remove data selector pattern from the data asset.
    - For I(action=synchronous_export), export technical objects from a Data Asset
    - For I(action=validate_connection), validate connection by connecting to the data asset using credentials in metadata.
version_added: "2.9"
author: Oracle (@oracle)
options:
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        required: true
    data_asset_key:
        description:
            - Unique data asset key.
        type: str
        required: true
    items:
        description:
            - Collection of pattern Ids.
            - Required for I(action=add_data_selector_patterns), I(action=remove_data_selector_patterns).
        type: list
    connection_detail:
        description:
            - ""
            - Applicable only for I(action=import_connection)I(action=parse_connection)I(action=validate_connection).
        type: dict
        suboptions:
            description:
                description:
                    - A description of the connection.
                type: str
            display_name:
                description:
                    - A user-friendly display name. Does not have to be unique, and it's changeable.
                      Avoid entering confidential information.
                type: str
                aliases: ["name"]
            type_key:
                description:
                    - The key of the object type. Type key's can be found via the '/types' endpoint.
                type: str
            custom_property_members:
                description:
                    - The list of customized properties along with the values for this object
                type: list
                suboptions:
                    key:
                        description:
                            - Unique Identifier of the attribute which is ID
                        type: str
                    display_name:
                        description:
                            - Name of the custom property
                        type: str
                        aliases: ["name"]
                    value:
                        description:
                            - The custom property value
                        type: str
                    namespace_name:
                        description:
                            - Namespace name of the custom property
                        type: str
                    description:
                        description:
                            - Description of the custom property
                        type: str
                    data_type:
                        description:
                            - The data type of the custom property
                        type: str
                        choices:
                            - "TEXT"
                            - "RICH_TEXT"
                            - "BOOLEAN"
                            - "NUMBER"
                            - "DATE"
                    namespace_key:
                        description:
                            - Unique namespace key that is immutable
                        type: str
                    is_multi_valued:
                        description:
                            - If this field allows multiple values to be set
                        type: bool
                    is_hidden:
                        description:
                            - If this field is a hidden field
                        type: bool
                    is_editable:
                        description:
                            - If this field is a editable field
                        type: bool
                    is_shown_in_list:
                        description:
                            - If this field is displayed in a list view of applicable objects.
                        type: bool
                    is_event_enabled:
                        description:
                            - If an OCI Event will be emitted when the custom property is modified.
                        type: bool
                    is_list_type:
                        description:
                            - Is this property allowed to have list of values
                        type: bool
                    allowed_values:
                        description:
                            - Allowed values for the custom property if any
                        type: list
            properties:
                description:
                    - "A map of maps that contains the properties which are specific to the connection type. Each connection type
                      definition defines it's set of required and optional properties. The map keys are category names and the
                      values are maps of property name to property value. Every property is contained inside of a category. Most
                      connections have required properties within the \\"default\\" category. To determine the set of optional and
                      required properties for a connection type, a query can be done on '/types?type=connection' that returns a
                      collection of all connection types. The appropriate connection type, which will include definitions of all
                      of it's properties, can be identified from this collection.
                      Example: `{\\"properties\\": { \\"default\\": { \\"username\\": \\"user1\\"}}}`"
                type: dict
            enc_properties:
                description:
                    - "A map of maps that contains the encrypted values for sensitive properties which are specific to the
                      connection type. Each connection type definition defines it's set of required and optional properties.
                      The map keys are category names and the values are maps of property name to property value. Every property is
                      contained inside of a category. Most connections have required properties within the \\"default\\" category.
                      To determine the set of optional and required properties for a connection type, a query can be done
                      on '/types?type=connection' that returns a collection of all connection types. The appropriate connection
                      type, which will include definitions of all of it's properties, can be identified from this collection.
                      Example: `{\\"encProperties\\": { \\"default\\": { \\"password\\": \\"example-password\\"}}}`"
                type: dict
            is_default:
                description:
                    - Indicates whether this connection is the default connection. The first connection of a data asset defaults
                      to being the default, subsequent connections default to not being the default. If a default connection already
                      exists, then trying to create a connection as the default will fail. In this case the default connection would
                      need to be updated not to be the default and then the new connection can then be created as the default.
                type: bool
            key:
                description:
                    - Unique connection key that is immutable.
                type: str
            time_created:
                description:
                    - "The date and time the connection was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                      Example: `2019-03-25T21:10:29.600Z`"
                type: str
            time_updated:
                description:
                    - The last time that any change was made to the connection. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
                type: str
            created_by_id:
                description:
                    - OCID of the user who created the connection.
                type: str
            updated_by_id:
                description:
                    - OCID of the user who modified the connection.
                type: str
            external_key:
                description:
                    - Unique external key of this object from the source system.
                type: str
            time_status_updated:
                description:
                    - Time that the connections status was last updated. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
                type: str
            lifecycle_state:
                description:
                    - The current state of the connection.
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
            data_asset_key:
                description:
                    - Unique key of the parent data asset.
                type: str
            uri:
                description:
                    - URI to the connection instance in the API.
                type: str
    connection_payload:
        description:
            - The information used to import the connection.
            - Required for I(action=import_connection).
        type: str
    import_file_contents:
        description:
            - The file contents to be imported. File size not to exceed 10 MB.
            - Required for I(action=import_data_asset).
        type: str
    import_type:
        description:
            - Type of import.
            - Required for I(action=import_data_asset).
        type: list
        choices:
            - "CUSTOM_PROPERTY_VALUES"
            - "ALL"
    is_missing_value_ignored:
        description:
            - Specify whether to ignore the missing values in the import file.
            - Applicable only for I(action=import_data_asset).
        type: bool
    connection_key:
        description:
            - Unique connection key.
            - Applicable only for I(action=parse_connection).
        type: str
    export_scope:
        description:
            - Array of objects and their child types to be selected for export.
            - Applicable only for I(action=synchronous_export).
        type: list
        suboptions:
            object_key:
                description:
                    - Unique key of the object selected for export.
                type: str
            export_type_ids:
                description:
                    - Array of type keys selected for export.
                type: list
    export_type:
        description:
            - Type of export.
            - Required for I(action=synchronous_export).
        type: list
        choices:
            - "CUSTOM_PROPERTY_VALUES"
            - "ALL"
    action:
        description:
            - The action to perform on the DataAsset.
        type: str
        required: true
        choices:
            - "add_data_selector_patterns"
            - "import_connection"
            - "import_data_asset"
            - "parse_connection"
            - "remove_data_selector_patterns"
            - "synchronous_export"
            - "validate_connection"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_data_selector_patterns on data_asset
  oci_data_catalog_data_asset_actions:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    action: add_data_selector_patterns

- name: Perform action import_connection on data_asset
  oci_data_catalog_data_asset_actions:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    action: import_connection

- name: Perform action import_data_asset on data_asset
  oci_data_catalog_data_asset_actions:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    action: import_data_asset

- name: Perform action parse_connection on data_asset
  oci_data_catalog_data_asset_actions:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    action: parse_connection

- name: Perform action remove_data_selector_patterns on data_asset
  oci_data_catalog_data_asset_actions:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    action: remove_data_selector_patterns

- name: Perform action synchronous_export on data_asset
  oci_data_catalog_data_asset_actions:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    action: synchronous_export

- name: Perform action validate_connection on data_asset
  oci_data_catalog_data_asset_actions:
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    action: validate_connection

"""

RETURN = """
data_asset:
    description:
        - Details of the DataAsset resource acted upon by the current operation
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
                - A user-friendly display name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        description:
            description:
                - Detailed description of the data asset.
            returned: on success
            type: string
            sample: description_example
        catalog_id:
            description:
                - The data catalog's OCID.
            returned: on success
            type: string
            sample: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
        external_key:
            description:
                - External URI that can be used to reference the object. Format will differ based on the type of object.
            returned: on success
            type: string
            sample: external_key_example
        type_key:
            description:
                - The key of the object type. Type key's can be found via the '/types' endpoint.
            returned: on success
            type: string
            sample: type_key_example
        lifecycle_state:
            description:
                - The current state of the data asset.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - "The date and time the data asset was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2019-03-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-03-25T21:10:29.600Z
        time_updated:
            description:
                - The last time that any change was made to the data asset. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_harvested:
            description:
                - The last time that a harvest was performed on the data asset. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        created_by_id:
            description:
                - OCID of the user who created the data asset.
            returned: on success
            type: string
            sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_id:
            description:
                - OCID of the user who last modified the data asset.
            returned: on success
            type: string
            sample: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
        uri:
            description:
                - URI to the data asset instance in the API.
            returned: on success
            type: string
            sample: uri_example
        custom_property_members:
            description:
                - The list of customized properties along with the values for this object
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique Identifier of the attribute which is ID
                    returned: on success
                    type: string
                    sample: key_example
                display_name:
                    description:
                        - Display name of the custom property
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - Description of the custom property
                    returned: on success
                    type: string
                    sample: description_example
                value:
                    description:
                        - The custom property value
                    returned: on success
                    type: string
                    sample: value_example
                data_type:
                    description:
                        - The data type of the custom property
                    returned: on success
                    type: string
                    sample: TEXT
                namespace_name:
                    description:
                        - Namespace name of the custom property
                    returned: on success
                    type: string
                    sample: namespace_name_example
                namespace_key:
                    description:
                        - Unique namespace key that is immutable
                    returned: on success
                    type: string
                    sample: namespace_key_example
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
                is_event_enabled:
                    description:
                        - If an OCI Event will be emitted when the custom property is modified.
                    returned: on success
                    type: bool
                    sample: true
                is_list_type:
                    description:
                        - Is this property allowed to have list of values
                    returned: on success
                    type: bool
                    sample: true
                allowed_values:
                    description:
                        - Allowed values for the custom property if any
                    returned: on success
                    type: list
                    sample: []
        data_selector_patterns:
            description:
                - The list of data selector patterns used in the harvest for this data asset to derive logical entities.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique pattern key that is immutable.
                    returned: on success
                    type: string
                    sample: key_example
                display_name:
                    description:
                        - A user-friendly display name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                    returned: on success
                    type: string
                    sample: display_name_example
                description:
                    description:
                        - Detailed description of the pattern.
                    returned: on success
                    type: string
                    sample: description_example
                catalog_id:
                    description:
                        - The data catalog's OCID.
                    returned: on success
                    type: string
                    sample: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
                time_created:
                    description:
                        - "The date and time the pattern was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2019-03-25T21:10:29.600Z`"
                    returned: on success
                    type: string
                    sample: 2019-03-25T21:10:29.600Z
                expression:
                    description:
                        - The expression used in the pattern that may include qualifiers.
                    returned: on success
                    type: string
                    sample: expression_example
                lifecycle_state:
                    description:
                        - State of the pattern.
                    returned: on success
                    type: string
                    sample: CREATING
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
    sample: {
        "key": "key_example",
        "display_name": "display_name_example",
        "description": "description_example",
        "catalog_id": "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx",
        "external_key": "external_key_example",
        "type_key": "type_key_example",
        "lifecycle_state": "CREATING",
        "time_created": "2019-03-25T21:10:29.600Z",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_harvested": "2013-10-20T19:20:30+01:00",
        "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
        "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx",
        "uri": "uri_example",
        "custom_property_members": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "description": "description_example",
            "value": "value_example",
            "data_type": "TEXT",
            "namespace_name": "namespace_name_example",
            "namespace_key": "namespace_key_example",
            "is_multi_valued": true,
            "is_hidden": true,
            "is_editable": true,
            "is_shown_in_list": true,
            "is_event_enabled": true,
            "is_list_type": true,
            "allowed_values": []
        }],
        "data_selector_patterns": [{
            "key": "key_example",
            "display_name": "display_name_example",
            "description": "description_example",
            "catalog_id": "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx",
            "time_created": "2019-03-25T21:10:29.600Z",
            "expression": "expression_example",
            "lifecycle_state": "CREATING"
        }],
        "properties": {}
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
    from oci.data_catalog import DataCatalogClient
    from oci.data_catalog.models import DataSelectorPatternDetails
    from oci.data_catalog.models import ImportConnectionDetails
    from oci.data_catalog.models import ImportDataAssetDetails
    from oci.data_catalog.models import ParseConnectionDetails
    from oci.data_catalog.models import ExportDataAssetDetails
    from oci.data_catalog.models import ValidateConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogDataAssetActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_data_selector_patterns
        import_connection
        import_data_asset
        parse_connection
        remove_data_selector_patterns
        synchronous_export
        validate_connection
    """

    @staticmethod
    def get_module_resource_id_param():
        return "data_asset_key"

    def get_module_resource_id(self):
        return self.module.params.get("data_asset_key")

    def get_get_fn(self):
        return self.client.get_data_asset

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_data_asset,
            catalog_id=self.module.params.get("catalog_id"),
            data_asset_key=self.module.params.get("data_asset_key"),
        )

    def add_data_selector_patterns(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DataSelectorPatternDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_data_selector_patterns,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                data_selector_pattern_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def import_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                import_connection_details=action_details,
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

    def import_data_asset(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ImportDataAssetDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.import_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                import_data_asset_details=action_details,
                import_type=self.module.params.get("import_type"),
                is_missing_value_ignored=self.module.params.get(
                    "is_missing_value_ignored"
                ),
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

    def parse_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ParseConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.parse_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                parse_connection_details=action_details,
                connection_key=self.module.params.get("connection_key"),
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

    def remove_data_selector_patterns(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DataSelectorPatternDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_data_selector_patterns,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                data_selector_pattern_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def synchronous_export(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ExportDataAssetDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.synchronous_export_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                synchronous_export_data_asset_details=action_details,
                export_type=self.module.params.get("export_type"),
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

    def validate_connection(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ValidateConnectionDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.validate_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                validate_connection_details=action_details,
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


DataCatalogDataAssetActionsHelperCustom = get_custom_class(
    "DataCatalogDataAssetActionsHelperCustom"
)


class ResourceHelper(
    DataCatalogDataAssetActionsHelperCustom, DataCatalogDataAssetActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            catalog_id=dict(type="str", required=True),
            data_asset_key=dict(type="str", required=True),
            items=dict(type="list"),
            connection_detail=dict(
                type="dict",
                options=dict(
                    description=dict(type="str"),
                    display_name=dict(aliases=["name"], type="str"),
                    type_key=dict(type="str"),
                    custom_property_members=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            key=dict(type="str"),
                            display_name=dict(aliases=["name"], type="str"),
                            value=dict(type="str"),
                            namespace_name=dict(type="str"),
                            description=dict(type="str"),
                            data_type=dict(
                                type="str",
                                choices=[
                                    "TEXT",
                                    "RICH_TEXT",
                                    "BOOLEAN",
                                    "NUMBER",
                                    "DATE",
                                ],
                            ),
                            namespace_key=dict(type="str"),
                            is_multi_valued=dict(type="bool"),
                            is_hidden=dict(type="bool"),
                            is_editable=dict(type="bool"),
                            is_shown_in_list=dict(type="bool"),
                            is_event_enabled=dict(type="bool"),
                            is_list_type=dict(type="bool"),
                            allowed_values=dict(type="list"),
                        ),
                    ),
                    properties=dict(type="dict"),
                    enc_properties=dict(type="dict"),
                    is_default=dict(type="bool"),
                    key=dict(type="str"),
                    time_created=dict(type="str"),
                    time_updated=dict(type="str"),
                    created_by_id=dict(type="str"),
                    updated_by_id=dict(type="str"),
                    external_key=dict(type="str"),
                    time_status_updated=dict(type="str"),
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
                    data_asset_key=dict(type="str"),
                    uri=dict(type="str"),
                ),
            ),
            connection_payload=dict(type="str"),
            import_file_contents=dict(type="str"),
            import_type=dict(type="list", choices=["CUSTOM_PROPERTY_VALUES", "ALL"]),
            is_missing_value_ignored=dict(type="bool"),
            connection_key=dict(type="str"),
            export_scope=dict(
                type="list",
                elements="dict",
                options=dict(
                    object_key=dict(type="str"), export_type_ids=dict(type="list")
                ),
            ),
            export_type=dict(type="list", choices=["CUSTOM_PROPERTY_VALUES", "ALL"]),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_data_selector_patterns",
                    "import_connection",
                    "import_data_asset",
                    "parse_connection",
                    "remove_data_selector_patterns",
                    "synchronous_export",
                    "validate_connection",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="data_asset",
        service_client_class=DataCatalogClient,
        namespace="data_catalog",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
