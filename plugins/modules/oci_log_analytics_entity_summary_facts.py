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
module: oci_log_analytics_entity_summary_facts
short_description: Fetches details about a LogAnalyticsEntitySummary resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a LogAnalyticsEntitySummary resource in Oracle Cloud Infrastructure
    - Returns log analytics entities count summary report.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific log_analytics_entity_summary
  oci_log_analytics_entity_summary_facts:
    # required
    namespace_name: namespace_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
log_analytics_entity_summary:
    description:
        - LogAnalyticsEntitySummary resource
    returned: on success
    type: complex
    contains:
        active_entities_count:
            description:
                - Total number of ACTIVE entities
            returned: on success
            type: int
            sample: 56
        entities_with_has_logs_collected_count:
            description:
                - Entities with log collection enabled
            returned: on success
            type: int
            sample: 56
        entities_with_management_agent_count:
            description:
                - Entities with management agent
            returned: on success
            type: int
            sample: 56
        compartment_id:
            description:
                - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "active_entities_count": 56,
        "entities_with_has_logs_collected_count": 56,
        "entities_with_management_agent_count": 56,
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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


class LogAnalyticsEntitySummaryFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_entities_summary,
            namespace_name=self.module.params.get("namespace_name"),
            compartment_id=self.module.params.get("compartment_id"),
        )


LogAnalyticsEntitySummaryFactsHelperCustom = get_custom_class(
    "LogAnalyticsEntitySummaryFactsHelperCustom"
)


class ResourceFactsHelper(
    LogAnalyticsEntitySummaryFactsHelperCustom, LogAnalyticsEntitySummaryFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            namespace_name=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_analytics_entity_summary",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_analytics_entity_summary=result)


if __name__ == "__main__":
    main()
