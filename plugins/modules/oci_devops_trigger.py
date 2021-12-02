#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_devops_trigger
short_description: Manage a Trigger resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Trigger resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Trigger.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    display_name:
        description:
            - Name of the Trigger
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    description:
        description:
            - Optional description about the Trigger
            - This parameter is updatable.
        type: str
    project_id:
        description:
            - Project to which the Trigger will belong
            - Required for create using I(state=present).
        type: str
    trigger_source:
        description:
            - "Source of the Trigger (allowed values are - GITHUB, GITLAB)"
            - Required for create using I(state=present), update using I(state=present) with trigger_id present.
        type: str
        choices:
            - "GITHUB"
            - "DEVOPS_CODE_REPOSITORY"
            - "GITLAB"
    actions:
        description:
            - The list of actions that are to be performed for this Trigger
            - Required for create using I(state=present).
            - This parameter is updatable.
            - Applicable when trigger_source is one of ['DEVOPS_CODE_REPOSITORY', 'GITHUB', 'GITLAB']
        type: list
        elements: dict
        suboptions:
            type:
                description:
                    - "The type of action that will be taken (allowed value - TRIGGER_BUILD_PIPELINE)"
                type: str
                choices:
                    - "TRIGGER_BUILD_PIPELINE"
                required: true
            filter:
                description:
                    - ""
                type: dict
                suboptions:
                    trigger_source:
                        description:
                            - "Source of the Trigger (allowed values are - GITHUB, GITLAB)"
                        type: str
                        choices:
                            - "DEVOPS_CODE_REPOSITORY"
                            - "GITLAB"
                            - "GITHUB"
                        required: true
                    events:
                        description:
                            - The events, only support PUSH at this time
                        type: list
                        elements: str
                        choices:
                            - "PUSH"
                            - "PULL_REQUEST_CREATED"
                            - "PULL_REQUEST_UPDATED"
                            - "PULL_REQUEST_REOPENED"
                            - "PULL_REQUEST_MERGED"
                    include:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            head_ref:
                                description:
                                    - Branch for push event
                                type: str
                            base_ref:
                                description:
                                    - The target branch for pull requests; not applicable for push
                                    - Applicable when trigger_source is one of ['GITHUB', 'GITLAB']
                                type: str
            build_pipeline_id:
                description:
                    - The id of the build pipeline to be triggered
                type: str
                required: true
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
    repository_id:
        description:
            - The Devops Code Repository Id
            - This parameter is updatable.
            - Applicable when trigger_source is 'DEVOPS_CODE_REPOSITORY'
        type: str
    trigger_id:
        description:
            - unique Trigger identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Trigger.
            - Use I(state=present) to create or update a Trigger.
            - Use I(state=absent) to delete a Trigger.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create trigger with trigger_source = GITHUB
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: GITHUB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Create trigger with trigger_source = DEVOPS_CODE_REPOSITORY
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: DEVOPS_CODE_REPOSITORY

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

- name: Create trigger with trigger_source = GITLAB
  oci_devops_trigger:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    trigger_source: GITLAB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger with trigger_source = GITHUB
  oci_devops_trigger:
    # required
    trigger_source: GITHUB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger with trigger_source = DEVOPS_CODE_REPOSITORY
  oci_devops_trigger:
    # required
    trigger_source: DEVOPS_CODE_REPOSITORY

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger with trigger_source = GITLAB
  oci_devops_trigger:
    # required
    trigger_source: GITLAB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = GITHUB
  oci_devops_trigger:
    # required
    trigger_source: GITHUB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = DEVOPS_CODE_REPOSITORY
  oci_devops_trigger:
    # required
    trigger_source: DEVOPS_CODE_REPOSITORY

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}
    repository_id: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"

- name: Update trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set) with trigger_source = GITLAB
  oci_devops_trigger:
    # required
    trigger_source: GITLAB

    # optional
    display_name: display_name_example
    description: description_example
    actions:
    - # required
      type: TRIGGER_BUILD_PIPELINE
      build_pipeline_id: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"

      # optional
      filter:
        # required
        trigger_source: DEVOPS_CODE_REPOSITORY

        # optional
        events: [ "null" ]
        include:
          # optional
          head_ref: head_ref_example
          base_ref: base_ref_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete trigger
  oci_devops_trigger:
    # required
    trigger_id: "ocid1.trigger.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete trigger using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_devops_trigger:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
trigger:
    description:
        - Details of the Trigger resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - Name for Trigger.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - Description about the Trigger
            returned: on success
            type: str
            sample: description_example
        project_id:
            description:
                - Project to which the Trigger belongs
            returned: on success
            type: str
            sample: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - Compartment to which the Trigger belongs
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_source:
            description:
                - "Source of the Trigger (allowed values are - GITHUB, GITLAB)"
            returned: on success
            type: str
            sample: GITHUB
        time_created:
            description:
                - The time the the Trigger was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Trigger was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Trigger.
            returned: on success
            type: str
            sample: ACTIVE
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        actions:
            description:
                - The list of actions that are to be performed for this Trigger
            returned: on success
            type: complex
            contains:
                type:
                    description:
                        - "The type of action that will be taken (allowed value - TRIGGER_BUILD_PIPELINE)"
                    returned: on success
                    type: str
                    sample: TRIGGER_BUILD_PIPELINE
                filter:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        trigger_source:
                            description:
                                - "Source of the Trigger (allowed values are - GITHUB, GITLAB)"
                            returned: on success
                            type: str
                            sample: DEVOPS_CODE_REPOSITORY
                        events:
                            description:
                                - The events, only support PUSH at this time
                            returned: on success
                            type: list
                            sample: []
                        include:
                            description:
                                - ""
                            returned: on success
                            type: complex
                            contains:
                                head_ref:
                                    description:
                                        - Branch for push event
                                    returned: on success
                                    type: str
                                    sample: head_ref_example
                                base_ref:
                                    description:
                                        - The target branch for pull requests; not applicable for push
                                    returned: on success
                                    type: str
                                    sample: base_ref_example
                build_pipeline_id:
                    description:
                        - The id of the build pipeline to be triggered
                    returned: on success
                    type: str
                    sample: "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
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
        repository_id:
            description:
                - The OCID of OCI Devops Repository
            returned: on success
            type: str
            sample: "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx"
        trigger_url:
            description:
                - The endpoint which listens to Trigger events
            returned: on success
            type: str
            sample: trigger_url_example
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "project_id": "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "trigger_source": "GITHUB",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecycle_details": "lifecycle_details_example",
        "actions": [{
            "type": "TRIGGER_BUILD_PIPELINE",
            "filter": {
                "trigger_source": "DEVOPS_CODE_REPOSITORY",
                "events": [],
                "include": {
                    "head_ref": "head_ref_example",
                    "base_ref": "base_ref_example"
                }
            },
            "build_pipeline_id": "ocid1.buildpipeline.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {},
        "repository_id": "ocid1.repository.oc1..xxxxxxEXAMPLExxxxxx",
        "trigger_url": "trigger_url_example"
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
    from oci.devops.models import CreateTriggerDetails
    from oci.devops.models import UpdateTriggerDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TriggerHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "trigger_id"

    def get_module_resource_id(self):
        return self.module.params.get("trigger_id")

    def get_get_fn(self):
        return self.client.get_trigger

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_trigger, trigger_id=self.module.params.get("trigger_id"),
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
        return oci_common_utils.list_all_resources(self.client.list_triggers, **kwargs)

    def get_create_model_class(self):
        return CreateTriggerDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(create_trigger_details=create_details,),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def get_update_model_class(self):
        return UpdateTriggerDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(
                trigger_id=self.module.params.get("trigger_id"),
                update_trigger_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_trigger,
            call_fn_args=(),
            call_fn_kwargs=dict(trigger_id=self.module.params.get("trigger_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


TriggerHelperCustom = get_custom_class("TriggerHelperCustom")


class ResourceHelper(TriggerHelperCustom, TriggerHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            display_name=dict(aliases=["name"], type="str"),
            description=dict(type="str"),
            project_id=dict(type="str"),
            trigger_source=dict(
                type="str", choices=["GITHUB", "DEVOPS_CODE_REPOSITORY", "GITLAB"]
            ),
            actions=dict(
                type="list",
                elements="dict",
                options=dict(
                    type=dict(
                        type="str", required=True, choices=["TRIGGER_BUILD_PIPELINE"]
                    ),
                    filter=dict(
                        type="dict",
                        options=dict(
                            trigger_source=dict(
                                type="str",
                                required=True,
                                choices=["DEVOPS_CODE_REPOSITORY", "GITLAB", "GITHUB"],
                            ),
                            events=dict(
                                type="list",
                                elements="str",
                                choices=[
                                    "PUSH",
                                    "PULL_REQUEST_CREATED",
                                    "PULL_REQUEST_UPDATED",
                                    "PULL_REQUEST_REOPENED",
                                    "PULL_REQUEST_MERGED",
                                ],
                            ),
                            include=dict(
                                type="dict",
                                options=dict(
                                    head_ref=dict(type="str"), base_ref=dict(type="str")
                                ),
                            ),
                        ),
                    ),
                    build_pipeline_id=dict(type="str", required=True),
                ),
            ),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            repository_id=dict(type="str"),
            trigger_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="trigger",
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
