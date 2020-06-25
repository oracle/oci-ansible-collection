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
module: oci_ons_subscription
short_description: Manage a Subscription resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to create, update and delete a Subscription resource in Oracle Cloud Infrastructure
    - "For I(state=present), creates a subscription for the specified topic and sends a subscription confirmation URL to the endpoint. The subscription remains
      in \\"Pending\\" status until it has been confirmed.
      For information about confirming subscriptions, see
      L(To confirm a subscription,https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm#confirmSub)."
    - "Transactions Per Minute (TPM) per-tenancy limit for this operation: 60."
    - "This resource has the following action operations in the M(oci_subscription_actions) module: get_unsubscription, resend_subscription_confirmation."
version_added: "2.9"
author: Oracle (@oracle)
options:
    topic_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the topic for the subscription.
            - Required for create using I(state=present).
        type: str
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment for the subscription.
            - Required for create using I(state=present).
        type: str
    protocol:
        description:
            - The protocol used for the subscription.
            - "Allowed values:
                * `CUSTOM_HTTPS`
                * `EMAIL`
                * `HTTPS` (deprecated; for PagerDuty endpoints, use `PAGERDUTY`)
                * `PAGERDUTY`
                * `SLACK`"
            - For information about subscription protocols, see
              L(To create a subscription,https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm#createSub).
            - Required for create using I(state=present).
        type: str
    endpoint:
        description:
            - "A locator that corresponds to the subscription protocol.
              For example, an email address for a subscription that uses the `EMAIL` protocol, or a URL for a subscription that uses an HTTP-based protocol.
              HTTP-based protocols use URL endpoints that begin with \\"http:\\" or \\"https:\\".
              A URL cannot exceed 512 characters.
              Avoid entering confidential information."
            - For protocol-specific endpoint formats and steps to get or create endpoints, see
              L(To create a subscription,https://docs.cloud.oracle.com/iaas/Content/Notification/Tasks/managingtopicsandsubscriptions.htm#createSub).
            - Required for create using I(state=present).
        type: str
    metadata:
        description:
            - Metadata for the subscription.
        type: str
    freeform_tags:
        description:
            - Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see
              L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Department\\": \\"Finance\\"}`"
        type: dict
    defined_tags:
        description:
            - Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see L(Resource
              Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
            - "Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
        type: dict
    subscription_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the subscription to update.
            - Required for update using I(state=present).
            - Required for delete using I(state=absent).
        type: str
        aliases: ["id"]
    delivery_policy:
        description:
            - The delivery policy of the subscription. Stored as a JSON string.
        type: dict
        suboptions:
            backoff_retry_policy:
                description:
                    - ""
                type: dict
                suboptions:
                    max_retry_duration:
                        description:
                            - The maximum retry duration in milliseconds. Default value is `7200000` (2 hours).
                        type: int
                        required: true
                    policy_type:
                        description:
                            - The type of delivery policy.
                        type: str
                        choices:
                            - "EXPONENTIAL"
                        required: true
    state:
        description:
            - The state of the Subscription.
            - Use I(state=present) to create or update a Subscription.
            - Use I(state=absent) to delete a Subscription.
        type: str
        required: false
        default: 'present'
        choices: ["present", "absent"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_creatable_resource, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Create subscription
  oci_ons_subscription:
    topic_id: topic_OCID
    compartment_id: compartment_OCID
    protocol: EMAIL
    endpoint: john.smith@example.com

- name: Update subscription
  oci_ons_subscription:
    freeform_tags: '{''Department'': ''Finance''}'
    subscription_id: ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx

- name: Delete subscription
  oci_ons_subscription:
    subscription_id: ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx
    state: absent

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
    sample: {
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
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.ons import NotificationDataPlaneClient
    from oci.ons.models import CreateSubscriptionDetails
    from oci.ons.models import UpdateSubscriptionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionHelperGen(OCIResourceHelperBase):
    """Supported operations: create, update, get, list and delete"""

    def get_module_resource_id_param(self):
        return "subscription_id"

    def get_module_resource_id(self):
        return self.module.params.get("subscription_id")

    def get_get_fn(self):
        return self.client.get_subscription

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription,
            subscription_id=self.module.params.get("subscription_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        optional_list_method_params = ["topic_id"]

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
            self.client.list_subscriptions, **kwargs
        )

    def get_create_model_class(self):
        return CreateSubscriptionDetails

    def create_resource(self):
        create_details = self.get_create_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.create_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(create_subscription_details=create_details,),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.CREATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def get_update_model_class(self):
        return UpdateSubscriptionDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                subscription_id=self.module.params.get("subscription_id"),
                update_subscription_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_active_states(),
        )

    def delete_resource(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.delete_subscription,
            call_fn_args=(),
            call_fn_kwargs=dict(
                subscription_id=self.module.params.get("subscription_id"),
            ),
            waiter_type=oci_wait_utils.LIFECYCLE_STATE_WAITER_KEY,
            operation=oci_common_utils.DELETE_OPERATION_KEY,
            waiter_client=self.client,
            resource_helper=self,
            wait_for_states=self.get_resource_terminated_states(),
        )


SubscriptionHelperCustom = get_custom_class("SubscriptionHelperCustom")


class ResourceHelper(SubscriptionHelperCustom, SubscriptionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=True, supports_wait=True
    )
    module_args.update(
        dict(
            topic_id=dict(type="str"),
            compartment_id=dict(type="str"),
            protocol=dict(type="str"),
            endpoint=dict(type="str"),
            metadata=dict(type="str"),
            freeform_tags=dict(type="dict"),
            defined_tags=dict(type="dict"),
            subscription_id=dict(aliases=["id"], type="str"),
            delivery_policy=dict(
                type="dict",
                options=dict(
                    backoff_retry_policy=dict(
                        type="dict",
                        options=dict(
                            max_retry_duration=dict(type="int", required=True),
                            policy_type=dict(
                                type="str", required=True, choices=["EXPONENTIAL"]
                            ),
                        ),
                    )
                ),
            ),
            state=dict(type="str", default="present", choices=["present", "absent"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="subscription",
        service_client_class=NotificationDataPlaneClient,
        namespace="ons",
    )

    result = dict(changed=False)

    if resource_helper.is_delete():
        result = resource_helper.delete()
    elif resource_helper.is_update():
        result = resource_helper.update()
    elif resource_helper.is_create():
        result = resource_helper.create()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
