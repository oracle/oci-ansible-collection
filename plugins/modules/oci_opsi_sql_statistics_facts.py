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
module: oci_opsi_sql_statistics_facts
short_description: Fetches details about one or multiple SqlStatistics resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SqlStatistics resources in Oracle Cloud Infrastructure
    - Query SQL Warehouse to get the performance statistics for SQLs taking greater than X% database time for a given
      time period across the given databases or database types in a compartment and in all sub-compartments if specified.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    database_type:
        description:
            - Filter by one or more database type.
              Possible values are ADW-S, ATP-S, ADW-D, ATP-D, EXTERNAL-PDB, EXTERNAL-NONCDB.
        type: list
        elements: str
        choices:
            - "ADW-S"
            - "ATP-S"
            - "ADW-D"
            - "ATP-D"
            - "EXTERNAL-PDB"
            - "EXTERNAL-NONCDB"
            - "COMANAGED-VM-CDB"
            - "COMANAGED-VM-PDB"
            - "COMANAGED-VM-NONCDB"
            - "COMANAGED-BM-CDB"
            - "COMANAGED-BM-PDB"
            - "COMANAGED-BM-NONCDB"
            - "COMANAGED-EXACS-CDB"
            - "COMANAGED-EXACS-PDB"
            - "COMANAGED-EXACS-NONCDB"
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
        type: list
        elements: str
    id:
        description:
            - Optional list of database insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    exadata_insight_id:
        description:
            - Optional list of exadata insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    cdb_name:
        description:
            - Filter by one or more cdb name.
        type: list
        elements: str
    host_name:
        description:
            - Filter by one or more hostname.
        type: list
        elements: str
    database_time_pct_greater_than:
        description:
            - Filter sqls by percentage of db time.
        type: float
    sql_identifier:
        description:
            - "One or more unique SQL_IDs for a SQL Statement.
              Example: `6rgjh9bjmy2s7`"
        type: list
        elements: str
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
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - "The field to use when sorting SQL statistics.
              Example: databaseTimeInSec"
        type: str
        choices:
            - "databaseTimeInSec"
            - "executionsPerHour"
            - "executionsCount"
            - "cpuTimeInSec"
            - "ioTimeInSec"
            - "inefficientWaitTimeInSec"
            - "responseTimeInSec"
            - "planCount"
            - "variability"
            - "averageActiveSessions"
            - "databaseTimePct"
            - "inefficiencyInPct"
            - "changeInCpuTimeInPct"
            - "changeInIoTimeInPct"
            - "changeInInefficientWaitTimeInPct"
            - "changeInResponseTimeInPct"
            - "changeInAverageActiveSessionsInPct"
            - "changeInExecutionsPerHourInPct"
            - "changeInInefficiencyInPct"
    category:
        description:
            - Filter sqls by one or more performance categories.
        type: list
        elements: str
        choices:
            - "DEGRADING"
            - "VARIANT"
            - "INEFFICIENT"
            - "CHANGING_PLANS"
            - "IMPROVING"
            - "DEGRADING_VARIANT"
            - "DEGRADING_INEFFICIENT"
            - "DEGRADING_CHANGING_PLANS"
            - "DEGRADING_INCREASING_IO"
            - "DEGRADING_INCREASING_CPU"
            - "DEGRADING_INCREASING_INEFFICIENT_WAIT"
            - "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO"
            - "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU"
            - "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"
            - "VARIANT_INEFFICIENT"
            - "VARIANT_CHANGING_PLANS"
            - "VARIANT_INCREASING_IO"
            - "VARIANT_INCREASING_CPU"
            - "VARIANT_INCREASING_INEFFICIENT_WAIT"
            - "VARIANT_CHANGING_PLANS_AND_INCREASING_IO"
            - "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU"
            - "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"
            - "INEFFICIENT_CHANGING_PLANS"
            - "INEFFICIENT_INCREASING_INEFFICIENT_WAIT"
            - "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT"
    defined_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
              The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    defined_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
              or \\"{namespace}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
              The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    compartment_id_in_subtree:
        description:
            - A flag to search all resources within a given compartment and all sub-compartments.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List sql_statistics
  oci_opsi_sql_statistics_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_type: [ "ADW-S" ]
    database_id: [ "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx" ]
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    exadata_insight_id: [ "ocid1.exadatainsight.oc1..xxxxxxEXAMPLExxxxxx" ]
    cdb_name: [ "cdb_name_example" ]
    host_name: [ "host_name_example" ]
    database_time_pct_greater_than: 1.0
    sql_identifier: [ "sql_identifier_example" ]
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: databaseTimeInSec
    category: [ "DEGRADING" ]
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true

"""

RETURN = """
sql_statistics:
    description:
        - List of SqlStatistics resources
    returned: on success
    type: complex
    contains:
        sql_identifier:
            description:
                - Unique SQL_ID for a SQL Statement.
            returned: on success
            type: str
            sample: sql_identifier_example
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
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                database_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
                    returned: on success
                    type: str
                    sample: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
                compartment_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                database_name:
                    description:
                        - The database name. The database name is unique within the tenancy.
                    returned: on success
                    type: str
                    sample: database_name_example
                database_display_name:
                    description:
                        - The user-friendly name for the database. The name does not have to be unique.
                    returned: on success
                    type: str
                    sample: database_display_name_example
                database_type:
                    description:
                        - Operations Insights internal representation of the database type.
                    returned: on success
                    type: str
                    sample: database_type_example
                database_version:
                    description:
                        - The version of the database.
                    returned: on success
                    type: str
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
                            type: str
                            sample: host_name_example
                        instance_name:
                            description:
                                - The instance name of the database insight resource.
                            returned: on success
                            type: str
                            sample: instance_name_example
                cdb_name:
                    description:
                        - Name of the CDB.Only applies to PDB.
                    returned: on success
                    type: str
                    sample: cdb_name_example
        category:
            description:
                - SQL belongs to one or more categories based on the insights.
            returned: on success
            type: list
            sample: []
        statistics:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                database_time_in_sec:
                    description:
                        - Database Time in seconds
                    returned: on success
                    type: float
                    sample: 1.2
                executions_per_hour:
                    description:
                        - Number of executions per hour
                    returned: on success
                    type: float
                    sample: 1.2
                executions_count:
                    description:
                        - Total number of executions
                    returned: on success
                    type: int
                    sample: 56
                cpu_time_in_sec:
                    description:
                        - CPU Time in seconds
                    returned: on success
                    type: float
                    sample: 1.2
                io_time_in_sec:
                    description:
                        - I/O Time in seconds
                    returned: on success
                    type: float
                    sample: 1.2
                inefficient_wait_time_in_sec:
                    description:
                        - Inefficient Wait Time in seconds
                    returned: on success
                    type: float
                    sample: 1.2
                response_time_in_sec:
                    description:
                        - Response time is the average elaspsed time per execution. It is the ratio of Total Database Time to the number of executions
                    returned: on success
                    type: float
                    sample: 1.2
                plan_count:
                    description:
                        - Number of SQL execution plans used by the SQL
                    returned: on success
                    type: int
                    sample: 56
                variability:
                    description:
                        - Variability is the ratio of the standard deviation in response time to the mean of response time of the SQL
                    returned: on success
                    type: float
                    sample: 1.2
                average_active_sessions:
                    description:
                        - Average Active Sessions represent the average active sessions at a point in time. It is the number of sessions that are either working
                          or waiting.
                    returned: on success
                    type: float
                    sample: 1.2
                database_time_pct:
                    description:
                        - Percentage of Database Time
                    returned: on success
                    type: float
                    sample: 1.2
                inefficiency_in_pct:
                    description:
                        - Percentage of Inefficiency. It is calculated by Total Database Time divided by Total Wait Time
                    returned: on success
                    type: float
                    sample: 1.2
                change_in_cpu_time_in_pct:
                    description:
                        - Percent change in CPU Time based on linear regression
                    returned: on success
                    type: float
                    sample: 1.2
                change_in_io_time_in_pct:
                    description:
                        - Percent change in IO Time based on linear regression
                    returned: on success
                    type: float
                    sample: 1.2
                change_in_inefficient_wait_time_in_pct:
                    description:
                        - Percent change in Inefficient Wait Time based on linear regression
                    returned: on success
                    type: float
                    sample: 1.2
                change_in_response_time_in_pct:
                    description:
                        - Percent change in Response Time based on linear regression
                    returned: on success
                    type: float
                    sample: 1.2
                change_in_average_active_sessions_in_pct:
                    description:
                        - Percent change in Average Active Sessions based on linear regression
                    returned: on success
                    type: float
                    sample: 1.2
                change_in_executions_per_hour_in_pct:
                    description:
                        - Percent change in Executions per hour based on linear regression
                    returned: on success
                    type: float
                    sample: 1.2
                change_in_inefficiency_in_pct:
                    description:
                        - Percent change in Inefficiency based on linear regression
                    returned: on success
                    type: float
                    sample: 1.2
    sample: [{
        "sql_identifier": "sql_identifier_example",
        "database_details": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "database_id": "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx",
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "database_name": "database_name_example",
            "database_display_name": "database_display_name_example",
            "database_type": "database_type_example",
            "database_version": "database_version_example",
            "instances": [{
                "host_name": "host_name_example",
                "instance_name": "instance_name_example"
            }],
            "cdb_name": "cdb_name_example"
        },
        "category": [],
        "statistics": {
            "database_time_in_sec": 1.2,
            "executions_per_hour": 1.2,
            "executions_count": 56,
            "cpu_time_in_sec": 1.2,
            "io_time_in_sec": 1.2,
            "inefficient_wait_time_in_sec": 1.2,
            "response_time_in_sec": 1.2,
            "plan_count": 56,
            "variability": 1.2,
            "average_active_sessions": 1.2,
            "database_time_pct": 1.2,
            "inefficiency_in_pct": 1.2,
            "change_in_cpu_time_in_pct": 1.2,
            "change_in_io_time_in_pct": 1.2,
            "change_in_inefficient_wait_time_in_pct": 1.2,
            "change_in_response_time_in_pct": 1.2,
            "change_in_average_active_sessions_in_pct": 1.2,
            "change_in_executions_per_hour_in_pct": 1.2,
            "change_in_inefficiency_in_pct": 1.2
        }
    }]
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


class SqlStatisticsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "database_type",
            "database_id",
            "id",
            "exadata_insight_id",
            "cdb_name",
            "host_name",
            "database_time_pct_greater_than",
            "sql_identifier",
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "sort_order",
            "sort_by",
            "category",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_sql_statistics,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SqlStatisticsFactsHelperCustom = get_custom_class("SqlStatisticsFactsHelperCustom")


class ResourceFactsHelper(SqlStatisticsFactsHelperCustom, SqlStatisticsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_type=dict(
                type="list",
                elements="str",
                choices=[
                    "ADW-S",
                    "ATP-S",
                    "ADW-D",
                    "ATP-D",
                    "EXTERNAL-PDB",
                    "EXTERNAL-NONCDB",
                    "COMANAGED-VM-CDB",
                    "COMANAGED-VM-PDB",
                    "COMANAGED-VM-NONCDB",
                    "COMANAGED-BM-CDB",
                    "COMANAGED-BM-PDB",
                    "COMANAGED-BM-NONCDB",
                    "COMANAGED-EXACS-CDB",
                    "COMANAGED-EXACS-PDB",
                    "COMANAGED-EXACS-NONCDB",
                ],
            ),
            database_id=dict(type="list", elements="str"),
            id=dict(type="list", elements="str"),
            exadata_insight_id=dict(type="list", elements="str"),
            cdb_name=dict(type="list", elements="str"),
            host_name=dict(type="list", elements="str"),
            database_time_pct_greater_than=dict(type="float"),
            sql_identifier=dict(type="list", elements="str"),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str",
                choices=[
                    "databaseTimeInSec",
                    "executionsPerHour",
                    "executionsCount",
                    "cpuTimeInSec",
                    "ioTimeInSec",
                    "inefficientWaitTimeInSec",
                    "responseTimeInSec",
                    "planCount",
                    "variability",
                    "averageActiveSessions",
                    "databaseTimePct",
                    "inefficiencyInPct",
                    "changeInCpuTimeInPct",
                    "changeInIoTimeInPct",
                    "changeInInefficientWaitTimeInPct",
                    "changeInResponseTimeInPct",
                    "changeInAverageActiveSessionsInPct",
                    "changeInExecutionsPerHourInPct",
                    "changeInInefficiencyInPct",
                ],
            ),
            category=dict(
                type="list",
                elements="str",
                choices=[
                    "DEGRADING",
                    "VARIANT",
                    "INEFFICIENT",
                    "CHANGING_PLANS",
                    "IMPROVING",
                    "DEGRADING_VARIANT",
                    "DEGRADING_INEFFICIENT",
                    "DEGRADING_CHANGING_PLANS",
                    "DEGRADING_INCREASING_IO",
                    "DEGRADING_INCREASING_CPU",
                    "DEGRADING_INCREASING_INEFFICIENT_WAIT",
                    "DEGRADING_CHANGING_PLANS_AND_INCREASING_IO",
                    "DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU",
                    "DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT",
                    "VARIANT_INEFFICIENT",
                    "VARIANT_CHANGING_PLANS",
                    "VARIANT_INCREASING_IO",
                    "VARIANT_INCREASING_CPU",
                    "VARIANT_INCREASING_INEFFICIENT_WAIT",
                    "VARIANT_CHANGING_PLANS_AND_INCREASING_IO",
                    "VARIANT_CHANGING_PLANS_AND_INCREASING_CPU",
                    "VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT",
                    "INEFFICIENT_CHANGING_PLANS",
                    "INEFFICIENT_INCREASING_INEFFICIENT_WAIT",
                    "INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT",
                ],
            ),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_statistics",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_statistics=result)


if __name__ == "__main__":
    main()
