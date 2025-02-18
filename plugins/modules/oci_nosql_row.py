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
module: oci_nosql_row
short_description: Manage a Row resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update and delete a Row resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    value:
        description:
            - The map of values from a row.
            - Required for update using I(state=present) with table_name_or_id present.
        type: dict
    option:
        description:
            - Specifies a condition for the put operation.
            - This parameter is updatable.
        type: str
        choices:
            - "IF_ABSENT"
            - "IF_PRESENT"
    ttl:
        description:
            - Time-to-live for the row, in days.
            - This parameter is updatable.
        type: int
    is_ttl_use_table_default:
        description:
            - If true, set time-to-live for this row to the table's default.
            - This parameter is updatable.
        type: bool
    identity_cache_size:
        description:
            - Sets the number of generated identity values that are
              requested from the server during a put. If present and greater than 0,
              this value takes precedence over a default value for the table.
            - This parameter is updatable.
        type: int
    is_exact_match:
        description:
            - If present and true, the presented row value must exactly
              match the table's schema.  Otherwise, rows with missing
              non-key fields or extra fields can be written successfully.
            - This parameter is updatable.
        type: bool
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
        type: str
        aliases: ["id"]
        required: true
    key:
        description:
            - "An array of strings, each of the format \\"column-name:value\\",
              representing the primary key of the row."
            - Required for delete using I(state=absent).
        type: list
        elements: str
    compartment_id:
        description:
            - The OCID of the table's compartment.  Required
              if the tableNameOrId path parameter is a table name.
              Optional if tableNameOrId is an OCID.  If tableNameOrId
              is an OCID, and compartmentId is supplied, the latter
              must match the identified table's compartmentId.
            - This parameter is updatable.
        type: str
    is_get_return_row:
        description:
            - If true, and the put fails due to an option setting, then
              the existing row will be returned.
            - This parameter is updatable.
        type: bool
    timeout_in_ms:
        description:
            - Timeout setting for the put.
            - This parameter is updatable.
        type: int
    state:
        description:
            - The state of the Row.
            - Use I(state=present) to update an existing a Row.
            - Use I(state=absent) to delete a Row.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update row
  oci_nosql_row:
    # required
    value: null
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    option: IF_ABSENT
    ttl: 56
    is_ttl_use_table_default: true
    identity_cache_size: 56
    is_exact_match: true
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_get_return_row: true
    timeout_in_ms: 56

- name: Delete row
  oci_nosql_row:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    key: [ "key_example" ]
    state: absent

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    is_get_return_row: true
    timeout_in_ms: 56

"""

RETURN = """
row:
    description:
        - Details of the Row resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        version:
            description:
                - An opaque version string associated with the row.
            returned: on success
            type: str
            sample: version_example
        generated_value:
            description:
                - The value generated if the operation created a new value for
                  an identity column. If the table has no identity column, this value
                  is null. If it has an identity column, and a value was generated for
                  that column, it is non-null.
            returned: on success
            type: str
            sample: generated_value_example
        is_success:
            description:
                - Convey the success or failure of the operation.
            returned: on success
            type: bool
            sample: true
        existing_version:
            description:
                - The version string associated with the existing row.
                  Returned if the put fails due to options setting in the
                  request.
            returned: on success
            type: str
            sample: existing_version_example
        existing_value:
            description:
                - The map of values from a row.
            returned: on success
            type: dict
            sample: {}
        usage:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                read_units_consumed:
                    description:
                        - Read Units consumed by this operation.
                    returned: on success
                    type: int
                    sample: 56
                write_units_consumed:
                    description:
                        - Write Units consumed by this operation.
                    returned: on success
                    type: int
                    sample: 56
    sample: {
        "version": "version_example",
        "generated_value": "generated_value_example",
        "is_success": true,
        "existing_version": "existing_version_example",
        "existing_value": {},
        "usage": {
            "read_units_consumed": 56,
            "write_units_consumed": 56
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
    from oci.nosql import NosqlClient
    from oci.nosql.models import UpdateRowDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RowHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and delete"""

    def get_possible_entity_types(self):
        return super(RowHelperGen, self).get_possible_entity_types() + [
            "row",
            "rows",
            "nosqlrow",
            "nosqlrows",
            "rowresource",
            "rowsresource",
            "nosql",
        ]

    def get_module_resource_id_param(self):
        return "table_name_or_id"

    def get_module_resource_id(self):
        return self.module.params.get("table_name_or_id")

    def get_get_fn(self):
        return self.client.get_row

    def get_resource(self):
        optional_params = [
            "compartment_id",
            "timeout_in_ms",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_row,
            table_name_or_id=self.module.params.get("table_name_or_id"),
            key=self.module.params.get("key"),
            **optional_kwargs
        )

    def get_update_model_class(self):
        return UpdateRowDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_row,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                update_row_details=update_details,
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
            call_fn=self.client.delete_row,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                key=self.module.params.get("key"),
                compartment_id=self.module.params.get("compartment_id"),
                is_get_return_row=self.module.params.get("is_get_return_row"),
                timeout_in_ms=self.module.params.get("timeout_in_ms"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


RowHelperCustom = get_custom_class("RowHelperCustom")


class ResourceHelper(RowHelperCustom, RowHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            value=dict(type="dict"),
            option=dict(type="str", choices=["IF_ABSENT", "IF_PRESENT"]),
            ttl=dict(type="int"),
            is_ttl_use_table_default=dict(type="bool"),
            identity_cache_size=dict(type="int"),
            is_exact_match=dict(type="bool"),
            table_name_or_id=dict(aliases=["id"], type="str", required=True),
            key=dict(type="list", elements="str", no_log=True),
            compartment_id=dict(type="str"),
            is_get_return_row=dict(type="bool"),
            timeout_in_ms=dict(type="int"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="row",
        service_client_class=NosqlClient,
        namespace="nosql",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
