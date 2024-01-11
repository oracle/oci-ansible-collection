# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils

try:
    import oci
    from oci.loggingsearch.models import (
        SearchLogsDetails,
        SearchResponse,
        SearchResultSummary,
    )

    HAS_OCI_PY_SDK = True

except ImportError:
    HAS_OCI_PY_SDK = False


class SearchFactsHelperCustom:
    # generated `list_resources` uses pagination supported by Python SDK.
    # Pagination supported by Python SDK checks for attribute `items` from response.
    # And response doesn't contain `items` attribute. Thus operation `SearchLogs` requires custom pagination.
    # function `list_call_get_all_results_generator` lazily loads results (either all results, or up to a given limit).
    def list_resources(self):
        results = []
        fields = []
        result_count = 0
        field_count = 0
        search_logs_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SearchLogsDetails
        )
        for response in oci.pagination.list_call_get_all_results_generator(
            self.client.search_logs, "response", search_logs_details
        ):
            if response.data.results is not None:
                results.extend(response.data.results)
            if response.data.fields is not None:
                fields.extend(response.data.fields)
            if response.data.summary.result_count is not None:
                result_count += response.data.summary.result_count
            if response.data.summary.field_count is not None:
                field_count += response.data.summary.field_count

        search_response = SearchResponse()
        search_response.results = results
        search_response.fields = fields

        search_result_summary = SearchResultSummary()
        search_result_summary.result_count = result_count
        search_result_summary.field_count = field_count

        search_response.summary = search_result_summary
        return search_response
