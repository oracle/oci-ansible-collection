#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_opsi_sql_statistics_time_series_facts
short_description: Fetches details about a SqlStatisticsTimeSeries resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SqlStatisticsTimeSeries resource in Oracle Cloud Infrastructure
    - Query SQL Warehouse to get the performance statistics time series for a given SQL across given databases for a given time period.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    sql_identifier:
        description:
            - "Unique SQL_ID for a SQL Statement.
              Example: `6rgjh9bjmy2s7`"
        type: str
        required: true
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
        type: list
    id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database insight resource.
        type: list
    host_name:
        description:
            - Filter by one or more hostname.
        type: list
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
    defined_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
    freeform_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
              The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
        type: list
    defined_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
              or \\"{namespace}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
    freeform_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
              The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for different tag names are interpreted as \\"AND\\"."
        type: list
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific sql_statistics_time_series
  oci_opsi_sql_statistics_time_series_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sql_identifier: 6rgjh9bjmy2s7

"""

RETURN = """
sql_statistics_time_series:
    description:
        - SqlStatisticsTimeSeries resource
    returned: on success
    type: complex
    contains:
        sql_identifier:
            description:
                - Unique SQL_ID for a SQL Statement.
            returned: on success
            type: string
            sample: sql_identifier_example
        time_interval_start:
            description:
                - The start timestamp that was passed into the request.
            returned: on success
            type: string
            sample: 2020-12-06T00:00:00.000Z
        time_interval_end:
            description:
                - The end timestamp that was passed into the request.
            returned: on success
            type: string
            sample: 2020-12-06T00:00:00.000Z
        item_duration_in_ms:
            description:
                - Time duration in milliseconds between data points (one hour or one day).
            returned: on success
            type: int
            sample: 86400000
        end_timestamps:
            description:
                - Array comprising of all the sampling period end timestamps in RFC 3339 format.
            returned: on success
            type: list
            sample: []
        items:
            description:
                - Array of SQL performance statistics across databases.
            returned: on success
            type: complex
            contains:
                database_details:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database insight resource.
                            returned: on success
                            type: string
                            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                        database_id:
                            description:
                                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
                            returned: on success
                            type: string
                            sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
                        database_name:
                            description:
                                - The database name. The database name is unique within the tenancy.
                            returned: on success
                            type: string
                            sample: database_name_example
                        database_display_name:
                            description:
                                - The user-friendly name for the database. The name does not have to be unique.
                            returned: on success
                            type: string
                            sample: database_display_name_example
                        database_type:
                            description:
                                - Operations Insights internal representation of the database type.
                            returned: on success
                            type: string
                            sample: database_type_example
                        database_version:
                            description:
                                - The version of the database.
                            returned: on success
                            type: string
                            sample: database_version_example
                        instances:
                            description:
                                - Array of hostname and instance name.
                            returned: on success
                            type: complex
                            contains:
                                host_name:
                                    description:
                                        - The hostname of the database insight resource.
                                    returned: on success
                                    type: string
                                    sample: host_name_example
                                instance_name:
                                    description:
                                        - The instance name of the database insight resource.
                                    returned: on success
                                    type: string
                                    sample: instance_name_example
                statistics:
                    description:
                        - SQL performance statistics for a given database
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - SQL performance statistic name
                            returned: on success
                            type: string
                            sample: name_example
                        values:
                            description:
                                - SQL performance statistic value
                            returned: on success
                            type: list
                            sample: []
    sample: {
        "sql_identifier": "sql_identifier_example",
        "time_interval_start": "2020-12-06T00:00:00.000Z",
        "time_interval_end": "2020-12-06T00:00:00.000Z",
        "item_duration_in_ms": 86400000,
        "end_timestamps": [],
        "items": [{
            "database_details": {
                "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
                "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
                "database_name": "database_name_example",
                "database_display_name": "database_display_name_example",
                "database_type": "database_type_example",
                "database_version": "database_version_example",
                "instances": [{
                    "host_name": "host_name_example",
                    "instance_name": "instance_name_example"
                }]
            },
            "statistics": [{
                "name": "name_example",
                "values": []
            }]
        }]
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


class SqlStatisticsTimeSeriesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
            "sql_identifier",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "database_id",
            "id",
            "host_name",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.summarize_sql_statistics_time_series,
            compartment_id=self.module.params.get("compartment_id"),
            sql_identifier=self.module.params.get("sql_identifier"),
            **optional_kwargs
        )


SqlStatisticsTimeSeriesFactsHelperCustom = get_custom_class(
    "SqlStatisticsTimeSeriesFactsHelperCustom"
)


class ResourceFactsHelper(
    SqlStatisticsTimeSeriesFactsHelperCustom, SqlStatisticsTimeSeriesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sql_identifier=dict(type="str", required=True),
            database_id=dict(type="list"),
            id=dict(type="list"),
            host_name=dict(type="list"),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            defined_tag_equals=dict(type="list"),
            freeform_tag_equals=dict(type="list"),
            defined_tag_exists=dict(type="list"),
            freeform_tag_exists=dict(type="list"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_statistics_time_series",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_statistics_time_series=result)


if __name__ == "__main__":
    main()
