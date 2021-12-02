#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_nosql_table_facts
short_description: Fetches details about one or multiple Table resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Table resources in Oracle Cloud Infrastructure
    - Get a list of tables in a compartment.
    - If I(table_name_or_id) is specified, the details of a single Table will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
            - Required to get a specific table.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of a table's compartment. When a table is identified
              by name, the compartmentId is often needed to provide
              context for interpreting the name.
            - Required to list multiple tables.
        type: str
    name:
        description:
            - "A shell-globbing-style (*?[]) filter for names."
        type: str
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific table
  oci_nosql_table_facts:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List tables
  oci_nosql_table_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: name_example
    sort_order: ASC
    sort_by: timeCreated
    lifecycle_state: ALL

"""

RETURN = """
tables:
    description:
        - List of Table resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Human-friendly table name, immutable.
            returned: on success
            type: str
            sample: name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the the table was created. An RFC3339 formatted
                  datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the the table's metadata was last updated. An
                  RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        table_limits:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                max_read_units:
                    description:
                        - Maximum sustained read throughput limit for the table.
                    returned: on success
                    type: int
                    sample: 56
                max_write_units:
                    description:
                        - Maximum sustained write throughput limit for the table.
                    returned: on success
                    type: int
                    sample: 56
                max_storage_in_g_bs:
                    description:
                        - Maximum size of storage used by the table.
                    returned: on success
                    type: int
                    sample: 56
        lifecycle_state:
            description:
                - The state of a table.
            returned: on success
            type: str
            sample: CREATING
        is_auto_reclaimable:
            description:
                - True if this table can be reclaimed after an idle period.
            returned: on success
            type: bool
            sample: true
        time_of_expiration:
            description:
                - If lifecycleState is INACTIVE, indicates when
                  this table will be automatically removed.
                  An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_details:
            description:
                - A message describing the current state in more detail.
            returned: on success
            type: str
            sample: lifecycle_details_example
        schema:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                columns:
                    description:
                        - The columns of a table.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The column name.
                            returned: on success
                            type: str
                            sample: name_example
                        type:
                            description:
                                - The column type.
                            returned: on success
                            type: str
                            sample: type_example
                        is_nullable:
                            description:
                                - The column nullable flag.
                            returned: on success
                            type: bool
                            sample: true
                        default_value:
                            description:
                                - The column default value.
                            returned: on success
                            type: str
                            sample: default_value_example
                primary_key:
                    description:
                        - A list of column names that make up a key.
                    returned: on success
                    type: list
                    sample: []
                shard_key:
                    description:
                        - A list of column names that make up a key.
                    returned: on success
                    type: list
                    sample: []
                ttl:
                    description:
                        - The default Time-to-Live for the table, in days.
                    returned: on success
                    type: int
                    sample: 56
        ddl_statement:
            description:
                - A DDL statement representing the schema.
            returned: on success
            type: str
            sample: ddl_statement_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined
                  name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and
                  scoped to a namespace.  Example: `{\\"foo-namespace\\":
                  {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Read-only system tag. These predefined keys are scoped to
                  namespaces.  At present the only supported namespace is
                  `\\"orcl-cloud\\"`; and the only key in that namespace is
                  `\\"free-tier-retained\\"`.
                  Example: `{\\"orcl-cloud\\"\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "table_limits": {
            "max_read_units": 56,
            "max_write_units": 56,
            "max_storage_in_g_bs": 56
        },
        "lifecycle_state": "CREATING",
        "is_auto_reclaimable": true,
        "time_of_expiration": "2013-10-20T19:20:30+01:00",
        "lifecycle_details": "lifecycle_details_example",
        "schema": {
            "columns": [{
                "name": "name_example",
                "type": "type_example",
                "is_nullable": true,
                "default_value": "default_value_example"
            }],
            "primary_key": [],
            "shard_key": [],
            "ttl": 56
        },
        "ddl_statement": "ddl_statement_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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


class TableFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "table_name_or_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
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
            self.client.get_table,
            table_name_or_id=self.module.params.get("table_name_or_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_tables,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TableFactsHelperCustom = get_custom_class("TableFactsHelperCustom")


class ResourceFactsHelper(TableFactsHelperCustom, TableFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            table_name_or_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "name"]),
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
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="table",
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

    module.exit_json(tables=result)


if __name__ == "__main__":
    main()
