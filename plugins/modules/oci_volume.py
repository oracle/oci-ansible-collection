#!/usr/bin/python
# Copyright (c) 2017, 2018, 2019, Oracle and/or its affiliates.
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
module: oci_volume
short_description: Manage volumes in OCI Block Volume service
description:
    - This module allows the user to perform create, delete & update operations on volumes in OCI Block Volume service.
version_added: "2.5"
options:
    availability_domain:
        description: The availability domain of the volume. Required when creating a volume with I(state=present).
        required: false
    backup_policy_id:
        description: ID of the volume backup policy to assign to the newly created volume. If omitted, no policy will be
                     assigned. I(backup_policy_id) can only be provided while creating a volume.
        required: false
    compartment_id:
        description: The OCID of the compartment that contains the volume. Required when creating a volume with
                     I(state=present).
        required: false
    lookup_all_attached_instances:
        description: Whether to fetch information of compute instances attached to this volume from all the compartments
                     in the tenancy.Fetching this information requires traversing through all the compartments in the
                     Tenancy and therefore can potentially take a long time. This option is only supported in
                     experimental mode.

                     When I(lookup_all_attached_instances=False), only attached compute instances
                     belonging to this volume's compartment, is returned. This is useful when the volume is used within
                     a single compartment. When I(lookup_all_attached_instances=True), all the compartments in the
                     tenancy are searched to find out the compute instances that are attached to this volume. Fetching
                     information about compute instances attached to this volume is an experimental feature
                     (ie, this may or may not be supported in future releases). To use such experimental features, set
                     the environment variable OCI_ANSIBLE_EXPERIMENTAL to True.
        required: false
        default: no
        type: bool
    display_name:
        description: A user-friendly name. Does not have to be unique, and it's changeable. Avoid entering confidential
                     information. If I(display_name) is not provided, it is auto-generated.
        required: False
        aliases: [ 'name' ]
    size_in_gbs:
        description: The size of the volume in GBs.
        required: false
        default: 50
    state:
        description: Create or update a volume with I(state=present). Delete a volume with I(state=absent).
        required: false
        default: present
        choices: ['present', 'absent']
    volume_id:
        description: The OCID of the volume. Required when updating a volume with I(state=present) or deleting a volume
                     with I(state=absent).
        required: false
        aliases: [ 'id' ]
    source_details:
        description: Specifies the volume source details for a new Block volume. The volume source is either another
                     Block volume in the same Availability Domain or a Block volume backup. This is an optional field.
                     If not specified or set to null, the new Block volume will be empty. When specified, the new Block
                     volume will contain data from the source volume or backup.
        required: false
        suboptions:
            id:
                description: The OCID of the volume backup from which the data should be restored on the newly created
                             volume when I(source_details.type=volumeBackup) or the OCID of the volume to be cloned when
                             I(source_details.type=volume).
                required: false
            type:
                description: Type of volume source details. Use I(source_details.type=volumeBackup) for restoring a
                             volume backup. Use I(source_details.type=volume) for cloning a volume.
                required: false
                choices: ['volumeBackup', 'volume']
            wait_for_copy:
                description: Whether to wait for the operation of copying from source volume or backup to complete when
                             I(source_details.id) is specified under C(source_details).
                required: false
                default: no
                type: bool
            copy_timeout:
                description: Time, in seconds, to wait for the operation to complete when I(wait_for_copy=yes).
                required: false
                default: 1800
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
- name: Create a volume
  oci_volume:
    availability_domain: IwGV:US-ASHBURN-AD-2
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: ansible_volume
    wait: no

- name: Create a clone of an existing volume
  oci_volume:
    availability_domain: IwGV:US-ASHBURN-AD-2
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: ansible_volume
    source_details:
      id: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx
      type: volume
      wait_for_copy: yes
      copy_timeout: 900

- name: Create a volume and initialize it from a backup
  oci_volume:
    availability_domain: IwGV:US-ASHBURN-AD-2
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    name: ansible_volume
    source_details:
      id: ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx
      type: volumeBackup

- name: Update a volume
  oci_volume:
    name: ansible_test_volume
    volume_id: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx

- name: Delete a volume
  oci_volume:
    volume_id: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx
    state: 'absent'
"""

RETURN = """
volume:
    description: Information about the volume
    returned: On successful create and update operation
    type: complex
    contains:
        availability_domain:
            description: The Availability Domain of the volume.
            returned: always
            type: string
            sample: IwGV:US-ASHBURN-AD-2
        compartment_id:
            description: The OCID of the compartment that contains the volume.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: Name of the volume.
            returned: always
            type: string
            sample: ansible_test_volume
        id:
            description: The OCID of the volume.
            returned: always
            type: string
            sample: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx
        is_hydrated:
            description: Specifies whether the cloned volume's data has finished copying from the source volume or
                         backup.
            returned: always
            type: bool
            sample: False
        lifecycle_state:
            description: The current state of a volume.
            returned: always
            type: string
            sample: PROVISIONING
        size_in_gbs:
            description: The size of the volume in GBs.
            returned: always
            type: int
            sample: 50
        size_in_mbs:
            description: The size of the volume in MBs.
            returned: always
            type: int
            sample: 51200
        source_details:
            description: The volume source, either an existing volume in the same Availability Domain or a volume
                         backup.
            returned: always
            type: dict
            contains:
                id:
                    description: The OCID of the source volume or the OCID of the volume backup.
                    returned: When a volume is initialized from a source volume or a backup.
                    type: string
                    sample: ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx
                type:
                    description: Type of volume source either 'volumeBackup' or 'volume'.
                    returned: When a volume is initialized from a source volume or a backup.
                    type: string
                    sample: volumeBackup
            sample: {
                     "id": "ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx",
                     "type": "volumeBackup"
            }
        time_created:
            description: The date and time the volume was created. Format defined by RFC3339.
            returned: always
            type: datetime
            sample: 2017-11-22T19:40:08.871000+00:00
        attached_instance_information:
            description: Information of instances currently attached to the block volume.
            returned: In experimental mode.
            type: list
            contains:
                attachment_type:
                    description: The type of volume attachment.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: iscsi
                availability_domain:
                    description: The Availability Domain of an instance.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: BnQb:PHX-AD-1
                chap_secret:
                    description: The Challenge-Handshake-Authentication-Protocol (CHAP) secret valid for the associated CHAP
                         user name. (Also called the "CHAP password".)
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: d6866c0d-298b-48ba-95af-309b4faux45e
                chap_username:
                    description: The volume's system-generated Challenge-Handshake-Authentication-Protocol (CHAP) user name.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
                compartment_id:
                    description: The OCID of the compartment.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
                display_name:
                    description: A user-friendly name. Does not have to be unique, and it cannot be changed.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: My volume attachment
                id:
                    description: The OCID of the volume attachment.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: ocid1.volumeattachment.oc1.phx.xxxxxEXAMPLExxxxx
                instance_id:
                    description: The OCID of the instance the volume is attached to.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: ocid1.instance.oc1.phx.xxxxxEXAMPLExxxxx
                ipv4:
                    description: The volume's iSCSI IP address.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: 169.254.0.2
                iqn:
                    description: The target volume's iSCSI Qualified Name in the format defined by RFC 3720.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: iqn.2015-12.us.oracle.com:456b0391-17b8-4122-bbf1-f85fc0bb97d9
                lifecycle_state:
                    description: The current state of the volume attachment.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: ATTACHED
                port:
                    description: The volume's iSCSI port.
                    returned: when this volume is attached to a compute instance
                    type: int
                    sample: 3260
                time_created:
                    description: The date and time the volume was created, in the format defined by RFC3339.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: 2016-08-25T21:10:29.600Z
                volume_id:
                    description: The OCID of the volume.
                    returned: when this volume is attached to a compute instance
                    type: string
                    sample: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
    sample: {
            "availability_domain": "IwGV:US-ASHBURN-AD-2",
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible_test_volume",
            "id": "ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx",
            "is_hydrated": true,
            "lifecycle_state": "AVAILABLE",
            "size_in_gbs": 50,
            "size_in_mbs": 51200,
            "source_details": {
                "id": "ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx",
                "type": "volume"
            },
            "time_created": "2017-12-05T15:35:28.747000+00:00",
            "attached_instance_information": [{
                        "attachment_type": "iscsi",
                        "availability_domain": "IwGV:US-ASHBURN-AD-2",
                        "chap_secret": null,
                        "chap_username": null,
                        "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
                        "display_name": "volumeattachment20171204124856",
                        "id": "ocid1.volumeattachment.oc1.iad.xxxxxEXAMPLExxxxx",
                        "instance_id": "ocid1.instance.oc1.iad.xxxxxEXAMPLExxxxx",
                        "ipv4": "169.254.2.7",
                        "iqn": "iqn.2015-12.com.oracleiaas:8ea342ff-4687-4038-b733-d20cb1025b48",
                        "lifecycle_state": "ATTACHED",
                        "port": 3260,
                        "time_created": "2017-12-04T12:48:56.497000+00:00",
                        "volume_id": "ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx"
            }]
        }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle.oci_utils import check_mode

try:
    import oci
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.core.compute_client import ComputeClient
    from oci.core.models.create_volume_details import CreateVolumeDetails
    from oci.core.models.update_volume_details import UpdateVolumeDetails
    from oci.core.models import VolumeSourceFromVolumeBackupDetails
    from oci.core.models import VolumeSourceFromVolumeDetails
    from oci.util import to_dict
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


def handle_delete_volume(block_storage_client, module):
    return oci_utils.delete_and_wait(
        resource_type="volume",
        client=block_storage_client,
        get_fn=block_storage_client.get_volume,
        kwargs_get={"volume_id": module.params["volume_id"]},
        delete_fn=block_storage_client.delete_volume,
        kwargs_delete={"volume_id": module.params["volume_id"]},
        module=module,
    )


def handle_create_volume(block_storage_client, module):
    create_volume_details = CreateVolumeDetails()

    for attribute in create_volume_details.attribute_map.keys():
        if attribute in module.params:
            setattr(create_volume_details, attribute, module.params[attribute])

    if module.params["source_details"]:
        source_details = module.params["source_details"]
        volume_source = None
        if "type" in source_details:
            if source_details["type"] == "volume":
                volume_source = VolumeSourceFromVolumeDetails()
                volume_source.id = source_details.get("id")

            elif source_details["type"] == "volumeBackup":
                volume_source = VolumeSourceFromVolumeBackupDetails()
                volume_source.id = source_details.get("id")

            else:
                module.fail_json(
                    msg="value of state must be one of: volume, volumeBackup"
                )

        else:
            module.fail_json(msg="missing required arguments: type")

        create_volume_details.source_details = volume_source

    result = oci_utils.create_and_wait(
        resource_type="volume",
        create_fn=block_storage_client.create_volume,
        kwargs_create={"create_volume_details": create_volume_details},
        client=block_storage_client,
        get_fn=block_storage_client.get_volume,
        get_param="volume_id",
        module=module,
    )

    wait_for_copy = False
    copy_timeout = 1800
    WAIT_FOR_INITIALIZATION = "wait_for_copy"
    INITIALIZATION_TIMEOUT = "copy_timeout"

    if create_volume_details.source_details is not None:
        if WAIT_FOR_INITIALIZATION in source_details:
            wait_for_copy = source_details[WAIT_FOR_INITIALIZATION]
            if INITIALIZATION_TIMEOUT in source_details:
                copy_timeout = source_details[INITIALIZATION_TIMEOUT]

    try:
        response = oci_utils.call_with_backoff(
            block_storage_client.get_volume, volume_id=result["volume"]["id"]
        )

        if wait_for_copy:
            result["volume"] = to_dict(
                oci.wait_until(
                    block_storage_client,
                    response,
                    "is_hydrated",
                    True,
                    max_wait_seconds=copy_timeout,
                ).data
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)
    except MaximumWaitTimeExceeded as ex:
        module.fail_json(msg=str(ex))

    return result


def handle_update_volume(block_storage_client, module):
    return oci_utils.check_and_update_resource(
        resource_type="volume",
        client=block_storage_client,
        get_fn=block_storage_client.get_volume,
        kwargs_get={"volume_id": module.params["volume_id"]},
        update_fn=block_storage_client.update_volume,
        primitive_params_update=["volume_id"],
        kwargs_non_primitive_update={UpdateVolumeDetails: "update_volume_details"},
        module=module,
        update_attributes=UpdateVolumeDetails().attribute_map.keys(),
    )


@check_mode
def add_attached_instance_info(module, result, lookup_attached_instance):
    compute_client = oci_utils.create_service_client(module, ComputeClient)

    if "volume" in result:
        try:
            result["volume"][
                "attached_instance_information"
            ] = oci_utils.get_attached_instances_info(
                module,
                lookup_attached_instance,
                list_attachments_fn=compute_client.list_volume_attachments,
                list_attachments_args={
                    "volume_id": result["volume"]["id"],
                    "compartment_id": result["volume"]["compartment_id"],
                },
            )
        except ServiceError as ex:
            module.fail_json(msg=ex.message)


def main():
    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=False),
            backup_policy_id=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
            volume_id=dict(type="str", required=False, aliases=["id"]),
            display_name=dict(type="str", required=False, aliases=["name"]),
            size_in_gbs=dict(type="int", required=False, default=50),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["absent", "present"],
            ),
            source_details=dict(type="dict", required=False),
            lookup_all_attached_instances=dict(
                type="bool", required=False, default="no"
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_together=[["availability_domain", "compartment_id"]],
        required_if=[["state", "absent", ["volume_id"]]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    state = module.params["state"]
    volume_id = module.params["volume_id"]

    if state == "absent":
        result = handle_delete_volume(block_storage_client, module)

    else:
        if volume_id is None:
            # Exclude size_in_mbs as it is deprecated but still in the CreateVolumeDetails.

            # Though the documentation
            # (https://oracle-cloud-infrastructure-python-sdk.readthedocs.io/en/latest/api/index.html#id194) says
            #  volumes are by default 1 TB but volumes get created with 50 GB size.
            exclude_attributes = {"size_in_mbs": True, "display_name": True}
            default_attribute_values = {"source_details": None, "size_in_gbs": 50}

            # If a user expects volume to be created from a volume backup or from an another volume using option
            # `source_details` and doesn't specify the option `size_in_gbs`, the default for `size_in_gbs` option should
            # be set to None and this option should be excluded while matching with existing volumes.
            if module.params["source_details"]:
                if not oci_utils.has_user_provided_value_for_option(
                    module, "size_in_gbs"
                ):
                    module.params["size_in_gbs"] = None
                    exclude_attributes["size_in_gbs"] = True
            result = oci_utils.check_and_create_resource(
                resource_type="volume",
                create_fn=handle_create_volume,
                kwargs_create={
                    "block_storage_client": block_storage_client,
                    "module": module,
                },
                list_fn=block_storage_client.list_volumes,
                kwargs_list={"compartment_id": module.params["compartment_id"]},
                module=module,
                model=CreateVolumeDetails(),
                exclude_attributes=exclude_attributes,
                default_attribute_values=default_attribute_values,
            )

        else:
            result = handle_update_volume(block_storage_client, module)

    add_attached_instance_info(
        module, result, module.params["lookup_all_attached_instances"]
    )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
