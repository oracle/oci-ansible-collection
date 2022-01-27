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
module: oci_osub_subscription_rate_card_facts
short_description: Fetches details about one or multiple RateCard resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple RateCard resources in Oracle Cloud Infrastructure
    - List API that returns all ratecards for given Subscription Id and Account ID (if provided) and
      for a particular date range
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    subscription_id:
        description:
            - Line level Subscription Id
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the compartment.
        type: str
        required: true
    time_from:
        description:
            - This param is used to get the rate card(s) whose effective start date starts on or after a particular date
        type: str
    time_to:
        description:
            - This param is used to get the rate card(s) whose effective end date ends on or before a particular date
        type: str
    part_number:
        description:
            - This param is used to get the rate card(s) filterd by the partNumber
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
            - "TIMECREATED"
            - "TIMESTART"
    x_one_origin_region:
        description:
            - The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List rate_cards
  oci_osub_subscription_rate_card_facts:
    # required
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_from: 2013-10-20T19:20:30+01:00
    time_to: 2013-10-20T19:20:30+01:00
    part_number: part_number_example
    sort_order: ASC
    sort_by: TIMECREATED
    x_one_origin_region: us-phoenix-1

"""

RETURN = """
rate_cards:
    description:
        - List of RateCard resources
    returned: on success
    type: complex
    contains:
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
    sample: [{
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
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.osub_subscription import RatecardClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RateCardFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "subscription_id",
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_from",
            "time_to",
            "part_number",
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
            self.client.list_rate_cards,
            subscription_id=self.module.params.get("subscription_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


RateCardFactsHelperCustom = get_custom_class("RateCardFactsHelperCustom")


class ResourceFactsHelper(RateCardFactsHelperCustom, RateCardFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            subscription_id=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            time_from=dict(type="str"),
            time_to=dict(type="str"),
            part_number=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "TIMESTART"]),
            x_one_origin_region=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="rate_card",
        service_client_class=RatecardClient,
        namespace="osub_subscription",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(rate_cards=result)


if __name__ == "__main__":
    main()
