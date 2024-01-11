# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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


class DataKeysActionsHelperCustom:
    GENERATE_ACTION_KEY = "generate"
    REMOVE_ACTION_KEY = "remove"

    def get_resource(self):
        return oci_common_utils.get_default_response_from_resource(
            oci_common_utils.list_all_resources(
                self.client.list_data_keys,
                apm_domain_id=self.module.params.get("apm_domain_id"),
            )
        )

    def is_action_necessary(self, action, resource=None):
        resource_dict = to_dict(resource)
        if action == self.GENERATE_ACTION_KEY:
            keys_to_generate = []
            if self.module.params.get("generate_data_keys_list_details"):
                for data_key in self.module.params.get(
                    "generate_data_keys_list_details"
                ):
                    if not oci_common_utils.is_in_list(resource_dict, data_key):
                        keys_to_generate.append(data_key)
            if keys_to_generate:
                self.module.params["generate_data_keys_list_details"] = keys_to_generate
                return True
            return False
        elif action == self.REMOVE_ACTION_KEY:
            keys_to_remove = []
            if self.module.params.get("remove_data_keys_list_details"):
                for data_key in self.module.params.get("remove_data_keys_list_details"):
                    if oci_common_utils.is_in_list(resource_dict, data_key):
                        keys_to_remove.append(data_key)
            if keys_to_remove:
                self.module.params["remove_data_keys_list_details"] = keys_to_remove
                return True
            return False
        return super(DataKeysActionsHelperCustom, self).is_action_necessary(
            action, resource
        )
