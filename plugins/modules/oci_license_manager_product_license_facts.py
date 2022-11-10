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
module: oci_license_manager_product_license_facts
short_description: Fetches details about one or multiple ProductLicense resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ProductLicense resources in Oracle Cloud Infrastructure
    - Retrieves all the product licenses from a given compartment.
    - If I(product_license_id) is specified, the details of a single ProductLicense will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    product_license_id:
        description:
            - Unique product license identifier.
            - Required to get a specific product_license.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license,
              and configuration.
            - Required to list multiple product_licenses.
        type: str
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific product_license
  oci_license_manager_product_license_facts:
    # required
    product_license_id: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"

- name: List product_licenses
  oci_license_manager_product_license_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_compartment_id_in_subtree: true
    sort_order: ASC
    sort_by: totalLicenseUnitsConsumed

"""

RETURN = """
product_licenses:
    description:
        - List of ProductLicense resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The product license L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) where the product license is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        status:
            description:
                - The current product license status.
            returned: on success
            type: str
            sample: INCOMPLETE
        status_description:
            description:
                - Status description for the current product license status.
            returned: on success
            type: str
            sample: status_description_example
        lifecycle_state:
            description:
                - The current product license state.
            returned: on success
            type: str
            sample: ACTIVE
        total_active_license_unit_count:
            description:
                - The total number of licenses available for the product license, calculated by adding up all the license counts for active license records
                  associated with the product license.
            returned: on success
            type: int
            sample: 56
        total_license_units_consumed:
            description:
                - The number of license units consumed. Updated after each allocation run.
            returned: on success
            type: float
            sample: 1.2
        total_license_record_count:
            description:
                - The number of license records associated with the product license.
            returned: on success
            type: int
            sample: 56
        active_license_record_count:
            description:
                - The number of active license records associated with the product license.
            returned: on success
            type: int
            sample: 56
        license_unit:
            description:
                - The product license unit.
            returned: on success
            type: str
            sample: OCPU
        is_vendor_oracle:
            description:
                - Specifies whether the vendor is Oracle or a third party.
            returned: on success
            type: bool
            sample: true
        is_over_subscribed:
            description:
                - Specifies whether or not the product license is oversubscribed.
            returned: on success
            type: bool
            sample: true
        is_unlimited:
            description:
                - Specifies if the license unit count is unlimited.
            returned: on success
            type: bool
            sample: true
        display_name:
            description:
                - License record name
            returned: on success
            type: str
            sample: display_name_example
        vendor_name:
            description:
                - The vendor of the ProductLicense
            returned: on success
            type: str
            sample: vendor_name_example
        time_created:
            description:
                - The time the product license was created. An L(RFC 3339,https://tools.ietf.org/html/rfc3339)-formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the product license was updated. An L(RFC 3339,https://tools.ietf.org/html/rfc3339)-formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        images:
            description:
                - The images associated with the product license.
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The image ID associated with the product license.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                listing_name:
                    description:
                        - The listing name associated with the product license.
                    returned: on success
                    type: str
                    sample: listing_name_example
                publisher:
                    description:
                        - The image publisher.
                    returned: on success
                    type: str
                    sample: publisher_example
                listing_id:
                    description:
                        - The image listing ID.
                    returned: on success
                    type: str
                    sample: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
                package_version:
                    description:
                        - The image package version.
                    returned: on success
                    type: str
                    sample: package_version_example
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type, or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "Usage of system tag keys. These predefined keys are scoped to namespaces.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "status": "INCOMPLETE",
        "status_description": "status_description_example",
        "lifecycle_state": "ACTIVE",
        "total_active_license_unit_count": 56,
        "total_license_units_consumed": 1.2,
        "total_license_record_count": 56,
        "active_license_record_count": 56,
        "license_unit": "OCPU",
        "is_vendor_oracle": true,
        "is_over_subscribed": true,
        "is_unlimited": true,
        "display_name": "display_name_example",
        "vendor_name": "vendor_name_example",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "images": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "listing_name": "listing_name_example",
            "publisher": "publisher_example",
            "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
            "package_version": "package_version_example"
        }],
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
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


class ProductLicenseFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "product_license_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_product_license,
            product_license_id=self.module.params.get("product_license_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "is_compartment_id_in_subtree",
            "sort_order",
            "sort_by",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_product_licenses,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ProductLicenseFactsHelperCustom = get_custom_class("ProductLicenseFactsHelperCustom")


class ResourceFactsHelper(
    ProductLicenseFactsHelperCustom, ProductLicenseFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            product_license_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            is_compartment_id_in_subtree=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["totalLicenseUnitsConsumed"]),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="product_license",
        service_client_class=LicenseManagerClient,
        namespace="license_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(product_licenses=result)


if __name__ == "__main__":
    main()
