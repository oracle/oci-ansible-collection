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
module: oci_onesubscription_invoiceline_computed_usage_facts
short_description: Fetches details about one or multiple InvoicelineComputedUsage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InvoicelineComputedUsage resources in Oracle Cloud Infrastructure
    - This is a collection API which returns a list of Invoiced Computed Usages for given Invoiceline id.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the root compartment.
        type: str
        required: true
    invoice_line_id:
        description:
            - "Invoice Line Identifier - Primary Key SPM"
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending ('ASC') or descending ('DESC').
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by Invoiced Computed Usages. You can provide one sort order (`sortOrder`).
        type: str
        choices:
            - "timeCreated"
            - "meteredOnDate"
    fields:
        description:
            - Partial response refers to an optimization technique offered
              by the RESTful web APIs to return only the information
              (fields) required by the client. This parameter is used to control what fields to
              return.
        type: list
        elements: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List invoiceline_computed_usages
  oci_onesubscription_invoiceline_computed_usage_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    invoice_line_id: "ocid1.invoiceline.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: timeCreated
    fields: [ "fields_example" ]

"""

RETURN = """
invoiceline_computed_usages:
    description:
        - List of InvoicelineComputedUsage resources
    returned: on success
    type: complex
    contains:
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
        quantity:
            description:
                - Total Quantity that was used for computation
            returned: on success
            type: float
            sample: 1.2
        net_unit_price:
            description:
                - Net Unit Price for the product in consideration, price actual.
            returned: on success
            type: float
            sample: 1.2
        time_metered_on:
            description:
                - Metered Service date.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        type:
            description:
                - Usage compute type in SPM.
            returned: on success
            type: str
            sample: PROMOTION
        cost:
            description:
                - Sum of Usage/Service Billing Line net Amount
            returned: on success
            type: float
            sample: 1.2
        cost_rounded:
            description:
                - Computed Line Amount rounded.
            returned: on success
            type: float
            sample: 1.2
    sample: [{
        "parent_product": {
            "part_number": "part_number_example",
            "name": "name_example",
            "unit_of_measure": "unit_of_measure_example",
            "billing_category": "billing_category_example",
            "product_category": "product_category_example",
            "ucm_rate_card_part_type": "ucm_rate_card_part_type_example"
        },
        "product": {
            "part_number": "part_number_example",
            "name": "name_example",
            "unit_of_measure": "unit_of_measure_example",
            "billing_category": "billing_category_example",
            "product_category": "product_category_example",
            "ucm_rate_card_part_type": "ucm_rate_card_part_type_example"
        },
        "quantity": 1.2,
        "net_unit_price": 1.2,
        "time_metered_on": "2013-10-20T19:20:30+01:00",
        "type": "PROMOTION",
        "cost": 1.2,
        "cost_rounded": 1.2
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.onesubscription import InvoiceSummaryClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InvoicelineComputedUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "invoice_line_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "fields",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_invoiceline_computed_usages,
            compartment_id=self.module.params.get("compartment_id"),
            invoice_line_id=self.module.params.get("invoice_line_id"),
            **optional_kwargs
        )


InvoicelineComputedUsageFactsHelperCustom = get_custom_class(
    "InvoicelineComputedUsageFactsHelperCustom"
)


class ResourceFactsHelper(
    InvoicelineComputedUsageFactsHelperCustom, InvoicelineComputedUsageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            invoice_line_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "meteredOnDate"]),
            fields=dict(type="list", elements="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="invoiceline_computed_usage",
        service_client_class=InvoiceSummaryClient,
        namespace="onesubscription",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(invoiceline_computed_usages=result)


if __name__ == "__main__":
    main()
