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
module: oci_management_agent_actions
short_description: Perform actions on a ManagementAgent resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagementAgent resource in Oracle Cloud Infrastructure
    - For I(action=deploy_plugins), deploys Plugins to a given list of agentIds.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    plugin_ids:
        description:
            - Plugin Id
        type: list
        elements: str
        required: true
    agent_compartment_id:
        description:
            - Management Agent Compartment Identifier
        type: str
        required: true
    agent_ids:
        description:
            - List of Agent identifiers
        type: list
        elements: str
        required: true
    action:
        description:
            - The action to perform on the ManagementAgent.
        type: str
        required: true
        choices:
            - "deploy_plugins"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action deploy_plugins on management_agent
  oci_management_agent_actions:
    agent_compartment_id: "ocid1.agentcompartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: deploy_plugins

"""


from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.management_agent import ManagementAgentClient
    from oci.management_agent.models import DeployPluginsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagementAgentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        deploy_plugins
    """

    def get_get_fn(self):
        return self.client.get_management_agent

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_agent,
            management_agent_id=self.module.params.get("management_agent_id"),
        )

    def deploy_plugins(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, DeployPluginsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.deploy_plugins,
            call_fn_args=(),
            call_fn_kwargs=dict(deploy_plugins_details=action_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


ManagementAgentActionsHelperCustom = get_custom_class(
    "ManagementAgentActionsHelperCustom"
)


class ResourceHelper(
    ManagementAgentActionsHelperCustom, ManagementAgentActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            plugin_ids=dict(type="list", elements="str", required=True),
            agent_compartment_id=dict(type="str", required=True),
            agent_ids=dict(type="list", elements="str", required=True),
            action=dict(type="str", required=True, choices=["deploy_plugins"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_agent",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
