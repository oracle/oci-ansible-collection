# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ConnectionHelperCustom:
    # API throws an error when we pass connection_type value.
    def get_optional_kwargs_for_list(self):
        optional_list_method_params = super(
            ConnectionHelperCustom, self
        ).get_optional_kwargs_for_list()
        optional_list_method_params.pop("connection_type", None)
        return optional_list_method_params


class BuildRunHelperCustom:
    # Running a build is not an idempotent operation. It is perfectly valid
    # to run the build multiple times.
    def get_matching_resource(self):
        return None
