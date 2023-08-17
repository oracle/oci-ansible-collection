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
module: oci_file_storage_file_system_facts
short_description: Fetches details about one or multiple FileSystem resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple FileSystem resources in Oracle Cloud Infrastructure
    - Lists the file system resources in the specified compartment, or by the specified compartment and
      file system snapshot policy.
    - If I(file_system_id) is specified, the details of a single FileSystem will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    file_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system.
            - Required to get a specific file_system.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple file_systems.
        type: str
    availability_domain:
        description:
            - The name of the availability domain.
            - "Example: `Uocm:PHX-AD-1`"
            - Required to list multiple file_systems.
        type: str
    display_name:
        description:
            - A user-friendly name. It does not have to be unique, and it is changeable.
            - "Example: `My resource`"
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Filter results by the specified lifecycle state. Must be a valid
              state for the resource type.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    source_snapshot_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the snapshot used to create a cloned file system. See
              L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        type: str
    parent_file_system_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system that contains the source snapshot of a
              cloned file system. See L(Cloning a File System,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/cloningFS.htm).
        type: str
    filesystem_snapshot_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the file system snapshot policy
              that is associated with the file systems.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide either value, but not both.
              By default, when you sort by time created, results are shown
              in descending order. When you sort by display name, results are
              shown in ascending order.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc', where 'asc' is
              ascending and 'desc' is descending. The default order is 'desc'
              except for numeric values.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific file_system
  oci_file_storage_file_system_facts:
    # required
    file_system_id: "ocid1.filesystem.oc1..xxxxxxEXAMPLExxxxxx"

- name: List file_systems
  oci_file_storage_file_system_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    availability_domain: Uocm:PHX-AD-1

    # optional
    display_name: display_name_example
    lifecycle_state: CREATING
    source_snapshot_id: "ocid1.sourcesnapshot.oc1..xxxxxxEXAMPLExxxxxx"
    parent_file_system_id: "ocid1.parentfilesystem.oc1..xxxxxxEXAMPLExxxxxx"
    filesystem_snapshot_policy_id: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
file_systems:
    description:
        - List of FileSystem resources
    returned: on success
    type: complex
    contains:
        is_targetable:
            description:
                - Specifies whether the file system can be used as a target file system for replication.
                  For more information, see L(Using Replication,https://docs.cloud.oracle.com/iaas/Content/File/Tasks/using-replication.htm).
                - Returned for get operation
            returned: on success
            type: bool
            sample: true
        replication_target_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the replication target associated with the file system.
                  Empty if the file system is not being used as target in a replication.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx"
        filesystem_snapshot_policy_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the associated file system snapshot policy, which
                  controls the frequency of snapshot creation and retention period of the taken snapshots.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx"
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
    sample: [{
        "is_targetable": true,
        "replication_target_id": "ocid1.replicationtarget.oc1..xxxxxxEXAMPLExxxxxx",
        "filesystem_snapshot_policy_id": "ocid1.filesystemsnapshotpolicy.oc1..xxxxxxEXAMPLExxxxxx",
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
        "lifecycle_details": "lifecycle_details_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.file_storage import FileStorageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class FileSystemFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "file_system_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "availability_domain",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_file_system,
            file_system_id=self.module.params.get("file_system_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "lifecycle_state",
            "source_snapshot_id",
            "parent_file_system_id",
            "filesystem_snapshot_policy_id",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_file_systems,
            compartment_id=self.module.params.get("compartment_id"),
            availability_domain=self.module.params.get("availability_domain"),
            **optional_kwargs
        )


FileSystemFactsHelperCustom = get_custom_class("FileSystemFactsHelperCustom")


class ResourceFactsHelper(FileSystemFactsHelperCustom, FileSystemFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            file_system_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            availability_domain=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=["CREATING", "ACTIVE", "DELETING", "DELETED", "FAILED"],
            ),
            source_snapshot_id=dict(type="str"),
            parent_file_system_id=dict(type="str"),
            filesystem_snapshot_policy_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="file_system",
        service_client_class=FileStorageClient,
        namespace="file_storage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(file_systems=result)


if __name__ == "__main__":
    main()
