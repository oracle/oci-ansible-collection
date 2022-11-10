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
module: oci_osp_gateway_invoice_facts
short_description: Fetches details about one or multiple Invoice resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Invoice resources in Oracle Cloud Infrastructure
    - Returns a list of invoices
    - If I(internal_invoice_id) is specified, the details of a single Invoice will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    internal_invoice_id:
        description:
            - The identifier of the invoice.
            - Required to get a specific invoice.
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
    invoice_id:
        description:
            - The invoice query param (not unique).
        type: str
    type:
        description:
            - A filter to only return resources that match the given type exactly.
        type: list
        elements: str
        choices:
            - "HARDWARE"
            - "SUBSCRIPTION"
            - "SUPPORT"
            - "LICENSE"
            - "EDUCATION"
            - "CONSULTING"
            - "SERVICE"
            - "USAGE"
    search_text:
        description:
            - "A filter to only return resources that match the given value.
              Looking for partial matches in the following fileds:
              Invoice No., Reference No. (plan number), Payment Ref, Total Amount(plan number), Balance Due(plan number)
              and Party/Customer Name"
        type: str
    time_invoice_start:
        description:
            - "description: Start time (UTC) of the target invoice date range for which to fetch invoice data (inclusive)."
        type: str
    time_invoice_end:
        description:
            - "description: End time (UTC) of the target invoice date range for which to fetch invoice data (exclusive)."
        type: str
    time_payment_start:
        description:
            - "description: Start time (UTC) of the target payment date range for which to fetch invoice data (inclusive)."
        type: str
    time_payment_end:
        description:
            - "description: End time (UTC) of the target payment date range for which to fetch invoice data (exclusive)."
        type: str
    status:
        description:
            - A filter to only return resources that match one of the status elements.
        type: list
        elements: str
        choices:
            - "OPEN"
            - "PAST_DUE"
            - "PAYMENT_SUBMITTED"
            - "CLOSED"
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
- name: Get a specific invoice
  oci_osp_gateway_invoice_facts:
    # required
    internal_invoice_id: "ocid1.internalinvoice.oc1..xxxxxxEXAMPLExxxxxx"
    osp_home_region: us-phoenix-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List invoices
  oci_osp_gateway_invoice_facts:
    # required
    osp_home_region: us-phoenix-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    invoice_id: "ocid1.invoice.oc1..xxxxxxEXAMPLExxxxxx"
    type: [ "HARDWARE" ]
    search_text: search_text_example
    time_invoice_start: 2013-10-20T19:20:30+01:00
    time_invoice_end: 2013-10-20T19:20:30+01:00
    time_payment_start: 2013-10-20T19:20:30+01:00
    time_payment_end: 2013-10-20T19:20:30+01:00
    status: [ "OPEN" ]
    sort_by: INVOICE_NO
    sort_order: ASC

"""

RETURN = """
invoices:
    description:
        - List of Invoice resources
    returned: on success
    type: complex
    contains:
        tax:
            description:
                - Tax of invoice amount
                - Returned for get operation
            returned: on success
            type: float
            sample: 10
        preferred_email:
            description:
                - Preferred Email on the invoice
                - Returned for get operation
            returned: on success
            type: str
            sample: preferred_email_example
        payment_terms:
            description:
                - Payment terms
                - Returned for get operation
            returned: on success
            type: str
            sample: payment_terms_example
        bill_to_address:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                contact_name:
                    description:
                        - Name of the contact person
                    returned: on success
                    type: str
                    sample: contact_name_example
                company_name:
                    description:
                        - Name of the customer company
                    returned: on success
                    type: str
                    sample: company_name_example
                address_line1:
                    description:
                        - Address line 1
                    returned: on success
                    type: str
                    sample: address_line1_example
                address_line2:
                    description:
                        - Address line 2
                    returned: on success
                    type: str
                    sample: address_line2_example
                address_line3:
                    description:
                        - Address line 3
                    returned: on success
                    type: str
                    sample: address_line3_example
                address_line4:
                    description:
                        - Address line 4
                    returned: on success
                    type: str
                    sample: address_line4_example
                street_name:
                    description:
                        - Street name
                    returned: on success
                    type: str
                    sample: street_name_example
                street_number:
                    description:
                        - House no
                    returned: on success
                    type: str
                    sample: street_number_example
                city:
                    description:
                        - Name of the city
                    returned: on success
                    type: str
                    sample: city_example
                country:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        country_id:
                            description:
                                - Indentifier of the country. This is a DB side unique id which was generated when the entity was created in the table
                            returned: on success
                            type: float
                            sample: 10
                        country_code:
                            description:
                                - Country code in ISO-3166-1 2-letter format
                            returned: on success
                            type: str
                            sample: country_code_example
                        country_name:
                            description:
                                - Name of the country
                            returned: on success
                            type: str
                            sample: country_name_example
                        language_id:
                            description:
                                - Language identifier
                            returned: on success
                            type: float
                            sample: 10
                        ascii3_country_code:
                            description:
                                - Country code in ISO-3166-1 3-letter format
                            returned: on success
                            type: str
                            sample: ascii3_country_code_example
                county:
                    description:
                        - County name
                    returned: on success
                    type: str
                    sample: county_example
                state:
                    description:
                        - Name of the state
                    returned: on success
                    type: str
                    sample: state_example
                postal_code:
                    description:
                        - ZIP no
                    returned: on success
                    type: str
                    sample: postal_code_example
                province:
                    description:
                        - Name of the province
                    returned: on success
                    type: str
                    sample: province_example
        invoice_id:
            description:
                - Invoice identifier which is generated on the on-premise sie. Pls note this is not an OCID
            returned: on success
            type: str
            sample: "ocid1.invoice.oc1..xxxxxxEXAMPLExxxxxx"
        invoice_number:
            description:
                - Invoice external reference
            returned: on success
            type: str
            sample: invoice_number_example
        internal_invoice_id:
            description:
                - Transaction identifier
            returned: on success
            type: str
            sample: "ocid1.internalinvoice.oc1..xxxxxxEXAMPLExxxxxx"
        is_credit_card_payable:
            description:
                - Is credit card payment eligible
            returned: on success
            type: bool
            sample: true
        invoice_status:
            description:
                - Invoice status
            returned: on success
            type: str
            sample: OPEN
        invoice_type:
            description:
                - Type of invoice
            returned: on success
            type: str
            sample: HARDWARE
        is_paid:
            description:
                - Is the invoice has been already payed
                - Returned for list operation
            returned: on success
            type: bool
            sample: true
        is_payable:
            description:
                - Whether invoice can be payed
            returned: on success
            type: bool
            sample: true
        invoice_amount:
            description:
                - Total amount of invoice
            returned: on success
            type: float
            sample: 10
        invoice_amount_due:
            description:
                - Balance of invoice
            returned: on success
            type: float
            sample: 10
        invoice_amount_credited:
            description:
                - Invoice amount credit
            returned: on success
            type: float
            sample: 10
        invoice_amount_adjusted:
            description:
                - Invoice amount adjust
            returned: on success
            type: float
            sample: 10
        invoice_amount_applied:
            description:
                - Invoice amount applied
            returned: on success
            type: float
            sample: 10
        time_invoice_due:
            description:
                - Due date of invoice
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_payment_failed:
            description:
                - Is the last payment failed
                - Returned for list operation
            returned: on success
            type: bool
            sample: true
        invoice_amount_in_dispute:
            description:
                - Invoice amount in dispute
                - Returned for list operation
            returned: on success
            type: float
            sample: 10
        invoice_ref_number:
            description:
                - Invoice reference number
            returned: on success
            type: str
            sample: invoice_ref_number_example
        invoice_po_number:
            description:
                - Invoice PO number
            returned: on success
            type: str
            sample: invoice_po_number_example
        time_invoice:
            description:
                - Date of invoice
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        currency:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                currency_code:
                    description:
                        - Currency code
                    returned: on success
                    type: str
                    sample: currency_code_example
                currency_symbol:
                    description:
                        - Currency symbol
                    returned: on success
                    type: str
                    sample: currency_symbol_example
                name:
                    description:
                        - Name of the currency
                    returned: on success
                    type: str
                    sample: name_example
                usd_conversion:
                    description:
                        - USD conversion rate of the currency
                    returned: on success
                    type: float
                    sample: 10
                round_decimal_point:
                    description:
                        - Round decimal point
                    returned: on success
                    type: float
                    sample: 10
        is_pdf_email_available:
            description:
                - Is emailing pdf allowed
            returned: on success
            type: bool
            sample: true
        is_display_view_pdf:
            description:
                - Is view access allowed
                - Returned for list operation
            returned: on success
            type: bool
            sample: true
        is_display_download_pdf:
            description:
                - Is pdf download access allowed
            returned: on success
            type: bool
            sample: true
        last_payment_detail:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                echeck_routing:
                    description:
                        - Last four routing digits of the card
                    returned: on success
                    type: str
                    sample: echeck_routing_example
                name_on_card:
                    description:
                        - Name on the credit card
                    returned: on success
                    type: str
                    sample: name_on_card_example
                credit_card_type:
                    description:
                        - Credit card type
                    returned: on success
                    type: str
                    sample: VISA
                last_digits:
                    description:
                        - Last four digits of the card
                    returned: on success
                    type: str
                    sample: last_digits_example
                time_expiration:
                    description:
                        - Expired date of the credit card
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_paid_on:
                    description:
                        - Paid the invoice on this day
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                paid_by:
                    description:
                        - example
                    returned: on success
                    type: str
                    sample: paid_by_example
                payment_method:
                    description:
                        - Payment method
                    returned: on success
                    type: str
                    sample: CREDIT_CARD
                amount_paid:
                    description:
                        - Amount that paid
                    returned: on success
                    type: float
                    sample: 10
                paypal_id:
                    description:
                        - The id (email address) of the paypal payment
                    returned: on success
                    type: str
                    sample: "ocid1.paypal.oc1..xxxxxxEXAMPLExxxxxx"
                paypal_reference:
                    description:
                        - paypal payment reference
                    returned: on success
                    type: str
                    sample: paypal_reference_example
        party_name:
            description:
                - Name of the bill to customer
                - Returned for list operation
            returned: on success
            type: str
            sample: party_name_example
        subscription_ids:
            description:
                - List of subscription identifiers
            returned: on success
            type: list
            sample: []
    sample: [{
        "tax": 10,
        "preferred_email": "preferred_email_example",
        "payment_terms": "payment_terms_example",
        "bill_to_address": {
            "contact_name": "contact_name_example",
            "company_name": "company_name_example",
            "address_line1": "address_line1_example",
            "address_line2": "address_line2_example",
            "address_line3": "address_line3_example",
            "address_line4": "address_line4_example",
            "street_name": "street_name_example",
            "street_number": "street_number_example",
            "city": "city_example",
            "country": {
                "country_id": 10,
                "country_code": "country_code_example",
                "country_name": "country_name_example",
                "language_id": 10,
                "ascii3_country_code": "ascii3_country_code_example"
            },
            "county": "county_example",
            "state": "state_example",
            "postal_code": "postal_code_example",
            "province": "province_example"
        },
        "invoice_id": "ocid1.invoice.oc1..xxxxxxEXAMPLExxxxxx",
        "invoice_number": "invoice_number_example",
        "internal_invoice_id": "ocid1.internalinvoice.oc1..xxxxxxEXAMPLExxxxxx",
        "is_credit_card_payable": true,
        "invoice_status": "OPEN",
        "invoice_type": "HARDWARE",
        "is_paid": true,
        "is_payable": true,
        "invoice_amount": 10,
        "invoice_amount_due": 10,
        "invoice_amount_credited": 10,
        "invoice_amount_adjusted": 10,
        "invoice_amount_applied": 10,
        "time_invoice_due": "2013-10-20T19:20:30+01:00",
        "is_payment_failed": true,
        "invoice_amount_in_dispute": 10,
        "invoice_ref_number": "invoice_ref_number_example",
        "invoice_po_number": "invoice_po_number_example",
        "time_invoice": "2013-10-20T19:20:30+01:00",
        "currency": {
            "currency_code": "currency_code_example",
            "currency_symbol": "currency_symbol_example",
            "name": "name_example",
            "usd_conversion": 10,
            "round_decimal_point": 10
        },
        "is_pdf_email_available": true,
        "is_display_view_pdf": true,
        "is_display_download_pdf": true,
        "last_payment_detail": {
            "echeck_routing": "echeck_routing_example",
            "name_on_card": "name_on_card_example",
            "credit_card_type": "VISA",
            "last_digits": "last_digits_example",
            "time_expiration": "2013-10-20T19:20:30+01:00",
            "time_paid_on": "2013-10-20T19:20:30+01:00",
            "paid_by": "paid_by_example",
            "payment_method": "CREDIT_CARD",
            "amount_paid": 10,
            "paypal_id": "ocid1.paypal.oc1..xxxxxxEXAMPLExxxxxx",
            "paypal_reference": "paypal_reference_example"
        },
        "party_name": "party_name_example",
        "subscription_ids": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osp_gateway import InvoiceServiceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InvoiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "osp_home_region",
            "compartment_id",
            "internal_invoice_id",
        ]

    def get_required_params_for_list(self):
        return [
            "osp_home_region",
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_invoice,
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
            internal_invoice_id=self.module.params.get("internal_invoice_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "invoice_id",
            "type",
            "search_text",
            "time_invoice_start",
            "time_invoice_end",
            "time_payment_start",
            "time_payment_end",
            "status",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_invoices,
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


InvoiceFactsHelperCustom = get_custom_class("InvoiceFactsHelperCustom")


class ResourceFactsHelper(InvoiceFactsHelperCustom, InvoiceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            internal_invoice_id=dict(aliases=["id"], type="str"),
            osp_home_region=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            invoice_id=dict(type="str"),
            type=dict(
                type="list",
                elements="str",
                choices=[
                    "HARDWARE",
                    "SUBSCRIPTION",
                    "SUPPORT",
                    "LICENSE",
                    "EDUCATION",
                    "CONSULTING",
                    "SERVICE",
                    "USAGE",
                ],
            ),
            search_text=dict(type="str"),
            time_invoice_start=dict(type="str"),
            time_invoice_end=dict(type="str"),
            time_payment_start=dict(type="str"),
            time_payment_end=dict(type="str"),
            status=dict(
                type="list",
                elements="str",
                choices=["OPEN", "PAST_DUE", "PAYMENT_SUBMITTED", "CLOSED"],
            ),
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
        resource_type="invoice",
        service_client_class=InvoiceServiceClient,
        namespace="osp_gateway",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(invoices=result)


if __name__ == "__main__":
    main()
