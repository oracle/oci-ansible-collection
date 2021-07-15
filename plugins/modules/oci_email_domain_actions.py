#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_email_domain_actions
short_description: Perform actions on an EmailDomain resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an EmailDomain resource in Oracle Cloud Infrastructure
    - "For I(action=change_compartment), moves a email domain into a different compartment.
      When provided, If-Match is checked against ETag value of the resource.
      For information about moving resources between compartments, see
      L(Moving Resources to a Different Compartment,https://docs.cloud.oracle.com/iaas/Content/Identity/Tasks/managingcompartments.htm#moveRes).
      **Note:** All Dkim objects associated with this email domain will also be moved into the provided compartment."
version_added: "2.9"
author: Oracle (@oracle)
options:
    email_domain_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of this email domain.
        type: str
        aliases: ["id"]
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the specified
              resource to.
        type: str
        required: true
    action:
        description:
            - The action to perform on the EmailDomain.
        type: str
        required: true
        choices:
            - "change_compartment"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on email_domain
  oci_email_domain_actions:
    email_domain_id: "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

"""

RETURN = """
email_domain:
    description:
        - Details of the EmailDomain resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the email domain in the Internet Domain Name System (DNS).
                - "Example: `example.net`"
            returned: on success
            type: string
            sample: example.net
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the email domain.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains this email domain.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The current state of the email domain.
            returned: on success
            type: string
            sample: ACTIVE
        active_dkim_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the DKIM key
                  that will be used to sign mail sent from this email domain.
            returned: on success
            type: string
            sample: "ocid1.activedkim.oc1..xxxxxxEXAMPLExxxxxx"
        is_spf:
            description:
                - Value of the SPF field. For more information about SPF, please see
                  L(SPF Authentication,https://docs.cloud.oracle.com/iaas/Content/Email/Concepts/overview.htm#components).
            returned: on success
            type: bool
            sample: true
        description:
            description:
                - The description of a email domain.
            returned: on success
            type: string
            sample: description_example
        time_created:
            description:
                - "The time the email domain was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format, \\"YYYY-MM-ddThh:mmZ\\"."
                - "Example: `2021-02-12T22:47:12.613Z`"
            returned: on success
            type: string
            sample: 2021-02-12T22:47:12.613Z
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
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "name": "example.net",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "active_dkim_id": "ocid1.activedkim.oc1..xxxxxxEXAMPLExxxxxx",
        "is_spf": true,
        "description": "description_example",
        "time_created": "2021-02-12T22:47:12.613Z",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.email import EmailClient
    from oci.email.models import ChangeEmailDomainCompartmentDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class EmailDomainActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
    """

    @staticmethod
    def get_module_resource_id_param():
        return "email_domain_id"

    def get_module_resource_id(self):
        return self.module.params.get("email_domain_id")

    def get_get_fn(self):
        return self.client.get_email_domain

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_email_domain,
            email_domain_id=self.module.params.get("email_domain_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeEmailDomainCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_email_domain_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                email_domain_id=self.module.params.get("email_domain_id"),
                change_email_domain_compartment_details=action_details,
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


EmailDomainActionsHelperCustom = get_custom_class("EmailDomainActionsHelperCustom")


class ResourceHelper(EmailDomainActionsHelperCustom, EmailDomainActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            email_domain_id=dict(aliases=["id"], type="str", required=True),
            compartment_id=dict(type="str", required=True),
            action=dict(type="str", required=True, choices=["change_compartment"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="email_domain",
        service_client_class=EmailClient,
        namespace="email",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
