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
module: oci_cloud_bridge_agent_dependency_facts
short_description: Fetches details about one or multiple AgentDependency resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AgentDependency resources in Oracle Cloud Infrastructure
    - Returns a list of AgentDependencies such as AgentDependencyCollection.
    - If I(agent_dependency_id) is specified, the details of a single AgentDependency will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    agent_dependency_id:
        description:
            - A unique AgentDependency identifier.
            - Required to get a specific agent_dependency.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple agent_dependencies.
        type: str
    agent_id:
        description:
            - A filter to return only resources that match the given Agent ID.
        type: str
    environment_id:
        description:
            - A filter to return only resources that match the given environment ID.
        type: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "timeUpdated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific agent_dependency
  oci_cloud_bridge_agent_dependency_facts:
    # required
    agent_dependency_id: "ocid1.agentdependency.oc1..xxxxxxEXAMPLExxxxxx"

- name: List agent_dependencies
  oci_cloud_bridge_agent_dependency_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    environment_id: "ocid1.environment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
agent_dependencies:
    description:
        - List of AgentDependency resources
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
    sample: [{
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
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_bridge import OcbAgentSvcClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AgentDependencyFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "agent_dependency_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_agent_dependency,
            agent_dependency_id=self.module.params.get("agent_dependency_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "agent_id",
            "environment_id",
            "lifecycle_state",
            "display_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_agent_dependencies,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AgentDependencyFactsHelperCustom = get_custom_class("AgentDependencyFactsHelperCustom")


class ResourceFactsHelper(
    AgentDependencyFactsHelperCustom, AgentDependencyFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            agent_dependency_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            agent_id=dict(type="str"),
            environment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "DELETING",
                    "DELETED",
                    "FAILED",
                ],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeCreated", "timeUpdated", "displayName"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="agent_dependency",
        service_client_class=OcbAgentSvcClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(agent_dependencies=result)


if __name__ == "__main__":
    main()
