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
module: oci_license_manager_product_license_consumer_facts
short_description: Fetches details about one or multiple ProductLicenseConsumer resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProductLicenseConsumer resources in Oracle Cloud Infrastructure
    - Retrieves the product license consumers for a particular product license ID.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    product_license_id:
        description:
            - Unique product license identifier.
        type: str
        required: true
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license,
              and configuration.
        type: str
        required: true
    is_compartment_id_in_subtree:
        description:
            - Indicates if the given compartment is the root compartment.
        type: bool
    sort_order:
        description:
            - The sort order to use, whether `ASC` or `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the attribute with which to sort the rules.
            - "Default: `licenseUnitsRequired`"
            - "* **licenseUnitsRequired:** Sorts by licenseUnitsRequired of the Resource."
        type: str
        choices:
            - "licenseUnitsRequired"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List product_license_consumers
  oci_license_manager_product_license_consumer_facts:
    # required
    product_license_id: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_compartment_id_in_subtree: true
    sort_order: ASC
    sort_by: licenseUnitsRequired

"""

RETURN = """
product_license_consumers:
    description:
        - List of ProductLicenseConsumer resources
    returned: on success
    type: complex
    contains:
        resource_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        resource_name:
            description:
                - The display name of the resource.
            returned: on success
            type: str
            sample: resource_name_example
        product_name:
            description:
                - The resource product name.
            returned: on success
            type: str
            sample: product_name_example
        resource_compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the resource.
            returned: on success
            type: str
            sample: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
        resource_compartment_name:
            description:
                - The display name of the compartment that contains the resource.
            returned: on success
            type: str
            sample: resource_compartment_name_example
        resource_unit_type:
            description:
                - The unit type for the resource.
            returned: on success
            type: str
            sample: OCPU
        resource_unit_count:
            description:
                - Number of units of the resource
            returned: on success
            type: float
            sample: 1.2
        license_unit_type:
            description:
                - The product license unit.
            returned: on success
            type: str
            sample: OCPU
        license_units_consumed:
            description:
                - Number of license units consumed by the resource.
            returned: on success
            type: float
            sample: 1.2
        is_base_license_available:
            description:
                - Specifies if the base license is available.
            returned: on success
            type: bool
            sample: true
        are_all_options_available:
            description:
                - Specifies if all options are available.
            returned: on success
            type: bool
            sample: true
        missing_products:
            description:
                - Collection of missing product licenses.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of the product.
                    returned: on success
                    type: str
                    sample: name_example
                count:
                    description:
                        - Units required for the missing product.
                    returned: on success
                    type: float
                    sample: 1.2
                category:
                    description:
                        - Product category base or option.
                    returned: on success
                    type: str
                    sample: BASE
    sample: [{
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_name": "resource_name_example",
        "product_name": "product_name_example",
        "resource_compartment_id": "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_compartment_name": "resource_compartment_name_example",
        "resource_unit_type": "OCPU",
        "resource_unit_count": 1.2,
        "license_unit_type": "OCPU",
        "license_units_consumed": 1.2,
        "is_base_license_available": true,
        "are_all_options_available": true,
        "missing_products": [{
            "name": "name_example",
            "count": 1.2,
            "category": "BASE"
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
    from oci.license_manager import LicenseManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ProductLicenseConsumerFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "product_license_id",
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "is_compartment_id_in_subtree",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_product_license_consumers,
            product_license_id=self.module.params.get("product_license_id"),
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ProductLicenseConsumerFactsHelperCustom = get_custom_class(
    "ProductLicenseConsumerFactsHelperCustom"
)


class ResourceFactsHelper(
    ProductLicenseConsumerFactsHelperCustom, ProductLicenseConsumerFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            product_license_id=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            is_compartment_id_in_subtree=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["licenseUnitsRequired"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="product_license_consumer",
        service_client_class=LicenseManagerClient,
        namespace="license_manager",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(product_license_consumers=result)


if __name__ == "__main__":
    main()
