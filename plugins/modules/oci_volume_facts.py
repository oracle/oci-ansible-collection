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
module: oci_volume_facts
short_description: Retrieve facts of volumes in OCI Block Volume service
description:
    - This module retrieves information of a specified volume or all the volumes in a specified compartment and
      availability domain.
version_added: "2.5"
options:
    availability_domain:
        description: The name of the Availability Domain.
        required: false
    compartment_id:
        description: The OCID of the compartment. Required to get information of all the volumes in a specified
                     compartment. This option is mutually exclusive with I(volume_id).
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
    volume_id:
        description: The OCID of the volume. Required to get information of a specific volume. This option is mutually
                     exclusive with I(compartment_id).
        required: false
        aliases: [ 'id' ]
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive. Allowed values are "PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING",
                     "TERMINATED", "FAULTY".
        required: false
        choices: ["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]
    volume_group_id:
        description: The OCID of the volume group.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of all the volumes for a specific availability domain & compartment_id
  oci_volume_facts:
    availability_domain: BnQb:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get information of a volume
  oci_volume_facts:
    volume_id: ocid1.volume.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
volumes:
    description: List of volume information
    returned: On success
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
            returned: always
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils
from ansible.module_utils.oracle.oci_utils import check_mode

try:
    from oci.core.blockstorage_client import BlockstorageClient
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


@check_mode
def add_attached_instance_info(module, volumes, lookup_attached_instance):
    compute_client = oci_utils.create_service_client(module, ComputeClient)

    if volumes:
        for volume in volumes:
            try:
                volume[
                    "attached_instance_information"
                ] = oci_utils.get_attached_instances_info(
                    module,
                    lookup_attached_instance,
                    list_attachments_fn=compute_client.list_volume_attachments,
                    list_attachments_args={
                        "volume_id": volume["id"],
                        "compartment_id": volume["compartment_id"],
                    },
                )
            except ServiceError as ex:
                module.fail_json(msg=ex.message)

    return volumes


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
            volume_id=dict(type="str", required=False, aliases=["id"]),
            lookup_all_attached_instances=dict(
                type="bool", required=False, default="no"
            ),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=[
                    "PROVISIONING",
                    "RESTORING",
                    "AVAILABLE",
                    "TERMINATING",
                    "TERMINATED",
                    "FAULTY",
                ],
            ),
            volume_group_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[["compartment_id", "volume_id"]],
        required_one_of=[["compartment_id", "volume_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    volume_id = module.params["volume_id"]

    try:
        if volume_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        block_storage_client.get_volume, volume_id=volume_id
                    ).data
                )
            ]

        else:
            compartment_id = module.params["compartment_id"]
            availability_domain = module.params["availability_domain"]
            if availability_domain is not None:
                result = to_dict(
                    oci_utils.list_all_resources(
                        block_storage_client.list_volumes,
                        compartment_id=compartment_id,
                        availability_domain=availability_domain,
                        display_name=module.params["display_name"],
                    )
                )
            else:
                optional_list_method_params = [
                    "display_name",
                    "lifecycle_state",
                    "volume_group_id",
                ]
                optional_kwargs = dict(
                    (param, module.params[param])
                    for param in optional_list_method_params
                    if module.params.get(param) is not None
                )
                result = to_dict(
                    oci_utils.list_all_resources(
                        block_storage_client.list_volumes,
                        compartment_id=compartment_id,
                        **optional_kwargs
                    )
                )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    add_attached_instance_info(
        module, result, module.params["lookup_all_attached_instances"]
    )

    module.exit_json(volumes=result)


if __name__ == "__main__":
    main()
