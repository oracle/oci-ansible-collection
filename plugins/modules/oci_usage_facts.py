#!/usr/bin/python
# Copyright (c) 2017, 2021 Oracle and/or its affiliates.
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
module: oci_usage_facts
short_description: Fetches details about one or multiple Usage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Usage resources in Oracle Cloud Infrastructure
    - Returns usage for the given account.
version_added: "2.9"
author: Oracle (@oracle)
options:
    tenant_id:
        description:
            - Tenant ID
        type: str
        required: true
    time_usage_started:
        description:
            - The usage start time.
        type: str
        required: true
    time_usage_ended:
        description:
            - The usage end time.
        type: str
        required: true
    granularity:
        description:
            - "The usage granularity.
              HOURLY - Hourly data aggregation.
              DAILY - Daily data aggregation.
              MONTHLY - Monthly data aggregation.
              TOTAL - Not yet supported."
        type: str
        choices:
            - "HOURLY"
            - "DAILY"
            - "MONTHLY"
            - "TOTAL"
        required: true
    query_type:
        description:
            - "The query usage type.
              Usage - Query the usage data.
              Cost - Query the cost/billing data."
        type: str
        choices:
            - "USAGE"
            - "COST"
    group_by:
        description:
            - "Aggregate the result by.
              example:
                `[\\"service\\"]`"
        type: list
    compartment_depth:
        description:
            - The compartment depth level.
        type: float
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List usages
  oci_usage_facts:
    tenant_id: ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx
    time_usage_started: 2013-10-20T19:20:30+01:00
    time_usage_ended: 2013-10-20T19:20:30+01:00
    granularity: HOURLY

"""

RETURN = """
usages:
    description:
        - List of Usage resources
    returned: on success
    type: complex
    contains:
        tenant_id:
            description:
                - The tenancy OCID.
            returned: on success
            type: string
            sample: ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx
        tenant_name:
            description:
                - The tenancy name.
            returned: on success
            type: string
            sample: tenant_name_example
        compartment_id:
            description:
                - The compartment OCID.
            returned: on success
            type: string
            sample: ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx
        compartment_path:
            description:
                - The compartment path, starting from root.
            returned: on success
            type: string
            sample: compartment_path_example
        compartment_name:
            description:
                - The compartment name.
            returned: on success
            type: string
            sample: compartment_name_example
        service:
            description:
                - The service name that is incurring the cost.
            returned: on success
            type: string
            sample: service_example
        resource_name:
            description:
                - The resource name that is incurring the cost.
            returned: on success
            type: string
            sample: resource_name_example
        resource_id:
            description:
                - The resource OCID that is incurring the cost.
            returned: on success
            type: string
            sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
        region:
            description:
                - The region of the usage.
            returned: on success
            type: string
            sample: region_example
        ad:
            description:
                - The availability domain of the usage.
            returned: on success
            type: string
            sample: ad_example
        weight:
            description:
                - The resource size being metered.
            returned: on success
            type: float
            sample: 10
        shape:
            description:
                - The resource shape.
            returned: on success
            type: string
            sample: shape_example
        sku_part_number:
            description:
                - The SKU part number.
            returned: on success
            type: string
            sample: sku_part_number_example
        sku_name:
            description:
                - The SKU friendly name.
            returned: on success
            type: string
            sample: sku_name_example
        unit:
            description:
                - The usage unit.
            returned: on success
            type: string
            sample: unit_example
        discount:
            description:
                - The discretionary discount applied to the SKU.
            returned: on success
            type: float
            sample: 10
        list_rate:
            description:
                - The SKU list rate (not discount).
            returned: on success
            type: float
            sample: 10
        platform:
            description:
                - Platform for the cost.
            returned: on success
            type: string
            sample: platform_example
        time_usage_started:
            description:
                - The usage start time.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        time_usage_ended:
            description:
                - The usage end time.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
        computed_amount:
            description:
                - The computed cost.
            returned: on success
            type: float
            sample: 10
        computed_quantity:
            description:
                - The usage number.
            returned: on success
            type: float
            sample: 10
        overages_flag:
            description:
                - The SPM OverageFlag.
            returned: on success
            type: string
            sample: overages_flag_example
        unit_price:
            description:
                - The price per unit.
            returned: on success
            type: float
            sample: 10
        currency:
            description:
                - The price currency.
            returned: on success
            type: string
            sample: currency_example
        subscription_id:
            description:
                - The subscription ID.
            returned: on success
            type: string
            sample: ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx
        overage:
            description:
                - The overage usage.
            returned: on success
            type: string
            sample: overage_example
        tags:
            description:
                - For grouping, a tag definition. For filtering, a definition and key.
            returned: on success
            type: complex
            contains:
                namespace:
                    description:
                        - The tag namespace.
                    returned: on success
                    type: string
                    sample: namespace_example
                key:
                    description:
                        - The tag key.
                    returned: on success
                    type: string
                    sample: key_example
                value:
                    description:
                        - The tag value.
                    returned: on success
                    type: string
                    sample: value_example
    sample: [{
        "tenant_id": "ocid1.tenant.oc1..xxxxxxEXAMPLExxxxxx",
        "tenant_name": "tenant_name_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_path": "compartment_path_example",
        "compartment_name": "compartment_name_example",
        "service": "service_example",
        "resource_name": "resource_name_example",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "region": "region_example",
        "ad": "ad_example",
        "weight": 10,
        "shape": "shape_example",
        "sku_part_number": "sku_part_number_example",
        "sku_name": "sku_name_example",
        "unit": "unit_example",
        "discount": 10,
        "list_rate": 10,
        "platform": "platform_example",
        "time_usage_started": "2013-10-20T19:20:30+01:00",
        "time_usage_ended": "2013-10-20T19:20:30+01:00",
        "computed_amount": 10,
        "computed_quantity": 10,
        "overages_flag": "overages_flag_example",
        "unit_price": 10,
        "currency": "currency_example",
        "subscription_id": "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx",
        "overage": "overage_example",
        "tags": [{
            "namespace": "namespace_example",
            "key": "key_example",
            "value": "value_example"
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
    from oci.usage_api import UsageapiClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class UsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "request_summarized_usages_details",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.request_summarized_usages,
            request_summarized_usages_details=self.module.params.get(
                "request_summarized_usages_details"
            ),
            **optional_kwargs
        )


UsageFactsHelperCustom = get_custom_class("UsageFactsHelperCustom")


class ResourceFactsHelper(UsageFactsHelperCustom, UsageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            tenant_id=dict(type="str", required=True),
            time_usage_started=dict(type="str", required=True),
            time_usage_ended=dict(type="str", required=True),
            granularity=dict(
                type="str",
                required=True,
                choices=["HOURLY", "DAILY", "MONTHLY", "TOTAL"],
            ),
            query_type=dict(type="str", choices=["USAGE", "COST"]),
            group_by=dict(type="list"),
            compartment_depth=dict(type="float"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="usage",
        service_client_class=UsageapiClient,
        namespace="usage_api",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(usages=result)


if __name__ == "__main__":
    main()
