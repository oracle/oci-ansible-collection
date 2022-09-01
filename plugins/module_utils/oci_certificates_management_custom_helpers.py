# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_config_utils

try:
    from oci.certificates import CertificatesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class CaBundleHelperCustom:
    def __init__(self, *args, **kwargs):
        super(CaBundleHelperCustom, self).__init__(*args, **kwargs)
        self.certificates_client = oci_config_utils.create_service_client(
            self.module, CertificatesClient
        )

    def get_existing_resource_dict_for_update(self):
        existing_resource_dict = super(
            CaBundleHelperCustom, self
        ).get_existing_resource_dict_for_update()
        ca_bundle = self.certificates_client.get_ca_bundle(
            existing_resource_dict.get("id")
        ).data
        existing_resource_dict.update({"ca_bundle_pem": ca_bundle.ca_bundle_pem})
        return existing_resource_dict


class CertificateAuthorityVersionActionsHelperCustom:

    CANCEL_CERTIFICATE_AUTHORITY_VERSION_DELETION = (
        "cancel_certificate_authority_version_deletion"
    )
    SCHEDULE_CERTIFICATE_AUTHORITY_VERSION_DELETION = (
        "schedule_certificate_authority_version_deletion"
    )

    def is_action_necessary(self, action, resource=None):
        if action.upper() == self.CANCEL_CERTIFICATE_AUTHORITY_VERSION_DELETION.upper():
            # do cancel_certificate_authority_version_deletion when resource has time_of_deletion
            return resource.time_of_deletion is not None

        if (
            action.upper()
            == self.SCHEDULE_CERTIFICATE_AUTHORITY_VERSION_DELETION.upper()
        ):
            # do schedule_certificate_authority_version_deletion when the resource has no time_of_deletion
            return resource.time_of_deletion is None
        return super(
            CertificateAuthorityVersionActionsHelperCustom, self
        ).is_action_necessary(action, resource)
