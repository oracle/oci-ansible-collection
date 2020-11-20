# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

logger = oci_common_utils.get_logger("oci_compute_instance_agent_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class InstanceAgentCommandHelperCustom:
    # The create operation is not idempotent since it is valid to have multiple commands with the given
    # values and there is no way for us to distinguish if the user wants to create another or not.
    def get_matching_resource(self):
        return None

    # this method is being overwritten as the InstanceAgentCommandSummary model does not reurn back `id` field,
    # it returns back the field `instance_agent_command_id`
    def get_get_model_from_summary_model(self, summary_model):
        return self.get_get_fn()(summary_model.instance_agent_command_id).data


class InstanceAgentCommandFactsHelperCustom:
    # overriding the list_resources method as it is not returning back the `display_name` field in return block.
    # calling the get_resource method to obtain the `display_name` field of the resource
    # TODO - this override will be removed once the service team fixes their bug
    def list_resources(self):
        command_list = super(
            InstanceAgentCommandFactsHelperCustom, self
        ).list_resources()
        # calling get function on the list of commands as the list_resource is not returnig all fields
        for i in range(len(command_list)):
            command = oci_common_utils.call_with_backoff(
                self.client.get_instance_agent_command,
                instance_agent_command_id=command_list[i].instance_agent_command_id,
            ).data
            command_list[i].display_name = command.display_name
        return command_list
