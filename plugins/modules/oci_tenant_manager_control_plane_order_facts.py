#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_tenant_manager_control_plane_order_facts
short_description: Fetches details about a Order resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Order resource in Oracle Cloud Infrastructure
    - Returns the order details given by the order ID in the JWT.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    activation_token:
        description:
            - Activation token containing an order ID. A JWT RFC 7519-formatted string.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific order
  oci_tenant_manager_control_plane_order_facts:
    # required
    activation_token: activation_token_example

"""

RETURN = """
order:
    description:
        - Order resource
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

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.tenant_manager_control_plane import OrdersClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OrderFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "activation_token",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_order,
            activation_token=self.module.params.get("activation_token"),
        )


OrderFactsHelperCustom = get_custom_class("OrderFactsHelperCustom")


class ResourceFactsHelper(OrderFactsHelperCustom, OrderFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(activation_token=dict(type="str", required=True, no_log=True),)
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="order",
        service_client_class=OrdersClient,
        namespace="tenant_manager_control_plane",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(order=result)


if __name__ == "__main__":
    main()
