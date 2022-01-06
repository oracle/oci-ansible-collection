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
module: oci_data_catalog_custom_property
short_description: Manage a CustomProperty resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a CustomProperty resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new Custom Property
version_added: "2.9.0"
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
            - Detailed description of the custom property.
            - This parameter is updatable.
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
    is_sortable:
        description:
            - If this field allows to sort from UI
            - This parameter is updatable.
        type: bool
    is_filterable:
        description:
            - If this field allows to filter or create facets from UI
            - This parameter is updatable.
        type: bool
    is_multi_valued:
        description:
            - If this field allows multiple values to be set
            - This parameter is updatable.
        type: bool
    is_hidden:
        description:
            - If this field is a hidden field
            - This parameter is updatable.
        type: bool
    is_editable:
        description:
            - If this field is a editable field
            - This parameter is updatable.
        type: bool
    is_shown_in_list:
        description:
            - If this field is displayed in a list view of applicable objects.
            - This parameter is updatable.
        type: bool
    is_hidden_in_search:
        description:
            - If this field is allowed to pop in search results
            - This parameter is updatable.
        type: bool
    is_event_enabled:
        description:
            - If an OCI Event will be emitted when the custom property is modified.
            - This parameter is updatable.
        type: bool
    allowed_values:
        description:
            - Allowed values for the custom property if any
            - This parameter is updatable.
        type: list
        elements: str
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
    custom_property_key:
        description:
            - Unique Custom Property key
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
    state:
        description:
            - The state of the CustomProperty.
            - Use I(state=present) to create or update a CustomProperty.
            - Use I(state=absent) to delete a CustomProperty.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create custom_property
  oci_data_catalog_custom_property:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    data_type: TEXT
    is_sortable: true
    is_filterable: true
    is_multi_valued: true
    is_hidden: true
    is_editable: true
    is_shown_in_list: true
    is_hidden_in_search: true
    is_event_enabled: true
    allowed_values: [ "allowed_values_example" ]
    properties: null

- name: Update custom_property
  oci_data_catalog_custom_property:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"
    custom_property_key: custom_property_key_example

    # optional
    display_name: display_name_example
    description: description_example
    is_sortable: true
    is_filterable: true
    is_multi_valued: true
    is_hidden: true
    is_editable: true
    is_shown_in_list: true
    is_hidden_in_search: true
    is_event_enabled: true
    allowed_values: [ "allowed_values_example" ]
    properties: null

- name: Update custom_property using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_catalog_custom_property:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    description: description_example
    is_sortable: true
    is_filterable: true
    is_multi_valued: true
    is_hidden: true
    is_editable: true
    is_shown_in_list: true
    is_hidden_in_search: true
    is_event_enabled: true
    allowed_values: [ "allowed_values_example" ]
    properties: null

- name: Delete custom_property
  oci_data_catalog_custom_property:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"
    custom_property_key: custom_property_key_example
    state: absent

- name: Delete custom_property using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_catalog_custom_property:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
custom_property:
    description:
        - Details of the CustomProperty resource acted upon by the current operation
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
                - Display name of the custom property
            returned: on success
            type: str
            sample: display_name_example
        data_type:
            description:
                - Data type of the custom property
            returned: on success
            type: str
            sample: TEXT
        description:
            description:
                - Description for the custom property
            returned: on success
            type: str
            sample: description_example
        namespace_name:
            description:
                - Namespace name of the custom property
            returned: on success
            type: str
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
            type: str
            sample: CREATING
        time_created:
            description:
                - "The date and time the custom property was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2019-03-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The last time that any change was made to the custom property. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by_id:
            description:
                - OCID of the user who created the custom property.
            returned: on success
            type: str
            sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_id:
            description:
                - OCID of the user who last modified the custom property.
            returned: on success
            type: str
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
                    type: str
                    sample: "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx"
                type_name:
                    description:
                        - Name of the type associated with
                    returned: on success
                    type: str
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
                    type: str
                    sample: "ocid1.type.oc1..xxxxxxEXAMPLExxxxxx"
                type_name:
                    description:
                        - Name of the type.
                    returned: on success
                    type: str
                    sample: type_name_example
                property_id:
                    description:
                        - Unique property key identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.property.oc1..xxxxxxEXAMPLExxxxxx"
                property_name:
                    description:
                        - Name of the property.
                    returned: on success
                    type: str
                    sample: property_name_example
                event_config_status:
                    description:
                        - Status of the configuration.
                    returned: on success
                    type: str
                    sample: ENABLED
                time_created:
                    description:
                        - "The date and time the event was configured, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                          Example: `2019-03-25T21:10:29.600Z`"
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The last time that any change was made to the configuration. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime
                          string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                created_by_id:
                    description:
                        - OCID of the user who created the configuration.
                    returned: on success
                    type: str
                    sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
                updated_by_id:
                    description:
                        - OCID of the user who last modified the configuration.
                    returned: on success
                    type: str
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
    sample: {
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
        "time_created": "2013-10-20T19:20:30+01:00",
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
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
            "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.data_catalog.models import CreateCustomPropertyDetails
    from oci.data_catalog.models import UpdateCustomPropertyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogCustomPropertyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "custom_property_key"

    def get_module_resource_id(self):
        return self.module.params.get("custom_property_key")

    def get_get_fn(self):
        return self.client.get_custom_property

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_custom_property,
            catalog_id=self.module.params.get("catalog_id"),
            namespace_id=self.module.params.get("namespace_id"),
            custom_property_key=self.module.params.get("custom_property_key"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "catalog_id",
            "namespace_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
            self.client.list_custom_properties, **kwargs
        )

    def get_create_model_class(self):
        return CreateCustomPropertyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_custom_property,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                namespace_id=self.module.params.get("namespace_id"),
                create_custom_property_details=create_details,
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
        return UpdateCustomPropertyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_custom_property,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                namespace_id=self.module.params.get("namespace_id"),
                custom_property_key=self.module.params.get("custom_property_key"),
                update_custom_property_details=update_details,
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
            call_fn=self.client.delete_custom_property,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                namespace_id=self.module.params.get("namespace_id"),
                custom_property_key=self.module.params.get("custom_property_key"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataCatalogCustomPropertyHelperCustom = get_custom_class(
    "DataCatalogCustomPropertyHelperCustom"
)


class ResourceHelper(
    DataCatalogCustomPropertyHelperCustom, DataCatalogCustomPropertyHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            catalog_id=dict(type="str", required=True),
            namespace_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            data_type=dict(
                type="str", choices=["TEXT", "RICH_TEXT", "BOOLEAN", "NUMBER", "DATE"]
            ),
            is_sortable=dict(type="bool"),
            is_filterable=dict(type="bool"),
            is_multi_valued=dict(type="bool"),
            is_hidden=dict(type="bool"),
            is_editable=dict(type="bool"),
            is_shown_in_list=dict(type="bool"),
            is_hidden_in_search=dict(type="bool"),
            is_event_enabled=dict(type="bool"),
            allowed_values=dict(type="list", elements="str"),
            properties=dict(type="dict"),
            custom_property_key=dict(type="str", no_log=True),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="custom_property",
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
