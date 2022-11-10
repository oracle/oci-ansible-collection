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
module: oci_mysql_analytics_cluster_memory_estimate_actions
short_description: Perform actions on an AnalyticsClusterMemoryEstimate resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AnalyticsClusterMemoryEstimate resource in Oracle Cloud Infrastructure
    - "For I(action=generate), dEPRECATED -- please use HeatWave API instead.
      Sends a request to estimate the memory footprints of user tables when loaded to Analytics Cluster memory."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    db_system_id:
        description:
            - The DB System L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the AnalyticsClusterMemoryEstimate.
        type: str
        required: true
        choices:
            - "generate"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action generate on analytics_cluster_memory_estimate
  oci_mysql_analytics_cluster_memory_estimate_actions:
    # required
    db_system_id: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
    action: generate

"""

RETURN = """
analytics_cluster_memory_estimate:
    description:
        - Details of the AnalyticsClusterMemoryEstimate resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        db_system_id:
            description:
                - The OCID of the DB System the Analytics Cluster memory estimate is associated with.
            returned: on success
            type: str
            sample: "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - Current status of the Work Request generating the Analytics Cluster memory estimate.
            returned: on success
            type: str
            sample: ACCEPTED
        time_created:
            description:
                - The date and time that the Work Request to generate the Analytics Cluster memory estimate was issued, as described by L(RFC
                  3339,https://tools.ietf.org/rfc/rfc333).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time that the Analytics Cluster memory estimate was generated, as described by L(RFC 3339,https://tools.ietf.org/rfc/rfc333).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        table_schemas:
            description:
                - Collection of schemas with estimated memory footprints for MySQL user tables of each schema
                  when loaded to Analytics Cluster memory.
            returned: on success
            type: complex
            contains:
                schema_name:
                    description:
                        - The name of the schema.
                    returned: on success
                    type: str
                    sample: schema_name_example
                per_table_estimates:
                    description:
                        - Estimated memory footprints for MySQL user tables of the schema
                          when loaded to Analytics Cluster memory.
                    returned: on success
                    type: complex
                    contains:
                        table_name:
                            description:
                                - The table name.
                            returned: on success
                            type: str
                            sample: table_name_example
                        to_load_column_count:
                            description:
                                - The number of columns to be loaded to Analytics Cluster memory.
                                  These columns contribute to the analytical memory footprint.
                            returned: on success
                            type: int
                            sample: 56
                        varlen_column_count:
                            description:
                                - The number of variable-length columns to be loaded to Analytics Cluster memory.
                                  These columns contribute to the analytical memory footprint.
                            returned: on success
                            type: int
                            sample: 56
                        estimated_row_count:
                            description:
                                - The estimated number of rows in the table. This number was used to
                                  derive the analytical memory footprint.
                            returned: on success
                            type: int
                            sample: 56
                        analytical_footprint_in_mbs:
                            description:
                                - The estimated memory footprint of the table in MBs when loaded to
                                  Analytics Cluster memory (null if the table cannot be loaded to the
                                  Analytics Cluster).
                            returned: on success
                            type: int
                            sample: 56
                        error_comment:
                            description:
                                - Error comment (empty string if no errors occured).
                            returned: on success
                            type: str
                            sample: error_comment_example
    sample: {
        "db_system_id": "ocid1.dbsystem.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "ACCEPTED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "table_schemas": [{
            "schema_name": "schema_name_example",
            "per_table_estimates": [{
                "table_name": "table_name_example",
                "to_load_column_count": 56,
                "varlen_column_count": 56,
                "estimated_row_count": 56,
                "analytical_footprint_in_mbs": 56,
                "error_comment": "error_comment_example"
            }]
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.mysql import WorkRequestsClient
    from oci.mysql import DbSystemClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MysqlAnalyticsClusterMemoryEstimateActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        generate
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestsClient)

    @staticmethod
    def get_module_resource_id_param():
        return "db_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("db_system_id")

    def get_get_fn(self):
        return self.client.get_analytics_cluster_memory_estimate

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_analytics_cluster_memory_estimate,
            db_system_id=self.module.params.get("db_system_id"),
        )

    def generate(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_analytics_cluster_memory_estimate,
            call_fn_args=(),
            call_fn_kwargs=dict(db_system_id=self.module.params.get("db_system_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


MysqlAnalyticsClusterMemoryEstimateActionsHelperCustom = get_custom_class(
    "MysqlAnalyticsClusterMemoryEstimateActionsHelperCustom"
)


class ResourceHelper(
    MysqlAnalyticsClusterMemoryEstimateActionsHelperCustom,
    MysqlAnalyticsClusterMemoryEstimateActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            db_system_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["generate"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="analytics_cluster_memory_estimate",
        service_client_class=DbSystemClient,
        namespace="mysql",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
