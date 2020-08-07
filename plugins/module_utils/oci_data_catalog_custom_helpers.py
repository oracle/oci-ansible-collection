# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class DataCatalogDataAssetHelperCustom:
    # this resource does not use standard `id` or `resource_id` as identifier, it uses `key` or `data_asset_key`.
    # overriding this method due to naming mismatch in input parameter (data_asset_key) and output parameter (key)
    def get_get_model_from_summary_model(self, summary_model):
        return self.client.get_data_asset(
            catalog_id=self.module.params.get("catalog_id"),
            data_asset_key=summary_model.key,
        ).data

    # this resource does not use standard `id` or `resource_id` as identifier, it uses `key` or `connection_key`.
    # overriding this method due to naming mismatch in input parameter (connection_key) and output parameter (key)
    def set_required_ids_in_module_when_name_is_identifier(self, resource):
        self.module.params["data_asset_key"] = resource["key"]


class DataCatalogConnectionHelperCustom:
    # the parameter "is_default" causes problems and does not list any
    # resources even though all the parameters are same
    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "display_name",
        ]
        return dict(
            (param, self.module.params[param]) for param in optional_list_method_params
        )

    # this resource does not use standard `id` or `resource_id` as identifier, it uses `key` or `connection_key`.
    # overriding this method due to naming mismatch in input parameter (connection_key) and output parameter (key)
    def get_get_model_from_summary_model(self, summary_model):
        return self.client.get_connection(
            catalog_id=self.module.params.get("catalog_id"),
            data_asset_key=summary_model.data_asset_key,
            connection_key=summary_model.key,
        ).data

    # this resource does not use standard `id` or `resource_id` as identifier, it uses `key` or `connection_key`.
    # overriding this method due to naming mismatch in input parameter (connection_key) and output parameter (key)
    def set_required_ids_in_module_when_name_is_identifier(self, resource):
        self.module.params["connection_key"] = resource["key"]


class DataCatalogCatalogActionsHelperCustom:
    # Overriding this method for ensuring idempotency while attaching and detaching endpoints to the catalog.
    # Attach or Detach actions are not performed if an attached endpoint is retried to be attached again or
    # a detached endpoint is attempted to be detached again
    def is_action_necessary(self, action, resource):
        attached_endpoints = resource.attached_catalog_private_endpoints
        if action == "attach_catalog_private_endpoint":
            endpoint_to_attach = self.module.params.get("catalog_private_endpoint_id")
            return not (endpoint_to_attach in attached_endpoints)
        elif action == "detach_catalog_private_endpoint":
            endpoint_to_detach = self.module.params.get("catalog_private_endpoint_id")
            return endpoint_to_detach in attached_endpoints
        # the last return is for the remaining two actions
        return super(DataCatalogCatalogActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
