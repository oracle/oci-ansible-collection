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
module: oci_cloud_bridge_agent_dependency
short_description: Manage an AgentDependency resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an AgentDependency resource in Oracle Cloud Infrastructure
    - For I(state=present), creates an AgentDependency.
    - "This resource has the following action operations in the M(oracle.oci.oci_cloud_bridge_agent_dependency_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment identifier.
            - Required for create using I(state=present).
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - Required for delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    display_name:
        description:
            - Display name of the Agent dependency.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    dependency_name:
        description:
            - Name of the dependency type. This should match the whitelisted enum of dependency names.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    dependency_version:
        description:
            - Version of the Agent dependency.
            - This parameter is updatable.
        type: str
    description:
        description:
            - Description about the Agent dependency.
            - This parameter is updatable.
        type: str
    namespace:
        description:
            - Object storage namespace associated with the customer's tenancy.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    bucket:
        description:
            - Object storage bucket where the dependency is uploaded.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
    object_name:
        description:
            - Name of the dependency object uploaded by the customer.
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: str
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
    system_tags:
        description:
            - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is predefined
              and scoped to namespaces.
              For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
              Example: `{orcl-cloud: {free-tier-retain: true}}`"
            - This parameter is updatable.
        type: dict
    agent_dependency_id:
        description:
            - A unique AgentDependency identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the AgentDependency.
            - Use I(state=present) to create or update an AgentDependency.
            - Use I(state=absent) to delete an AgentDependency.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create agent_dependency
  oci_cloud_bridge_agent_dependency:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    dependency_name: dependency_name_example
    namespace: namespace_example
    bucket: bucket_example
    object_name: object_name_example

    # optional
    dependency_version: dependency_version_example
    description: description_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update agent_dependency
  oci_cloud_bridge_agent_dependency:
    # required
    agent_dependency_id: "ocid1.agentdependency.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    dependency_name: dependency_name_example
    dependency_version: dependency_version_example
    description: description_example
    namespace: namespace_example
    bucket: bucket_example
    object_name: object_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Update agent_dependency using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_bridge_agent_dependency:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    dependency_name: dependency_name_example
    dependency_version: dependency_version_example
    description: description_example
    namespace: namespace_example
    bucket: bucket_example
    object_name: object_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    system_tags: null

- name: Delete agent_dependency
  oci_cloud_bridge_agent_dependency:
    # required
    agent_dependency_id: "ocid1.agentdependency.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete agent_dependency using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_cloud_bridge_agent_dependency:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    state: absent

"""

RETURN = """
agent_dependency:
    description:
        - Details of the AgentDependency resource acted upon by the current operation
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
                - Display name of the Agent dependency.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        dependency_name:
            description:
                - Name of the dependency type. This should match the whitelisted enum of dependency names.
            returned: on success
            type: str
            sample: dependency_name_example
        dependency_version:
            description:
                - Version of the Agent dependency.
            returned: on success
            type: str
            sample: dependency_version_example
        description:
            description:
                - Description about the Agent dependency.
            returned: on success
            type: str
            sample: description_example
        namespace:
            description:
                - Object storage namespace associated with the customer's tenancy.
            returned: on success
            type: str
            sample: namespace_example
        bucket:
            description:
                - Object storage bucket where the Agent dependency is uploaded.
            returned: on success
            type: str
            sample: bucket_example
        object_name:
            description:
                - Name of the dependency object uploaded by the customer.
            returned: on success
            type: str
            sample: object_name_example
        time_created:
            description:
                - The time when the AgentDependency was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        e_tag:
            description:
                - The eTag associated with the dependency object returned by Object Storage.
            returned: on success
            type: str
            sample: e_tag_example
        checksum:
            description:
                - The checksum associated with the dependency object returned by Object Storage.
            returned: on success
            type: str
            sample: checksum_example
        lifecycle_state:
            description:
                - The current state of AgentDependency.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed
                  state.
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
        "dependency_name": "dependency_name_example",
        "dependency_version": "dependency_version_example",
        "description": "description_example",
        "namespace": "namespace_example",
        "bucket": "bucket_example",
        "object_name": "object_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "e_tag": "e_tag_example",
        "checksum": "checksum_example",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.cloud_bridge.models import CreateAgentDependencyDetails
    from oci.cloud_bridge.models import UpdateAgentDependencyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AgentDependencyHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(AgentDependencyHelperGen, self).get_possible_entity_types() + [
            "ocbagentdependency",
            "ocbagentdependencies",
            "cloudBridgeocbagentdependency",
            "cloudBridgeocbagentdependencies",
            "ocbagentdependencyresource",
            "ocbagentdependenciesresource",
            "agentdependency",
            "agentdependencies",
            "cloudBridgeagentdependency",
            "cloudBridgeagentdependencies",
            "agentdependencyresource",
            "agentdependenciesresource",
            "cloudbridge",
        ]

    def get_module_resource_id_param(self):
        return "agent_dependency_id"

    def get_module_resource_id(self):
        return self.module.params.get("agent_dependency_id")

    def get_get_fn(self):
        return self.client.get_agent_dependency

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_agent_dependency, agent_dependency_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_agent_dependency,
            agent_dependency_id=self.module.params.get("agent_dependency_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["display_name"]

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
        return oci_common_utils.list_all_resources(
            self.client.list_agent_dependencies, **kwargs
        )

    def get_create_model_class(self):
        return CreateAgentDependencyDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_agent_dependency,
            call_fn_args=(),
            call_fn_kwargs=dict(create_agent_dependency_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateAgentDependencyDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_agent_dependency,
            call_fn_args=(),
            call_fn_kwargs=dict(
                agent_dependency_id=self.module.params.get("agent_dependency_id"),
                update_agent_dependency_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_agent_dependency,
            call_fn_args=(),
            call_fn_kwargs=dict(
                agent_dependency_id=self.module.params.get("agent_dependency_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


AgentDependencyHelperCustom = get_custom_class("AgentDependencyHelperCustom")


class ResourceHelper(AgentDependencyHelperCustom, AgentDependencyHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            dependency_name=dict(type="str"),
            dependency_version=dict(type="str"),
            description=dict(type="str"),
            namespace=dict(type="str"),
            bucket=dict(type="str"),
            object_name=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            system_tags=dict(type="dict"),
            agent_dependency_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="agent_dependency",
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
