# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from base64 import b64encode


class PrivateApplicationHelperCustom:
    """
    Custom helper for PrivateApplicationHelper resource.
    """

    def get_logo_file_b64_encoded_string(self, private_app_id):
        """
        Get logo file base64 encoded for the given private application id.
        @param private_app_id: str, private application id
        :returns: str, base64 encoded logo file
        """
        response = self.client.get_private_application_action_download_logo(
            private_app_id
        ).data

        chunk_size = oci_common_utils.MEBIBYTE
        file_content = b""
        for chunk in response.raw.stream(chunk_size, decode_content=True):
            file_content += chunk

        return "data:application/zip;base64," + b64encode(file_content).decode("ascii")

    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        """
        Overrides the generated method to include logo file.
        """

        existing_resource_dict = super(
            PrivateApplicationHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)

        logo_file = self.get_logo_file_b64_encoded_string(existing_resource.id)
        existing_resource_dict["logo_file_base64_encoded"] = logo_file

        return existing_resource_dict

    def get_existing_resource_dict_for_update(self):
        """
        Overrides the generated method to include logo file.
        """

        existing_resource_dict = super(
            PrivateApplicationHelperCustom, self
        ).get_existing_resource_dict_for_update()

        logo_file = self.get_logo_file_b64_encoded_string(
            existing_resource_dict.get("id", None)
        )
        existing_resource_dict["logo_file_base64_encoded"] = logo_file

        return existing_resource_dict

    def get_exclude_attributes(self):
        """
        Overriding the method to remove logo_file_base64_encoded
        from the excluded attributes.

        logo_file_base64_encoded will not be ignored during idempotence
        check as we are populating the required data in
        get_existing_resource_dict_for_update method.
        """
        exclude_attributes = super(
            PrivateApplicationHelperCustom, self
        ).get_exclude_attributes()

        remove_exclude_attributes = ["logo_file_base64_encoded"]
        exclude_attributes = [
            x for x in exclude_attributes if x not in remove_exclude_attributes
        ]

        return exclude_attributes
