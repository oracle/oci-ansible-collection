# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.util import to_dict

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicationHelperCustom:
    """
    Helper Custom for Marketplace Publications.
    """

    def get_create_model_dict_for_idempotence_check(self, create_model):
        """
        Override the generated api to exclude params in create model,
        that are:
            1. not present in existing resource models and
            2. can not be fetched via any other api in the sdk client and
            3. dont have relevance as far as the uniqueness of a
               Publication resource is concerned.
        """

        create_model_dict = super(
            PublicationHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)

        if create_model_dict and "package_details" in create_model_dict:
            create_model_dict["package_details"].pop("eula", None)

        return create_model_dict

    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        """
        Overrides the generated method to include package_details
        in the existing_resource.
        """

        existing_resource_dict = super(
            PublicationHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)

        # fetch package details
        package_details = to_dict(
            oci_common_utils.call_with_backoff(
                self.client.get_package,
                listing_id=existing_resource_dict["id"],
                package_version=self.module.params.get("package_details").get(
                    "package_version"
                ),
            ).data
        )

        # populate in existing resource
        existing_resource_dict["package_details"] = {
            "package_version": package_details.get("version"),
            "package_type": package_details.get("package_type"),
            "operating_system": package_details.get("operating_system"),
            "image_id": package_details.get("image_id"),
        }

        return existing_resource_dict

    def get_exclude_attributes(self):
        """
        Overrides the generated method to remove package_details
        from the attributes excluded for idempotence check.

        package_details will not be excluded for idempotency check now
        as we are populating necessary details in the resource dictionary
        in get_existing_resource_dict_for_idempotence_check method
        """
        exclude_attributes = super(
            PublicationHelperCustom, self
        ).get_exclude_attributes()

        remove_exclude_attributes = ["package_details"]
        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exclude_attributes
        ]

        return exclude_attributes
