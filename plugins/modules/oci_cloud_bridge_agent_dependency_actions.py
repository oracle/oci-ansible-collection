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
module: oci_cloud_bridge_agent_dependency_actions
short_description: Perform actions on an AgentDependency resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an AgentDependency resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a AgentDependency resource from one compartment identifier to another. When provided, If-Match is checked against
      ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    agent_dependency_id:
        description:
            - A unique AgentDependency identifier.
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
            - The action to perform on the AgentDependency.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on agent_dependency
  oci_cloud_bridge_agent_dependency_actions:
    # required
    agent_dependency_id: "ocid1.agentdependency.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.cloud_bridge import OcbAgentSvcClient
    from oci.cloud_bridge.models import ChangeAgentDependencyCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AgentDependencyActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "agent_dependency_id"

    def get_module_resource_id(self):
        return self.module.params.get("agent_dependency_id")

    def get_get_fn(self):
        return self.client.get_agent_dependency

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_agent_dependency,
            agent_dependency_id=self.module.params.get("agent_dependency_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeAgentDependencyCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_agent_dependency_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                agent_dependency_id=self.module.params.get("agent_dependency_id"),
                change_agent_dependency_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


AgentDependencyActionsHelperCustom = get_custom_class(
    "AgentDependencyActionsHelperCustom"
)


class ResourceHelper(
    AgentDependencyActionsHelperCustom, AgentDependencyActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            agent_dependency_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
