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
module: oci_tenant_manager_control_plane_recipient_invitation_actions
short_description: Perform actions on a RecipientInvitation resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a RecipientInvitation resource in Oracle Cloud Infrastructure
    - For I(action=accept), accepts a recipient invitation.
    - For I(action=ignore), ignores a recipient invitation.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    recipient_invitation_id:
        description:
            - OCID of recipient invitation to accept.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the RecipientInvitation.
        type: str
        required: true
        choices:
            - "accept"
            - "ignore"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action accept on recipient_invitation
  oci_tenant_manager_control_plane_recipient_invitation_actions:
    # required
    recipient_invitation_id: "ocid1.recipientinvitation.oc1..xxxxxxEXAMPLExxxxxx"
    action: accept

- name: Perform action ignore on recipient_invitation
  oci_tenant_manager_control_plane_recipient_invitation_actions:
    # required
    recipient_invitation_id: "ocid1.recipientinvitation.oc1..xxxxxxEXAMPLExxxxxx"
    action: ignore

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
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.tenant_manager_control_plane import WorkRequestClient
    from oci.tenant_manager_control_plane import RecipientInvitationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RecipientInvitationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        accept
        ignore
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "recipient_invitation_id"

    def get_module_resource_id(self):
        return self.module.params.get("recipient_invitation_id")

    def get_get_fn(self):
        return self.client.get_recipient_invitation

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_recipient_invitation,
            recipient_invitation_id=self.module.params.get("recipient_invitation_id"),
        )

    def accept(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.accept_recipient_invitation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                recipient_invitation_id=self.module.params.get(
                    "recipient_invitation_id"
                ),
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

    def ignore(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.ignore_recipient_invitation,
            call_fn_args=(),
            call_fn_kwargs=dict(
                recipient_invitation_id=self.module.params.get(
                    "recipient_invitation_id"
                ),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
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


RecipientInvitationActionsHelperCustom = get_custom_class(
    "RecipientInvitationActionsHelperCustom"
)


class ResourceHelper(
    RecipientInvitationActionsHelperCustom, RecipientInvitationActionsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            recipient_invitation_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["accept", "ignore"]),
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

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
