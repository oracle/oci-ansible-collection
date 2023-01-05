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
module: oci_opsi_awr_database_sql_report_facts
short_description: Fetches details about a AwrDatabaseSqlReport resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AwrDatabaseSqlReport resource in Oracle Cloud Infrastructure
    - Gets the SQL health check report for one SQL of the specified database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    awr_hub_id:
        description:
            - Unique Awr Hub identifier
        type: str
        aliases: ["id"]
        required: true
    awr_source_database_identifier:
        description:
            - "The internal ID of the database. The internal ID of the database is not the
              L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
              It can be retrieved from the following endpoint:
              /awrHubs/{awrHubId}/awrDatabases"
        type: str
        required: true
    sql_id:
        description:
            - The parameter to filter SQL by ID. Note that the SQL ID is generated internally by Oracle for each SQL statement and can be retrieved from AWR
              Report API (/awrHubs/{awrHubId}/awrDbReport).
        type: str
        required: true
    instance_number:
        description:
            - The optional single value query parameter to filter by database instance number.
        type: str
    begin_snapshot_identifier_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to filter on the snapshot ID.
        type: int
    end_snapshot_identifier_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the snapshot Identifier.
        type: int
    time_greater_than_or_equal_to:
        description:
            - "The optional greater than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ,
              example 2020-12-03T19:00:53Z"
        type: str
    time_less_than_or_equal_to:
        description:
            - "The optional less than or equal to query parameter to filter the timestamp. The timestamp format to be followed is: YYYY-MM-DDTHH:MM:SSZ, example
              2020-12-03T19:00:53Z"
        type: str
    report_format:
        description:
            - The format of the AWR report.
        type: str
        choices:
            - "HTML"
            - "TEXT"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific awr_database_sql_report
  oci_opsi_awr_database_sql_report_facts:
    # required
    awr_hub_id: "ocid1.awrhub.oc1..xxxxxxEXAMPLExxxxxx"
    awr_source_database_identifier: awr_source_database_identifier_example
    sql_id: "ocid1.sql.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    instance_number: instance_number_example
    begin_snapshot_identifier_greater_than_or_equal_to: 56
    end_snapshot_identifier_less_than_or_equal_to: 56
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    report_format: HTML

"""

RETURN = """
awr_database_sql_report:
    description:
        - AwrDatabaseSqlReport resource
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the query result.
            returned: on success
            type: str
            sample: name_example
        version:
            description:
                - The version of the query result.
            returned: on success
            type: str
            sample: version_example
        db_query_time_in_secs:
            description:
                - The time taken to query the database tier (in seconds).
            returned: on success
            type: float
            sample: 1.2
        awr_result_type:
            description:
                - The result type of AWR query.
            returned: on success
            type: str
            sample: AWRDB_SET
        content:
            description:
                - The content of the report.
            returned: on success
            type: str
            sample: content_example
        format:
            description:
                - The format of the report.
            returned: on success
            type: str
            sample: HTML
    sample: {
        "name": "name_example",
        "version": "version_example",
        "db_query_time_in_secs": 1.2,
        "awr_result_type": "AWRDB_SET",
        "content": "content_example",
        "format": "HTML"
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


class AwrDatabaseSqlReportFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "awr_hub_id",
            "awr_source_database_identifier",
            "sql_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "instance_number",
            "begin_snapshot_identifier_greater_than_or_equal_to",
            "end_snapshot_identifier_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "report_format",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_awr_database_sql_report,
            awr_hub_id=self.module.params.get("awr_hub_id"),
            awr_source_database_identifier=self.module.params.get(
                "awr_source_database_identifier"
            ),
            sql_id=self.module.params.get("sql_id"),
            **optional_kwargs
        )


AwrDatabaseSqlReportFactsHelperCustom = get_custom_class(
    "AwrDatabaseSqlReportFactsHelperCustom"
)


class ResourceFactsHelper(
    AwrDatabaseSqlReportFactsHelperCustom, AwrDatabaseSqlReportFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            awr_hub_id=dict(aliases=["id"], type="str", required=True),
            awr_source_database_identifier=dict(type="str", required=True),
            sql_id=dict(type="str", required=True),
            instance_number=dict(type="str"),
            begin_snapshot_identifier_greater_than_or_equal_to=dict(type="int"),
            end_snapshot_identifier_less_than_or_equal_to=dict(type="int"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            report_format=dict(type="str", choices=["HTML", "TEXT"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_database_sql_report",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_database_sql_report=result)


if __name__ == "__main__":
    main()
