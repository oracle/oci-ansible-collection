#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_osub_usage_computed_usage_facts
short_description: Fetches details about one or multiple ComputedUsage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ComputedUsage resources in Oracle Cloud Infrastructure
    - This is a collection API which returns a list of Computed Usages for given filters.
    - If I(computed_usage_id) is specified, the details of a single ComputedUsage will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    computed_usage_id:
        description:
            - The Computed Usage Id
            - Required to get a specific computed_usage.
        type: str
        aliases: ["id"]
    fields:
        description:
            - Partial response refers to an optimization technique offered
              by the RESTful web APIs to return only the information
              (fields) required by the client. This parameter is used to control what fields to
              return.
        type: list
        elements: str
    compartment_id:
        description:
            - The OCID of the root compartment.
        type: str
        required: true
    subscription_id:
        description:
            - Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM.
            - Required to list multiple computed_usages.
        type: str
    time_from:
        description:
            - Initial date to filter Computed Usage data in SPM. In the case of non aggregated data the time period between of fromDate and toDate , expressed
              in RFC 3339 timestamp format.
            - Required to list multiple computed_usages.
        type: str
    time_to:
        description:
            - Final date to filter Computed Usage data in SPM, expressed in RFC 3339 timestamp format.
            - Required to list multiple computed_usages.
        type: str
    parent_product:
        description:
            - Product part number for subscribed service line, called parent product.
        type: str
    computed_product:
        description:
            - Product part number for Computed Usage .
        type: str
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
            - "timeCreated"
            - "timeOfArrival"
            - "timeMeteredOn"
    x_one_origin_region:
        description:
            - The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific computed_usage
  oci_osub_usage_computed_usage_facts:
    # required
    computed_usage_id: "ocid1.computedusage.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    fields: [ "fields_example" ]
    x_one_origin_region: us-phoenix-1

- name: List computed_usages
  oci_osub_usage_computed_usage_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    time_from: 2013-10-20T19:20:30+01:00
    time_to: 2013-10-20T19:20:30+01:00

    # optional
    parent_product: parent_product_example
    computed_product: computed_product_example
    sort_order: ASC
    sort_by: timeCreated
    x_one_origin_region: us-phoenix-1

"""

RETURN = """
computed_usages:
    description:
        - List of ComputedUsage resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - SPM Internal computed usage Id , 32 character string
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - Computed Usage created time, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - Computed Usage updated time, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        parent_subscribed_service_id:
            description:
                - Subscribed service line parent id
            returned: on success
            type: str
            sample: "ocid1.parentsubscribedservice.oc1..xxxxxxEXAMPLExxxxxx"
        parent_product:
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
                provisioning_group:
                    description:
                        - Product provisioning group
                    returned: on success
                    type: str
                    sample: provisioning_group_example
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
        plan_number:
            description:
                - Subscription plan number
            returned: on success
            type: str
            sample: plan_number_example
        currency_code:
            description:
                - Currency code
            returned: on success
            type: str
            sample: currency_code_example
        rate_card_tierd_id:
            description:
                - References the tier in the ratecard for that usage (OCI will be using the same reference to cross-reference for correctness on the usage csv
                  report), comes from Entity OBSCNTR_IPT_PRODUCTTIER.
            returned: on success
            type: str
            sample: "ocid1.ratecardtierd.oc1..xxxxxxEXAMPLExxxxxx"
        rate_card_id:
            description:
                - Ratecard Id at subscribed service level
            returned: on success
            type: str
            sample: "ocid1.ratecard.oc1..xxxxxxEXAMPLExxxxxx"
        compute_source:
            description:
                - SPM Internal compute records source .
            returned: on success
            type: str
            sample: compute_source_example
        data_center:
            description:
                - Data Center Attribute as sent by MQS to SPM.
            returned: on success
            type: str
            sample: data_center_example
        mqs_message_id:
            description:
                - MQS Identfier send to SPM , SPM does not transform this attribute and is received as is.
            returned: on success
            type: str
            sample: "ocid1.mqsmessage.oc1..xxxxxxEXAMPLExxxxxx"
        computed_usage_id:
            description:
                - SPM Internal computed usage Id , 32 character string
                - Returned for list operation
            returned: on success
            type: str
            sample: "ocid1.computedusage.oc1..xxxxxxEXAMPLExxxxxx"
        quantity:
            description:
                - Total Quantity that was used for computation
            returned: on success
            type: str
            sample: quantity_example
        usage_number:
            description:
                - SPM Internal usage Line number identifier in SPM coming from Metered Services entity.
            returned: on success
            type: str
            sample: usage_number_example
        original_usage_number:
            description:
                - SPM Internal Original usage Line number identifier in SPM coming from Metered Services entity.
            returned: on success
            type: str
            sample: original_usage_number_example
        commitment_service_id:
            description:
                - Subscribed service commitmentId.
            returned: on success
            type: str
            sample: "ocid1.commitmentservice.oc1..xxxxxxEXAMPLExxxxxx"
        is_invoiced:
            description:
                - Invoicing status for the aggregated compute usage
            returned: on success
            type: bool
            sample: true
        type:
            description:
                - Usage compute type in SPM.
            returned: on success
            type: str
            sample: PROMOTION
        time_of_arrival:
            description:
                - Usae computation date, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_metered_on:
            description:
                - Metered Service date, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        net_unit_price:
            description:
                - Net Unit Price for the product in consideration, price actual.
            returned: on success
            type: str
            sample: net_unit_price_example
        cost_rounded:
            description:
                - Computed Line Amount rounded.
            returned: on success
            type: str
            sample: cost_rounded_example
        cost:
            description:
                - Computed Line Amount not rounded
            returned: on success
            type: str
            sample: cost_example
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
                provisioning_group:
                    description:
                        - Product provisioning group
                    returned: on success
                    type: str
                    sample: provisioning_group_example
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
        unit_of_measure:
            description:
                - Unit of Messure
            returned: on success
            type: str
            sample: unit_of_measure_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "parent_subscribed_service_id": "ocid1.parentsubscribedservice.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_product": {
            "part_number": "part_number_example",
            "name": "name_example",
            "unit_of_measure": "unit_of_measure_example",
            "provisioning_group": "provisioning_group_example",
            "billing_category": "billing_category_example",
            "product_category": "product_category_example",
            "ucm_rate_card_part_type": "ucm_rate_card_part_type_example"
        },
        "plan_number": "plan_number_example",
        "currency_code": "currency_code_example",
        "rate_card_tierd_id": "ocid1.ratecardtierd.oc1..xxxxxxEXAMPLExxxxxx",
        "rate_card_id": "ocid1.ratecard.oc1..xxxxxxEXAMPLExxxxxx",
        "compute_source": "compute_source_example",
        "data_center": "data_center_example",
        "mqs_message_id": "ocid1.mqsmessage.oc1..xxxxxxEXAMPLExxxxxx",
        "computed_usage_id": "ocid1.computedusage.oc1..xxxxxxEXAMPLExxxxxx",
        "quantity": "quantity_example",
        "usage_number": "usage_number_example",
        "original_usage_number": "original_usage_number_example",
        "commitment_service_id": "ocid1.commitmentservice.oc1..xxxxxxEXAMPLExxxxxx",
        "is_invoiced": true,
        "type": "PROMOTION",
        "time_of_arrival": "2013-10-20T19:20:30+01:00",
        "time_metered_on": "2013-10-20T19:20:30+01:00",
        "net_unit_price": "net_unit_price_example",
        "cost_rounded": "cost_rounded_example",
        "cost": "cost_example",
        "product": {
            "part_number": "part_number_example",
            "name": "name_example",
            "unit_of_measure": "unit_of_measure_example",
            "provisioning_group": "provisioning_group_example",
            "billing_category": "billing_category_example",
            "product_category": "product_category_example",
            "ucm_rate_card_part_type": "ucm_rate_card_part_type_example"
        },
        "unit_of_measure": "unit_of_measure_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osub_usage import ComputedUsageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputedUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "computed_usage_id",
            "compartment_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "subscription_id",
            "time_from",
            "time_to",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "fields",
            "x_one_origin_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_computed_usage,
            computed_usage_id=self.module.params.get("computed_usage_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "parent_product",
            "computed_product",
            "sort_order",
            "sort_by",
            "x_one_origin_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_computed_usages,
            compartment_id=self.module.params.get("compartment_id"),
            subscription_id=self.module.params.get("subscription_id"),
            time_from=self.module.params.get("time_from"),
            time_to=self.module.params.get("time_to"),
            **optional_kwargs
        )


ComputedUsageFactsHelperCustom = get_custom_class("ComputedUsageFactsHelperCustom")


class ResourceFactsHelper(ComputedUsageFactsHelperCustom, ComputedUsageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            computed_usage_id=dict(aliases=["id"], type="str"),
            fields=dict(type="list", elements="str"),
            compartment_id=dict(type="str", required=True),
            subscription_id=dict(type="str"),
            time_from=dict(type="str"),
            time_to=dict(type="str"),
            parent_product=dict(type="str"),
            computed_product=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeCreated", "timeOfArrival", "timeMeteredOn"]
            ),
            x_one_origin_region=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="computed_usage",
        service_client_class=ComputedUsageClient,
        namespace="osub_usage",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(computed_usages=result)


if __name__ == "__main__":
    main()
