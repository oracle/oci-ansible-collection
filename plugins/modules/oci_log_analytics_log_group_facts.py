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
module: oci_log_analytics_log_group_facts
short_description: Fetches details about one or multiple LogAnalyticsLogGroup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LogAnalyticsLogGroup resources in Oracle Cloud Infrastructure
    - Returns a list of log groups in a compartment. You may limit the number of log groups, provide sorting options, and filter the results by specifying a
      display name.
    - If I(log_analytics_log_group_id) is specified, the details of a single LogAnalyticsLogGroup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    log_analytics_log_group_id:
        description:
            - unique logAnalytics log group identifier
            - Required to get a specific log_analytics_log_group.
        type: str
        aliases: ["id"]
    namespace_name:
        description:
            - The Logging Analytics namespace used for the request.
        type: str
        required: true
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple log_analytics_log_groups.
        type: str
    display_name:
        description:
            - A filter to return only log analytics log groups whose displayName matches the entire display name given.
              The match is case-insensitive.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending. If no value is specified timeCreated is default.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific log_analytics_log_group
  oci_log_analytics_log_group_facts:
    # required
    log_analytics_log_group_id: "ocid1.loganalyticsloggroup.oc1..xxxxxxEXAMPLExxxxxx"
    namespace_name: namespace_name_example

- name: List log_analytics_log_groups
  oci_log_analytics_log_group_facts:
    # required
    namespace_name: namespace_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
log_analytics_log_groups:
    description:
        - List of LogAnalyticsLogGroup resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The log analytics entity OCID. This ID is a reference used by log analytics features and it represents
                  a resource that is provisioned and managed by the customer on their premises or on the cloud.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - "A user-friendly name that is changeable and that does not have to be unique.
                  Format: a leading alphanumeric, followed by zero or more
                  alphanumerics, underscores, spaces, backslashes, or hyphens in any order).
                  No trailing spaces allowed."
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description for this resource.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - Compartment Identifier L(OCID],https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the resource was created, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The date and time the resource was last updated, in the format defined by RFC3339.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
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


class LogAnalyticsLogGroupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "namespace_name",
            "log_analytics_log_group_id",
        ]

    def get_required_params_for_list(self):
        return [
            "namespace_name",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_log_analytics_log_group,
            namespace_name=self.module.params.get("namespace_name"),
            log_analytics_log_group_id=self.module.params.get(
                "log_analytics_log_group_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_log_analytics_log_groups,
            namespace_name=self.module.params.get("namespace_name"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LogAnalyticsLogGroupFactsHelperCustom = get_custom_class(
    "LogAnalyticsLogGroupFactsHelperCustom"
)


class ResourceFactsHelper(
    LogAnalyticsLogGroupFactsHelperCustom, LogAnalyticsLogGroupFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            log_analytics_log_group_id=dict(aliases=["id"], type="str"),
            namespace_name=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeCreated", "timeUpdated", "displayName"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="log_analytics_log_group",
        service_client_class=LogAnalyticsClient,
        namespace="log_analytics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(log_analytics_log_groups=result)


if __name__ == "__main__":
    main()
