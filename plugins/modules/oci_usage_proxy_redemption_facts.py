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
module: oci_usage_proxy_redemption_facts
short_description: Fetches details about one or multiple Redemption resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Redemption resources in Oracle Cloud Infrastructure
    - Returns the list of redemption for the subscription ID.
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
    time_redeemed_greater_than_or_equal_to:
        description:
            - The starting redeemed date filter for the redemption history.
        type: str
    time_redeemed_less_than:
        description:
            - The ending redeemed date filter for the redemption history.
        type: str
    sort_order:
        description:
            - The sort order to use, which can be ascending (ASC) or descending (DESC).
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to be used only for list redemptions API. Supports one sort order.
        type: str
        choices:
            - "TIMEREDEEMED"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List redemptions
  oci_usage_proxy_redemption_facts:
    # required
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    time_redeemed_greater_than_or_equal_to: 2013-10-20T19:20:30+01:00
    time_redeemed_less_than: 2013-10-20T19:20:30+01:00
    sort_order: ASC
    sort_by: TIMEREDEEMED

"""

RETURN = """
redemptions:
    description:
        - List of Redemption resources
    returned: on success
    type: complex
    contains:
        time_redeemed:
            description:
                - It provides redeem date.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        redemption_email:
            description:
                - It provides the redemption email id.
            returned: on success
            type: str
            sample: redemption_email_example
        redemption_code:
            description:
                - The redemption code used in the Billing Center during the reward redemption process.
            returned: on success
            type: str
            sample: redemption_code_example
        invoice_number:
            description:
                - It provides the invoice number against the redemption.
            returned: on success
            type: str
            sample: invoice_number_example
        invoice_total_amount:
            description:
                - It provides the invoice total amount of given redemption.
            returned: on success
            type: float
            sample: 1.2
        invoice_currency:
            description:
                - The currency associated with invoice.
            returned: on success
            type: str
            sample: invoice_currency_example
        redeemed_rewards:
            description:
                - It provides the redeemed rewards in invoice currency.
            returned: on success
            type: float
            sample: 3.4
        base_rewards:
            description:
                - It provides the redeemed rewards in base/subscription currency.
            returned: on success
            type: float
            sample: 3.4
        fx_rate:
            description:
                - It provides the fxRate between invoice currency and subscription currency.
            returned: on success
            type: float
            sample: 1.2
        time_invoiced:
            description:
                - It provides the invoice date.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "time_redeemed": "2013-10-20T19:20:30+01:00",
        "redemption_email": "redemption_email_example",
        "redemption_code": "redemption_code_example",
        "invoice_number": "invoice_number_example",
        "invoice_total_amount": 1.2,
        "invoice_currency": "invoice_currency_example",
        "redeemed_rewards": 3.4,
        "base_rewards": 3.4,
        "fx_rate": 1.2,
        "time_invoiced": "2013-10-20T19:20:30+01:00"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.usage import RewardsClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class RedemptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "tenancy_id",
            "subscription_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "time_redeemed_greater_than_or_equal_to",
            "time_redeemed_less_than",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_redemptions,
            tenancy_id=self.module.params.get("tenancy_id"),
            subscription_id=self.module.params.get("subscription_id"),
            **optional_kwargs
        )


RedemptionFactsHelperCustom = get_custom_class("RedemptionFactsHelperCustom")


class ResourceFactsHelper(RedemptionFactsHelperCustom, RedemptionFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tenancy_id=dict(type="str", required=True),
            subscription_id=dict(type="str", required=True),
            time_redeemed_greater_than_or_equal_to=dict(type="str"),
            time_redeemed_less_than=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMEREDEEMED"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="redemption",
        service_client_class=RewardsClient,
        namespace="usage",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(redemptions=result)


if __name__ == "__main__":
    main()
