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
module: oci_volume_backup_facts
short_description: Retrieve facts of volume backups in OCI Block Volume service
description:
    - This module retrieves information of a specified volume backup or all the volume backups in a compartment in OCI
      Block Volume service.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment.
        required: false
    volume_backup_id:
        description: The OCID of the volume backup.
        required: false
        aliases: [ 'id' ]
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive. Allowed values are "CREATING", "AVAILABLE", "TERMINATING", "TERMINATED",
                     "FAULTY", "REQUEST_RECEIVED".
        required: false
        choices: ["CREATING", "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED"]
    volume_id:
        description: The OCID of the volume
        required: false
author: "Rohit Chaware (@rohitChaware)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get information of all the volume backups in a compartment
  oci_volume_backup_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx

- name: Get information of a volume backup
  oci_volume_backup_facts:
    id: ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx
"""

RETURN = """
volume_backups:
    description: List of volume backup information
    returned: on success
    type: complex
    contains:
        compartment_id:
            description: The OCID of the compartment that contains the volume backup.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: A user-friendly name for the volume backup.
            returned: always
            type: string
            sample: test_backup
        id:
            description: The OCID of the volume backup.
            returned: always
            type: string
            sample: ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx
        lifecycle_state:
            description: The current state of a volume backup. Allowed values for this property are "CREATING",
                         "AVAILABLE", "TERMINATING", "TERMINATED", "FAULTY", "REQUEST_RECEIVED", 'UNKNOWN_ENUM_VALUE'.
            returned: always
            type: string
            sample: AVAILABLE
        size_in_gbs:
            description: The size of the volume, in GBs.
            returned: always
            type: string
            sample: 50
        size_in_mbs:
            description: The size of the volume, in MBs.
            returned: always
            type: string
            sample: 51200
        time_created:
            description: The date and time the volume backup was created. This is the time the actual point-in-time
                         image of the volume data was taken. Format defined by RFC3339.
            returned: always
            type: string
            sample: 2017-12-22T15:40:53.219000+00:00
        time_request_received:
            description: The date and time the request to create the volume backup was received. Format defined by
                         RFC3339.
            returned: always
            type: string
            sample: 2017-12-22T15:40:48.111000+00:00
        unique_size_in_gbs:
            description: The size used by the backup, in GBs. It is typically smaller than sizeInGBs, depending on the
                         space consumed on the volume and whether the backup is full or incremental.
            returned: always
            type: string
            sample: 0
        unique_size_in_mbs:
            description: The size used by the backup, in MBs. It is typically smaller than sizeInMBs, depending on the
                         space consumed on the volume and whether the backup is full or incremental.
            returned: always
            type: string
            sample: 1
        volume_id:
            description: The OCID of the volume.
            returned: always
            type: string
            sample: ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "ansible_backup",
            "id": "ocid1.volumebackup.oc1.iad.xxxxxEXAMPLExxxxx",
            "lifecycle_state": "AVAILABLE",
            "size_in_gbs": 50,
            "size_in_mbs": 51200,
            "time_created": "2017-12-22T15:40:53.219000+00:00",
            "time_request_received": "2017-12-22T15:40:48.111000+00:00",
            "unique_size_in_gbs": 0,
            "unique_size_in_mbs": 1,
            "volume_id": "ocid1.volume.oc1.iad.xxxxxEXAMPLExxxxx"
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
            volume_backup_id=dict(type="str", required=False, aliases=["id"]),
            volume_id=dict(type="str", required=False),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=[
                    "CREATING",
                    "AVAILABLE",
                    "TERMINATING",
                    "TERMINATED",
                    "FAULTY",
                    "REQUEST_RECEIVED",
                ],
            ),
        )
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False,
        mutually_exclusive=[["compartment_id", "volume_backup_id"]],
        required_one_of=[["compartment_id", "volume_backup_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    block_storage_client = oci_utils.create_service_client(module, BlockstorageClient)

    volume_backup_id = module.params["volume_backup_id"]

    try:
        if volume_backup_id is not None:
            result = [
                to_dict(
                    oci_utils.call_with_backoff(
                        block_storage_client.get_volume_backup,
                        volume_backup_id=volume_backup_id,
                    ).data
                )
            ]

        else:
            compartment_id = module.params["compartment_id"]
            optional_list_method_params = [
                "display_name",
                "lifecycle_state",
                "volume_id",
            ]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            result = to_dict(
                oci_utils.list_all_resources(
                    block_storage_client.list_volume_backups,
                    compartment_id=compartment_id,
                    **optional_kwargs
                )
            )
    except ServiceError as ex:
        module.fail_json(msg=ex.message)

    module.exit_json(volume_backups=result)


if __name__ == "__main__":
    main()
