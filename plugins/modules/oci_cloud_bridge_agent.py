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
module: oci_cloud_bridge_agent
short_description: Manage an Agent resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an Agent resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an Agent.
    - "This resource has the following action operations in the M(oracle.oci.oci_cloud_bridge_agent_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    agent_type:
        description:
            - Agent identifier.
            - Required for create using I(state=present).
        type: str
    agent_version:
        description:
            - Agent identifier.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - Compartment identifier.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    environment_id:
        description:
            - Environment identifier.
            - Required for create using I(state=present).
        type: str
    os_version:
        description:
            - OS version.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - Agent identifier.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    freeform_tags:
        description:
            - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
              predefined name, type, or namespace/scope. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Department\\": \\"Finance\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            - This parameter is updatable.
        type: dict
    agent_id:
        description:
            - Unique Agent identifier path parameter.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Agent.
            - Use I(state=present) to create or update an Agent.
            - Use I(state=absent) to delete an Agent.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create agent
  oci_cloud_bridge_agent:
    # required
    agent_type: agent_type_example
    agent_version: agent_version_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    environment_id: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
    os_version: os_version_example
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update agent
  oci_cloud_bridge_agent:
    # required
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update agent using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_bridge_agent:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete agent
  oci_cloud_bridge_agent:
    # required
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete agent using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_bridge_agent:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_bridge import OcbAgentSvcClient
    from oci.cloud_bridge.models import CreateAgentDetails
    from oci.cloud_bridge.models import UpdateAgentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AgentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AgentHelperGen, self).get_possible_entity_types() + [
            "ocbagent",
            "ocbagents",
            "cloudBridgeocbagent",
            "cloudBridgeocbagents",
            "ocbagentresource",
            "ocbagentsresource",
            "agent",
            "agents",
            "cloudBridgeagent",
            "cloudBridgeagents",
            "agentresource",
            "agentsresource",
            "cloudbridge",
        ]

    def get_module_resource_id_param(self):
        return "agent_id"

    def get_module_resource_id(self):
        return self.module.params.get("agent_id")

    def get_get_fn(self):
        return self.client.get_agent

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_agent, agent_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_agent, agent_id=self.module.params.get("agent_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["environment_id", "display_name", "agent_id"]

        return dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
            and (
                self._use_name_as_identifier()
                or (
                    not self.module.params.get("key_by")
                    or param in self.module.params.get("key_by")
                )
            )
        )

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(self.client.list_agents, **kwargs)

    def get_create_model_class(self):
        return CreateAgentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_agent,
            call_fn_args=(),
            call_fn_kwargs=dict(create_agent_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateAgentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_agent,
            call_fn_args=(),
            call_fn_kwargs=dict(
                agent_id=self.module.params.get("agent_id"),
                update_agent_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_agent,
            call_fn_args=(),
            call_fn_kwargs=dict(agent_id=self.module.params.get("agent_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AgentHelperCustom = get_custom_class("AgentHelperCustom")


class ResourceHelper(AgentHelperCustom, AgentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            agent_type=dict(type="str"),
            agent_version=dict(type="str"),
            compartment_id=dict(type="str"),
            environment_id=dict(type="str"),
            os_version=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            agent_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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

    result = dict(changed=False)

    if resource_helper.is_delete_using_name():
        result = resource_helper.delete_using_name()
    elif resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
