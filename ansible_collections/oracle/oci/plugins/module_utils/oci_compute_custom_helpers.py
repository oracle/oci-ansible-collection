# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils._text import to_text
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.core.models import ImageShapeCompatibilityEntry

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AppCatalogSubscriptionHelperCustom:
    def __init__(self, module, resource_type, service_client_class, namespace):
        module.params["resource_version"] = module.params["listing_resource_version"]

        super(AppCatalogSubscriptionHelperCustom, self).__init__(
            module, resource_type, service_client_class, namespace
        )

    # app_catalog_subscription does not have a resource id. It only has a create and delete operation.
    # Both can be distinguished based on the `state` attribute. So customise `get_module_resource_id` to return None
    # so that `is_create` would return True when state is present.
    def get_module_resource_id(self):
        return None

    def get_resource(self):
        app_catalog_subscriptions = oci_common_utils.list_all_resources(
            self.client.list_app_catalog_subscriptions,
            compartment_id=self.module.params["compartment_id"],
            listing_id=self.module.params["listing_id"],
        )
        for app_catalog_subscription in app_catalog_subscriptions:
            if (
                app_catalog_subscription.listing_resource_version
                == self.module.params["resource_version"]
            ):
                return oci_common_utils.get_default_response_from_resource(
                    resource=app_catalog_subscription
                )
        raise oci_common_utils.raise_does_not_exist_service_error(
            message="The app catalog subscription does not exist."
        )

    def get_exclude_attributes(self):
        exclude_attributes = super(
            AppCatalogSubscriptionHelperCustom, self
        ).get_exclude_attributes()
        # exclude the attributes from the create model which are not present in the get model for idempotency check
        return exclude_attributes + [
            "oracle_terms_of_use_link",
            "eula_link",
            "time_retrieved",
            "signature",
        ]


class InstanceHelperCustom:
    def get_exclude_attributes(self):
        return super(InstanceHelperCustom, self).get_exclude_attributes() + [
            "create_vnic_details",
        ]

    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            InstanceHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # is_pv_encryption_in_transit_enabled is a top level param on LaunchInstanceDetails but it gets returned
        # inside Instance.LaunchOptions so we need to propagate the value so that the existing resource matching
        # logic works properly
        if create_model_dict.get("is_pv_encryption_in_transit_enabled") is not None:
            launch_options = dict(
                is_pv_encryption_in_transit_enabled=create_model_dict.pop(
                    "is_pv_encryption_in_transit_enabled"
                )
            )
        else:
            launch_options = dict()
        create_model_dict["launch_options"] = launch_options
        return create_model_dict


class InstanceConsoleHistoryContentFactsHelperCustom:
    # API returns bytes. Convert to text and return to the user.
    def get_resource(self):
        super_get_response = super(
            InstanceConsoleHistoryContentFactsHelperCustom, self
        ).get_resource()
        if super_get_response.data:
            super_get_response.data = to_text(super_get_response.data)
        return super_get_response


class BootVolumeAttachmentHelperCustom:
    # An instance can only be attached to one boot volume and the name given to the attachment does not affect the
    # resource. Also a display_name update to the attachment resource does not seem to take affect.
    # So exclude display_name for idempotency.
    def get_exclude_attributes(self):
        return super(
            BootVolumeAttachmentHelperCustom, self
        ).get_exclude_attributes() + ["display_name"]


class ImageHelperCustom:
    def get_exclude_attributes(self):
        exclude_attributes = super(ImageHelperCustom, self).get_exclude_attributes()
        # exclude the attributes from the create model which are not present in the get model for idempotency check
        return exclude_attributes + [
            "instance_id",
            "image_source_details",
        ]


class ImageShapeCompatibilityEntryHelperCustom:
    def get_resource(self):
        # This resource does not have a get or list method. `update` and `delete` does not return anything and
        # updating even if the entry exists does not throw any error. Same with delete. So choosing to make the API
        # call always. The customisation for `get_resource` is only to make the other functions work and to return
        # some data to the user.
        return oci_common_utils.get_default_response_from_resource(
            resource=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, ImageShapeCompatibilityEntry
            )
        )

    def is_update_necessary(self):
        # This resource does not have a get or list method. So no way to check if it already exists or not. So always
        # update. Also making the API call even if the entry exists does not throw any error. So choosing to make
        # the API call always.
        return True
