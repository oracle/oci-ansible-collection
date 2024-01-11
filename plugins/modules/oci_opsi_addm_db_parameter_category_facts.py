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
module: oci_opsi_addm_db_parameter_category_facts
short_description: Fetches details about one or multiple AddmDbParameterCategory resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AddmDbParameterCategory resources in Oracle Cloud Infrastructure
    - Gets list of ADDM database parameter categories for the specified databases.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    database_id:
        description:
            - Optional list of database L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated DBaaS entity.
        type: list
        elements: str
    id:
        description:
            - Optional list of database insight resource L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Field name for sorting the database parameter categories
        type: str
        choices:
            - "name"
    defined_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a defined tag matching the value will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_equals:
        description:
            - "A list of tag filters to apply.  Only resources with a freeform tag matching the value will be returned.
              The key for each tag is \\"{tagName}.{value}\\".  All inputs are case-insensitive.
              Multiple values for the same tag name are interpreted as \\"OR\\".  Values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    defined_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified defined tags exist will be returned.
              Each item in the list has the format \\"{namespace}.{tagName}.true\\" (for checking existence of a defined tag)
              or \\"{namespace}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for the same key (i.e. same namespace and tag name) are interpreted as \\"OR\\".
              Values for different keys (i.e. different namespaces, different tag names, or both) are interpreted as \\"AND\\"."
        type: list
        elements: str
    freeform_tag_exists:
        description:
            - "A list of tag existence filters to apply.  Only resources for which the specified freeform tags exist the value will be returned.
              The key for each tag is \\"{tagName}.true\\".  All inputs are case-insensitive.
              Currently, only existence (\\"true\\" at the end) is supported. Absence (\\"false\\" at the end) is not supported.
              Multiple values for different tag names are interpreted as \\"AND\\"."
        type: list
        elements: str
    compartment_id_in_subtree:
        description:
            - A flag to search all resources within a given compartment and all sub-compartments.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List addm_db_parameter_categories
  oci_opsi_addm_db_parameter_category_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    database_id: [ "ocid1.database.oc1..xxxxxxEXAMPLExxxxxx" ]
    id: [ "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx" ]
    sort_order: ASC
    sort_by: name
    defined_tag_equals: [ "defined_tag_equals_example" ]
    freeform_tag_equals: [ "freeform_tag_equals_example" ]
    defined_tag_exists: [ "defined_tag_exists_example" ]
    freeform_tag_exists: [ "freeform_tag_exists_example" ]
    compartment_id_in_subtree: true

"""

RETURN = """
addm_db_parameter_categories:
    description:
        - List of AddmDbParameterCategory resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Database insight.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Name of database parameter category
            returned: on success
            type: str
            sample: name_example
        display_name:
            description:
                - Display name of database parameter  category
            returned: on success
            type: str
            sample: display_name_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "display_name": "display_name_example"
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


class AddmDbParameterCategoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "database_id",
            "id",
            "sort_order",
            "sort_by",
            "defined_tag_equals",
            "freeform_tag_equals",
            "defined_tag_exists",
            "freeform_tag_exists",
            "compartment_id_in_subtree",
            "name",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_addm_db_parameter_categories,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AddmDbParameterCategoryFactsHelperCustom = get_custom_class(
    "AddmDbParameterCategoryFactsHelperCustom"
)


class ResourceFactsHelper(
    AddmDbParameterCategoryFactsHelperCustom, AddmDbParameterCategoryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            database_id=dict(type="list", elements="str"),
            id=dict(type="list", elements="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name"]),
            defined_tag_equals=dict(type="list", elements="str"),
            freeform_tag_equals=dict(type="list", elements="str"),
            defined_tag_exists=dict(type="list", elements="str"),
            freeform_tag_exists=dict(type="list", elements="str"),
            compartment_id_in_subtree=dict(type="bool"),
            name=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="addm_db_parameter_category",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(addm_db_parameter_categories=result)


if __name__ == "__main__":
    main()
