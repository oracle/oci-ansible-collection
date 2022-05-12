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
module: oci_usage_proxy_monthly_reward_facts
short_description: Fetches details about one or multiple MonthlyReward resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple MonthlyReward resources in Oracle Cloud Infrastructure
    - Returns the list of rewards for a subscription ID.
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List monthly_rewards
  oci_usage_proxy_monthly_reward_facts:
    # required
    tenancy_id: "ocid1.tenancy.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
monthly_rewards:
    description:
        - List of MonthlyReward resources
    returned: on success
    type: complex
    contains:
        available_rewards:
            description:
                - The number of rewards available for a specific usage period.
            returned: on success
            type: float
            sample: 3.4
        redeemed_rewards:
            description:
                - The number of rewards redeemed for a specific month.
            returned: on success
            type: float
            sample: 3.4
        earned_rewards:
            description:
                - The number of rewards earned for the specific usage period.
            returned: on success
            type: float
            sample: 3.4
        is_manual:
            description:
                - The boolean parameter to indicate whether or not the available rewards are manually posted.
            returned: on success
            type: bool
            sample: true
        time_rewards_expired:
            description:
                - The date and time when rewards expire.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_rewards_earned:
            description:
                - The date and time when rewards accrue.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_usage_started:
            description:
                - The start date and time for the usage period.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_usage_ended:
            description:
                - The end date and time for the usage period.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        usage_amount:
            description:
                - The usage amount for the usage period.
            returned: on success
            type: float
            sample: 1.2
        eligible_usage_amount:
            description:
                - The eligible usage amount for the usage period.
            returned: on success
            type: float
            sample: 1.2
        ineligible_usage_amount:
            description:
                - The ineligible usage amount for the usage period.
            returned: on success
            type: float
            sample: 1.2
        usage_period_key:
            description:
                - The usage period ID.
            returned: on success
            type: str
            sample: usage_period_key_example
    sample: [{
        "available_rewards": 3.4,
        "redeemed_rewards": 3.4,
        "earned_rewards": 3.4,
        "is_manual": true,
        "time_rewards_expired": "2013-10-20T19:20:30+01:00",
        "time_rewards_earned": "2013-10-20T19:20:30+01:00",
        "time_usage_started": "2013-10-20T19:20:30+01:00",
        "time_usage_ended": "2013-10-20T19:20:30+01:00",
        "usage_amount": 1.2,
        "eligible_usage_amount": 1.2,
        "ineligible_usage_amount": 1.2,
        "usage_period_key": "usage_period_key_example"
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


class MonthlyRewardFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "tenancy_id",
            "subscription_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_rewards,
            tenancy_id=self.module.params.get("tenancy_id"),
            subscription_id=self.module.params.get("subscription_id"),
            **optional_kwargs
        )


MonthlyRewardFactsHelperCustom = get_custom_class("MonthlyRewardFactsHelperCustom")


class ResourceFactsHelper(MonthlyRewardFactsHelperCustom, MonthlyRewardFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tenancy_id=dict(type="str", required=True),
            subscription_id=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="monthly_reward",
        service_client_class=RewardsClient,
        namespace="usage",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(monthly_rewards=result)


if __name__ == "__main__":
    main()
