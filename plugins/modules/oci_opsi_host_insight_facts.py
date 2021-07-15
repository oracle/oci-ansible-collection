#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_opsi_host_insight_facts
short_description: Fetches details about one or multiple HostInsight resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HostInsight resources in Oracle Cloud Infrastructure
    - Gets a list of host insights based on the query parameters specified. Either compartmentId or id query parameter must be specified.
    - If I(host_insight_id) is specified, the details of a single HostInsight will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    host_insight_id:
        description:
            - Unique host insight identifier
            - Required to get a specific host_insight.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
    status:
        description:
            - Resource Status
        type: list
        choices:
            - "DISABLED"
            - "ENABLED"
            - "TERMINATED"
    lifecycle_state:
        description:
            - Lifecycle states
        type: list
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
            - "NEEDS_ATTENTION"
    host_type:
        description:
            - Filter by one or more host types.
              Possible value is EXTERNAL-HOST.
        type: list
    platform_type:
        description:
            - Filter by one or more platform types.
              Possible value is LINUX.
        type: list
        choices:
            - "LINUX"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Host insight list sort options. If `fields` parameter is selected, the `sortBy` parameter must be one of the fields specified.
        type: str
        choices:
            - "hostName"
            - "hostType"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List host_insights
  oci_opsi_host_insight_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific host_insight
  oci_opsi_host_insight_facts:
    host_insight_id: "ocid1.hostinsight.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
host_insights:
    description:
        - List of HostInsight resources
    returned: on success
    type: complex
    contains:
        entity_source:
            description:
                - Source of the host entity.
            returned: on success
            type: string
            sample: MACS_MANAGED_EXTERNAL_HOST
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the host insight resource.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        host_name:
            description:
                - The host name. The host name is unique amongst the hosts managed by the same management agent.
            returned: on success
            type: string
            sample: host_name_example
        host_display_name:
            description:
                - The user-friendly name for the host. The name does not have to be unique.
            returned: on success
            type: string
            sample: host_display_name_example
        host_type:
            description:
                - Operations Insights internal representation of the host type. Possible value is EXTERNAL-HOST.
            returned: on success
            type: string
            sample: host_type_example
        processor_count:
            description:
                - Processor count. This is the OCPU count for Autonomous Database and CPU core count for other database types.
            returned: on success
            type: int
            sample: 56
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
                - Indicates the status of a host insight in Operations Insights
            returned: on success
            type: string
            sample: ENABLED
        time_created:
            description:
                - The time the the host insight was first enabled. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the host insight was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the host.
            returned: on success
            type: string
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: string
            sample: lifecycle_details_example
        management_agent_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the Management Agent
            returned: on success
            type: string
            sample: "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx"
        platform_name:
            description:
                - Platform name.
            returned: on success
            type: string
            sample: platform_name_example
        platform_type:
            description:
                - Platform type.
            returned: on success
            type: string
            sample: LINUX
        platform_version:
            description:
                - Platform version.
            returned: on success
            type: string
            sample: platform_version_example
    sample: [{
        "entity_source": "MACS_MANAGED_EXTERNAL_HOST",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "host_name": "host_name_example",
        "host_display_name": "host_display_name_example",
        "host_type": "host_type_example",
        "processor_count": 56,
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "status": "ENABLED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "management_agent_id": "ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx",
        "platform_name": "platform_name_example",
        "platform_type": "LINUX",
        "platform_version": "platform_version_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.opsi import OperationsInsightsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HostInsightFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "host_insight_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_host_insight,
            host_insight_id=self.module.params.get("host_insight_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "status",
            "lifecycle_state",
            "host_type",
            "platform_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_host_insights, **optional_kwargs
        )


HostInsightFactsHelperCustom = get_custom_class("HostInsightFactsHelperCustom")


class ResourceFactsHelper(HostInsightFactsHelperCustom, HostInsightFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            host_insight_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            status=dict(type="list", choices=["DISABLED", "ENABLED", "TERMINATED"]),
            lifecycle_state=dict(
                type="list",
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
            host_type=dict(type="list"),
            platform_type=dict(type="list", choices=["LINUX"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["hostName", "hostType"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="host_insight",
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

    module.exit_json(host_insights=result)


if __name__ == "__main__":
    main()
