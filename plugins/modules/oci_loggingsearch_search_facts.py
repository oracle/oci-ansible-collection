#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.
# GENERATED FILE - DO NOT EDIT - MANUAL CHANGES WILL BE OVERWRITTEN


from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_loggingsearch_search_facts
short_description: Fetches details about one or multiple Search resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Search resources in Oracle Cloud Infrastructure
    - Submit a query to search logs.
    - See L(Using the API,https://docs.cloud.oracle.com/Content/Logging/Concepts/using_the_api_searchlogs.htm) for SDK examples.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    time_start:
        description:
            - Start filter log's date and time, in the format defined by RFC3339.
        type: str
        required: true
    time_end:
        description:
            - End filter log's date and time, in the format defined by RFC3339.
        type: str
        required: true
    search_query:
        description:
            - Query corresponding to the search operation. This query is parsed and validated before execution and
              should follow the specification. For more information on the query language specification, see
              L(Logging Query Language Specification,https://docs.cloud.oracle.com/Content/Logging/Reference/query_language_specification.htm).
        type: str
        required: true
    is_return_field_info:
        description:
            - Whether to return field schema information for the log stream specified in searchQuery.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List searches
  oci_loggingsearch_search_facts:
    # required
    time_start: time_start_example
    time_end: time_end_example
    search_query: search_query_example

    # optional
    is_return_field_info: true

"""

RETURN = """
searches:
    description:
        - List of Search resources
    returned: on success
    type: complex
    contains:
        results:
            description:
                - List of search results
            returned: on success
            type: complex
            contains:
                data:
                    description:
                        - JSON blob containing the search entry with the projected fields.
                    returned: on success
                    type: dict
                    sample: {}
        fields:
            description:
                - List of log field schema information.
            returned: on success
            type: complex
            contains:
                field_name:
                    description:
                        - Field name
                    returned: on success
                    type: str
                    sample: field_name_example
                field_type:
                    description:
                        - "Field type -
                          * `STRING`: A sequence of characters.
                          * `NUMBER`: Numeric type which can be an integer or floating point.
                          * `BOOLEAN`: Either true or false.
                          * `ARRAY`: An ordered collection of values."
                    returned: on success
                    type: str
                    sample: STRING
        summary:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                result_count:
                    description:
                        - Total number of search results.
                    returned: on success
                    type: int
                    sample: 56
                field_count:
                    description:
                        - Total number of field schema information.
                    returned: on success
                    type: int
                    sample: 56
    sample: [{
        "results": [{
            "data": {}
        }],
        "fields": [{
            "field_name": "field_name_example",
            "field_type": "STRING"
        }],
        "summary": {
            "result_count": 56,
            "field_count": 56
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.loggingsearch import LogSearchClient
    from oci.loggingsearch.models import SearchLogsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SearchFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "time_start",
            "time_end",
            "search_query",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.search_logs,
            search_logs_details=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, SearchLogsDetails
            ),
            **optional_kwargs
        )


SearchFactsHelperCustom = get_custom_class("SearchFactsHelperCustom")


class ResourceFactsHelper(SearchFactsHelperCustom, SearchFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            time_start=dict(type="str", required=True),
            time_end=dict(type="str", required=True),
            search_query=dict(type="str", required=True),
            is_return_field_info=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="search",
        service_client_class=LogSearchClient,
        namespace="loggingsearch",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(searches=result)


if __name__ == "__main__":
    main()
