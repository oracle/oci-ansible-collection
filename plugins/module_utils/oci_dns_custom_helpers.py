# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class ZoneHelperCustom:
    def get_get_model_from_summary_model(self, summary_model):
        if self.module.params.get("scope") is not None:
            return oci_common_utils.call_with_backoff(
                self.client.get_zone,
                zone_name_or_id=summary_model.id,
                scope=self.module.params.get("scope"),
            ).data
        return super(ZoneHelperCustom, self).get_get_model_from_summary_model(
            summary_model
        )


# This class handles some of the common customisations across some of the dns modules which works on a collection of
# records. For ex: zone_records, domain_records, rrset etc.
#
# Some of the common customisations that apply to these modules are:
#   * Have both update and patch methods and differentiators method customisations (is_update, is_patch). There is no
#     clear differentiation between between update and patch in general since they both need a resource id and same
#     state value. But in the DNS records modules, we can differentiate them using the existence of some attributes like
#     update_items, patch_items etc.
#   * update_items and patch_items are mutually exclusive
#   * update and patch methods do not support check mode and check changed based on the changed resource value
#     after performing the operation. This is done so that some of the fields (for ex: rdata) is normalized in the
#     server and would not be same to what are sent during create. We need third party libraries if we need to normalize
#     and perform the check which is not an option since this would put a dependency on that for using our modules.
#     Another option would be to just exclude those attributes but I don't think it is a good idea either since we
#     would not be able to handle updates in those fields. This behaviour is consistent with the legacy modules.
class DNSRecordsHelperCustom:
    def __init__(self, *args, **kwargs):
        super(DNSRecordsHelperCustom, self).__init__(*args, **kwargs)
        if (
            self.module.params.get("update_items") is not None
            and self.module.params.get("patch_items") is not None
        ):
            self.module.fail_json(
                msg="update_items and patch_items are mutually exclusive"
            )
        self.module.params["items"] = self.module.params.get(
            "update_items"
        ) or self.module.params.get("patch_items")

    def is_update(self):
        is_update = super(DNSRecordsHelperCustom, self).is_update()
        if not is_update:
            return False
        if self.module.params.get("update_items") is None:
            return False
        return True

    def is_patch(self):
        is_patch = super(DNSRecordsHelperCustom, self).is_patch()
        if not is_patch:
            return False
        if self.module.params.get("patch_items") is None:
            return False
        return True


class ZoneRecordsHelperCustom(DNSRecordsHelperCustom):
    # This is one of scenarios where the update takes a list of items.
    # The list API returns a list of items and we need to know if we need to do update or not
    # It is not possible to find which resource user is trying to update because
    # we have the input as list of items. So returning None for get_resource so the update always happens
    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(resource=None)


class DomainRecordsHelperCustom(DNSRecordsHelperCustom):
    pass


class RrsetHelperCustom(DNSRecordsHelperCustom):
    pass


class ViewHelperCustom:
    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_view,
            view_id=summary_model.id,
            scope=self.module.params.get("scope"),
        ).data


class ResolverHelperCustom:
    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver,
            resolver_id=summary_model.id,
            scope=self.module.params.get("scope"),
        ).data


class ResolverEndpointHelperCustom:
    def get_resource(self):
        # The API endpoint for getting endpoint intermittently fails with 404. CLI has the same issue as well so it
        # should be an API issue. The console uses the get_resolver endpoint to get the details of endpoints as well.
        # So using the same here as well.
        resolver = oci_common_utils.call_with_backoff(
            self.client.get_resolver,
            resolver_id=self.module.params.get("resolver_id"),
            scope=self.module.params.get("scope"),
        ).data
        endpoints = resolver.endpoints or []
        for endpoint in endpoints:
            if endpoint.name == self.module.params.get("name"):
                return oci_common_utils.get_default_response_from_resource(
                    resource=self.get_get_model_from_summary_model(endpoint)
                )
        return oci_common_utils.raise_does_not_exist_service_error()

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver_endpoint,
            resolver_id=self.module.params.get("resolver_id"),
            resolver_endpoint_name=summary_model.name,
            scope=self.module.params.get("scope"),
        ).data


class ZoneActionsHelperCustom:
    """
    Customizes any generated behavior in the ZoneActionsHelperGen.
    """

    def get_resource(self):
        """
        Override the generated method to include the optional params
        while performing get_resource, before applying any action.
        """

        optional_get_method_params = ["scope"]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_zone,
            zone_name_or_id=self.module.params.get("zone_id"),
            **optional_kwargs
        )


class ViewActionsHelperCustom:
    """
    Customizes any generated behavior in the ViewActionsHelperGen.
    """

    def get_resource(self):
        """
        Override the generated method to include the optional params
        while performing get_resource, before applying any action.
        """

        optional_get_method_params = ["scope"]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_view,
            view_id=self.module.params.get("view_id"),
            **optional_kwargs
        )


class TsigKeyActionsHelperCustom:
    """
    Customizes any generated behavior in the TsigKeyActionsHelperGen.
    """

    def get_resource(self):
        """
        Override the generated method to include the optional params
        while performing get_resource, before applying any action.
        """

        optional_get_method_params = ["scope"]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_tsig_key,
            tsig_key_id=self.module.params.get("tsig_key_id"),
            **optional_kwargs
        )


class SteeringPolicyActionsHelperCustom:
    """
    Customizes any generated behavior in the SteeringPolicyActionsHelperGen.
    """

    def get_resource(self):
        """
        Override the generated method to include the optional params
        while performing get_resource, before applying any action.
        """

        optional_get_method_params = ["scope"]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_steering_policy,
            steering_policy_id=self.module.params.get("steering_policy_id"),
            **optional_kwargs
        )


class ResolverActionsHelperCustom:
    """
    Customizes any generated behavior in the ResolverActionsHelperGen.
    """

    def get_resource(self):
        """
        Override the generated method to include the optional params
        while performing get_resource, before applying any action.
        """

        optional_get_method_params = ["scope"]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_resolver,
            resolver_id=self.module.params.get("resolver_id"),
            **optional_kwargs
        )
