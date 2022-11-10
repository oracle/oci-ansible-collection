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
module: oci_marketplace_tax_facts
short_description: Fetches details about one or multiple Tax resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Tax resources in Oracle Cloud Infrastructure
    - Returns list of all tax implications that current tenant may be liable to once they launch the listing.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    listing_id:
        description:
            - The unique identifier for the listing.
        type: str
        required: true
    compartment_id:
        description:
            - The unique identifier for the compartment.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List taxes
  oci_marketplace_tax_facts:
    # required
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
taxes:
    description:
        - List of Tax resources
    returned: on success
    type: complex
    contains:
        code:
            description:
                - Unique code for the tax.
            returned: on success
            type: str
            sample: "null"

        name:
            description:
                - Name of the tax code.
            returned: on success
            type: str
            sample: name_example
        country:
            description:
                - Country, which imposes the tax.
            returned: on success
            type: str
            sample: country_example
        url:
            description:
                - The URL with more details about this tax.
            returned: on success
            type: str
            sample: url_example
    sample: [{
        "code": null,
        "name": "name_example",
        "country": "country_example",
        "url": "url_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.marketplace import MarketplaceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TaxFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "listing_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_taxes,
            listing_id=self.module.params.get("listing_id"),
            **optional_kwargs
        )


TaxFactsHelperCustom = get_custom_class("TaxFactsHelperCustom")


class ResourceFactsHelper(TaxFactsHelperCustom, TaxFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            listing_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="tax",
        service_client_class=MarketplaceClient,
        namespace="marketplace",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(taxes=result)


if __name__ == "__main__":
    main()
