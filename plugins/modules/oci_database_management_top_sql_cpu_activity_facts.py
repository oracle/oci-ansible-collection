#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_database_management_top_sql_cpu_activity_facts
short_description: Fetches details about a TopSqlCpuActivity resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a TopSqlCpuActivity resource in Oracle Cloud Infrastructure
    - Get SQL ID with top cpu activity from storage server.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    external_exadata_storage_server_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Exadata storage server.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific top_sql_cpu_activity
  oci_database_management_top_sql_cpu_activity_facts:
    # required
    external_exadata_storage_server_id: "ocid1.externalexadatastorageserver.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
top_sql_cpu_activity:
    description:
        - TopSqlCpuActivity resource
    returned: on success
    type: complex
    contains:
        activity:
            description:
                - A list of sql cpu activity.
            returned: on success
            type: complex
            contains:
                database_name:
                    description:
                        - The database name.
                    returned: on success
                    type: str
                    sample: database_name_example
                sql_id:
                    description:
                        - The SQL ID.
                    returned: on success
                    type: str
                    sample: "ocid1.sql.oc1..xxxxxxEXAMPLExxxxxx"
                cpu_activity:
                    description:
                        - The CPU activity percentage.
                    returned: on success
                    type: float
                    sample: 3.4
    sample: {
        "activity": [{
            "database_name": "database_name_example",
            "sql_id": "ocid1.sql.oc1..xxxxxxEXAMPLExxxxxx",
            "cpu_activity": 3.4
        }]
    }
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


class TopSqlCpuActivityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "external_exadata_storage_server_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_top_sql_cpu_activity,
            external_exadata_storage_server_id=self.module.params.get(
                "external_exadata_storage_server_id"
            ),
        )


TopSqlCpuActivityFactsHelperCustom = get_custom_class(
    "TopSqlCpuActivityFactsHelperCustom"
)


class ResourceFactsHelper(
    TopSqlCpuActivityFactsHelperCustom, TopSqlCpuActivityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            external_exadata_storage_server_id=dict(
                aliases=["id"], type="str", required=True
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="top_sql_cpu_activity",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(top_sql_cpu_activity=result)


if __name__ == "__main__":
    main()
