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
module: oci_cloud_bridge_environment_actions
short_description: Perform actions on an Environment resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Environment resource in Oracle Cloud Infrastructure
    - For I(action=add_agent_dependency), add a dependency to the environment. When provided, If-Match is checked against ETag values of the resource.
    - For I(action=change_compartment), moves a source environment resource from one compartment identifier to another. When provided, If-Match is checked
      against ETag values of the resource.
    - For I(action=remove_agent_dependency), adds a dependency to the source environment. When provided, If-Match is checked against ETag values of the
      resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
            - Required for I(action=change_compartment).
        type: str
    environment_id:
        description:
            - Unique environment identifier.
        type: str
        aliases: ["id"]
        required: true
    agent_dependency_id:
        description:
            - The OCID of the agentDependency, which is added to the source environment.
            - Required for I(action=add_agent_dependency), I(action=remove_agent_dependency).
        type: str
    action:
        description:
            - The action to perform on the Environment.
        type: str
        required: true
        choices:
            - "add_agent_dependency"
            - "change_compartment"
            - "remove_agent_dependency"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action add_agent_dependency on environment
  oci_cloud_bridge_environment_actions:
    # required
    environment_id: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
    agent_dependency_id: "ocid1.agentdependency.oc1..xxxxxxEXAMPLExxxxxx"
    action: add_agent_dependency

- name: Perform action change_compartment on environment
  oci_cloud_bridge_environment_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    environment_id: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action remove_agent_dependency on environment
  oci_cloud_bridge_environment_actions:
    # required
    environment_id: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
    agent_dependency_id: "ocid1.agentdependency.oc1..xxxxxxEXAMPLExxxxxx"
    action: remove_agent_dependency

"""

RETURN = """
environment:
    description:
        - Details of the Environment resource acted upon by the current operation
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
                - Environment identifier, which can be renamed.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time when the source environment was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the source environment was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the source environment.
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
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.cloud_bridge.models import AddAgentDependencyDetails
    from oci.cloud_bridge.models import ChangeEnvironmentCompartmentDetails
    from oci.cloud_bridge.models import RemoveAgentDependencyDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EnvironmentActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        add_agent_dependency
        change_compartment
        remove_agent_dependency
    """

    @staticmethod
    def get_module_resource_id_param():
        return "environment_id"

    def get_module_resource_id(self):
        return self.module.params.get("environment_id")

    def get_get_fn(self):
        return self.client.get_environment

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_environment,
            environment_id=self.module.params.get("environment_id"),
        )

    def add_agent_dependency(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, AddAgentDependencyDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.add_agent_dependency,
            call_fn_args=(),
            call_fn_kwargs=dict(
                environment_id=self.module.params.get("environment_id"),
                add_agent_dependency_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeEnvironmentCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_environment_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                environment_id=self.module.params.get("environment_id"),
                change_environment_compartment_details=action_details,
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

    def remove_agent_dependency(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, RemoveAgentDependencyDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.remove_agent_dependency,
            call_fn_args=(),
            call_fn_kwargs=dict(
                environment_id=self.module.params.get("environment_id"),
                remove_agent_dependency_details=action_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


EnvironmentActionsHelperCustom = get_custom_class("EnvironmentActionsHelperCustom")


class ResourceHelper(EnvironmentActionsHelperCustom, EnvironmentActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            environment_id=dict(aliases=["id"], type="str", required=True),
            agent_dependency_id=dict(type="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "add_agent_dependency",
                    "change_compartment",
                    "remove_agent_dependency",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="environment",
        service_client_class=OcbAgentSvcClient,
        namespace="cloud_bridge",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
