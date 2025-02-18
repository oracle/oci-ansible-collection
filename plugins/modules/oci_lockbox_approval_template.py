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
module: oci_lockbox_approval_template
short_description: Manage an ApprovalTemplate resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete an ApprovalTemplate resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new approval template.
    - "This resource has the following action operations in the M(oracle.oci.oci_lockbox_approval_template_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier (OCID) of the compartment where the resource is located.
            - Required for create using I(state=present).
        type: str
    approver_levels:
        description:
            - ""
            - Required for create using I(state=present).
            - This parameter is updatable.
        type: dict
        suboptions:
            level1:
                description:
                    - ""
                type: dict
                required: true
                suboptions:
                    approver_type:
                        description:
                            - The approver type of this approver level.
                        type: str
                        choices:
                            - "GROUP"
                            - "USER"
                        required: true
                    approver_id:
                        description:
                            - The group or user ocid of the approver for this approver level.
                        type: str
                        required: true
            level2:
                description:
                    - ""
                type: dict
                suboptions:
                    approver_type:
                        description:
                            - The approver type of this approver level.
                        type: str
                        choices:
                            - "GROUP"
                            - "USER"
                        required: true
                    approver_id:
                        description:
                            - The group or user ocid of the approver for this approver level.
                        type: str
                        required: true
            level3:
                description:
                    - ""
                type: dict
                suboptions:
                    approver_type:
                        description:
                            - The approver type of this approver level.
                        type: str
                        choices:
                            - "GROUP"
                            - "USER"
                        required: true
                    approver_id:
                        description:
                            - The group or user ocid of the approver for this approver level.
                        type: str
                        required: true
    display_name:
        description:
            - approval template identifier
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    auto_approval_state:
        description:
            - The auto approval state of the lockbox.
            - This parameter is updatable.
        type: str
        choices:
            - "ENABLED"
            - "DISABLED"
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
    approval_template_id:
        description:
            - The unique identifier (OCID) of the approval template.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the ApprovalTemplate.
            - Use I(state=present) to create or update an ApprovalTemplate.
            - Use I(state=absent) to delete an ApprovalTemplate.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create approval_template
  oci_lockbox_approval_template:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    approver_levels:
      # required
      level1:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
      level2:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
      level3:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    auto_approval_state: ENABLED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update approval_template
  oci_lockbox_approval_template:
    # required
    approval_template_id: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    approver_levels:
      # required
      level1:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
      level2:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
      level3:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
    display_name: display_name_example
    auto_approval_state: ENABLED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update approval_template using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_lockbox_approval_template:
    # required
    display_name: display_name_example

    # optional
    approver_levels:
      # required
      level1:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"

        # optional
      level2:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
      level3:
        # required
        approver_type: GROUP
        approver_id: "ocid1.approver.oc1..xxxxxxEXAMPLExxxxxx"
    auto_approval_state: ENABLED
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete approval_template
  oci_lockbox_approval_template:
    # required
    approval_template_id: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete approval_template using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_lockbox_approval_template:
    # required
    display_name: display_name_example
    state: absent

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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.lockbox import LockboxClient
    from oci.lockbox.models import CreateApprovalTemplateDetails
    from oci.lockbox.models import UpdateApprovalTemplateDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApprovalTemplateHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(ApprovalTemplateHelperGen, self).get_possible_entity_types() + [
            "lockboxapprovaltemplate",
            "lockboxapprovaltemplates",
            "lockboxlockboxapprovaltemplate",
            "lockboxlockboxapprovaltemplates",
            "lockboxapprovaltemplateresource",
            "lockboxapprovaltemplatesresource",
            "approvaltemplate",
            "approvaltemplates",
            "approvaltemplateresource",
            "approvaltemplatesresource",
            "lockbox",
        ]

    def get_module_resource_id_param(self):
        return "approval_template_id"

    def get_module_resource_id(self):
        return self.module.params.get("approval_template_id")

    def get_get_fn(self):
        return self.client.get_approval_template

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_approval_template, approval_template_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_approval_template,
            approval_template_id=self.module.params.get("approval_template_id"),
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
            self.client.list_approval_templates, **kwargs
        )

    def get_create_model_class(self):
        return CreateApprovalTemplateDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_approval_template,
            call_fn_args=(),
            call_fn_kwargs=dict(create_approval_template_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateApprovalTemplateDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_approval_template,
            call_fn_args=(),
            call_fn_kwargs=dict(
                approval_template_id=self.module.params.get("approval_template_id"),
                update_approval_template_details=update_details,
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
            call_fn=self.client.delete_approval_template,
            call_fn_args=(),
            call_fn_kwargs=dict(
                approval_template_id=self.module.params.get("approval_template_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


ApprovalTemplateHelperCustom = get_custom_class("ApprovalTemplateHelperCustom")


class ResourceHelper(ApprovalTemplateHelperCustom, ApprovalTemplateHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            approver_levels=dict(
                type="dict",
                options=dict(
                    level1=dict(
                        type="dict",
                        required=True,
                        options=dict(
                            approver_type=dict(
                                type="str", required=True, choices=["GROUP", "USER"]
                            ),
                            approver_id=dict(type="str", required=True),
                        ),
                    ),
                    level2=dict(
                        type="dict",
                        options=dict(
                            approver_type=dict(
                                type="str", required=True, choices=["GROUP", "USER"]
                            ),
                            approver_id=dict(type="str", required=True),
                        ),
                    ),
                    level3=dict(
                        type="dict",
                        options=dict(
                            approver_type=dict(
                                type="str", required=True, choices=["GROUP", "USER"]
                            ),
                            approver_id=dict(type="str", required=True),
                        ),
                    ),
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            auto_approval_state=dict(type="str", choices=["ENABLED", "DISABLED"]),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            approval_template_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
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
