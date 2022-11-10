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
module: oci_database_management_sql_tuning_set_facts
short_description: Fetches details about one or multiple SqlTuningSet resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SqlTuningSet resources in Oracle Cloud Infrastructure
    - Lists the SQL tuning sets for the specified Managed Database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    owner:
        description:
            - The owner of the SQL tuning set.
        type: str
    name_contains:
        description:
            - Allow searching the name of the SQL tuning set by partial matching. The search is case insensitive.
        type: str
    sort_by:
        description:
            - The option to sort the SQL tuning set summary data.
        type: str
        choices:
            - "NAME"
    sort_order:
        description:
            - The option to sort information in ascending ('ASC') or descending ('DESC') order. Ascending order is the default order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List sql_tuning_sets
  oci_database_management_sql_tuning_set_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    owner: owner_example
    name_contains: name_contains_example
    sort_by: NAME
    sort_order: ASC

"""

RETURN = """
sql_tuning_sets:
    description:
        - List of SqlTuningSet resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the SQL tuning set.
            returned: on success
            type: str
            sample: name_example
        owner:
            description:
                - The owner of the SQL tuning set.
            returned: on success
            type: str
            sample: owner_example
        description:
            description:
                - The description of the SQL tuning set.
            returned: on success
            type: str
            sample: description_example
        statement_counts:
            description:
                - The number of SQL statements in the SQL tuning set.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "name": "name_example",
        "owner": "owner_example",
        "description": "description_example",
        "statement_counts": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import SqlTuningClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SqlTuningSetFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "owner",
            "name_contains",
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sql_tuning_sets,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


SqlTuningSetFactsHelperCustom = get_custom_class("SqlTuningSetFactsHelperCustom")


class ResourceFactsHelper(SqlTuningSetFactsHelperCustom, SqlTuningSetFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            owner=dict(type="str"),
            name_contains=dict(type="str"),
            sort_by=dict(type="str", choices=["NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sql_tuning_set",
        service_client_class=SqlTuningClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sql_tuning_sets=result)


if __name__ == "__main__":
    main()
