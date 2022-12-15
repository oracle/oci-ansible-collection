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
module: oci_opsi_summarize_host_insights_top_processes_usage_facts
short_description: Fetches details about one or multiple SummarizeHostInsightsTopProcessesUsage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SummarizeHostInsightsTopProcessesUsage resources in Oracle Cloud Infrastructure
    - Returns response with aggregated data (timestamp, usageData) for top processes on a specific date.
      Data is aggregated for the time specified and processes are sorted descendent by the process metric specified (CPU, MEMORY, VIRTUAL_MEMORY).
      hostInsightId, processMetric must be specified.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    id:
        description:
            - Required L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host insight resource.
        type: str
        required: true
    resource_metric:
        description:
            - Host top processes resource metric sort options.
              Supported values are CPU, MEMORY, VIIRTUAL_MEMORY.
        type: str
        required: true
    timestamp:
        description:
            - Timestamp at which to gather the top processes.
              This will be top processes over the hour or over the day pending the time range passed into the query.
        type: str
        required: true
    time_interval_start:
        description:
            - Analysis start time in UTC in ISO 8601 format(inclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              The minimum allowed value is 2 years prior to the current day.
              timeIntervalStart and timeIntervalEnd parameters are used together.
              If analysisTimeInterval is specified, this parameter is ignored.
        type: str
    time_interval_end:
        description:
            - Analysis end time in UTC in ISO 8601 format(exclusive).
              Example 2019-10-30T00:00:00Z (yyyy-MM-ddThh:mm:ssZ).
              timeIntervalStart and timeIntervalEnd are used together.
              If timeIntervalEnd is not specified, current time is used as timeIntervalEnd.
        type: str
    analysis_time_interval:
        description:
            - Specify time period in ISO 8601 format with respect to current time.
              Default is last 30 days represented by P30D.
              If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
              Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to
              current time (P25M).
        type: str
    host_type:
        description:
            - Filter by one or more host types.
              Possible values are CLOUD-HOST, EXTERNAL-HOST
        type: list
        elements: str
    host_id:
        description:
            - Optional L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host (Compute Id)
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List summarize_host_insights_top_processes_usages
  oci_opsi_summarize_host_insights_top_processes_usage_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    resource_metric: resource_metric_example
    timestamp: 2013-10-20T19:20:30+01:00

    # optional
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    analysis_time_interval: analysis_time_interval_example
    host_type: [ "host_type_example" ]
    host_id: "ocid1.host.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
summarize_host_insights_top_processes_usages:
    description:
        - List of SummarizeHostInsightsTopProcessesUsage resources
    returned: on success
    type: complex
    contains:
        command:
            description:
                - Command line and arguments used to launch process.
            returned: on success
            type: str
            sample: command_example
        process_hash:
            description:
                - Unique identifier for a process.
            returned: on success
            type: str
            sample: process_hash_example
        cpu_usage:
            description:
                - Process CPU usage.
            returned: on success
            type: float
            sample: 1.2
        cpu_utilization:
            description:
                - Process CPU utilization percentage.
            returned: on success
            type: float
            sample: 1.2
        memory_utilization:
            description:
                - Process memory utilization percentage.
            returned: on success
            type: float
            sample: 1.2
        virtual_memory_in_mbs:
            description:
                - Process virtual memory in Megabytes.
            returned: on success
            type: float
            sample: 1.2
        physical_memory_in_mbs:
            description:
                - Procress physical memory in Megabytes.
            returned: on success
            type: float
            sample: 1.2
        max_process_count:
            description:
                - Maximum number of processes running at time of collection.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "command": "command_example",
        "process_hash": "process_hash_example",
        "cpu_usage": 1.2,
        "cpu_utilization": 1.2,
        "memory_utilization": 1.2,
        "virtual_memory_in_mbs": 1.2,
        "physical_memory_in_mbs": 1.2,
        "max_process_count": 56
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


class SummarizeHostInsightsTopProcessesUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "id",
            "resource_metric",
            "timestamp",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_interval_start",
            "time_interval_end",
            "analysis_time_interval",
            "host_type",
            "host_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_host_insight_top_processes_usage,
            compartment_id=self.module.params.get("compartment_id"),
            id=self.module.params.get("id"),
            resource_metric=self.module.params.get("resource_metric"),
            timestamp=self.module.params.get("timestamp"),
            **optional_kwargs
        )


SummarizeHostInsightsTopProcessesUsageFactsHelperCustom = get_custom_class(
    "SummarizeHostInsightsTopProcessesUsageFactsHelperCustom"
)


class ResourceFactsHelper(
    SummarizeHostInsightsTopProcessesUsageFactsHelperCustom,
    SummarizeHostInsightsTopProcessesUsageFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            id=dict(type="str", required=True),
            resource_metric=dict(type="str", required=True),
            timestamp=dict(type="str", required=True),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            analysis_time_interval=dict(type="str"),
            host_type=dict(type="list", elements="str"),
            host_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="summarize_host_insights_top_processes_usage",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(summarize_host_insights_top_processes_usages=result)


if __name__ == "__main__":
    main()
