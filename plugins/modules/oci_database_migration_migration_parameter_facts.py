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
module: oci_database_migration_migration_parameter_facts
short_description: Fetches details about one or multiple MigrationParameter resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MigrationParameter resources in Oracle Cloud Infrastructure
    - List of parameters that can be used to customize migrations.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    migration_type:
        description:
            - A filter to return only resources that match a certain Migration Type.
        type: str
        choices:
            - "ONLINE"
            - "OFFLINE"
    database_combination:
        description:
            - A filter to return only resources that match a certain Database Combination.
        type: str
        choices:
            - "MYSQL"
            - "ORACLE"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending.
              Default order for displayName is ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List migration_parameters
  oci_database_migration_migration_parameter_facts:

    # optional
    migration_type: ONLINE
    database_combination: MYSQL
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
migration_parameters:
    description:
        - List of MigrationParameter resources
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
        display_name:
            description:
                - Parameter display name.
            returned: on success
            type: str
            sample: display_name_example
        doc_url_link:
            description:
                - Parameter documentation URL link.
            returned: on success
            type: str
            sample: doc_url_link_example
        description:
            description:
                - Parameter name description.
            returned: on success
            type: str
            sample: description_example
        category_name:
            description:
                - Parameter category name.
            returned: on success
            type: str
            sample: category_name_example
        category_display_name:
            description:
                - Parameter category display name.
            returned: on success
            type: str
            sample: category_display_name_example
        migration_type:
            description:
                - Migration Stage.
            returned: on success
            type: str
            sample: ONLINE
        default_value:
            description:
                - Default value for a parameter.
            returned: on success
            type: str
            sample: default_value_example
        min_value:
            description:
                - Parameter minimum value.
            returned: on success
            type: float
            sample: 3.4
        max_value:
            description:
                - Parameter maximum value.
            returned: on success
            type: float
            sample: 3.4
        hint_text:
            description:
                - Hint text for parameter value.
            returned: on success
            type: str
            sample: hint_text_example
        name:
            description:
                - Parameter name.
            returned: on success
            type: str
            sample: name_example
        data_type:
            description:
                - Parameter data type.
            returned: on success
            type: str
            sample: STRING
    sample: [{
        "database_combination": "MYSQL",
        "display_name": "display_name_example",
        "doc_url_link": "doc_url_link_example",
        "description": "description_example",
        "category_name": "category_name_example",
        "category_display_name": "category_display_name_example",
        "migration_type": "ONLINE",
        "default_value": "default_value_example",
        "min_value": 3.4,
        "max_value": 3.4,
        "hint_text": "hint_text_example",
        "name": "name_example",
        "data_type": "STRING"
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


class MigrationParameterFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "migration_type",
            "database_combination",
            "sort_by",
            "sort_order",
            "name",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_migration_parameters, **optional_kwargs
        )


MigrationParameterFactsHelperCustom = get_custom_class(
    "MigrationParameterFactsHelperCustom"
)


class ResourceFactsHelper(
    MigrationParameterFactsHelperCustom, MigrationParameterFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            migration_type=dict(type="str", choices=["ONLINE", "OFFLINE"]),
            database_combination=dict(type="str", choices=["MYSQL", "ORACLE"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="migration_parameter",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(migration_parameters=result)


if __name__ == "__main__":
    main()
