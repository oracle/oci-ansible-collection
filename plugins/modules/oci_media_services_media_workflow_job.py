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
module: oci_media_services_media_workflow_job
short_description: Manage a MediaWorkflowJob resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a MediaWorkflowJob resource in Oracle Cloud Infrastructure
    - For I(state=present), run the MediaWorkflow according to the given mediaWorkflow definition and configuration.
    - "This resource has the following action operations in the M(oracle.oci.oci_media_services_media_workflow_job_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    media_workflow_name:
        description:
            - Name of the system MediaWorkflow that should be run.
            - Applicable when workflow_identifier_type is 'NAME'
        type: str
    workflow_identifier_type:
        description:
            - Discriminate identification of a workflow by name versus a workflow by ID.
            - Required for create using I(state=present).
        type: str
        choices:
            - "NAME"
            - "ID"
    media_workflow_configuration_ids:
        description:
            - Configurations to be applied to this run of the workflow.
        type: list
        elements: str
    compartment_id:
        description:
            - ID of the compartment in which the job should be created.
            - Required for create using I(state=present).
        type: str
    parameters:
        description:
            - Parameters that override parameters specified in MediaWorkflowTaskDeclarations, the MediaWorkflow,
              the MediaWorkflow's MediaWorkflowConfigurations and the MediaWorkflowConfigurations of this
              MediaWorkflowJob. The parameters are given as JSON. The top level and 2nd level elements must be
              JSON objects (vs arrays, scalars, etc). The top level keys refer to a task's key and the 2nd level
              keys refer to a parameter's name.
        type: dict
    media_workflow_id:
        description:
            - OCID of the MediaWorkflow that should be run.
            - Applicable when workflow_identifier_type is 'ID'
        type: str
    display_name:
        description:
            - Name of the Media Workflow Job. Does not have to be unique. Avoid entering confidential information.
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
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
    media_workflow_job_id:
        description:
            - Unique MediaWorkflowJob identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the MediaWorkflowJob.
            - Use I(state=present) to create or update a MediaWorkflowJob.
            - Use I(state=absent) to delete a MediaWorkflowJob.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create media_workflow_job with workflow_identifier_type = NAME
  oci_media_services_media_workflow_job:
    # required
    workflow_identifier_type: NAME
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    media_workflow_name: media_workflow_name_example
    media_workflow_configuration_ids: [ "media_workflow_configuration_ids_example" ]
    parameters: null
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create media_workflow_job with workflow_identifier_type = ID
  oci_media_services_media_workflow_job:
    # required
    workflow_identifier_type: ID
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    media_workflow_configuration_ids: [ "media_workflow_configuration_ids_example" ]
    parameters: null
    media_workflow_id: "ocid1.mediaworkflow.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update media_workflow_job
  oci_media_services_media_workflow_job:
    # required
    media_workflow_job_id: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update media_workflow_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_media_workflow_job:
    # required
    display_name: display_name_example

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete media_workflow_job
  oci_media_services_media_workflow_job:
    # required
    media_workflow_job_id: "ocid1.mediaworkflowjob.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete media_workflow_job using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_media_workflow_job:
    # required
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.media_services import MediaServicesClient
    from oci.media_services.models import CreateMediaWorkflowJobDetails
    from oci.media_services.models import UpdateMediaWorkflowJobDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaWorkflowJobHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(MediaWorkflowJobHelperGen, self).get_possible_entity_types() + [
            "mediaworkflowjob",
            "mediaworkflowjobs",
            "mediaServicesmediaworkflowjob",
            "mediaServicesmediaworkflowjobs",
            "mediaworkflowjobresource",
            "mediaworkflowjobsresource",
            "mediaservices",
        ]

    def get_module_resource_id_param(self):
        return "media_workflow_job_id"

    def get_module_resource_id(self):
        return self.module.params.get("media_workflow_job_id")

    def get_get_fn(self):
        return self.client.get_media_workflow_job

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow_job, media_workflow_job_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow_job,
            media_workflow_job_id=self.module.params.get("media_workflow_job_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "media_workflow_id",
            "display_name",
        ]

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
            self.client.list_media_workflow_jobs, **kwargs
        )

    def get_create_model_class(self):
        return CreateMediaWorkflowJobDetails

    def get_exclude_attributes(self):
        return ["workflow_identifier_type", "media_workflow_name"]

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_media_workflow_job,
            call_fn_args=(),
            call_fn_kwargs=dict(create_media_workflow_job_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateMediaWorkflowJobDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_media_workflow_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_workflow_job_id=self.module.params.get("media_workflow_job_id"),
                update_media_workflow_job_details=update_details,
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
            call_fn=self.client.delete_media_workflow_job,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_workflow_job_id=self.module.params.get("media_workflow_job_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MediaWorkflowJobHelperCustom = get_custom_class("MediaWorkflowJobHelperCustom")


class ResourceHelper(MediaWorkflowJobHelperCustom, MediaWorkflowJobHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            media_workflow_name=dict(type="str"),
            workflow_identifier_type=dict(type="str", choices=["NAME", "ID"]),
            media_workflow_configuration_ids=dict(type="list", elements="str"),
            compartment_id=dict(type="str"),
            parameters=dict(type="dict"),
            media_workflow_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            media_workflow_job_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
