#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_file_storage_file_system
short_description: Manage a FileSystem resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a FileSystem resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new file system in the specified compartment and
      availability domain. Instances can mount file systems in
      another availability domain, but doing so might increase
      latency when compared to mounting instances in the same
      availability domain.
    - After you create a file system, you can associate it with a mount
      target. Instances can then mount the file system by connecting to the
      mount target's IP address. You can associate a file system with
      more than one mount target at a time.
    - For information about access control and compartments, see
      L(Overview of the IAM Service,https://docs.cloud.oracle.com/Content/Identity/Concepts/overview.htm).
    - For information about Network Security Groups access control, see
      L(Network Security Groups,https://docs.cloud.oracle.com/Content/Network/Concepts/networksecuritygroups.htm).
    - For information about availability domains, see L(Regions and
      Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm).
      To get a list of availability domains, use the
      `ListAvailabilityDomains` operation in the Identity and Access
      Management Service API.
    - All Oracle Cloud Infrastructure resources, including
      file systems, get an Oracle-assigned, unique ID called an Oracle
      Cloud Identifier (L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm)).
      When you create a resource, you can find its OCID in the response.
      You can also retrieve a resource's OCID by using a List API operation on that resource
      type or by viewing the resource in the Console.
    - "This resource has the following action operations in the M(oracle.oci.oci_file_storage_file_system_actions) module: change_compartment,
      estimate_replication."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    availability_domain:
        description:
            - The availability domain to create the file system in.
            - "Example: `Uocm:PHX-AD-1`"
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to create the file system in.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    source_snapshot_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the snapshot used to create a cloned file system.
              See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
              Avoid entering confidential information.
            - "Example: `My file system`"
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
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
    kms_key_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the KMS key used to encrypt the encryption keys associated
              with this file system.
            - This parameter is updatable.
        type: str
    filesystem_snapshot_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated file system snapshot policy, which
              controls the frequency of snapshot creation and retention period of the taken snapshots.
            - May be unset as a blank value.
            - This parameter is updatable.
        type: str
    file_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the FileSystem.
            - Use I(state=present) to create or update a FileSystem.
            - Use I(state=absent) to delete a FileSystem.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create file_system
  oci_file_storage_file_system:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    source_snapshot_id: "ocid1.sourcesnapshot.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update file_system
  oci_file_storage_file_system:
    # required
    file_system_id: "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update file_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_file_system:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    kms_key_id: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete file_system
  oci_file_storage_file_system:
    # required
    file_system_id: "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete file_system using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_file_storage_file_system:
    # required
    availability_domain: Uocm:PHX-AD-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
file_system:
    description:
        - Details of the FileSystem resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        availability_domain:
            description:
                - The availability domain the file system is in. May be unset
                  as a blank or NULL value.
                - "Example: `Uocm:PHX-AD-1`"
            returned: on success
            type: str
            sample: Uocm:PHX-AD-1
        metered_bytes:
            description:
                - The number of bytes consumed by the file system, including
                  any snapshots. This number reflects the metered size of the file
                  system and is updated asynchronously with respect to
                  updates to the file system.
                  For more information, see L(File System Usage and Metering,https://docs.cloud.oracle.com/Content/File/Concepts/FSutilization.htm).
            returned: on success
            type: int
            sample: 56
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment that contains the file system.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My file system`"
            returned: on success
            type: str
            sample: display_name_example
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the file system.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - The date and time the file system was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        kms_key_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the KMS key which is the master encryption key for the
                  file system.
            returned: on success
            type: str
            sample: "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx"
        source_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                parent_file_system_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system that contains the source
                          snapshot of a cloned file system.
                          See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
                    returned: on success
                    type: str
                    sample: "ocid1.parentfilesystem.oc1..xxxxxxEXAMPLExxxxxx"
                source_snapshot_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source snapshot used to create a cloned file
                          system.
                          See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
                    returned: on success
                    type: str
                    sample: "ocid1.sourcesnapshot.oc1..xxxxxxEXAMPLExxxxxx"
        is_clone_parent:
            description:
                - Specifies whether the file system has been cloned.
                  See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
            returned: on success
            type: bool
            sample: true
        is_hydrated:
            description:
                - Specifies whether the data has finished copying from the source to the clone.
                  Hydration can take up to several hours to complete depending on the size of the source.
                  The source and clone remain available during hydration, but there may be some performance impact.
                  See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm#hydration).
            returned: on success
            type: bool
            sample: true
        lifecycle_details:
            description:
                - Additional information about the current 'lifecycleState'.
            returned: on success
            type: str
            sample: lifecycle_details_example
        is_targetable:
            description:
                - Specifies whether the file system can be used as a target file system for replication. The system sets this value to `true` if the file system
                  is unexported, hasn't yet been specified as a target file system in any replication resource, and has no user snapshots. After the file system
                  has been specified as a target in a replication, or if the file system contains user snapshots, the system sets this value to `false`.
                  For more information, see L(Using Replication,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/using-replication.htm).
            returned: on success
            type: bool
            sample: true
        replication_target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication target associated with the file system.
                  Empty if the file system is not being used as target in a replication.
            returned: on success
            type: str
            sample: "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx"
        filesystem_snapshot_policy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated file system snapshot policy, which
                  controls the frequency of snapshot creation and retention period of the taken snapshots.
            returned: on success
            type: str
            sample: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "metered_bytes": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "source_details": {
            "parent_file_system_id": "ocid1.parentfilesystem.oc1..xxxxxxEXAMPLExxxxxx",
            "source_snapshot_id": "ocid1.sourcesnapshot.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_clone_parent": true,
        "is_hydrated": true,
        "lifecycle_details": "lifecycle_details_example",
        "is_targetable": true,
        "replication_target_id": "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx",
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
    from oci.file_storage.models import CreateFileSystemDetails
    from oci.file_storage.models import UpdateFileSystemDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FileSystemHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(FileSystemHelperGen, self).get_possible_entity_types() + [
            "filesystem",
            "filesystems",
            "fileStoragefilesystem",
            "fileStoragefilesystems",
            "filesystemresource",
            "filesystemsresource",
            "filestorage",
        ]

    def get_module_resource_id_param(self):
        return "file_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("file_system_id")

    def get_get_fn(self):
        return self.client.get_file_system

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_file_system, file_system_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_file_system,
            file_system_id=self.module.params.get("file_system_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
            "availability_domain",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = (
            ["display_name", "source_snapshot_id"]
            if self._use_name_as_identifier()
            else ["display_name", "source_snapshot_id", "filesystem_snapshot_policy_id"]
        )

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
        return oci_common_utils.list_all_resources(
            self.client.list_file_systems, **kwargs
        )

    def get_create_model_class(self):
        return CreateFileSystemDetails

    def get_exclude_attributes(self):
        return ["source_snapshot_id"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_file_system,
            call_fn_args=(),
            call_fn_kwargs=dict(create_file_system_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateFileSystemDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_file_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                file_system_id=self.module.params.get("file_system_id"),
                update_file_system_details=update_details,
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
            call_fn=self.client.delete_file_system,
            call_fn_args=(),
            call_fn_kwargs=dict(
                file_system_id=self.module.params.get("file_system_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


FileSystemHelperCustom = get_custom_class("FileSystemHelperCustom")


class ResourceHelper(FileSystemHelperCustom, FileSystemHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            availability_domain=dict(type="str"),
            compartment_id=dict(type="str"),
            source_snapshot_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            kms_key_id=dict(type="str"),
            filesystem_snapshot_policy_id=dict(type="str"),
            file_system_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="file_system",
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
