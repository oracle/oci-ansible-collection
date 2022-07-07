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
module: oci_onesubscription_invoice_facts
short_description: Fetches details about one or multiple Invoice resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Invoice resources in Oracle Cloud Infrastructure
    - This is a collection API which returns a list of Invoices for given filters.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the root compartment.
        type: str
        required: true
    ar_customer_transaction_id:
        description:
            - AR Unique identifier for an invoice .
        type: str
        required: true
    time_from:
        description:
            - Initial date to filter Invoice data in SPM.
        type: str
    time_to:
        description:
            - Final date to filter Invoice data in SPM.
        type: str
    sort_order:
        description:
            - The sort order to use, either ascending ('ASC') or descending ('DESC').
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort order ('sortOrder').
        type: str
        choices:
            - "ORDERNUMBER"
            - "TIMEINVOICING"
    fields:
        description:
            - Partial response refers to an optimization technique offered
              by the RESTful web APIs to return only the information
              (fields) required by the client. This parameter is used to control what fields to
              return.
        type: list
        elements: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List invoices
  oci_onesubscription_invoice_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    ar_customer_transaction_id: "ocid1.arcustomertransaction.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_from: 2013-10-20T19:20:30+01:00
    time_to: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: ORDERNUMBER
    fields: [ "fields_example" ]

"""

RETURN = """
invoices:
    description:
        - List of Invoice resources
    returned: on success
    type: complex
    contains:
        spm_invoice_number:
            description:
                - SPM Document Number is an functional identifier for invoice in SPM
            returned: on success
            type: str
            sample: spm_invoice_number_example
        ar_invoices:
            description:
                - AR Invoice Numbers comma separated under one invoice
            returned: on success
            type: str
            sample: ar_invoices_example
        bill_to_customer:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Commercial name also called customer name.
                    returned: on success
                    type: str
                    sample: name_example
                name_phonetic:
                    description:
                        - Phonetic name.
                    returned: on success
                    type: str
                    sample: name_phonetic_example
                tca_customer_account_number:
                    description:
                        - TCA customer account number.
                    returned: on success
                    type: str
                    sample: tca_customer_account_number_example
                is_public_sector:
                    description:
                        - The business partner is part of the public sector or not.
                    returned: on success
                    type: bool
                    sample: true
                is_chain_customer:
                    description:
                        - The business partner is chain customer or not.
                    returned: on success
                    type: bool
                    sample: true
                customer_chain_type:
                    description:
                        - Customer chain type.
                    returned: on success
                    type: str
                    sample: customer_chain_type_example
                tca_party_number:
                    description:
                        - TCA party number.
                    returned: on success
                    type: str
                    sample: tca_party_number_example
                tca_party_id:
                    description:
                        - TCA party ID.
                    returned: on success
                    type: int
                    sample: 56
                tca_customer_account_id:
                    description:
                        - TCA customer account ID.
                    returned: on success
                    type: int
                    sample: 56
        bill_to_contact:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name.
                    returned: on success
                    type: str
                    sample: name_example
                user_name:
                    description:
                        - userName.
                    returned: on success
                    type: str
                    sample: user_name_example
                first_name:
                    description:
                        - First name.
                    returned: on success
                    type: str
                    sample: first_name_example
                last_name:
                    description:
                        - Last name.
                    returned: on success
                    type: str
                    sample: last_name_example
                email:
                    description:
                        - Email.
                    returned: on success
                    type: str
                    sample: email_example
                tca_contact_id:
                    description:
                        - TCA contact ID.
                    returned: on success
                    type: int
                    sample: 56
                tca_cust_accnt_site_id:
                    description:
                        - TCA customer account site ID.
                    returned: on success
                    type: int
                    sample: 56
                tca_party_id:
                    description:
                        - TCA party ID.
                    returned: on success
                    type: int
                    sample: 56
        bill_to_address:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                location:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        address1:
                            description:
                                - Address first line.
                            returned: on success
                            type: str
                            sample: address1_example
                        address2:
                            description:
                                - Address second line.
                            returned: on success
                            type: str
                            sample: address2_example
                        postal_code:
                            description:
                                - Postal code.
                            returned: on success
                            type: str
                            sample: postal_code_example
                        city:
                            description:
                                - City.
                            returned: on success
                            type: str
                            sample: city_example
                        country:
                            description:
                                - Country.
                            returned: on success
                            type: str
                            sample: country_example
                        region:
                            description:
                                - Region.
                            returned: on success
                            type: str
                            sample: us-phoenix-1
                        tca_location_id:
                            description:
                                - TCA Location identifier.
                            returned: on success
                            type: int
                            sample: 56
                name:
                    description:
                        - Address name identifier.
                    returned: on success
                    type: str
                    sample: name_example
                phone:
                    description:
                        - Phone.
                    returned: on success
                    type: str
                    sample: phone_example
                is_bill_to:
                    description:
                        - Identify as the customer's billing address.
                    returned: on success
                    type: bool
                    sample: true
                is_ship_to:
                    description:
                        - Identify as the customer's shipping address.
                    returned: on success
                    type: bool
                    sample: true
                bill_site_use_id:
                    description:
                        - Bill to site use Id.
                    returned: on success
                    type: int
                    sample: 56
                service2_site_use_id:
                    description:
                        - Service to site use Id.
                    returned: on success
                    type: int
                    sample: 56
                tca_cust_acct_site_id:
                    description:
                        - TCA customer account site Id.
                    returned: on success
                    type: int
                    sample: 56
                tca_party_site_number:
                    description:
                        - Party site number.
                    returned: on success
                    type: str
                    sample: tca_party_site_number_example
        payment_method:
            description:
                - Payment Method
            returned: on success
            type: str
            sample: payment_method_example
        payment_term:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Payment Term name
                    returned: on success
                    type: str
                    sample: name_example
                value:
                    description:
                        - Payment Term value
                    returned: on success
                    type: str
                    sample: value_example
                description:
                    description:
                        - Payment term Description
                    returned: on success
                    type: str
                    sample: description_example
                is_active:
                    description:
                        - Payment term active flag
                    returned: on success
                    type: bool
                    sample: true
                time_created:
                    description:
                        - Payment term last update date
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                created_by:
                    description:
                        - User that created the Payment term
                    returned: on success
                    type: str
                    sample: created_by_example
                time_updated:
                    description:
                        - Payment term last update date
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                updated_by:
                    description:
                        - User that updated the Payment term
                    returned: on success
                    type: str
                    sample: updated_by_example
        receipt_method:
            description:
                - Receipt Method of Payment Mode
            returned: on success
            type: str
            sample: receipt_method_example
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
        organization:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Organization name
                    returned: on success
                    type: str
                    sample: name_example
                number:
                    description:
                        - Organization ID
                    returned: on success
                    type: float
                    sample: 1.2
        type:
            description:
                - Document Type in SPM like SPM Invoice,SPM Credit Memo etc.,
            returned: on success
            type: str
            sample: type_example
        status:
            description:
                - Document Status in SPM which depicts current state of invoice
            returned: on success
            type: str
            sample: status_example
        subscription_number:
            description:
                - Invoice associated subscription plan number.
            returned: on success
            type: str
            sample: subscription_number_example
        time_invoice_date:
            description:
                - Invoice Date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - SPM Invocie creation date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by:
            description:
                - User that executed SPM Invoice process
            returned: on success
            type: str
            sample: created_by_example
        time_updated:
            description:
                - SPM Invoice updated date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        updated_by:
            description:
                - User that updated SPM Invoice
            returned: on success
            type: str
            sample: updated_by_example
        invoice_lines:
            description:
                - Invoice Lines under particular invoice.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - SPM Invoice Line internal identifier
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
                                - Product part number
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
                                - Unit of Measure
                            returned: on success
                            type: str
                            sample: unit_of_measure_example
                        billing_category:
                            description:
                                - Metered service billing category
                            returned: on success
                            type: str
                            sample: billing_category_example
                        product_category:
                            description:
                                - Product category
                            returned: on success
                            type: str
                            sample: product_category_example
                        ucm_rate_card_part_type:
                            description:
                                - Rate card part type of Product
                            returned: on success
                            type: str
                            sample: ucm_rate_card_part_type_example
                ar_invoice_number:
                    description:
                        - AR Invoice Number for Invoice Line
                    returned: on success
                    type: str
                    sample: ar_invoice_number_example
                data_center:
                    description:
                        - Data Center Attribute.
                    returned: on success
                    type: str
                    sample: data_center_example
                time_start:
                    description:
                        - Usage start time
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_end:
                    description:
                        - Usage end time
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "spm_invoice_number": "spm_invoice_number_example",
        "ar_invoices": "ar_invoices_example",
        "bill_to_customer": {
            "name": "name_example",
            "name_phonetic": "name_phonetic_example",
            "tca_customer_account_number": "tca_customer_account_number_example",
            "is_public_sector": true,
            "is_chain_customer": true,
            "customer_chain_type": "customer_chain_type_example",
            "tca_party_number": "tca_party_number_example",
            "tca_party_id": 56,
            "tca_customer_account_id": 56
        },
        "bill_to_contact": {
            "name": "name_example",
            "user_name": "user_name_example",
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "email": "email_example",
            "tca_contact_id": 56,
            "tca_cust_accnt_site_id": 56,
            "tca_party_id": 56
        },
        "bill_to_address": {
            "location": {
                "address1": "address1_example",
                "address2": "address2_example",
                "postal_code": "postal_code_example",
                "city": "city_example",
                "country": "country_example",
                "region": "us-phoenix-1",
                "tca_location_id": 56
            },
            "name": "name_example",
            "phone": "phone_example",
            "is_bill_to": true,
            "is_ship_to": true,
            "bill_site_use_id": 56,
            "service2_site_use_id": 56,
            "tca_cust_acct_site_id": 56,
            "tca_party_site_number": "tca_party_site_number_example"
        },
        "payment_method": "payment_method_example",
        "payment_term": {
            "name": "name_example",
            "value": "value_example",
            "description": "description_example",
            "is_active": true,
            "time_created": "2013-10-20T19:20:30+01:00",
            "created_by": "created_by_example",
            "time_updated": "2013-10-20T19:20:30+01:00",
            "updated_by": "updated_by_example"
        },
        "receipt_method": "receipt_method_example",
        "currency": {
            "name": "name_example",
            "iso_code": "iso_code_example",
            "std_precision": 56
        },
        "organization": {
            "name": "name_example",
            "number": 1.2
        },
        "type": "type_example",
        "status": "status_example",
        "subscription_number": "subscription_number_example",
        "time_invoice_date": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "updated_by": "updated_by_example",
        "invoice_lines": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "product": {
                "part_number": "part_number_example",
                "name": "name_example",
                "unit_of_measure": "unit_of_measure_example",
                "billing_category": "billing_category_example",
                "product_category": "product_category_example",
                "ucm_rate_card_part_type": "ucm_rate_card_part_type_example"
            },
            "ar_invoice_number": "ar_invoice_number_example",
            "data_center": "data_center_example",
            "time_start": "2013-10-20T19:20:30+01:00",
            "time_end": "2013-10-20T19:20:30+01:00"
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.onesubscription import InvoiceSummaryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InvoiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "ar_customer_transaction_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_from",
            "time_to",
            "sort_order",
            "sort_by",
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_invoices,
            compartment_id=self.module.params.get("compartment_id"),
            ar_customer_transaction_id=self.module.params.get(
                "ar_customer_transaction_id"
            ),
            **optional_kwargs
        )


InvoiceFactsHelperCustom = get_custom_class("InvoiceFactsHelperCustom")


class ResourceFactsHelper(InvoiceFactsHelperCustom, InvoiceFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            ar_customer_transaction_id=dict(type="str", required=True),
            time_from=dict(type="str"),
            time_to=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ORDERNUMBER", "TIMEINVOICING"]),
            fields=dict(type="list", elements="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="invoice",
        service_client_class=InvoiceSummaryClient,
        namespace="onesubscription",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(invoices=result)


if __name__ == "__main__":
    main()
