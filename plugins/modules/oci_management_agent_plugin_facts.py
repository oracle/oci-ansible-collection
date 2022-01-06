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
module: oci_management_agent_plugin_facts
short_description: Fetches details about one or multiple ManagementAgentPlugin resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagementAgentPlugin resources in Oracle Cloud Infrastructure
    - Returns a list of managementAgentPlugins.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to which a request will be scoped.
        type: str
        required: true
    display_name:
        description:
            - Filter to return only Management Agent Plugins having the particular display name.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Default order for displayName is ascending. If no value is specified displayName is default.
        type: str
        choices:
            - "displayName"
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
            - Filter to return only results having the particular platform type.
        type: list
        elements: str
        choices:
            - "LINUX"
            - "WINDOWS"
            - "SOLARIS"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List management_agent_plugins
  oci_management_agent_plugin_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    sort_order: ASC
    sort_by: displayName
    lifecycle_state: CREATING
    platform_type: [ "LINUX" ]

"""

RETURN = """
management_agent_plugins:
    description:
        - List of ManagementAgentPlugin resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Management Agent Plugin Id
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Management Agent Plugin Name
            returned: on success
            type: str
            sample: name_example
        version:
            description:
                - Management Agent Plugin Version
            returned: on success
            type: int
            sample: 56
        supported_platform_types:
            description:
                - Supported Platform Types
            returned: on success
            type: list
            sample: []
        display_name:
            description:
                - Management Agent Plugin Display Name
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Management Agent Plugin description
            returned: on success
            type: str
            sample: description_example
        is_console_deployable:
            description:
                - A flag to indicate whether a given plugin can be deployed from Agent Console UI or not.
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The current state of Management Agent Plugin
            returned: on success
            type: str
            sample: CREATING
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "version": 56,
        "supported_platform_types": [],
        "display_name": "display_name_example",
        "description": "description_example",
        "is_console_deployable": true,
        "lifecycle_state": "CREATING"
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


class ManagementAgentPluginFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "sort_order",
            "sort_by",
            "lifecycle_state",
            "platform_type",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_management_agent_plugins,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ManagementAgentPluginFactsHelperCustom = get_custom_class(
    "ManagementAgentPluginFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagementAgentPluginFactsHelperCustom, ManagementAgentPluginFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            display_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["displayName"]),
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
            platform_type=dict(
                type="list", elements="str", choices=["LINUX", "WINDOWS", "SOLARIS"]
            ),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="management_agent_plugin",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(management_agent_plugins=result)


if __name__ == "__main__":
    main()
