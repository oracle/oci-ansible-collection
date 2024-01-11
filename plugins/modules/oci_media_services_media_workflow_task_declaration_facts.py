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
module: oci_media_services_media_workflow_task_declaration_facts
short_description: Fetches details about one or multiple MediaWorkflowTaskDeclaration resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MediaWorkflowTaskDeclaration resources in Oracle Cloud Infrastructure
    - Returns a list of MediaWorkflowTaskDeclarations.
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
    version:
        description:
            - A filter to select MediaWorkflowTaskDeclaration by version.
        type: int
    is_current:
        description:
            - A filter to only select the newest version for each MediaWorkflowTaskDeclaration name.
        type: bool
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided.
        type: str
        choices:
            - "name"
            - "version"
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
- name: List media_workflow_task_declarations
  oci_media_services_media_workflow_task_declaration_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    version: 0
    is_current: true
    sort_by: name
    sort_order: ASC

"""

RETURN = """
media_workflow_task_declarations:
    description:
        - List of MediaWorkflowTaskDeclaration resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - MediaWorkflowTaskDeclaration identifier. The name and version should be unique among
                  MediaWorkflowTaskDeclarations.
            returned: on success
            type: str
            sample: name_example
        version:
            description:
                - The version of MediaWorkflowTaskDeclaration, incremented whenever the team implementing the task processor
                  modifies the JSON schema of this declaration's definitions, parameters or list of required parameters.
            returned: on success
            type: int
            sample: 56
        parameters_schema:
            description:
                - JSON schema specifying the parameters supported by this type of task. This is used to validate tasks'
                  parameters when jobs are created.
            returned: on success
            type: dict
            sample: {}
        parameters_schema_allowing_references:
            description:
                - JSON schema similar to the parameterSchema, but permits parameter values to refer to other parameters using the
                  ${/path/to/another/parmeter} syntax.  This is used to validate task parameters when workflows are created.
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "name": "name_example",
        "version": 56,
        "parameters_schema": {},
        "parameters_schema_allowing_references": {}
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


class MediaWorkflowTaskDeclarationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
            "version",
            "is_current",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_media_workflow_task_declarations, **optional_kwargs
        )


MediaWorkflowTaskDeclarationFactsHelperCustom = get_custom_class(
    "MediaWorkflowTaskDeclarationFactsHelperCustom"
)


class ResourceFactsHelper(
    MediaWorkflowTaskDeclarationFactsHelperCustom,
    MediaWorkflowTaskDeclarationFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            version=dict(type="int"),
            is_current=dict(type="bool"),
            sort_by=dict(type="str", choices=["name", "version"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="media_workflow_task_declaration",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(media_workflow_task_declarations=result)


if __name__ == "__main__":
    main()
