#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_data_catalog_connection
short_description: Manage a Connection resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Connection resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new connection.
    - "This resource has the following action operations in the M(oci_connection_actions) module: test."
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
    description:
        description:
            - A description of the connection.
            - This parameter is updatable.
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
    type_key:
        description:
            - The key of the object type. Type key's can be found via the '/types' endpoint.
            - Required for create using I(state=present).
        type: str
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
            - Required for create using I(state=present).
            - This parameter is updatable.
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
              Example: `{\\"encProperties\\": { \\"default\\": { \\"password\\": \\"pwd\\"}}}`"
            - This parameter is updatable.
        type: dict
    is_default:
        description:
            - Indicates whether this connection is the default connection. The first connection of a data asset defaults
              to being the default, subsequent connections default to not being the default. If a default connection already
              exists, then trying to create a connection as the default will fail. In this case the default connection would
              need to be updated not to be the default and then the new connection can then be created as the default.
            - This parameter is updatable.
        type: bool
    connection_key:
        description:
            - Unique connection key.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create connection
  oci_data_catalog_connection:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
    data_asset_key: data_asset_key_example
    display_name: display_name_example
    type_key: type_key_example

- name: Update connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_catalog_connection:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
    data_asset_key: data_asset_key_example
    description: description_example
    display_name: display_name_example
    is_default: true

- name: Update connection
  oci_data_catalog_connection:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
    data_asset_key: data_asset_key_example
    connection_key: connection_key_example

- name: Delete connection
  oci_data_catalog_connection:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
    data_asset_key: data_asset_key_example
    connection_key: connection_key_example
    state: absent

- name: Delete connection using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_catalog_connection:
    catalog_id: ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx
    data_asset_key: data_asset_key_example
    display_name: display_name_example
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
                - Unique connection key that is immutable.
            returned: on success
            type: string
            sample: key_example
        description:
            description:
                - A description of the connection.
            returned: on success
            type: string
            sample: description_example
        display_name:
            description:
                - A user-friendly display name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        time_created:
            description:
                - "The date and time the connection was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2019-03-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2019-03-25T21:10:29.600Z
        time_updated:
            description:
                - The last time that any change was made to the connection. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        created_by_id:
            description:
                - OCID of the user who created the connection.
            returned: on success
            type: string
            sample: ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx
        updated_by_id:
            description:
                - OCID of the user who modified the connection.
            returned: on success
            type: string
            sample: ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx
        properties:
            description:
                - "A map of maps that contains the properties which are specific to the connection type. Each connection type
                  definition defines it's set of required and optional properties. The map keys are category names and the
                  values are maps of property name to property value. Every property is contained inside of a category. Most
                  connections have required properties within the \\"default\\" category.
                  Example: `{\\"properties\\": { \\"default\\": { \\"username\\": \\"user1\\"}}}`"
            returned: on success
            type: dict
            sample: {}
        external_key:
            description:
                - Unique external key of this object from the source system.
            returned: on success
            type: string
            sample: external_key_example
        time_status_updated:
            description:
                - Time that the connections status was last updated. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the connection.
            returned: on success
            type: string
            sample: CREATING
        is_default:
            description:
                - Indicates whether this connection is the default connection.
            returned: on success
            type: bool
            sample: true
        data_asset_key:
            description:
                - Unique key of the parent data asset.
            returned: on success
            type: string
            sample: data_asset_key_example
        type_key:
            description:
                - The key of the object type. Type key's can be found via the '/types' endpoint.
            returned: on success
            type: string
            sample: type_key_example
        uri:
            description:
                - URI to the connection instance in the API.
            returned: on success
            type: string
            sample: uri_example
    sample: {
        "key": "key_example",
        "description": "description_example",
        "display_name": "display_name_example",
        "time_created": "2019-03-25T21:10:29.600Z",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
        "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx",
        "properties": {},
        "external_key": "external_key_example",
        "time_status_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "is_default": true,
        "data_asset_key": "data_asset_key_example",
        "type_key": "type_key_example",
        "uri": "uri_example"
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
    from oci.data_catalog.models import CreateConnectionDetails
    from oci.data_catalog.models import UpdateConnectionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogConnectionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "connection_key"

    def get_module_resource_id(self):
        return self.module.params.get("connection_key")

    def get_get_fn(self):
        return self.client.get_connection

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_connection,
            catalog_id=self.module.params.get("catalog_id"),
            data_asset_key=self.module.params.get("data_asset_key"),
            connection_key=self.module.params.get("connection_key"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "catalog_id",
            "data_asset_key",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name"]
            if self._use_name_as_identifier()
            else ["display_name", "is_default"]
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
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                create_connection_details=create_details,
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
        return UpdateConnectionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
                connection_key=self.module.params.get("connection_key"),
                update_connection_details=update_details,
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
            call_fn=self.client.delete_connection,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                data_asset_key=self.module.params.get("data_asset_key"),
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


DataCatalogConnectionHelperCustom = get_custom_class(
    "DataCatalogConnectionHelperCustom"
)


class ResourceHelper(DataCatalogConnectionHelperCustom, DataCatalogConnectionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            catalog_id=dict(type="str", required=True),
            data_asset_key=dict(type="str", required=True),
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            type_key=dict(type="str"),
            properties=dict(type="dict"),
            enc_properties=dict(type="dict"),
            is_default=dict(type="bool"),
            connection_key=dict(type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="connection",
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
