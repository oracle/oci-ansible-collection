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
module: oci_ons_subscription_confirmation_facts
short_description: Fetches details about a SubscriptionConfirmation resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a SubscriptionConfirmation resource in Oracle Cloud Infrastructure
    - Gets the confirmation details for the specified subscription.
    - "Transactions Per Minute (TPM) per-tenancy limit for this operation: 60."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subscription to get the confirmation details for.
        type: str
        required: true
    token:
        description:
            - The subscription confirmation token.
        type: str
        required: true
    protocol:
        description:
            - The protocol used for the subscription.
            - "Allowed values:
                * `CUSTOM_HTTPS`
                * `EMAIL`
                * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`)
                * `ORACLE_FUNCTIONS`
                * `PAGERDUTY`
                * `SLACK`
                * `SMS`"
            - For information about subscription protocols, see
              L(To create a subscription,https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm#createSub).
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific subscription_confirmation
  oci_ons_subscription_confirmation_facts:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    token: token_example
    protocol: protocol_example

"""

RETURN = """
subscription_confirmation:
    description:
        - SubscriptionConfirmation resource
    returned: on success
    type: complex
    contains:
        topic_name:
            description:
                - The name of the subscribed topic.
            returned: on success
            type: str
            sample: topic_name_example
        topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic associated with the specified
                  subscription.
            returned: on success
            type: str
            sample: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
        endpoint:
            description:
                - A locator that corresponds to the subscription protocol.
                  For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.
            returned: on success
            type: str
            sample: endpoint_example
        unsubscribe_url:
            description:
                - The URL for unsubscribing from the topic.
            returned: on success
            type: str
            sample: unsubscribe_url_example
        message:
            description:
                - A human-readable string indicating the status of the subscription confirmation.
            returned: on success
            type: str
            sample: message_example
        subscription_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subscription specified in the request.
            returned: on success
            type: str
            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    sample: {
        "topic_name": "topic_name_example",
        "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
        "endpoint": "endpoint_example",
        "unsubscribe_url": "unsubscribe_url_example",
        "message": "message_example",
        "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.ons import NotificationDataPlaneClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionConfirmationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "id",
            "token",
            "protocol",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_confirm_subscription,
            id=self.module.params.get("id"),
            token=self.module.params.get("token"),
            protocol=self.module.params.get("protocol"),
        )


SubscriptionConfirmationFactsHelperCustom = get_custom_class(
    "SubscriptionConfirmationFactsHelperCustom"
)


class ResourceFactsHelper(
    SubscriptionConfirmationFactsHelperCustom, SubscriptionConfirmationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            id=dict(type="str", required=True),
            token=dict(type="str", required=True, no_log=True),
            protocol=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="subscription_confirmation",
        service_client_class=NotificationDataPlaneClient,
        namespace="ons",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(subscription_confirmation=result)


if __name__ == "__main__":
    main()
