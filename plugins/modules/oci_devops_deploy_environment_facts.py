#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_devops_deploy_environment_facts
short_description: Fetches details about one or multiple DeployEnvironment resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple DeployEnvironment resources in Oracle Cloud Infrastructure
    - Returns a list of deployment environments.
    - If I(deploy_environment_id) is specified, the details of a single DeployEnvironment will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    deploy_environment_id:
        description:
            - Unique environment identifier.
            - Required to get a specific deploy_environment.
        type: str
        aliases: ["id"]
    project_id:
        description:
            - unique project identifier
        type: str
    compartment_id:
        description:
            - The OCID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only DeployEnvironments that matches the given lifecycleState.
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
            - The sort order to use. Use either ascending or descending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for time created is descending. Default order for display name is
              ascending. If no value is specified, then the default time created value is considered.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List deploy_environments
  oci_devops_deploy_environment_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific deploy_environment
  oci_devops_deploy_environment_facts:
    deploy_environment_id: "ocid1.deployenvironment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
deploy_environments:
    description:
        - List of DeployEnvironment resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the deployment environment.
            returned: on success
            type: string
            sample: description_example
        display_name:
            description:
                - Deployment environment display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: string
            sample: display_name_example
        project_id:
            description:
                - The OCID of a project.
            returned: on success
            type: string
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_environment_type:
            description:
                - Deployment environment type.
            returned: on success
            type: string
            sample: OKE_CLUSTER
        time_created:
            description:
                - Time the deployment environment was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_updated:
            description:
                - Time the deployment environment was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        lifecycle_state:
            description:
                - The current state of the deployment environment.
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
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces. See L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\":
                  \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
        compute_instance_group_selectors:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - A list of selectors for the instance group. UNION operator is used for combining the instances selected by each selector.
                    returned: on success
                    type: complex
                    contains:
                        selector_type:
                            description:
                                - Defines the type of the instance selector for the group.
                            returned: on success
                            type: string
                            sample: INSTANCE_IDS
                        compute_instance_ids:
                            description:
                                - Compute instance OCID identifiers that are members of this group.
                            returned: on success
                            type: list
                            sample: []
                        region:
                            description:
                                - Region identifier referred by the deployment environment. Region identifiers are listed at https://docs.oracle.com/en-
                                  us/iaas/Content/General/Concepts/regions.htm
                            returned: on success
                            type: string
                            sample: region_example
                        query:
                            description:
                                - Query expression confirming to the OCI Search Language syntax to select compute instances for the group. The language is
                                  documented at https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm
                            returned: on success
                            type: string
                            sample: query_example
        function_id:
            description:
                - The OCID of the Function.
            returned: on success
            type: string
            sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_id:
            description:
                - The OCID of the Kubernetes cluster.
            returned: on success
            type: string
            sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "deploy_environment_type": "OKE_CLUSTER",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "compute_instance_group_selectors": {
            "items": [{
                "selector_type": "INSTANCE_IDS",
                "compute_instance_ids": [],
                "region": "region_example",
                "query": "query_example"
            }]
        },
        "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
        "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeployEnvironmentFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "deploy_environment_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_environment,
            deploy_environment_id=self.module.params.get("deploy_environment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "project_id",
            "compartment_id",
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
            self.client.list_deploy_environments, **optional_kwargs
        )


DeployEnvironmentFactsHelperCustom = get_custom_class(
    "DeployEnvironmentFactsHelperCustom"
)


class ResourceFactsHelper(
    DeployEnvironmentFactsHelperCustom, DeployEnvironmentFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            deploy_environment_id=dict(aliases=["id"], type="str"),
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
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
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="deploy_environment",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(deploy_environments=result)


if __name__ == "__main__":
    main()
