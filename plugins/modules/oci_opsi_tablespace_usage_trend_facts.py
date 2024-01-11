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
module: oci_opsi_tablespace_usage_trend_facts
short_description: Fetches details about one or multiple TablespaceUsageTrend resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TablespaceUsageTrend resources in Oracle Cloud Infrastructure
    - Returns response with usage time series data (endTimestamp, usage, capacity) with breakdown by tablespaceName for the time period specified.
      The maximum time range for analysis is 2 years, hence this is intentionally not paginated.
      Either databaseId or id must be specified.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    analysis_time_interval:
        description:
            - Specify time period in ISO 8601 format with respect to current time.
              Default is last 30 days represented by P30D.
              If timeInterval is specified, then timeIntervalStart and timeIntervalEnd will be ignored.
              Examples  P90D (last 90 days), P4W (last 4 weeks), P2M (last 2 months), P1Y (last 12 months), . Maximum value allowed is 25 months prior to
              current time (P25M).
        type: str
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
    database_id:
        description:
            - Optional L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
        type: str
    id:
        description:
            - L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database insight resource.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List tablespace_usage_trends
  oci_opsi_tablespace_usage_trend_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
tablespace_usage_trends:
    description:
        - List of TablespaceUsageTrend resources
    returned: on success
    type: complex
    contains:
        tablespace_name:
            description:
                - The name of tablespace.
            returned: on success
            type: str
            sample: tablespace_name_example
        tablespace_type:
            description:
                - Type of tablespace
            returned: on success
            type: str
            sample: tablespace_type_example
        usage_data:
            description:
                - List of usage data samples for a tablespace
            returned: on success
            type: complex
            contains:
                end_timestamp:
                    description:
                        - The timestamp in which the current sampling period ends in RFC 3339 format.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                usage:
                    description:
                        - Total amount used of the resource metric type (CPU, STORAGE).
                    returned: on success
                    type: float
                    sample: 1.2
                capacity:
                    description:
                        - The maximum allocated amount of the resource metric type  (CPU, STORAGE) for a set of databases.
                    returned: on success
                    type: float
                    sample: 1.2
    sample: [{
        "tablespace_name": "tablespace_name_example",
        "tablespace_type": "tablespace_type_example",
        "usage_data": [{
            "end_timestamp": "2013-10-20T19:20:30+01:00",
            "usage": 1.2,
            "capacity": 1.2
        }]
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


class TablespaceUsageTrendFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "database_id",
            "id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_database_insight_tablespace_usage_trend,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TablespaceUsageTrendFactsHelperCustom = get_custom_class(
    "TablespaceUsageTrendFactsHelperCustom"
)


class ResourceFactsHelper(
    TablespaceUsageTrendFactsHelperCustom, TablespaceUsageTrendFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            database_id=dict(type="str"),
            id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tablespace_usage_trend",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(tablespace_usage_trends=result)


if __name__ == "__main__":
    main()
