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
module: oci_em_warehouse_facts
short_description: Fetches details about one or multiple EmWarehouse resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple EmWarehouse resources in Oracle Cloud Infrastructure
    - Returns a list of EmWarehouses.
    - If I(em_warehouse_id) is specified, the details of a single EmWarehouse will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    em_warehouse_id:
        description:
            - unique EmWarehouse identifier
            - Required to get a specific em_warehouse.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    operations_insights_warehouse_id:
        description:
            - unique operationsInsightsWarehouseId identifier
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
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific em_warehouse
  oci_em_warehouse_facts:
    # required
    em_warehouse_id: "ocid1.emwarehouse.oc1..xxxxxxEXAMPLExxxxxx"

- name: List em_warehouses
  oci_em_warehouse_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
em_warehouses:
    description:
        - List of EmWarehouse resources
    returned: on success
    type: complex
    contains:
        operations_insights_warehouse_id:
            description:
                - operations Insights Warehouse Identifier
            returned: on success
            type: str
            sample: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - EmWarehouse Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        em_warehouse_type:
            description:
                - Type of the EmWarehouse.
            returned: on success
            type: str
            sample: em_warehouse_type_example
        em_bridge_id:
            description:
                - EMBridge Identifier
            returned: on success
            type: str
            sample: "ocid1.embridge.oc1..xxxxxxEXAMPLExxxxxx"
        latest_etl_run_status:
            description:
                - Data Flow Run Status
            returned: on success
            type: str
            sample: latest_etl_run_status_example
        latest_etl_run_message:
            description:
                - Data Flow Run Status Message
            returned: on success
            type: str
            sample: latest_etl_run_message_example
        latest_etl_run_time:
            description:
                - Data Flow Run Total Time
            returned: on success
            type: str
            sample: latest_etl_run_time_example
        time_created:
            description:
                - The time the the EmWarehouse was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the EmWarehouse was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the EmWarehouse.
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
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "operations_insights_warehouse_id": "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "em_warehouse_type": "em_warehouse_type_example",
        "em_bridge_id": "ocid1.embridge.oc1..xxxxxxEXAMPLExxxxxx",
        "latest_etl_run_status": "latest_etl_run_status_example",
        "latest_etl_run_message": "latest_etl_run_message_example",
        "latest_etl_run_time": "latest_etl_run_time_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.em_warehouse import EmDataLakeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EmWarehouseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "em_warehouse_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_em_warehouse,
            em_warehouse_id=self.module.params.get("em_warehouse_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "lifecycle_state",
            "display_name",
            "operations_insights_warehouse_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_em_warehouses, **optional_kwargs
        )


EmWarehouseFactsHelperCustom = get_custom_class("EmWarehouseFactsHelperCustom")


class ResourceFactsHelper(EmWarehouseFactsHelperCustom, EmWarehouseFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            em_warehouse_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            operations_insights_warehouse_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="em_warehouse",
        service_client_class=EmDataLakeClient,
        namespace="em_warehouse",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(em_warehouses=result)


if __name__ == "__main__":
    main()
