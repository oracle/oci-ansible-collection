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
module: oci_volume_backup_policy_assignment
short_description: Manage volume backup policy assignments in OCI Block Volume service
description:
    - This module allows the user to perform create & delete operations on volume backup policy assignments in OCI Block
      Volume service.
version_added: "2.5"
options:
    asset_id:
        description: The OCID of the asset (e.g. a volume) to which to assign the policy. Required to create a volume
                     backup policy assignment with I(state=present).
        required: false
    policy_id:
        description: The OCID of the volume backup policy to assign to an asset. Required to create a volume backup
                     policy assignment with I(state=present).
        required: false
    state:
        description: Use I(state=present) to create a volume backup policy assignment. Use I(state=absent) to delete a
                     volume backup policy assignment.
        required: false
        default: present
        choices: ['present', 'absent']
    policy_assignment_id:
        description: OCID of the volume backup policy assignment. Required to delete a volume backup policy assignment.
        required: false
        aliases: ['id']
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
- name: Create a volume backup policy assignment
  oci_volume_backup_policy_assignment:
    asset_id: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx
    policy_id: ocid1.volumebackuppolicy.oc1..xxxxxEXAMPLExxxxx

- name: Delete a volume backup policy assignment
  oci_volume_backup_policy_assignment:
    id: ocid1.volumebackuppolicyassign.oc1.iad.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
volume_backup_policy_assignment:
    description: Information about the volume backup policy assignment
    returned: on successful operation
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
    sample: {
            "asset_id": "ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx",
            "policy_id": "ocid1.volumebackuppolicy.oc1..xxxxxEXAMPLExxxxx",
            "id": "ocid1.volumebackuppolicyassign.oc1.iad.xxxxxEXAMPLExxxxx",
            "time_created": "2017-12-22T15:40:53.219000+00:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.core.models import CreateVolumeBackupPolicyAssignmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_volume_backup_policy_assignment(block_storage_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="volume_backup_policy_assignment",
        client=block_storage_client,
        get_fn=block_storage_client.get_volume_backup_policy_assignment,
        kwargs_get={"policy_assignment_id": module.params["policy_assignment_id"]},
        delete_fn=block_storage_client.delete_volume_backup_policy_assignment,
        kwargs_delete={"policy_assignment_id": module.params["policy_assignment_id"]},
        module=module,
        wait_applicable=False,
    )
    return result


def create_volume_backup_policy_assignment(block_storage_client, module):
    cvb = CreateVolumeBackupPolicyAssignmentDetails()

    for attribute in cvb.attribute_map.keys():
        if attribute in module.params:
            setattr(cvb, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(
        resource_type="volume_backup_policy_assignment",
        create_fn=block_storage_client.create_volume_backup_policy_assignment,
        kwargs_create={"create_volume_backup_policy_assignment_details": cvb},
        client=block_storage_client,
        get_fn=block_storage_client.get_volume_backup_policy_assignment,
        get_param="policy_assignment_id",
        module=module,
        wait_applicable=False,
    )

    return result


def main():
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            asset_id=dict(type="str", required=False),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            policy_assignment_id=dict(type="str", required=False, aliases=["id"]),
            policy_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[["state", "absent", ["policy_assignment_id"]]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    state = module.params["state"]

    if state == "absent":
        result = delete_volume_backup_policy_assignment(block_storage_client, module)

    else:
        result = oci_utils.check_and_create_resource(
            resource_type="volume_backup_policy_assignment",
            create_fn=create_volume_backup_policy_assignment,
            kwargs_create={
                "block_storage_client": block_storage_client,
                "module": module,
            },
            list_fn=block_storage_client.get_volume_backup_policy_asset_assignment,
            kwargs_list={"asset_id": module.params["asset_id"]},
            module=module,
            model=CreateVolumeBackupPolicyAssignmentDetails(),
        )
    module.exit_json(**result)


if __name__ == "__main__":
    main()
