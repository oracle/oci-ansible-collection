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
module: oci_media_services_media_workflow_configuration_actions
short_description: Perform actions on a MediaWorkflowConfiguration resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a MediaWorkflowConfiguration resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a MediaWorkflowConfiguration resource from one compartment identifier to another. When provided, If-Match is
      checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    media_workflow_configuration_id:
        description:
            - Unique MediaWorkflowConfiguration identifier.
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
            - The action to perform on the MediaWorkflowConfiguration.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on media_workflow_configuration
  oci_media_services_media_workflow_configuration_actions:
    # required
    media_workflow_configuration_id: "ocid1.mediaworkflowconfiguration.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.media_services import MediaServicesClient
    from oci.media_services.models import (
        ChangeMediaWorkflowConfigurationCompartmentDetails,
    )

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class MediaWorkflowConfigurationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "media_workflow_configuration_id"

    def get_module_resource_id(self):
        return self.module.params.get("media_workflow_configuration_id")

    def get_get_fn(self):
        return self.client.get_media_workflow_configuration

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_media_workflow_configuration,
            media_workflow_configuration_id=self.module.params.get(
                "media_workflow_configuration_id"
            ),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeMediaWorkflowConfigurationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_media_workflow_configuration_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                media_workflow_configuration_id=self.module.params.get(
                    "media_workflow_configuration_id"
                ),
                change_media_workflow_configuration_compartment_details=action_details,
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


MediaWorkflowConfigurationActionsHelperCustom = get_custom_class(
    "MediaWorkflowConfigurationActionsHelperCustom"
)


class ResourceHelper(
    MediaWorkflowConfigurationActionsHelperCustom,
    MediaWorkflowConfigurationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            media_workflow_configuration_id=dict(
                aliases=["id"], type="str", required=True
            ),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
