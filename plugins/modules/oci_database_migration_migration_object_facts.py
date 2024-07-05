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
module: oci_database_migration_migration_object_facts
short_description: Fetches details about one or multiple MigrationObject resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MigrationObject resources in Oracle Cloud Infrastructure
    - Display excluded/included objects.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    migration_id:
        description:
            - The OCID of the migration
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List migration_objects
  oci_database_migration_migration_object_facts:
    # required
    migration_id: "ocid1.migration.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
migration_objects:
    description:
        - List of MigrationObject resources
    returned: on success
    type: complex
    contains:
        database_combination:
            description:
                - "The combination of source and target databases participating in a migration.
                  Example: ORACLE means the migration is meant for migrating Oracle source and target databases."
            returned: on success
            type: str
            sample: MYSQL
        items:
            description:
                - An array of database objects that are either included or excluded from the migration.
            returned: on success
            type: complex
            contains:
                object_status:
                    description:
                        - Object status.
                    returned: on success
                    type: str
                    sample: EXCLUDE
                schema:
                    description:
                        - Schema of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: schema_example
                object_name:
                    description:
                        - Name of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: object_name_example
                type:
                    description:
                        - Type of object to exclude.
                          If not specified, matching owners and object names of type TABLE would be excluded.
                    returned: on success
                    type: str
                    sample: type_example
                owner:
                    description:
                        - Owner of the object (regular expression is allowed)
                    returned: on success
                    type: str
                    sample: owner_example
                is_omit_excluded_table_from_replication:
                    description:
                        - Whether an excluded table should be omitted from replication. Only valid for database objects
                          that have are of type TABLE and object status EXCLUDE.
                    returned: on success
                    type: bool
                    sample: true
        bulk_include_exclude_data:
            description:
                - Specifies the database objects to be excluded from the migration in bulk.
                  The definition accepts input in a CSV format, newline separated for each entry.
                  More details can be found in the documentation.
            returned: on success
            type: str
            sample: bulk_include_exclude_data_example
    sample: [{
        "database_combination": "MYSQL",
        "items": [{
            "object_status": "EXCLUDE",
            "schema": "schema_example",
            "object_name": "object_name_example",
            "type": "type_example",
            "owner": "owner_example",
            "is_omit_excluded_table_from_replication": true
        }],
        "bulk_include_exclude_data": "bulk_include_exclude_data_example"
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


class MigrationObjectFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "migration_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_migration_objects,
            migration_id=self.module.params.get("migration_id"),
            **optional_kwargs
        )


MigrationObjectFactsHelperCustom = get_custom_class("MigrationObjectFactsHelperCustom")


class ResourceFactsHelper(
    MigrationObjectFactsHelperCustom, MigrationObjectFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(migration_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="migration_object",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(migration_objects=result)


if __name__ == "__main__":
    main()
