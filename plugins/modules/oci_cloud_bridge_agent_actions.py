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
module: oci_cloud_bridge_agent_actions
short_description: Perform actions on an Agent resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Agent resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an Agent resource from one compartment identifier to another. When provided, If-Match is checked against ETag
      values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    agent_id:
        description:
            - Unique Agent identifier path parameter.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Agent.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on agent
  oci_cloud_bridge_agent_actions:
    # required
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
agent:
    description:
        - Details of the Agent resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Agent identifier, can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        agent_type:
            description:
                - Type of the Agent.
            returned: on success
            type: str
            sample: APPLIANCE
        agent_version:
            description:
                - Agent identifier.
            returned: on success
            type: str
            sample: agent_version_example
        os_version:
            description:
                - OS version.
            returned: on success
            type: str
            sample: os_version_example
        time_created:
            description:
                - The time when the Agent was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the Agent was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_sync_received:
            description:
                - The time when the last heartbeat of the Agent was noted. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        heart_beat_status:
            description:
                - The current heartbeat status of the Agent based on its timeLastSyncReceived value.
            returned: on success
            type: str
            sample: HEALTHY
        environment_id:
            description:
                - Environment identifier.
            returned: on success
            type: str
            sample: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
        agent_pub_key:
            description:
                - Resource principal public key.
            returned: on success
            type: str
            sample: agent_pub_key_example
        time_expire_agent_key_in_ms:
            description:
                - The time since epoch for when the public key will expire. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Agent.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state of the Agent in more detail. For example, it can be used to provide actionable information for a
                  resource in Failed state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        plugin_list:
            description:
                - List of plugins associated with the agent.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Plugin identifier, which can be renamed.
                    returned: on success
                    type: str
                    sample: name_example
                agent_id:
                    description:
                        - Agent identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
                plugin_version:
                    description:
                        - Plugin version.
                    returned: on success
                    type: str
                    sample: plugin_version_example
                time_created:
                    description:
                        - The time when the plugin was created. An RFC3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_updated:
                    description:
                        - The time when the plugin was updated. An RFC3339 formatted datetime string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                lifecycle_state:
                    description:
                        - The current state of the plugin.
                    returned: on success
                    type: str
                    sample: lifecycle_state_example
                lifecycle_details:
                    description:
                        - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in
                          Failed state.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
                freeform_tags:
                    description:
                        - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                          predefined name, type, or namespace/scope. For more information, see L(Resource
                          Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Department\\": \\"Finance\\"}`"
                    returned: on success
                    type: dict
                    sample: {'Department': 'Finance'}
                defined_tags:
                    description:
                        - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                          For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                          Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                    returned: on success
                    type: dict
                    sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace/scope. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "agent_type": "APPLIANCE",
        "agent_version": "agent_version_example",
        "os_version": "os_version_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "time_last_sync_received": "2013-10-20T19:20:30+01:00",
        "heart_beat_status": "HEALTHY",
        "environment_id": "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx",
        "agent_pub_key": "agent_pub_key_example",
        "time_expire_agent_key_in_ms": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "plugin_list": [{
            "name": "name_example",
            "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
            "plugin_version": "plugin_version_example",
            "time_created": "2013-10-20T19:20:30+01:00",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "lifecycle_state": "lifecycle_state_example",
            "lifecycle_details": "lifecycle_details_example",
            "freeform_tags": {'Department': 'Finance'},
            "defined_tags": {'Operations': {'CostCenter': 'US'}}
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.cloud_bridge import OcbAgentSvcClient
    from oci.cloud_bridge.models import ChangeAgentCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AgentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "agent_id"

    def get_module_resource_id(self):
        return self.module.params.get("agent_id")

    def get_get_fn(self):
        return self.client.get_agent

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_agent, agent_id=self.module.params.get("agent_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAgentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_agent_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                agent_id=self.module.params.get("agent_id"),
                change_agent_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AgentActionsHelperCustom = get_custom_class("AgentActionsHelperCustom")


class ResourceHelper(AgentActionsHelperCustom, AgentActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            agent_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="agent",
        service_client_class=OcbAgentSvcClient,
        namespace="cloud_bridge",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
