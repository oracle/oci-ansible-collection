#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_database_migration_migration_object_type_facts
short_description: Fetches details about one or multiple MigrationObjectType resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MigrationObjectType resources in Oracle Cloud Infrastructure
    - Display sample object types to exclude or include for a Migration.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    connection_type:
        description:
            - The connection type for migration objects.
        type: str
        choices:
            - "MYSQL"
            - "ORACLE"
        required: true
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order for name is custom based on it's usage frequency. If no value is specified name is default.
        type: str
        choices:
            - "name"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List migration_object_types
  oci_database_migration_migration_object_type_facts:
    # required
    connection_type: MYSQL

    # optional
    sort_by: name
    sort_order: ASC

"""

RETURN = """
migration_object_types:
    description:
        - List of MigrationObjectType resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Object type name
            returned: on success
            type: str
            sample: name_example
    sample: [{
        "name": "name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database_migration import DatabaseMigrationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MigrationObjectTypeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "connection_type",
        ]

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_migration_object_types,
            connection_type=self.module.params.get("connection_type"),
            **optional_kwargs
        )


MigrationObjectTypeFactsHelperCustom = get_custom_class(
    "MigrationObjectTypeFactsHelperCustom"
)


class ResourceFactsHelper(
    MigrationObjectTypeFactsHelperCustom, MigrationObjectTypeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            connection_type=dict(
                type="str", required=True, choices=["MYSQL", "ORACLE"]
            ),
            sort_by=dict(type="str", choices=["name"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="migration_object_type",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(migration_object_types=result)


if __name__ == "__main__":
    main()
