#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_cloud_bridge_asset_aggregation_facts
short_description: Fetches details about one or multiple AssetAggregation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AssetAggregation resources in Oracle Cloud Infrastructure
    - Returns an aggregation of assets. Aggregation groups are sorted by groupBy property.
      Default sort order is ascending, but can be overridden by the sortOrder parameter.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
    aggregation_properties:
        description:
            - An array of properties on which to aggregate.
        type: list
        elements: str
        required: true
    lifecycle_state:
        description:
            - A filter to return only assets whose lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "DELETED"
    source_key:
        description:
            - Source key from where the assets originate.
        type: str
    external_asset_key:
        description:
            - External asset key.
        type: str
    asset_type:
        description:
            - The type of asset.
        type: str
        choices:
            - "VMWARE_VM"
            - "VM"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    group_by:
        description:
            - The dimensions in which to group the aggregations.
        type: list
        elements: str
    inventory_id:
        description:
            - Unique Inventory identifier.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List asset_aggregations
  oci_cloud_bridge_asset_aggregation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    aggregation_properties: [ "aggregation_properties_example" ]

    # optional
    lifecycle_state: ACTIVE
    source_key: source_key_example
    external_asset_key: external_asset_key_example
    asset_type: VMWARE_VM
    sort_order: ASC
    group_by: [ "group_by_example" ]
    inventory_id: "ocid1.inventory.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
asset_aggregations:
    description:
        - List of AssetAggregation resources
    returned: on success
    type: complex
    contains:
        dimensions:
            description:
                - The dimensions along which assets can be aggregated for analytics.
            returned: on success
            type: dict
            sample: {}
        count:
            description:
                - Returns the total number of observations from the group of assets.
            returned: on success
            type: int
            sample: 56
        max:
            description:
                - Returns the highest value from all the assets.
            returned: on success
            type: float
            sample: 1.2
        mean:
            description:
                - Returns the value of sum divided by count from the group of assets.
            returned: on success
            type: float
            sample: 1.2
        min:
            description:
                - Returns the lowest value from the group of assets.
            returned: on success
            type: float
            sample: 1.2
        sum:
            description:
                - Returns all values added together from the group of assets.
            returned: on success
            type: float
            sample: 1.2
        aggregated_property:
            description:
                - Aggregated property.
            returned: on success
            type: str
            sample: aggregated_property_example
    sample: [{
        "dimensions": {},
        "count": 56,
        "max": 1.2,
        "mean": 1.2,
        "min": 1.2,
        "sum": 1.2,
        "aggregated_property": "aggregated_property_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_bridge import InventoryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AssetAggregationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "aggregation_properties",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "source_key",
            "external_asset_key",
            "asset_type",
            "sort_order",
            "group_by",
            "inventory_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.analyze_assets,
            compartment_id=self.module.params.get("compartment_id"),
            aggregation_properties=self.module.params.get("aggregation_properties"),
            **optional_kwargs
        )


AssetAggregationFactsHelperCustom = get_custom_class(
    "AssetAggregationFactsHelperCustom"
)


class ResourceFactsHelper(
    AssetAggregationFactsHelperCustom, AssetAggregationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            aggregation_properties=dict(type="list", elements="str", required=True),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "DELETED"]),
            source_key=dict(type="str", no_log=True),
            external_asset_key=dict(type="str", no_log=True),
            asset_type=dict(type="str", choices=["VMWARE_VM", "VM"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            group_by=dict(type="list", elements="str"),
            inventory_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="asset_aggregation",
        service_client_class=InventoryClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(asset_aggregations=result)


if __name__ == "__main__":
    main()
