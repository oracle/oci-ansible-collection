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
module: oci_license_manager_top_utilized_product_license_facts
short_description: Fetches details about one or multiple TopUtilizedProductLicense resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TopUtilizedProductLicense resources in Oracle Cloud Infrastructure
    - Retrieves the top utilized product licenses for a given compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
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
            - "Default: `totalLicenseUnitsConsumed`"
            - "* **totalLicenseUnitsConsumed:** Sorts by totalLicenseUnitsConsumed of ProductLicense."
        type: str
        choices:
            - "totalLicenseUnitsConsumed"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List top_utilized_product_licenses
  oci_license_manager_top_utilized_product_license_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_compartment_id_in_subtree: true
    sort_order: ASC
    sort_by: totalLicenseUnitsConsumed

"""

RETURN = """
top_utilized_product_licenses:
    description:
        - List of TopUtilizedProductLicense resources
    returned: on success
    type: complex
    contains:
        product_license_id:
            description:
                - The product license L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"
        product_type:
            description:
                - The product type.
            returned: on success
            type: str
            sample: product_type_example
        unit_type:
            description:
                - The product license unit.
            returned: on success
            type: str
            sample: OCPU
        total_units_consumed:
            description:
                - Number of license units consumed.
            returned: on success
            type: float
            sample: 1.2
        total_license_unit_count:
            description:
                - Total number of license units in the product license provided by the user.
            returned: on success
            type: int
            sample: 56
        is_unlimited:
            description:
                - Specifies if the license unit count is unlimited.
            returned: on success
            type: bool
            sample: true
        status:
            description:
                - The current product license status.
            returned: on success
            type: str
            sample: INCOMPLETE
    sample: [{
        "product_license_id": "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx",
        "product_type": "product_type_example",
        "unit_type": "OCPU",
        "total_units_consumed": 1.2,
        "total_license_unit_count": 56,
        "is_unlimited": true,
        "status": "INCOMPLETE"
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


class TopUtilizedProductLicenseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
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
            self.client.list_top_utilized_product_licenses,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TopUtilizedProductLicenseFactsHelperCustom = get_custom_class(
    "TopUtilizedProductLicenseFactsHelperCustom"
)


class ResourceFactsHelper(
    TopUtilizedProductLicenseFactsHelperCustom, TopUtilizedProductLicenseFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            is_compartment_id_in_subtree=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["totalLicenseUnitsConsumed"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="top_utilized_product_license",
        service_client_class=LicenseManagerClient,
        namespace="license_manager",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(top_utilized_product_licenses=result)


if __name__ == "__main__":
    main()
