# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

try:
    import oci
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)

logger = oci_common_utils.get_logger("oci_database_management_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def _info(s):
    get_logger().info(s)


def get_logger():
    return logger


# this method is added for comparing the parameters keys which are generated during `change parameter
# operation`, mainly added to support the idempotency logic
def compare_change_db_params(existing_params, new_param):
    is_value_not_equal = new_param.get("value", None) != existing_params.value
    is_comment_not_equal = (
        new_param.get("update_comment", None) != existing_params.update_comment
    )
    if is_value_not_equal or is_comment_not_equal:
        return True
    return False


class DatabaseParameterActionsHelperCustom:
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.list_database_parameters,
                managed_database_id=self.module.params.get("managed_database_id"),
            )
        )

    # overriding as there was conflict with the parameters parameter so changed the name of reset operation
    # parameter to `reset_parameters`
    def reset(self):
        reset_parameters_value = self.module.params.get("reset_parameters")
        self.module.params["parameters"] = reset_parameters_value
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params,
            oci.database_management.models.ResetDatabaseParametersDetails,
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.reset_database_parameters,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                reset_database_parameters_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    # overriding as there was conflict with the parameters parameter so changed the name of change operation
    # parameter to `change_parameters`
    def change(self):
        change_parameters_value = self.module.params.get("change_parameters")
        self.module.params["parameters"] = change_parameters_value
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params,
            oci.database_management.models.ChangeDatabaseParametersDetails,
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_database_parameters,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
                change_database_parameters_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )

    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        existing_params = {}
        for res in resource:
            existing_params[str(res.name)] = res
        if action == "change":
            for params in self.module.params.get("change_parameters"):
                if params["name"] in existing_params:
                    is_not_equal = compare_change_db_params(
                        existing_params[params["name"]], params
                    )
                    if is_not_equal:
                        return True
                else:
                    return True
            return False
        return super(DatabaseParameterActionsHelperCustom, self).is_action_necessary(
            action, resource
        )

    # For the 'change' action we are setting the required response type with error_code, status
    # and error_message, as the response type defined in the spec was None for the non is_action_
    # necessary tasks
    def perform_action(self, action):

        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))
        if action == "change":
            try:
                get_response = self.get_resource()
            except ServiceError as se:
                self.module.fail_json(
                    msg="Getting resource failed with exception: {0}".format(se.message)
                )
            else:
                resource = to_dict(get_response.data)
            is_action_necessary = self.is_action_necessary(action, get_response.data)
            if not is_action_necessary:
                action_response = (
                    oci.database_management.models.update_database_parameters_result.UpdateDatabaseParametersResult()
                )
                setattr(action_response, "status", {})
                all_params = self.module.params.get("change_parameters")
                for param in all_params:
                    db_param_status = (
                        oci.database_management.models.database_parameter_update_status.DatabaseParameterUpdateStatus()
                    )
                    setattr(db_param_status, "status", "SUCCEEDED")
                    setattr(db_param_status, "error_code", None)
                    setattr(db_param_status, "error_message", None)
                    action_response.status[str(param["name"])] = db_param_status

                return self.prepare_result(
                    changed=False,
                    resource_type=self.get_response_field_name(action),
                    resource=to_dict(action_response),
                )

            if self.check_mode:
                return self.prepare_result(
                    changed=True,
                    resource_type=self.get_response_field_name(action),
                    resource=resource,
                )

            try:
                actioned_resource = action_fn()
            except MaximumWaitTimeExceeded as mwtex:
                self.module.fail_json(msg=str(mwtex))
            except ServiceError as se:
                self.module.fail_json(
                    msg="Performing action failed with exception: {0}".format(
                        se.message
                    )
                )
            else:
                try:
                    actioned_resource = actioned_resource or self.get_resource().data
                except (ServiceError, NotImplementedError) as ex:
                    _debug(
                        "Action {0} succeeded but did not return the resource. Error fetching the resource using "
                        "the get operation: {1}".format(action, ex)
                    )
                return self.prepare_result(
                    changed=True,
                    resource_type=self.get_response_field_name(action),
                    resource=to_dict(actioned_resource),
                )
        else:
            return super(DatabaseParameterActionsHelperCustom, self).perform_action(
                action
            )


class ManagedDatabaseGroupActionsHelperCustom:
    def is_action_necessary(self, action, resource=None):
        resource = resource or self.get_resource().data
        managed_dbs_list = getattr(resource, "managed_databases", None) or []
        _debug(
            "MDB Resource details {0} {1} {2}".format(
                managed_dbs_list, action, self.module.params.get("managed_database_id")
            )
        )
        if action == "add_managed_database":
            if managed_dbs_list:
                managed_db_ids = [
                    getattr(managed_db, "id", None) for managed_db in managed_dbs_list
                ]
                if (
                    managed_db_ids
                    and self.module.params.get("managed_database_id") in managed_db_ids
                ):
                    return False
                else:
                    return True
            else:
                return True
        elif action == "remove_managed_database":
            if managed_dbs_list:
                managed_db_ids = [
                    getattr(managed_db, "id", None) for managed_db in managed_dbs_list
                ]
                if (
                    managed_db_ids
                    and self.module.params.get("managed_database_id") in managed_db_ids
                ):
                    return True
                else:
                    return False
            else:
                return False
        else:
            return super(
                ManagedDatabaseGroupActionsHelperCustom, self
            ).is_action_necessary(action, resource)
