#!/usr/bin/python
# Copyright (c) 2018, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_volume_backup_policy_assignment_facts
short_description: Retrieve information of a volume backup policy assignment in OCI Block Volume service
description:
    - This module retrieves information of the specified volume backup policy assignment or the volume backup policy
      assignment for the specified asset.
version_added: "2.5"
options:
    policy_assignment_id:
        description: The OCID of the volume backup policy assignment. I(policy_assignment_id) is required to get
                     information of the specified volume backup policy assignment.
        required: false
        aliases: ['id']
    asset_id:
        description: The OCID of an asset (e.g. a volume). I(asset_id) is required to get information of the volume
                     backup policy assignment for the specified asset.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: oracle
"""

EXAMPLES = """
- name: Get information of a volume backup policy assignment
  oci_volume_backup_policy_assignment_facts:
    id: ocid1.volumebackuppolicyassign.oc1.iad.xxxxxEXAMPLExxxxx

- name: Get information of volume backup assignment for the specified asset
  oci_volume_backup_policy_assignment_facts:
    asset_id: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx
"""

RETURN = """
volume_backup_policy_assignments:
    description: List of volume backup policy assignment
    returned: on success
    type: complex
    contains:
        asset_id:
            description: The OCID of the asset (e.g. a volume) to which the policy has been assigned.
            returned: always
            type: string
            sample: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx
        id:
            description: The OCID of the volume backup policy assignment.
            returned: always
            type: string
            sample: ocid1.volumebackuppolicyassign.oc1.iad.xxxxxEXAMPLExxxxx
        policy_id:
            description: The OCID of the volume backup policy that has been assigned to an asset.
            returned: always
            type: string
            sample: ocid1.volumebackuppolicy.oc1..xxxxxEXAMPLExxxxx
        time_created:
            description: The date and time the volume backup policy assignment was created. Format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-12-22T15:40:53.219000+00:00
    sample: [{
            "asset_id": "ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx",
            "policy_id": "ocid1.volumebackuppolicy.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.volumebackuppolicyassign.oc1.iad.xxxxxEXAMPLExxxxx",
            "time_created": "2017-12-22T15:40:53.219000+00:00"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            policy_assignment_id=dict(type="str", required=False, aliases=["id"]),
            asset_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["policy_assignment_id", "asset_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    policy_assignment_id = module.params["policy_assignment_id"]

    try:
        if policy_assignment_id:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        block_storage_client.get_volume_backup_policy_assignment,
                        policy_assignment_id=policy_assignment_id,
                    ).data
                )
            ]
        else:
            result = to_dict(
                oci_utils.call_with_backoff(
                    block_storage_client.get_volume_backup_policy_asset_assignment,
                    asset_id=module.params["asset_id"],
                ).data
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(volume_backup_policy_assignments=result)


if __name__ == "__main__":
    main()
