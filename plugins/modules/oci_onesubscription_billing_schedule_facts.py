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
module: oci_onesubscription_billing_schedule_facts
short_description: Fetches details about one or multiple BillingSchedule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple BillingSchedule resources in Oracle Cloud Infrastructure
    - This list API returns all billing schedules for given subscription id and
      for a particular Subscribed Service if provided
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
            - This param is used to get only the billing schedules for a particular Subscription Id
        type: str
        required: true
    subscribed_service_id:
        description:
            - This param is used to get only the billing schedules for a particular Subscribed Service
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
- name: List billing_schedules
  oci_onesubscription_billing_schedule_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    subscription_id: "ocid1.subscription.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    subscribed_service_id: "ocid1.subscribedservice.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: ORDERNUMBER

"""

RETURN = """
billing_schedules:
    description:
        - List of BillingSchedule resources
    returned: on success
    type: complex
    contains:
        subscribed_service_id:
            description:
                - SPM internal Subscribed Service ID
            returned: on success
            type: str
            sample: "ocid1.subscribedservice.oc1..xxxxxxEXAMPLExxxxxx"
        time_start:
            description:
                - Billing schedule start date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - Billing schedule end date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_invoicing:
            description:
                - Billing schedule invoicing date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        invoice_status:
            description:
                - Billing schedule invoice status
            returned: on success
            type: str
            sample: INVOICED
        quantity:
            description:
                - Billing schedule quantity
            returned: on success
            type: str
            sample: quantity_example
        net_unit_price:
            description:
                - Billing schedule net unit price
            returned: on success
            type: str
            sample: net_unit_price_example
        amount:
            description:
                - Billing schedule line net amount
            returned: on success
            type: str
            sample: amount_example
        billing_frequency:
            description:
                - Billing frequency
            returned: on success
            type: str
            sample: billing_frequency_example
        ar_invoice_number:
            description:
                - Indicates the associated AR Invoice Number
            returned: on success
            type: str
            sample: ar_invoice_number_example
        ar_customer_transaction_id:
            description:
                - Indicates the associated AR Customer transaction id a unique identifier existing on AR.
            returned: on success
            type: str
            sample: "ocid1.arcustomertransaction.oc1..xxxxxxEXAMPLExxxxxx"
        order_number:
            description:
                - Order number associated with the Subscribed Service
            returned: on success
            type: str
            sample: order_number_example
        product:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                part_number:
                    description:
                        - Indicates the associated AR Invoice Number
                    returned: on success
                    type: str
                    sample: part_number_example
                name:
                    description:
                        - Product name
                    returned: on success
                    type: str
                    sample: name_example
    sample: [{
        "subscribed_service_id": "ocid1.subscribedservice.oc1..xxxxxxEXAMPLExxxxxx",
        "time_start": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "time_invoicing": "2013-10-20T19:20:30+01:00",
        "invoice_status": "INVOICED",
        "quantity": "quantity_example",
        "net_unit_price": "net_unit_price_example",
        "amount": "amount_example",
        "billing_frequency": "billing_frequency_example",
        "ar_invoice_number": "ar_invoice_number_example",
        "ar_customer_transaction_id": "ocid1.arcustomertransaction.oc1..xxxxxxEXAMPLExxxxxx",
        "order_number": "order_number_example",
        "product": {
            "part_number": "part_number_example",
            "name": "name_example"
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.onesubscription import BillingScheduleClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class BillingScheduleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "subscription_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "subscribed_service_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_billing_schedules,
            compartment_id=self.module.params.get("compartment_id"),
            subscription_id=self.module.params.get("subscription_id"),
            **optional_kwargs
        )


BillingScheduleFactsHelperCustom = get_custom_class("BillingScheduleFactsHelperCustom")


class ResourceFactsHelper(
    BillingScheduleFactsHelperCustom, BillingScheduleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            subscription_id=dict(type="str", required=True),
            subscribed_service_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["ORDERNUMBER", "TIMEINVOICING"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="billing_schedule",
        service_client_class=BillingScheduleClient,
        namespace="onesubscription",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(billing_schedules=result)


if __name__ == "__main__":
    main()
