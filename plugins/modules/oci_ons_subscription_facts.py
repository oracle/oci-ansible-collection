#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_ons_subscription_facts
short_description: Fetches details about one or multiple Subscription resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Subscription resources in Oracle Cloud Infrastructure
    - Lists the subscriptions in the specified compartment or topic.
    - "Transactions Per Minute (TPM) per-tenancy limit for this operation: 60."
    - If I(subscription_id) is specified, the details of a single Subscription will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    subscription_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subscription to retrieve.
            - Required to get a specific subscription.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
            - Required to list multiple subscriptions.
        type: str
    topic_id:
        description:
            - Return all subscriptions that are subscribed to the given topic OCID. Either this query parameter or the compartmentId query parameter must be
              set.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List subscriptions
  oci_ons_subscription_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx

- name: Get a specific subscription
  oci_ons_subscription_facts:
    subscription_id: ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
subscriptions:
    description:
        - List of Subscription resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subscription.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated topic.
            returned: on success
            type: string
            sample: ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx
        protocol:
            description:
                - The protocol used for the subscription.
                  For information about subscription protocols, see
                  L(To create a subscription,https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm#createSub).
            returned: on success
            type: string
            sample: EMAIL
        endpoint:
            description:
                - A locator that corresponds to the subscription protocol.
                  For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.
            returned: on success
            type: string
            sample: endpoint_example
        lifecycle_state:
            description:
                - The lifecycle state of the subscription. The status of a new subscription is PENDING; when confirmed, the subscription status changes to
                  ACTIVE.
            returned: on success
            type: string
            sample: PENDING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment for the subscription.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        created_time:
            description:
                - The time when this suscription was created.
            returned: on success
            type: int
            sample: 56
        deliver_policy:
            description:
                - The delivery policy of the subscription. Stored as a JSON string.
            returned: on success
            type: string
            sample: deliver_policy_example
        etag:
            description:
                - For optimistic concurrency control. See `if-match`.
            returned: on success
            type: string
            sample: etag_example
        freeform_tags:
            description:
                - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
                  L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        delivery_policy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                backoff_retry_policy:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        max_retry_duration:
                            description:
                                - The maximum retry duration in milliseconds. Default value is `7200000` (2 hours).
                            returned: on success
                            type: int
                            sample: 56
                        policy_type:
                            description:
                                - The type of delivery policy.
                            returned: on success
                            type: string
                            sample: EXPONENTIAL
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
        "protocol": "EMAIL",
        "endpoint": "endpoint_example",
        "lifecycle_state": "PENDING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "created_time": 56,
        "deliver_policy": "deliver_policy_example",
        "etag": "etag_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "delivery_policy": {
            "backoff_retry_policy": {
                "max_retry_duration": 56,
                "policy_type": "EXPONENTIAL"
            }
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.ons import NotificationDataPlaneClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "subscription_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription,
            subscription_id=self.module.params.get("subscription_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "topic_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_subscriptions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


SubscriptionFactsHelperCustom = get_custom_class("SubscriptionFactsHelperCustom")


class ResourceFactsHelper(SubscriptionFactsHelperCustom, SubscriptionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            subscription_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            topic_id=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="subscription",
        service_client_class=NotificationDataPlaneClient,
        namespace="ons",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(subscriptions=result)


if __name__ == "__main__":
    main()
