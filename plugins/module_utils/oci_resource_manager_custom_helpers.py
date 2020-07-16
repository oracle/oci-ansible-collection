# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from base64 import b64encode


def get_base64_encoded_stack_tf_config(client, stack_id):
    response = oci_common_utils.call_with_backoff(
        client.get_stack_tf_config, stack_id=stack_id
    ).data
    return b64encode(response.content).decode("ascii")


class StackHelperCustom:
    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        existing_resource_dict = super(
            StackHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)
        if self.module.params.get(
            "key_by"
        ) and "config_source" not in self.module.params.get("key_by"):
            return existing_resource_dict
        if not (
            self.module.params.get("config_source")
            and self.module.params.get("config_source").get("config_source_type")
            == "ZIP_UPLOAD"
            and self.module.params.get("config_source").get("zip_file_base64_encoded")
        ):
            return existing_resource_dict
        if (
            existing_resource_dict.get("config_source")
            and existing_resource_dict.get("config_source").get("config_source_type")
            == "ZIP_UPLOAD"
        ):
            existing_resource_dict["config_source"][
                "zip_file_base64_encoded"
            ] = get_base64_encoded_stack_tf_config(
                self.client, existing_resource_dict.get("id")
            )
        return existing_resource_dict

    def get_existing_resource_dict_for_update(self):
        existing_resource_dict = super(
            StackHelperCustom, self
        ).get_existing_resource_dict_for_update()
        if (
            self.module.params.get("config_source")
            and self.module.params.get("config_source").get("zip_file_base64_encoded")
            and existing_resource_dict.get("config_source")
            and existing_resource_dict.get("config_source").get("config_source_type")
            == "ZIP_UPLOAD"
        ):
            existing_resource_dict["config_source"][
                "zip_file_base64_encoded"
            ] = get_base64_encoded_stack_tf_config(
                self.client, existing_resource_dict.get("id")
            )
        return existing_resource_dict


class JobHelperCustom:
    # Creating a job is not an idempotent operation. It might not be possible to determine if there were any changes
    # done to the stack itself (terraform config can be updated). So I don't think there is a reliable way for ansible
    # to determine if a job actually needs to run or not. Also it is perfectly valid to run some (for ex: plan) jobs
    # multiple times. I think it is safe to rely on terraform since it anyway performs actions based on changes and
    # try not to implement what terraform already does in ansible which might not be possible in most of the cases.
    def get_matching_resource(self):
        return None

    def is_resource_dead(self, resource):
        if resource.lifecycle_state == "CANCELED":
            return True

        return False
