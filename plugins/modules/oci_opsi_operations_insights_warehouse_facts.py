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
module: oci_opsi_operations_insights_warehouse_facts
short_description: Fetches details about one or multiple OperationsInsightsWarehouse resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple OperationsInsightsWarehouse resources in Oracle Cloud Infrastructure
    - Gets a list of Operations Insights warehouses. Either compartmentId or id must be specified.
      There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.
    - If I(operations_insights_warehouse_id) is specified, the details of a single OperationsInsightsWarehouse will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operations_insights_warehouse_id:
        description:
            - Unique Operations Insights Warehouse identifier
            - Required to get a specific operations_insights_warehouse.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the entire display name.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Lifecycle states
        type: list
        elements: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific operations_insights_warehouse
  oci_opsi_operations_insights_warehouse_facts:
    # required
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"

- name: List operations_insights_warehouses
  oci_opsi_operations_insights_warehouse_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: [ "CREATING" ]
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
operations_insights_warehouses:
    description:
        - List of OperationsInsightsWarehouse resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OPSI Warehouse OCID
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friedly name of Operations Insights Warehouse that does not have to be unique.
            returned: on success
            type: str
            sample: display_name_example
        cpu_allocated:
            description:
                - Number of OCPUs allocated to OPSI Warehouse ADW.
            returned: on success
            type: float
            sample: 1.2
        cpu_used:
            description:
                - Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.
            returned: on success
            type: float
            sample: 1.2
        storage_allocated_in_gbs:
            description:
                - Storage allocated to OPSI Warehouse ADW.
            returned: on success
            type: float
            sample: 1.2
        storage_used_in_gbs:
            description:
                - Storage by OPSI Warehouse ADW in GB.
            returned: on success
            type: float
            sample: 1.2
        dynamic_group_id:
            description:
                - OCID of the dynamic group created for the warehouse
            returned: on success
            type: str
            sample: "ocid1.dynamicgroup.oc1..xxxxxxEXAMPLExxxxxx"
        operations_insights_tenancy_id:
            description:
                - Tenancy Identifier of Operations Insights service
            returned: on success
            type: str
            sample: "ocid1.operationsinsightstenancy.oc1..xxxxxxEXAMPLExxxxxx"
        time_last_wallet_rotated:
            description:
                - The time at which the ADW wallet was last rotated for the Operations Insights Warehouse. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time at which the resource was first created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time at which the resource was last updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - Possible lifecycle states
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "cpu_allocated": 1.2,
        "cpu_used": 1.2,
        "storage_allocated_in_gbs": 1.2,
        "storage_used_in_gbs": 1.2,
        "dynamic_group_id": "ocid1.dynamicgroup.oc1..xxxxxxEXAMPLExxxxxx",
        "operations_insights_tenancy_id": "ocid1.operationsinsightstenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "time_last_wallet_rotated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperationsInsightsWarehouseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "operations_insights_warehouse_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_operations_insights_warehouse,
            operations_insights_warehouse_id=self.module.params.get(
                "operations_insights_warehouse_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
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
            self.client.list_operations_insights_warehouses, **optional_kwargs
        )


OperationsInsightsWarehouseFactsHelperCustom = get_custom_class(
    "OperationsInsightsWarehouseFactsHelperCustom"
)


class ResourceFactsHelper(
    OperationsInsightsWarehouseFactsHelperCustom,
    OperationsInsightsWarehouseFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            operations_insights_warehouse_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="list",
                elements="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="operations_insights_warehouse",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(operations_insights_warehouses=result)


if __name__ == "__main__":
    main()
