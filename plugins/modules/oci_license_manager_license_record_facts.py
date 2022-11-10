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
module: oci_license_manager_license_record_facts
short_description: Fetches details about one or multiple LicenseRecord resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple LicenseRecord resources in Oracle Cloud Infrastructure
    - Retrieves all license records for a given product license ID.
    - If I(license_record_id) is specified, the details of a single LicenseRecord will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    license_record_id:
        description:
            - Unique license record identifier.
            - Required to get a specific license_record.
        type: str
        aliases: ["id"]
    product_license_id:
        description:
            - Unique product license identifier.
            - Required to list multiple license_records.
        type: str
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
            - "Default: `expirationDate`"
            - "* **expirationDate:** Sorts by expiration date of the license record."
        type: str
        choices:
            - "expirationDate"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get a specific license_record
  oci_license_manager_license_record_facts:
    # required
    license_record_id: "ocid1.licenserecord.oc1..xxxxxxEXAMPLExxxxxx"

- name: List license_records
  oci_license_manager_license_record_facts:
    # required
    product_license_id: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: expirationDate

"""

RETURN = """
license_records:
    description:
        - List of LicenseRecord resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The license record L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        product_license_id:
            description:
                - The product license L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) with which the license record is
                  associated.
            returned: on success
            type: str
            sample: "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) where the license record is created.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The license record display name. Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        product_id:
            description:
                - The license record product ID.
            returned: on success
            type: str
            sample: "ocid1.product.oc1..xxxxxxEXAMPLExxxxxx"
        license_count:
            description:
                - The number of license units added by the user for the given license record.
                  Default 1
            returned: on success
            type: int
            sample: 56
        expiration_date:
            description:
                - "The license record end date in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  date format.
                  Example: `2018-09-12`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        support_end_date:
            description:
                - "The license record support end date in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  date format.
                  Example: `2018-09-12`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        is_unlimited:
            description:
                - Specifies if the license count is unlimited.
            returned: on success
            type: bool
            sample: true
        is_perpetual:
            description:
                - Specifies if the license record term is perpertual.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - The time the license record was created. An L(RFC 3339,https://tools.ietf.org/html/rfc3339)-formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time the license record was updated. An L(RFC 3339,https://tools.ietf.org/html/rfc3339)-formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current license record state.
            returned: on success
            type: str
            sample: ACTIVE
        license_unit:
            description:
                - The product license unit.
            returned: on success
            type: str
            sample: OCPU
        product_license:
            description:
                - The product license name with which the license record is associated.
            returned: on success
            type: str
            sample: product_license_example
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
        "product_license_id": "ocid1.productlicense.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "product_id": "ocid1.product.oc1..xxxxxxEXAMPLExxxxxx",
        "license_count": 56,
        "expiration_date": "2013-10-20T19:20:30+01:00",
        "support_end_date": "2013-10-20T19:20:30+01:00",
        "is_unlimited": true,
        "is_perpetual": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "license_unit": "OCPU",
        "product_license": "product_license_example",
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


class LicenseRecordFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "license_record_id",
        ]

    def get_required_params_for_list(self):
        return [
            "product_license_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_license_record,
            license_record_id=self.module.params.get("license_record_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_license_records,
            product_license_id=self.module.params.get("product_license_id"),
            **optional_kwargs
        )


LicenseRecordFactsHelperCustom = get_custom_class("LicenseRecordFactsHelperCustom")


class ResourceFactsHelper(LicenseRecordFactsHelperCustom, LicenseRecordFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            license_record_id=dict(aliases=["id"], type="str"),
            product_license_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["expirationDate"]),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="license_record",
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

    module.exit_json(license_records=result)


if __name__ == "__main__":
    main()
