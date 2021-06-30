#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_file_storage_file_system_actions
short_description: Perform actions on a FileSystem resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a FileSystem resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a file system and its associated snapshots into a different compartment within the same tenancy. For information
      about moving resources between compartments, see L(Moving Resources to a Different
      Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes)
version_added: "2.9"
author: Oracle (@oracle)
options:
    file_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to move the file system to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the FileSystem.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on file_system
  oci_file_storage_file_system_actions:
    compartment_id: "ocid1.compartment.oc1..unique_ID"
    file_system_id: "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx"
    action: "change_compartment"

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
            type: string
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
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. It does not have to be unique, and it is changeable.
                  Avoid entering confidential information.
                - "Example: `My file system`"
            returned: on success
            type: string
            sample: My file system
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the file system.
            returned: on success
            type: string
            sample: CREATING
        time_created:
            description:
                - The date and time the file system was created, expressed in
                  L(RFC 3339,https://tools.ietf.org/rfc/rfc3339) timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2016-08-25T21:10:29.600Z
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
            type: string
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
                          See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningafilesystem.htm).
                    returned: on success
                    type: string
                    sample: "ocid1.parentfilesystem.oc1..xxxxxxEXAMPLExxxxxx"
                source_snapshot_id:
                    description:
                        - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the source snapshot used to create a cloned file
                          system.
                          See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningafilesystem.htm).
                    returned: on success
                    type: string
                    sample: "ocid1.sourcesnapshot.oc1..xxxxxxEXAMPLExxxxxx"
        is_clone_parent:
            description:
                - Specifies whether the file system has been cloned.
                  See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningafilesystem.htm).
            returned: on success
            type: bool
            sample: true
        is_hydrated:
            description:
                - Specifies whether the data has finished copying from the source to the clone.
                  Hydration can take up to several hours to complete depending on the size of the source.
                  The source and clone remain available during hydration, but there may be some performance impact.
                  See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningafilesystem.htm#hydration).
            returned: on success
            type: bool
            sample: true
        lifecycle_details:
            description:
                - Additional information about the current 'lifecycleState'.
            returned: on success
            type: string
            sample: lifecycle_details_example
    sample: {
        "availability_domain": "Uocm:PHX-AD-1",
        "metered_bytes": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "My file system",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "time_created": "2016-08-25T21:10:29.600Z",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "kms_key_id": "ocid1.kmskey.oc1..xxxxxxEXAMPLExxxxxx",
        "source_details": {
            "parent_file_system_id": "ocid1.parentfilesystem.oc1..xxxxxxEXAMPLExxxxxx",
            "source_snapshot_id": "ocid1.sourcesnapshot.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "is_clone_parent": true,
        "is_hydrated": true,
        "lifecycle_details": "lifecycle_details_example"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.file_storage import FileStorageClient
    from oci.file_storage.models import ChangeFileSystemCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FileSystemActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "file_system_id"

    def get_module_resource_id(self):
        return self.module.params.get("file_system_id")

    def get_get_fn(self):
        return self.client.get_file_system

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_file_system,
            file_system_id=self.module.params.get("file_system_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeFileSystemCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_file_system_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                file_system_id=self.module.params.get("file_system_id"),
                change_file_system_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


FileSystemActionsHelperCustom = get_custom_class("FileSystemActionsHelperCustom")


class ResourceHelper(FileSystemActionsHelperCustom, FileSystemActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            file_system_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="file_system",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
