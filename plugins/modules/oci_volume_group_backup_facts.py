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
module: oci_volume_group_backup_facts
short_description: Retrieve facts of volume group backups in OCI Block Volume service
description:
    - This module retrieves information of a specified volume group backup or all the volume group backups in a
      compartment in OCI Block Volume service.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment.
        required: false
    volume_group_backup_id:
        description: The OCID of the volume group backup.
        required: false
        aliases: [ 'id' ]
    volume_group_id:
        description: The OCID of the volume group.
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of all the volume group backups in a compartment
  oci_volume_group_backup_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get information of a volume group backup
  oci_volume_group_backup_facts:
    id: ocid1.volumegroupbackup.oc1.iad.xxxxxEXAMPLExxxxx
"""

RETURN = """
volume_group_backups:
    description: List of volume group backup information
    returned: on success
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
    sample: [{
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
            compartment_id=dict(type="str", required=False),
            volume_group_backup_id=dict(type="str", required=False, aliases=["id"]),
            volume_group_id=dict(type="str", required=False),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        required_one_of=[["compartment_id", "volume_group_backup_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    volume_group_backup_id = module.params["volume_group_backup_id"]

    try:
        if volume_group_backup_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        block_storage_client.get_volume_group_backup,
                        volume_group_backup_id=volume_group_backup_id,
                    ).data
                )
            ]

        else:
            compartment_id = module.params["compartment_id"]
            optional_list_method_params = ["display_name", "volume_group_id"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    block_storage_client.list_volume_group_backups,
                    compartment_id=compartment_id,
                    **optional_kwargs
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(volume_group_backups=result)


if __name__ == "__main__":
    main()
