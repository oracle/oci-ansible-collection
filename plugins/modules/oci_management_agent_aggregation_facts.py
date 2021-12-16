#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_management_agent_aggregation_facts
short_description: Fetches details about one or multiple ManagementAgentAggregation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagementAgentAggregation resources in Oracle Cloud Infrastructure
    - "Gets count of the inventory of agents for a given compartment id, group by, and isPluginDeployed parameters.
      Supported groupBy parameters: availabilityStatus, platformType, version"
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to which a request will be scoped.
        type: str
        required: true
    group_by:
        description:
            - The field by which to group Management Agents. Currently, only one groupBy dimension is supported at a time.
        type: list
        elements: str
        choices:
            - "availabilityStatus"
            - "platformType"
            - "version"
        required: true
    has_plugins:
        description:
            - When set to true then agents that have at least one plugin deployed will be returned. When set to false only agents that have no plugins deployed
              will be returned.
        type: bool
    install_type:
        description:
            - A filter to return either agents or gateway types depending upon install type selected by user. By default both install type will be returned.
        type: str
        choices:
            - "AGENT"
            - "GATEWAY"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List management_agent_aggregations
  oci_management_agent_aggregation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    group_by: [ "availabilityStatus" ]

    # optional
    has_plugins: true
    install_type: AGENT

"""

RETURN = """
management_agent_aggregations:
    description:
        - List of ManagementAgentAggregation resources
    returned: on success
    type: complex
    contains:
        dimensions:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                availability_status:
                    description:
                        - The availability status of managementAgent
                    returned: on success
                    type: str
                    sample: ACTIVE
                platform_type:
                    description:
                        - Platform Type
                    returned: on success
                    type: str
                    sample: LINUX
                version:
                    description:
                        - Agent image version
                    returned: on success
                    type: str
                    sample: version_example
                has_plugins:
                    description:
                        - Whether or not a managementAgent has at least one plugin
                    returned: on success
                    type: bool
                    sample: true
                install_type:
                    description:
                        - The install type, either AGENT or GATEWAY
                    returned: on success
                    type: str
                    sample: AGENT
        count:
            description:
                - The number of Management Agents in this group
            returned: on success
            type: int
            sample: 56
    sample: [{
        "dimensions": {
            "availability_status": "ACTIVE",
            "platform_type": "LINUX",
            "version": "version_example",
            "has_plugins": true,
            "install_type": "AGENT"
        },
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
    from oci.management_agent import ManagementAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementAgentAggregationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "group_by",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "has_plugins",
            "install_type",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_management_agent_counts,
            compartment_id=self.module.params.get("compartment_id"),
            group_by=self.module.params.get("group_by"),
            **optional_kwargs
        )


ManagementAgentAggregationFactsHelperCustom = get_custom_class(
    "ManagementAgentAggregationFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagementAgentAggregationFactsHelperCustom,
    ManagementAgentAggregationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            group_by=dict(
                type="list",
                elements="str",
                required=True,
                choices=["availabilityStatus", "platformType", "version"],
            ),
            has_plugins=dict(type="bool"),
            install_type=dict(type="str", choices=["AGENT", "GATEWAY"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_agent_aggregation",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_agent_aggregations=result)


if __name__ == "__main__":
    main()
