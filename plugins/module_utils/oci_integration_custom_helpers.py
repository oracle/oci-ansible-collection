# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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


class IntegrationInstanceHelperCustom:
    def get_exclude_attributes(self):
        exclude_attributes = super(
            IntegrationInstanceHelperCustom, self
        ).get_exclude_attributes()
        # exclude the attributes from the create model which are not present in the get model for idempotency check
        return exclude_attributes + [
            "idcs_at",
        ]

    def get_default_module_wait_timeout(self):
        return 3600


class IntegrationInstanceActionsHelperCustom:
    STOP_ACTION_KEY = "STOP"
    CHANGE_INTEGRATION_INSTANCE_NETWORK_ENDPOINT_ACTION_KEY = (
        "CHANGE_INTEGRATION_INSTANCE_NETWORK_ENDPOINT"
    )
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    def get_action_idempotent_states(self, action):
        action_idempotent_states = super(
            IntegrationInstanceActionsHelperCustom, self
        ).get_action_idempotent_states(action)
        if action.upper() == self.STOP_ACTION_KEY:
            return action_idempotent_states + [self.LIFECYCLE_STATE_INACTIVE]
        return action_idempotent_states

    def get_action_desired_states(self, action):
        action_desired_states = super(
            IntegrationInstanceActionsHelperCustom, self
        ).get_action_desired_states(action)
        if action.upper() == self.STOP_ACTION_KEY:
            return action_desired_states + [self.LIFECYCLE_STATE_INACTIVE]
        return action_desired_states

    def is_action_necessary(self, action, resource=None):
        if (
            action.upper()
            == self.CHANGE_INTEGRATION_INSTANCE_NETWORK_ENDPOINT_ACTION_KEY
        ):
            # Let the API throw the validation error
            if not self.module.params.get("network_endpoint_details"):
                return True
            resource = resource or self.get_resource()
            return not oci_common_utils.compare_dicts(
                self.module.params.get("network_endpoint_details"),
                to_dict(getattr(resource, "network_endpoint_details", None)),
            )
        return super(IntegrationInstanceActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
