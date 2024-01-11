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
module: oci_lockbox_access_materials_facts
short_description: Fetches details about a AccessMaterials resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AccessMaterials resource in Oracle Cloud Infrastructure
    - Retrieves the access credential/material associated with the access request.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    access_request_id:
        description:
            - The unique identifier (OCID) of the access request.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific access_materials
  oci_lockbox_access_materials_facts:
    # required
    access_request_id: "ocid1.accessrequest.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
access_materials:
    description:
        - AccessMaterials resource
    returned: on success
    type: complex
    contains:
        details:
            description:
                - The contents of the material. This is a map that contains the various fields needed for access.
            returned: on success
            type: dict
            sample: {}
    sample: {
        "details": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.lockbox import LockboxClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AccessMaterialsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "access_request_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_access_materials,
            access_request_id=self.module.params.get("access_request_id"),
        )


AccessMaterialsFactsHelperCustom = get_custom_class("AccessMaterialsFactsHelperCustom")


class ResourceFactsHelper(
    AccessMaterialsFactsHelperCustom, AccessMaterialsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(access_request_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="access_materials",
        service_client_class=LockboxClient,
        namespace="lockbox",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(access_materials=result)


if __name__ == "__main__":
    main()
