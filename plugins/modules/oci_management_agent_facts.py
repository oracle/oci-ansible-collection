#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_management_agent_facts
short_description: Fetches details about one or multiple ManagementAgent resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagementAgent resources in Oracle Cloud Infrastructure
    - Returns a list of Management Agent.
    - If I(management_agent_id) is specified, the details of a single ManagementAgent will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    management_agent_id:
        description:
            - Unique Management Agent identifier
            - Required to get a specific management_agent.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment from which the Management Agents to be listed.
            - Required to list multiple management_agents.
        type: str
    plugin_name:
        description:
            - Filter to return only Management Agents having the particular Plugin installed.
        type: str
    version:
        description:
            - Filter to return only Management Agents having the particular agent version.
        type: str
    display_name:
        description:
            - Filter to return only Management Agents having the particular display name.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - Filter to return only Management Agents in the particular lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
            - "TERMINATED"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    platform_type:
        description:
            - Filter to return only Management Agents having the particular platform type.
        type: str
        choices:
            - "LINUX"
            - "WINDOWS"
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
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
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List management_agents
  oci_management_agent_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific management_agent
  oci_management_agent_facts:
    management_agent_id: ocid1.managementagent.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
management_agents:
    description:
        - List of ManagementAgent resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - agent identifier
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        install_key_id:
            description:
                - agent install key identifier
            returned: on success
            type: string
            sample: ocid1.installkey.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - Management Agent Name
            returned: on success
            type: string
            sample: display_name_example
        platform_type:
            description:
                - Platform Type
            returned: on success
            type: string
            sample: LINUX
        platform_name:
            description:
                - Platform Name
            returned: on success
            type: string
            sample: platform_name_example
        platform_version:
            description:
                - Platform Version
            returned: on success
            type: string
            sample: platform_version_example
        version:
            description:
                - Management Agent Version
            returned: on success
            type: string
            sample: version_example
        host:
            description:
                - Management Agent host machine name
            returned: on success
            type: string
            sample: host_example
        install_path:
            description:
                - Path where Management Agent is installed
            returned: on success
            type: string
            sample: install_path_example
        plugin_list:
            description:
                - list of managementAgentPlugins associated with the agent
            returned: on success
            type: complex
            contains:
                plugin_id:
                    description:
                        - Plugin Id
                    returned: on success
                    type: string
                    sample: ocid1.plugin.oc1..xxxxxxEXAMPLExxxxxx
                plugin_name:
                    description:
                        - Management Agent Plugin Name
                    returned: on success
                    type: string
                    sample: plugin_name_example
                plugin_display_name:
                    description:
                        - Management Agent Plugin Identifier, can be renamed
                    returned: on success
                    type: string
                    sample: plugin_display_name_example
                plugin_version:
                    description:
                        - Plugin Version
                    returned: on success
                    type: string
                    sample: plugin_version_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        is_agent_auto_upgradable:
            description:
                - true if the agent can be upgraded automatically; false if it must be upgraded manually. true is currently unsupported.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the Management Agent was created. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - The time the Management Agent was updated. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_last_heartbeat:
            description:
                - The time the Management Agent has last recorded its health status in telemetry. This value will be null if the agent has not recorded its
                  health status in last 7 days. An RFC3339 formatted datetime string
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of managementAgent
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
        "install_key_id": "ocid1.installkey.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "platform_type": "LINUX",
        "platform_name": "platform_name_example",
        "platform_version": "platform_version_example",
        "version": "version_example",
        "host": "host_example",
        "install_path": "install_path_example",
        "plugin_list": [{
            "plugin_id": "ocid1.plugin.oc1..xxxxxxEXAMPLExxxxxx",
            "plugin_name": "plugin_name_example",
            "plugin_display_name": "plugin_display_name_example",
            "plugin_version": "plugin_version_example"
        }],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "is_agent_auto_upgradable": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_heartbeat": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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


class ManagementAgentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "management_agent_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_agent,
            management_agent_id=self.module.params.get("management_agent_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "plugin_name",
            "version",
            "display_name",
            "lifecycle_state",
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
            self.client.list_management_agents,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ManagementAgentFactsHelperCustom = get_custom_class("ManagementAgentFactsHelperCustom")


class ResourceFactsHelper(
    ManagementAgentFactsHelperCustom, ManagementAgentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            management_agent_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            plugin_name=dict(type="str"),
            version=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
                    "TERMINATED",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            platform_type=dict(type="str", choices=["LINUX", "WINDOWS"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_agent",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_agents=result)


if __name__ == "__main__":
    main()
