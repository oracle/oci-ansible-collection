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
module: oci_snapshot_facts
short_description: Fetches details of the OCI Snapshot instances
description:
    - Fetches details of the OCI Snapshot instances.
version_added: "2.5"
options:
    file_system_id:
        description: The identifier of the File System of which Snapshot has been taken
        required: false
    snapshot_id:
        description: Identifier of the Snapshot whose details needs to be fetched.
        required: false
        aliases: ['id']
    lifecycle_state:
        description: A filter to only return resources that match the given lifecycle state.  The state value is
                     case-insensitive.
        required: false
        choices: ['CREATING', 'ACTIVE', 'DELETING', 'DELETED', 'FAILED']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle ]
"""

EXAMPLES = """
# Fetch Snapshot
- name: List all Snapshots of a specific File System
  oci_snapshot_facts:
      file_system_id: 'ocid1.filesystem..xxxxxEXAMPLExxxxx'

# Fetch Snapshots, filtered by lifecycle state
- name: List all Snapshots of a specific File System, filtered by lifecycle state
  oci_snapshot_facts:
      file_system_id: 'ocid1.filesystem..xxxxxEXAMPLExxxxx'
      lifecycle_state: 'CREATING'

# Fetch specific Snapshot
- name: List a specific Snapshot
  oci_snapshot_facts:
      snapshot_id: 'ocid1.snapshot..xxxxxEXAMPLExxxxx'
"""

RETURN = """
    snapshots:
        description: Attributes of the Fetched Snapshots.
        returned: success
        type: complex
        contains:
            file_system_id:
                description: The identifier of the File System of which Snapshot has been taken
                returned: always
                type: string
                sample: ocid1.filesystem.oc1.xzvf..xxxxxEXAMPLExxxxx
            name:
                description: The user-friendly name for the Snapshot.
                returned: always
                type: string
                sample: ansible-snapshot
            defined_tags:
                description: Defined tags for this resource. Each key is predefined and scoped to a namespace.
                             For more information, see
                             U(https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm).
                returned: always
                type: dict
                sample: {"Department": "Finance"}
            freeform_tags:
                description: Free-form tags for this resource. Each tag is a simple key-value pair with no
                             predefined name, type, or namespace. For more information, see
                             U(https://docs.us-phoenix-1.oraclecloud.com/Content/General/Concepts/resourcetags.htm).
                returned: always
                type: dict
                sample: {"Operations": {"CostCenter": "42"}}
            id:
                description: The identifier of the Snapshot
                returned: always
                type: string
                sample: ocid1.snapshot.oc1.xzvf..xxxxxEXAMPLExxxxx
            lifecycle_state:
                description: The current state of the Snapshot.
                returned: always
                type: string
                sample: ACTIVE
            time_created:
                description: Date and time when the Snapshot was created, in
                             the format defined by RFC3339
                returned: always
                type: datetime
                sample: 2018-10-16T09:43:24.328000+00:00

        sample: [{
                   "file_system_id":"ocid1.filesystem.oc1.iad.xxxxxEXAMPLExxxxx",
                   "id":"ocid1.snapshot.oc1.iad.xxxxxEXAMPLExxxxx",
                   "defined_tags":{
                                   "ansible_tag_namespace_integration_test_1":{
                                   "ansible_tag_1":"initial"
                                 }
                                },
                   "freeform_tags":{
                                   "system_license":"trial"
                                  },
                   "lifecycle_state":"ACTIVE",
                   "name":"ansible_snapshot",
                   "time_created":"2018-10-16T09:43:24.328000+00:00"
                }]

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.file_storage.file_storage_client import FileStorageClient
    from oci.exceptions import ServiceError
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = None


def list_snapshots(file_storage_client, module):
    result = dict(snapshots="")
    file_system_id = module.params.get("file_system_id")
    snapshot_id = module.params.get("snapshot_id")
    try:
        if file_system_id:
            get_logger().debug(
                "Listing all Snapshots under File System %s", file_system_id
            )
            optional_list_method_params = ["lifecycle_state"]
            optional_kwargs = dict(
                (param, module.params[param])
                for param in optional_list_method_params
                if module.params.get(param) is not None
            )
            existing_snapshots_summary = to_dict(
                oci_utils.list_all_resources(
                    file_storage_client.list_snapshots,
                    file_system_id=file_system_id,
                    **optional_kwargs
                )
            )
            existing_snapshots = [
                oci_utils.call_with_backoff(
                    file_storage_client.get_snapshot, snapshot_id=snapshot["id"]
                ).data
                for snapshot in existing_snapshots_summary
            ]
        elif snapshot_id:
            get_logger().debug("Listing Snapshot %s", snapshot_id)
            response = oci_utils.call_with_backoff(
                file_storage_client.get_snapshot, snapshot_id=snapshot_id
            )
            existing_snapshots = [response.data]
        else:
            module.fail_json(
                msg="No value provided for either file_system_id or snapshot_id"
            )
    except ServiceError as ex:
        get_logger().error("Unable to list Snapshots due to %s", ex.message)
        module.fail_json(msg=ex.message)
    result["snapshots"] = to_dict(existing_snapshots)
    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_snapshot_facts")
    set_logger(logger)
    module_args = oci_utils.get_common_arg_spec()
    module_args.update(
        dict(
            file_system_id=dict(type="str", required=False),
            snapshot_id=dict(type="str", required=False, aliases=["id"]),
            lifecycle_state=dict(
                type="str",
                required=False,
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
        )
    )
    module = AnsibleModule(
        argument_spec=module_args,
        mutually_exclusive=[["file_system_id", "snapshot_id"]],
    )

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    result = list_snapshots(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
