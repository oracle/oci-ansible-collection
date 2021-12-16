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
module: oci_email_sender_facts
short_description: Fetches details about one or multiple Sender resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Sender resources in Oracle Cloud Infrastructure
    - Gets a collection of approved sender email addresses and sender IDs.
    - If I(sender_id) is specified, the details of a single Sender will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    sender_id:
        description:
            - The unique OCID of the sender.
            - Required to get a specific sender.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID for the compartment.
            - Required to list multiple senders.
        type: str
    lifecycle_state:
        description:
            - The current state of a sender.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "DELETED"
    domain:
        description:
            - A filter to only return resources that match the given domain exactly.
        type: str
    email_address:
        description:
            - The email address of the approved sender.
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
- name: Get a specific sender
  oci_email_sender_facts:
    # required
    sender_id: "ocid1.sender.oc1..xxxxxxEXAMPLExxxxxx"

- name: List senders
  oci_email_sender_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    lifecycle_state: CREATING
    domain: domain_example
    email_address: email_address_example
    sort_by: TIMECREATED
    sort_order: ASC

"""

RETURN = """
senders:
    description:
        - List of Sender resources
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
                - Returned for get operation
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
                - Returned for get operation
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
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "email_address": "email_address_example",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "is_spf": true,
        "lifecycle_state": "CREATING",
        "time_created": "2013-10-20T19:20:30+01:00",
        "email_domain_id": "ocid1.emaildomain.oc1..xxxxxxEXAMPLExxxxxx",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
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


class SenderFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "sender_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_sender, sender_id=self.module.params.get("sender_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "lifecycle_state",
            "domain",
            "email_address",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_senders,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SenderFactsHelperCustom = get_custom_class("SenderFactsHelperCustom")


class ResourceFactsHelper(SenderFactsHelperCustom, SenderFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            sender_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            lifecycle_state=dict(
                type="str", choices=["CREATING", "ACTIVE", "DELETING", "DELETED"]
            ),
            domain=dict(type="str"),
            email_address=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "EMAILADDRESS"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="sender",
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

    module.exit_json(senders=result)


if __name__ == "__main__":
    main()
