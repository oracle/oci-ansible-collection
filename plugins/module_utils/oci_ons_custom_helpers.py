# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

__metaclass__ = type


class NotificationTopicHelperCustom:
    def get_get_model_from_summary_model(self, summary_model):
        return self.client.get_topic(topic_id=summary_model.topic_id).data


class SubscriptionActionsHelperCustom:
    # the get_<functions> have been re-written as the actions_module expects the `id` parameter as an input
    # but fetches the subscription resource using the `subscription_id` parameter. This inconsistency starts
    # throwing error as the ONS service expects the subscriptionId parameter to fetch the resource.
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription, subscription_id=self.module.params.get("id"),
        )
