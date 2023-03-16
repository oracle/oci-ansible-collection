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
module: oci_opsi_sql_insights_facts
short_description: Fetches details about a SqlInsights resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SqlInsights resource in Oracle Cloud Infrastructure
    - Query SQL Warehouse to get the performance insights for SQLs taking greater than X% database time for a given
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
    vmcluster_name:
        description:
            - Optional list of Exadata Insight VM cluster name.
        type: list
        elements: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List sql_insights
  oci_opsi_sql_insights_facts:
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
    analysis_time_interval: analysis_time_interval_example
    time_interval_start: 2013-10-20T19:20:30+01:00
    time_interval_end: 2013-10-20T19:20:30+01:00
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true
    vmcluster_name: [ "vmcluster_name_example" ]

"""

RETURN = """
sql_insights:
    description:
        - SqlInsights resource
    returned: on success
    type: complex
    contains:
        time_interval_start:
            description:
                - The start timestamp that was passed into the request.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_interval_end:
            description:
                - The end timestamp that was passed into the request.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        inventory:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                total_sqls:
                    description:
                        - Total number of sqls. Example `2000`
                    returned: on success
                    type: int
                    sample: 56
                total_databases:
                    description:
                        - Total number of Databases. Example `400`
                    returned: on success
                    type: int
                    sample: 56
                sqls_analyzed:
                    description:
                        - Total number of sqls analyzed by the query. Example `120`
                    returned: on success
                    type: int
                    sample: 56
        items:
            description:
                - List of insights.
            returned: on success
            type: complex
            contains:
                text:
                    description:
                        - Insight text.
                          For example `Degrading SQLs`, `Variant SQLs`,
                            `Inefficient SQLs`, `Improving SQLs`, `SQLs with Plan Changes`,
                            `Degrading SQLs have increasing IO Time above 50%`,
                            `Degrading SQLs are variant`,
                            `2 of the 2 variant SQLs have plan changes`,
                            `Inefficient SQLs have increasing CPU Time above 50%
                    returned: on success
                    type: str
                    sample: text_example
                values:
                    description:
                        - "SQL counts for a given insight. For example insight text `2 of 10 SQLs have degrading response time` will have values as [2,10]\\""
                    returned: on success
                    type: list
                    sample: []
                category:
                    description:
                        - Insight category. It would be one of the following
                          DEGRADING,
                          VARIANT,
                          INEFFICIENT,
                          CHANGING_PLANS,
                          IMPROVING,
                          DEGRADING_VARIANT,
                          DEGRADING_INEFFICIENT,
                          DEGRADING_CHANGING_PLANS,
                          DEGRADING_INCREASING_IO,
                          DEGRADING_INCREASING_CPU,
                          DEGRADING_INCREASING_INEFFICIENT_WAIT,
                          DEGRADING_CHANGING_PLANS_AND_INCREASING_IO,
                          DEGRADING_CHANGING_PLANS_AND_INCREASING_CPU,
                          DEGRADING_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT,VARIANT_INEFFICIENT,
                          VARIANT_CHANGING_PLANS,
                          VARIANT_INCREASING_IO,
                          VARIANT_INCREASING_CPU,
                          VARIANT_INCREASING_INEFFICIENT_WAIT,
                          VARIANT_CHANGING_PLANS_AND_INCREASING_IO,
                          VARIANT_CHANGING_PLANS_AND_INCREASING_CPU,
                          VARIANT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT,
                          INEFFICIENT_CHANGING_PLANS,
                          INEFFICIENT_INCREASING_INEFFICIENT_WAIT,
                          INEFFICIENT_CHANGING_PLANS_AND_INCREASING_INEFFICIENT_WAIT
                    returned: on success
                    type: str
                    sample: category_example
        thresholds:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                degradation_in_pct:
                    description:
                        - Degradation Percent Threshold is used to derive degrading SQLs.
                    returned: on success
                    type: int
                    sample: 56
                variability:
                    description:
                        - Variability Percent Threshold is used to derive variant SQLs.
                    returned: on success
                    type: float
                    sample: 3.4
                inefficiency_in_pct:
                    description:
                        - Inefficiency Percent Threshold is used to derive inefficient SQLs.
                    returned: on success
                    type: int
                    sample: 56
                increase_in_io_in_pct:
                    description:
                        - PctIncreaseInIO is used for deriving insights for SQLs which are degrading or
                          variant or inefficient. And these SQLs should also have increasing change in IO Time
                          beyond threshold. Insights are derived using linear regression.
                    returned: on success
                    type: int
                    sample: 56
                increase_in_cpu_in_pct:
                    description:
                        - PctIncreaseInCPU is used for deriving insights for SQLs which are degrading or
                          variant or inefficient. And these SQLs should also have increasing change in CPU Time
                          beyond threshold. Insights are derived using linear regression.
                    returned: on success
                    type: int
                    sample: 56
                increase_in_inefficient_wait_in_pct:
                    description:
                        - PctIncreaseInIO is used for deriving insights for SQLs which are degrading or
                          variant or inefficient. And these SQLs should also have increasing change in
                          Other Wait Time beyond threshold. Insights are derived using linear regression.
                    returned: on success
                    type: int
                    sample: 56
                improved_in_pct:
                    description:
                        - Improved Percent Threshold is used to derive improving SQLs.
                    returned: on success
                    type: int
                    sample: 56
    sample: {
        "time_interval_start": "2013-10-20T19:20:30+01:00",
        "time_interval_end": "2013-10-20T19:20:30+01:00",
        "inventory": {
            "total_sqls": 56,
            "total_databases": 56,
            "sqls_analyzed": 56
        },
        "items": [{
            "text": "text_example",
            "values": [],
            "category": "category_example"
        }],
        "thresholds": {
            "degradation_in_pct": 56,
            "variability": 3.4,
            "inefficiency_in_pct": 56,
            "increase_in_io_in_pct": 56,
            "increase_in_cpu_in_pct": 56,
            "increase_in_inefficient_wait_in_pct": 56,
            "improved_in_pct": 56
        }
    }
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


class SqlInsightsFactsHelperGen(OCIResourceFactsHelperBase):
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
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
            "vmcluster_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_sql_insights,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SqlInsightsFactsHelperCustom = get_custom_class("SqlInsightsFactsHelperCustom")


class ResourceFactsHelper(SqlInsightsFactsHelperCustom, SqlInsightsFactsHelperGen):
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
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
            vmcluster_name=dict(type="list", elements="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_insights=result)


if __name__ == "__main__":
    main()
