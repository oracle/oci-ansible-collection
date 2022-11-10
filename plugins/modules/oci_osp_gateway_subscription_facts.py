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
module: oci_osp_gateway_subscription_facts
short_description: Fetches details about one or multiple Subscription resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Subscription resources in Oracle Cloud Infrastructure
    - Get the subscription data for the compartment
    - If I(subscription_id) is specified, the details of a single Subscription will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    subscription_id:
        description:
            - Subscription id(OCID).
            - Required to get a specific subscription.
        type: str
        aliases: ["id"]
    osp_home_region:
        description:
            - The home region's public name of the logged in user.
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. Only one field can be selected for sorting.
        type: str
        choices:
            - "INVOICE_NO"
            - "REF_NO"
            - "STATUS"
            - "TYPE"
            - "INVOICE_DATE"
            - "DUE_DATE"
            - "PAYM_REF"
            - "TOTAL_AMOUNT"
            - "BALANCE_DUE"
    sort_order:
        description:
            - The sort order to use (ascending or descending).
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific subscription
  oci_osp_gateway_subscription_facts:
    # required
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    osp_home_region: us-phoenix-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List subscriptions
  oci_osp_gateway_subscription_facts:
    # required
    osp_home_region: us-phoenix-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: INVOICE_NO
    sort_order: ASC

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
                - Subscription id identifier (OCID).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        subscription_plan_number:
            description:
                - Subscription plan number.
            returned: on success
            type: str
            sample: subscription_plan_number_example
        plan_type:
            description:
                - Subscription plan type.
            returned: on success
            type: str
            sample: FREE_TIER
        time_start:
            description:
                - Start date of the subscription.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        ship_to_cust_acct_site_id:
            description:
                - Ship to customer account site address id.
            returned: on success
            type: str
            sample: "ocid1.shiptocustacctsite.oc1..xxxxxxEXAMPLExxxxxx"
        ship_to_cust_acct_role_id:
            description:
                - Ship to customer account role.
            returned: on success
            type: str
            sample: "ocid1.shiptocustacctrole.oc1..xxxxxxEXAMPLExxxxxx"
        bill_to_cust_account_id:
            description:
                - Bill to customer Account id.
            returned: on success
            type: str
            sample: "ocid1.billtocustaccount.oc1..xxxxxxEXAMPLExxxxxx"
        is_intent_to_pay:
            description:
                - Payment intension.
            returned: on success
            type: bool
            sample: true
        currency_code:
            description:
                - Currency code
            returned: on success
            type: str
            sample: currency_code_example
        gsi_org_code:
            description:
                - GSI Subscription external code.
            returned: on success
            type: str
            sample: gsi_org_code_example
        language_code:
            description:
                - Language short code (en, de, hu, etc)
            returned: on success
            type: str
            sample: language_code_example
        organization_id:
            description:
                - GSI organization external identifier.
            returned: on success
            type: str
            sample: "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx"
        upgrade_state:
            description:
                - Status of the upgrade.
            returned: on success
            type: str
            sample: PROMO
        upgrade_state_details:
            description:
                - "This field is used to describe the Upgrade State in case of error (E.g. Upgrade failure caused by interfacing Tax details- TaxError)"
            returned: on success
            type: str
            sample: TAX_ERROR
        tax_info:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                tax_payer_id:
                    description:
                        - Tay payer identifier.
                    returned: on success
                    type: str
                    sample: "ocid1.taxpayer.oc1..xxxxxxEXAMPLExxxxxx"
                tax_reg_number:
                    description:
                        - Tax registration number.
                    returned: on success
                    type: str
                    sample: tax_reg_number_example
                no_tax_reason_code:
                    description:
                        - Tax exemption reason code.
                    returned: on success
                    type: str
                    sample: no_tax_reason_code_example
                no_tax_reason_code_details:
                    description:
                        - Tax exemption reason description.
                    returned: on success
                    type: str
                    sample: no_tax_reason_code_details_example
                tax_cnpj:
                    description:
                        - Brazilian companies' CNPJ number.
                    returned: on success
                    type: str
                    sample: tax_cnpj_example
        payment_options:
            description:
                - Payment option list of a subscription.
            returned: on success
            type: complex
            contains:
                credit_card_type:
                    description:
                        - Credit card type.
                    returned: on success
                    type: str
                    sample: VISA
                last_digits:
                    description:
                        - Last four digits of the card.
                    returned: on success
                    type: str
                    sample: last_digits_example
                name_on_card:
                    description:
                        - Name on the credit card.
                    returned: on success
                    type: str
                    sample: name_on_card_example
                time_expiration:
                    description:
                        - Expired date of the credit card.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                wallet_instrument_id:
                    description:
                        - Wallet instrument internal id.
                    returned: on success
                    type: str
                    sample: "ocid1.walletinstrument.oc1..xxxxxxEXAMPLExxxxxx"
                wallet_transaction_id:
                    description:
                        - Wallet transaction id.
                    returned: on success
                    type: str
                    sample: "ocid1.wallettransaction.oc1..xxxxxxEXAMPLExxxxxx"
                payment_method:
                    description:
                        - Payment method
                    returned: on success
                    type: str
                    sample: CREDIT_CARD
                email_address:
                    description:
                        - The email address of the paypal user.
                    returned: on success
                    type: str
                    sample: email_address_example
                first_name:
                    description:
                        - First name of the paypal user.
                    returned: on success
                    type: str
                    sample: first_name_example
                last_name:
                    description:
                        - Last name of the paypal user.
                    returned: on success
                    type: str
                    sample: last_name_example
                ext_billing_agreement_id:
                    description:
                        - Agreement id for the paypal account.
                    returned: on success
                    type: str
                    sample: "ocid1.extbillingagreement.oc1..xxxxxxEXAMPLExxxxxx"
        payment_gateway:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                merchant_defined_data:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        promo_type:
                            description:
                                - Promotion type code.
                            returned: on success
                            type: str
                            sample: promo_type_example
                        cloud_account_name:
                            description:
                                - Cloud account name.
                            returned: on success
                            type: str
                            sample: cloud_account_name_example
        billing_address:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                address_key:
                    description:
                        - Address identifier.
                    returned: on success
                    type: str
                    sample: address_key_example
                line1:
                    description:
                        - Address line 1.
                    returned: on success
                    type: str
                    sample: line1_example
                line2:
                    description:
                        - Address line 2.
                    returned: on success
                    type: str
                    sample: line2_example
                city:
                    description:
                        - Name of the city.
                    returned: on success
                    type: str
                    sample: city_example
                country:
                    description:
                        - Country of the address.
                    returned: on success
                    type: str
                    sample: country_example
                postal_code:
                    description:
                        - Post code of the address.
                    returned: on success
                    type: str
                    sample: postal_code_example
                state:
                    description:
                        - State of the address.
                    returned: on success
                    type: str
                    sample: state_example
                email_address:
                    description:
                        - Contact person email address.
                    returned: on success
                    type: str
                    sample: email_address_example
                company_name:
                    description:
                        - Name of the customer company.
                    returned: on success
                    type: str
                    sample: company_name_example
                first_name:
                    description:
                        - First name of the contact person.
                    returned: on success
                    type: str
                    sample: first_name_example
                last_name:
                    description:
                        - Last name of the contact person.
                    returned: on success
                    type: str
                    sample: last_name_example
        time_plan_upgrade:
            description:
                - Date of upgrade/conversion when planType changed from FREE_TIER to PAYG
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "subscription_plan_number": "subscription_plan_number_example",
        "plan_type": "FREE_TIER",
        "time_start": "2013-10-20T19:20:30+01:00",
        "ship_to_cust_acct_site_id": "ocid1.shiptocustacctsite.oc1..xxxxxxEXAMPLExxxxxx",
        "ship_to_cust_acct_role_id": "ocid1.shiptocustacctrole.oc1..xxxxxxEXAMPLExxxxxx",
        "bill_to_cust_account_id": "ocid1.billtocustaccount.oc1..xxxxxxEXAMPLExxxxxx",
        "is_intent_to_pay": true,
        "currency_code": "currency_code_example",
        "gsi_org_code": "gsi_org_code_example",
        "language_code": "language_code_example",
        "organization_id": "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx",
        "upgrade_state": "PROMO",
        "upgrade_state_details": "TAX_ERROR",
        "tax_info": {
            "tax_payer_id": "ocid1.taxpayer.oc1..xxxxxxEXAMPLExxxxxx",
            "tax_reg_number": "tax_reg_number_example",
            "no_tax_reason_code": "no_tax_reason_code_example",
            "no_tax_reason_code_details": "no_tax_reason_code_details_example",
            "tax_cnpj": "tax_cnpj_example"
        },
        "payment_options": [{
            "credit_card_type": "VISA",
            "last_digits": "last_digits_example",
            "name_on_card": "name_on_card_example",
            "time_expiration": "2013-10-20T19:20:30+01:00",
            "wallet_instrument_id": "ocid1.walletinstrument.oc1..xxxxxxEXAMPLExxxxxx",
            "wallet_transaction_id": "ocid1.wallettransaction.oc1..xxxxxxEXAMPLExxxxxx",
            "payment_method": "CREDIT_CARD",
            "email_address": "email_address_example",
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "ext_billing_agreement_id": "ocid1.extbillingagreement.oc1..xxxxxxEXAMPLExxxxxx"
        }],
        "payment_gateway": {
            "merchant_defined_data": {
                "promo_type": "promo_type_example",
                "cloud_account_name": "cloud_account_name_example"
            }
        },
        "billing_address": {
            "address_key": "address_key_example",
            "line1": "line1_example",
            "line2": "line2_example",
            "city": "city_example",
            "country": "country_example",
            "postal_code": "postal_code_example",
            "state": "state_example",
            "email_address": "email_address_example",
            "company_name": "company_name_example",
            "first_name": "first_name_example",
            "last_name": "last_name_example"
        },
        "time_plan_upgrade": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osp_gateway import SubscriptionServiceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "subscription_id",
            "osp_home_region",
            "compartment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "osp_home_region",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription,
            subscription_id=self.module.params.get("subscription_id"),
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_subscriptions,
            osp_home_region=self.module.params.get("osp_home_region"),
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
            osp_home_region=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            sort_by=dict(
                type="str",
                choices=[
                    "INVOICE_NO",
                    "REF_NO",
                    "STATUS",
                    "TYPE",
                    "INVOICE_DATE",
                    "DUE_DATE",
                    "PAYM_REF",
                    "TOTAL_AMOUNT",
                    "BALANCE_DUE",
                ],
            ),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="subscription",
        service_client_class=SubscriptionServiceClient,
        namespace="osp_gateway",
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
