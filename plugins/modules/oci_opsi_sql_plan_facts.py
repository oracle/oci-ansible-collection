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
module: oci_opsi_sql_plan_facts
short_description: Fetches details about one or multiple SqlPlan resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SqlPlan resources in Oracle Cloud Infrastructure
    - Query SQL Warehouse to list the plan xml for a given SQL execution plan. This returns a SqlPlanCollection object, but is currently limited to a single
      plan.
      Either databaseId or id must be specified.
version_added: "2.9.0"
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
    plan_hash:
        description:
            - "Unique plan hash for a SQL Plan of a particular SQL Statement.
              Example: `9820154385`"
        type: list
        elements: int
        required: true
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
- name: List sql_plans
  oci_opsi_sql_plan_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sql_identifier: sql_identifier_example
    plan_hash: [ "56" ]

    # optional
    database_id: "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx"
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
sql_plans:
    description:
        - List of SqlPlan resources
    returned: on success
    type: complex
    contains:
        plan_hash:
            description:
                - Plan hash value for the SQL Execution Plan
            returned: on success
            type: int
            sample: 56
        plan_content:
            description:
                - Plan XML Content
            returned: on success
            type: str
            sample: plan_content_example
    sample: [{
        "plan_hash": 56,
        "plan_content": "plan_content_example"
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


class SqlPlanFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "sql_identifier",
            "plan_hash",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "database_id",
            "id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sql_plans,
            compartment_id=self.module.params.get("compartment_id"),
            sql_identifier=self.module.params.get("sql_identifier"),
            plan_hash=self.module.params.get("plan_hash"),
            **optional_kwargs
        )


SqlPlanFactsHelperCustom = get_custom_class("SqlPlanFactsHelperCustom")


class ResourceFactsHelper(SqlPlanFactsHelperCustom, SqlPlanFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sql_identifier=dict(type="str", required=True),
            plan_hash=dict(type="list", elements="int", required=True),
            database_id=dict(type="str"),
            id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_plan",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_plans=result)


if __name__ == "__main__":
    main()
