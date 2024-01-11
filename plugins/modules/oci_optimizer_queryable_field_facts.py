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
module: oci_optimizer_queryable_field_facts
short_description: Fetches details about one or multiple QueryableField resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple QueryableField resources in Oracle Cloud Infrastructure
    - Lists the fields that are indexed for querying and their associated value types.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        required: true
    compartment_id_in_subtree:
        description:
            - When set to true, the hierarchy of compartments is traversed and all compartments and subcompartments in the tenancy are returned depending on the
              the setting of `accessLevel`.
            - Can only be set to true when performing ListCompartments on the tenancy (root compartment).
        type: bool
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List queryable_fields
  oci_optimizer_queryable_field_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id_in_subtree: true

"""

RETURN = """
queryable_fields:
    description:
        - List of QueryableField resources
    returned: on success
    type: complex
    contains:
        field_type:
            description:
                - The type of the field, which dictates the semantics and query constraints that you can use when searching or querying.
            returned: on success
            type: str
            sample: STRING
        field_name:
            description:
                - The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.
            returned: on success
            type: str
            sample: field_name_example
        object_properties:
            description:
                - If the field type is `OBJECT`, this property lists the individual properties of the object that can be queried.
            returned: on success
            type: complex
            contains:
                field_type:
                    description:
                        - The type of the field, which dictates the semantics and query constraints that you can use when searching or querying.
                    returned: on success
                    type: str
                    sample: STRING
                field_name:
                    description:
                        - The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.
                    returned: on success
                    type: str
                    sample: field_name_example
                object_properties:
                    description:
                        - If the field type is `OBJECT`, this property lists the individual properties of the object that can be queried.
                    returned: on success
                    type: complex
                    contains:
                        field_type:
                            description:
                                - The type of the field, which dictates the semantics and query constraints that you can use when searching or querying.
                            returned: on success
                            type: str
                            sample: STRING
                        field_name:
                            description:
                                - The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.
                            returned: on success
                            type: str
                            sample: field_name_example
                        object_properties:
                            description:
                                - If the field type is `OBJECT`, this property lists the individual properties of the object that can be queried.
                            returned: on success
                            type: list
                            sample: []
    sample: [{
        "field_type": "STRING",
        "field_name": "field_name_example",
        "object_properties": [{
            "field_type": "STRING",
            "field_name": "field_name_example",
            "object_properties": [{
                "field_type": "STRING",
                "field_name": "field_name_example",
                "object_properties": []
            }]
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.optimizer import OptimizerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class QueryableFieldFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "compartment_id_in_subtree",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_resource_action_queryable_fields,
            compartment_id=self.module.params.get("compartment_id"),
            compartment_id_in_subtree=self.module.params.get(
                "compartment_id_in_subtree"
            ),
            **optional_kwargs
        )


QueryableFieldFactsHelperCustom = get_custom_class("QueryableFieldFactsHelperCustom")


class ResourceFactsHelper(
    QueryableFieldFactsHelperCustom, QueryableFieldFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            compartment_id_in_subtree=dict(type="bool", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="queryable_field",
        service_client_class=OptimizerClient,
        namespace="optimizer",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(queryable_fields=result)


if __name__ == "__main__":
    main()
