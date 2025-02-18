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
module: oci_media_services_media_workflow
short_description: Manage a MediaWorkflow resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a MediaWorkflow resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new MediaWorkflow.
    - "This resource has the following action operations in the M(oracle.oci.oci_media_services_media_workflow_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Compartment Identifier.
            - Required for create using I(state=present).
        type: str
    display_name:
        description:
            - Name for the MediaWorkflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    tasks:
        description:
            - The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array must be unique
              within the array. The order of tasks given here will be preserved.
            - This parameter is updatable.
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - The type of process to run at this task. Refers to the name of a MediaWorkflowTaskDeclaration.
                type: str
            version:
                description:
                    - The version of the MediaWorkflowTaskDeclaration.
                type: int
                required: true
            key:
                description:
                    - A unique identifier for this task within its workflow. Keys are used to reference a task within workflows
                      and MediaWorkflowJobs. Tasks are referenced as prerequisites and to track output and state.
                type: str
                required: true
            prerequisites:
                description:
                    - Keys to the other tasks in this workflow that must be completed before execution of this task can begin.
                type: list
                elements: str
            enable_parameter_reference:
                description:
                    - Allows this task to be conditionally enabled.  If no value or a blank value is given, the task is
                      unconditionally enbled.  Otherwise the given string specifies a parameter of the job created for this task's
                      workflow using the JSON pointer syntax. The JSON pointer is validated when a job is created from the workflow of this task.
                type: str
            enable_when_referenced_parameter_equals:
                description:
                    - Used in conjunction with enableParameterReference to conditionally enable a task.  When a job is created
                      from the workflow of this task, the task will only be enabled if the value of the parameter specified by
                      enableParameterReference is equal to the value of this property. This property must be prenset if and only if
                      a enableParameterReference is given. The value is a JSON node.
                type: dict
            parameters:
                description:
                    - Data specifiying how this task is to be run. The data is a JSON object that must conform to the JSON Schema
                      specified by the parameters of the MediaWorkflowTaskDeclaration this task references. The parameters may
                      contain values or references to other parameters.
                type: dict
    media_workflow_configuration_ids:
        description:
            - Configurations to be applied to all the jobs for this workflow. Parameters in these configurations are
              overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflowJob and the
              parameters of the MediaWorkflowJob.
            - This parameter is updatable.
        type: list
        elements: str
    parameters:
        description:
            - JSON object representing named parameters and their default values that can be referenced throughout this workflow.
              The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating
              MediaWorkflowJobs from this MediaWorkflow.
            - This parameter is updatable.
        type: dict
    freeform_tags:
        description:
            - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
              Example: `{\\"bar-key\\": \\"value\\"}`"
            - This parameter is updatable.
        type: dict
    defined_tags:
        description:
            - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
              Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            - This parameter is updatable.
        type: dict
    media_workflow_id:
        description:
            - Unique MediaWorkflow identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the MediaWorkflow.
            - Use I(state=present) to create or update a MediaWorkflow.
            - Use I(state=absent) to delete a MediaWorkflow.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create media_workflow
  oci_media_services_media_workflow:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example

    # optional
    tasks:
    - # required
      version: 56
      key: key_example

      # optional
      type: type_example
      prerequisites: [ "prerequisites_example" ]
      enable_parameter_reference: enable_parameter_reference_example
      enable_when_referenced_parameter_equals: null
      parameters: null
    media_workflow_configuration_ids: [ "media_workflow_configuration_ids_example" ]
    parameters: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update media_workflow
  oci_media_services_media_workflow:
    # required
    media_workflow_id: "ocid1.mediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    tasks:
    - # required
      version: 56
      key: key_example

      # optional
      type: type_example
      prerequisites: [ "prerequisites_example" ]
      enable_parameter_reference: enable_parameter_reference_example
      enable_when_referenced_parameter_equals: null
      parameters: null
    media_workflow_configuration_ids: [ "media_workflow_configuration_ids_example" ]
    parameters: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update media_workflow using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_media_workflow:
    # required
    display_name: display_name_example

    # optional
    tasks:
    - # required
      version: 56
      key: key_example

      # optional
      type: type_example
      prerequisites: [ "prerequisites_example" ]
      enable_parameter_reference: enable_parameter_reference_example
      enable_when_referenced_parameter_equals: null
      parameters: null
    media_workflow_configuration_ids: [ "media_workflow_configuration_ids_example" ]
    parameters: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete media_workflow
  oci_media_services_media_workflow:
    # required
    media_workflow_id: "ocid1.mediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete media_workflow using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_media_workflow:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
media_workflow:
    description:
        - Details of the MediaWorkflow resource acted upon by the current operation
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
                - Name of the Media Workflow. Does not have to be unique, and it's changeable. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        tasks:
            description:
                - The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array is unique
                  within the array.  The order of the items is preserved from the order of the tasks array in
                  CreateMediaWorkflowDetails or UpdateMediaWorkflowDetails.
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - The type of process to run at this task. Refers to the name of a MediaWorkflowTaskDeclaration.
                    returned: on success
                    type: str
                    sample: type_example
                version:
                    description:
                        - The version of the MediaWorkflowTaskDeclaration.
                    returned: on success
                    type: int
                    sample: 56
                key:
                    description:
                        - A unique identifier for this task within its workflow. Keys are used to reference a task within workflows
                          and MediaWorkflowJobs. Tasks are referenced as prerequisites and to track output and state.
                    returned: on success
                    type: str
                    sample: key_example
                prerequisites:
                    description:
                        - Keys to the other tasks in this workflow that must be completed before execution of this task can begin.
                    returned: on success
                    type: list
                    sample: []
                enable_parameter_reference:
                    description:
                        - Allows this task to be conditionally enabled.  If no value or a blank value is given, the task is
                          unconditionally enbled.  Otherwise the given string specifies a parameter of the job created for this task's
                          workflow using the JSON pointer syntax. The JSON pointer is validated when a job is created from the workflow of this task.
                    returned: on success
                    type: str
                    sample: enable_parameter_reference_example
                enable_when_referenced_parameter_equals:
                    description:
                        - Used in conjunction with enableParameterReference to conditionally enable a task.  When a job is created
                          from the workflow of this task, the task will only be enabled if the value of the parameter specified by
                          enableParameterReference is equal to the value of this property. This property must be prenset if and only if
                          a enableParameterReference is given. The value is a JSON node.
                    returned: on success
                    type: dict
                    sample: {}
                parameters:
                    description:
                        - Data specifiying how this task is to be run. The data is a JSON object that must conform to the JSON Schema
                          specified by the parameters of the MediaWorkflowTaskDeclaration this task references. The parameters may
                          contain values or references to other parameters.
                    returned: on success
                    type: dict
                    sample: {}
        media_workflow_configuration_ids:
            description:
                - Configurations to be applied to all the runs of this workflow. Parameters in these configurations are
                  overridden by parameters in the MediaWorkflowConfigurations of the MediaWorkflowJob and the
                  parameters of the MediaWorkflowJob. If the same parameter appears in multiple configurations, the values that
                  appear in the configuration at the highest index will be used.
            returned: on success
            type: list
            sample: []
        parameters:
            description:
                - JSON object representing named parameters and their default values that can be referenced throughout this workflow.
                  The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating
                  MediaWorkflowJobs from this MediaWorkflow.
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time when the MediaWorkflow was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the MediaWorkflow was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the MediaWorkflow.
            returned: on success
            type: str
            sample: ACTIVE
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecyle_details_example
        version:
            description:
                - The version of the MediaWorkflow.
            returned: on success
            type: int
            sample: 56
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "tasks": [{
            "type": "type_example",
            "version": 56,
            "key": "key_example",
            "prerequisites": [],
            "enable_parameter_reference": "enable_parameter_reference_example",
            "enable_when_referenced_parameter_equals": {},
            "parameters": {}
        }],
        "media_workflow_configuration_ids": [],
        "parameters": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecyle_details": "lifecyle_details_example",
        "version": 56,
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
    from oci.media_services import MediaServicesClient
    from oci.media_services.models import CreateMediaWorkflowDetails
    from oci.media_services.models import UpdateMediaWorkflowDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaWorkflowHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MediaWorkflowHelperGen, self).get_possible_entity_types() + [
            "mediaworkflow",
            "mediaworkflows",
            "mediaServicesmediaworkflow",
            "mediaServicesmediaworkflows",
            "mediaworkflowresource",
            "mediaworkflowsresource",
            "mediaservices",
        ]

    def get_module_resource_id_param(self):
        return "media_workflow_id"

    def get_module_resource_id(self):
        return self.module.params.get("media_workflow_id")

    def get_get_fn(self):
        return self.client.get_media_workflow

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow, media_workflow_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow,
            media_workflow_id=self.module.params.get("media_workflow_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["compartment_id", "display_name"]

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
            self.client.list_media_workflows, **kwargs
        )

    def get_create_model_class(self):
        return CreateMediaWorkflowDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_media_workflow,
            call_fn_args=(),
            call_fn_kwargs=dict(create_media_workflow_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateMediaWorkflowDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_media_workflow,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_workflow_id=self.module.params.get("media_workflow_id"),
                update_media_workflow_details=update_details,
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
            call_fn=self.client.delete_media_workflow,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_workflow_id=self.module.params.get("media_workflow_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MediaWorkflowHelperCustom = get_custom_class("MediaWorkflowHelperCustom")


class ResourceHelper(MediaWorkflowHelperCustom, MediaWorkflowHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            tasks=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(type="str"),
                    version=dict(type="int", required=True),
                    key=dict(type="str", required=True, no_log=True),
                    prerequisites=dict(type="list", elements="str"),
                    enable_parameter_reference=dict(type="str"),
                    enable_when_referenced_parameter_equals=dict(type="dict"),
                    parameters=dict(type="dict"),
                ),
            ),
            media_workflow_configuration_ids=dict(type="list", elements="str"),
            parameters=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            media_workflow_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="media_workflow",
        service_client_class=MediaServicesClient,
        namespace="media_services",
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
