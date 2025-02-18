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
module: oci_osub_usage_computed_usage_aggregated_facts
short_description: Fetches details about one or multiple ComputedUsageAggregated resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ComputedUsageAggregated resources in Oracle Cloud Infrastructure
    - "This is a collection API which returns a list of aggregated computed usage details (there can be multiple Parent Products under a given SubID each of
      which is represented under Subscription Service Line # in SPM)."
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the root compartment.
        type: str
        required: true
    subscription_id:
        description:
            - Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM.
        type: str
        required: true
    time_from:
        description:
            - Initial date to filter Computed Usage data in SPM. In the case of non aggregated data the time period between of fromDate and toDate , expressed
              in RFC 3339 timestamp format.
        type: str
        required: true
    time_to:
        description:
            - Final date to filter Computed Usage data in SPM, expressed in RFC 3339 timestamp format.
        type: str
        required: true
    parent_product:
        description:
            - Product part number for subscribed service line, called parent product.
        type: str
    grouping:
        description:
            - Grouping criteria to use for aggregate the computed Usage, either hourly (`HOURLY`), daily (`DAILY`), monthly(`MONTHLY`) or none (`NONE`) to not
              follow a grouping criteria by date.
        type: str
        choices:
            - "HOURLY"
            - "DAILY"
            - "MONTHLY"
            - "NONE"
    x_one_origin_region:
        description:
            - The OCI home region name in case home region is not us-ashburn-1 (IAD), e.g. ap-mumbai-1, us-phoenix-1 etc.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List computed_usage_aggregateds
  oci_osub_usage_computed_usage_aggregated_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    time_from: 2013-10-20T19:20:30+01:00
    time_to: 2013-10-20T19:20:30+01:00

    # optional
    parent_product: parent_product_example
    grouping: HOURLY
    x_one_origin_region: us-phoenix-1

"""

RETURN = """
computed_usage_aggregateds:
    description:
        - List of ComputedUsageAggregated resources
    returned: on success
    type: complex
    contains:
        subscription_id:
            description:
                - Subscription Id is an identifier associated to the service used for filter the Computed Usage in SPM
            returned: on success
            type: str
            sample: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
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
        time_start:
            description:
                - Subscribed services contract line start date, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - Subscribed services contract line end date, expressed in RFC 3339 timestamp format.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        plan_number:
            description:
                - Subscribed service asociated subscription plan number.
            returned: on success
            type: str
            sample: plan_number_example
        currency_code:
            description:
                - Currency code
            returned: on success
            type: str
            sample: currency_code_example
        rate_card_id:
            description:
                - Inernal SPM Ratecard Id at line level
            returned: on success
            type: str
            sample: "ocid1.ratecard.oc1..xxxxxxEXAMPLExxxxxx"
        pricing_model:
            description:
                - Subscribed services pricing model
            returned: on success
            type: str
            sample: PAY_AS_YOU_GO
        aggregated_computed_usages:
            description:
                - Aggregation of computed usages for the subscribed service.
            returned: on success
            type: complex
            contains:
                quantity:
                    description:
                        - Total Quantity that was used for computation
                    returned: on success
                    type: str
                    sample: quantity_example
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
                data_center:
                    description:
                        - Data Center Attribute as sent by MQS to SPM.
                    returned: on success
                    type: str
                    sample: data_center_example
                time_metered_on:
                    description:
                        - Metered Service date , expressed in RFC 3339 timestamp format.
                    returned: on success
                    type: str
                    sample: "2013-10-20T19:20:30+01:00"
                net_unit_price:
                    description:
                        - Net Unit Price for the product in consideration.
                    returned: on success
                    type: str
                    sample: net_unit_price_example
                cost_unrounded:
                    description:
                        - Sum of Computed Line Amount unrounded
                    returned: on success
                    type: str
                    sample: cost_unrounded_example
                cost:
                    description:
                        - Sum of Computed Line Amount rounded
                    returned: on success
                    type: str
                    sample: cost_example
                type:
                    description:
                        - Usage compute type in SPM.
                    returned: on success
                    type: str
                    sample: PROMOTION
    sample: [{
        "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx",
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
        "time_start": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "plan_number": "plan_number_example",
        "currency_code": "currency_code_example",
        "rate_card_id": "ocid1.ratecard.oc1..xxxxxxEXAMPLExxxxxx",
        "pricing_model": "PAY_AS_YOU_GO",
        "aggregated_computed_usages": [{
            "quantity": "quantity_example",
            "product": {
                "part_number": "part_number_example",
                "name": "name_example",
                "unit_of_measure": "unit_of_measure_example",
                "provisioning_group": "provisioning_group_example",
                "billing_category": "billing_category_example",
                "product_category": "product_category_example",
                "ucm_rate_card_part_type": "ucm_rate_card_part_type_example"
            },
            "data_center": "data_center_example",
            "time_metered_on": "2013-10-20T19:20:30+01:00",
            "net_unit_price": "net_unit_price_example",
            "cost_unrounded": "cost_unrounded_example",
            "cost": "cost_example",
            "type": "PROMOTION"
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
    from oci.osub_usage import ComputedUsageClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ComputedUsageAggregatedFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "subscription_id",
            "time_from",
            "time_to",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "parent_product",
            "grouping",
            "x_one_origin_region",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_computed_usage_aggregateds,
            compartment_id=self.module.params.get("compartment_id"),
            subscription_id=self.module.params.get("subscription_id"),
            time_from=self.module.params.get("time_from"),
            time_to=self.module.params.get("time_to"),
            **optional_kwargs
        )


ComputedUsageAggregatedFactsHelperCustom = get_custom_class(
    "ComputedUsageAggregatedFactsHelperCustom"
)


class ResourceFactsHelper(
    ComputedUsageAggregatedFactsHelperCustom, ComputedUsageAggregatedFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            subscription_id=dict(type="str", required=True),
            time_from=dict(type="str", required=True),
            time_to=dict(type="str", required=True),
            parent_product=dict(type="str"),
            grouping=dict(type="str", choices=["HOURLY", "DAILY", "MONTHLY", "NONE"]),
            x_one_origin_region=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="computed_usage_aggregated",
        service_client_class=ComputedUsageClient,
        namespace="osub_usage",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(computed_usage_aggregateds=result)


if __name__ == "__main__":
    main()
