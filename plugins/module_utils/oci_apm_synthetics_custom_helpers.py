# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ScriptHelperCustom:
    # parameters value in the create model and get model are of different types.
    # List[ScriptParameter] vs List[ScriptParameterInfo]. So this customisation is added for the structure of the params
    # to match for idempotence check.
    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        resource_dict = super(
            ScriptHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)
        parameters = []
        existing_parameters = resource_dict.get("parameters")
        if existing_parameters:
            for existing_parameter in existing_parameters:
                parameters.append(existing_parameter.get("script_parameter"))
            resource_dict["parameters"] = parameters
        return resource_dict

    # if a script parameter is marked as secret, it would just contain "*****" in the get model.
    # So there is no reliable way for us to check it. So exclude that parameter for idempotence check.
    def get_create_model_dict_for_idempotence_check(self, existing_resource):
        create_model_dict = super(
            ScriptHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(existing_resource)
        parameters = create_model_dict.get("parameters")
        if parameters:
            for parameter in parameters:
                if parameter.get("is_secret"):
                    parameter.pop("param_value", None)
        return create_model_dict


class MonitorHelperCustom:
    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        resource_dict = super(
            MonitorHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)
        parameters = []
        existing_parameters = resource_dict.get("script_parameters")
        if existing_parameters:
            for existing_parameter in existing_parameters:
                parameters.append(existing_parameter.get("monitor_script_parameter"))
            resource_dict["script_parameters"] = parameters
        return resource_dict

    def get_existing_resource_dict_for_update(self):
        resource_dict = super(
            MonitorHelperCustom, self
        ).get_existing_resource_dict_for_update()
        parameters = []
        existing_parameters = resource_dict.get("script_parameters")
        if existing_parameters:
            for existing_parameter in existing_parameters:
                parameters.append(existing_parameter.get("monitor_script_parameter"))
            resource_dict["script_parameters"] = parameters
        return resource_dict

    def get_create_model_dict_for_idempotence_check(self, existing_resource):
        create_model_dict = super(
            MonitorHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(existing_resource)
        if create_model_dict.get("vantage_points"):
            create_model_dict["vantage_points"] = [
                dict(name=vantage_point)
                for vantage_point in create_model_dict["vantage_points"]
            ]
        return create_model_dict

    def get_update_model_dict_for_idempotence_check(self, update_model):
        update_model_dict = super(
            MonitorHelperCustom, self
        ).get_update_model_dict_for_idempotence_check(update_model)
        if update_model_dict.get("vantage_points"):
            update_model_dict["vantage_points"] = [
                dict(name=vantage_point)
                for vantage_point in update_model_dict["vantage_points"]
            ]
        return update_model_dict
