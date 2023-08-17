# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MountTargetFactsHelperCustom:
    def list_resources(self):
        existing_mount_targets_summary = to_dict(
            super(MountTargetFactsHelperCustom, self).list_resources()
        )
        result = [
            oci_common_utils.call_with_backoff(
                self.client.get_mount_target, mount_target_id=mount_target["id"],
            ).data
            for mount_target in existing_mount_targets_summary
        ]
        return result


class FileSystemHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            FileSystemHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # source_snapshot_id is a top level param on CreateFileSystem but it gets returned
        # inside file_system.source_details so we need to propagate the value so that the existing resource matching
        # logic works properly
        if create_model_dict.get("source_snapshot_id") is not None:
            create_model_dict["source_details"] = dict(
                source_snapshot_id=create_model_dict.pop("source_snapshot_id", None)
            )
        return create_model_dict


class FilesystemSnapshotPolicyActionsHelperCustom:
    # Pause action operation updates the lifecycle state of the file system snapshot policy
    # from ACTIVE to INACTIVE.
    def get_action_desired_states(self, action):
        action_desired_states = super(
            FilesystemSnapshotPolicyActionsHelperCustom, self
        ).get_action_desired_states(action)

        if action.lower() == "pause":
            return action_desired_states + [
                "INACTIVE",
            ]
        return action_desired_states
