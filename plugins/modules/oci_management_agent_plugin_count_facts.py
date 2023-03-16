#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_management_agent_plugin_count_facts
short_description: Fetches details about one or multiple ManagementAgentPluginCount resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagementAgentPluginCount resources in Oracle Cloud Infrastructure
    - "Gets count of the inventory of management agent plugins for a given compartment id and group by parameter.
      Supported groupBy parameter: pluginName"
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
            - The field by which to group Management Agent Plugins
        type: str
        choices:
            - "pluginName"
        required: true
    compartment_id_in_subtree:
        description:
            - if set to true then it fetches resources for all compartments where user has access to else only on the compartment specified.
        type: bool
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List management_agent_plugin_counts
  oci_management_agent_plugin_count_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    group_by: pluginName

    # optional
    compartment_id_in_subtree: true

"""

RETURN = """
management_agent_plugin_counts:
    description:
        - List of ManagementAgentPluginCount resources
    returned: on success
    type: complex
    contains:
        dimensions:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                plugin_name:
                    description:
                        - Management Agent Plugin Name
                    returned: on success
                    type: str
                    sample: plugin_name_example
                plugin_display_name:
                    description:
                        - Management Agent Plugin Display Name
                    returned: on success
                    type: str
                    sample: plugin_display_name_example
        count:
            description:
                - The number of Management Agent Plugins in this group
            returned: on success
            type: int
            sample: 56
    sample: [{
        "dimensions": {
            "plugin_name": "plugin_name_example",
            "plugin_display_name": "plugin_display_name_example"
        },
        "count": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.management_agent import ManagementAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementAgentPluginCountFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "group_by",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id_in_subtree",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.summarize_management_agent_plugin_counts,
            compartment_id=self.module.params.get("compartment_id"),
            group_by=self.module.params.get("group_by"),
            **optional_kwargs
        )


ManagementAgentPluginCountFactsHelperCustom = get_custom_class(
    "ManagementAgentPluginCountFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagementAgentPluginCountFactsHelperCustom,
    ManagementAgentPluginCountFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            group_by=dict(type="str", required=True, choices=["pluginName"]),
            compartment_id_in_subtree=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_agent_plugin_count",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_agent_plugin_counts=result)


if __name__ == "__main__":
    main()
