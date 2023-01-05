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
module: oci_cloud_bridge_historical_metric_facts
short_description: Fetches details about one or multiple HistoricalMetric resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HistoricalMetric resources in Oracle Cloud Infrastructure
    - List asset historical metrics.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    asset_id:
        description:
            - Unique asset identifier.
        type: str
        required: true
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
            - "timeUpdated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List historical_metrics
  oci_cloud_bridge_historical_metric_facts:
    # required
    asset_id: "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
historical_metrics:
    description:
        - List of HistoricalMetric resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Metric name.
            returned: on success
            type: str
            sample: name_example
        aggregation:
            description:
                - Aggregation time interval.
            returned: on success
            type: str
            sample: aggregation_example
        value:
            description:
                - Aggregation value.
            returned: on success
            type: float
            sample: 3.4
        time_created:
            description:
                - The time the HistoricalMetric was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the HistoricalMetric was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "name": "name_example",
        "aggregation": "aggregation_example",
        "value": 3.4,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00"
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


class HistoricalMetricFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "asset_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_historical_metrics,
            asset_id=self.module.params.get("asset_id"),
            **optional_kwargs
        )


HistoricalMetricFactsHelperCustom = get_custom_class(
    "HistoricalMetricFactsHelperCustom"
)


class ResourceFactsHelper(
    HistoricalMetricFactsHelperCustom, HistoricalMetricFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            asset_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeCreated", "timeUpdated", "displayName"]
            ),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="historical_metric",
        service_client_class=InventoryClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(historical_metrics=result)


if __name__ == "__main__":
    main()
