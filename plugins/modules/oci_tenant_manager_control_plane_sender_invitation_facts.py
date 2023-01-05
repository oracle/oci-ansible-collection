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
module: oci_tenant_manager_control_plane_sender_invitation_facts
short_description: Fetches details about one or multiple SenderInvitation resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SenderInvitation resources in Oracle Cloud Infrastructure
    - Return a (paginated) list of sender invitations.
    - If I(sender_invitation_id) is specified, the details of a single SenderInvitation will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    sender_invitation_id:
        description:
            - OCID of the sender invitation to retrieve.
            - Required to get a specific sender_invitation.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The ID of the compartment in which to list resources.
            - Required to list multiple sender_invitations.
        type: str
    recipient_tenancy_id:
        description:
            - The tenancy that the invitation is addressed to.
        type: str
    lifecycle_state:
        description:
            - The lifecycle state of the resource.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "INACTIVE"
            - "UPDATING"
            - "FAILED"
            - "TERMINATED"
    status:
        description:
            - The status of the sender invitation.
        type: str
        choices:
            - "PENDING"
            - "CANCELED"
            - "ACCEPTED"
            - "EXPIRED"
            - "FAILED"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
        aliases: ["name"]
    sort_by:
        description:
            - "The field to sort by. Only one sort order can be provided.
              * The default order for timeCreated is descending.
              * The default order for displayName is ascending.
              * If no value is specified, timeCreated is the default."
        type: str
        choices:
            - "timeCreated"
            - "displayName"
    sort_order:
        description:
            - The sort order to use, whether 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific sender_invitation
  oci_tenant_manager_control_plane_sender_invitation_facts:
    # required
    sender_invitation_id: "ocid1.senderinvitation.oc1..xxxxxxEXAMPLExxxxxx"

- name: List sender_invitations
  oci_tenant_manager_control_plane_sender_invitation_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    recipient_tenancy_id: "ocid1.recipienttenancy.oc1..xxxxxxEXAMPLExxxxxx"
    lifecycle_state: CREATING
    status: PENDING
    display_name: display_name_example
    sort_by: timeCreated
    sort_order: ASC

"""

RETURN = """
sender_invitations:
    description:
        - List of SenderInvitation resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - OCID of the sender invitation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID of the sender tenancy.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-created name to describe the invitation. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        recipient_invitation_id:
            description:
                - OCID of the corresponding recipient invitation.
            returned: on success
            type: str
            sample: "ocid1.recipientinvitation.oc1..xxxxxxEXAMPLExxxxxx"
        recipient_tenancy_id:
            description:
                - OCID of the recipient tenancy.
            returned: on success
            type: str
            sample: "ocid1.recipienttenancy.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - Lifecycle state of the sender invitation.
            returned: on success
            type: str
            sample: CREATING
        status:
            description:
                - Status of the sender invitation.
            returned: on success
            type: str
            sample: PENDING
        time_created:
            description:
                - Date-time when this sender invitation was created.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Date-time when this sender invitation was last updated.
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
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "recipient_invitation_id": "ocid1.recipientinvitation.oc1..xxxxxxEXAMPLExxxxxx",
        "recipient_tenancy_id": "ocid1.recipienttenancy.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "CREATING",
        "status": "PENDING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "recipient_email_address": "recipient_email_address_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import SenderInvitationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SenderInvitationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "sender_invitation_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sender_invitation,
            sender_invitation_id=self.module.params.get("sender_invitation_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "recipient_tenancy_id",
            "lifecycle_state",
            "status",
            "display_name",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_sender_invitations,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SenderInvitationFactsHelperCustom = get_custom_class(
    "SenderInvitationFactsHelperCustom"
)


class ResourceFactsHelper(
    SenderInvitationFactsHelperCustom, SenderInvitationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            sender_invitation_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            recipient_tenancy_id=dict(type="str"),
            lifecycle_state=dict(
                type="str",
                choices=[
                    "CREATING",
                    "ACTIVE",
                    "INACTIVE",
                    "UPDATING",
                    "FAILED",
                    "TERMINATED",
                ],
            ),
            status=dict(
                type="str",
                choices=["PENDING", "CANCELED", "ACCEPTED", "EXPIRED", "FAILED"],
            ),
            display_name=dict(aliases=["name"], type="str"),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sender_invitation",
        service_client_class=SenderInvitationClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(sender_invitations=result)


if __name__ == "__main__":
    main()
