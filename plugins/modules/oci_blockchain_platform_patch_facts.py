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
module: oci_blockchain_platform_patch_facts
short_description: Fetches details about one or multiple BlockchainPlatformPatch resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BlockchainPlatformPatch resources in Oracle Cloud Infrastructure
    - List Blockchain Platform Patches
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    blockchain_platform_id:
        description:
            - Unique service identifier.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List blockchain_platform_patches
  oci_blockchain_platform_patch_facts:
    # required
    blockchain_platform_id: "ocid1.blockchainplatform.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
blockchain_platform_patches:
    description:
        - List of BlockchainPlatformPatch resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - patch id
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        service_version:
            description:
                - patch service version
            returned: on success
            type: str
            sample: service_version_example
        patch_info_url:
            description:
                - A URL for the patch specific documentation
            returned: on success
            type: str
            sample: patch_info_url_example
        time_patch_due:
            description:
                - patch due date for customer initiated patching
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "service_version": "service_version_example",
        "patch_info_url": "patch_info_url_example",
        "time_patch_due": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.blockchain import BlockchainPlatformClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BlockchainPlatformPatchFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "blockchain_platform_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_blockchain_platform_patches,
            blockchain_platform_id=self.module.params.get("blockchain_platform_id"),
            **optional_kwargs
        )


BlockchainPlatformPatchFactsHelperCustom = get_custom_class(
    "BlockchainPlatformPatchFactsHelperCustom"
)


class ResourceFactsHelper(
    BlockchainPlatformPatchFactsHelperCustom, BlockchainPlatformPatchFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(blockchain_platform_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="blockchain_platform_patch",
        service_client_class=BlockchainPlatformClient,
        namespace="blockchain",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(blockchain_platform_patches=result)


if __name__ == "__main__":
    main()
