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
module: oci_devops_deploy_environment
short_description: Manage a DeployEnvironment resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a DeployEnvironment resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new deployment environment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    description:
        description:
            - Optional description about the deployment environment.
            - This parameter is updatable.
        type: str
    display_name:
        description:
            - Deployment environment display name. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    deploy_environment_type:
        description:
            - Deployment environment type.
            - Required for create using I(state=present), update using I(state=present) with deploy_environment_id present.
        type: str
        choices:
            - "COMPUTE_INSTANCE_GROUP"
            - "OKE_CLUSTER"
            - "FUNCTION"
    project_id:
        description:
            - The OCID of a project.
            - Required for create using I(state=present).
        type: str
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.  See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace. See L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm). Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    compute_instance_group_selectors:
        description:
            - ""
            - This parameter is updatable.
            - Applicable when deploy_environment_type is 'COMPUTE_INSTANCE_GROUP'
            - Required when deploy_environment_type is 'COMPUTE_INSTANCE_GROUP'
        type: dict
        suboptions:
            items:
                description:
                    - A list of selectors for the instance group. UNION operator is used for combining the instances selected by each selector.
                    - Required when deploy_environment_type is 'COMPUTE_INSTANCE_GROUP'
                type: list
                elements: dict
                required: true
                suboptions:
                    selector_type:
                        description:
                            - Defines the type of the instance selector for the group.
                        type: str
                        choices:
                            - "INSTANCE_IDS"
                            - "INSTANCE_QUERY"
                        required: true
                    compute_instance_ids:
                        description:
                            - Compute instance OCID identifiers that are members of this group.
                            - Required when selector_type is 'INSTANCE_IDS'
                        type: list
                        elements: str
                    region:
                        description:
                            - Region identifier referred by the deployment environment. Region identifiers are listed at https://docs.oracle.com/en-
                              us/iaas/Content/General/Concepts/regions.htm
                            - Required when selector_type is 'INSTANCE_QUERY'
                        type: str
                    query:
                        description:
                            - Query expression confirming to the OCI Search Language syntax to select compute instances for the group. The language is
                              documented at https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm
                            - Required when selector_type is 'INSTANCE_QUERY'
                        type: str
    cluster_id:
        description:
            - The OCID of the Kubernetes cluster.
            - This parameter is updatable.
            - Applicable when deploy_environment_type is 'OKE_CLUSTER'
            - Required when deploy_environment_type is 'OKE_CLUSTER'
        type: str
    function_id:
        description:
            - The OCID of the Function.
            - This parameter is updatable.
            - Applicable when deploy_environment_type is 'FUNCTION'
            - Required when deploy_environment_type is 'FUNCTION'
        type: str
    deploy_environment_id:
        description:
            - Unique environment identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the DeployEnvironment.
            - Use I(state=present) to create or update a DeployEnvironment.
            - Use I(state=absent) to delete a DeployEnvironment.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create deploy_environment with deploy_environment_type = COMPUTE_INSTANCE_GROUP
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: COMPUTE_INSTANCE_GROUP
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compute_instance_group_selectors:
      # required
      items:
      - # required
        selector_type: INSTANCE_IDS
        compute_instance_ids: [ "compute_instance_ids_example" ]

- name: Create deploy_environment with deploy_environment_type = OKE_CLUSTER
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: OKE_CLUSTER
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create deploy_environment with deploy_environment_type = FUNCTION
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: FUNCTION
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_id: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update deploy_environment with deploy_environment_type = COMPUTE_INSTANCE_GROUP
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: COMPUTE_INSTANCE_GROUP

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compute_instance_group_selectors:
      # required
      items:
      - # required
        selector_type: INSTANCE_IDS
        compute_instance_ids: [ "compute_instance_ids_example" ]

- name: Update deploy_environment with deploy_environment_type = OKE_CLUSTER
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: OKE_CLUSTER

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update deploy_environment with deploy_environment_type = FUNCTION
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_id: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update deploy_environment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_environment_type = COMPUTE_INSTANCE_GROUP
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: COMPUTE_INSTANCE_GROUP

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    compute_instance_group_selectors:
      # required
      items:
      - # required
        selector_type: INSTANCE_IDS
        compute_instance_ids: [ "compute_instance_ids_example" ]

- name: Update deploy_environment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_environment_type = OKE_CLUSTER
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: OKE_CLUSTER

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    cluster_id: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update deploy_environment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with deploy_environment_type = FUNCTION
  oci_devops_deploy_environment:
    # required
    deploy_environment_type: FUNCTION

    # optional
    description: description_example
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    function_id: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"

- name: Delete deploy_environment
  oci_devops_deploy_environment:
    # required
    deploy_environment_id: "ocid1.deployenvironment.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete deploy_environment using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_deploy_environment:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
deploy_environment:
    description:
        - Details of the DeployEnvironment resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the deployment environment.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Deployment environment display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        project_id:
            description:
                - The OCID of a project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of a compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        deploy_environment_type:
            description:
                - Deployment environment type.
            returned: on success
            type: str
            sample: OKE_CLUSTER
        time_created:
            description:
                - Time the deployment environment was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the deployment environment was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the deployment environment.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
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
                            type: str
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
                            type: str
                            sample: us-phoenix-1
                        query:
                            description:
                                - Query expression confirming to the OCI Search Language syntax to select compute instances for the group. The language is
                                  documented at https://docs.oracle.com/en-us/iaas/Content/Search/Concepts/querysyntax.htm
                            returned: on success
                            type: str
                            sample: query_example
        function_id:
            description:
                - The OCID of the Function.
            returned: on success
            type: str
            sample: "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx"
        cluster_id:
            description:
                - The OCID of the Kubernetes cluster.
            returned: on success
            type: str
            sample: "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
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
                "region": "us-phoenix-1",
                "query": "query_example"
            }]
        },
        "function_id": "ocid1.function.oc1..xxxxxxEXAMPLExxxxxx",
        "cluster_id": "ocid1.cluster.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.devops import DevopsClient
    from oci.devops.models import CreateDeployEnvironmentDetails
    from oci.devops.models import UpdateDeployEnvironmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DeployEnvironmentHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(DeployEnvironmentHelperGen, self).get_possible_entity_types() + [
            "devopsdeployenvironment",
            "devopsdeployenvironments",
            "devopsdevopsdeployenvironment",
            "devopsdevopsdeployenvironments",
            "devopsdeployenvironmentresource",
            "devopsdeployenvironmentsresource",
            "deployenvironment",
            "deployenvironments",
            "deployenvironmentresource",
            "deployenvironmentsresource",
            "devops",
        ]

    def get_module_resource_id_param(self):
        return "deploy_environment_id"

    def get_module_resource_id(self):
        return self.module.params.get("deploy_environment_id")

    def get_get_fn(self):
        return self.client.get_deploy_environment

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_environment, deploy_environment_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_deploy_environment,
            deploy_environment_id=self.module.params.get("deploy_environment_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["project_id", "display_name"]

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
            self.client.list_deploy_environments, **kwargs
        )

    def get_create_model_class(self):
        return CreateDeployEnvironmentDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_deploy_environment,
            call_fn_args=(),
            call_fn_kwargs=dict(create_deploy_environment_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateDeployEnvironmentDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_deploy_environment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_environment_id=self.module.params.get("deploy_environment_id"),
                update_deploy_environment_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_deploy_environment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                deploy_environment_id=self.module.params.get("deploy_environment_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DeployEnvironmentHelperCustom = get_custom_class("DeployEnvironmentHelperCustom")


class ResourceHelper(DeployEnvironmentHelperCustom, DeployEnvironmentHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            description=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            deploy_environment_type=dict(
                type="str",
                choices=["COMPUTE_INSTANCE_GROUP", "OKE_CLUSTER", "FUNCTION"],
            ),
            project_id=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            compute_instance_group_selectors=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            selector_type=dict(
                                type="str",
                                required=True,
                                choices=["INSTANCE_IDS", "INSTANCE_QUERY"],
                            ),
                            compute_instance_ids=dict(type="list", elements="str"),
                            region=dict(type="str"),
                            query=dict(type="str"),
                        ),
                    )
                ),
            ),
            cluster_id=dict(type="str"),
            function_id=dict(type="str"),
            deploy_environment_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="deploy_environment",
        service_client_class=DevopsClient,
        namespace="devops",
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
