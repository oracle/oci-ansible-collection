# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.


from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils


class SecretBundleFactsHelperCustom:
    def get_required_params_for_get(self):
        # we combined get_secret_by_path with get_secret_bundle operation.
        # we could get either secret_name or secret_by_id
        # is_get method checks if all the get_required_params_for_get are not None.
        # We could get None for secret_id when secret_name is passed and vice versa.
        # Hence returning empty List as it is_get always return True
        return []

    def get_resource(self):
        optional_get_method_params = [
            "secret_id",
            "version_number",
            "secret_version_name",
            "stage",
            "secret_name",
            "vault_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        if self.module.params.get("secret_id", None):
            return oci_common_utils.call_with_backoff(
                self.client.get_secret_bundle, **optional_kwargs
            )
        return oci_common_utils.call_with_backoff(
            self.client.get_secret_bundle_by_name,
            secret_name=self.module.params.get("secret_name"),
            vault_id=self.module.params.get("vault_id"),
            stage=self.module.params.get("stage"),
        )
