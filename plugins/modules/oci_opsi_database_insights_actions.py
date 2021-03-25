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
module: oci_opsi_database_insights_actions
short_description: Perform actions on a DatabaseInsights resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a DatabaseInsights resource in Oracle Cloud Infrastructure
    - For I(action=ingest_sql_bucket), the sqlbucket endpoint takes in a JSON payload, persists it in Operations Insights ingest pipeline.
    - For I(action=ingest_sql_plan_lines), the SqlPlanLines endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
    - "For I(action=ingest_sql_text), the SqlText endpoint takes in a JSON payload, persists it in Operation Insights ingest pipeline.
      Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should be masked prior
      to ingestion."
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
    items:
        description:
            - List of SQL Bucket Metric Entries.
        type: list
        suboptions:
            version:
                description:
                    - "Version
                      Example: `1`"
                type: float
            database_type:
                description:
                    - Operations Insights internal representation of the database type.
                type: str
            time_collected:
                description:
                    - "Collection timestamp
                      Example: `\\"2020-03-31T00:00:00.000Z\\"`"
                type: str
                required: true
            sql_identifier:
                description:
                    - Unique SQL_ID for a SQL Statement.
                type: str
                required: true
            plan_hash:
                description:
                    - Plan hash value for the SQL Execution Plan
                type: int
            bucket_id:
                description:
                    - "SQL Bucket ID, examples <= 3 secs, 3-10 secs, 10-60 secs, 1-5 min, > 5 min
                      Example: `\\"<= 3 secs\\"`"
                type: str
            executions_count:
                description:
                    - "Total number of executions
                      Example: `60`"
                type: int
            cpu_time_in_sec:
                description:
                    - "Total CPU time
                      Example: `1046`"
                type: float
            io_time_in_sec:
                description:
                    - "Total IO time
                      Example: `5810`"
                type: float
            other_wait_time_in_sec:
                description:
                    - "Total other wait time
                      Example: `24061`"
                type: float
            total_time_in_sec:
                description:
                    - "Total time
                      Example: `30917`"
                type: float
            operation:
                description:
                    - "Operation
                      Example: `\\"SELECT STATEMENT\\"`"
                type: str
            remark:
                description:
                    - "Remark
                      Example: `\\"\\"`"
                type: str
            options:
                description:
                    - "Options
                      Example: `\\"RANGE SCAN\\"`"
                type: str
            object_node:
                description:
                    - "Object Node
                      Example: `\\"Q4000\\"`"
                type: str
            object_owner:
                description:
                    - "Object Owner
                      Example: `\\"TENANT_A#SCHEMA\\"`"
                type: str
            object_name:
                description:
                    - "Object Name
                      Example: `\\"PLAN_LINES_PK\\"`"
                type: str
            object_alias:
                description:
                    - "Object Alias
                      Example: `\\"PLAN_LINES@SEL$1\\"`"
                type: str
            object_instance:
                description:
                    - "Object Instance
                      Example: `37472`"
                type: int
            object_type:
                description:
                    - "Object Type
                      Example: `\\"INDEX (UNIQUE)\\"`"
                type: str
            optimizer:
                description:
                    - "Optimizer
                      Example: `\\"CLUSTER\\"`"
                type: str
            search_columns:
                description:
                    - "Search Columns
                      Example: `3`"
                type: int
            identifier:
                description:
                    - "Identifier
                      Example: `3`"
                type: int
            parent_identifier:
                description:
                    - "Parent Identifier
                      Example: `2`"
                type: int
            depth:
                description:
                    - "Depth
                      Example: `3`"
                type: int
            position:
                description:
                    - "Position
                      Example: `1`"
                type: int
            cost:
                description:
                    - "Cost
                      Example: `1`"
                type: int
            cardinality:
                description:
                    - "Cardinality
                      Example: `1`"
                type: int
            bytes:
                description:
                    - "Bytes
                      Example: `150`"
                type: int
            other:
                description:
                    - "Other
                      Example: ``"
                type: str
            other_tag:
                description:
                    - "Other Tag
                      Example: `\\"PARALLEL_COMBINED_WITH_PARENT\\"`"
                type: str
            partition_start:
                description:
                    - "Partition start
                      Example: `1`"
                type: str
            partition_stop:
                description:
                    - "Partition stop
                      Example: `2`"
                type: str
            partition_identifier:
                description:
                    - "Partition identifier
                      Example: `8`"
                type: int
            distribution:
                description:
                    - "Distribution
                      Example: `\\"QC (RANDOM)\\"`"
                type: str
            cpu_cost:
                description:
                    - "CPU cost
                      Example: `7321`"
                type: int
            io_cost:
                description:
                    - "IO cost
                      Example: `1`"
                type: int
            temp_space:
                description:
                    - "Time space
                      Example: `15614000`"
                type: int
            access_predicates:
                description:
                    - "Access predicates
                      Example: `\\"\\\\\\"RESOURCE_ID\\\\\\"=:1 AND \\\\\\"QUERY_ID\\\\\\"=:2\\"`"
                type: str
            filter_predicates:
                description:
                    - "Filter predicates
                      Example: `\\"(INTERNAL_FUNCTION(\\\\\\"J\\\\\\".\\\\\\"DATABASE_ROLE\\\\\\") OR (\\\\\\"J\\\\\\".\\\\\\"DATABASE_ROLE\\\\\\" IS NULL AND
                      SYS_CONTEXT('userenv','database_role')='PRIMARY'))\\"`"
                type: str
            projection:
                description:
                    - "Projection
                      Example: `\\"COUNT(*)[22]\\"`"
                type: str
            qblock_name:
                description:
                    - "Qblock Name
                      Example: `\\"SEL$1\\"`"
                type: str
            elapsed_time_in_sec:
                description:
                    - "Total elapsed time
                      Example: `1.2`"
                type: float
            other_xml:
                description:
                    - "Other SQL
                      Example: `\\"<other_xml><info type=\\\\\\"db_version\\\\\\">18.0.0.0</info><info
                      type=\\\\\\"parse_schema\\\\\\"><![CDATA[\\\\\\"SYS\\\\\\"]]></info><info type=\\\\\\"plan_hash_full\\\\\\">483892784</info><info
                      type=\\\\\\"plan_hash\\\\\\">2709293936</info><info type=\\\\\\"plan_hash_2\\\\\\">483892784</info><outline_data><hint><![CDATA[IGNORE_OPT
                      IM_EMBEDDED_HINTS]]></hint><hint><![CDATA[OPTIMIZER_FEATURES_ENABLE('18.1.0')]]></hint><hint><![CDATA[DB_VERSION('18.1.0')]]></hint><hint>
                      <![CDATA[OPT_PARAM('_b_tree_bitmap_plans' 'false')]]></hint><hint><![CDATA[OPT_PARAM('_optim_peek_user_binds'
                      'false')]]></hint><hint><![CDATA[OPT_PARAM('result_cache_mode' 'FORCE')]]></hint><hint><![CDATA[OPT_PARAM('_fix_control' '20648883:0
                      27745220:1 30001331:1 30142527:1
                      30539126:1')]]></hint><hint><![CDATA[OUTLINE_LEAF(@\\\\\\"SEL$1\\\\\\")]]></hint><hint><![CDATA[INDEX(@\\\\\\"SEL$1\\\\\\"
                      \\\\\\"USER$\\\\\\"@\\\\\\"SEL$1\\\\\\" \\\\\\"I_USER#\\\\\\")]]></hint></outline_data></other_xml>\\"`"
                type: str
            sql_command:
                description:
                    - "SQL command
                      Example: `\\"SELECT\\"`"
                type: str
            exact_matching_signature:
                description:
                    - "Exact matching signature
                      Example: `\\"18067345456756876713\\"`"
                type: str
            force_matching_signature:
                description:
                    - "Force matching signature
                      Example: `\\"18067345456756876713\\"`"
                type: str
            sql_full_text:
                description:
                    - "Full SQL Text
                      Example: `\\"SELECT username,profile,default_tablespace,temporary_tablespace FROM dba_users\\"`
                      Disclaimer: SQL text being uploaded explicitly via APIs is not masked. Any sensitive literals contained in the sqlFullText column should
                      be masked prior to ingestion."
                type: str
    action:
        description:
            - The action to perform on the DatabaseInsights.
        type: str
        required: true
        choices:
            - "ingest_sql_bucket"
            - "ingest_sql_plan_lines"
            - "ingest_sql_text"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action ingest_sql_bucket on database_insights
  oci_opsi_database_insights_actions:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: ingest_sql_bucket

- name: Perform action ingest_sql_plan_lines on database_insights
  oci_opsi_database_insights_actions:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: ingest_sql_plan_lines

- name: Perform action ingest_sql_text on database_insights
  oci_opsi_database_insights_actions:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    action: ingest_sql_text

"""

RETURN = """
database_insights:
    description:
        - Details of the DatabaseInsights resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        message:
            description:
                - Success message returned as a result of the upload.
            returned: on success
            type: string
            sample: message_example
    sample: {
        "message": "message_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient
    from oci.opsi.models import IngestSqlBucketDetails
    from oci.opsi.models import IngestSqlPlanLinesDetails
    from oci.opsi.models import IngestSqlTextDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DatabaseInsightsActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        ingest_sql_bucket
        ingest_sql_plan_lines
        ingest_sql_text
    """

    def ingest_sql_bucket(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlBucketDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_bucket,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                ingest_sql_bucket_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def ingest_sql_plan_lines(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlPlanLinesDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_plan_lines,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                ingest_sql_plan_lines_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def ingest_sql_text(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, IngestSqlTextDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ingest_sql_text,
            call_fn_args=(),
            call_fn_kwargs=dict(
                compartment_id=self.module.params.get("compartment_id"),
                database_id=self.module.params.get("database_id"),
                ingest_sql_text_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


DatabaseInsightsActionsHelperCustom = get_custom_class(
    "DatabaseInsightsActionsHelperCustom"
)


class ResourceHelper(
    DatabaseInsightsActionsHelperCustom, DatabaseInsightsActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_id=dict(type="str", required=True),
            items=dict(
                type="list",
                elements="dict",
                options=dict(
                    version=dict(type="float"),
                    database_type=dict(type="str"),
                    time_collected=dict(type="str", required=True),
                    sql_identifier=dict(type="str", required=True),
                    plan_hash=dict(type="int"),
                    bucket_id=dict(type="str"),
                    executions_count=dict(type="int"),
                    cpu_time_in_sec=dict(type="float"),
                    io_time_in_sec=dict(type="float"),
                    other_wait_time_in_sec=dict(type="float"),
                    total_time_in_sec=dict(type="float"),
                    operation=dict(type="str"),
                    remark=dict(type="str"),
                    options=dict(type="str"),
                    object_node=dict(type="str"),
                    object_owner=dict(type="str"),
                    object_name=dict(type="str"),
                    object_alias=dict(type="str"),
                    object_instance=dict(type="int"),
                    object_type=dict(type="str"),
                    optimizer=dict(type="str"),
                    search_columns=dict(type="int"),
                    identifier=dict(type="int"),
                    parent_identifier=dict(type="int"),
                    depth=dict(type="int"),
                    position=dict(type="int"),
                    cost=dict(type="int"),
                    cardinality=dict(type="int"),
                    bytes=dict(type="int"),
                    other=dict(type="str"),
                    other_tag=dict(type="str"),
                    partition_start=dict(type="str"),
                    partition_stop=dict(type="str"),
                    partition_identifier=dict(type="int"),
                    distribution=dict(type="str"),
                    cpu_cost=dict(type="int"),
                    io_cost=dict(type="int"),
                    temp_space=dict(type="int"),
                    access_predicates=dict(type="str"),
                    filter_predicates=dict(type="str"),
                    projection=dict(type="str"),
                    qblock_name=dict(type="str"),
                    elapsed_time_in_sec=dict(type="float"),
                    other_xml=dict(type="str"),
                    sql_command=dict(type="str"),
                    exact_matching_signature=dict(type="str"),
                    force_matching_signature=dict(type="str"),
                    sql_full_text=dict(type="str"),
                ),
            ),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "ingest_sql_bucket",
                    "ingest_sql_plan_lines",
                    "ingest_sql_text",
                ],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="database_insights",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
