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
module: oci_blockstorage_volume_backup_policy_assignment_facts
short_description: Fetches details about one or multiple VolumeBackupPolicyAssignment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple VolumeBackupPolicyAssignment resources in Oracle Cloud Infrastructure
    - Gets the volume backup policy assignment for the specified volume. The
      `assetId` query parameter is required, and the returned list will contain at most
      one item, since volume can only have one volume backup policy assigned at a time.
    - If I(policy_assignment_id) is specified, the details of a single VolumeBackupPolicyAssignment will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    policy_assignment_id:
        description:
            - The OCID of the volume backup policy assignment.
            - Required to get a specific volume_backup_policy_assignment.
        type: str
        aliases: ["id"]
    asset_id:
        description:
            - The OCID of an asset (e.g. a volume).
            - Required to list multiple volume_backup_policy_assignments.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific volume_backup_policy_assignment
  oci_blockstorage_volume_backup_policy_assignment_facts:
    # required
    policy_assignment_id: "ocid1.policyassignment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List volume_backup_policy_assignments
  oci_blockstorage_volume_backup_policy_assignment_facts:
    # required
    asset_id: "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
volume_backup_policy_assignments:
    description:
        - List of VolumeBackupPolicyAssignment resources
    returned: on success
    type: complex
    contains:
        asset_id:
            description:
                - The OCID of the volume the policy has been assigned to.
            returned: on success
            type: str
            sample: "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The OCID of the volume backup policy assignment.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        policy_id:
            description:
                - The OCID of the volume backup policy that has been assigned to the volume.
            returned: on success
            type: str
            sample: "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the volume backup policy was assigned to the volume. The format is
                  defined by L(RFC3339,https://tools.ietf.org/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "asset_id": "ocid1.asset.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "policy_id": "ocid1.policy.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import BlockstorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VolumeBackupPolicyAssignmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "policy_assignment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "asset_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_volume_backup_policy_assignment,
            policy_assignment_id=self.module.params.get("policy_assignment_id"),
        )

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.get_volume_backup_policy_asset_assignment,
            asset_id=self.module.params.get("asset_id"),
            **optional_kwargs
        )


VolumeBackupPolicyAssignmentFactsHelperCustom = get_custom_class(
    "VolumeBackupPolicyAssignmentFactsHelperCustom"
)


class ResourceFactsHelper(
    VolumeBackupPolicyAssignmentFactsHelperCustom,
    VolumeBackupPolicyAssignmentFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            policy_assignment_id=dict(aliases=["id"], type="str"),
            asset_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="volume_backup_policy_assignment",
        service_client_class=BlockstorageClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(volume_backup_policy_assignments=result)


if __name__ == "__main__":
    main()
