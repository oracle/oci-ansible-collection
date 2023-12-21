#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_nosql_table_actions
short_description: Perform actions on a Table resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Table resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), change a table's compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    table_name_or_id:
        description:
            - A table name within the compartment, or a table OCID.
        type: str
        aliases: ["id"]
        required: true
    from_compartment_id:
        description:
            - The OCID of the table's current compartment.  Required
              if the tableNameOrId path parameter is a table name.
              Optional if tableNameOrId is an OCID.  If tableNameOrId
              is an OCID, and fromCompartmentId is supplied, the latter
              must match the identified table's current compartmentId.
        type: str
    to_compartment_id:
        description:
            - The OCID of the table's new compartment.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Table.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on table
  oci_nosql_table_actions:
    # required
    table_name_or_id: "ocid1.tablenameor.oc1..xxxxxxEXAMPLExxxxxx"
    to_compartment_id: "ocid1.tocompartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

    # optional
    from_compartment_id: "ocid1.fromcompartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
table:
    description:
        - Details of the Table resource acted upon by the current operation
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
                capacity_mode:
                    description:
                        - The capacity mode of the table.  If capacityMode = ON_DEMAND,
                          maxReadUnits and maxWriteUnits are not used, and both will have
                          the value of zero.
                    returned: on success
                    type: str
                    sample: PROVISIONED
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
                        is_as_uuid:
                            description:
                                - True if the STRING column was declared AS UUID.
                            returned: on success
                            type: bool
                            sample: true
                        is_generated:
                            description:
                                - True if the STRING AS UUID column is also GENERATED BY DEFAULT.
                            returned: on success
                            type: bool
                            sample: true
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
                identity:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        column_name:
                            description:
                                - The name of the identity column.
                            returned: on success
                            type: str
                            sample: column_name_example
                        is_always:
                            description:
                                - True if the identity value is GENERATED ALWAYS.
                            returned: on success
                            type: bool
                            sample: true
                        is_null:
                            description:
                                - True if the identity value is GENERATED BY DEFAULT ON NULL.
                            returned: on success
                            type: bool
                            sample: true
        ddl_statement:
            description:
                - A DDL statement representing the schema.
            returned: on success
            type: str
            sample: ddl_statement_example
        schema_state:
            description:
                - "The current state of this table's schema. Available states are
                  MUTABLE - The schema can be changed. The table is not eligible for replication.
                  FROZEN - The schema is immutable. The table is eligible for replication."
            returned: on success
            type: str
            sample: MUTABLE
        is_multi_region:
            description:
                - True if this table is currently a member of a replication set.
            returned: on success
            type: bool
            sample: true
        local_replica_initialization_in_percent:
            description:
                - If this table is in a replication set, this value represents
                  the progress of the initialization of the replica's data.  A
                  value of 100 indicates that initialization has completed.
            returned: on success
            type: int
            sample: 56
        replicas:
            description:
                - An array of Replica listing this table's replicas, if any
            returned: on success
            type: complex
            contains:
                region:
                    description:
                        - A customer-facing region identifier
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                table_id:
                    description:
                        - The OCID of the replica table
                    returned: on success
                    type: str
                    sample: "ocid1.table.oc1..xxxxxxEXAMPLExxxxxx"
                max_write_units:
                    description:
                        - Maximum sustained write throughput limit of the replica table.
                    returned: on success
                    type: int
                    sample: 56
                capacity_mode:
                    description:
                        - The capacity mode of the replica.
                    returned: on success
                    type: str
                    sample: PROVISIONED
                lifecycle_state:
                    description:
                        - The state of the replica.
                    returned: on success
                    type: str
                    sample: CREATING
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "table_limits": {
            "max_read_units": 56,
            "max_write_units": 56,
            "max_storage_in_g_bs": 56,
            "capacity_mode": "PROVISIONED"
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
                "default_value": "default_value_example",
                "is_as_uuid": true,
                "is_generated": true
            }],
            "primary_key": [],
            "shard_key": [],
            "ttl": 56,
            "identity": {
                "column_name": "column_name_example",
                "is_always": true,
                "is_null": true
            }
        },
        "ddl_statement": "ddl_statement_example",
        "schema_state": "MUTABLE",
        "is_multi_region": true,
        "local_replica_initialization_in_percent": 56,
        "replicas": [{
            "region": "us-phoenix-1",
            "table_id": "ocid1.table.oc1..xxxxxxEXAMPLExxxxxx",
            "max_write_units": 56,
            "capacity_mode": "PROVISIONED",
            "lifecycle_state": "CREATING",
            "lifecycle_details": "lifecycle_details_example"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.nosql import NosqlClient
    from oci.nosql.models import ChangeTableCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TableActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "table_name_or_id"

    def get_module_resource_id(self):
        return self.module.params.get("table_name_or_id")

    def get_get_fn(self):
        return self.client.get_table

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_table,
            table_name_or_id=self.module.params.get("table_name_or_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeTableCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_table_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                table_name_or_id=self.module.params.get("table_name_or_id"),
                change_table_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


TableActionsHelperCustom = get_custom_class("TableActionsHelperCustom")


class ResourceHelper(TableActionsHelperCustom, TableActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            table_name_or_id=dict(aliases=["id"], type="str", required=True),
            from_compartment_id=dict(type="str"),
            to_compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="table",
        service_client_class=NosqlClient,
        namespace="nosql",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
