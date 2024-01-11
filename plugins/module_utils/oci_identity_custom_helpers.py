# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

"""This module contains all the customisations for identity modules."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.exceptions import ServiceError, MaximumWaitTimeExceeded

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False
import logging

logger = logging.getLogger(__name__)


class ApiKeyHelperCustom:
    # For idempotence comparison
    # We pass as key and get key_value in response
    def get_existing_resource_dict_for_idempotence_check(self, resource):
        existing_dict = super(
            ApiKeyHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(resource)
        if "key_value" in existing_dict:
            existing_dict["key"] = existing_dict["key_value"]
        return existing_dict

    def get_exclude_attributes(self):
        exclude_attributes = super(ApiKeyHelperCustom, self).get_exclude_attributes()
        remove_exlcuded_attributes = ["key"]

        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exlcuded_attributes
        ]

        return exclude_attributes


class CompartmentHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        if module.params.get("compartment_id") and module.params.get(
            "parent_compartment_id"
        ):
            module.fail_json(
                msg="Parameters are mutually exclusive: compartment_id, parent_compartment_id."
            )

        super(CompartmentHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # default implementation ends up using "comparment_id" from response
    # as the unique identifier but we really want to use "id"
    # otherwise we will end up trying to update the parent compartment of the
    # one we are aiming for
    def set_required_ids_in_module_when_name_is_identifier(self, resource):
        id_param = self.get_module_resource_id_param()
        if resource.get("id"):
            self.module.params[id_param] = resource["id"]

    # the module uses 'parent_compartment_id' so as not to conflict with the compartment_id
    # parameter on UPDATE, but the SDK/API operation expects 'compartment_id'
    def get_create_model(self):
        params_copy = self.module.params.copy()
        params_copy["compartment_id"] = params_copy["parent_compartment_id"]
        return oci_common_utils.convert_input_data_to_model_class(
            params_copy, self.get_create_model_class()
        )

    def get_required_kwargs_for_list(self):
        # the module 'compartment_id' parameter represents the unique identifier for a compartment
        # to be used by update and delete
        # any time we are listing compartments to do an idempotency check or to find a resource by name
        # we want to use 'parent_compartment_id'
        return {"compartment_id": self.module.params.get("parent_compartment_id")}


class CompartmentFactsHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        if module.params.get("compartment_id") and module.params.get(
            "parent_compartment_id"
        ):
            module.fail_json(
                msg="Parameters are mutually exclusive: compartment_id, parent_compartment_id."
            )

        super(CompartmentFactsHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    def list_subcompartments(self, compartment_id, optional_kwargs):
        subcompartments = []

        immediate_subcompartments = oci_common_utils.list_all_resources(
            self.client.list_compartments,
            compartment_id=compartment_id,
            **optional_kwargs
        )

        if immediate_subcompartments:
            subcompartments.extend(immediate_subcompartments)

        for comp in immediate_subcompartments:
            subcompartments.extend(self.list_subcompartments(comp.id, optional_kwargs))
        return subcompartments

    def list_resources(self):
        optional_list_method_params = [
            "access_level",
            "compartment_id_in_subtree",
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )

        parent_compartment_id = self.module.params.get("parent_compartment_id")
        # service doesn't support `compartment_id_in_subtree` for non root compartments
        # but we do as a matter of convenience
        if not self.is_compartment_root(
            parent_compartment_id
        ) and self.module.params.get("compartment_id_in_subtree"):
            # compartment_id_in_subtree is not allowed on list calls for non root compartment
            del optional_kwargs["compartment_id_in_subtree"]
            # name filtering is done AFTER because we don't want to prune the search
            # based on name without searching subcompartments
            if "name" in optional_kwargs:
                del optional_kwargs["name"]

            subcompartments = self.list_subcompartments(
                parent_compartment_id, optional_kwargs
            )
            if self.module.params.get("name"):
                subcompartments = [
                    compartment
                    for compartment in subcompartments
                    if compartment.name == self.module.params.get("name")
                ]

            return subcompartments
        else:
            return oci_common_utils.list_all_resources(
                self.client.list_compartments,
                compartment_id=self.module.params.get("parent_compartment_id"),
                **optional_kwargs
            )

    def is_compartment_root(self, compartment_id):
        # Returns True when compartment_id is OCID of the tenancy.
        # can't do GET compartment because user may not have access
        # so use GetTenancy which will return the tenancy if
        # compartment_id == tenancy_ocid and will give 404 otherwise
        try:
            oci_common_utils.call_with_backoff(
                self.client.get_tenancy, tenancy_id=compartment_id
            ).data
        except ServiceError as se:
            if se.status == 404:
                return False
            else:
                raise

        return True


class MfaTotpDeviceActionsHelperCustom:
    def is_action_necessary(self, action, resource):
        if action.upper() == "ACTIVATE":
            if resource.is_activated:
                return False
            return True
        elif action.upper() == "GENERATE_TOTP_SEED":
            return True


class MfaTotpDeviceHelperCustom:
    def get_matching_resource(self):
        # mfa_totp_device has no create model, there are no params
        # and a user can only have one mfa_totp_device
        # therefore, if any mfa totp device exists for this user,
        # it is a match
        for resource in self.list_resources():
            if not self._is_resource_active(resource):
                continue

            return resource
        return None


class PolicyHelperCustom:
    # user must pass in version date in format YYYY-MM-DD but service
    # returns it as 2020-01-17T00:00:00+00:00 so we need to normalize
    # for comparison purposes
    def update_version_date(self, model_dict):
        if model_dict["version_date"]:
            model_dict["version_date"] = "{version_date}T00:00:00+00:00".format(
                version_date=model_dict["version_date"]
            )

        return model_dict

    def get_create_model_dict_for_idempotence_check(self, create_model):
        model_dict = super(
            PolicyHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        self.update_version_date(model_dict)
        return model_dict

    def get_update_model_dict_for_idempotence_check(self, update_model):
        model_dict = super(
            PolicyHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        self.update_version_date(model_dict)
        return model_dict


class UiPasswordHelperCustom:
    def is_create(self):
        return True


class TagHelperCustom:
    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            TagHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        resource = self.get_resource().data
        if (
            update_model_dict["validator"]
            and update_model_dict["validator"]["validator_type"] == "DEFAULT"
            and resource.validator is None
        ):
            update_model_dict["validator"] = None
        return update_model_dict


class UserCapabilitiesHelperCustom:

    # As per API documentation operation `UpdateUserCapabilities` returns `User` resource in response body.
    # This override is required as generated module doesn't have get_resource method to return `User` resource.
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user, user_id=self.module.params.get("user_id"),
        )

    # for idempotency check we compare `UpdateUserCapabilitiesDetails` and `UserCapabilities`.
    # There is no API call to fetch just `UserCapabilities` resource for a user. This resource is a part of
    # `User` resource.
    def is_update_necessary(self, existing_resource_dict):
        update_model = self.get_update_model()
        update_model_dict = self.get_update_model_dict_for_idempotence_check(
            update_model
        )
        update_is_necessary = not oci_common_utils.compare_dicts(
            update_model_dict, existing_resource_dict["capabilities"]
        )

        logger.debug(
            "is update necessary for {resource_type}: {update_is_necessary}".format(
                resource_type=self.get_response_field_name(),
                update_is_necessary=update_is_necessary,
            )
        )

        return update_is_necessary


class UserStateHelperCustom:

    # As per API documentation operation `UpdateUserState` returns `User` resource in response body.
    # This override is required as generated module doesn't have get_resource method to return `User` resource.
    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_user, user_id=self.module.params.get("user_id"),
        )

    # operation `UpdateUserState` updates state to unblocked. Only "false" is supported
    # (for changing the state to unblocked). If set to "true" API throws an error: Changing
    # user state to 'Blocked' is not supported.
    def is_update_necessary(self, existing_resource_dict):
        if self.module.params.get("blocked") is not None and not self.module.params.get(
            "blocked"
        ):
            if existing_resource_dict.get("inactive_status", None) == 4:
                return True
            else:
                return False
        return super(UserStateHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )


class TagActionsHelperCustom:
    # overriding the perform_action method as bulk_delete tags operation does not support
    # get_resource method which is an integral part of the main perform_action method
    def perform_action(self, action):
        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))

        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=None,
            )

        # if sent list is empty or None, return back without performing the action with
        # status of resource as not changed
        if action == "bulk_delete":
            tag_ids = self.module.params.get("tag_definition_ids")
            if not tag_ids:
                return self.prepare_result(
                    changed=False,
                    resource_type=self.get_response_field_name(action),
                    resource=None,
                )

        try:
            action_fn()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=None,
            )


class CompartmentActionsHelperCustom:
    # overriding the perform_action method as bulk_move and bulk_delete actions do not support
    # get_resource method which is an integral part of the main perform_action method
    def perform_action(self, action):
        if action in ["move", "recover"]:
            return super(CompartmentActionsHelperCustom, self).perform_action(action)

        action_fn = self.get_action_fn(action)
        if not action_fn:
            self.module.fail_json(msg="{0} not supported by the module.".format(action))

        if self.check_mode:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=None,
            )

        # if resource list is empty or None, return back without performing the action with
        # status of resource as not changed
        resources_list = self.module.params.get("resources")
        if not resources_list:
            return self.prepare_result(
                changed=False,
                resource_type=self.get_response_field_name(action),
                resource=None,
            )

        try:
            action_fn()
        except MaximumWaitTimeExceeded as mwtex:
            self.module.fail_json(msg=str(mwtex))
        except ServiceError as se:
            self.module.fail_json(
                msg="Performing action failed with exception: {0}".format(se.message)
            )
        else:
            return self.prepare_result(
                changed=True,
                resource_type=self.get_response_field_name(action),
                resource=None,
            )

    # this method is overridden to ensure idempotency for the move and recover actions
    def is_action_necessary(self, action, resource_data):
        if action == "move":
            return resource_data.compartment_id != self.module.params.get(
                "target_compartment_id"
            )
        if action == "recover":
            return resource_data.lifecycle_state == "DELETED"
        return super(CompartmentActionsHelperCustom, self).is_action_necessary(
            action, resource_data
        )


class TagDefaultHelperCustom:
    def get_optional_kwargs_for_list(self):
        if self.module.params.get("tag_definition_id"):
            return dict(tag_definition_id=self.module.params.get("tag_definition_id"))
        elif self.module.params.get("compartment_id"):
            return dict(tag_definition_id=self.module.params.get("compartment_id"))
        return dict()
