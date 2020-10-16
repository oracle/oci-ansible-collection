# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class ManagementAgentInstallKeyHelperCustom:
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    # is_key_active does not exist in the resource model and updating it alters the lifecycle_state of the resource. So
    # we need to check the existing lifecycle_state of the resource to determine whether we need the update operation.
    def is_update_necessary(self, existing_resource_dict):
        if self.module.params.get("is_key_active") is not None:
            is_key_active = False
            if (
                existing_resource_dict.get("lifecycle_state")
                == self.LIFECYCLE_STATE_ACTIVE
            ):
                is_key_active = True
            existing_resource_dict["is_key_active"] = is_key_active
        return super(ManagementAgentInstallKeyHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )

    # The default behaviour of the update operation is to wait until the resource is in active states. But updating
    # `is_key_active` to False makes the resource to go into inactive state. So override the wait for states accordingly
    def get_wait_for_states_for_operation(self, operation):
        wait_for_states = super(
            ManagementAgentInstallKeyHelperCustom, self
        ).get_wait_for_states_for_operation(operation)
        if (
            operation == oci_common_utils.UPDATE_OPERATION_KEY
            and self.module.params.get("is_key_active") is not None
        ):
            return [
                self.LIFECYCLE_STATE_ACTIVE
                if self.module.params.get("is_key_active")
                else self.LIFECYCLE_STATE_INACTIVE
            ]
        return wait_for_states


class ManagementAgentActionsHelperCustom:
    # The action module works with a collection of agent_ids instead of a single resource. So get_resource is not
    # applicable here. This is a dummy implementation so that other methods work.
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)

    def is_action_necessary(self, action, resource=None):
        if action == "deploy_plugins":
            agent_ids = self.module.params.get("agent_ids")
            if agent_ids is None:
                self.module.fail_json("agent_ids required for deploy_plugins action")
            plugin_ids = self.module.params.get("plugin_ids")
            if plugin_ids is None:
                self.module.fail_json("plugin_ids required for deploy_plugins action")
            if not plugin_ids or not agent_ids:
                return False
            agents = [
                oci_common_utils.call_with_backoff(
                    self.client.get_management_agent, management_agent_id=agent_id
                ).data
                for agent_id in agent_ids
            ]
            for agent in agents:
                if not agent.plugin_list:
                    return True
                existing_plugin_ids = [plugin.plugin_id for plugin in agent.plugin_list]
                if not all(
                    [plugin_id in existing_plugin_ids for plugin_id in plugin_ids]
                ):
                    return True
            return False
        return super(ManagementAgentActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
