# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible.module_utils._text import to_text


class KubeconfigHelperCustom:
    def create_resource(self):
        response_data = super(KubeconfigHelperCustom, self).create_resource()
        return to_text(response_data.content)


class NodePoolHelperCustom:
    # Some attrs end with details and the get returns the same field without details
    # This case we should still match them for update and create
    def get_existing_resource_dict_for_idempotence_check(self, existing_resource):
        existing_resource_dict = super(
            NodePoolHelperCustom, self
        ).get_existing_resource_dict_for_idempotence_check(existing_resource)
        if existing_resource_dict.get("node_source"):
            existing_resource_dict["node_source_details"] = existing_resource_dict.pop(
                "node_source"
            )
        return existing_resource_dict

    def is_update_necessary(self, existing_resource_dict):
        if existing_resource_dict.get("node_source"):
            existing_resource_dict["node_source_details"] = existing_resource_dict.get(
                "node_source"
            )
        return super(NodePoolHelperCustom, self).is_update_necessary(
            existing_resource_dict
        )
