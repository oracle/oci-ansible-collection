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
module: oci_database_management_availability_metric_facts
short_description: Fetches details about one or multiple AvailabilityMetric resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AvailabilityMetric resources in Oracle Cloud Infrastructure
    - Gets the availability metrics related to managed database for the Oracle
      database specified by managedDatabaseId.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    start_time:
        description:
            - "The start time of the time range to retrieve the health metrics of a Managed Database
              in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
        type: str
        required: true
    end_time:
        description:
            - "The end time of the time range to retrieve the health metrics of a Managed Database
              in UTC in ISO-8601 format, which is \\"yyyy-MM-dd'T'hh:mm:ss.sss'Z'\\"."
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List availability_metrics
  oci_database_management_availability_metric_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    start_time: start_time_example
    end_time: end_time_example

"""

RETURN = """
availability_metrics:
    description:
        - List of AvailabilityMetric resources
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


class AvailabilityMetricFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
            "start_time",
            "end_time",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_managed_database_availability_metrics,
            managed_database_id=self.module.params.get("managed_database_id"),
            start_time=self.module.params.get("start_time"),
            end_time=self.module.params.get("end_time"),
            **optional_kwargs
        )


AvailabilityMetricFactsHelperCustom = get_custom_class(
    "AvailabilityMetricFactsHelperCustom"
)


class ResourceFactsHelper(
    AvailabilityMetricFactsHelperCustom, AvailabilityMetricFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            start_time=dict(type="str", required=True),
            end_time=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="availability_metric",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(availability_metrics=result)


if __name__ == "__main__":
    main()
