# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    import oci
    from oci.util import to_dict
    from oci.core import BlockstorageClient

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class BootVolumeBackupActionsHelperCustom:
    def is_action_necessary(self, action, *args, **kwargs):
        if action.upper() == "COPY":
            # boot_volume_backup copied from another backup will have the source backup in source_boot_volume_backup_id
            # parameter. Use it to find if the copy already exists in the destination region.
            if not self.module.params.get("destination_region"):
                self.module.fail_json(
                    msg="destination_required parameter required for copying the backup."
                )
            this_backup = self.get_resource().data
            destination_region_client = BlockstorageClient(
                dict(
                    self.client._config, region=self.module.params["destination_region"]
                ),
                **self.client._kwargs
            )
            for destination_region_backup in [
                volume_backup
                for volume_backup in oci_common_utils.list_all_resources(
                    destination_region_client.list_boot_volume_backups,
                    compartment_id=this_backup.compartment_id,
                )
                if self._is_resource_active(volume_backup)
            ]:
                if (
                    destination_region_backup.source_boot_volume_backup_id
                    == this_backup.id
                ):
                    # It might not be a very good idea to exit from this method but currently is_action_necessary
                    # does not provide a way to return a resource.
                    # TODO: Check and modify is_action_necessary to return a resource
                    self.module.exit_json(
                        **self.prepare_result(
                            changed=False,
                            resource_type=self.resource_type,
                            resource=to_dict(destination_region_backup),
                        )
                    )
            return True
        return super(BootVolumeBackupActionsHelperCustom, self).is_action_necessary(
            action, *args, **kwargs
        )

    def copy(self, *args, **kwargs):
        # The generated copy waits on the source backup lifecycle state. But the source backup remains in AVAILABLE
        # state when the copy is in progress. So override to wait until the copy is done by checking the destination
        # backup lifecycle state instead.
        destination_backup = super(BootVolumeBackupActionsHelperCustom, self).copy(
            *args, **kwargs
        )
        destination_region_client = BlockstorageClient(
            dict(
                self.client._config, region=self.module.params.get("destination_region")
            ),
            **self.client._kwargs
        )
        return oci.wait_until(
            destination_region_client,
            destination_region_client.get_boot_volume_backup(
                boot_volume_backup_id=destination_backup.id
            ),
            evaluate_response=lambda r: r.data.lifecycle_state
            in oci_common_utils.DEFAULT_READY_STATES,
            max_wait_seconds=self.module.params.get(
                "wait_timeout", oci_common_utils.MAX_WAIT_TIMEOUT_IN_SECONDS
            ),
        ).data


class VolumeBackupActionsHelperCustom:
    def is_action_necessary(self, action, *args, **kwargs):
        if action.upper() == "COPY":
            # volume_backup copied from another backup will have the source backup in source_volume_backup_id parameter.
            # Use it to find if the copy already exists in the destination region.
            if not self.module.params.get("destination_region"):
                self.module.fail_json(
                    msg="destination_required parameter required for copying the backup."
                )
            this_backup = self.get_resource().data
            destination_region_client = BlockstorageClient(
                dict(
                    self.client._config, region=self.module.params["destination_region"]
                ),
                **self.client._kwargs
            )
            for destination_region_backup in [
                volume_backup
                for volume_backup in oci_common_utils.list_all_resources(
                    destination_region_client.list_volume_backups,
                    compartment_id=this_backup.compartment_id,
                )
                if self._is_resource_active(volume_backup)
            ]:
                if destination_region_backup.source_volume_backup_id == this_backup.id:
                    # It might not be a very good idea to exit from this method but currently is_action_necessary
                    # does not provide a way to return a resource.
                    # TODO: Check and modify is_action_necessary to return a resource
                    self.module.exit_json(
                        **self.prepare_result(
                            changed=False,
                            resource_type=self.resource_type,
                            resource=to_dict(destination_region_backup),
                        )
                    )
            return True
        return super(VolumeBackupActionsHelperCustom, self).is_action_necessary(
            action, *args, **kwargs
        )

    def copy(self, *args, **kwargs):
        # The generated copy waits on the source backup lifecycle state. But the source backup remains in AVAILABLE
        # state when the copy is in progress. So override to wait until the copy is done by checking the destination
        # backup lifecycle state instead.
        destination_backup = super(VolumeBackupActionsHelperCustom, self).copy(
            *args, **kwargs
        )
        destination_region_client = BlockstorageClient(
            dict(
                self.client._config, region=self.module.params.get("destination_region")
            ),
            **self.client._kwargs
        )
        return oci.wait_until(
            destination_region_client,
            destination_region_client.get_volume_backup(
                volume_backup_id=destination_backup.id
            ),
            evaluate_response=lambda r: r.data.lifecycle_state
            in oci_common_utils.DEFAULT_READY_STATES,
            max_wait_seconds=self.module.params.get(
                "wait_timeout", oci_common_utils.MAX_WAIT_TIMEOUT_IN_SECONDS
            ),
        ).data
