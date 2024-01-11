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
module: oci_log_analytics_lookup_summary_report_facts
short_description: Fetches details about a LookupSummaryReport resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a LookupSummaryReport resource in Oracle Cloud Infrastructure
    - Returns the count of user created and oracle defined lookups.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific lookup_summary_report
  oci_log_analytics_lookup_summary_report_facts:
    # required
    namespace_name: namespace_name_example

"""

RETURN = """
lookup_summary_report:
    description:
        - LookupSummaryReport resource
    returned: on success
    type: complex
    contains:
        user_created_count:
            description:
                - The number of user created lookups.
            returned: on success
            type: int
            sample: 56
        oracle_defined_count:
            description:
                - The number of oracle defined lookups.
            returned: on success
            type: int
            sample: 56
        total_count:
            description:
                - The total number of lookups.
            returned: on success
            type: int
            sample: 56
    sample: {
        "user_created_count": 56,
        "oracle_defined_count": 56,
        "total_count": 56
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.log_analytics import LogAnalyticsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LookupSummaryReportFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lookup_summary,
            namespace_name=self.module.params.get("namespace_name"),
        )


LookupSummaryReportFactsHelperCustom = get_custom_class(
    "LookupSummaryReportFactsHelperCustom"
)


class ResourceFactsHelper(
    LookupSummaryReportFactsHelperCustom, LookupSummaryReportFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(namespace_name=dict(type="str", required=True),))

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="lookup_summary_report",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(lookup_summary_report=result)


if __name__ == "__main__":
    main()
