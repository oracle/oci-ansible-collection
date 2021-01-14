# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.resource_search.models import (
        FreeTextSearchDetails,
        StructuredSearchDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ResourceFactsHelperCustom:
    def is_list(self):
        return True

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        search_details = None
        if self.module.params["type"] == "FreeText":
            search_details = oci_common_utils.convert_input_data_to_model_class(
                self.module.params, FreeTextSearchDetails
            )
        else:
            search_details = oci_common_utils.convert_input_data_to_model_class(
                self.module.params, StructuredSearchDetails
            )
        return oci_common_utils.list_all_resources(
            self.client.search_resources,
            search_details=search_details,
            **optional_kwargs
        )
