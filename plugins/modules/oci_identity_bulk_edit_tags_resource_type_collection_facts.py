#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_identity_bulk_edit_tags_resource_type_collection_facts
short_description: Fetches details about one or multiple BulkEditTagsResourceTypeCollection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BulkEditTagsResourceTypeCollection resources in Oracle Cloud Infrastructure
    - Lists the resource types that support bulk tag editing.
version_added: "2.9"
author: Oracle (@oracle)
options: {}
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List bulk_edit_tags_resource_type_collections
  oci_identity_bulk_edit_tags_resource_type_collection_facts:

"""

RETURN = """
bulk_edit_tags_resource_type_collections:
    description:
        - List of BulkEditTagsResourceTypeCollection resources
    returned: on success
    type: complex
    contains:
        items:
            description:
                - The collection of resource types that support bulk editing of tags.
            returned: on success
            type: complex
            contains:
                resource_type:
                    description:
                        - The unique name of the resource type.
                    returned: on success
                    type: string
                    sample: resource_type_example
                metadata_keys:
                    description:
                        - The metadata keys required to identify the resource.
                        - "For example, for a bucket, the value of `metadataKeys` will be L(\\"namespaceName\\", \\"bucketName\\"].
                          This information will match the API documentation.
                          See [UpdateBucket,https://docs.cloud.oracle.com/api/#/en/objectstorage/latest/Bucket/UpdateBucket) and
                          L(DeleteBucket,https://docs.cloud.oracle.com/api/#/en/objectstorage/latest/Bucket/DeleteBucket)."
                    returned: on success
                    type: list
                    sample: []
    sample: [{
        "items": [{
            "resource_type": "resource_type_example",
            "metadata_keys": []
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BulkEditTagsResourceTypeCollectionFactsHelperGen(OCIResourceFactsHelperBase):
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
            self.client.list_bulk_edit_tags_resource_types, **optional_kwargs
        )


BulkEditTagsResourceTypeCollectionFactsHelperCustom = get_custom_class(
    "BulkEditTagsResourceTypeCollectionFactsHelperCustom"
)


class ResourceFactsHelper(
    BulkEditTagsResourceTypeCollectionFactsHelperCustom,
    BulkEditTagsResourceTypeCollectionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict())

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bulk_edit_tags_resource_type_collection",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(bulk_edit_tags_resource_type_collections=result)


if __name__ == "__main__":
    main()
