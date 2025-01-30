#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_opsi_news_reports_facts
short_description: Fetches details about one or multiple NewsReports resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple NewsReports resources in Oracle Cloud Infrastructure
    - Gets a list of news reports based on the query parameters specified. Either compartmentId or id query parameter must be specified.
    - If I(news_report_id) is specified, the details of a single NewsReports will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    news_report_id:
        description:
            - Unique news report identifier.
            - Required to get a specific news_reports.
        type: str
        aliases: ["id"]
    status:
        description:
            - Resource Status
        type: list
        elements: str
        choices:
            - "DISABLED"
            - "ENABLED"
            - "TERMINATED"
    lifecycle_state:
        description:
            - Lifecycle states
        type: list
        elements: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "NEEDS_ATTENTION"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - News report list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.
        type: str
        choices:
            - "name"
            - "newsFrequency"
    compartment_id_in_subtree:
        description:
            - A flag to search all resources within a given compartment and all sub-compartments.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: Get a specific news_reports
  oci_opsi_news_reports_facts:
    # required
    news_report_id: "ocid1.newsreport.oc1..xxxxxxEXAMPLExxxxxx"

- name: List news_reports
  oci_opsi_news_reports_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    news_report_id: "ocid1.newsreport.oc1..xxxxxxEXAMPLExxxxxx"
    status: [ "DISABLED" ]
    lifecycle_state: [ "CREATING" ]
    sort_order: ASC
    sort_by: name
    compartment_id_in_subtree: true

"""

RETURN = """
news_reports:
    description:
        - List of NewsReports resources
    returned: on success
    type: complex
    contains:
        news_frequency:
            description:
                - News report frequency.
            returned: on success
            type: str
            sample: WEEKLY
        content_types:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                capacity_planning_resources:
                    description:
                        - Supported resources for capacity planning content type.
                    returned: on success
                    type: list
                    sample: []
        locale:
            description:
                - Language of the news report.
            returned: on success
            type: str
            sample: EN
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the news report resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - The description of the news report.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The news report name.
            returned: on success
            type: str
            sample: name_example
        ons_topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the ONS topic.
            returned: on success
            type: str
            sample: "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        status:
            description:
                - Indicates the status of a news report in Operations Insights.
            returned: on success
            type: str
            sample: DISABLED
        time_created:
            description:
                - The time the the news report was first enabled. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the news report was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the news report.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
    sample: [{
        "news_frequency": "WEEKLY",
        "content_types": {
            "capacity_planning_resources": []
        },
        "locale": "EN",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "ons_topic_id": "ocid1.onstopic.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "status": "DISABLED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class NewsReportsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "news_report_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_news_report,
            news_report_id=self.module.params.get("news_report_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "news_report_id",
            "status",
            "lifecycle_state",
            "sort_order",
            "sort_by",
            "compartment_id_in_subtree",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_news_reports, **optional_kwargs
        )


NewsReportsFactsHelperCustom = get_custom_class("NewsReportsFactsHelperCustom")


class ResourceFactsHelper(NewsReportsFactsHelperCustom, NewsReportsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            news_report_id=dict(aliases=["id"], type="str"),
            status=dict(
                type="list",
                elements="str",
                choices=["DISABLED", "ENABLED", "TERMINATED"],
            ),
            lifecycle_state=dict(
                type="list",
                elements="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                    "NEEDS_ATTENTION",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name", "newsFrequency"]),
            compartment_id_in_subtree=dict(type="bool"),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="news_reports",
        service_client_class=OperationsInsightsClient,
        namespace="opsi",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(news_reports=result)


if __name__ == "__main__":
    main()
