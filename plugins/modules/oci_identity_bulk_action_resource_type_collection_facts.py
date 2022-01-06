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
module: oci_identity_bulk_action_resource_type_collection_facts
short_description: Fetches details about one or multiple BulkActionResourceTypeCollection resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BulkActionResourceTypeCollection resources in Oracle Cloud Infrastructure
    - Lists the resource-types supported by compartment bulk actions. Use this API to help you provide the correct
      resource-type information to the L(BulkDeleteResources,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/identity/20160918/Compartment/BulkDeleteResources/)
      and L(BulkMoveResources,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/identity/20160918/Compartment/BulkMoveResources/) operations. The returned list
      of
      resource-types provides the appropriate resource-type names to use with the bulk action operations along with
      the type of identifying information you'll need to provide for each resource-type. Most resource-types just
      require an L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) to identify a specific resource, but some resource-types,
      such as buckets, require you to provide other identifying information.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bulk_action_type:
        description:
            - The type of bulk action.
        type: str
        choices:
            - "BULK_MOVE_RESOURCES"
            - "BULK_DELETE_RESOURCES"
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List bulk_action_resource_type_collections
  oci_identity_bulk_action_resource_type_collection_facts:
    # required
    bulk_action_type: BULK_MOVE_RESOURCES

"""

RETURN = """
bulk_action_resource_type_collections:
    description:
        - List of BulkActionResourceTypeCollection resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name of the resource-type.
            returned: on success
            type: str
            sample: name_example
        metadata_keys:
            description:
                - "List of metadata keys required to identify a specific resource. Some resource-types require information besides an OCID to identify
                  a specific resource. For example, the resource-type `buckets` requires metadataKeys L(\\"namespaceName\\", \\"bucketName\\"] to
                  identify a specific bucket. The required information to identify a resource is in the API documentation for the
                  resource-type. For example, the required information for `buckets` is found in the
                  [DeleteBucket API,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/objectstorage/20160918/Bucket/DeleteBucket)."
            returned: on success
            type: list
            sample: []
    sample: [{
        "name": "name_example",
        "metadata_keys": []
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


class BulkActionResourceTypeCollectionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "bulk_action_type",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_bulk_action_resource_types,
            bulk_action_type=self.module.params.get("bulk_action_type"),
            **optional_kwargs
        )


BulkActionResourceTypeCollectionFactsHelperCustom = get_custom_class(
    "BulkActionResourceTypeCollectionFactsHelperCustom"
)


class ResourceFactsHelper(
    BulkActionResourceTypeCollectionFactsHelperCustom,
    BulkActionResourceTypeCollectionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            bulk_action_type=dict(
                type="str",
                required=True,
                choices=["BULK_MOVE_RESOURCES", "BULK_DELETE_RESOURCES"],
            ),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="bulk_action_resource_type_collection",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(bulk_action_resource_type_collections=result)


if __name__ == "__main__":
    main()
