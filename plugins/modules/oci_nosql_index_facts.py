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
module: oci_nosql_index_facts
short_description: Fetches details about one or multiple Index resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Index resources in Oracle Cloud Infrastructure
    - Get a list of indexes on a table.
    - If I(index_name) is specified, the details of a single Index will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
        type: str
        required: true
    index_name:
        description:
            - The name of a table's index.
            - Required to get a specific index.
        type: str
    compartment_id:
        description:
            - The ID of a table's compartment. When a table is identified
              by name, the compartmentId is often needed to provide
              context for interpreting the name.
        type: str
    name:
        description:
            - "A shell-globbing-style (*?[]) filter for names."
        type: str
    lifecycle_state:
        description:
            - Filter list by the lifecycle state of the item.
        type: str
        choices:
            - "ALL"
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "INACTIVE"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be
              provided. Default order for timeCreated is descending. Default
              order for name is ascending. If no value is specified
              timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific index
  oci_nosql_index_facts:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    index_name: index_name_example

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List indexes
  oci_nosql_index_facts:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    lifecycle_state: ALL
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
indexes:
    description:
        - List of Index resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - Compartment Identifier.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        table_name:
            description:
                - The name of the table to which this index belongs.
                - Returned for get operation
            returned: on success
            type: str
            sample: table_name_example
        table_id:
            description:
                - the OCID of the table to which this index belongs.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.table.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Index name.
            returned: on success
            type: str
            sample: name_example
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
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "table_name": "table_name_example",
        "table_id": "ocid1.table.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "keys": [{
            "column_name": "column_name_example",
            "json_path": "json_path_example",
            "json_field_type": "json_field_type_example"
        }],
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.nosql import NosqlClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IndexFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "table_name_or_id",
            "index_name",
        ]

    def get_required_params_for_list(self):
        return [
            "table_name_or_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_index,
            table_name_or_id=self.module.params.get("table_name_or_id"),
            index_name=self.module.params.get("index_name"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_indexes,
            table_name_or_id=self.module.params.get("table_name_or_id"),
            **optional_kwargs
        )


IndexFactsHelperCustom = get_custom_class("IndexFactsHelperCustom")


class ResourceFactsHelper(IndexFactsHelperCustom, IndexFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            table_name_or_id=dict(type="str", required=True),
            index_name=dict(type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ALL",
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "INACTIVE",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "name"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="index",
        service_client_class=NosqlClient,
        namespace="nosql",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(indexes=result)


if __name__ == "__main__":
    main()
