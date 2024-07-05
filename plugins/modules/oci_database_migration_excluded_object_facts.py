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
module: oci_database_migration_excluded_object_facts
short_description: Fetches details about one or multiple ExcludedObject resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ExcludedObject resources in Oracle Cloud Infrastructure
    - List the excluded database objects.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    job_id:
        description:
            - The OCID of the job
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
              Default order for reasonCategory is ascending.
              If no value is specified reasonCategory is default.
        type: str
        choices:
            - "type"
            - "reasonCategory"
    type:
        description:
            - Excluded object type.
        type: str
    owner:
        description:
            - Excluded object owner
        type: str
    object:
        description:
            - Excluded object name
        type: str
    owner_contains:
        description:
            - Excluded object owner which contains provided value.
        type: str
    object_contains:
        description:
            - Excluded object name which contains provided value.
        type: str
    reason_category:
        description:
            - Reason category for the excluded object
        type: str
        choices:
            - "ORACLE_MAINTAINED"
            - "GG_UNSUPPORTED"
            - "USER_EXCLUDED"
            - "MANDATORY_EXCLUDED"
            - "USER_EXCLUDED_TYPE"
    source_rule:
        description:
            - Exclude object rule that matches the excluded object, if applicable.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List excluded_objects
  oci_database_migration_excluded_object_facts:
    # required
    job_id: "ocid1.job.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: type
    type: type_example
    owner: owner_example
    object: object_example
    owner_contains: owner_contains_example
    object_contains: object_contains_example
    reason_category: ORACLE_MAINTAINED
    source_rule: source_rule_example

"""

RETURN = """
excluded_objects:
    description:
        - List of ExcludedObject resources
    returned: on success
    type: complex
    contains:
        owner:
            description:
                - Database object owner.
            returned: on success
            type: str
            sample: owner_example
        object:
            description:
                - Database object name.
            returned: on success
            type: str
            sample: object_example
        type:
            description:
                - Database object type.
            returned: on success
            type: str
            sample: type_example
        reason_category:
            description:
                - Reason category for object exclusion.
            returned: on success
            type: str
            sample: ORACLE_MAINTAINED
        source_rule:
            description:
                - Reason for exclusion.
            returned: on success
            type: str
            sample: source_rule_example
    sample: [{
        "owner": "owner_example",
        "object": "object_example",
        "type": "type_example",
        "reason_category": "ORACLE_MAINTAINED",
        "source_rule": "source_rule_example"
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


class ExcludedObjectFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "job_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "type",
            "owner",
            "object",
            "owner_contains",
            "object_contains",
            "reason_category",
            "source_rule",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_excluded_objects,
            job_id=self.module.params.get("job_id"),
            **optional_kwargs
        )


ExcludedObjectFactsHelperCustom = get_custom_class("ExcludedObjectFactsHelperCustom")


class ResourceFactsHelper(
    ExcludedObjectFactsHelperCustom, ExcludedObjectFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            job_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["type", "reasonCategory"]),
            type=dict(type="str"),
            owner=dict(type="str"),
            object=dict(type="str"),
            owner_contains=dict(type="str"),
            object_contains=dict(type="str"),
            reason_category=dict(
                type="str",
                choices=[
                    "ORACLE_MAINTAINED",
                    "GG_UNSUPPORTED",
                    "USER_EXCLUDED",
                    "MANDATORY_EXCLUDED",
                    "USER_EXCLUDED_TYPE",
                ],
            ),
            source_rule=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="excluded_object",
        service_client_class=DatabaseMigrationClient,
        namespace="database_migration",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(excluded_objects=result)


if __name__ == "__main__":
    main()
