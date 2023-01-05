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
module: oci_onesubscription_subscribed_service_facts
short_description: Fetches details about one or multiple SubscribedService resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SubscribedService resources in Oracle Cloud Infrastructure
    - This list API returns all subscribed services for given Subscription ID
    - If I(subscribed_service_id) is specified, the details of a single SubscribedService will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    subscribed_service_id:
        description:
            - The Subscribed Service Id
            - Required to get a specific subscribed_service.
        type: str
        aliases: ["id"]
    fields:
        description:
            - "Partial response refers to an optimization technique offered
              by the RESTful web APIs to return only the information
              (fields) required by the client. In this mechanism, the client
              sends the required field names as the query parameters for
              an API to the server, and the server trims down the default
              response content by removing the fields that are not required
              by the client. The parameter used to control what fields to
              return should be a query string parameter called \\"fields\\" of
              type array, and usecollectionFormat"
        type: list
        elements: str
    compartment_id:
        description:
            - The OCID of the root compartment.
            - Required to list multiple subscribed_services.
        type: str
    subscription_id:
        description:
            - Line level Subscription Id
            - Required to list multiple subscribed_services.
        type: str
    order_line_id:
        description:
            - Order Line identifier at subscribed service level . This identifier is originated in Order Management module. Default is null.
        type: int
    status:
        description:
            - This param is used to filter subscribed services based on its status
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific subscribed_service
  oci_onesubscription_subscribed_service_facts:
    # required
    subscribed_service_id: "ocid1.subscribedservice.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    fields: [ "fields_example" ]

- name: List subscribed_services
  oci_onesubscription_subscribed_service_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    order_line_id: 56
    status: status_example
    sort_order: ASC
    sort_by: ORDERNUMBER

"""

RETURN = """
subscribed_services:
    description:
        - List of SubscribedService resources
    returned: on success
    type: complex
    contains:
        commitment_services:
            description:
                - List of Commitment services of a line
                - Returned for get operation
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
        rate_cards:
            description:
                - List of Rate Cards of a Subscribed Service
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                subscribed_service_id:
                    description:
                        - SPM internal Subscribed Service ID
                    returned: on success
                    type: str
                    sample: "ocid1.subscribedservice.oc1..xxxxxxEXAMPLExxxxxx"
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
                time_start:
                    description:
                        - Rate card start date
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                time_end:
                    description:
                        - Rate card end date
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                net_unit_price:
                    description:
                        - Rate card net unit price
                    returned: on success
                    type: str
                    sample: net_unit_price_example
                discretionary_discount_percentage:
                    description:
                        - Rate card discretionary discount percentage
                    returned: on success
                    type: str
                    sample: discretionary_discount_percentage_example
                overage_price:
                    description:
                        - Rate card overage price
                    returned: on success
                    type: str
                    sample: overage_price_example
                is_tier:
                    description:
                        - Rate card price tier flag
                    returned: on success
                    type: bool
                    sample: true
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
                rate_card_tiers:
                    description:
                        - List of tiered rate card prices
                    returned: on success
                    type: complex
                    contains:
                        up_to_quantity:
                            description:
                                - Rate card tier quantity range
                            returned: on success
                            type: str
                            sample: up_to_quantity_example
                        net_unit_price:
                            description:
                                - Rate card tier net unit price
                            returned: on success
                            type: str
                            sample: net_unit_price_example
                        overage_price:
                            description:
                                - Rate card tier overage price
                            returned: on success
                            type: str
                            sample: overage_price_example
        id:
            description:
                - SPM internal Subscribed Service ID
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        type:
            description:
                - Subscribed Service line type
            returned: on success
            type: str
            sample: type_example
        serial_number:
            description:
                - Subscribed service line number
            returned: on success
            type: str
            sample: serial_number_example
        subscription_id:
            description:
                - Subscription ID associated to the subscribed service
            returned: on success
            type: str
            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
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
        price_period:
            description:
                - Indicates the period for which the commitment amount can be utilised exceeding which the amount lapses. Also used in calculation of total
                  contract line value
            returned: on success
            type: str
            sample: price_period_example
        line_net_amount:
            description:
                - Subscribed service line net amount
            returned: on success
            type: str
            sample: line_net_amount_example
        is_variable_commitment:
            description:
                - Indicates if the commitment lines can have different quantities
            returned: on success
            type: bool
            sample: true
        is_allowance:
            description:
                - Indicates if a service can recieve usages and consequently have available amounts computed
            returned: on success
            type: bool
            sample: true
        used_amount:
            description:
                - Subscribed service used amount
            returned: on success
            type: str
            sample: used_amount_example
        available_amount:
            description:
                - Subscribed sercice available or remaining amount
            returned: on success
            type: str
            sample: available_amount_example
        funded_allocation_value:
            description:
                - "Funded Allocation line value
                  example: 12000.00"
            returned: on success
            type: str
            sample: funded_allocation_value_example
        is_having_usage:
            description:
                - Indicator on whether or not there has been usage for the subscribed service
            returned: on success
            type: bool
            sample: true
        is_cap_to_price_list:
            description:
                - If true compares rate between ratecard and the active pricelist and minimum rate would be fetched
            returned: on success
            type: bool
            sample: true
        credit_percentage:
            description:
                - Subscribed service credit percentage
            returned: on success
            type: str
            sample: credit_percentage_example
        partner_transaction_type:
            description:
                - "This field contains the name of the partner to which the subscription belongs - depending on which the invoicing may differ"
            returned: on success
            type: str
            sample: partner_transaction_type_example
        is_credit_enabled:
            description:
                - Used in context of service credit lines
            returned: on success
            type: bool
            sample: true
        overage_policy:
            description:
                - Overage Policy of Subscribed Service
            returned: on success
            type: str
            sample: overage_policy_example
        overage_bill_to:
            description:
                - Overage Bill To of Subscribed Service
            returned: on success
            type: str
            sample: overage_bill_to_example
        payg_policy:
            description:
                - "Pay As You Go policy of Subscribed Service (Can be null - indicating no payg policy)"
            returned: on success
            type: str
            sample: payg_policy_example
        promo_order_line_id:
            description:
                - Not null if this service has an associated promotion line in SPM. Contains the line identifier from Order Management of
                  the associated promo line.
            returned: on success
            type: int
            sample: 56
        promotion_pricing_type:
            description:
                - "Promotion Pricing Type of Subscribed Service (Can be null - indicating no promotion pricing)"
            returned: on success
            type: str
            sample: promotion_pricing_type_example
        rate_card_discount_percentage:
            description:
                - Subscribed service Rate Card Discount Percentage
            returned: on success
            type: str
            sample: rate_card_discount_percentage_example
        overage_discount_percentage:
            description:
                - Subscribed service Overage Discount Percentage
            returned: on success
            type: str
            sample: overage_discount_percentage_example
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
                tca_cust_account_number:
                    description:
                        - TCA customer account number.
                    returned: on success
                    type: str
                    sample: tca_cust_account_number_example
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
                username:
                    description:
                        - Username.
                    returned: on success
                    type: str
                    sample: username_example
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
                                - Region.
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
                        - Identify as the customer shipping address.
                    returned: on success
                    type: bool
                    sample: true
                is_ship_to:
                    description:
                        - Identify as the customer invoicing address.
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
        payment_number:
            description:
                - Payment Number of Subscribed Service
            returned: on success
            type: str
            sample: payment_number_example
        time_payment_expiry:
            description:
                - Subscribed service payment expiry date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
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
        payment_method:
            description:
                - Payment Method of Subscribed Service
            returned: on success
            type: str
            sample: payment_method_example
        transaction_extension_id:
            description:
                - Subscribed service Transaction Extension Id
            returned: on success
            type: int
            sample: 56
        sales_channel:
            description:
                - Sales Channel of Subscribed Service
            returned: on success
            type: str
            sample: sales_channel_example
        eligible_to_renew:
            description:
                - Subscribed service eligible to renew field
            returned: on success
            type: str
            sample: eligible_to_renew_example
        renewed_subscribed_service_id:
            description:
                - SPM renewed Subscription ID
            returned: on success
            type: str
            sample: "ocid1.renewedsubscribedservice.oc1..xxxxxxEXAMPLExxxxxx"
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
        renewal_opty_id:
            description:
                - Subscribed service Opportunity Id
            returned: on success
            type: int
            sample: 56
        renewal_opty_number:
            description:
                - Renewal Opportunity Number of Subscribed Service
            returned: on success
            type: str
            sample: renewal_opty_number_example
        renewal_opty_type:
            description:
                - Renewal Opportunity Type of Subscribed Service
            returned: on success
            type: str
            sample: renewal_opty_type_example
        booking_opty_number:
            description:
                - Booking Opportunity Number of Subscribed Service
            returned: on success
            type: str
            sample: booking_opty_number_example
        revenue_line_id:
            description:
                - Subscribed service Revenue Line Id
            returned: on success
            type: int
            sample: 56
        revenue_line_number:
            description:
                - Revenue Line NUmber of Subscribed Service
            returned: on success
            type: str
            sample: revenue_line_number_example
        major_set:
            description:
                - Subscribed service Major Set
            returned: on success
            type: int
            sample: 56
        time_majorset_start:
            description:
                - Subscribed service Major Set Start date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_majorset_end:
            description:
                - Subscribed service Major Set End date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        system_arr_in_lc:
            description:
                - Subscribed service System ARR
            returned: on success
            type: str
            sample: system_arr_in_lc_example
        system_arr_in_sc:
            description:
                - Subscribed service System ARR in Standard Currency
            returned: on success
            type: str
            sample: system_arr_in_sc_example
        system_atr_arr_in_lc:
            description:
                - Subscribed service System ATR-ARR
            returned: on success
            type: str
            sample: system_atr_arr_in_lc_example
        system_atr_arr_in_sc:
            description:
                - Subscribed service System ATR-ARR in Standard Currency
            returned: on success
            type: str
            sample: system_atr_arr_in_sc_example
        revised_arr_in_lc:
            description:
                - Subscribed service Revised ARR
            returned: on success
            type: str
            sample: revised_arr_in_lc_example
        revised_arr_in_sc:
            description:
                - Subscribed service Revised ARR in Standard Currency
            returned: on success
            type: str
            sample: revised_arr_in_sc_example
        total_value:
            description:
                - Subscribed service total value
            returned: on success
            type: str
            sample: total_value_example
        original_promo_amount:
            description:
                - Subscribed service Promotion Amount
            returned: on success
            type: str
            sample: original_promo_amount_example
        order_header_id:
            description:
                - Sales Order Header associated to the subscribed service
            returned: on success
            type: int
            sample: 56
        order_number:
            description:
                - Sales Order Number associated to the subscribed service
            returned: on success
            type: int
            sample: 56
        order_type:
            description:
                - Order Type of Subscribed Service
            returned: on success
            type: str
            sample: order_type_example
        order_line_id:
            description:
                - Sales Order Line Id associated to the subscribed service
            returned: on success
            type: int
            sample: 56
        order_line_number:
            description:
                - Sales Order Line Number associated to the subscribed service
            returned: on success
            type: int
            sample: 56
        commitment_schedule_id:
            description:
                - Subscribed service commitment schedule Id
            returned: on success
            type: str
            sample: "ocid1.commitmentschedule.oc1..xxxxxxEXAMPLExxxxxx"
        sales_account_party_id:
            description:
                - Subscribed service sales account party id
            returned: on success
            type: int
            sample: 56
        data_center:
            description:
                - Subscribed service data center
            returned: on success
            type: str
            sample: data_center_example
        data_center_region:
            description:
                - Subscribed service data center region
            returned: on success
            type: str
            sample: us-phoenix-1
        admin_email:
            description:
                - Subscribed service admin email id
            returned: on success
            type: str
            sample: admin_email_example
        buyer_email:
            description:
                - Subscribed service buyer email id
            returned: on success
            type: str
            sample: buyer_email_example
        subscription_source:
            description:
                - Subscribed service source
            returned: on success
            type: str
            sample: subscription_source_example
        provisioning_source:
            description:
                - Subscribed service provisioning source
            returned: on success
            type: str
            sample: provisioning_source_example
        fulfillment_set:
            description:
                - Subscribed service fulfillment set
            returned: on success
            type: str
            sample: fulfillment_set_example
        is_intent_to_pay:
            description:
                - Subscribed service intent to pay flag
            returned: on success
            type: bool
            sample: true
        is_payg:
            description:
                - Subscribed service payg flag
            returned: on success
            type: bool
            sample: true
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
        start_date_type:
            description:
                - Subscribed service start date type
            returned: on success
            type: str
            sample: start_date_type_example
        time_provisioned:
            description:
                - Subscribed service provisioning date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        promo_type:
            description:
                - Subscribed service promotion type
            returned: on success
            type: str
            sample: promo_type_example
        service_to_customer:
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
                tca_cust_account_number:
                    description:
                        - TCA customer account number.
                    returned: on success
                    type: str
                    sample: tca_cust_account_number_example
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
        service_to_contact:
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
                username:
                    description:
                        - Username.
                    returned: on success
                    type: str
                    sample: username_example
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
        service_to_address:
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
                                - Region.
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
                        - Identify as the customer shipping address.
                    returned: on success
                    type: bool
                    sample: true
                is_ship_to:
                    description:
                        - Identify as the customer invoicing address.
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
        sold_to_customer:
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
                tca_cust_account_number:
                    description:
                        - TCA customer account number.
                    returned: on success
                    type: str
                    sample: tca_cust_account_number_example
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
        sold_to_contact:
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
                username:
                    description:
                        - Username.
                    returned: on success
                    type: str
                    sample: username_example
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
        end_user_customer:
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
                tca_cust_account_number:
                    description:
                        - TCA customer account number.
                    returned: on success
                    type: str
                    sample: tca_cust_account_number_example
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
        end_user_contact:
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
                username:
                    description:
                        - Username.
                    returned: on success
                    type: str
                    sample: username_example
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
        end_user_address:
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
                                - Region.
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
                        - Identify as the customer shipping address.
                    returned: on success
                    type: bool
                    sample: true
                is_ship_to:
                    description:
                        - Identify as the customer invoicing address.
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
        reseller_customer:
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
                tca_cust_account_number:
                    description:
                        - TCA customer account number.
                    returned: on success
                    type: str
                    sample: tca_cust_account_number_example
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
        reseller_contact:
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
                username:
                    description:
                        - Username.
                    returned: on success
                    type: str
                    sample: username_example
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
        reseller_address:
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
                                - Region.
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
                        - Identify as the customer shipping address.
                    returned: on success
                    type: bool
                    sample: true
                is_ship_to:
                    description:
                        - Identify as the customer invoicing address.
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
        csi:
            description:
                - Subscribed service CSI number
            returned: on success
            type: int
            sample: 56
        customer_transaction_reference:
            description:
                - Identifier for a customer's transactions for purchase of ay oracle services
            returned: on success
            type: str
            sample: customer_transaction_reference_example
        partner_credit_amount:
            description:
                - Subscribed service partner credit amount
            returned: on success
            type: str
            sample: partner_credit_amount_example
        is_single_rate_card:
            description:
                - Indicates if the Subscribed service has a single ratecard
            returned: on success
            type: bool
            sample: true
        agreement_id:
            description:
                - Subscribed service agreement ID
            returned: on success
            type: int
            sample: 56
        agreement_name:
            description:
                - Subscribed service agrrement name
            returned: on success
            type: str
            sample: agreement_name_example
        agreement_type:
            description:
                - Subscribed service agrrement type
            returned: on success
            type: str
            sample: agreement_type_example
        billing_frequency:
            description:
                - Subscribed service invoice frequency
            returned: on success
            type: str
            sample: billing_frequency_example
        time_welcome_email_sent:
            description:
                - Subscribed service welcome email sent date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_service_configuration_email_sent:
            description:
                - Subscribed service service configuration email sent date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_customer_config:
            description:
                - Subscribed service customer config date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_agreement_end:
            description:
                - Subscribed service agrrement end date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_created:
            description:
                - Subscribed service creation date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        created_by:
            description:
                - User that created the subscribed service
            returned: on success
            type: str
            sample: created_by_example
        time_updated:
            description:
                - Subscribed service last update date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        updated_by:
            description:
                - User that updated the subscribed service
            returned: on success
            type: str
            sample: updated_by_example
        ratecard_type:
            description:
                - SPM Ratecard Type
            returned: on success
            type: str
            sample: ratecard_type_example
    sample: [{
        "commitment_services": [{
            "time_start": "2013-10-20T19:20:30+01:00",
            "time_end": "2013-10-20T19:20:30+01:00",
            "quantity": "quantity_example",
            "available_amount": "available_amount_example",
            "line_net_amount": "line_net_amount_example",
            "funded_allocation_value": "funded_allocation_value_example"
        }],
        "rate_cards": [{
            "subscribed_service_id": "ocid1.subscribedservice.oc1..xxxxxxEXAMPLExxxxxx",
            "product": {
                "part_number": "part_number_example",
                "name": "name_example",
                "unit_of_measure": "unit_of_measure_example",
                "billing_category": "billing_category_example",
                "product_category": "product_category_example",
                "ucm_rate_card_part_type": "ucm_rate_card_part_type_example"
            },
            "time_start": "2013-10-20T19:20:30+01:00",
            "time_end": "2013-10-20T19:20:30+01:00",
            "net_unit_price": "net_unit_price_example",
            "discretionary_discount_percentage": "discretionary_discount_percentage_example",
            "overage_price": "overage_price_example",
            "is_tier": true,
            "currency": {
                "name": "name_example",
                "iso_code": "iso_code_example",
                "std_precision": 56
            },
            "rate_card_tiers": [{
                "up_to_quantity": "up_to_quantity_example",
                "net_unit_price": "net_unit_price_example",
                "overage_price": "overage_price_example"
            }]
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "type": "type_example",
        "serial_number": "serial_number_example",
        "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx",
        "product": {
            "part_number": "part_number_example",
            "name": "name_example",
            "unit_of_measure": "unit_of_measure_example",
            "billing_category": "billing_category_example",
            "product_category": "product_category_example",
            "ucm_rate_card_part_type": "ucm_rate_card_part_type_example"
        },
        "time_start": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "quantity": "quantity_example",
        "status": "status_example",
        "operation_type": "operation_type_example",
        "net_unit_price": "net_unit_price_example",
        "price_period": "price_period_example",
        "line_net_amount": "line_net_amount_example",
        "is_variable_commitment": true,
        "is_allowance": true,
        "used_amount": "used_amount_example",
        "available_amount": "available_amount_example",
        "funded_allocation_value": "funded_allocation_value_example",
        "is_having_usage": true,
        "is_cap_to_price_list": true,
        "credit_percentage": "credit_percentage_example",
        "partner_transaction_type": "partner_transaction_type_example",
        "is_credit_enabled": true,
        "overage_policy": "overage_policy_example",
        "overage_bill_to": "overage_bill_to_example",
        "payg_policy": "payg_policy_example",
        "promo_order_line_id": 56,
        "promotion_pricing_type": "promotion_pricing_type_example",
        "rate_card_discount_percentage": "rate_card_discount_percentage_example",
        "overage_discount_percentage": "overage_discount_percentage_example",
        "bill_to_customer": {
            "name": "name_example",
            "name_phonetic": "name_phonetic_example",
            "tca_cust_account_number": "tca_cust_account_number_example",
            "is_public_sector": true,
            "is_chain_customer": true,
            "customer_chain_type": "customer_chain_type_example",
            "tca_party_number": "tca_party_number_example",
            "tca_party_id": 56,
            "tca_customer_account_id": 56
        },
        "bill_to_contact": {
            "name": "name_example",
            "username": "username_example",
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
        "payment_number": "payment_number_example",
        "time_payment_expiry": "2013-10-20T19:20:30+01:00",
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
        "payment_method": "payment_method_example",
        "transaction_extension_id": 56,
        "sales_channel": "sales_channel_example",
        "eligible_to_renew": "eligible_to_renew_example",
        "renewed_subscribed_service_id": "ocid1.renewedsubscribedservice.oc1..xxxxxxEXAMPLExxxxxx",
        "term_value": 56,
        "term_value_uom": "term_value_uom_example",
        "renewal_opty_id": 56,
        "renewal_opty_number": "renewal_opty_number_example",
        "renewal_opty_type": "renewal_opty_type_example",
        "booking_opty_number": "booking_opty_number_example",
        "revenue_line_id": 56,
        "revenue_line_number": "revenue_line_number_example",
        "major_set": 56,
        "time_majorset_start": "2013-10-20T19:20:30+01:00",
        "time_majorset_end": "2013-10-20T19:20:30+01:00",
        "system_arr_in_lc": "system_arr_in_lc_example",
        "system_arr_in_sc": "system_arr_in_sc_example",
        "system_atr_arr_in_lc": "system_atr_arr_in_lc_example",
        "system_atr_arr_in_sc": "system_atr_arr_in_sc_example",
        "revised_arr_in_lc": "revised_arr_in_lc_example",
        "revised_arr_in_sc": "revised_arr_in_sc_example",
        "total_value": "total_value_example",
        "original_promo_amount": "original_promo_amount_example",
        "order_header_id": 56,
        "order_number": 56,
        "order_type": "order_type_example",
        "order_line_id": 56,
        "order_line_number": 56,
        "commitment_schedule_id": "ocid1.commitmentschedule.oc1..xxxxxxEXAMPLExxxxxx",
        "sales_account_party_id": 56,
        "data_center": "data_center_example",
        "data_center_region": "us-phoenix-1",
        "admin_email": "admin_email_example",
        "buyer_email": "buyer_email_example",
        "subscription_source": "subscription_source_example",
        "provisioning_source": "provisioning_source_example",
        "fulfillment_set": "fulfillment_set_example",
        "is_intent_to_pay": true,
        "is_payg": true,
        "pricing_model": "pricing_model_example",
        "program_type": "program_type_example",
        "start_date_type": "start_date_type_example",
        "time_provisioned": "2013-10-20T19:20:30+01:00",
        "promo_type": "promo_type_example",
        "service_to_customer": {
            "name": "name_example",
            "name_phonetic": "name_phonetic_example",
            "tca_cust_account_number": "tca_cust_account_number_example",
            "is_public_sector": true,
            "is_chain_customer": true,
            "customer_chain_type": "customer_chain_type_example",
            "tca_party_number": "tca_party_number_example",
            "tca_party_id": 56,
            "tca_customer_account_id": 56
        },
        "service_to_contact": {
            "name": "name_example",
            "username": "username_example",
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "email": "email_example",
            "tca_contact_id": 56,
            "tca_cust_accnt_site_id": 56,
            "tca_party_id": 56
        },
        "service_to_address": {
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
        "sold_to_customer": {
            "name": "name_example",
            "name_phonetic": "name_phonetic_example",
            "tca_cust_account_number": "tca_cust_account_number_example",
            "is_public_sector": true,
            "is_chain_customer": true,
            "customer_chain_type": "customer_chain_type_example",
            "tca_party_number": "tca_party_number_example",
            "tca_party_id": 56,
            "tca_customer_account_id": 56
        },
        "sold_to_contact": {
            "name": "name_example",
            "username": "username_example",
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "email": "email_example",
            "tca_contact_id": 56,
            "tca_cust_accnt_site_id": 56,
            "tca_party_id": 56
        },
        "end_user_customer": {
            "name": "name_example",
            "name_phonetic": "name_phonetic_example",
            "tca_cust_account_number": "tca_cust_account_number_example",
            "is_public_sector": true,
            "is_chain_customer": true,
            "customer_chain_type": "customer_chain_type_example",
            "tca_party_number": "tca_party_number_example",
            "tca_party_id": 56,
            "tca_customer_account_id": 56
        },
        "end_user_contact": {
            "name": "name_example",
            "username": "username_example",
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "email": "email_example",
            "tca_contact_id": 56,
            "tca_cust_accnt_site_id": 56,
            "tca_party_id": 56
        },
        "end_user_address": {
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
        "reseller_customer": {
            "name": "name_example",
            "name_phonetic": "name_phonetic_example",
            "tca_cust_account_number": "tca_cust_account_number_example",
            "is_public_sector": true,
            "is_chain_customer": true,
            "customer_chain_type": "customer_chain_type_example",
            "tca_party_number": "tca_party_number_example",
            "tca_party_id": 56,
            "tca_customer_account_id": 56
        },
        "reseller_contact": {
            "name": "name_example",
            "username": "username_example",
            "first_name": "first_name_example",
            "last_name": "last_name_example",
            "email": "email_example",
            "tca_contact_id": 56,
            "tca_cust_accnt_site_id": 56,
            "tca_party_id": 56
        },
        "reseller_address": {
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
        "csi": 56,
        "customer_transaction_reference": "customer_transaction_reference_example",
        "partner_credit_amount": "partner_credit_amount_example",
        "is_single_rate_card": true,
        "agreement_id": 56,
        "agreement_name": "agreement_name_example",
        "agreement_type": "agreement_type_example",
        "billing_frequency": "billing_frequency_example",
        "time_welcome_email_sent": "2013-10-20T19:20:30+01:00",
        "time_service_configuration_email_sent": "2013-10-20T19:20:30+01:00",
        "time_customer_config": "2013-10-20T19:20:30+01:00",
        "time_agreement_end": "2013-10-20T19:20:30+01:00",
        "time_created": "2013-10-20T19:20:30+01:00",
        "created_by": "created_by_example",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "updated_by": "updated_by_example",
        "ratecard_type": "ratecard_type_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.onesubscription import SubscribedServiceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SubscribedServiceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "subscribed_service_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "subscription_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_subscribed_service,
            subscribed_service_id=self.module.params.get("subscribed_service_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "order_line_id",
            "status",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_subscribed_services,
            compartment_id=self.module.params.get("compartment_id"),
            subscription_id=self.module.params.get("subscription_id"),
            **optional_kwargs
        )


SubscribedServiceFactsHelperCustom = get_custom_class(
    "SubscribedServiceFactsHelperCustom"
)


class ResourceFactsHelper(
    SubscribedServiceFactsHelperCustom, SubscribedServiceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            subscribed_service_id=dict(aliases=["id"], type="str"),
            fields=dict(type="list", elements="str"),
            compartment_id=dict(type="str"),
            subscription_id=dict(type="str"),
            order_line_id=dict(type="int"),
            status=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ORDERNUMBER", "TIMEINVOICING"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="subscribed_service",
        service_client_class=SubscribedServiceClient,
        namespace="onesubscription",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(subscribed_services=result)


if __name__ == "__main__":
    main()
