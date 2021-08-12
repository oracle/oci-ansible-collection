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
module: oci_marketplace_third_party_paid_listing_eligibility_facts
short_description: Fetches details about a ThirdPartyPaidListingEligibility resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a ThirdPartyPaidListingEligibility resource in Oracle Cloud Infrastructure
    - Returns eligibility details of the tenancy to see and launch third party paid listings
version_added: "2.9"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier for the compartment.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific third_party_paid_listing_eligibility
  oci_marketplace_third_party_paid_listing_eligibility_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
third_party_paid_listing_eligibility:
    description:
        - ThirdPartyPaidListingEligibility resource
    returned: on success
    type: complex
    contains:
        is_paid_listing_eligible:
            description:
                - Whether the tenant is permitted to use paid listings
            returned: on success
            type: bool
            sample: true
        is_paid_listing_throttled:
            description:
                - Whether the tenant is currently prevented from using paid listings because of throttling
            returned: on success
            type: bool
            sample: true
        eligibility_reason:
            description:
                - Reason the account is ineligible to launch paid listings
            returned: on success
            type: string
            sample: ELIGIBLE
    sample: {
        "is_paid_listing_eligible": true,
        "is_paid_listing_throttled": true,
        "eligibility_reason": "ELIGIBLE"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.marketplace import AccountClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ThirdPartyPaidListingEligibilityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_third_party_paid_listing_eligibility,
            compartment_id=self.module.params.get("compartment_id"),
        )


ThirdPartyPaidListingEligibilityFactsHelperCustom = get_custom_class(
    "ThirdPartyPaidListingEligibilityFactsHelperCustom"
)


class ResourceFactsHelper(
    ThirdPartyPaidListingEligibilityFactsHelperCustom,
    ThirdPartyPaidListingEligibilityFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="third_party_paid_listing_eligibility",
        service_client_class=AccountClient,
        namespace="marketplace",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(third_party_paid_listing_eligibility=result)


if __name__ == "__main__":
    main()
