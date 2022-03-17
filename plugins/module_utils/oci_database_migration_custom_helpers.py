# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

logger = oci_common_utils.get_logger("oci_announcements_service_custom_helpers")


class MigrationHelperCustom:
    def get_create_model_dict_for_idempotence_check(self, create_model):
        create_model_dict = super(
            MigrationHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(create_model)
        # there is no property admin_credentials in the top level properties. this is wrong
        if create_model_dict.get("admin_credentials") is not None:
            create_model_dict["admin_credentials"].pop("password", None)
        return create_model_dict
