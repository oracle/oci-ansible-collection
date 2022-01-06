# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)

__metaclass__ = type


class NotificationTopicHelperCustom:
    def get_get_model_from_summary_model(self, summary_model):
        return self.client.get_topic(topic_id=summary_model.topic_id).data

    # The generated module operations have NONE_WAITER which is not correct. Overriding to wait on lifecycle_state
    # waiter. This should ideally be handled in the codegen or add an override in oci_wait_utils instead of overriding
    # the whole methods. But adding an override in oci_wait_utils causes all the tests to run. There is already an
    # issue to redesign oci_wait_utils to avoid this.
    # TODO: Change this once the oci_wait_utils is redesigned
    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_topic,
            call_fn_args=(),
            call_fn_kwargs=dict(create_topic_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_topic,
            call_fn_args=(),
            call_fn_kwargs=dict(
                topic_id=self.module.params.get("topic_id"),
                topic_attributes_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_topic,
            call_fn_args=(),
            call_fn_kwargs=dict(topic_id=self.module.params.get("topic_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


class SubscriptionActionsHelperCustom:
    # the get_<functions> have been re-written as the actions_module expects the `id` parameter as an input
    # but fetches the subscription resource using the `subscription_id` parameter. This inconsistency starts
    # throwing error as the ONS service expects the subscriptionId parameter to fetch the resource.
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription, subscription_id=self.module.params.get("id"),
        )
