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
module: oci_media_services_media_workflow_job_actions
short_description: Perform actions on a MediaWorkflowJob resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MediaWorkflowJob resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a MediaWorkflowJob resource from one compartment identifier to another.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    media_workflow_job_id:
        description:
            - Unique MediaWorkflowJob identifier.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the resource should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the MediaWorkflowJob.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on media_workflow_job
  oci_media_services_media_workflow_job_actions:
    # required
    media_workflow_job_id: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
media_workflow_job:
    description:
        - Details of the MediaWorkflowJob resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        media_workflow_configuration_ids:
            description:
                - Configurations to be applied to this run of the workflow.
            returned: on success
            type: list
            sample: []
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
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
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
        task_lifecycle_state:
            description:
                - Status of each task.
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
            returned: on success
            type: dict
            sample: {}
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
        runnable:
            description:
                - A JSON representation of the job as it will be run by the system. All the task declarations, configurations
                  and parameters are merged. Parameter values are all fully resolved.
            returned: on success
            type: dict
            sample: {}
        outputs:
            description:
                - A list of JobOutput for the workflowJob.
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
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_ended:
            description:
                - Time when the job finished. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        "media_workflow_configuration_ids": [],
        "media_workflow_id": "ocid1.mediaworkflow.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "ACCEPTED",
        "lifecycle_details": "lifecycle_details_example",
        "task_lifecycle_state": [{
            "key": "key_example",
            "lifecycle_state": "lifecycle_state_example",
            "lifecycle_details": "lifecycle_details_example"
        }],
        "parameters": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.media_services import MediaServicesClient
    from oci.media_services.models import ChangeMediaWorkflowJobCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaWorkflowJobActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "media_workflow_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("media_workflow_job_id")

    def get_get_fn(self):
        return self.client.get_media_workflow_job

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow_job,
            media_workflow_job_id=self.module.params.get("media_workflow_job_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeMediaWorkflowJobCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_media_workflow_job_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_workflow_job_id=self.module.params.get("media_workflow_job_id"),
                change_media_workflow_job_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
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


MediaWorkflowJobActionsHelperCustom = get_custom_class(
    "MediaWorkflowJobActionsHelperCustom"
)


class ResourceHelper(
    MediaWorkflowJobActionsHelperCustom, MediaWorkflowJobActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            media_workflow_job_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="media_workflow_job",
        service_client_class=MediaServicesClient,
        namespace="media_services",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
