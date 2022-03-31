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
module: oci_data_catalog_data_asset
short_description: Manage a DataAsset resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DataAsset resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new data asset.
    - "This resource has the following action operations in the M(oracle.oci.oci_data_catalog_data_asset_actions) module: add_data_selector_patterns,
      import_connection, import_data_asset, parse_connection, remove_data_selector_patterns, synchronous_export, validate_connection."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    type_key:
        description:
            - The key of the data asset type. This can be obtained via the '/types' endpoint.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - A user-friendly display name. Does not have to be unique, and it's changeable.
              Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Detailed description of the data asset.
            - This parameter is updatable.
        type: str
    custom_property_members:
        description:
            - The list of customized properties along with the values for this object
            - This parameter is updatable.
        type: list
        elements: dict
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
    properties:
        description:
            - "A map of maps that contains the properties which are specific to the data asset type. Each data asset type
              definition defines it's set of required and optional properties. The map keys are category names and the
              values are maps of property name to property value. Every property is contained inside of a category. Most
              data assets have required properties within the \\"default\\" category. To determine the set of optional and
              required properties for a data asset type, a query can be done on '/types?type=dataAsset' that returns a
              collection of all data asset types. The appropriate data asset type, which includes definitions of all of
              it's properties, can be identified from this collection.
              Example: `{\\"properties\\": { \\"default\\": { \\"host\\": \\"host1\\", \\"port\\": \\"1521\\", \\"database\\": \\"orcl\\"}}}`"
            - This parameter is updatable.
        type: dict
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        required: true
    data_asset_key:
        description:
            - Unique data asset key.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["key"]
    state:
        description:
            - The state of the DataAsset.
            - Use I(state=present) to create or update a DataAsset.
            - Use I(state=absent) to delete a DataAsset.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create data_asset
  oci_data_catalog_data_asset:
    # required
    type_key: type_key_example
    display_name: display_name_example
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    custom_property_members:
    - # optional
      key: key_example
      display_name: display_name_example
      value: value_example
      namespace_name: namespace_name_example
    properties: null

- name: Update data_asset
  oci_data_catalog_data_asset:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example

    # optional
    display_name: display_name_example
    description: description_example
    custom_property_members:
    - # optional
      key: key_example
      display_name: display_name_example
      value: value_example
      namespace_name: namespace_name_example
    properties: null

- name: Update data_asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_catalog_data_asset:
    # required
    display_name: display_name_example
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    custom_property_members:
    - # optional
      key: key_example
      display_name: display_name_example
      value: value_example
      namespace_name: namespace_name_example
    properties: null

- name: Delete data_asset
  oci_data_catalog_data_asset:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    data_asset_key: data_asset_key_example
    state: absent

- name: Delete data_asset using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_catalog_data_asset:
    # required
    display_name: display_name_example
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

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
            type: str
            sample: key_example
        display_name:
            description:
                - A user-friendly display name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Detailed description of the data asset.
            returned: on success
            type: str
            sample: description_example
        catalog_id:
            description:
                - The data catalog's OCID.
            returned: on success
            type: str
            sample: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
        external_key:
            description:
                - External URI that can be used to reference the object. Format will differ based on the type of object.
            returned: on success
            type: str
            sample: external_key_example
        type_key:
            description:
                - The key of the object type. Type key's can be found via the '/types' endpoint.
            returned: on success
            type: str
            sample: type_key_example
        lifecycle_state:
            description:
                - The current state of the data asset.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - "The date and time the data asset was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2019-03-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The last time that any change was made to the data asset. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_harvested:
            description:
                - The last time that a harvest was performed on the data asset. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by_id:
            description:
                - OCID of the user who created the data asset.
            returned: on success
            type: str
            sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_id:
            description:
                - OCID of the user who last modified the data asset.
            returned: on success
            type: str
            sample: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
        uri:
            description:
                - URI to the data asset instance in the API.
            returned: on success
            type: str
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
                    type: str
                    sample: key_example
                display_name:
                    description:
                        - Display name of the custom property
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Description of the custom property
                    returned: on success
                    type: str
                    sample: description_example
                value:
                    description:
                        - The custom property value
                    returned: on success
                    type: str
                    sample: value_example
                data_type:
                    description:
                        - The data type of the custom property
                    returned: on success
                    type: str
                    sample: TEXT
                namespace_name:
                    description:
                        - Namespace name of the custom property
                    returned: on success
                    type: str
                    sample: namespace_name_example
                namespace_key:
                    description:
                        - Unique namespace key that is immutable
                    returned: on success
                    type: str
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
                    type: str
                    sample: key_example
                display_name:
                    description:
                        - A user-friendly display name. Does not have to be unique, and it's changeable.
                          Avoid entering confidential information.
                    returned: on success
                    type: str
                    sample: display_name_example
                description:
                    description:
                        - Detailed description of the pattern.
                    returned: on success
                    type: str
                    sample: description_example
                catalog_id:
                    description:
                        - The data catalog's OCID.
                    returned: on success
                    type: str
                    sample: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
                time_created:
                    description:
                        - "The date and time the pattern was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2019-03-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                expression:
                    description:
                        - Input string which drives the selection process, allowing for fine-grained control using qualifiers.
                          Refer to the user documentation for details of the format and examples. A pattern cannot include both
                          a prefix and an expression.
                    returned: on success
                    type: str
                    sample: expression_example
                file_path_prefix:
                    description:
                        - Input string which drives the selection process.
                          Refer to the user documentation for details of the format and examples. A pattern cannot include both
                          a prefix and an expression.
                    returned: on success
                    type: str
                    sample: file_path_prefix_example
                lifecycle_state:
                    description:
                        - State of the pattern.
                    returned: on success
                    type: str
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
        "time_created": "2013-10-20T19:20:30+01:00",
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
            "time_created": "2013-10-20T19:20:30+01:00",
            "expression": "expression_example",
            "file_path_prefix": "file_path_prefix_example",
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
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.data_catalog import DataCatalogClient
    from oci.data_catalog.models import CreateDataAssetDetails
    from oci.data_catalog.models import UpdateDataAssetDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogDataAssetHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataCatalogDataAssetHelperGen, self
        ).get_possible_entity_types() + [
            "dataasset",
            "dataassets",
            "dataCatalogdataasset",
            "dataCatalogdataassets",
            "dataassetresource",
            "dataassetsresource",
            "datacatalog",
        ]

    def get_module_resource_id_param(self):
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

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "catalog_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name", "type_key"]

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
            self.client.list_data_assets, **kwargs
        )

    def get_create_model_class(self):
        return CreateDataAssetDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                create_data_asset_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateDataAssetDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                update_data_asset_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_data_asset,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataCatalogDataAssetHelperCustom = get_custom_class("DataCatalogDataAssetHelperCustom")


class ResourceHelper(DataCatalogDataAssetHelperCustom, DataCatalogDataAssetHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            type_key=dict(type="str", no_log=True),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            custom_property_members=dict(
                type="list",
                elements="dict",
                options=dict(
                    key=dict(type="str", no_log=True),
                    display_name=dict(aliases=["name"], type="str"),
                    value=dict(type="str"),
                    namespace_name=dict(type="str"),
                ),
            ),
            properties=dict(type="dict"),
            catalog_id=dict(type="str", required=True),
            data_asset_key=dict(aliases=["key"], type="str", no_log=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
