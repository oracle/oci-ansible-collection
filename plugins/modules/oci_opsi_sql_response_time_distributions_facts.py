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
module: oci_opsi_sql_response_time_distributions_facts
short_description: Fetches details about a SqlResponseTimeDistributions resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SqlResponseTimeDistributions resource in Oracle Cloud Infrastructure
    - Query SQL Warehouse to summarize the response time distribution of query executions for a given SQL for a given time period.
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    database_id:
        description:
            - Required L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the database.
        type: str
        required: true
    sql_identifier:
        description:
            - "Unique SQL_ID for a SQL Statement.
              Example: `6rgjh9bjmy2s7`"
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific sql_response_time_distributions
  oci_opsi_sql_response_time_distributions_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
    database_id: ocid1.database.oc1..xxxxxxEXAMPLExxxxxx
    sql_identifier: 6rgjh9bjmy2s7

"""

RETURN = """
sql_response_time_distributions:
    description:
        - SqlResponseTimeDistributions resource
    returned: on success
    type: complex
    contains:
        bucket_id:
            description:
                - Response time bucket id
            returned: on success
            type: string
            sample: ocid1.bucket.oc1..xxxxxxEXAMPLExxxxxx
        executions_count:
            description:
                - Total number of SQL executions
            returned: on success
            type: int
            sample: 56
    sample: {
        "bucket_id": "ocid1.bucket.oc1..xxxxxxEXAMPLExxxxxx",
        "executions_count": 56
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


class SqlResponseTimeDistributionsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
            "database_id",
            "sql_identifier",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "analysis_time_interval",
            "time_interval_start",
            "time_interval_end",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.summarize_sql_response_time_distributions,
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                sql_identifier=self.module.params.get("sql_identifier"),
                **optional_kwargs
            )
        )


SqlResponseTimeDistributionsFactsHelperCustom = get_custom_class(
    "SqlResponseTimeDistributionsFactsHelperCustom"
)


class ResourceFactsHelper(
    SqlResponseTimeDistributionsFactsHelperCustom,
    SqlResponseTimeDistributionsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_id=dict(type="str", required=True),
            sql_identifier=dict(type="str", required=True),
            analysis_time_interval=dict(type="str"),
            time_interval_start=dict(type="str"),
            time_interval_end=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_response_time_distributions",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_response_time_distributions=result)


if __name__ == "__main__":
    main()
