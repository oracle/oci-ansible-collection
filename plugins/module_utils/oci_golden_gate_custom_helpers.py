# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class DeploymentHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            DeploymentHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        if create_model_dict.get("ogg_data"):
            create_model_dict.get("ogg_data").pop("admin_password", None)
            create_model_dict.get("ogg_data").pop("key", None)
        return create_model_dict

    # I have seen the operations getting timedout sometimes. So increasing the timeout to avoid timeout failures.
    def get_default_module_wait_timeout(self):
        return 3600


class DeploymentActionsHelperCustom:
    def get_action_idempotent_states(self, action):
        if action.upper() == "START":
            return ["ACTIVE"]
        if action.upper() == "STOP":
            return ["INACTIVE"]
        return super(DeploymentActionsHelperCustom, self).get_action_idempotent_states(
            action
        )

    def get_action_desired_states(self, action):
        if action.upper() == "START":
            return ["ACTIVE"]
        if action.upper() == "STOP":
            return ["INACTIVE"]
        return super(DeploymentActionsHelperCustom, self).get_action_desired_states(
            action
        )


class DatabaseRegistrationHelperCustom:
    # password and wallet are not available in the get model. So cannot compare them for idempotence.
    def get_exclude_attributes(self):
        exclude_attributes = super(
            DatabaseRegistrationHelperCustom, self
        ).get_exclude_attributes()
        exclude_attributes += ["password", "wallet"]
        return exclude_attributes

    def is_update_necessary(self, existing_resource_dict):

        # password and wallet are not available in the resource. So if the user is trying to update them, there
        # is no way for us to check. So skip idempotence in cases where user has provided these attributes.
        if self.module.params.get("password") or self.module.params.get("wallet"):
            return True

        return super(DatabaseRegistrationHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )
