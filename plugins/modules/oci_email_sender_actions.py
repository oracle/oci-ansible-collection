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
module: oci_email_sender_actions
short_description: Perform actions on a Sender resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Sender resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a sender into a different compartment. When provided, If-Match is checked against ETag values of the resource.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    sender_id:
        description:
            - The unique OCID of the sender.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment
              into which the sender should be moved.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Sender.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action change_compartment on sender
  oci_email_sender_actions:
    # required
    sender_id: "ocid1.sender.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
sender:
    description:
        - Details of the Sender resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID for the compartment.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        email_address:
            description:
                - Email address of the sender.
            returned: on success
            type: str
            sample: email_address_example
        id:
            description:
                - The unique OCID of the sender.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        is_spf:
            description:
                - Value of the SPF field. For more information about SPF, please see
                  L(SPF Authentication,https://docs.us-phoenix-1.oraclecloud.com/Content/Email/Concepts/overview.htm#components).
            returned: on success
            type: bool
            sample: true
        lifecycle_state:
            description:
                - The sender's current lifecycle state.
            returned: on success
            type: str
            sample: CREATING
        time_created:
            description:
                - "The date and time the approved sender was added in \\"YYYY-MM-ddThh:mmZ\\"
                  format with a Z offset, as defined by RFC 3339."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        email_domain_id:
            description:
                - The email domain used to assert responsibility for emails sent from this sender.
            returned: on success
            type: str
            sample: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "email_address": "email_address_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_spf": true,
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "email_domain_id": "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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
    from oci.email import EmailClient
    from oci.email.models import ChangeSenderCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SenderActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "sender_id"

    def get_module_resource_id(self):
        return self.module.params.get("sender_id")

    def get_get_fn(self):
        return self.client.get_sender

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sender, sender_id=self.module.params.get("sender_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeSenderCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_sender_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                sender_id=self.module.params.get("sender_id"),
                change_sender_compartment_details=action_details,
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


SenderActionsHelperCustom = get_custom_class("SenderActionsHelperCustom")


class ResourceHelper(SenderActionsHelperCustom, SenderActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            sender_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="sender",
        service_client_class=EmailClient,
        namespace="email",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
