# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

"""This module contains all the customisations for identity modules."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class MfaTotpDeviceActionsHelperCustom:
    def is_action_necessary(self, action):
        if action.upper() == "ACTIVATE":
            resource = self.get_resource().data
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
    def convert_request_model_fields_to_computed_server_values(self, model):
        # user must pass in version date in format YYYY-MM-DD but service
        # returns it as 2020-01-17T00:00:00+00:00 so we need to normalize
        # for comparison purposes
        if model.version_date:
            model.version_date = "{version_date}T00:00:00+00:00".format(
                version_date=model.version_date
            )


class TagHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        if "name" in module.params:
            module.params["tag_name"] = module.params["name"]

        super(TagHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # there is no resource_id param for a tag, the name is the unique identifier
    # thus it is an update if the tag exists, and a create if it doesn't
    # so we re-use that logic from is_update_using_name
    def is_update(self):
        return self.is_update_using_name()

    # for this module, the name is the unique identifier so we always want
    # to use_name_as_identifier
    def _use_name_as_identifier(self):
        return True

    def get_module_resource_id(self):
        return None


class UiPasswordHelperCustom:

    # there is no concept of idempotency for this module
    # it re-executes create / reset password every time module is invoked
    def get_matching_resource(self):
        return None

    def get_module_resource_id(self):
        return None
