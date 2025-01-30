# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class KeyVersionHelperCustom:
    def get_module_resource_id_param(self):
        return "id"

    def get_module_resource_id(self):
        return self.module.params.get("id")

    # Currently the module doesn't have the keyVersionId param
    # The ID is returned after create in CreateOperationLifecycleStateWaiter
    # This customization can be replaced with a new waiter logic in the future
    def get_resource(self):
        if self.module.params.get("id") is None:
            return None
        else:
            return oci_common_utils.call_with_backoff(
                self.client.get_key_version,
                key_id=self.module.params.get("key_id"),
                key_version_id=self.module.params.get("id"),
            )

    # there is no concept of idempotency for this module
    # it re-executes create new version every time module is invoked
    def get_matching_resource(self):
        return None

    def is_create(self):
        return True


class VaultActionsHelperCustom:
    REPLICA_CREATION_SUMMARY_STATUS = ["CREATED", "CREATING"]
    REPLICA_DELETION_SUMMARY_STATUS = ["DELETED", "DELETING"]

    def is_action_necessary(self, action, resource=None):
        # For replica actions: create/delete we check if the replica exists by checking if there are any replication details
        # and if for the given region whether the status is same as what we are expecting to change it to.
        if action == "create_vault_replica":
            replication_details = getattr(resource, "replica_details", None)
            if replication_details is None:
                return True

            region_param = self.module.params.get("replica_region")
            existing_replicas = self.client.list_vault_replicas(
                self.module.params.get("vault_id")
            )
            for replica in existing_replicas:
                existing_region = getattr(replica, "region", None)
                existing_status = getattr(replica, "status", None)
                if (
                    existing_region == region_param
                    and existing_status in self.REPLICA_CREATION_SUMMARY_STATUS
                ):
                    return False
            return True
        elif action == "delete_vault_replica":
            replication_details = getattr(resource, "replica_details", None)
            if replication_details is None:
                return False

            region_param = self.module.params.get("replica_region")
            existing_replicas = self.client.list_vault_replicas(
                self.module.params.get("vault_id")
            )
            for replica in existing_replicas:
                existing_region = getattr(replica, "region", None)
                existing_status = getattr(replica, "status", None)
                if (
                    getattr(replica, "region", None) == region_param
                    and existing_status in self.REPLICA_CREATION_SUMMARY_STATUS
                ):
                    return True
            return False
        elif kms_is_action_necessary(self, action, resource) is False:
            return False
        return super(VaultActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class KeyActionsHelperCustom:
    def is_action_necessary(self, action, resource):
        if kms_is_action_necessary(self, action, resource) is False:
            return False
        return super(KeyActionsHelperCustom, self).is_action_necessary(action, resource)


class KeyVersionActionsHelperCustom:
    def is_action_necessary(self, action, resource):
        if kms_is_action_necessary(self, action, resource) is False:
            return False
        return super(KeyVersionActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


def kms_is_action_necessary(resource_helper, action, resource):
    # For schedule_key_deletion key (idempotence), we see that the updated key does not have time_of_deletion set, as the key is in PENDING_DELETION state.
    if (
        hasattr(resource, "lifecycle_state")
        and (
            resource.lifecycle_state == "PENDING_DELETION"
            or resource.lifecycle_state == "DELETED"
        )
        and hasattr(resource, "time_of_deletion")
        and resource.time_of_deletion is not None
        and action == "schedule_key_deletion"
        and resource_helper.module.params.get("time_of_deletion") is None
    ):
        return False
    else:
        # Idempotency for modules with delete date like KMS (consider only in deleted lifecycle_state)
        # If the deleted date is equal to the request delete date, we should not execute the action (changed=false)
        # If the deleted date is different, we will execute the action and return server errors
        if (
            hasattr(resource, "lifecycle_state")
            and (
                resource.lifecycle_state == "PENDING_DELETION"
                or resource.lifecycle_state == "DELETED"
            )
            and hasattr(resource, "time_of_deletion")
            and resource.time_of_deletion is not None
            and resource_helper.module.params.get("time_of_deletion") is not None
        ):
            if resource.time_of_deletion == oci_common_utils.deserialize_datetime(
                resource_helper.module.params["time_of_deletion"]
            ):
                return False
            else:
                resource_helper.module.warn(
                    "This resource was deleted on: {0}. To change the deletion date, "
                    "cancel the current deletion and delete this resource again using the new requested date {1}".format(
                        resource.time_of_deletion.isoformat(sep="T"),
                        resource_helper.module.params["time_of_deletion"],
                    )
                )
    return True


class SecretActionsHelperCustom:
    def is_action_necessary(self, action, resource):
        if kms_is_action_necessary(self, action, resource) is False:
            return False
        return super(SecretActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
