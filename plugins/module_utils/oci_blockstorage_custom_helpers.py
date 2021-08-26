# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

logger = oci_common_utils.get_logger("oci_blockstorage_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class BootVolumeBackupActionsHelperCustom:
    def is_action_necessary(self, action, resource, *args, **kwargs):
        if action.upper() == "COPY":
            # boot_volume_backup copied from another backup will have the source backup in source_boot_volume_backup_id
            # parameter. Use it to find if the copy already exists in the destination region.
            if not self.module.params.get("destination_region"):
                self.module.fail_json(
                    msg="destination_required parameter required for copying the backup."
                )
            this_backup = resource
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
            action, resource, *args, **kwargs
        )


class VolumeBackupActionsHelperCustom:
    def is_action_necessary(self, action, resource, *args, **kwargs):
        if action.upper() == "COPY":
            # volume_backup copied from another backup will have the source backup in source_volume_backup_id parameter.
            # Use it to find if the copy already exists in the destination region.
            if not self.module.params.get("destination_region"):
                self.module.fail_json(
                    msg="destination_required parameter required for copying the backup."
                )
            this_backup = resource
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
            action, resource, *args, **kwargs
        )

    # as we are waiting for copy by default.
    # increasing the default wait timeout to 2 hours
    # as this operation can be lengthy depending on the volume size
    def get_wait_timeout(self):
        return 7200


class BootVolumeKmsKeyHelperCustom:
    # When a boot volume is not mapped to a kms key, the get operation returns a 404. The base class update requires
    # the get operation to work. In most of the cases, it is the right assumption to make as we expect the resource
    # to exist when we are trying to update it. This is a special case where it is a mapping (boot volume and kms). This
    # works mostly like create. But to use create logic, we will have to override a bunch of methods used by create and
    # also it might cause unnecessary side effects if there is any change in create logic. So overriding update method
    # to handle the special case.
    def update(self):

        try:
            resource = self.get_resource().data
        except ServiceError as se:
            if se.status != 404:
                self.module.fail_json(
                    msg="Getting resource failed with exception: {error}".format(
                        error=se.message
                    )
                )
        else:
            if resource.kms_key_id == self.module.params.get("kms_key_id"):
                return self.prepare_result(
                    changed=False,
                    resource_type=self.resource_type,
                    resource=to_dict(resource),
                )
        if self.check_mode:
            return self.prepare_result(
                changed=True, resource_type=self.resource_type, resource=dict(),
            )
        self.update_resource()
        # The super update_resource method has a none waiter. But the boot volume does not come to ready state
        # immediately. So wait until the boot volume comes to proper state.
        oci.wait_until(
            self.client,
            self.client.get_boot_volume(
                boot_volume_id=self.module.params.get("boot_volume_id")
            ),
            evaluate_response=lambda r: r.data.lifecycle_state
            in oci_common_utils.DEFAULT_READY_STATES,
            max_wait_seconds=self.get_wait_timeout(),
        )
        return self.prepare_result(
            changed=True,
            resource_type=self.resource_type,
            resource=to_dict(self.get_resource().data),
        )

    def delete(self):
        result = super(BootVolumeKmsKeyHelperCustom, self).delete()
        # The super delete_resource method has a none waiter. But the volume does not come to ready state immediately.
        # So wait until the volume comes to proper state.
        oci.wait_until(
            self.client,
            self.client.get_boot_volume(
                boot_volume_id=self.module.params.get("boot_volume_id")
            ),
            evaluate_response=lambda r: r.data.lifecycle_state
            in oci_common_utils.DEFAULT_READY_STATES,
            max_wait_seconds=self.get_wait_timeout(),
        )
        return result


class VolumeKmsKeyHelperCustom:
    # When a volume is not mapped to a kms key, the get operation returns a 404. The base class update requires
    # the get operation to work. In most of the cases, it is the right assumption to make as we expect the resource
    # to exist when we are trying to update it. This is a special case where it is a mapping (volume and kms). This
    # works mostly like create. But to use create logic, we will have to override a bunch of methods used by create and
    # also it might cause unnecessary side effects if there is any change in create logic. So overriding update method
    # to handle the special case.
    def update(self):

        try:
            resource = self.get_resource().data
        except ServiceError as se:
            if se.status != 404:
                self.module.fail_json(
                    msg="Getting resource failed with exception: {error}".format(
                        error=se.message
                    )
                )
        else:
            if resource.kms_key_id == self.module.params.get("kms_key_id"):
                return self.prepare_result(
                    changed=False,
                    resource_type=self.resource_type,
                    resource=to_dict(resource),
                )
        if self.check_mode:
            return self.prepare_result(
                changed=True, resource_type=self.resource_type, resource=dict(),
            )
        self.update_resource()
        # The super update_resource method has a none waiter. But the volume does not come to ready state immediately.
        # So wait until the volume comes to proper state.
        oci.wait_until(
            self.client,
            self.client.get_volume(volume_id=self.module.params.get("volume_id")),
            evaluate_response=lambda r: r.data.lifecycle_state
            in oci_common_utils.DEFAULT_READY_STATES,
            max_wait_seconds=self.get_wait_timeout(),
        )
        return self.prepare_result(
            changed=True,
            resource_type=self.resource_type,
            resource=to_dict(self.get_resource().data),
        )

    def delete(self):
        result = super(VolumeKmsKeyHelperCustom, self).delete()
        # The super delete_resource method has a none waiter. But the volume does not come to ready state immediately.
        # So wait until the volume comes to proper state.
        oci.wait_until(
            self.client,
            self.client.get_volume(volume_id=self.module.params.get("volume_id")),
            evaluate_response=lambda r: r.data.lifecycle_state
            in oci_common_utils.DEFAULT_READY_STATES,
            max_wait_seconds=self.get_wait_timeout(),
        )
        return result


def get_volume_backup_policy_asset_assignment(client, asset_id):
    try:
        volume_backup_policy_asset_assignment = client.get_volume_backup_policy_asset_assignment(
            asset_id=asset_id
        ).data
    except ServiceError as se:
        if se.status != 404:
            raise
        return None
    else:
        if not volume_backup_policy_asset_assignment:
            return None
        # Currently a volume can only have one backup policy attached to it
        return volume_backup_policy_asset_assignment[0].policy_id


class BootVolumeHelperCustom:
    def get_existing_resource_dict_for_idempotence_check(self, resource):
        resource_dict = super(
            BootVolumeHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(resource)
        if not self.module.params.get("backup_policy_id"):
            return resource_dict
        if self.module.params.get(
            "key_by"
        ) is not None and "backup_policy_id" not in self.module.params.get("key_by"):
            return resource_dict
        # user has provided the backup_policy_id during volume creation. But the get model does not return this
        # value. So we have to make an extra call to get this information.
        resource_dict["backup_policy_id"] = get_volume_backup_policy_asset_assignment(
            self.client, resource.id
        )
        return resource_dict


class VolumeHelperCustom:
    def get_existing_resource_dict_for_idempotence_check(self, resource):
        resource_dict = super(
            VolumeHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(resource)
        if not self.module.params.get("backup_policy_id"):
            return resource_dict
        if self.module.params.get(
            "key_by"
        ) is not None and "backup_policy_id" not in self.module.params.get("key_by"):
            return resource_dict
        # user has provided the backup_policy_id during volume creation. But the get model does not return this
        # value. So we have to make an extra call to get this information.
        resource_dict["backup_policy_id"] = get_volume_backup_policy_asset_assignment(
            self.client, resource.id
        )
        return resource_dict


class VolumeGroupBackupActionsHelperCustom:
    def is_action_necessary(self, action, resource, *args, **kwargs):
        if action.upper() == "COPY":
            # volume_group_backup copied from another backup will have the source backup in source_volume_group_backup_id parameter.
            # Use it to find if the copy already exists in the destination region.
            if not self.module.params.get("destination_region"):
                self.module.fail_json(
                    msg="destination_required parameter required for copying the backup."
                )
            this_backup = resource
            destination_region_client = BlockstorageClient(
                dict(
                    self.client._config, region=self.module.params["destination_region"]
                ),
                **self.client._kwargs
            )
            for destination_region_backup in [
                volume_group_backup
                for volume_group_backup in oci_common_utils.list_all_resources(
                    destination_region_client.list_volume_group_backups,
                    compartment_id=this_backup.compartment_id,
                )
                if self._is_resource_active(volume_group_backup)
            ]:
                if (
                    destination_region_backup.source_volume_group_backup_id
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
        return super(VolumeGroupBackupActionsHelperCustom, self).is_action_necessary(
            action, resource, *args, **kwargs
        )

    def copy(self, *args, **kwargs):
        # The generated copy waits on the source backup lifecycle state. But the source backup remains in AVAILABLE
        # state when the copy is in progress. So override to wait until the copy is done by checking the destination
        # backup lifecycle state instead.
        destination_backup = super(VolumeGroupBackupActionsHelperCustom, self).copy(
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
            destination_region_client.get_volume_group_backup(
                volume_group_backup_id=destination_backup.id
            ),
            evaluate_response=lambda r: r.data.lifecycle_state
            in oci_common_utils.DEFAULT_READY_STATES,
            max_wait_seconds=self.get_wait_timeout(),
        ).data

    # as we are waiting for copy by default.
    # increasing the default wait timeout to 2 hours
    # as this operation can be lengthy depending on the volume group size
    def get_wait_timeout(self):
        return 7200
