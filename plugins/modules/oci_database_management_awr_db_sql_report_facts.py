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
module: oci_database_management_awr_db_sql_report_facts
short_description: Fetches details about a AwrDbSqlReport resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AwrDbSqlReport resource in Oracle Cloud Infrastructure
    - Gets the SQL health check report for one SQL of the specific database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    awr_db_id:
        description:
            - "The parameter to filter the database by internal ID.
              Note that the internal ID of the database can be retrieved from the following endpoint:
              /managedDatabases/{managedDatabaseId}/awrDbs"
        type: str
        aliases: ["id"]
        required: true
    sql_id:
        description:
            - The parameter to filter SQL by ID. Note that the SQL ID is generated internally by Oracle for each SQL statement and can be retrieved from AWR
              Report API (/managedDatabases/{managedDatabaseId}/awrDbs/{awrDbId}/awrDbReport) or Performance Hub API
              (/internal/managedDatabases/{managedDatabaseId}/actions/retrievePerformanceData)
        type: str
        required: true
    inst_num:
        description:
            - The optional single value query parameter to filter the database instance number.
        type: str
    begin_sn_id_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to filter on the snapshot ID.
        type: int
    end_sn_id_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the snapshot ID.
        type: int
    time_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to query parameter to filter the timestamp.
        type: str
    time_less_than_or_equal_to:
        description:
            - The optional less than or equal to query parameter to filter the timestamp.
        type: str
    report_format:
        description:
            - The format of the AWR report.
        type: str
        choices:
            - "HTML"
            - "TEXT"
    container_id:
        description:
            - "The optional query parameter to filter the database container by an exact ID value.
              Note that the database container ID can be retrieved from the following endpoint:
              /managedDatabases/{managedDatabaseId}/awrDbSnapshotRanges"
        type: int
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific awr_db_sql_report
  oci_database_management_awr_db_sql_report_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    awr_db_id: "ocid1.awrdb.oc1..xxxxxxEXAMPLExxxxxx"
    sql_id: "ocid1.sql.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    inst_num: inst_num_example
    begin_sn_id_greater_than_or_equal_to: 56
    end_sn_id_less_than_or_equal_to: 56
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    report_format: HTML
    container_id: 56

"""

RETURN = """
awr_db_sql_report:
    description:
        - AwrDbSqlReport resource
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
        query_key:
            description:
                - The ID assigned to the query instance.
            returned: on success
            type: str
            sample: query_key_example
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
        "query_key": "query_key_example",
        "db_query_time_in_secs": 1.2,
        "awr_result_type": "AWRDB_SET",
        "content": "content_example",
        "format": "HTML"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AwrDbSqlReportFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "managed_database_id",
            "awr_db_id",
            "sql_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "inst_num",
            "begin_sn_id_greater_than_or_equal_to",
            "end_sn_id_less_than_or_equal_to",
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "report_format",
            "container_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_awr_db_sql_report,
            managed_database_id=self.module.params.get("managed_database_id"),
            awr_db_id=self.module.params.get("awr_db_id"),
            sql_id=self.module.params.get("sql_id"),
            **optional_kwargs
        )


AwrDbSqlReportFactsHelperCustom = get_custom_class("AwrDbSqlReportFactsHelperCustom")


class ResourceFactsHelper(
    AwrDbSqlReportFactsHelperCustom, AwrDbSqlReportFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            awr_db_id=dict(aliases=["id"], type="str", required=True),
            sql_id=dict(type="str", required=True),
            inst_num=dict(type="str"),
            begin_sn_id_greater_than_or_equal_to=dict(type="int"),
            end_sn_id_less_than_or_equal_to=dict(type="int"),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            report_format=dict(type="str", choices=["HTML", "TEXT"]),
            container_id=dict(type="int"),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="awr_db_sql_report",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(awr_db_sql_report=result)


if __name__ == "__main__":
    main()
