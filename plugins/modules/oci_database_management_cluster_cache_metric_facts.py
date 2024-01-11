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
module: oci_database_management_cluster_cache_metric_facts
short_description: Fetches details about a ClusterCacheMetric resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ClusterCacheMetric resource in Oracle Cloud Infrastructure
    - Gets the metrics related to cluster cache for the Oracle
      Real Application Clusters (Oracle RAC) database specified
      by managedDatabaseId.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        aliases: ["id"]
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
- name: Get a specific cluster_cache_metric
  oci_database_management_cluster_cache_metric_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    start_time: start_time_example
    end_time: end_time_example

"""

RETURN = """
cluster_cache_metric:
    description:
        - ClusterCacheMetric resource
    returned: on success
    type: complex
    contains:
        cluster_cache_metrics:
            description:
                - A list of cluster cache metrics for a specific Managed Database.
            returned: on success
            type: complex
            contains:
                metric_name:
                    description:
                        - The name of the metric the time series data corresponds to.
                    returned: on success
                    type: str
                    sample: metric_name_example
                datapoints:
                    description:
                        - The time series metric data for the given metric.
                    returned: on success
                    type: complex
                    contains:
                        timestamp:
                            description:
                                - The date and time the metric was created.
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        value:
                            description:
                                - The value of the metric.
                            returned: on success
                            type: float
                            sample: 1.2
                        unit:
                            description:
                                - The unit of the metric value.
                            returned: on success
                            type: str
                            sample: unit_example
                        dimensions:
                            description:
                                - The dimensions of the metric.
                            returned: on success
                            type: complex
                            contains:
                                dimension_name:
                                    description:
                                        - The name of the dimension.
                                    returned: on success
                                    type: str
                                    sample: dimension_name_example
                                dimension_value:
                                    description:
                                        - The value of the dimension.
                                    returned: on success
                                    type: str
                                    sample: dimension_value_example
    sample: {
        "cluster_cache_metrics": [{
            "metric_name": "metric_name_example",
            "datapoints": [{
                "timestamp": "2013-10-20T19:20:30+01:00",
                "value": 1.2,
                "unit": "unit_example",
                "dimensions": [{
                    "dimension_name": "dimension_name_example",
                    "dimension_value": "dimension_value_example"
                }]
            }]
        }]
    }
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


class ClusterCacheMetricFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "start_time",
            "end_time",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_cluster_cache_metric,
            managed_database_id=self.module.params.get("managed_database_id"),
            start_time=self.module.params.get("start_time"),
            end_time=self.module.params.get("end_time"),
        )


ClusterCacheMetricFactsHelperCustom = get_custom_class(
    "ClusterCacheMetricFactsHelperCustom"
)


class ResourceFactsHelper(
    ClusterCacheMetricFactsHelperCustom, ClusterCacheMetricFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(aliases=["id"], type="str", required=True),
            start_time=dict(type="str", required=True),
            end_time=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="cluster_cache_metric",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(cluster_cache_metric=result)


if __name__ == "__main__":
    main()
