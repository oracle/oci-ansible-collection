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
module: oci_resource_search_resource_type_facts
short_description: Fetches details about one or multiple ResourceType resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ResourceType resources in Oracle Cloud Infrastructure
    - Lists all resource types that you can search or query for.
    - If I(name) is specified, the details of a single ResourceType will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name of the resource type.
            - Required to get a specific resource_type.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific resource_type
  oci_resource_search_resource_type_facts:
    # required
    name: name_example

- name: List resource_types
  oci_resource_search_resource_type_facts:

"""

RETURN = """
resource_types:
    description:
        - List of ResourceType resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name of the resource type, which matches the value returned as part of the ResourceSummary object.
            returned: on success
            type: str
            sample: name_example
        fields:
            description:
                - List of all the fields and their value type that are indexed for querying.
            returned: on success
            type: complex
            contains:
                field_type:
                    description:
                        - The type of the field, which dictates what semantics and query constraints you can use when searching or querying.
                    returned: on success
                    type: str
                    sample: IDENTIFIER
                field_name:
                    description:
                        - The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.
                    returned: on success
                    type: str
                    sample: field_name_example
                is_array:
                    description:
                        - Indicates that this field is actually an array of the specified field type.
                    returned: on success
                    type: bool
                    sample: true
                object_properties:
                    description:
                        - If the field type is `OBJECT`, then this property will provide all the individual properties of the object that can
                          be queried.
                    returned: on success
                    type: complex
                    contains:
                        field_type:
                            description:
                                - The type of the field, which dictates what semantics and query constraints you can use when searching or querying.
                            returned: on success
                            type: str
                            sample: IDENTIFIER
                        field_name:
                            description:
                                - The name of the field to use when constructing the query. Field names are present for all types except `OBJECT`.
                            returned: on success
                            type: str
                            sample: field_name_example
                        is_array:
                            description:
                                - Indicates that this field is actually an array of the specified field type.
                            returned: on success
                            type: bool
                            sample: true
                        object_properties:
                            description:
                                - If the field type is `OBJECT`, then this property will provide all the individual properties of the object that can
                                  be queried.
                            returned: on success
                            type: list
                            sample: []
    sample: [{
        "name": "name_example",
        "fields": [{
            "field_type": "IDENTIFIER",
            "field_name": "field_name_example",
            "is_array": true,
            "object_properties": [{
                "field_type": "IDENTIFIER",
                "field_name": "field_name_example",
                "is_array": true,
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
    from oci.resource_search import ResourceSearchClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceTypeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "name",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_resource_type, name=self.module.params.get("name"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_resource_types, **optional_kwargs
        )


ResourceTypeFactsHelperCustom = get_custom_class("ResourceTypeFactsHelperCustom")


class ResourceFactsHelper(ResourceTypeFactsHelperCustom, ResourceTypeFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(name=dict(type="str"),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_type",
        service_client_class=ResourceSearchClient,
        namespace="resource_search",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_types=result)


if __name__ == "__main__":
    main()
