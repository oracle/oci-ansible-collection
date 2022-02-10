# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
    # creation of a analytics_instance is a long running process. So, increasing the timeout
    def get_default_module_wait_timeout(self):
        return 3600


class VanityUrlHelperCustom:

    # vanity_url doesn't have a list API. getting the list of vanity_url's of the analytics_instance using GET analytics_instance API
    def list_resources(self):
        analytics_instance_id = self.module.params.get("analytics_instance_id")
        anlaytics_instance_details = oci_common_utils.call_with_backoff(
            self.client.get_analytics_instance,
            analytics_instance_id=analytics_instance_id,
        ).data
        vanityurl_details = []
        if (
            anlaytics_instance_details
            and anlaytics_instance_details.lifecycle_state == "ACTIVE"
            and getattr(anlaytics_instance_details, "vanity_url_details", None)
        ):
            vanityurl_details = list(
                anlaytics_instance_details.vanity_url_details.values()
            )
        return vanityurl_details

    # vanity_url doesnt have a get api. we are getting analytics instance and getting vanity_url from it.
    def get_resource(self):
        vanity_url_list = self.list_resources()
        for resource in vanity_url_list:
            resource_dict = to_dict(resource)
            vanity_url_key = self.module.params.get("vanity_url_key")
            if vanity_url_key and vanity_url_key == resource_dict.get("key"):
                return oci_common_utils.get_default_response_from_resource(resource)
            elif oci_common_utils.compare_dicts(
                source_dict=self.module.params,
                target_dict=resource_dict,
                ignore_attr_if_not_in_target=True,
            ):
                return oci_common_utils.get_default_response_from_resource(resource)
        return oci_common_utils.raise_does_not_exist_service_error()

    # vanity_url does not exist in the respective analytics_instance when the vanity_url is dead. So we just check of vanity_url is None
    def is_resource_dead(self, resource):
        return getattr(resource, "key", None) != self.module.params.get(
            "vanity_url_key"
        )

    # get_exlude_attributes not generated as vanity_url doesn't have a get/list operation
    def get_exclude_attributes(self):
        exclude_attributes = super(VanityUrlHelperCustom, self).get_exclude_attributes()
        return exclude_attributes + [
            "passphrase",
            "private_key",
            "ca_certificate",
        ]


class PrivateAccessChannelHelperCustom:

    # The resource_id of private_access_channel is private_access_channel_key
    def get_module_resource_id_param(self):
        return "private_access_channel_key"

    # The resource_id of private_access_channel is private_access_channel_key
    def get_module_resource_id(self):
        return self.module.params.get("private_access_channel_key")

    # There is no LIST API for private_access_channel. So, using the analytics_instance to get the list of private_access_channel
    def list_resources(self):
        analytics_instance_id = self.module.params.get("analytics_instance_id")
        anlaytics_instance_details = oci_common_utils.call_with_backoff(
            self.client.get_analytics_instance,
            analytics_instance_id=analytics_instance_id,
        ).data
        private_access_channels = []
        if (
            anlaytics_instance_details
            and anlaytics_instance_details.lifecycle_state == "ACTIVE"
            and getattr(anlaytics_instance_details, "private_access_channels", None)
        ):
            private_access_channel_dict = (
                anlaytics_instance_details.private_access_channels
            )
            private_access_channels = list(private_access_channel_dict.values())

        return private_access_channels

    # creation of a private_access_channel is a long running process. So, increasing the timeout
    def get_default_module_wait_timeout(self):
        return 7200

    # private_access_channel does not exist in the respective analytics_instance when the private_access_channel is dead.
    # So we just check of private_access_channel is None
    def is_resource_dead(self, resource):
        return getattr(resource, "key", None) != self.module.params.get(
            "private_access_channel_key"
        )

    # the GET api of private_access_channel takes private_access_channel_key which is auto generated during creation.
    # We dont have the private_access_channel_key during create. So getting it using analytics_instance GET api
    def get_resource(self):
        private_access_channels = self.list_resources()
        if private_access_channels:
            for channel in private_access_channels:
                resource_dict = to_dict(channel)
                private_access_channel_key = self.module.params.get(
                    "private_access_channel_key"
                )
                if (
                    private_access_channel_key
                    and private_access_channel_key == channel.key
                ):
                    return oci_common_utils.get_default_response_from_resource(
                        resource=channel
                    )
                elif oci_common_utils.compare_dicts(
                    source_dict=self.module.params,
                    target_dict=resource_dict,
                    ignore_attr_if_not_in_target=True,
                ):
                    return oci_common_utils.get_default_response_from_resource(
                        resource=channel
                    )

        return oci_common_utils.raise_does_not_exist_service_error()


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
