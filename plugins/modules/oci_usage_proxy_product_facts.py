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
module: oci_usage_proxy_product_facts
short_description: Fetches details about one or multiple Product resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Product resources in Oracle Cloud Infrastructure
    - Provides product information that is specific to a reward usage period and its usage details.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    tenancy_id:
        description:
            - The OCID of the tenancy.
        type: str
        required: true
    subscription_id:
        description:
            - The subscription ID for which rewards information is requested for.
        type: str
        required: true
    usage_period_key:
        description:
            - The SPM Identifier for the usage period.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, which can be ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Supports one sort order.
        type: str
        choices:
            - "TIMECREATED"
            - "TIMESTART"
    producttype:
        description:
            - The field to specify the type of product.
        type: str
        choices:
            - "ALL"
            - "ELIGIBLE"
            - "INELIGIBLE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List products
  oci_usage_proxy_product_facts:
    # required
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"
    usage_period_key: usage_period_key_example

    # optional
    sort_order: ASC
    sort_by: TIMECREATED
    producttype: ALL

"""

RETURN = """
products:
    description:
        - List of Product resources
    returned: on success
    type: complex
    contains:
        product_number:
            description:
                - The rate card product number.
            returned: on success
            type: str
            sample: product_number_example
        product_name:
            description:
                - The rate card product name.
            returned: on success
            type: str
            sample: product_name_example
        usage_amount:
            description:
                - The rate card product usage amount.
            returned: on success
            type: float
            sample: 1.2
        earned_rewards:
            description:
                - The earned rewards for the product.
            returned: on success
            type: float
            sample: 3.4
        is_eligible_to_earn_rewards:
            description:
                - The boolean parameter to indicate if the product is eligible to earn rewards.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "product_number": "product_number_example",
        "product_name": "product_name_example",
        "usage_amount": 1.2,
        "earned_rewards": 3.4,
        "is_eligible_to_earn_rewards": true
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.usage import RewardsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProductFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "tenancy_id",
            "subscription_id",
            "usage_period_key",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "producttype",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_products,
            tenancy_id=self.module.params.get("tenancy_id"),
            subscription_id=self.module.params.get("subscription_id"),
            usage_period_key=self.module.params.get("usage_period_key"),
            **optional_kwargs
        )


ProductFactsHelperCustom = get_custom_class("ProductFactsHelperCustom")


class ResourceFactsHelper(ProductFactsHelperCustom, ProductFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tenancy_id=dict(type="str", required=True),
            subscription_id=dict(type="str", required=True),
            usage_period_key=dict(type="str", required=True, no_log=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "TIMESTART"]),
            producttype=dict(type="str", choices=["ALL", "ELIGIBLE", "INELIGIBLE"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="product",
        service_client_class=RewardsClient,
        namespace="usage",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(products=result)


if __name__ == "__main__":
    main()
