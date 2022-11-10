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
module: oci_nosql_index
short_description: Manage an Index resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete an Index resource in Oracle Cloud Infrastructure
    - For I(state=present), create a new index on the table identified by tableNameOrId.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    keys:
        description:
            - A set of keys for a secondary index.
            - Required for create using I(state=present).
        type: list
        elements: dict
        suboptions:
            column_name:
                description:
                    - The name of a column to be included as an index key.
                type: str
                required: true
            json_path:
                description:
                    - If the specified column is of type JSON, jsonPath contains
                      a dotted path indicating the field within the JSON object
                      that will be the index key.
                type: str
            json_field_type:
                description:
                    - If the specified column is of type JSON, jsonFieldType contains
                      the type of the field indicated by jsonPath.
                type: str
    is_if_not_exists:
        description:
            - If true, the operation completes successfully even when the
              index exists.  Otherwise, an attempt to create an index
              that already exists will return an error.
        type: bool
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
        type: str
        required: true
    name:
        description:
            - Index name.
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the table's compartment.  Required
              if the tableNameOrId path parameter is a table name.
              Optional if tableNameOrId is an OCID.  If tableNameOrId
              is an OCID, and compartmentId is supplied, the latter
              must match the identified table's compartmentId.
        type: str
    is_if_exists:
        description:
            - "Set as true to select \\"if exists\\" behavior."
        type: bool
    state:
        description:
            - The state of the Index.
            - Use I(state=present) to create an Index.
            - Use I(state=absent) to delete an Index.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create index
  oci_nosql_index:
    # required
    keys:
    - # required
      column_name: column_name_example

      # optional
      json_path: json_path_example
      json_field_type: json_field_type_example
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    is_if_not_exists: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete index
  oci_nosql_index:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    state: absent

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_if_exists: true

"""

RETURN = """
index:
    description:
        - Details of the Index resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Index name.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        table_name:
            description:
                - The name of the table to which this index belongs.
            returned: on success
            type: str
            sample: table_name_example
        table_id:
            description:
                - the OCID of the table to which this index belongs.
            returned: on success
            type: str
            sample: "ocid1.table.oc1..xxxxxxEXAMPLExxxxxx"
        keys:
            description:
                - A set of keys for a secondary index.
            returned: on success
            type: complex
            contains:
                column_name:
                    description:
                        - The name of a column to be included as an index key.
                    returned: on success
                    type: str
                    sample: column_name_example
                json_path:
                    description:
                        - If the specified column is of type JSON, jsonPath contains
                          a dotted path indicating the field within the JSON object
                          that will be the index key.
                    returned: on success
                    type: str
                    sample: json_path_example
                json_field_type:
                    description:
                        - If the specified column is of type JSON, jsonFieldType contains
                          the type of the field indicated by jsonPath.
                    returned: on success
                    type: str
                    sample: json_field_type_example
        lifecycle_state:
            description:
                - The state of an index.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: {
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "table_name": "table_name_example",
        "table_id": "ocid1.table.oc1..xxxxxxEXAMPLExxxxxx",
        "keys": [{
            "column_name": "column_name_example",
            "json_path": "json_path_example",
            "json_field_type": "json_field_type_example"
        }],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
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
    from oci.nosql import NosqlClient
    from oci.nosql.models import CreateIndexDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IndexHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(IndexHelperGen, self).get_possible_entity_types() + [
            "index",
            "indexes",
            "nosqlindex",
            "nosqlindexes",
            "indexresource",
            "indexesresource",
            "nosql",
        ]

    def get_module_resource_id_param(self):
        return "name"

    def get_module_resource_id(self):
        return self.module.params.get("name")

    def get_get_fn(self):
        return self.client.get_index

    def get_resource(self):
        optional_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_index,
            table_name_or_id=self.module.params.get("table_name_or_id"),
            index_name=self.module.params.get("name"),
            **optional_kwargs
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "table_name_or_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "name"]

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
        return oci_common_utils.list_all_resources(self.client.list_indexes, **kwargs)

    def get_create_model_class(self):
        return CreateIndexDetails

    def get_exclude_attributes(self):
        return ["is_if_not_exists"]

    def is_update(self):
        if not self.module.params.get("state") == "present":
            return False

        return self.does_resource_exist()

    def is_create(self):
        if not self.module.params.get("state") == "present":
            return False

        return not self.does_resource_exist()

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_index,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                create_index_details=create_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_index,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                index_name=self.module.params.get("name"),
                compartment_id=self.module.params.get("compartment_id"),
                is_if_exists=self.module.params.get("is_if_exists"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


IndexHelperCustom = get_custom_class("IndexHelperCustom")


class ResourceHelper(IndexHelperCustom, IndexHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            keys=dict(
                type="list",
                elements="dict",
                no_log=False,
                options=dict(
                    column_name=dict(type="str", required=True),
                    json_path=dict(type="str"),
                    json_field_type=dict(type="str"),
                ),
            ),
            is_if_not_exists=dict(type="bool"),
            table_name_or_id=dict(type="str", required=True),
            name=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            is_if_exists=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="index",
        service_client_class=NosqlClient,
        namespace="nosql",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
