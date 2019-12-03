#!/usr/bin/python
# Copyright (c) 2018, 2019, Oracle and/or its affiliates.
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
module: oci_volume_group_facts
short_description: Retrieve facts of volume groups in OCI Block Volume service
description:
    - This module retrieves information of a specified volume group or all the volume groups in a specified compartment.
version_added: "2.5"
options:
    availability_domain:
        description: The name of the Availability Domain.
        required: false
    compartment_id:
        description: The OCID of the compartment. Required to get information of all the volume groups in a specified
                     compartment.
        required: false
    volume_group_id:
        description: The OCID of the volume group. Required to get information of the specified volume group.
        required: false
        aliases: [ 'id' ]
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive. Allowed values are "PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING",
                     "TERMINATED", "FAULTY".
        required: false
        choices: ["PROVISIONING", "RESTORING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY"]
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of all the volume groups for a specific availability domain & compartment_id
  oci_volume_group_facts:
    availability_domain: BnQb:PHX-AD-1
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get information of a volume group
  oci_volume_group_facts:
    volume_group_id: ocid1.volumegroup.oc1.phx.xxxxxEXAMPLExxxxx
"""

RETURN = """
volume_groups:
    description: List of volume group information
    returned: On success
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
    sample: [{
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
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            availability_domain=dict(type="str", required=False),
            compartment_id=dict(type="str", required=False),
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
            volume_group_id=dict(type="str", required=False, aliases=["id"]),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "volume_group_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    volume_group_id = module.params["volume_group_id"]

    try:
        if volume_group_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        block_storage_client.get_volume_group,
                        volume_group_id=volume_group_id,
                    ).data
                )
            ]

        else:
            compartment_id = module.params["compartment_id"]
            optional_list_method_params = [
                "display_name",
                "lifecycle_state",
                "availability_domain",
            ]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    block_storage_client.list_volume_groups,
                    compartment_id=compartment_id,
                    **optional_kwargs
                )
            )

    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(volume_groups=result)


if __name__ == "__main__":
    main()
