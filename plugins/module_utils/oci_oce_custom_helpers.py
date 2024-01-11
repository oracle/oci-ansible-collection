# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class OceInstanceHelperCustom:
    # NEW license type can still be passed for backward compatibility,
    # but NEW license type is same as PREMIUM license type.
    # API returns PREMIUM license type even if NEW license type is set.
    def get_create_model_dict_for_idempotence_check(self, existing_resource):
        create_model_dict = super(
            OceInstanceHelperCustom, self
        ).get_create_model_dict_for_idempotence_check(existing_resource)
        if (
            create_model_dict.get("instance_license_type") is not None
            and create_model_dict.get("instance_license_type") == "NEW"
        ):
            create_model_dict["instance_license_type"] = "PREMIUM"
        return create_model_dict
