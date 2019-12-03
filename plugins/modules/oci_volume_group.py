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
module: oci_volume_group
short_description: Manage volume groups in OCI Block Volume service
description:
    - This module allows the user to perform create, delete & update operations on volume groups in OCI Block Volume
      service.
version_added: "2.5"
options:
    availability_domain:
        description: The availability domain of the volume group. Required when creating a volume group with
                     I(state=present).
        required: false
    compartment_id:
        description: The OCID of the compartment that contains the volume group. Required when creating a volume group
                     with I(state=present).
        required: false
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information. If I(display_name) is not provided, it is auto-generated.
        required: False
        aliases: [ 'name' ]
    state:
        description: Create or update a volume group with I(state=present). Delete a volume group with I(state=absent).
        required: false
        default: present
        choices: ['present', 'absent']
    volume_group_id:
        description: The OCID of the volume group. Required when updating a volume group with I(state=present) or
                     deleting a volume group with I(state=absent).
        required: false
        aliases: [ 'id' ]
    volume_ids:
        description: OCIDs for the volumes in this volume group. Specify the full list of volume IDs to include in the
                     volume group when updating a volume group with I(state=present). If the volume ID is not specified
                     in the call, it will be removed from the volume group. For creating a volume group with a list of
                     volumes, use I(volume_ids) under I(source_details).
        required: false
    source_details:
        description: Specifies the volume group source details for a new volume group. The volume source is either a
                     list of volume ids in the same availability domain, another volume group or a volume group backup.
                     I(source_details) is required to create a volume group.
        required: false
        suboptions:
            volume_group_id:
                description: The OCID of the volume group to clone from.
                required: false
            volume_group_backup_id:
                description: The OCID of the volume group backup to restore from.
                required: false
            volume_ids:
                description: OCIDs for the volumes in this volume group.
                required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a clone of an existing volume group
  oci_volume_group:
    availability_domain: IwGV:US-ASHBURN-AD-2
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: ansible_volume_group
    source_details:
      volume_group_id: ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx

- name: Create a volume group initialized from a backup
  oci_volume_group:
    availability_domain: IwGV:US-ASHBURN-AD-2
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    source_details:
      volume_group_backup_id: ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx

- name: Create a volume group from a set of volumes
  oci_volume_group:
    availability_domain: IwGV:US-ASHBURN-AD-2
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    source_details:
      volume_ids:
        - 'ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx...abcd'
        - 'ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx...efgh'

- name: Update the display name of a volume group
  oci_volume_group:
    volume_group_id: ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx
    name: ansible_test_volume_group

- name: Update a volume group to remove a volume from the volume group
  oci_volume_group:
    availability_domain: IwGV:US-ASHBURN-AD-2
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    source_details:
      volume_ids:
        - 'ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx...efgh'

- name: Delete a volume group
  oci_volume_group:
    id: ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx
    state: 'absent'
"""

RETURN = """
volume_group:
    description: Information about the volume group
    returned: On successful operation
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain of the volume group.
            returned: always
            type: string
            sample: IwGV:US-ASHBURN-AD-2
        compartment_id:
            description: The OCID of the compartment that contains the volume group.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        defined_tags:
            description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
            returned: always
            type: string
            sample: {"Operations": {"CostCenter": "42"}}
        display_name:
            description: Name of the volume group.
            returned: always
            type: string
            sample: ansible_test_volume
        freeform_tags:
            description: Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name,
                         type, or namespace.
            returned: always
            type: string
            sample: {"Department": "Finance"}
        id:
            description: The OCID of the volume group.
            returned: always
            type: string
            sample: ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx
        is_hydrated:
            description: Specifies whether the newly created cloned volume group's data has finished copying from the
                         source volume group or backup.
            returned: always
            type: bool
            sample: False
        lifecycle_state:
            description: The current state of a volume group.
            returned: always
            type: string
            sample: PROVISIONING
        size_in_gbs:
            description: The aggregate size of the volume group in GBs.
            returned: always
            type: int
            sample: 50
        size_in_mbs:
            description: The aggregate size of the volume group in MBs.
            returned: always
            type: int
            sample: 51200
        source_details:
            description: The volume group source. The source is either another list of volume IDs in the same
                         availability domain, another volume group, or a volume group backup.
            returned: always
            type: dict
            contains:
                id:
                    description: The OCID of the volume group to clone from or OCIDs for the volumes in this volume
                                 group or OCID of the volume group backup to restore from.
                    returned: always
                    type: string
                    sample: ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx
                type:
                    description: Type of volume group source either 'volumeGroupBackupId' or 'volumeGroupId' or
                                 'volumeIds'.
                    returned: always
                    type: string
                    sample: volumeGroupBackupId
            sample: {
                     "id": "ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx",
                     "type": "volumeGroupBackupId"
            }
        time_created:
            description: The date and time the volume group was created. Format defined by RFC3339.
            returned: always
            type: datetime
            sample: 2017-11-22T19:40:08.871000+00:00
        volume_ids:
            description: OCIDs for the volumes in this volume group.
            returned: always
            type: datetime
            sample: ['ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx']
    sample: {
            "availability_domain": "IwGV:US-ASHBURN-AD-2",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible_test_volume_group",
            "id": "ocid1.volumegroup.oc1.iad.xxxxxEXAMPLExxxxx",
            "is_hydrated": true,
            "lifecycle_state": "AVAILABLE",
            "size_in_gbs": 50,
            "size_in_mbs": 51200,
            "source_details": {
                "id": "ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx",
                "type": "volumeGroupBackupId"
            },
            "time_created": "2017-12-05T15:35:28.747000+00:00",
            "volume_ids": ['ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx']
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.core.models import CreateVolumeGroupDetails
    from oci.core.models import UpdateVolumeGroupDetails
    from oci.core.models import VolumeGroupSourceFromVolumeGroupBackupDetails
    from oci.core.models import VolumeGroupSourceFromVolumeGroupDetails
    from oci.core.models import VolumeGroupSourceFromVolumesDetails

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def handle_delete_volume_group(block_storage_client, module):
    return oci_utils.delete_and_wait(
        resource_type="volume_group",
        client=block_storage_client,
        get_fn=block_storage_client.get_volume_group,
        kwargs_get={"volume_group_id": module.params["volume_group_id"]},
        delete_fn=block_storage_client.delete_volume_group,
        kwargs_delete={"volume_group_id": module.params["volume_group_id"]},
        module=module,
    )


def handle_create_volume_group(block_storage_client, module):
    create_volume_group_details = CreateVolumeGroupDetails()

    for attribute in create_volume_group_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_volume_group_details, attribute, module.params[attribute])

    source_details = module.params["source_details"]
    volume_group_source = None

    if source_details.get("volume_ids"):
        volume_group_source = VolumeGroupSourceFromVolumesDetails()
        volume_group_source.volume_ids = source_details["volume_ids"]
    elif source_details.get("volume_group_backup_id"):
        volume_group_source = VolumeGroupSourceFromVolumeGroupBackupDetails()
        volume_group_source.volume_group_backup_id = source_details[
            "volume_group_backup_id"
        ]
    elif source_details.get("volume_group_id"):
        volume_group_source = VolumeGroupSourceFromVolumeGroupDetails()
        volume_group_source.volume_group_id = source_details["volume_group_id"]
    else:
        module.fail_json(
            msg="Specify one of the following under source_details: 'volume_ids', "
            "'volume_group_backup_id', 'volume_group_id'."
        )

    create_volume_group_details.source_details = volume_group_source

    result = oci_utils.create_and_wait(
        resource_type="volume_group",
        create_fn=block_storage_client.create_volume_group,
        kwargs_create={"create_volume_group_details": create_volume_group_details},
        client=block_storage_client,
        get_fn=block_storage_client.get_volume_group,
        get_param="volume_group_id",
        module=module,
    )
    return result


def handle_update_volume_group(block_storage_client, module):
    return oci_utils.check_and_update_resource(
        resource_type="volume_group",
        client=block_storage_client,
        get_fn=block_storage_client.get_volume_group,
        kwargs_get={"volume_group_id": module.params["volume_group_id"]},
        update_fn=block_storage_client.update_volume_group,
        primitive_params_update=["volume_group_id"],
        kwargs_non_primitive_update={
            UpdateVolumeGroupDetails: "update_volume_group_details"
        },
        module=module,
        update_attributes=UpdateVolumeGroupDetails().attribute_map.keys(),
    )


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
            volume_group_id=dict(type="str", required=False, aliases=["id"]),
            display_name=dict(type="str", required=False, aliases=["name"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            volume_ids=dict(type="list", required=False),
            source_details=dict(type="dict", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_if=[["state", "absent", ["volume_group_id"]]],
        mutually_exclusive=[["volume_ids", "source_details"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    state = module.params["state"]
    volume_group_id = module.params["volume_group_id"]

    if state == "absent":
        result = handle_delete_volume_group(block_storage_client, module)

    else:
        if volume_group_id is None:
            result = oci_utils.check_and_create_resource(
                resource_type="volume_group",
                create_fn=handle_create_volume_group,
                kwargs_create={
                    "block_storage_client": block_storage_client,
                    "module": module,
                },
                list_fn=block_storage_client.list_volume_groups,
                kwargs_list={
                    "compartment_id": module.params["compartment_id"],
                    "availability_domain": module.params["availability_domain"],
                },
                module=module,
                model=CreateVolumeGroupDetails(),
            )

        else:
            result = handle_update_volume_group(block_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
