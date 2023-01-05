#!/usr/bin/python
# Copyright (c) 2020, 2023 Oracle and/or its affiliates.
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
module: oci_license_manager_license_metric_facts
short_description: Fetches details about a LicenseMetric resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a LicenseMetric resource in Oracle Cloud Infrastructure
    - Retrieves the license metrics for a given compartment.
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific license_metric
  oci_license_manager_license_metric_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_compartment_id_in_subtree: true

"""

RETURN = """
license_metric:
    description:
        - LicenseMetric resource
    returned: on success
    type: complex
    contains:
        total_product_license_count:
            description:
                - Total number of product licenses in a particular compartment.
            returned: on success
            type: int
            sample: 56
        total_byol_instance_count:
            description:
                - Total number of BYOL instances in a particular compartment.
            returned: on success
            type: int
            sample: 56
        total_license_included_instance_count:
            description:
                - Total number of License Included (LI) instances in a particular compartment.
            returned: on success
            type: int
            sample: 56
        license_record_expiring_soon_count:
            description:
                - Total number of license records that will expire within 90 days in a particular compartment.
            returned: on success
            type: int
            sample: 56
    sample: {
        "total_product_license_count": 56,
        "total_byol_instance_count": 56,
        "total_license_included_instance_count": 56,
        "license_record_expiring_soon_count": 56
    }
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


class LicenseMetricFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        optional_get_method_params = [
            "is_compartment_id_in_subtree",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_license_metric,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


LicenseMetricFactsHelperCustom = get_custom_class("LicenseMetricFactsHelperCustom")


class ResourceFactsHelper(LicenseMetricFactsHelperCustom, LicenseMetricFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            is_compartment_id_in_subtree=dict(type="bool"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="license_metric",
        service_client_class=LicenseManagerClient,
        namespace="license_manager",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(license_metric=result)


if __name__ == "__main__":
    main()
