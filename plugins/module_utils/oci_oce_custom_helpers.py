# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

logger = oci_common_utils.get_logger("oci_oce_custom_helpers")


def _debug(s):
    get_logger().debug(s)


def get_logger():
    return logger


class OceInstanceHelperCustom:
    # exclude the attributes from the create model which are not present in the get model for idempotency check
    def get_exclude_attributes(self):
        exclude_attributes = super(
            OceInstanceHelperCustom, self
        ).get_exclude_attributes()
        return exclude_attributes + [
            "idcs_access_token",
        ]
