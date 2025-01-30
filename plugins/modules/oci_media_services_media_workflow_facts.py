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
module: oci_media_services_media_workflow_facts
short_description: Fetches details about one or multiple MediaWorkflow resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MediaWorkflow resources in Oracle Cloud Infrastructure
    - Lists the MediaWorkflows.
    - If I(media_workflow_id) is specified, the details of a single MediaWorkflow will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    media_workflow_id:
        description:
            - Unique MediaWorkflow identifier.
            - Required to get a specific media_workflow.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    lifecycle_state:
        description:
            - A filter to return only the resources with lifecycleState matching the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "NEEDS_ATTENTION"
            - "DELETED"
    display_name:
        description:
            - A filter to return only the resources that match the entire display name given.
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
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default
              order for displayName is ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific media_workflow
  oci_media_services_media_workflow_facts:
    # required
    media_workflow_id: "ocid1.mediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"

- name: List media_workflows
  oci_media_services_media_workflow_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: ACTIVE
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
media_workflows:
    description:
        - List of MediaWorkflow resources
    returned: on success
    type: complex
    contains:
        tasks:
            description:
                - The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array is unique
                  within the array.  The order of the items is preserved from the order of the tasks array in
                  CreateMediaWorkflowDetails or UpdateMediaWorkflowDetails.
                - Returned for get operation
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
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        parameters:
            description:
                - JSON object representing named parameters and their default values that can be referenced throughout this workflow.
                  The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating
                  MediaWorkflowJobs from this MediaWorkflow.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        lifecyle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecyle_details_example
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
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for list operation
            returned: on success
            type: str
            sample: lifecycle_details_example
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
    sample: [{
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
        "lifecyle_details": "lifecyle_details_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "version": 56,
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
    from oci.media_services import MediaServicesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaWorkflowFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "media_workflow_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow,
            media_workflow_id=self.module.params.get("media_workflow_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_media_workflows, **optional_kwargs
        )


MediaWorkflowFactsHelperCustom = get_custom_class("MediaWorkflowFactsHelperCustom")


class ResourceFactsHelper(MediaWorkflowFactsHelperCustom, MediaWorkflowFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            media_workflow_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str", choices=["ACTIVE", "NEEDS_ATTENTION", "DELETED"]
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="media_workflow",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(media_workflows=result)


if __name__ == "__main__":
    main()
