# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_config_utils,
    oci_common_utils,
)
from ansible.module_utils import six

try:
    from oci.mysql import WorkRequestsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


logger = oci_common_utils.get_logger("oci_mysql_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class MysqlDbSystemActionsHelperCustom:
    def get_action_desired_states(self, action):
        action_desired_states = super(
            MysqlDbSystemActionsHelperCustom, self
        ).get_action_desired_states(action)

        if action.lower() == "stop":
            return action_desired_states + [
                "INACTIVE",
            ]
        return action_desired_states

    def get_action_idempotent_states(self, action):
        action_idempotent_states = super(
            MysqlDbSystemActionsHelperCustom, self
        ).get_action_idempotent_states(action)

        if action.lower() == "stop":
            return action_idempotent_states + [
                "INACTIVE",
            ]
        return action_idempotent_states


# The waiter client for this service uses mysql WorkRequestsClient
class MysqlDbSystemHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        self.work_request_client = oci_config_utils.create_service_client(
            module, WorkRequestsClient
        )

        super(MysqlDbSystemHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # override the waiting client with the WorkRequestsClient
    def get_waiter_client(self):
        return self.work_request_client

    # get model doesn't return admin_username and admin_password of existing database resources. Thus, excluding
    # these for idempotency.
    def get_exclude_attributes(self):
        return super(MysqlDbSystemHelperCustom, self).get_exclude_attributes() + [
            "admin_password",
            "admin_username",
        ]

    def get_update_model(self):
        # right now this happens to be the same as exclude attributes
        # if the service eventually supports updating username / password
        # we should empty this list and leave exlude attributes, thus I am
        # keeping them as separate
        # this is a unique case for this API because it has fields on the Update model
        # that are not possible to update
        update_attributes_not_present_on_get_model_which_dont_support_update = [
            "admin_password",
            "admin_username",
        ]
        existing_resource_dict = self.get_existing_resource_dict_for_update()
        params_to_pass_in_update_call = {}

        # MySQL UpdateDbSystem will throw an error if you specify any fields in the update request that the service
        # does not allow updating (which is most of the fields)
        # Thus, we only want to pass through values that are updated relative to the existing value on the resource
        # For example, if we pass subnet_id, even if it is set to the same value as resource.subnet_id the service will
        # throw an error, so we have custom logic to exclude it
        for key, input_value in six.iteritems(self.module.params):
            if (
                key
                in update_attributes_not_present_on_get_model_which_dont_support_update
            ):
                continue

            if input_value is not None and key in existing_resource_dict:
                existing_value = existing_resource_dict[key]
                values_are_equal = input_value == existing_value
                dicts_are_equivalent = (
                    isinstance(input_value, dict)
                    and isinstance(existing_value, dict)
                    and oci_common_utils.compare_dicts(input_value, existing_value)
                )
                if values_are_equal or dicts_are_equivalent:
                    _debug(
                        "skipping updating field {field_name} because it already matches the value on the resource.".format(
                            field_name=key
                        )
                    )
                    continue

            params_to_pass_in_update_call[key] = input_value

        return oci_common_utils.convert_input_data_to_model_class(
            params_to_pass_in_update_call, self.get_update_model_class()
        )
