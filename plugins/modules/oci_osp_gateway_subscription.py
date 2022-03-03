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
module: oci_osp_gateway_subscription
short_description: Manage a Subscription resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update a Subscription resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    subscription_id:
        description:
            - Subscription id(OCID).
        type: str
        aliases: ["id"]
        required: true
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
    subscription:
        description:
            - ""
        type: dict
        required: true
        suboptions:
            id:
                description:
                    - Subscription id identifier (OCID).
                    - This parameter is updatable.
                type: str
            subscription_plan_number:
                description:
                    - Subscription plan number.
                    - This parameter is updatable.
                type: str
                required: true
            plan_type:
                description:
                    - Subscription plan type.
                    - This parameter is updatable.
                type: str
                choices:
                    - "FREE_TIER"
                    - "PAYG"
            time_start:
                description:
                    - Start date of the subscription.
                    - This parameter is updatable.
                type: str
            ship_to_cust_acct_site_id:
                description:
                    - Ship to customer account site address id.
                    - This parameter is updatable.
                type: str
            ship_to_cust_acct_role_id:
                description:
                    - Ship to customer account role.
                    - This parameter is updatable.
                type: str
            bill_to_cust_account_id:
                description:
                    - Bill to customer Account id.
                    - This parameter is updatable.
                type: str
            is_intent_to_pay:
                description:
                    - Payment intension.
                    - This parameter is updatable.
                type: bool
            currency_code:
                description:
                    - Currency code
                    - This parameter is updatable.
                type: str
            gsi_org_code:
                description:
                    - GSI Subscription external code.
                    - This parameter is updatable.
                type: str
            language_code:
                description:
                    - Language short code (en, de, hu, etc)
                    - This parameter is updatable.
                type: str
            organization_id:
                description:
                    - GSI organization external identifier.
                    - This parameter is updatable.
                type: str
            upgrade_state:
                description:
                    - Status of the upgrade.
                    - This parameter is updatable.
                type: str
                choices:
                    - "PROMO"
                    - "SUBMITTED"
                    - "ERROR"
                    - "UPGRADED"
            upgrade_state_details:
                description:
                    - "This field is used to describe the Upgrade State in case of error (E.g. Upgrade failure caused by interfacing Tax details- TaxError)"
                    - This parameter is updatable.
                type: str
                choices:
                    - "TAX_ERROR"
                    - "UPGRADE_ERROR"
            tax_info:
                description:
                    - ""
                type: dict
                suboptions:
                    tax_payer_id:
                        description:
                            - Tay payer identifier.
                            - This parameter is updatable.
                        type: str
                    tax_reg_number:
                        description:
                            - Tax registration number.
                            - This parameter is updatable.
                        type: str
                    no_tax_reason_code:
                        description:
                            - Tax exemption reason code.
                            - This parameter is updatable.
                        type: str
                    no_tax_reason_code_details:
                        description:
                            - Tax exemption reason description.
                            - This parameter is updatable.
                        type: str
                    tax_cnpj:
                        description:
                            - Brazilian companies' CNPJ number.
                            - This parameter is updatable.
                        type: str
            payment_options:
                description:
                    - Payment option list of a subscription.
                type: list
                elements: dict
                suboptions:
                    wallet_instrument_id:
                        description:
                            - Wallet instrument internal id.
                            - This parameter is updatable.
                        type: str
                    wallet_transaction_id:
                        description:
                            - Wallet transaction id.
                            - This parameter is updatable.
                        type: str
                    payment_method:
                        description:
                            - Payment method
                            - This parameter is updatable.
                        type: str
                        choices:
                            - "CREDIT_CARD"
                            - "PAYPAL"
                        required: true
            payment_gateway:
                description:
                    - ""
                type: dict
                suboptions:
                    merchant_defined_data:
                        description:
                            - ""
                        type: dict
                        suboptions:
                            promo_type:
                                description:
                                    - Promotion type code.
                                    - This parameter is updatable.
                                type: str
                            cloud_account_name:
                                description:
                                    - Cloud account name.
                                    - This parameter is updatable.
                                type: str
            billing_address:
                description:
                    - ""
                type: dict
                suboptions:
                    address_key:
                        description:
                            - Address identifier.
                            - This parameter is updatable.
                        type: str
                    line1:
                        description:
                            - Address line 1.
                            - This parameter is updatable.
                        type: str
                    line2:
                        description:
                            - Address line 2.
                            - This parameter is updatable.
                        type: str
                    city:
                        description:
                            - Name of the city.
                            - This parameter is updatable.
                        type: str
                    country:
                        description:
                            - Country of the address.
                            - This parameter is updatable.
                        type: str
                    postal_code:
                        description:
                            - Post code of the address.
                            - This parameter is updatable.
                        type: str
                    state:
                        description:
                            - State of the address.
                            - This parameter is updatable.
                        type: str
                    email_address:
                        description:
                            - Contact person email address.
                            - This parameter is updatable.
                        type: str
                    company_name:
                        description:
                            - Name of the customer company.
                            - This parameter is updatable.
                        type: str
                    first_name:
                        description:
                            - First name of the contact person.
                            - This parameter is updatable.
                        type: str
                    last_name:
                        description:
                            - Last name of the contact person.
                            - This parameter is updatable.
                        type: str
            time_plan_upgrade:
                description:
                    - Date of upgrade/conversion when planType changed from FREE_TIER to PAYG
                    - This parameter is updatable.
                type: str
    email:
        description:
            - User email
        type: str
        required: true
    state:
        description:
            - The state of the Subscription.
            - Use I(state=present) to update an existing a Subscription.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Update subscription
  oci_osp_gateway_subscription:
    # required
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    osp_home_region: us-phoenix-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subscription:
      # required
      subscription_plan_number: subscription_plan_number_example

      # optional
      id: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
      plan_type: FREE_TIER
      time_start: time_start_example
      ship_to_cust_acct_site_id: "ocid1.shiptocustacctsite.oc1..xxxxxxEXAMPLExxxxxx"
      ship_to_cust_acct_role_id: "ocid1.shiptocustacctrole.oc1..xxxxxxEXAMPLExxxxxx"
      bill_to_cust_account_id: "ocid1.billtocustaccount.oc1..xxxxxxEXAMPLExxxxxx"
      is_intent_to_pay: true
      currency_code: currency_code_example
      gsi_org_code: gsi_org_code_example
      language_code: language_code_example
      organization_id: "ocid1.organization.oc1..xxxxxxEXAMPLExxxxxx"
      upgrade_state: PROMO
      upgrade_state_details: TAX_ERROR
      tax_info:
        # optional
        tax_payer_id: "ocid1.taxpayer.oc1..xxxxxxEXAMPLExxxxxx"
        tax_reg_number: tax_reg_number_example
        no_tax_reason_code: no_tax_reason_code_example
        no_tax_reason_code_details: no_tax_reason_code_details_example
        tax_cnpj: tax_cnpj_example
      payment_options:
      - # required
        payment_method: CREDIT_CARD

        # optional
        wallet_instrument_id: "ocid1.walletinstrument.oc1..xxxxxxEXAMPLExxxxxx"
        wallet_transaction_id: "ocid1.wallettransaction.oc1..xxxxxxEXAMPLExxxxxx"
      payment_gateway:
        # optional
        merchant_defined_data:
          # optional
          promo_type: promo_type_example
          cloud_account_name: cloud_account_name_example
      billing_address:
        # optional
        address_key: address_key_example
        line1: line1_example
        line2: line2_example
        city: city_example
        country: country_example
        postal_code: postal_code_example
        state: state_example
        email_address: email_address_example
        company_name: company_name_example
        first_name: first_name_example
        last_name: last_name_example
      time_plan_upgrade: time_plan_upgrade_example
    email: email_example

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
    sample: {
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
            "wallet_instrument_id": "ocid1.walletinstrument.oc1..xxxxxxEXAMPLExxxxxx",
            "wallet_transaction_id": "ocid1.wallettransaction.oc1..xxxxxxEXAMPLExxxxxx",
            "payment_method": "CREDIT_CARD"
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
    from oci.osp_gateway import SubscriptionServiceClient
    from oci.osp_gateway.models import UpdateSubscriptionDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscriptionHelperGen(OCIResourceHelperBase):
    """Supported operations: update, get and list"""

    def get_possible_entity_types(self):
        return super(SubscriptionHelperGen, self).get_possible_entity_types() + [
            "subscription",
            "subscriptions",
            "ospGatewaysubscription",
            "ospGatewaysubscriptions",
            "subscriptionresource",
            "subscriptionsresource",
            "ospgateway",
        ]

    def get_module_resource_id_param(self):
        return "subscription_id"

    def get_module_resource_id(self):
        return self.module.params.get("subscription_id")

    def get_get_fn(self):
        return self.client.get_subscription

    def get_get_model_from_summary_model(self, summary_model):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription, subscription_id=summary_model.id,
        ).data

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_subscription,
            subscription_id=self.module.params.get("subscription_id"),
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
        )

    def get_required_kwargs_for_list(self):
        required_list_method_params = [
            "osp_home_region",
            "compartment_id",
        ]

        return dict(
            (param, self.module.params[param]) for param in required_list_method_params
        )

    def get_optional_kwargs_for_list(self):
        return dict()

    def list_resources(self):

        required_kwargs = self.get_required_kwargs_for_list()
        optional_kwargs = self.get_optional_kwargs_for_list()
        kwargs = oci_common_utils.merge_dicts(required_kwargs, optional_kwargs)
        return oci_common_utils.list_all_resources(
            self.client.list_subscriptions, **kwargs
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
                osp_home_region=self.module.params.get("osp_home_region"),
                compartment_id=self.module.params.get("compartment_id"),
                update_subscription_details=update_details,
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_wait_for_states_for_operation(
                oci_common_utils.UPDATE_OPERATION_KEY,
            ),
        )


SubscriptionHelperCustom = get_custom_class("SubscriptionHelperCustom")


class ResourceHelper(SubscriptionHelperCustom, SubscriptionHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            subscription_id=dict(aliases=["id"], type="str", required=True),
            osp_home_region=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            subscription=dict(
                type="dict",
                required=True,
                options=dict(
                    id=dict(type="str"),
                    subscription_plan_number=dict(type="str", required=True),
                    plan_type=dict(type="str", choices=["FREE_TIER", "PAYG"]),
                    time_start=dict(type="str"),
                    ship_to_cust_acct_site_id=dict(type="str"),
                    ship_to_cust_acct_role_id=dict(type="str"),
                    bill_to_cust_account_id=dict(type="str"),
                    is_intent_to_pay=dict(type="bool"),
                    currency_code=dict(type="str"),
                    gsi_org_code=dict(type="str"),
                    language_code=dict(type="str"),
                    organization_id=dict(type="str"),
                    upgrade_state=dict(
                        type="str", choices=["PROMO", "SUBMITTED", "ERROR", "UPGRADED"]
                    ),
                    upgrade_state_details=dict(
                        type="str", choices=["TAX_ERROR", "UPGRADE_ERROR"]
                    ),
                    tax_info=dict(
                        type="dict",
                        options=dict(
                            tax_payer_id=dict(type="str"),
                            tax_reg_number=dict(type="str"),
                            no_tax_reason_code=dict(type="str"),
                            no_tax_reason_code_details=dict(type="str"),
                            tax_cnpj=dict(type="str"),
                        ),
                    ),
                    payment_options=dict(
                        type="list",
                        elements="dict",
                        options=dict(
                            wallet_instrument_id=dict(type="str"),
                            wallet_transaction_id=dict(type="str"),
                            payment_method=dict(
                                type="str",
                                required=True,
                                choices=["CREDIT_CARD", "PAYPAL"],
                            ),
                        ),
                    ),
                    payment_gateway=dict(
                        type="dict",
                        options=dict(
                            merchant_defined_data=dict(
                                type="dict",
                                options=dict(
                                    promo_type=dict(type="str"),
                                    cloud_account_name=dict(type="str"),
                                ),
                            )
                        ),
                    ),
                    billing_address=dict(
                        type="dict",
                        options=dict(
                            address_key=dict(type="str", no_log=True),
                            line1=dict(type="str"),
                            line2=dict(type="str"),
                            city=dict(type="str"),
                            country=dict(type="str"),
                            postal_code=dict(type="str"),
                            state=dict(type="str"),
                            email_address=dict(type="str"),
                            company_name=dict(type="str"),
                            first_name=dict(type="str"),
                            last_name=dict(type="str"),
                        ),
                    ),
                    time_plan_upgrade=dict(type="str"),
                ),
            ),
            email=dict(type="str", required=True),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="subscription",
        service_client_class=SubscriptionServiceClient,
        namespace="osp_gateway",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
