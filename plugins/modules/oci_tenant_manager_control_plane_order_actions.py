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
module: oci_tenant_manager_control_plane_order_actions
short_description: Perform actions on an Order resource in Oracle Cloud Infrastructure
description:
    - Perform actions on an Order resource in Oracle Cloud Infrastructure
    - For I(action=activate), triggers an order activation workflow on behalf of the tenant, given by compartment ID in the body.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - Tenant ID to activate the order.
        type: str
        required: true
    activation_token:
        description:
            - Activation token containing an order ID. A JWT RFC 7519-formatted string.
        type: str
        required: true
    action:
        description:
            - The action to perform on the Order.
        type: str
        required: true
        choices:
            - "activate"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action activate on order
  oci_tenant_manager_control_plane_order_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    activation_token: activation_token_example
    action: activate

"""

RETURN = """
order:
    description:
        - Details of the Order resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        order_number:
            description:
                - Immutable and unique order number holding customer subscription information.
            returned: on success
            type: str
            sample: order_number_example
        data_center_region:
            description:
                - Order's data center region.
            returned: on success
            type: str
            sample: us-phoenix-1
        admin_email:
            description:
                - Email address of the administrator who owns the subscription.
            returned: on success
            type: str
            sample: admin_email_example
        order_state:
            description:
                - State of the order.
            returned: on success
            type: str
            sample: order_state_example
        subscriptions:
            description:
                - Array of subscriptions associated with the order.
            returned: on success
            type: complex
            contains:
                spm_subscription_id:
                    description:
                        - Subscription ID.
                    returned: on success
                    type: str
                    sample: "ocid1.spmsubscription.oc1..xxxxxxEXAMPLExxxxxx"
                service:
                    description:
                        - Subscription service name.
                    returned: on success
                    type: str
                    sample: service_example
                start_date:
                    description:
                        - Subscription start date. An RFC 3339-formatted date and time string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                end_date:
                    description:
                        - Subscription end date. An RFC 3339-formatted date and time string.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                skus:
                    description:
                        - List of SKUs the subscription contains.
                    returned: on success
                    type: complex
                    contains:
                        number:
                            description:
                                - SKU number.
                            returned: on success
                            type: str
                            sample: number_example
                        name:
                            description:
                                - SKU name.
                            returned: on success
                            type: str
                            sample: name_example
                        quantity:
                            description:
                                - SKU quantity.
                            returned: on success
                            type: int
                            sample: 56
    sample: {
        "order_number": "order_number_example",
        "data_center_region": "us-phoenix-1",
        "admin_email": "admin_email_example",
        "order_state": "order_state_example",
        "subscriptions": [{
            "spm_subscription_id": "ocid1.spmsubscription.oc1..xxxxxxEXAMPLExxxxxx",
            "service": "service_example",
            "start_date": "2013-10-20T19:20:30+01:00",
            "end_date": "2013-10-20T19:20:30+01:00",
            "skus": [{
                "number": "number_example",
                "name": "name_example",
                "quantity": 56
            }]
        }]
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.tenant_manager_control_plane import WorkRequestClient
    from oci.tenant_manager_control_plane import OrdersClient
    from oci.tenant_manager_control_plane.models import ActivateOrderDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OrderActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        activate
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "activation_token"

    def get_module_resource_id(self):
        return self.module.params.get("activation_token")

    def get_get_fn(self):
        return self.client.get_order

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_order,
            activation_token=self.module.params.get("activation_token"),
        )

    def activate(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ActivateOrderDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.activate_order,
            call_fn_args=(),
            call_fn_kwargs=dict(
                activate_order_details=action_details,
                activation_token=self.module.params.get("activation_token"),
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


OrderActionsHelperCustom = get_custom_class("OrderActionsHelperCustom")


class ResourceHelper(OrderActionsHelperCustom, OrderActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            activation_token=dict(type="str", required=True, no_log=True),
            action=dict(type="str", required=True, choices=["activate"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="order",
        service_client_class=OrdersClient,
        namespace="tenant_manager_control_plane",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
