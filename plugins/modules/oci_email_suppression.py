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
module: oci_email_suppression
short_description: Manage a Suppression resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create and delete a Suppression resource in Oracle Cloud Infrastructure
    - "For I(state=present), adds recipient email addresses to the suppression list for a tenancy.
      Addresses added to the suppression list via the API are denoted as
      \\"MANUAL\\" in the `reason` field. *Note:* All email addresses added to the
      suppression list are normalized to include only lowercase letters."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to contain the suppression. Since
              suppressions are at the customer level, this must be the tenancy
              OCID.
            - Required for create using I(state=present).
        type: str
    email_address:
        description:
            - The recipient email address of the suppression.
            - Required for create using I(state=present).
        type: str
    suppression_id:
        description:
            - The unique OCID of the suppression.
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    state:
        description:
            - The state of the Suppression.
            - Use I(state=present) to create a Suppression.
            - Use I(state=absent) to delete a Suppression.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource ]
"""

EXAMPLES = """
- name: Create suppression
  oci_email_suppression:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    email_address: email_address_example

- name: Delete suppression
  oci_email_suppression:
    # required
    suppression_id: "ocid1.suppression.oc1..xxxxxxEXAMPLExxxxxx"
    state: absent

"""

RETURN = """
suppression:
    description:
        - Details of the Suppression resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The OCID of the compartment to contain the suppression. Since
                  suppressions are at the customer level, this must be the tenancy
                  OCID.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        email_address:
            description:
                - Email address of the suppression.
            returned: on success
            type: str
            sample: email_address_example
        id:
            description:
                - The unique ID of the suppression.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        reason:
            description:
                - The reason that the email address was suppressed. For more information on the types of bounces, see L(Suppression List,https://docs.us-
                  phoenix-1.oraclecloud.com/Content/Email/Concepts/overview.htm#components).
            returned: on success
            type: str
            sample: UNKNOWN
        time_created:
            description:
                - "The date and time the suppression was added in \\"YYYY-MM-ddThh:mmZ\\"
                  format with a Z offset, as defined by RFC 3339."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_last_suppressed:
            description:
                - "The last date and time the suppression prevented submission
                  in \\"YYYY-MM-ddThh:mmZ\\"
                  format with a Z offset, as defined by RFC 3339."
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        message_id:
            description:
                - The value of the Message-ID header from the email that triggered a suppression.
                  This value is as defined in RFC 5322 section 3.6.4, excluding angle-brackets.
                  Not provided for all types of suppressions.
            returned: on success
            type: str
            sample: "ocid1.message.oc1..xxxxxxEXAMPLExxxxxx"
        error_detail:
            description:
                - The specific error message returned by a system that resulted in the suppression.
                  This message is usually an SMTP error code with additional descriptive text.
                  Not provided for all types of suppressions.
            returned: on success
            type: str
            sample: error_detail_example
        error_source:
            description:
                - DNS name of the source of the error that caused the suppression.
                  Will be set to either the remote-mta or reporting-mta field from a delivery status notification (RFC 3464) when available.
                  Not provided for all types of suppressions, and not always known.
                - "Note: Most SMTP errors that cause suppressions come from software run by email receiving systems rather than from OCI email delivery itself."
            returned: on success
            type: str
            sample: error_source_example
    sample: {
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "email_address": "email_address_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "reason": "UNKNOWN",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_suppressed": "2013-10-20T19:20:30+01:00",
        "message_id": "ocid1.message.oc1..xxxxxxEXAMPLExxxxxx",
        "error_detail": "error_detail_example",
        "error_source": "error_source_example"
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
    from oci.email import EmailClient
    from oci.email.models import CreateSuppressionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SuppressionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, get, list and delete"""

    def get_possible_entity_types(self):
        return super(SuppressionHelperGen, self).get_possible_entity_types() + [
            "suppression",
            "suppressions",
            "emailsuppression",
            "emailsuppressions",
            "suppressionresource",
            "suppressionsresource",
            "email",
        ]

    def get_module_resource_id_param(self):
        return "suppression_id"

    def get_module_resource_id(self):
        return self.module.params.get("suppression_id")

    def get_get_fn(self):
        return self.client.get_suppression

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_suppression, suppression_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_suppression,
            suppression_id=self.module.params.get("suppression_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["email_address"]

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
            self.client.list_suppressions, **kwargs
        )

    def get_create_model_class(self):
        return CreateSuppressionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_suppression,
            call_fn_args=(),
            call_fn_kwargs=dict(create_suppression_details=create_details,),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.CREATE_OPERATION_KEY,
            ),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_suppression,
            call_fn_args=(),
            call_fn_kwargs=dict(
                suppression_id=self.module.params.get("suppression_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.DELETE_OPERATION_KEY,
            ),
        )


SuppressionHelperCustom = get_custom_class("SuppressionHelperCustom")


class ResourceHelper(SuppressionHelperCustom, SuppressionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=False
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            email_address=dict(type="str"),
            suppression_id=dict(aliases=["id"], type="str"),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="suppression",
        service_client_class=EmailClient,
        namespace="email",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
