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
module: oci_opsi_operations_insights_warehouse_resource_usage_summary_facts
short_description: Fetches details about a OperationsInsightsWarehouseResourceUsageSummary resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a OperationsInsightsWarehouseResourceUsageSummary resource in Oracle Cloud Infrastructure
    - Gets the details of resources used by an Operations Insights Warehouse.
      There is only expected to be 1 warehouse per tenant. The warehouse is expected to be in the root compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    operations_insights_warehouse_id:
        description:
            - Unique Operations Insights Warehouse identifier
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific operations_insights_warehouse_resource_usage_summary
  oci_opsi_operations_insights_warehouse_resource_usage_summary_facts:
    # required
    operations_insights_warehouse_id: "ocid1.operationsinsightswarehouse.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
operations_insights_warehouse_resource_usage_summary:
    description:
        - OperationsInsightsWarehouseResourceUsageSummary resource
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OPSI Warehouse OCID
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        cpu_used:
            description:
                - Number of OCPUs used by OPSI Warehouse ADW. Can be fractional.
            returned: on success
            type: float
            sample: 1.2
        storage_used_in_gbs:
            description:
                - Storage by OPSI Warehouse ADW in GB.
            returned: on success
            type: float
            sample: 1.2
        lifecycle_state:
            description:
                - Possible lifecycle states
            returned: on success
            type: str
            sample: CREATING
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "cpu_used": 1.2,
        "storage_used_in_gbs": 1.2,
        "lifecycle_state": "CREATING"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OperationsInsightsWarehouseResourceUsageSummaryFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "operations_insights_warehouse_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.summarize_operations_insights_warehouse_resource_usage,
            operations_insights_warehouse_id=self.module.params.get(
                "operations_insights_warehouse_id"
            ),
        )


OperationsInsightsWarehouseResourceUsageSummaryFactsHelperCustom = get_custom_class(
    "OperationsInsightsWarehouseResourceUsageSummaryFactsHelperCustom"
)


class ResourceFactsHelper(
    OperationsInsightsWarehouseResourceUsageSummaryFactsHelperCustom,
    OperationsInsightsWarehouseResourceUsageSummaryFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            operations_insights_warehouse_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="operations_insights_warehouse_resource_usage_summary",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(operations_insights_warehouse_resource_usage_summary=result)


if __name__ == "__main__":
    main()
