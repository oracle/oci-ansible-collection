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
module: oci_tenant_manager_control_plane_recipient_invitation
short_description: Manage a RecipientInvitation resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a RecipientInvitation resource in Oracle Cloud Infrastructure
    - "This resource has the following action operations in the M(oracle.oci.oci_tenant_manager_control_plane_recipient_invitation_actions) module: accept,
      ignore."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    recipient_invitation_id:
        description:
            - OCID of the recipient invitation to update.
            - Required for update using I(state=present) when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is not set.
        type: str
        aliases: ["id"]
    display_name:
        description:
            - A user-created name to describe the invitation. Avoid entering confidential information.
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
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
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required for update when environment variable C(OCI_USE_NAME_AS_IDENTIFIER) is set.
        type: str
    state:
        description:
            - The state of the RecipientInvitation.
            - Use I(state=present) to update an existing a RecipientInvitation.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update recipient_invitation
  oci_tenant_manager_control_plane_recipient_invitation:
    # required
    recipient_invitation_id: "ocid1.recipientinvitation.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

- name: Update recipient_invitation using name (when environment variable OCI_USE_NAME_AS_IDENTIFIER is set)
  oci_tenant_manager_control_plane_recipient_invitation:
    # required
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    freeform_tags: {'Department': 'Finance'}
    defined_tags: {'Operations': {'CostCenter': 'US'}}

"""

RETURN = """
recipient_invitation:
    description:
        - Details of the RecipientInvitation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the recipient invitation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID of the recipient tenancy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        subjects:
            description:
                - The list of subjects the invitation contains.
            returned: on success
            type: list
            sample: []
        sender_invitation_id:
            description:
                - OCID of the corresponding sender invitation.
            returned: on success
            type: str
            sample: "ocid1.senderinvitation.oc1..xxxxxxEXAMPLExxxxxx"
        sender_tenancy_id:
            description:
                - OCID of the sender tenancy.
            returned: on success
            type: str
            sample: "ocid1.sendertenancy.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the recipient invitation.
            returned: on success
            type: str
            sample: CREATING
        status:
            description:
                - Status of the recipient invitation.
            returned: on success
            type: str
            sample: PENDING
        display_name:
            description:
                - A user-created name to describe the invitation. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - Date and time when the recipient invitation was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date and time when the recipient invitation was last updated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        recipient_email_address:
            description:
                - Email address of the recipient.
            returned: on success
            type: str
            sample: recipient_email_address_example
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
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "subjects": [],
        "sender_invitation_id": "ocid1.senderinvitation.oc1..xxxxxxEXAMPLExxxxxx",
        "sender_tenancy_id": "ocid1.sendertenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "status": "PENDING",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "recipient_email_address": "recipient_email_address_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import WorkRequestClient
    from oci.tenant_manager_control_plane import RecipientInvitationClient
    from oci.tenant_manager_control_plane.models import UpdateRecipientInvitationDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RecipientInvitationHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    def get_possible_entity_types(self):
        return super(RecipientInvitationHelperGen, self).get_possible_entity_types() + [
            "recipientinvitation",
            "recipientinvitations",
            "tenantManagerControlPlanerecipientinvitation",
            "tenantManagerControlPlanerecipientinvitations",
            "recipientinvitationresource",
            "recipientinvitationsresource",
            "tenantmanagercontrolplane",
        ]

    def get_module_resource_id_param(self):
        return "recipient_invitation_id"

    def get_module_resource_id(self):
        return self.module.params.get("recipient_invitation_id")

    def get_get_fn(self):
        return self.client.get_recipient_invitation

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_recipient_invitation,
            recipient_invitation_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_recipient_invitation,
            recipient_invitation_id=self.module.params.get("recipient_invitation_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_recipient_invitations, **kwargs
        )

    def get_update_model_class(self):
        return UpdateRecipientInvitationDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_recipient_invitation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                recipient_invitation_id=self.module.params.get(
                    "recipient_invitation_id"
                ),
                update_recipient_invitation_details=update_details,
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


RecipientInvitationHelperCustom = get_custom_class("RecipientInvitationHelperCustom")


class ResourceHelper(RecipientInvitationHelperCustom, RecipientInvitationHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            recipient_invitation_id=dict(aliases=["id"], type="str"),
            display_name=dict(aliases=["name"], type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            compartment_id=dict(type="str"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="recipient_invitation",
        service_client_class=RecipientInvitationClient,
        namespace="tenant_manager_control_plane",
    )

    result = dict(changed=False)

    if resource_helper.is_update_using_name():
        result = resource_helper.update_using_name()
    elif resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
