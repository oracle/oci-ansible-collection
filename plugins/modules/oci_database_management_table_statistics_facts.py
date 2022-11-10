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
module: oci_database_management_table_statistics_facts
short_description: Fetches details about one or multiple TableStatistics resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TableStatistics resources in Oracle Cloud Infrastructure
    - Lists the database table statistics grouped by different statuses such as Not Stale Stats, Stale Stats, and No Stats.
      This also includes the percentage of each status.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List table_statistics
  oci_database_management_table_statistics_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
table_statistics:
    description:
        - List of TableStatistics resources
    returned: on success
    type: complex
    contains:
        type:
            description:
                - The valid status categories of table statistics.
            returned: on success
            type: str
            sample: NO_STATS
        count:
            description:
                - The number of objects aggregated by status category.
            returned: on success
            type: int
            sample: 56
        percentage:
            description:
                - The percentage of objects with a particular status.
            returned: on success
            type: float
            sample: 1.2
    sample: [{
        "type": "NO_STATS",
        "count": 56,
        "percentage": 1.2
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TableStatisticsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_table_statistics,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


TableStatisticsFactsHelperCustom = get_custom_class("TableStatisticsFactsHelperCustom")


class ResourceFactsHelper(
    TableStatisticsFactsHelperCustom, TableStatisticsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(managed_database_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="table_statistics",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(table_statistics=result)


if __name__ == "__main__":
    main()
