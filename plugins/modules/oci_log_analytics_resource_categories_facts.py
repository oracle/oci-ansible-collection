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
module: oci_log_analytics_resource_categories_facts
short_description: Fetches details about one or multiple ResourceCategories resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ResourceCategories resources in Oracle Cloud Infrastructure
    - Returns a list of resources and their category assignments.
      You may limit the number of results, provide sorting order, and filter by information such as resource type.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    categories:
        description:
            - A comma-separated list of categories used for filtering
        type: str
    resource_types:
        description:
            - A comma-separated list of resource types used for filtering. Only resources of the types
              specified will be returned. Examples include SOURCE, PARSER, LOOKUP, etc.
        type: str
    resource_ids:
        description:
            - A comma-separated list of resource unique identifiers used for filtering. Only resources
              with matching unique identifiers will be returned.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The attribute used to sort the returned category resources.
        type: str
        choices:
            - "resourceType"
            - "categoryName"
            - "resourceId"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List resource_categories
  oci_log_analytics_resource_categories_facts:
    # required
    namespace_name: namespace_name_example

    # optional
    categories: categories_example
    resource_types: resource_types_example
    resource_ids: resource_ids_example
    sort_order: ASC
    sort_by: resourceType

"""

RETURN = """
resource_categories:
    description:
        - List of ResourceCategories resources
    returned: on success
    type: complex
    contains:
        resource_id:
            description:
                - The unique identifier of the resource, usually a name or ocid.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        resource_type:
            description:
                - The resource type.
            returned: on success
            type: str
            sample: resource_type_example
        category_name:
            description:
                - The category name to which this resource belongs.
            returned: on success
            type: str
            sample: category_name_example
        is_system:
            description:
                - The system flag. A value of false denotes a user-created category assignment.
                  A value of true denotes an Oracle-defined category assignment.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_type": "resource_type_example",
        "category_name": "category_name_example",
        "is_system": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceCategoriesFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "namespace_name",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "categories",
            "resource_types",
            "resource_ids",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_resource_categories,
            namespace_name=self.module.params.get("namespace_name"),
            **optional_kwargs
        )


ResourceCategoriesFactsHelperCustom = get_custom_class(
    "ResourceCategoriesFactsHelperCustom"
)


class ResourceFactsHelper(
    ResourceCategoriesFactsHelperCustom, ResourceCategoriesFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            categories=dict(type="str"),
            resource_types=dict(type="str"),
            resource_ids=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["resourceType", "categoryName", "resourceId"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_categories",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_categories=result)


if __name__ == "__main__":
    main()
