# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False

logger = oci_common_utils.get_logger("oci_logging_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class LogHelperCustom:
    def get_get_fn(self):
        def get_fn(log_id):
            return self.client.get_log(
                log_id=log_id, log_group_id=self.module.params["log_group_id"],
            )

        return get_fn


class LogActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        if action not in ["change_log_log_group"]:
            return super(LogActionsHelperCustom, self).is_action_necessary(
                action, resource
            )

        try:
            # parameter `target_log_group_id` is not marked as required but we receive Internal Server Error if we don't
            # pass it in request body. Ideally this case should have been handled by API. User will receive the Internal
            # Server Error if this parameter is unavailable in request body.
            if self.module.params.get("target_log_group_id") is None:
                return True

            oci_common_utils.call_with_backoff(
                self.client.get_log,
                log_group_id=self.module.params.get("target_log_group_id"),
                log_id=self.module.params.get("log_id"),
            )

        except ServiceError as se:
            if se.status == 404:
                _debug(
                    "Fetching Log resource failed with an exception: {0}".format(
                        se.message
                    )
                )
                return True
            raise
        else:
            return False

    def perform_action(self, action):
        if action not in ["change_log_log_group"]:
            return super(LogActionsHelperCustom, self).perform_action(action)

        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))

        is_action_necessary = self.is_action_necessary(action)

        # when action is not necessary it means that the log with given `log_id` is already a part of target group.
        # in that case we choose to return the `Log` in response. But here we would pass `target_log_group_id` as a
        # `log_group_id` to fetch `Log` resource otherwise we hit NotFoundException.
        if not is_action_necessary:
            resource = to_dict(
                oci_common_utils.call_with_backoff(
                    self.client.get_log,
                    log_group_id=self.module.params.get("target_log_group_id"),
                    log_id=self.module.params.get("log_id"),
                ).data
            )

            return self.prepare_result(
                changed=False, resource_type=self.resource_type, resource=resource
            )

        if self.check_mode:
            resource = self.get_resource().data
            return self.prepare_result(
                changed=True, resource_type=self.resource_type, resource=resource
            )

        try:
            actioned_resource = action_fn()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            # sometimes when there is no waiting and also the operation does not return anything. For ex: the bucket
            # action "make_bucket_writable" returns None and also there is no waiting. In those cases, get the resource
            # and return it instead.
            try:
                actioned_resource = actioned_resource or self.get_resource().data
            except (ServiceError, NotImplementedError) as ex:
                _debug(
                    "Action {0} succeeded but did not return the resource. Error fetching the resource using "
                    "the get operation: {1}".format(action, ex)
                )
            return self.prepare_result(
                changed=True,
                resource_type=self.resource_type,
                resource=to_dict(actioned_resource),
            )
