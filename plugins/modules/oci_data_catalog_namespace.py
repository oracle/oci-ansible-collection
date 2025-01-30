#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_data_catalog_namespace
short_description: Manage a Namespace resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Namespace resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new Namespace to be used by a custom property
version_added: "2.9.0"
author: Oracle (@oracle)
options:
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
            - Detailed description of the Namespace.
            - This parameter is updatable.
        type: str
    is_service_defined:
        description:
            - If this field is defined by service or by a user
            - This parameter is updatable.
        type: bool
    catalog_id:
        description:
            - Unique catalog identifier.
        type: str
        required: true
    namespace_id:
        description:
            - Unique namespace identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Namespace.
            - Use I(state=present) to create or update a Namespace.
            - Use I(state=absent) to delete a Namespace.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create namespace
  oci_data_catalog_namespace:
    # required
    display_name: display_name_example
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    is_service_defined: true

- name: Update namespace
  oci_data_catalog_namespace:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    description: description_example
    is_service_defined: true

- name: Update namespace using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_catalog_namespace:
    # required
    display_name: display_name_example
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    is_service_defined: true

- name: Delete namespace
  oci_data_catalog_namespace:
    # required
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_id: "ocid1.namespace.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete namespace using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_data_catalog_namespace:
    # required
    display_name: display_name_example
    catalog_id: "ocid1.catalog.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
namespace:
    description:
        - Details of the Namespace resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        key:
            description:
                - Unique namespace key that is immutable.
            returned: on success
            type: str
            sample: key_example
        display_name:
            description:
                - Name of the Namespace
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description for the namespace
            returned: on success
            type: str
            sample: description_example
        is_service_defined:
            description:
                - If this field is defined by service or by a user
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of the namespace.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - "The date and time the namespace was created, in the format defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
                  Example: `2019-03-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The last time that any change was made to the namespace. An L(RFC3339,https://tools.ietf.org/html/rfc3339) formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by_id:
            description:
                - OCID of the user who created the namespace.
            returned: on success
            type: str
            sample: "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx"
        updated_by_id:
            description:
                - OCID of the user who last modified the namespace.
            returned: on success
            type: str
            sample: "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "key": "key_example",
        "display_name": "display_name_example",
        "description": "description_example",
        "is_service_defined": true,
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "created_by_id": "ocid1.createdby.oc1..xxxxxxEXAMPLExxxxxx",
        "updated_by_id": "ocid1.updatedby.oc1..xxxxxxEXAMPLExxxxxx"
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
    from oci.data_catalog import DataCatalogClient
    from oci.data_catalog.models import CreateNamespaceDetails
    from oci.data_catalog.models import UpdateNamespaceDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DataCatalogNamespaceHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            DataCatalogNamespaceHelperGen, self
        ).get_possible_entity_types() + [
            "namespace",
            "namespaces",
            "dataCatalognamespace",
            "dataCatalognamespaces",
            "namespaceresource",
            "namespacesresource",
            "datacatalog",
        ]

    def get_module_resource_id_param(self):
        return "namespace_id"

    def get_module_resource_id(self):
        return self.module.params.get("namespace_id")

    def get_get_fn(self):
        return self.client.get_namespace

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_namespace,
            catalog_id=self.module.params.get("catalog_id"),
            namespace_id=self.module.params.get("namespace_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "catalog_id",
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
            self.client.list_namespaces, **kwargs
        )

    def get_create_model_class(self):
        return CreateNamespaceDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                create_namespace_details=create_details,
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
        return UpdateNamespaceDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                namespace_id=self.module.params.get("namespace_id"),
                update_namespace_details=update_details,
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
            call_fn=self.client.delete_namespace,
            call_fn_args=(),
            call_fn_kwargs=dict(
                catalog_id=self.module.params.get("catalog_id"),
                namespace_id=self.module.params.get("namespace_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


DataCatalogNamespaceHelperCustom = get_custom_class("DataCatalogNamespaceHelperCustom")


class ResourceHelper(DataCatalogNamespaceHelperCustom, DataCatalogNamespaceHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            is_service_defined=dict(type="bool"),
            catalog_id=dict(type="str", required=True),
            namespace_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="namespace",
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
