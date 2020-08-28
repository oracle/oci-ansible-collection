# Copyright (c) 2020 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    from oci.usage_api.models import RequestSummarizedUsagesDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UsageFactsHelperCustom:
    def is_list(self):
        return True

    def list_resources(self):
        request_summarized_usages_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RequestSummarizedUsagesDetails
        )
        return oci_common_utils.list_all_resources(
            self.client.request_summarized_usages,
            request_summarized_usages_details=request_summarized_usages_details,
        )
