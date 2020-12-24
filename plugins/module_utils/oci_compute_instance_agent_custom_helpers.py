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
