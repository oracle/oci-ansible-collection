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
module: oci_ons_subscription_actions
short_description: Perform actions on a Subscription resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Subscription resource in Oracle Cloud Infrastructure
    - "For I(action=get_unsubscription), unsubscribes the subscription from the topic.
      Transactions Per Minute (TPM) per-tenancy limit for this operation: 60."
    - "For I(action=resend_subscription_confirmation), resends the confirmation details for the specified subscription.
      Transactions Per Minute (TPM) per-tenancy limit for this operation: 60."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    token:
        description:
            - The subscription confirmation token.
            - Required for I(action=get_unsubscription).
        type: str
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
            - Required for I(action=get_unsubscription).
        type: str
    id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subscription to unsubscribe from.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Subscription.
        type: str
        required: true
        choices:
            - "get_unsubscription"
            - "resend_subscription_confirmation"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action get_unsubscription on subscription
  oci_ons_subscription_actions:
    # required
    token: token_example
    protocol: protocol_example
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    action: get_unsubscription

- name: Perform action resend_subscription_confirmation on subscription
  oci_ons_subscription_actions:
    # required
    id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
    action: resend_subscription_confirmation

"""

RETURN = """
subscription:
    description:
        - Details of the Subscription resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subscription.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        topic_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the associated topic.
            returned: on success
            type: str
            sample: "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx"
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
            returned: on success
            type: str
            sample: protocol_example
        endpoint:
            description:
                - A locator that corresponds to the subscription protocol.
                  For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.
            returned: on success
            type: str
            sample: endpoint_example
        lifecycle_state:
            description:
                - The lifecycle state of the subscription. The status of a new subscription is PENDING; when confirmed, the subscription status changes to
                  ACTIVE.
            returned: on success
            type: str
            sample: PENDING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment for the subscription.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
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
            type: str
            sample: deliver_policy_example
        etag:
            description:
                - For optimistic concurrency control. See `if-match`.
            returned: on success
            type: str
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
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "topic_id": "ocid1.topic.oc1..xxxxxxEXAMPLExxxxxx",
        "protocol": "protocol_example",
        "endpoint": "endpoint_example",
        "lifecycle_state": "PENDING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "created_time": 56,
        "deliver_policy": "deliver_policy_example",
        "etag": "etag_example",
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
    from oci.ons import NotificationDataPlaneClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        get_unsubscription
        resend_subscription_confirmation
    """

    @staticmethod
    def get_module_resource_id_param():
        return "id"

    def get_module_resource_id(self):
        return self.module.params.get("id")

    def get_get_fn(self):
        return self.client.get_subscription

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription,
            subscription_id=self.module.params.get("subscription_id"),
        )

    def get_unsubscription(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.get_unsubscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                id=self.module.params.get("id"),
                token=self.module.params.get("token"),
                protocol=self.module.params.get("protocol"),
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

    def resend_subscription_confirmation(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.resend_subscription_confirmation,
            call_fn_args=(),
            call_fn_kwargs=dict(id=self.module.params.get("id"),),
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


SubscriptionActionsHelperCustom = get_custom_class("SubscriptionActionsHelperCustom")


class ResourceHelper(SubscriptionActionsHelperCustom, SubscriptionActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            token=dict(type="str", no_log=True),
            protocol=dict(type="str"),
            id=dict(type="str", required=True),
            action=dict(
                type="str",
                required=True,
                choices=["get_unsubscription", "resend_subscription_confirmation"],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="subscription",
        service_client_class=NotificationDataPlaneClient,
        namespace="ons",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
