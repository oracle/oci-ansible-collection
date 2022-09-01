# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class DatabaseRegistrationHelperCustom:
    def is_update_necessary(self, existing_resource_dict):

        # password and wallet are not available in the resource. So if the user is trying to update them, there
        # is no way for us to check. So skip idempotence in cases where user has provided these attributes.
        if self.module.params.get("password") or self.module.params.get("wallet"):
            return True

        return super(DatabaseRegistrationHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )


class DeploymentBackupActionsHelperCustom:

    CANCEL_ACTION_KEY = "cancel"
    BACKUP_CANCELLED_STATUS = ["CANCELED", "CANCELING"]

    def is_cancel_necessary(self, resource):
        if getattr(resource, "lifecycle_state", None) in self.BACKUP_CANCELLED_STATUS:
            return False
        return True

    def is_action_necessary(self, action, resource=None):
        if action.lower() == self.CANCEL_ACTION_KEY:
            return self.is_cancel_necessary(resource)
        return super(DeploymentBackupActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
