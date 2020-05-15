# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

"""This module contains all the customisations for identity modules."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApiKeyHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        model_dict = super(
            ApiKeyHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)

        if model_dict["key"]:
            model_dict["key_value"] = model_dict["key"]
            del model_dict["key"]

        return model_dict

    def get_attributes_to_consider_for_create_idempotency_check(self, create_model):
        attributes_to_consider = super(
            ApiKeyHelperCustom, self
        ).get_attributes_to_consider_for_create_idempotency_check(create_model)
        if "key" in attributes_to_consider:
            attributes_to_consider.remove("key")
            attributes_to_consider.append("key_value")

        return attributes_to_consider


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

    def list_resources(self):
        optional_list_method_params = []

        # the module 'compartment_id' parameter represents the unique identifier for a compartment
        # to be used by update and delete
        # any time we are listing compartments to do an idempotency check or to find a resource by name
        # we want to use 'parent_compartment_id'
        required_kwargs = {
            "compartment_id": self.module.params.get("parent_compartment_id")
        }

        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                not self.module.params.get("key_by")
                or param in self.module.params.get("key_by")
            )
        )

        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)

        return oci_common_utils.list_all_resources(
            self.client.list_compartments, **kwargs
        )


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

    def get_required_params_for_list(self):
        return [
            "parent_compartment_id",
        ]

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


class IdentityProviderHelperCustom:

    # metadata is not returned by GET or LIST so we should not try
    # to match using it
    def get_exclude_attributes(self):
        global_exclude_attribtes = super(
            IdentityProviderHelperCustom, self
        ).get_exclude_attributes()[:]
        global_exclude_attribtes.append("metadata")
        return global_exclude_attribtes


class UiPasswordHelperCustom:

    # there is no concept of idempotency for this module
    # it re-executes create / reset password every time module is invoked
    def get_matching_resource(self):
        return None

    def is_create(self):
        return True
