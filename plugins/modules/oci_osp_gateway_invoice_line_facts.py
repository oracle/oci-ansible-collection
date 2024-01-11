#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_osp_gateway_invoice_line_facts
short_description: Fetches details about one or multiple InvoiceLine resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InvoiceLine resources in Oracle Cloud Infrastructure
    - Returns the invoice product list by invoice id
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    osp_home_region:
        description:
            - The home region's public name of the logged in user.
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    internal_invoice_id:
        description:
            - The identifier of the invoice.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List invoice_lines
  oci_osp_gateway_invoice_line_facts:
    # required
    osp_home_region: us-phoenix-1
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    internal_invoice_id: "ocid1.internalinvoice.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
invoice_lines:
    description:
        - List of InvoiceLine resources
    returned: on success
    type: complex
    contains:
        product:
            description:
                - Product of the item
            returned: on success
            type: str
            sample: product_example
        order_no:
            description:
                - Product of the item
            returned: on success
            type: str
            sample: order_no_example
        part_number:
            description:
                - Part number
            returned: on success
            type: str
            sample: part_number_example
        time_start:
            description:
                - Start date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_end:
            description:
                - End date
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        quantity:
            description:
                - Quantity of the ordered product
            returned: on success
            type: float
            sample: 10
        net_unit_price:
            description:
                - Unit price of the ordered product
            returned: on success
            type: float
            sample: 10
        total_price:
            description:
                - Total price of the ordered product (Net unit price x quantity)
            returned: on success
            type: float
            sample: 10
        currency:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                currency_code:
                    description:
                        - Currency code
                    returned: on success
                    type: str
                    sample: currency_code_example
                currency_symbol:
                    description:
                        - Currency symbol
                    returned: on success
                    type: str
                    sample: currency_symbol_example
                name:
                    description:
                        - Name of the currency
                    returned: on success
                    type: str
                    sample: name_example
                usd_conversion:
                    description:
                        - USD conversion rate of the currency
                    returned: on success
                    type: float
                    sample: 10
                round_decimal_point:
                    description:
                        - Round decimal point
                    returned: on success
                    type: float
                    sample: 10
    sample: [{
        "product": "product_example",
        "order_no": "order_no_example",
        "part_number": "part_number_example",
        "time_start": "2013-10-20T19:20:30+01:00",
        "time_end": "2013-10-20T19:20:30+01:00",
        "quantity": 10,
        "net_unit_price": 10,
        "total_price": 10,
        "currency": {
            "currency_code": "currency_code_example",
            "currency_symbol": "currency_symbol_example",
            "name": "name_example",
            "usd_conversion": 10,
            "round_decimal_point": 10
        }
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.osp_gateway import InvoiceServiceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InvoiceLineFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "osp_home_region",
            "compartment_id",
            "internal_invoice_id",
        ]

    def list_resources(self):
        optional_list_method_params = []
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_invoice_lines,
            osp_home_region=self.module.params.get("osp_home_region"),
            compartment_id=self.module.params.get("compartment_id"),
            internal_invoice_id=self.module.params.get("internal_invoice_id"),
            **optional_kwargs
        )


InvoiceLineFactsHelperCustom = get_custom_class("InvoiceLineFactsHelperCustom")


class ResourceFactsHelper(InvoiceLineFactsHelperCustom, InvoiceLineFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            osp_home_region=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            internal_invoice_id=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="invoice_line",
        service_client_class=InvoiceServiceClient,
        namespace="osp_gateway",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(invoice_lines=result)


if __name__ == "__main__":
    main()
