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
module: oci_devops_project_actions
short_description: Perform actions on a Project resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Project resource in Oracle Cloud Infrastructure
    - For I(action=cancel_scheduled_cascading_project_deletion), cascading operation that restores Project and child resources from a DELETING state to an
      active state
    - For I(action=change_compartment), moves a project resource from one compartment OCID to another.
    - For I(action=schedule_cascading_project_deletion), cascading operation that marks Project and child DevOps resources in a DELETING state for a retention
      period
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment to which the resource must be moved.
            - Required for I(action=change_compartment).
        type: str
    project_id:
        description:
            - Unique project identifier.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Project.
        type: str
        required: true
        choices:
            - "cancel_scheduled_cascading_project_deletion"
            - "change_compartment"
            - "schedule_cascading_project_deletion"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action cancel_scheduled_cascading_project_deletion on project
  oci_devops_project_actions:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    action: cancel_scheduled_cascading_project_deletion

- name: Perform action change_compartment on project
  oci_devops_project_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action schedule_cascading_project_deletion on project
  oci_devops_project_actions:
    # required
    project_id: "ocid1.project.oc1..xxxxxxEXAMPLExxxxxx"
    action: schedule_cascading_project_deletion

"""

RETURN = """
project:
    description:
        - Details of the Project resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Project name (case-sensitive).
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Project description.
            returned: on success
            type: str
            sample: description_example
        compartment_id:
            description:
                - The OCID of the compartment where the project is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        namespace:
            description:
                - Namespace associated with the project.
            returned: on success
            type: str
            sample: namespace_example
        notification_config:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                topic_id:
                    description:
                        - The topic ID for notifications.
                    returned: on success
                    type: str
                    sample: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Time the project was created. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Time the project was updated. Format defined by L(RFC3339,https://datatracker.ietf.org/doc/html/rfc3339).
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the project.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "namespace": "namespace_example",
        "notification_config": {
            "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
        },
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "lifecycle_details_example",
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
    from oci.devops import DevopsClient
    from oci.devops.models import ChangeProjectCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DevopsProjectActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        cancel_scheduled_cascading_project_deletion
        change_compartment
        schedule_cascading_project_deletion
    """

    @staticmethod
    def get_module_resource_id_param():
        return "project_id"

    def get_module_resource_id(self):
        return self.module.params.get("project_id")

    def get_get_fn(self):
        return self.client.get_project

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_project, project_id=self.module.params.get("project_id"),
        )

    def cancel_scheduled_cascading_project_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.cancel_scheduled_cascading_project_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(project_id=self.module.params.get("project_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeProjectCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_project_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                project_id=self.module.params.get("project_id"),
                change_project_compartment_details=action_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )

    def schedule_cascading_project_deletion(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.schedule_cascading_project_deletion,
            call_fn_args=(),
            call_fn_kwargs=dict(project_id=self.module.params.get("project_id"),),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


DevopsProjectActionsHelperCustom = get_custom_class("DevopsProjectActionsHelperCustom")


class ResourceHelper(DevopsProjectActionsHelperCustom, DevopsProjectActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            project_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "cancel_scheduled_cascading_project_deletion",
                    "change_compartment",
                    "schedule_cascading_project_deletion",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="project",
        service_client_class=DevopsClient,
        namespace="devops",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
