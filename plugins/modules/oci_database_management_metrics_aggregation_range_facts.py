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
module: oci_database_management_metrics_aggregation_range_facts
short_description: Fetches details about one or multiple MetricsAggregationRange resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MetricsAggregationRange resources in Oracle Cloud Infrastructure
    - Gets metrics for the external ASM specified by `externalAsmId`.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_asm_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the external ASM.
        type: str
        required: true
    start_time:
        description:
            - The beginning of the time range set to retrieve metric data for the DB system
              and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.
        type: str
        required: true
    end_time:
        description:
            - The end of the time range set to retrieve metric data for the DB system
              and its members. Expressed in UTC in ISO-8601 format, which is `yyyy-MM-dd'T'hh:mm:ss.sss'Z'`.
        type: str
        required: true
    filter_by_metric_names:
        description:
            - The filter used to retrieve a specific set of metrics by passing the desired metric names with a comma separator. Note that, by default, the
              service returns all supported metrics.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List metrics_aggregation_ranges
  oci_database_management_metrics_aggregation_range_facts:
    # required
    external_asm_id: "ocid1.externalasm.oc1..xxxxxxEXAMPLExxxxxx"
    start_time: start_time_example
    end_time: end_time_example

    # optional
    filter_by_metric_names: filter_by_metric_names_example

"""

RETURN = """
metrics_aggregation_ranges:
    description:
        - List of MetricsAggregationRange resources
    returned: on success
    type: complex
    contains:
        header:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                metric_name:
                    description:
                        - The name of the metric.
                    returned: on success
                    type: str
                    sample: metric_name_example
                duration_in_seconds:
                    description:
                        - The duration of the returned aggregated data in seconds.
                    returned: on success
                    type: int
                    sample: 56
                metadata:
                    description:
                        - The additional information about the metric.
                        - "Example: `\\"unit\\": \\"bytes\\"`"
                    returned: on success
                    type: dict
                    sample: {}
                dimensions:
                    description:
                        - The qualifiers provided in the definition of the returned metric.
                    returned: on success
                    type: dict
                    sample: {}
                start_timestamp_in_epoch_seconds:
                    description:
                        - The start time associated with the value of the metric.
                    returned: on success
                    type: int
                    sample: 56
                mean:
                    description:
                        - The mean value of the metric.
                    returned: on success
                    type: float
                    sample: 1.2
        metrics:
            description:
                - The list of metrics returned for the specified request. Each of the metrics
                  has a `metricName` and additional properties like `metadata`, `dimensions`.
                  If a property is not set, then use the value from `header`.
                - "Suppose `m` be an item in the `metrics` array:
                  - If `m.metricName` is not set, use `header.metricName` instead
                  - If `m.durationInSeconds` is not set, use `header.durationInSeconds` instead
                  - If `m.dimensions` is not set, use `header.dimensions` instead
                  - If `m.metadata` is not set, use `header.metadata` instead"
            returned: on success
            type: complex
            contains:
                metric_name:
                    description:
                        - The name of the metric.
                    returned: on success
                    type: str
                    sample: metric_name_example
                duration_in_seconds:
                    description:
                        - The duration of the returned aggregated data in seconds.
                    returned: on success
                    type: int
                    sample: 56
                metadata:
                    description:
                        - The additional information about the metric.
                        - "Example: `\\"unit\\": \\"bytes\\"`"
                    returned: on success
                    type: dict
                    sample: {}
                dimensions:
                    description:
                        - The qualifiers provided in the definition of the returned metric.
                    returned: on success
                    type: dict
                    sample: {}
                start_timestamp_in_epoch_seconds:
                    description:
                        - The start time associated with the value of the metric.
                    returned: on success
                    type: int
                    sample: 56
                mean:
                    description:
                        - The mean value of the metric.
                    returned: on success
                    type: float
                    sample: 1.2
        range_start_time_in_epoch_seconds:
            description:
                - The beginning of the time range (inclusive) of the returned metric data.
            returned: on success
            type: int
            sample: 56
        range_end_time_in_epoch_seconds:
            description:
                - The end of the time range (exclusive) of the returned metric data.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "header": {
            "metric_name": "metric_name_example",
            "duration_in_seconds": 56,
            "metadata": {},
            "dimensions": {},
            "start_timestamp_in_epoch_seconds": 56,
            "mean": 1.2
        },
        "metrics": [{
            "metric_name": "metric_name_example",
            "duration_in_seconds": 56,
            "metadata": {},
            "dimensions": {},
            "start_timestamp_in_epoch_seconds": 56,
            "mean": 1.2
        }],
        "range_start_time_in_epoch_seconds": 56,
        "range_end_time_in_epoch_seconds": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MetricsAggregationRangeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "external_asm_id",
            "start_time",
            "end_time",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "filter_by_metric_names",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_external_asm_metrics,
            external_asm_id=self.module.params.get("external_asm_id"),
            start_time=self.module.params.get("start_time"),
            end_time=self.module.params.get("end_time"),
            **optional_kwargs
        )


MetricsAggregationRangeFactsHelperCustom = get_custom_class(
    "MetricsAggregationRangeFactsHelperCustom"
)


class ResourceFactsHelper(
    MetricsAggregationRangeFactsHelperCustom, MetricsAggregationRangeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_asm_id=dict(type="str", required=True),
            start_time=dict(type="str", required=True),
            end_time=dict(type="str", required=True),
            filter_by_metric_names=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="metrics_aggregation_range",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(metrics_aggregation_ranges=result)


if __name__ == "__main__":
    main()
