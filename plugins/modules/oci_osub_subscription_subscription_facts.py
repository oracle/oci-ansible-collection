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
module: oci_osub_subscription_subscription_facts
short_description: Fetches details about one or multiple Subscription resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Subscription resources in Oracle Cloud Infrastructure
    - "This list API returns all subscriptions for a given plan number or subscription id or buyer email
      and provides additional parameters to include ratecard and commitment details.
      This API expects exactly one of the above mentioned parameters as input. If more than one parameters are provided the API will throw
      a 400 - invalid parameters exception and if no parameters are provided it will throw a 400 - missing parameter exception"
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        required: true
    plan_number:
        description:
            - The Plan Number
        type: str
    subscription_id:
        description:
            - Line level Subscription Id
        type: str
    buyer_email:
        description:
            - Buyer Email Id
        type: str
    is_commit_info_required:
        description:
            - Boolean value to decide whether commitment services will be shown
        type: bool
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`).
        type: str
        choices:
            - "TIMECREATED"
            - "TIMESTART"
    x_one_gateway_subscription_id:
        description:
            - This header is meant to be used only for internal purposes and will be ignored on any public request. The purpose of this header is
              to help on Gateway to API calls identification.
        type: str
    x_one_origin_region:
        description:
            - The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List subscriptions
  oci_osub_subscription_subscription_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    plan_number: plan_number_example
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    buyer_email: buyer_email_example
    is_commit_info_required: true
    sort_order: ASC
    sort_by: TIMECREATED
    x_one_gateway_subscription_id: "ocid1.xonegatewaysubscription.oc1..xxxxxxEXAMPLExxxxxx"
    x_one_origin_region: us-phoenix-1

"""

RETURN = """
subscriptions:
    description:
        - List of Subscription resources
    returned: on success
    type: complex
    contains:
        status:
            description:
                - Status of the plan
            returned: on success
            type: str
            sample: status_example
        time_start:
            description:
                - Represents the date when the first service of the subscription was activated
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - Represents the date when the last service of the subscription ends
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        currency:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Currency name
                    returned: on success
                    type: str
                    sample: name_example
                iso_code:
                    description:
                        - Currency Code
                    returned: on success
                    type: str
                    sample: iso_code_example
                std_precision:
                    description:
                        - Standard Precision of the Currency
                    returned: on success
                    type: int
                    sample: 56
        service_name:
            description:
                - Customer friendly service name provided by PRG
            returned: on success
            type: str
            sample: service_name_example
        subscribed_services:
            description:
                - List of Subscribed Services of the plan
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - SPM internal Subscribed Service ID
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                product:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        part_number:
                            description:
                                - Product part numner
                            returned: on success
                            type: str
                            sample: part_number_example
                        name:
                            description:
                                - Product name
                            returned: on success
                            type: str
                            sample: name_example
                        unit_of_measure:
                            description:
                                - Unit of measure
                            returned: on success
                            type: str
                            sample: unit_of_measure_example
                        provisioning_group:
                            description:
                                - Product provisioning group
                            returned: on success
                            type: str
                            sample: provisioning_group_example
                quantity:
                    description:
                        - Subscribed service quantity
                    returned: on success
                    type: str
                    sample: quantity_example
                status:
                    description:
                        - Subscribed service status
                    returned: on success
                    type: str
                    sample: status_example
                operation_type:
                    description:
                        - Subscribed service operation type
                    returned: on success
                    type: str
                    sample: operation_type_example
                net_unit_price:
                    description:
                        - Subscribed service net unit price
                    returned: on success
                    type: str
                    sample: net_unit_price_example
                funded_allocation_value:
                    description:
                        - "Funded Allocation line value
                          example: 12000.00"
                    returned: on success
                    type: str
                    sample: funded_allocation_value_example
                partner_transaction_type:
                    description:
                        - "This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ"
                    returned: on success
                    type: str
                    sample: partner_transaction_type_example
                term_value:
                    description:
                        - Term value in Months
                    returned: on success
                    type: int
                    sample: 56
                term_value_uom:
                    description:
                        - Term value UOM
                    returned: on success
                    type: str
                    sample: term_value_uom_example
                booking_opty_number:
                    description:
                        - Booking Opportunity Number of Subscribed Service
                    returned: on success
                    type: str
                    sample: booking_opty_number_example
                total_value:
                    description:
                        - Subscribed service total value
                    returned: on success
                    type: str
                    sample: total_value_example
                order_number:
                    description:
                        - Sales Order Number associated to the subscribed service
                    returned: on success
                    type: int
                    sample: 56
                data_center_region:
                    description:
                        - Subscribed service data center region
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                pricing_model:
                    description:
                        - Subscribed service pricing model
                    returned: on success
                    type: str
                    sample: pricing_model_example
                program_type:
                    description:
                        - Subscribed service program type
                    returned: on success
                    type: str
                    sample: program_type_example
                promo_type:
                    description:
                        - Subscribed service promotion type
                    returned: on success
                    type: str
                    sample: promo_type_example
                csi:
                    description:
                        - Subscribed service CSI number
                    returned: on success
                    type: int
                    sample: 56
                is_intent_to_pay:
                    description:
                        - Subscribed service intent to pay flag
                    returned: on success
                    type: bool
                    sample: true
                time_start:
                    description:
                        - Subscribed service start date
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_end:
                    description:
                        - Subscribed service end date
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                commitment_services:
                    description:
                        - List of Commitment services of a line
                    returned: on success
                    type: complex
                    contains:
                        time_start:
                            description:
                                - Commitment start date
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        time_end:
                            description:
                                - Commitment end date
                            returned: on success
                            type: str
                            sample: "2013-10-20T19:20:30+01:00"
                        quantity:
                            description:
                                - Commitment quantity
                            returned: on success
                            type: str
                            sample: quantity_example
                        available_amount:
                            description:
                                - Commitment available amount
                            returned: on success
                            type: str
                            sample: available_amount_example
                        line_net_amount:
                            description:
                                - Commitment line net amount
                            returned: on success
                            type: str
                            sample: line_net_amount_example
                        funded_allocation_value:
                            description:
                                - Funded Allocation line value
                            returned: on success
                            type: str
                            sample: funded_allocation_value_example
    sample: [{
        "status": "status_example",
        "time_start": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "currency": {
            "name": "name_example",
            "iso_code": "iso_code_example",
            "std_precision": 56
        },
        "service_name": "service_name_example",
        "subscribed_services": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "product": {
                "part_number": "part_number_example",
                "name": "name_example",
                "unit_of_measure": "unit_of_measure_example",
                "provisioning_group": "provisioning_group_example"
            },
            "quantity": "quantity_example",
            "status": "status_example",
            "operation_type": "operation_type_example",
            "net_unit_price": "net_unit_price_example",
            "funded_allocation_value": "funded_allocation_value_example",
            "partner_transaction_type": "partner_transaction_type_example",
            "term_value": 56,
            "term_value_uom": "term_value_uom_example",
            "booking_opty_number": "booking_opty_number_example",
            "total_value": "total_value_example",
            "order_number": 56,
            "data_center_region": "us-phoenix-1",
            "pricing_model": "pricing_model_example",
            "program_type": "program_type_example",
            "promo_type": "promo_type_example",
            "csi": 56,
            "is_intent_to_pay": true,
            "time_start": "2013-10-20T19:20:30+01:00",
            "time_end": "2013-10-20T19:20:30+01:00",
            "commitment_services": [{
                "time_start": "2013-10-20T19:20:30+01:00",
                "time_end": "2013-10-20T19:20:30+01:00",
                "quantity": "quantity_example",
                "available_amount": "available_amount_example",
                "line_net_amount": "line_net_amount_example",
                "funded_allocation_value": "funded_allocation_value_example"
            }]
        }]
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osub_subscription import SubscriptionClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "plan_number",
            "subscription_id",
            "buyer_email",
            "is_commit_info_required",
            "sort_order",
            "sort_by",
            "x_one_gateway_subscription_id",
            "x_one_origin_region",
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
            compartment_id=dict(type="str", required=True),
            plan_number=dict(type="str"),
            subscription_id=dict(type="str"),
            buyer_email=dict(type="str"),
            is_commit_info_required=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "TIMESTART"]),
            x_one_gateway_subscription_id=dict(type="str"),
            x_one_origin_region=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="subscription",
        service_client_class=SubscriptionClient,
        namespace="osub_subscription",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(subscriptions=result)


if __name__ == "__main__":
    main()
