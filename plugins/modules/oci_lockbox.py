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
module: oci_lockbox
short_description: Manage a Lockbox resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Lockbox resource in Oracle Cloud Infrastructure
    - For I(state=present), creates a new Lockbox.
    - "This resource has the following action operations in the M(oracle.oci.oci_lockbox_actions) module: change_compartment."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    resource_id:
        description:
            - The unique identifier (OCID) of the customer's resource.
            - Required for create using I(state=present).
        type: str
    lockbox_partner:
        description:
            - The partner using this lockbox to lock a resource.
            - Required for create using I(state=present).
        type: str
        choices:
            - "FAAAS"
            - "CANARY"
    compartment_id:
        description:
            - The unique identifier (OCID) of the compartment where the resource is located.
            - Required for create using I(state=present).
        type: str
    partner_compartment_id:
        description:
            - Compartment Identifier
            - Required for create using I(state=present).
        type: str
    access_context_attributes:
        description:
            - ""
            - Required for create using I(state=present).
        type: dict
        suboptions:
            items:
                description:
                    - List of context attributes.
                type: list
                elements: dict
                required: true
                suboptions:
                    name:
                        description:
                            - The name of the context attribute
                        type: str
                        required: true
                    description:
                        description:
                            - The description of the context attribute
                        type: str
                    default_value:
                        description:
                            - An optional default value used when access request context value is not provided
                        type: str
    display_name:
        description:
            - Lockbox Identifier
            - Required for create, update, delete when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
            - This parameter is updatable when C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["name"]
    approval_template_id:
        description:
            - Approval template ID
            - This parameter is updatable.
        type: str
    max_access_duration:
        description:
            - The maximum amount of time operator has access to associated resources.
            - This parameter is updatable.
        type: str
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
    lockbox_id:
        description:
            - unique Lockbox identifier
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
            - Required for delete using I(state=absent) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Lockbox.
            - Use I(state=present) to create or update a Lockbox.
            - Use I(state=absent) to delete a Lockbox.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create lockbox
  oci_lockbox:
    # required
    resource_id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    lockbox_partner: FAAAS
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    partner_compartment_id: "ocid1.partnercompartment.oc1..xxxxxxEXAMPLExxxxxx"
    access_context_attributes:
      # required
      items:
      - # required
        name: name_example

        # optional
        description: description_example
        default_value: default_value_example

    # optional
    display_name: display_name_example
    approval_template_id: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"
    max_access_duration: max_access_duration_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update lockbox
  oci_lockbox:
    # required
    lockbox_id: "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    approval_template_id: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"
    max_access_duration: max_access_duration_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update lockbox using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_lockbox:
    # required
    display_name: display_name_example

    # optional
    approval_template_id: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"
    max_access_duration: max_access_duration_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Delete lockbox
  oci_lockbox:
    # required
    lockbox_id: "ocid1.lockbox.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

- name: Delete lockbox using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_lockbox:
    # required
    display_name: display_name_example
    state: absent

"""

RETURN = """
lockbox:
    description:
        - Details of the Lockbox resource acted upon by the current operation
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
                - Lockbox Identifier, can be renamed
            returned: on success
            type: str
            sample: display_name_example
        compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        partner_compartment_id:
            description:
                - Compartment Identifier
            returned: on success
            type: str
            sample: "ocid1.partnercompartment.oc1..xxxxxxEXAMPLExxxxxx"
        resource_id:
            description:
                - The unique identifier (OCID) of associated resource that the lockbox is created for.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lockbox_partner:
            description:
                - The partner using this lockbox to lock a resource.
            returned: on success
            type: str
            sample: FAAAS
        time_created:
            description:
                - The time the the Lockbox was created. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the Lockbox was updated. An RFC3339 formatted datetime string
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the Lockbox.
            returned: on success
            type: str
            sample: ACTIVE
        access_context_attributes:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                items:
                    description:
                        - List of context attributes.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of the context attribute
                            returned: on success
                            type: str
                            sample: name_example
                        description:
                            description:
                                - The description of the context attribute
                            returned: on success
                            type: str
                            sample: description_example
                        default_value:
                            description:
                                - An optional default value used when access request context value is not provided
                            returned: on success
                            type: str
                            sample: default_value_example
        approval_template_id:
            description:
                - Approval template ID
            returned: on success
            type: str
            sample: "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx"
        max_access_duration:
            description:
                - The maximum amount of time operator has access to associated resources.
            returned: on success
            type: str
            sample: max_access_duration_example
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed
                  state.
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "partner_compartment_id": "ocid1.partnercompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lockbox_partner": "FAAAS",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "access_context_attributes": {
            "items": [{
                "name": "name_example",
                "description": "description_example",
                "default_value": "default_value_example"
            }]
        },
        "approval_template_id": "ocid1.approvaltemplate.oc1..xxxxxxEXAMPLExxxxxx",
        "max_access_duration": "max_access_duration_example",
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
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.lockbox import LockboxClient
    from oci.lockbox.models import CreateLockboxDetails
    from oci.lockbox.models import UpdateLockboxDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class LockboxHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_possible_entity_types(self):
        return super(LockboxHelperGen, self).get_possible_entity_types() + [
            "lockbox",
            "lockboxes",
            "lockboxlockbox",
            "lockboxlockboxes",
            "lockboxresource",
            "lockboxesresource",
        ]

    def get_module_resource_id_param(self):
        return "lockbox_id"

    def get_module_resource_id(self):
        return self.module.params.get("lockbox_id")

    def get_get_fn(self):
        return self.client.get_lockbox

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_lockbox, lockbox_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_lockbox, lockbox_id=self.module.params.get("lockbox_id"),
        )

    def get_required_kwargs_for_list(self):
        return dict()

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
            "resource_id",
            "lockbox_partner",
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
        return oci_common_utils.list_all_resources(self.client.list_lockboxes, **kwargs)

    def get_create_model_class(self):
        return CreateLockboxDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_lockbox,
            call_fn_args=(),
            call_fn_kwargs=dict(create_lockbox_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def get_update_model_class(self):
        return UpdateLockboxDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_lockbox,
            call_fn_args=(),
            call_fn_kwargs=dict(
                lockbox_id=self.module.params.get("lockbox_id"),
                update_lockbox_details=update_details,
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
            call_fn=self.client.delete_lockbox,
            call_fn_args=(),
            call_fn_kwargs=dict(lockbox_id=self.module.params.get("lockbox_id"),),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


LockboxHelperCustom = get_custom_class("LockboxHelperCustom")


class ResourceHelper(LockboxHelperCustom, LockboxHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            resource_id=dict(type="str"),
            lockbox_partner=dict(type="str", choices=["FAAAS", "CANARY"]),
            compartment_id=dict(type="str"),
            partner_compartment_id=dict(type="str"),
            access_context_attributes=dict(
                type="dict",
                options=dict(
                    items=dict(
                        type="list",
                        elements="dict",
                        required=True,
                        options=dict(
                            name=dict(type="str", required=True),
                            description=dict(type="str"),
                            default_value=dict(type="str"),
                        ),
                    )
                ),
            ),
            display_name=dict(aliases=["name"], type="str"),
            approval_template_id=dict(type="str"),
            max_access_duration=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            lockbox_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="lockbox",
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
