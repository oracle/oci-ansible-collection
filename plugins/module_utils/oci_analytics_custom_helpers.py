# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.analytics.models import ChangeAnalyticsInstanceNetworkEndpointDetails
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = oci_common_utils.get_logger("oci_analytics_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class AnalyticsInstanceHelperCustom:
    # exclude the attributes from the create model which are not present in the get model for idempotency check
    def get_exclude_attributes(self):
        exclude_attributes = super(
            AnalyticsInstanceHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "idcs_access_token",
        ]

    # creation of a analytics_instance is a long running process. So, increasing the timeout
    def get_default_module_wait_timeout(self):
        return 3600


class AnalyticsInstanceActionsHelperCustom:
    ACTION_SCALE_ANALYTICS_INSTANCE = "scale"
    ACTION_CHANGE_ANALYTICS_INSTANCE_NETWORK_ENDPOINT_DETAILS = (
        "change_analytics_instance_network_endpoint"
    )

    def is_action_necessary(self, action, resource=None):

        # Handling idempotency for `scale` operation when both `capacity_type` & `capacity_value` are same as
        # existing capacity metadata.

        if (
            (action.lower() == self.ACTION_SCALE_ANALYTICS_INSTANCE)
            and self.module.params.get("capacity")
            and (
                resource.capacity.capacity_type
                == self.module.params.get("capacity").get("capacity_type")
                and resource.capacity.capacity_value
                == self.module.params.get("capacity").get("capacity_value")
            )
        ):
            return False

        elif (
            action.lower()
            == self.ACTION_CHANGE_ANALYTICS_INSTANCE_NETWORK_ENDPOINT_DETAILS
        ):

            action_details = oci_common_utils.convert_input_data_to_model_class(
                self.module.params, ChangeAnalyticsInstanceNetworkEndpointDetails
            )
            return not oci_common_utils.compare_dicts(
                to_dict(action_details.network_endpoint_details),
                to_dict(resource.network_endpoint_details),
            )

        return super(AnalyticsInstanceActionsHelperCustom, self).is_action_necessary(
            action, resource
        )

    # adding state 'INACTIVE' to the list returned by `get_action_idempotent_states(action)` when performing
    # `stop` operation.
    def get_action_idempotent_states(self, action):
        action_idempotent_states = super(
            AnalyticsInstanceActionsHelperCustom, self
        ).get_action_idempotent_states(action)

        if action.lower() == "stop":
            return action_idempotent_states + [
                "INACTIVE",
            ]
        return action_idempotent_states
