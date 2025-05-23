#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_file_storage_snapshot
short_description: Manage a Snapshot resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Snapshot resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new snapshot of the specified file system. You
      can access the snapshot at `.snapshot/<name>`.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    file_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system to take a snapshot of.
            - Required for create using I(state=present).
        type: str
    name:
        description:
            - Name of the snapshot. This value is immutable. It must also be unique with respect
              to all other non-DELETED snapshots on the associated file
              system.
            - Avoid entering confidential information.
            - "Example: `Sunday`"
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    freeform_tags:
        description:
            - "Free-form tags for this resource. Each tag is a simple key-value pair
               with no predefined name, type, or namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    expiration_time:
        description:
            - The time when this snapshot will be deleted.
            - This parameter is updatable.
        type: str
    snapshot_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the snapshot.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Snapshot.
            - Use I(state=present) to create or update a Snapshot.
            - Use I(state=absent) to delete a Snapshot.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create snapshot
  oci_file_storage_snapshot:
    # required
    file_system_id: "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    expiration_time: expiration_time_example

- name: Update snapshot
  oci_file_storage_snapshot:
    # required
    snapshot_id: "ocid1.snapshot.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    expiration_time: expiration_time_example

- name: Update snapshot using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_snapshot:
    # required
    name: name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    expiration_time: expiration_time_example

- name: Delete snapshot
  oci_file_storage_snapshot:
    # required
    snapshot_id: "ocid1.snapshot.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete snapshot using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_snapshot:
    # required
    name: name_example
    state: absent

"""

RETURN = """
snapshot:
    description:
        - Details of the Snapshot resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        file_system_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system from which the snapshot
                  was created.
            returned: on success
            type: str
            sample: "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the snapshot.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the snapshot.
            returned: on success
            type: str
            sample: CREATING
        name:
            description:
                - Name of the snapshot. This value is immutable.
                - Avoid entering confidential information.
                - "Example: `Sunday`"
            returned: on success
            type: str
            sample: name_example
        time_created:
            description:
                - The date and time the snapshot was created, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        snapshot_type:
            description:
                - Specifies generation type of the snapshot.
            returned: on success
            type: str
            sample: USER
        snapshot_time:
            description:
                - "The date and time the snapshot was taken, expressed
                  in L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                  This value might be the same or different from `timeCreated` depending
                  on the following factors:
                  - If the snapshot is created in the original file system directory.
                  - If the snapshot is cloned from a file system.
                  - If the snapshot is replicated from a file system."
                - "Example: `2020-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        provenance_id:
            description:
                - An L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) identifying the parent from which this snapshot was cloned.
                  If this snapshot was not cloned, then the `provenanceId` is the same as the snapshot `id` value.
                  If this snapshot was cloned, then the `provenanceId` value is the parent's `provenanceId`.
                  See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
            returned: on success
            type: str
            sample: "ocid1.provenance.oc1..xxxxxxEXAMPLExxxxxx"
        is_clone_source:
            description:
                - Specifies whether the snapshot has been cloned.
                  See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
            returned: on success
            type: bool
            sample: true
        lifecycle_details:
            description:
                - Additional information about the current `lifecycleState`.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair
                   with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        expiration_time:
            description:
                - The time when this snapshot will be deleted.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        filesystem_snapshot_policy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system snapshot policy that created this
                  snapshot.
            returned: on success
            type: str
            sample: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "file_system_id": "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "name": "name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "snapshot_type": "USER",
        "snapshot_time": "2013-10-20T19:20:30+01:00",
        "provenance_id": "ocid1.provenance.oc1..xxxxxxEXAMPLExxxxxx",
        "is_clone_source": true,
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "expiration_time": "2013-10-20T19:20:30+01:00",
        "filesystem_snapshot_policy_id": "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import CreateSnapshotDetails
    from oci.file_storage.models import UpdateSnapshotDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SnapshotHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(SnapshotHelperGen, self).get_possible_entity_types() + [
            "snapshot",
            "snapshots",
            "fileStoragesnapshot",
            "fileStoragesnapshots",
            "snapshotresource",
            "snapshotsresource",
            "filestorage",
        ]

    def get_module_resource_id_param(self):
        return "snapshot_id"

    def get_module_resource_id(self):
        return self.module.params.get("snapshot_id")

    def get_get_fn(self):
        return self.client.get_snapshot

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_snapshot, snapshot_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_snapshot, snapshot_id=self.module.params.get("snapshot_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["file_system_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_snapshots, **kwargs)

    def get_create_model_class(self):
        return CreateSnapshotDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_snapshot,
            call_fn_args=(),
            call_fn_kwargs=dict(create_snapshot_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateSnapshotDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_snapshot,
            call_fn_args=(),
            call_fn_kwargs=dict(
                snapshot_id=self.module.params.get("snapshot_id"),
                update_snapshot_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_snapshot,
            call_fn_args=(),
            call_fn_kwargs=dict(snapshot_id=self.module.params.get("snapshot_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


SnapshotHelperCustom = get_custom_class("SnapshotHelperCustom")


class ResourceHelper(SnapshotHelperCustom, SnapshotHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            file_system_id=dict(type="str"),
            name=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            expiration_time=dict(type="str"),
            snapshot_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="snapshot",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
