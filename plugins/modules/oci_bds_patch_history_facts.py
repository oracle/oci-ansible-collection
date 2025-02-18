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
module: oci_bds_patch_history_facts
short_description: Fetches details about one or multiple PatchHistory resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PatchHistory resources in Oracle Cloud Infrastructure
    - List the patch history of this cluster.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    bds_instance_id:
        description:
            - The OCID of the cluster.
        type: str
        required: true
    lifecycle_state:
        description:
            - The status of the patch.
        type: str
        choices:
            - "INSTALLING"
            - "INSTALLED"
            - "FAILED"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    patch_version:
        description:
            - The version of the patch
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    patch_type:
        description:
            - The type of a BDS patch history entity.
        type: str
        choices:
            - "ODH"
            - "OS"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List patch_histories
  oci_bds_patch_history_facts:
    # required
    bds_instance_id: "ocid1.bdsinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: INSTALLING
    sort_by: timeCreated
    patch_version: patch_version_example
    sort_order: ASC
    patch_type: ODH

"""

RETURN = """
patch_histories:
    description:
        - List of PatchHistory resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - The version of the patch.
            returned: on success
            type: str
            sample: version_example
        lifecycle_state:
            description:
                - The status of this patch.
            returned: on success
            type: str
            sample: INSTALLING
        time_updated:
            description:
                - The time when the patch history was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        patch_type:
            description:
                - "The type of current patch history.
                  DP - Data Plane patch(This history type is internal available only)
                  ODH - Oracle Distribution of Hadoop patch
                  OS - Operating System patch"
            returned: on success
            type: str
            sample: ODH
    sample: [{
        "version": "version_example",
        "lifecycle_state": "INSTALLING",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "patch_type": "ODH"
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


class PatchHistoryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "bds_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "sort_by",
            "patch_version",
            "sort_order",
            "patch_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_patch_histories,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            **optional_kwargs
        )


PatchHistoryFactsHelperCustom = get_custom_class("PatchHistoryFactsHelperCustom")


class ResourceFactsHelper(PatchHistoryFactsHelperCustom, PatchHistoryFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            bds_instance_id=dict(type="str", required=True),
            lifecycle_state=dict(
                type="str", choices=["INSTALLING", "INSTALLED", "FAILED"]
            ),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            patch_version=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            patch_type=dict(type="str", choices=["ODH", "OS"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="patch_history",
        service_client_class=BdsClient,
        namespace="bds",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(patch_histories=result)


if __name__ == "__main__":
    main()
