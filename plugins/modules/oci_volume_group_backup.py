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
module: oci_volume_group_backup
short_description: Manage volume group backups in OCI Block Volume service
description:
    - This module allows the user to perform create, delete & update operations on volume group backups in OCI Block
      Volume service.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment that will contain the volume group backup. This parameter is optional,
                     by default backup will be created in the same compartment as source volume group.
        required: false
    display_name:
        description: A user-friendly name for the volume group backup. Does not have to be unique and it's changeable.
                     Avoid entering confidential information.
        required: false
        aliases: ['name']
    state:
        description: Use I(state=present) to create or update a volume group backup. Use I(state=absent) to delete a
                     volume group backup.
        required: false
        default: present
        choices: ['present', 'absent']
    type:
        description: The type of backup to create.
        required: false
        default: INCREMENTAL
        choices: ['FULL', 'INCREMENTAL']
    volume_group_backup_id:
        description: The OCID of the volume group backup. Required to update a volume group backup with I(state=present)
                     or to delete a volume group backup with I(state=absent).
        required: false
        aliases: [ 'id' ]
    volume_group_id:
        description: The OCID of the volume group that needs to be backed up. Required to create a volume group backup
                     with I(state=present).
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a volume group backup
  oci_volume_group_backup:
    name: my_backup
    volume_group_id: ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx
    wait_until: CREATING

- name: Forcefully ensure non-idempotent volume group backup creation
  oci_volume_group_backup:
    name: my_backup
    volume_group_id: ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx
    force_create: True

- name: Update name of a volume group backup
  oci_volume_group_backup:
    name: test_backup
    id: ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx

- name: Delete a volume group backup
  oci_volume_group_backup:
    id: ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx
    state: absent
"""

RETURN = """
volume_group_backup:
    description: Information about the volume group backup
    returned: on successful create, delete and update operation
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment that contains the volume group backup.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: A user-friendly name for the volume group backup.
            returned: always
            type: string
            sample: test_backup
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: The OCID of the volume group backup.
            returned: always
            type: string
            sample: ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The current state of a volume group backup. Allowed values for this property are "CREATING",
                         "COMMITTED", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED",
                         'UNKNOWN_ENUM_VALUE'.
            returned: always
            type: string
            sample: AVAILABLE
        size_in_gbs:
            description: The aggregate size of the volume group backup, in GBs.
            returned: always
            type: string
            sample: 50
        size_in_mbs:
            description: The aggregate size of the volume group backup, in MBs.
            returned: always
            type: string
            sample: 51200
        time_created:
            description: The date and time the volume group backup was created. This is the time the actual
                         point-in-time image of the volume group data was taken. Format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-12-22T15:40:53.219000+00:00
        time_request_received:
            description: The date and time the request to create the volume group backup was received. Format defined by
                         RFC3339.
            returned: always
            type: string
            sample: 2017-12-22T15:40:48.111000+00:00
        type:
            description: The type of a volume group backup.
            returned: always
            type: string
            sample: FULL
        unique_size_in_gbs:
            description: The aggregate size used by the volume group backup, in GBs. It is typically smaller than
                         sizeInGBs, depending on the space consumed on the volume group and whether the volume backup is
                         full or incremental.
            returned: always
            type: string
            sample: 0
        unique_size_in_mbs:
            description: The aggregate size used by the volume group backup, in MBs. It is typically smaller than
                         sizeInMBs, depending on the space consumed on the volume group and whether the volume backup is
                         full or incremental.
            returned: always
            type: string
            sample: 1
        volume_backup_ids:
            description: OCIDs for the volume backups in this volume group backup.
            returned: always
            type: string
            sample: ["ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx"]
        volume_group_id:
            description: The OCID of the source volume group.
            returned: always
            type: string
            sample: ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx
    sample: {
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "defined_tags": {},
            "display_name": "ansible_backup",
            "freeform_tags": {},
            "id": "ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "size_in_gbs": 50,
            "size_in_mbs": 51200,
            "time_created": "2017-12-22T15:40:53.219000+00:00",
            "time_request_received": "2017-12-22T15:40:48.111000+00:00",
            "type": "FULL",
            "unique_size_in_gbs": 0,
            "unique_size_in_mbs": 1,
            "volume_backup_ids": ["ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx"],
            "volume_group_id": "ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils


try:
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.core.models import CreateVolumeGroupBackupDetails
    from oci.core.models import UpdateVolumeGroupBackupDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def delete_volume_group_backup(block_storage_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="volume_group_backup",
        client=block_storage_client,
        get_fn=block_storage_client.get_volume_group_backup,
        kwargs_get={"volume_group_backup_id": module.params["id"]},
        delete_fn=block_storage_client.delete_volume_group_backup,
        kwargs_delete={
            "volume_group_backup_id": module.params["volume_group_backup_id"]
        },
        module=module,
    )
    return result


def create_volume_group_backup(block_storage_client, module):
    cvgbd = CreateVolumeGroupBackupDetails()

    for attribute in cvgbd.attribute_map.keys():
        if attribute in module.params:
            setattr(cvgbd, attribute, module.params[attribute])

    result = oci_utils.create_and_wait(
        resource_type="volume_group_backup",
        create_fn=block_storage_client.create_volume_group_backup,
        kwargs_create={"create_volume_group_backup_details": cvgbd},
        client=block_storage_client,
        get_fn=block_storage_client.get_volume_group_backup,
        get_param="volume_group_backup_id",
        module=module,
        states=[module.params["wait_until"], "FAULTY", "AVAILABLE"],
    )

    return result


def update_volume_group_backup(block_storage_client, module):
    return oci_utils.check_and_update_resource(
        resource_type="volume_group_backup",
        client=block_storage_client,
        get_fn=block_storage_client.get_volume_group_backup,
        kwargs_get={"volume_group_backup_id": module.params["volume_group_backup_id"]},
        update_fn=block_storage_client.update_volume_group_backup,
        primitive_params_update=["volume_group_backup_id"],
        kwargs_non_primitive_update={
            UpdateVolumeGroupBackupDetails: "update_volume_group_backup_details"
        },
        module=module,
        update_attributes=UpdateVolumeGroupBackupDetails().attribute_map.keys(),
    )


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=False),
            display_name=dict(type="str", required=False, aliases=["name"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            type=dict(
                type="str",
                required=False,
                default="INCREMENTAL",
                choices=["FULL", "INCREMENTAL"],
            ),
            volume_group_backup_id=dict(type="str", required=False, aliases=["id"]),
            volume_group_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[["state", "absent", ["volume_group_backup_id"]]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    state = module.params["state"]
    volume_group_backup_id = module.params["volume_group_backup_id"]

    if state == "absent":
        result = delete_volume_group_backup(block_storage_client, module)

    else:
        if volume_group_backup_id is None:
            if module.params["compartment_id"]:
                compartment_id = module.params["compartment_id"]
            # Get compartment_id of volume group to list all the volume group backups of the volume group in that
            # compartment.
            else:
                compartment_id = block_storage_client.get_volume_group(
                    module.params["volume_group_id"]
                ).data.compartment_id
            result = oci_utils.check_and_create_resource(
                resource_type="volume_group_backup",
                create_fn=create_volume_group_backup,
                kwargs_create={
                    "block_storage_client": block_storage_client,
                    "module": module,
                },
                list_fn=block_storage_client.list_volume_group_backups,
                kwargs_list={
                    "compartment_id": compartment_id,
                    "volume_group_id": module.params["volume_group_id"],
                },
                module=module,
                model=CreateVolumeGroupBackupDetails(),
            )
        else:
            result = update_volume_group_backup(block_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
