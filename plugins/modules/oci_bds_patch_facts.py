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
module: oci_bds_patch_facts
short_description: Fetches details about one or multiple Patch resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Patch resources in Oracle Cloud Infrastructure
    - List all the available patches for this cluster.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List patches
  oci_bds_patch_facts:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
patches:
    description:
        - List of Patch resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - The version of the patch.
            returned: on success
            type: str
            sample: version_example
        time_released:
            description:
                - The time when the patch was released.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "version": "version_example",
        "time_released": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.bds import BdsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PatchFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "bds_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_patches,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            **optional_kwargs
        )


PatchFactsHelperCustom = get_custom_class("PatchFactsHelperCustom")


class ResourceFactsHelper(PatchFactsHelperCustom, PatchFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(bds_instance_id=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="patch",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(patches=result)


if __name__ == "__main__":
    main()
