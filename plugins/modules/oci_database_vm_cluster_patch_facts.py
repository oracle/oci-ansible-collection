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
module: oci_database_vm_cluster_patch_facts
short_description: Fetches details about one or multiple VmClusterPatch resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VmClusterPatch resources in Oracle Cloud Infrastructure
    - Lists the patches applicable to the specified VM cluster in an Exadata Cloud@Customer system.
    - If I(patch_id) is specified, the details of a single VmClusterPatch will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    vm_cluster_id:
        description:
            - The VM cluster L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        required: true
    patch_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch.
            - Required to get a specific vm_cluster_patch.
        type: str
        aliases: ["id"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific vm_cluster_patch
  oci_database_vm_cluster_patch_facts:
    # required
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"
    patch_id: "ocid1.patch.oc1..xxxxxxEXAMPLExxxxxx"

- name: List vm_cluster_patches
  oci_database_vm_cluster_patch_facts:
    # required
    vm_cluster_id: "ocid1.vmcluster.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
vm_cluster_patches:
    description:
        - List of VmClusterPatch resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the patch.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The text describing this patch package.
            returned: on success
            type: str
            sample: description_example
        last_action:
            description:
                - Action that is currently being performed or was completed last.
            returned: on success
            type: str
            sample: APPLY
        available_actions:
            description:
                - Actions that can possibly be performed using this patch.
            returned: on success
            type: list
            sample: []
        lifecycle_details:
            description:
                - A descriptive text associated with the lifecycleState.
                  Typically can contain additional displayable text.
            returned: on success
            type: str
            sample: lifecycle_details_example
        lifecycle_state:
            description:
                - The current state of the patch as a result of lastAction.
            returned: on success
            type: str
            sample: AVAILABLE
        time_released:
            description:
                - The date and time that the patch was released.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        version:
            description:
                - The version of this patch package.
            returned: on success
            type: str
            sample: version_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "last_action": "APPLY",
        "available_actions": [],
        "lifecycle_details": "lifecycle_details_example",
        "lifecycle_state": "AVAILABLE",
        "time_released": "2013-10-20T19:20:30+01:00",
        "version": "version_example"
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


class VmClusterPatchFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "vm_cluster_id",
            "patch_id",
        ]

    def get_required_params_for_list(self):
        return [
            "vm_cluster_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vm_cluster_patch,
            vm_cluster_id=self.module.params.get("vm_cluster_id"),
            patch_id=self.module.params.get("patch_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_vm_cluster_patches,
            vm_cluster_id=self.module.params.get("vm_cluster_id"),
            **optional_kwargs
        )


VmClusterPatchFactsHelperCustom = get_custom_class("VmClusterPatchFactsHelperCustom")


class ResourceFactsHelper(
    VmClusterPatchFactsHelperCustom, VmClusterPatchFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            vm_cluster_id=dict(type="str", required=True),
            patch_id=dict(aliases=["id"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vm_cluster_patch",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vm_cluster_patches=result)


if __name__ == "__main__":
    main()
