#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_database_management_attention_log_counts_facts
short_description: Fetches details about one or multiple AttentionLogCounts resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AttentionLogCounts resources in Oracle Cloud Infrastructure
    - Get the counts of attention logs for the specified Managed Database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        required: true
    time_greater_than_or_equal_to:
        description:
            - The optional greater than or equal to timestamp to filter the logs.
        type: str
    time_less_than_or_equal_to:
        description:
            - The optional less than or equal to timestamp to filter the logs.
        type: str
    urgency_filter:
        description:
            - The optional parameter to filter the attention logs by urgency.
        type: str
        choices:
            - "IMMEDIATE"
            - "SOON"
            - "DEFERRABLE"
            - "INFO"
            - "ALL"
    group_by:
        description:
            - The optional parameter used to group different attention logs.
        type: str
        choices:
            - "URGENCY"
            - "TYPE"
    type_filter:
        description:
            - The optional parameter to filter the attention or alert logs by type.
        type: str
        choices:
            - "UNKNOWN"
            - "INCIDENT_ERROR"
            - "ERROR"
            - "WARNING"
            - "NOTIFICATION"
            - "TRACE"
            - "ALL"
    log_search_text:
        description:
            - The optional query parameter to filter the attention or alert logs by search text.
        type: str
    is_regular_expression:
        description:
            - The flag to indicate whether the search text is regular expression or not.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List attention_log_counts
  oci_database_management_attention_log_counts_facts:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_less_than_or_equal_to: 2013-10-20T19:20:30+01:00
    urgency_filter: IMMEDIATE
    group_by: URGENCY
    type_filter: UNKNOWN
    log_search_text: log_search_text_example
    is_regular_expression: true

"""

RETURN = """
attention_log_counts:
    description:
        - List of AttentionLogCounts resources
    returned: on success
    type: complex
    contains:
        category:
            description:
                - The category of different attention logs.
            returned: on success
            type: str
            sample: UNKNOWN
        count:
            description:
                - The count of attention logs with specific category.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "category": "UNKNOWN",
        "count": 56
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DiagnosabilityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AttentionLogCountsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_database_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_greater_than_or_equal_to",
            "time_less_than_or_equal_to",
            "urgency_filter",
            "group_by",
            "type_filter",
            "log_search_text",
            "is_regular_expression",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_attention_log_counts,
            managed_database_id=self.module.params.get("managed_database_id"),
            **optional_kwargs
        )


AttentionLogCountsFactsHelperCustom = get_custom_class(
    "AttentionLogCountsFactsHelperCustom"
)


class ResourceFactsHelper(
    AttentionLogCountsFactsHelperCustom, AttentionLogCountsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_database_id=dict(type="str", required=True),
            time_greater_than_or_equal_to=dict(type="str"),
            time_less_than_or_equal_to=dict(type="str"),
            urgency_filter=dict(
                type="str", choices=["IMMEDIATE", "SOON", "DEFERRABLE", "INFO", "ALL"]
            ),
            group_by=dict(type="str", choices=["URGENCY", "TYPE"]),
            type_filter=dict(
                type="str",
                choices=[
                    "UNKNOWN",
                    "INCIDENT_ERROR",
                    "ERROR",
                    "WARNING",
                    "NOTIFICATION",
                    "TRACE",
                    "ALL",
                ],
            ),
            log_search_text=dict(type="str"),
            is_regular_expression=dict(type="bool"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="attention_log_counts",
        service_client_class=DiagnosabilityClient,
        namespace="database_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(attention_log_counts=result)


if __name__ == "__main__":
    main()
