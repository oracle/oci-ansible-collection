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
module: oci_marketplace_launch_eligibility_facts
short_description: Fetches details about a LaunchEligibility resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a LaunchEligibility resource in Oracle Cloud Infrastructure
    - Returns Tenant eligibility and other information for launching a PIC image
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier for the compartment.
        type: str
        required: true
    image_id:
        description:
            - Image ID
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific launch_eligibility
  oci_marketplace_launch_eligibility_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
launch_eligibility:
    description:
        - LaunchEligibility resource
    returned: on success
    type: complex
    contains:
        image_id:
            description:
                - PIC Image ID
            returned: on success
            type: str
            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        is_launch_allowed:
            description:
                - Is the tenant permitted to launch the PIC image
            returned: on success
            type: bool
            sample: true
        meters:
            description:
                - related meters for the PIC image
            returned: on success
            type: str
            sample: meters_example
        ineligibility_reason:
            description:
                - Reason the account is ineligible to launch paid listings
            returned: on success
            type: str
            sample: INELIGIBLE_ACCOUNT_COUNTRY
    sample: {
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "is_launch_allowed": true,
        "meters": "meters_example",
        "ineligibility_reason": "INELIGIBLE_ACCOUNT_COUNTRY"
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


class LaunchEligibilityFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
            "image_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_launch_eligibility,
            compartment_id=self.module.params.get("compartment_id"),
            image_id=self.module.params.get("image_id"),
        )


LaunchEligibilityFactsHelperCustom = get_custom_class(
    "LaunchEligibilityFactsHelperCustom"
)


class ResourceFactsHelper(
    LaunchEligibilityFactsHelperCustom, LaunchEligibilityFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            image_id=dict(type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="launch_eligibility",
        service_client_class=AccountClient,
        namespace="marketplace",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(launch_eligibility=result)


if __name__ == "__main__":
    main()
