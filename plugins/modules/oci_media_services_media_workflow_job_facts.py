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
module: oci_media_services_media_workflow_job_facts
short_description: Fetches details about one or multiple MediaWorkflowJob resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MediaWorkflowJob resources in Oracle Cloud Infrastructure
    - Lists the MediaWorkflowJobs.
    - If I(media_workflow_job_id) is specified, the details of a single MediaWorkflowJob will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    media_workflow_job_id:
        description:
            - Unique MediaWorkflowJob identifier.
            - Required to get a specific media_workflow_job.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
        type: str
    media_workflow_id:
        description:
            - Unique MediaWorkflow identifier.
        type: str
    display_name:
        description:
            - A filter to return only the resources that match the entire display name given.
        type: str
        aliases: ["name"]
    lifecycle_state:
        description:
            - A filter to return only the resources with lifecycleState matching the given lifecycleState.
        type: str
        choices:
            - "ACCEPTED"
            - "IN_PROGRESS"
            - "WAITING"
            - "FAILED"
            - "SUCCEEDED"
            - "CANCELING"
            - "CANCELED"
    sort_by:
        description:
            - The parameter sort by.
        type: str
        choices:
            - "timeCreated"
            - "workflowId"
            - "lifecycleState"
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
- name: Get a specific media_workflow_job
  oci_media_services_media_workflow_job_facts:
    # required
    media_workflow_job_id: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"

- name: List media_workflow_jobs
  oci_media_services_media_workflow_job_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    media_workflow_id: "ocid1.mediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    lifecycle_state: ACCEPTED
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
media_workflow_jobs:
    description:
        - List of MediaWorkflowJob resources
    returned: on success
    type: complex
    contains:
        media_workflow_configuration_ids:
            description:
                - Configurations to be applied to this run of the workflow.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        compartment_id:
            description:
                - Compartment Identifier.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        task_lifecycle_state:
            description:
                - Status of each task.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - Unique key within a MediaWorkflowJob for the task.
                    returned: on success
                    type: str
                    sample: key_example
                lifecycle_state:
                    description:
                        - The current state of the MediaWorkflowJob task.
                    returned: on success
                    type: str
                    sample: lifecycle_state_example
                lifecycle_details:
                    description:
                        - The lifecycle details of MediaWorkflowJob task.
                    returned: on success
                    type: str
                    sample: lifecycle_details_example
        parameters:
            description:
                - Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow,
                  the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this
                  MediaWorkflowJob. The parameters are given as JSON.  The top level and 2nd level elements must be
                  JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level
                  keys refer to a parameter's name.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        runnable:
            description:
                - A JSON representation of the job as it will be run by the system. All the task declarations, configurations
                  and parameters are merged. Parameter values are all fully resolved.
                - Returned for get operation
            returned: on success
            type: dict
            sample: {}
        outputs:
            description:
                - A list of JobOutput for the workflowJob.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                asset_type:
                    description:
                        - Type of job output.
                    returned: on success
                    type: str
                    sample: AUDIO
                namespace_name:
                    description:
                        - The namespace name of the job output.
                    returned: on success
                    type: str
                    sample: namespace_name_example
                bucket_name:
                    description:
                        - The bucket name of the job output.
                    returned: on success
                    type: str
                    sample: bucket_name_example
                object_name:
                    description:
                        - The object name of the job output.
                    returned: on success
                    type: str
                    sample: object_name_example
                id:
                    description:
                        - The ID associated with the job output.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_started:
            description:
                - Time when the job started to execute. An RFC3339 formatted datetime string.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - Time when the job finished. An RFC3339 formatted datetime string.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        media_workflow_id:
            description:
                - The workflow to execute.
            returned: on success
            type: str
            sample: "ocid1.mediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - Unique identifier for this run of the workflow.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - Creation time of the job. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Updated time of the job. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the MediaWorkflowJob.
            returned: on success
            type: str
            sample: ACCEPTED
        lifecycle_details:
            description:
                - The lifecyle details.
            returned: on success
            type: str
            sample: lifecycle_details_example
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
        "media_workflow_configuration_ids": [],
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "task_lifecycle_state": [{
            "key": "key_example",
            "lifecycle_state": "lifecycle_state_example",
            "lifecycle_details": "lifecycle_details_example"
        }],
        "parameters": {},
        "runnable": {},
        "outputs": [{
            "asset_type": "AUDIO",
            "namespace_name": "namespace_name_example",
            "bucket_name": "bucket_name_example",
            "object_name": "object_name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "time_started": "2013-10-20T19:20:30+01:00",
        "time_ended": "2013-10-20T19:20:30+01:00",
        "media_workflow_id": "ocid1.mediaworkflow.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACCEPTED",
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
    from oci.media_services import MediaServicesClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaWorkflowJobFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "media_workflow_job_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow_job,
            media_workflow_job_id=self.module.params.get("media_workflow_job_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "media_workflow_id",
            "display_name",
            "lifecycle_state",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_media_workflow_jobs, **optional_kwargs
        )


MediaWorkflowJobFactsHelperCustom = get_custom_class(
    "MediaWorkflowJobFactsHelperCustom"
)


class ResourceFactsHelper(
    MediaWorkflowJobFactsHelperCustom, MediaWorkflowJobFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            media_workflow_job_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            media_workflow_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "ACCEPTED",
                    "IN_PROGRESS",
                    "WAITING",
                    "FAILED",
                    "SUCCEEDED",
                    "CANCELING",
                    "CANCELED",
                ],
            ),
            sort_by=dict(
                type="str", choices=["timeCreated", "workflowId", "lifecycleState"]
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="media_workflow_job",
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

    module.exit_json(media_workflow_jobs=result)


if __name__ == "__main__":
    main()
