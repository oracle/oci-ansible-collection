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
module: oci_snapshot
short_description: Create and delete a Snapshot in OCI Filesystem Service.
description:
    - Create an OCI Snapshot
    - Delete an OCI Snapshot, if present.
version_added: "2.5"
options:
    file_system_id:
        description: Identifier of the of the file system to take a snapshot of. Mandatory for create operation.
        required: false
    name:
        description: Name of the snapshot. This value is immutable. It must also be unique with respect to all other
                     non-DELETED snapshots on the associated file system. Avoid entering confidential information.
        required: false
    snapshot_id:
        description: Identifier of the existing Snapshot which required to be deleted.
                     Mandatory for delete.
        required: false
        aliases: ['id']
    state:
        description: Create, update and delete Snapshot. For I(state=present), if it does not exist, it gets created.
        required: false
        default: 'present'
        choices: ['present','absent']
author:
    - "Debayan Gupta(@debayan_gupta)"
extends_documentation_fragment: [ oracle, oracle_creatable_resource, oracle_wait_options, oracle_tags ]
"""

EXAMPLES = """
# Note: These examples do not set authentication details.
# Create Snapshot
- name: Create Snapshot
  oci_snapshot:
    file_system_id: 'ocid1.filesystem.oc1..xxxxxEXAMPLExxxxx'
    name: 'ansible_snapshot'
    freeform_tags:
        deployment: 'production'
    defined_tags:
        target_users:
            division: 'documentation'
    state: 'present'

# Update Snapshot's Freeform Tags
- name: Update Snapshot's Freeform Tags
  oci_snapshot:
    snapshot_id: 'ocid1.snapshot.oc1..xxxxxEXAMPLExxxxx'
    freeform_tags:
        deployment: 'trial'
    state: 'present'

# Update Snapshot's Defined Tags
- name: Update Snapshot's Defined Tags
  oci_snapshot:
    snapshot_id: 'ocid1.snapshot.oc1..xxxxxEXAMPLExxxxx'
    defined_tags:
        target_users:
            division: 'development'
    state: 'present'

# Delete Snapshot
- name: Delete Snapshot
  oci_snapshot:
    id: 'ocid1.snapshot.oc1..xxxxxEXAMPLExxxxx'
    state: 'absent'
"""

RETURN = """
    snapshot:
        description: Attributes of the created Snapshot. For delete, deleted Snapshot
                     description will be returned.
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

        sample: {
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
                }

"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.file_storage.file_storage_client import FileStorageClient
    from oci.exceptions import ServiceError, ClientError
    from oci.file_storage.models import CreateSnapshotDetails, UpdateSnapshotDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def create_or_update_snapshot(file_storage_client, module):
    result = dict(changed=False, snapshot="")
    snapshot_id = module.params.get("snapshot_id")
    try:
        if snapshot_id:
            result = update_snapshot(file_storage_client, module)
        else:
            result = oci_utils.check_and_create_resource(
                resource_type="snapshot",
                create_fn=create_snapshot,
                kwargs_create={
                    "file_storage_client": file_storage_client,
                    "module": module,
                },
                list_fn=file_storage_client.list_snapshots,
                kwargs_list={"file_system_id": module.params.get("file_system_id")},
                module=module,
                model=CreateSnapshotDetails(),
            )
    except ServiceError as ex:
        get_logger().error("Unable to create/update Snapshot due to: %s", ex.message)
        module.fail_json(msg=ex.message)
    except ClientError as ex:
        get_logger().error("Unable to create/update Snapshot due to: %s", str(ex))
        module.fail_json(msg=str(ex))

    return result


def create_snapshot(file_storage_client, module):
    create_snapshot_details = CreateSnapshotDetails()
    for attribute in create_snapshot_details.attribute_map:
        create_snapshot_details.__setattr__(attribute, module.params.get(attribute))

    result = oci_utils.create_and_wait(
        resource_type="snapshot",
        create_fn=file_storage_client.create_snapshot,
        kwargs_create={"create_snapshot_details": create_snapshot_details},
        client=file_storage_client,
        get_fn=file_storage_client.get_snapshot,
        get_param="snapshot_id",
        module=module,
    )
    return result


def update_snapshot(file_storage_client, module):
    result = oci_utils.check_and_update_resource(
        resource_type="snapshot",
        get_fn=file_storage_client.get_snapshot,
        kwargs_get={"snapshot_id": module.params["snapshot_id"]},
        update_fn=file_storage_client.update_snapshot,
        client=file_storage_client,
        primitive_params_update=["snapshot_id"],
        kwargs_non_primitive_update={UpdateSnapshotDetails: "update_snapshot_details"},
        module=module,
        update_attributes=UpdateSnapshotDetails().attribute_map,
    )
    return result


def delete_snapshot(file_storage_client, module):
    result = oci_utils.delete_and_wait(
        resource_type="snapshot",
        client=file_storage_client,
        get_fn=file_storage_client.get_snapshot,
        kwargs_get={"snapshot_id": module.params["snapshot_id"]},
        delete_fn=file_storage_client.delete_snapshot,
        kwargs_delete={"snapshot_id": module.params["snapshot_id"]},
        module=module,
    )

    return result


def set_logger(input_logger):
    global logger
    logger = input_logger


def get_logger():
    return logger


def main():
    logger = oci_utils.get_logger("oci_snapshot")
    set_logger(logger)

    module_args = oci_utils.get_taggable_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            file_system_id=dict(type="str", required=False),
            name=dict(type="str", required=False),
            snapshot_id=dict(type="str", required=False, aliases=["id"]),
            state=dict(
                type="str",
                required=False,
                default="present",
                choices=["present", "absent"],
            ),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module")

    file_storage_client = oci_utils.create_service_client(module, FileStorageClient)
    state = module.params["state"]

    if state == "present":
        result = create_or_update_snapshot(file_storage_client, module)
    elif state == "absent":
        result = delete_snapshot(file_storage_client, module)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
