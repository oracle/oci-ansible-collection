# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)


try:
    from oci.bds.models import RemoveAutoScalingConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False

logger = oci_common_utils.get_logger("oci_bigdata_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


# BDS has a list of nodes. The update operation only updates the tags not the nodes.
# If the user updates the nodes count and reruns, nothing will happen
# because we exclude the nodes from the idempotency check.
# Some node types can be updated using actions.
class BdsInstanceHelperCustom:
    def get_exclude_attributes(self):
        exclude_attributes = super(
            BdsInstanceHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "nodes",  # Nodes can have different number and types, update is not supported
        ]


class BdsInstanceActionsHelperCustom:
    # We need to check the value of is_cloud_sql_configured to know if SQL is configured for idempotency check
    def is_action_necessary(self, action, resource):
        if (
            action.lower() == "add_cloud_sql"
            and resource.is_cloud_sql_configured is True
        ):
            return False
        if (
            action.lower() == "remove_cloud_sql"
            and resource.is_cloud_sql_configured is False
        ):
            return False
        return super(BdsInstanceActionsHelperCustom, self).is_action_necessary(
            action, resource
        )


class BdsAutoScaleConfigHelperCustom:
    ########################################################################################################################
    # ------ OVERRIDES FOR CREATE_OPERATION AS THE WORK_REQUEST RESPONSE DOES NOT RETURN BACK ID OF AUTOSCALECONFIG ------ #

    # This is just a dummy function so that the waiting logic does not thrown an error. The work request does not
    # return the autoScaleConfig resource. So we will have to fetch it by running list_resources() on the bds_instance.
    def get_get_fn(self):
        def get_fn(auto_scaling_configuration_id):
            return oci_common_utils.get_default_response_from_resource(resource=None)

        return get_fn

    def create_resource(self):
        super(BdsAutoScaleConfigHelperCustom, self).create_resource()
        list_auto_scale_configs = self.list_resources()

        auto_scale_config_id = None
        for auto_scale_config in list_auto_scale_configs:
            if (
                auto_scale_config.display_name == self.module.params.get("display_name")
                and auto_scale_config.lifecycle_state == "ACTIVE"
            ):
                auto_scale_config_id = auto_scale_config.id
                break

        if not auto_scale_config_id:
            self.module.fail_json(
                msg="Error fetching the created AutoScaleConfig resource."
            )

        return oci_common_utils.call_with_backoff(
            self.client.get_auto_scaling_configuration,
            bds_instance_id=self.module.params.get("bds_instance_id"),
            auto_scaling_configuration_id=auto_scale_config_id,
        ).data

    ########################################################################################################################

    # logic for idempotency
    # is_enabled and cluster_admin_password are not available in get_resource() operation
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            BdsAutoScaleConfigHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # If is_enabled is True,
        # this should result in the lifecycle_state as ACTIVE.
        # If is_enabled is False,
        # that should result in the lifecycle_state as DELETED.
        if create_model_dict.get("is_enabled") is True:
            create_model_dict["lifecycle_state"] = "ACTIVE"
        elif create_model_dict.get("is_enabled") is False:
            create_model_dict["lifecycle_state"] = "DELETED"
        return create_model_dict

    # logic for idempotency
    # is_enabled and cluster_admin_password are not available in get_resource() operation
    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            BdsAutoScaleConfigHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        # If is_enabled is True,
        # this should update the lifecycle_state to ACTIVE.
        # If is_enabled is False,
        # that should update the lifecycle_state to DELETED.
        if update_model_dict.get("is_enabled") is True:
            update_model_dict["lifecycle_state"] = "ACTIVE"
        elif update_model_dict.get("is_enabled") is False:
            update_model_dict["lifecycle_state"] = "DELETED"
        update_model_dict.pop("is_enabled", None)
        update_model_dict.pop("cluster_admin_password", None)
        return update_model_dict

    # customizations for delete_resource operation
    # overiding this method as the service team have written a `POST` API for this as an action, instead
    # of a `DELETE` operation.
    def delete_resource(self):
        remove_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveAutoScalingConfigurationDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_auto_scaling_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                bds_instance_id=self.module.params.get("bds_instance_id"),
                auto_scaling_configuration_id=self.module.params.get(
                    "auto_scaling_configuration_id"
                ),
                remove_auto_scaling_configuration_details=remove_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


class BdsMetastoreConfigurationHelperCustom:

    # remove the bds_api_key_passphrase, cluster_admin_password parameters for the idempotence check,
    # As get_resource doesn't return these parameters.
    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            BdsMetastoreConfigurationHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        update_model_dict.pop("bds_api_key_passphrase", None)
        update_model_dict.pop("cluster_admin_password", None)
        return update_model_dict
