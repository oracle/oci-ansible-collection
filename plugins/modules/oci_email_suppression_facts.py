#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_email_suppression_facts
short_description: Fetches details about one or multiple Suppression resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Suppression resources in Oracle Cloud Infrastructure
    - Gets a list of suppressed recipient email addresses for a user. The
      `compartmentId` for suppressions must be a tenancy OCID. The returned list
      is sorted by creation time in descending order.
    - If I(suppression_id) is specified, the details of a single Suppression will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    suppression_id:
        description:
            - The unique OCID of the suppression.
            - Required to get a specific suppression.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID for the compartment.
            - Required to list multiple suppressions.
        type: str
    email_address:
        description:
            - The email address of the suppression.
        type: str
    time_created_greater_than_or_equal_to:
        description:
            - "Search for suppressions that were created within a specific date range,
              using this parameter to specify the earliest creation date for the
              returned list (inclusive). Specifying this parameter without the
              corresponding `timeCreatedLessThan` parameter will retrieve suppressions created from the
              given `timeCreatedGreaterThanOrEqualTo` to the current time, in \\"YYYY-MM-ddThh:mmZ\\" format with a
              Z offset, as defined by RFC 3339."
            - "**Example:** 2016-12-19T16:39:57.600Z"
        type: str
    time_created_less_than:
        description:
            - "Search for suppressions that were created within a specific date range,
              using this parameter to specify the latest creation date for the returned
              list (exclusive). Specifying this parameter without the corresponding
              `timeCreatedGreaterThanOrEqualTo` parameter will retrieve all suppressions created before the
              specified end date, in \\"YYYY-MM-ddThh:mmZ\\" format with a Z offset, as
              defined by RFC 3339."
            - "**Example:** 2016-12-19T16:39:57.600Z"
        type: str
    sort_by:
        description:
            - The field to sort by. The `TIMECREATED` value returns the list in in
              descending order by default. The `EMAILADDRESS` value returns the list in
              ascending order by default. Use the `SortOrderQueryParam` to change the
              direction of the returned list of items.
        type: str
        choices:
            - "TIMECREATED"
            - "EMAILADDRESS"
    sort_order:
        description:
            - The sort order to use, either ascending or descending order.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List suppressions
  oci_email_suppression_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific suppression
  oci_email_suppression_facts:
    suppression_id: "ocid1.suppression.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
suppressions:
    description:
        - List of Suppression resources
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
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "email_address": "email_address_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "reason": "UNKNOWN",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_last_suppressed": "2013-10-20T19:20:30+01:00",
        "message_id": "ocid1.message.oc1..xxxxxxEXAMPLExxxxxx",
        "error_detail": "error_detail_example",
        "error_source": "error_source_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.email import EmailClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SuppressionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "suppression_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_suppression,
            suppression_id=self.module.params.get("suppression_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "email_address",
            "time_created_greater_than_or_equal_to",
            "time_created_less_than",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_suppressions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SuppressionFactsHelperCustom = get_custom_class("SuppressionFactsHelperCustom")


class ResourceFactsHelper(SuppressionFactsHelperCustom, SuppressionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            suppression_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            email_address=dict(type="str"),
            time_created_greater_than_or_equal_to=dict(type="str"),
            time_created_less_than=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "EMAILADDRESS"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="suppression",
        service_client_class=EmailClient,
        namespace="email",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(suppressions=result)


if __name__ == "__main__":
    main()
