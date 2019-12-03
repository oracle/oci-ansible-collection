#!/usr/bin/python
# Copyright (c) 2019, Oracle and/or its affiliates.
# This software is made available to you under the terms of the GPL 3.0 license or the Apache 2.0 license.
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# Apache License v2.0
# See LICENSE.TXT for details.

from __future__ import absolute_import, division, print_function

__metaclass__ = type

ANSIBLE_METADATA = {
    "metadata_version": "1.1",
    "status": ["preview"],
    "supported_by": "community",
}

DOCUMENTATION = """
---
module: oci_app_catalog_subscription_facts
short_description: Retrieve details about App Catalog subscriptions in OCI Compute Service
description:
    - This module retrieves information of app catalog subscriptions in the specified compartment.
version_added: "2.5"
options:
    compartment_id:
        description: The OCID of the compartment.
        required: true
    listing_id:
        description: The OCID of the listing.
        required: false
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the app catalog subscriptions in the specified compartment
  oci_app_catalog_subscription_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
- name: Get the app catalog subscriptions for a specific listing in a compartment
  oci_app_catalog_subscription_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    listing_id: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
- name: Get the app catalog subscriptions having the given display name in a compartment
  oci_app_catalog_subscription_facts:
    compartment_id: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
    display_name: Test app catalog listing
"""

RETURN = """
app_catalog_subscriptions:
    description: List of app catalog subscriptions
    returned: always
    type: complex
    contains:
        compartment_id:
            description: The compartmentID of the subscription.
            returned: always
            type: string
            sample: ocid1.compartment.oc1..xxxxxEXAMPLExxxxx
        display_name:
            description: The display name of the listing.
            returned: always
            type: string
            sample: Test app catalog
        listing_id:
            description: The ocid of the listing resource.
            returned: always
            type: string
            sample: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
        listing_resource_id:
            description: Listing resource id.
            returned: always
            type: string
            sample: ocid1.image.oc1..xxxxxEXAMPLExxxxx
        listing_resource_version:
            description: Listing resource version.
            returned: always
            type: string
            sample: "1.0.0"
        publisher_name:
            description: Name of the publisher who published this listing.
            returned: always
            type: string
            sample: Test Publisher
        summary:
            description: Summary of the listing.
            returned: always
            type: string
            sample: Test app catalog listing
        time_created:
            description: Date and time at which the subscription was created, in RFC3339 format.
            returned: always
            type: string
            sample: 2019-02-14T19:53:30.878000+00:00
    sample: [{
            "compartment_id": "ocid1.compartment.oc1..xxxxxEXAMPLExxxxx",
            "display_name": "Test app catalog",
            "listing_id": "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
            "listing_resource_id": "ocid1.image.oc1..xxxxxEXAMPLExxxxx",
            "listing_resource_version": "1.0.0",
            "publisher_name": "Test Publisher",
            "summary": "Test app catalog listing",
            "time_created": "2019-02-14T19:53:30.878000+00:00"
            }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible.module_utils.oracle import oci_utils

try:
    from oci.core.compute_client import ComputeClient
    from oci.util import to_dict
    from oci.exceptions import ServiceError

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


def list_app_catalog_subscriptions(compute_client, module):
    compartment_id = module.params["compartment_id"]
    optional_list_method_params = ["listing_id", "display_name"]
    optional_kwargs = dict(
        (param, module.params[param])
        for param in optional_list_method_params
        if module.params.get(param) is not None
    )
    return to_dict(
        oci_utils.list_all_resources(
            compute_client.list_app_catalog_subscriptions,
            compartment_id=compartment_id,
            **optional_kwargs
        )
    )


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            listing_id=dict(type="str", required=False),
        )
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    try:
        result = list_app_catalog_subscriptions(compute_client, module)
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(app_catalog_subscriptions=result)


if __name__ == "__main__":
    main()
