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
module: oci_media_services_system_media_workflow_facts
short_description: Fetches details about one or multiple SystemMediaWorkflow resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SystemMediaWorkflow resources in Oracle Cloud Infrastructure
    - Lists the SystemMediaWorkflows that can be used to run a job by name or as a template to create a MediaWorkflow.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    name:
        description:
            - A filter to return only the resources with their system defined, unique name matching the given name.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List system_media_workflows
  oci_media_services_system_media_workflow_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    sort_order: ASC

"""

RETURN = """
system_media_workflows:
    description:
        - List of SystemMediaWorkflow resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - System provided unique identifier for this static media workflow.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Description of this workflow's processing and how that processing can be customized by
                  specifying parameter values.
            returned: on success
            type: str
            sample: description_example
        parameters:
            description:
                - JSON object representing named parameters and their default values that can be referenced throughout this workflow.
                  The values declared here can be overridden by the MediaWorkflowConfigurations or parameters supplied when creating
                  MediaWorkflowJobs from this MediaWorkflow.
            returned: on success
            type: dict
            sample: {}
        tasks:
            description:
                - The processing to be done in this workflow. Each key of the MediaWorkflowTasks in this array is unique
                  within the array. The order of the items is preserved from the order of the tasks array in
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
    sample: [{
        "name": "name_example",
        "description": "description_example",
        "parameters": {},
        "tasks": [{
            "type": "type_example",
            "version": 56,
            "key": "key_example",
            "prerequisites": [],
            "enable_parameter_reference": "enable_parameter_reference_example",
            "enable_when_referenced_parameter_equals": {},
            "parameters": {}
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.media_services import MediaServicesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SystemMediaWorkflowFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_system_media_workflows, **optional_kwargs
        )


SystemMediaWorkflowFactsHelperCustom = get_custom_class(
    "SystemMediaWorkflowFactsHelperCustom"
)


class ResourceFactsHelper(
    SystemMediaWorkflowFactsHelperCustom, SystemMediaWorkflowFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="system_media_workflow",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(system_media_workflows=result)


if __name__ == "__main__":
    main()
