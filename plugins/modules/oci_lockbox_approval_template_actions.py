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
module: oci_lockbox_approval_template_actions
short_description: Perform actions on an ApprovalTemplate resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an ApprovalTemplate resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves an ApprovalTemplate resource from one compartment identifier to another. When provided, If-Match is checked
      against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    approval_template_id:
        description:
            - The unique identifier (OCID) of the approval template.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The unique identifier (OCID) of the compartment where the resource is located.
        type: str
        required: true
    action:
        description:
            - The action to perform on the ApprovalTemplate.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on approval_template
  oci_lockbox_approval_template_actions:
    # required
    approval_template_id: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
approval_template:
    description:
        - Details of the ApprovalTemplate resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier (OCID) of the approval template, which can't be changed after creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The approval template display name.
            returned: on success
            type: str
            sample: display_name_example
        lifecycle_state:
            description:
                - The current state of the approval template.
            returned: on success
            type: str
            sample: ACTIVE
        approver_levels:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                level1:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        approver_type:
                            description:
                                - The approver type of this approver level.
                            returned: on success
                            type: str
                            sample: GROUP
                        approver_id:
                            description:
                                - The group or user ocid of the approver for this approver level.
                            returned: on success
                            type: str
                            sample: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
                level2:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        approver_type:
                            description:
                                - The approver type of this approver level.
                            returned: on success
                            type: str
                            sample: GROUP
                        approver_id:
                            description:
                                - The group or user ocid of the approver for this approver level.
                            returned: on success
                            type: str
                            sample: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
                level3:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        approver_type:
                            description:
                                - The approver type of this approver level.
                            returned: on success
                            type: str
                            sample: GROUP
                        approver_id:
                            description:
                                - The group or user ocid of the approver for this approver level.
                            returned: on success
                            type: str
                            sample: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The unique identifier (OCID) of the customer compartment where the approval template is located.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        auto_approval_state:
            description:
                - The auto approval state of the lockbox.
            returned: on success
            type: str
            sample: ENABLED
        time_created:
            description:
                - The time the the approval template was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the approval template was updated. An RFC3339 formatted datetime string
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
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "lifecycle_state": "ACTIVE",
        "approver_levels": {
            "level1": {
                "approver_type": "GROUP",
                "approver_id": "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "level2": {
                "approver_type": "GROUP",
                "approver_id": "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
            },
            "level3": {
                "approver_type": "GROUP",
                "approver_id": "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
            }
        },
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "auto_approval_state": "ENABLED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
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
    from oci.lockbox import LockboxClient
    from oci.lockbox.models import ChangeApprovalTemplateCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApprovalTemplateActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "approval_template_id"

    def get_module_resource_id(self):
        return self.module.params.get("approval_template_id")

    def get_get_fn(self):
        return self.client.get_approval_template

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_approval_template,
            approval_template_id=self.module.params.get("approval_template_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeApprovalTemplateCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_approval_template_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                approval_template_id=self.module.params.get("approval_template_id"),
                change_approval_template_compartment_details=action_details,
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


ApprovalTemplateActionsHelperCustom = get_custom_class(
    "ApprovalTemplateActionsHelperCustom"
)


class ResourceHelper(
    ApprovalTemplateActionsHelperCustom, ApprovalTemplateActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            approval_template_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="approval_template",
        service_client_class=LockboxClient,
        namespace="lockbox",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
