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
module: oci_devops_build_pipeline_facts
short_description: Fetches details about one or multiple BuildPipeline resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BuildPipeline resources in Oracle Cloud Infrastructure
    - Returns a list of build pipelines.
    - If I(build_pipeline_id) is specified, the details of a single BuildPipeline will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    build_pipeline_id:
        description:
            - Unique build pipeline identifier.
            - Required to get a specific build_pipeline.
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
            - A filter to return only build pipelines that matches the given lifecycle state.
        type: str
        choices:
            - "CREATING"
            - "UPDATING"
            - "ACTIVE"
            - "INACTIVE"
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
- name: Get a specific build_pipeline
  oci_devops_build_pipeline_facts:
    # required
    build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

- name: List build_pipelines
  oci_devops_build_pipeline_facts:

    # optional
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    display_name: display_name_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
build_pipelines:
    description:
        - List of BuildPipeline resources
    returned: on success
    type: complex
    contains:
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
                - Returned for get operation
            returned: on success
            type: str
            sample: lifecycle_details_example
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - Optional description about the build pipeline.
            returned: on success
            type: str
            sample: description_example
        display_name:
            description:
                - Build pipeline display name, which can be renamed and is not necessarily unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - The OCID of the compartment where the build pipeline is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        project_id:
            description:
                - The OCID of the DevOps project.
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The time the build pipeline was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the build pipeline was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the build pipeline.
            returned: on success
            type: str
            sample: CREATING
        build_pipeline_parameters:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of parameters defined for a build pipeline.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - "Name of the parameter (case-sensitive). Parameter name must be ^[a-zA-Z][a-zA-Z_0-9]*$.
                                  Example: 'Build_Pipeline_param' is not same as 'build_pipeline_Param'"
                            returned: on success
                            type: str
                            sample: name_example
                        default_value:
                            description:
                                - Default value of the parameter.
                            returned: on success
                            type: str
                            sample: default_value_example
                        description:
                            description:
                                - Description of the parameter.
                            returned: on success
                            type: str
                            sample: description_example
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
    sample: [{
        "lifecycle_details": "lifecycle_details_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "build_pipeline_parameters": {
            "items": [{
                "name": "name_example",
                "default_value": "default_value_example",
                "description": "description_example"
            }]
        },
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
    from oci.devops import DevopsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BuildPipelineFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "build_pipeline_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_build_pipeline,
            build_pipeline_id=self.module.params.get("build_pipeline_id"),
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
            self.client.list_build_pipelines, **optional_kwargs
        )


BuildPipelineFactsHelperCustom = get_custom_class("BuildPipelineFactsHelperCustom")


class ResourceFactsHelper(BuildPipelineFactsHelperCustom, BuildPipelineFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            build_pipeline_id=dict(aliases=["id"], type="str"),
            project_id=dict(type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "UPDATING",
                    "ACTIVE",
                    "INACTIVE",
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

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="build_pipeline",
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

    module.exit_json(build_pipelines=result)


if __name__ == "__main__":
    main()
