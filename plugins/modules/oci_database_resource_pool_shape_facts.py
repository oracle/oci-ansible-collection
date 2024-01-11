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
module: oci_database_resource_pool_shape_facts
short_description: Fetches details about one or multiple ResourcePoolShape resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ResourcePoolShape resources in Oracle Cloud Infrastructure
    - Lists available resource pools shapes.
version_added: "2.9.0"
author: Oracle (@oracle)
options: {}
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List resource_pool_shapes
  oci_database_resource_pool_shape_facts:

"""

RETURN = """
resource_pool_shapes:
    description:
        - List of ResourcePoolShape resources
    returned: on success
    type: complex
    contains:
        shape:
            description:
                - Predefined shape of the resource pool.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "shape": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourcePoolShapeFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.resource_pool_shapes, **optional_kwargs
        )


ResourcePoolShapeFactsHelperCustom = get_custom_class(
    "ResourcePoolShapeFactsHelperCustom"
)


class ResourceFactsHelper(
    ResourcePoolShapeFactsHelperCustom, ResourcePoolShapeFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict())

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="resource_pool_shape",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(resource_pool_shapes=result)


if __name__ == "__main__":
    main()
