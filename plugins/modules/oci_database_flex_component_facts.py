#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_database_flex_component_facts
short_description: Fetches details about one or multiple FlexComponentCollection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple FlexComponentCollection resources in Oracle Cloud Infrastructure
    - "Gets a list of the flex components that can be used to launch a new DB system. The flex component determines resources to allocate to the DB system -
      Database Servers and Storage Servers."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    name:
        description:
            - A filter to return only resources that match the entire name given. The match is not case sensitive.
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
            - The field to sort by.  You can provide one sort order (`sortOrder`).  Default order for NAME is ascending. The NAME sort order is case sensitive.
        type: str
        choices:
            - "NAME"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List flex_component_collections
  oci_database_flex_component_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
flex_component_collections:
    description:
        - List of FlexComponentCollection resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the Flex Component used for the DB system.
            returned: on success
            type: str
            sample: name_example
        minimum_core_count:
            description:
                - The minimum number of CPU cores that can be enabled on the DB Server for this Flex Component.
            returned: on success
            type: int
            sample: 56
        available_core_count:
            description:
                - The maximum number of CPU cores that can ben enabled on the DB Server for this Flex Component.
            returned: on success
            type: int
            sample: 56
        available_db_storage_in_gbs:
            description:
                - The maximum  storage that can be enabled on the Storage Server for this Flex Component.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "name": "name_example",
        "minimum_core_count": 56,
        "available_core_count": 56,
        "available_db_storage_in_gbs": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FlexComponentCollectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_flex_components,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


FlexComponentCollectionFactsHelperCustom = get_custom_class(
    "FlexComponentCollectionFactsHelperCustom"
)


class ResourceFactsHelper(
    FlexComponentCollectionFactsHelperCustom, FlexComponentCollectionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAME"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="flex_component_collection",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(flex_component_collections=result)


if __name__ == "__main__":
    main()
