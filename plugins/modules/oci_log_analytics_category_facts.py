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
module: oci_log_analytics_category_facts
short_description: Fetches details about one or multiple LogAnalyticsCategory resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LogAnalyticsCategory resources in Oracle Cloud Infrastructure
    - Returns a list of categories, containing detailed information about them. You may limit the number of results, provide sorting order, and filter by
      information such as category name or description.
    - If I(category_name) is specified, the details of a single LogAnalyticsCategory will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    category_name:
        description:
            - The category name.
            - Required to get a specific log_analytics_category.
        type: str
    category_type:
        description:
            - A comma-separated list of category types used for filtering. Only categories of the
              specified types will be returned.
        type: str
    category_display_text:
        description:
            - The category display text used for filtering. Only categories matching the specified display
              name or description will be returned.
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
            - The attribute used to sort the returned categories
        type: str
        choices:
            - "displayName"
            - "type"
    name:
        description:
            - A filter to return only log analytics entities whose name matches the entire name given. The match
              is case-insensitive.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific log_analytics_category
  oci_log_analytics_category_facts:
    # required
    namespace_name: namespace_name_example
    category_name: category_name_example

- name: List log_analytics_categories
  oci_log_analytics_category_facts:
    # required
    namespace_name: namespace_name_example

    # optional
    category_type: category_type_example
    category_display_text: category_display_text_example
    sort_order: ASC
    sort_by: displayName
    name: name_example

"""

RETURN = """
log_analytics_categories:
    description:
        - List of LogAnalyticsCategory resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name that identifies the category.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - The category description.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - The category display name.
            returned: on success
            type: str
            sample: display_name_example
        type:
            description:
                - "The category type. Values include \\"PRODUCT\\", \\"TIER\\", \\"VENDOR\\" and \\"GENERIC\\"."
            returned: on success
            type: str
            sample: type_example
        is_system:
            description:
                - The system flag. A value of false denotes a user-created
                  category. A value of true denotes an Oracle-defined category.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "name": "name_example",
        "description": "description_example",
        "display_name": "display_name_example",
        "type": "type_example",
        "is_system": true
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LogAnalyticsCategoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "category_name",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_category,
            namespace_name=self.module.params.get("namespace_name"),
            category_name=self.module.params.get("category_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "category_type",
            "category_display_text",
            "sort_order",
            "sort_by",
            "name",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_categories,
            namespace_name=self.module.params.get("namespace_name"),
            **optional_kwargs
        )


LogAnalyticsCategoryFactsHelperCustom = get_custom_class(
    "LogAnalyticsCategoryFactsHelperCustom"
)


class ResourceFactsHelper(
    LogAnalyticsCategoryFactsHelperCustom, LogAnalyticsCategoryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            category_name=dict(type="str"),
            category_type=dict(type="str"),
            category_display_text=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName", "type"]),
            name=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_analytics_category",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_analytics_categories=result)


if __name__ == "__main__":
    main()
