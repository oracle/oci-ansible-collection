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
module: oci_media_services_media_workflow_configuration
short_description: Manage a MediaWorkflowConfiguration resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a MediaWorkflowConfiguration resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new MediaWorkflowConfiguration.
    - "This resource has the following action operations in the M(oracle.oci.oci_media_services_media_workflow_configuration_actions) module:
      change_compartment."
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
            - MediaWorkflowConfiguration identifier. Avoid entering confidential information.
            - Required for create using I(state=present).
            - Required for update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    parameters:
        description:
            - Reuseable parameter values encoded as a JSON; the top and second level JSON elements are
              objects. Each key of the top level object refers to a task key that is unqiue to the
              workflow, each of the second level objects' keys refer to the name of a parameter that is
              unique to the task. taskKey -> parameterName -> parameterValue
            - Required for create using I(state=present).
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
    media_workflow_configuration_id:
        description:
            - Unique MediaWorkflowConfiguration identifier.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the MediaWorkflowConfiguration.
            - Use I(state=present) to create or update a MediaWorkflowConfiguration.
            - Use I(state=absent) to delete a MediaWorkflowConfiguration.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create media_workflow_configuration
  oci_media_services_media_workflow_configuration:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    parameters: null

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update media_workflow_configuration
  oci_media_services_media_workflow_configuration:
    # required
    media_workflow_configuration_id: "ocid1.mediaworkflowconfiguration.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    parameters: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update media_workflow_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_media_workflow_configuration:
    # required
    display_name: display_name_example

    # optional
    parameters: null
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete media_workflow_configuration
  oci_media_services_media_workflow_configuration:
    # required
    media_workflow_configuration_id: "ocid1.mediaworkflowconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete media_workflow_configuration using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_media_services_media_workflow_configuration:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
media_workflow_configuration:
    description:
        - Details of the MediaWorkflowConfiguration resource acted upon by the current operation
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
                - Display name for the MediaWorkflowConfiguration. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        parameters:
            description:
                - Reuseable parameter values encoded as a JSON; the top and second level JSON elements are
                  objects. Each key of the top level object refer to a task key that is unqiue to the
                  workflow, each of the second level objects' keys refer to the name of a parameter that is
                  unique to the task. taskKey -> parameterName -> parameterValue
            returned: on success
            type: dict
            sample: {}
        time_created:
            description:
                - The time when the the MediaWorkflowConfiguration was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the MediaWorkflowConfiguration was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the MediaWorkflowConfiguration.
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
        "parameters": {},
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "lifecyle_details": "lifecyle_details_example",
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
    from oci.media_services.models import CreateMediaWorkflowConfigurationDetails
    from oci.media_services.models import UpdateMediaWorkflowConfigurationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaWorkflowConfigurationHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(
            MediaWorkflowConfigurationHelperGen, self
        ).get_possible_entity_types() + [
            "mediaworkflowconfiguration",
            "mediaworkflowconfigurations",
            "mediaServicesmediaworkflowconfiguration",
            "mediaServicesmediaworkflowconfigurations",
            "mediaworkflowconfigurationresource",
            "mediaworkflowconfigurationsresource",
            "mediaservices",
        ]

    def get_module_resource_id_param(self):
        return "media_workflow_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("media_workflow_configuration_id")

    def get_get_fn(self):
        return self.client.get_media_workflow_configuration

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow_configuration,
            media_workflow_configuration_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow_configuration,
            media_workflow_configuration_id=self.module.params.get(
                "media_workflow_configuration_id"
            ),
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
            self.client.list_media_workflow_configurations, **kwargs
        )

    def get_create_model_class(self):
        return CreateMediaWorkflowConfigurationDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_media_workflow_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                create_media_workflow_configuration_details=create_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateMediaWorkflowConfigurationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_media_workflow_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_workflow_configuration_id=self.module.params.get(
                    "media_workflow_configuration_id"
                ),
                update_media_workflow_configuration_details=update_details,
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
            call_fn=self.client.delete_media_workflow_configuration,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_workflow_configuration_id=self.module.params.get(
                    "media_workflow_configuration_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


MediaWorkflowConfigurationHelperCustom = get_custom_class(
    "MediaWorkflowConfigurationHelperCustom"
)


class ResourceHelper(
    MediaWorkflowConfigurationHelperCustom, MediaWorkflowConfigurationHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            parameters=dict(type="dict"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            media_workflow_configuration_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="media_workflow_configuration",
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
