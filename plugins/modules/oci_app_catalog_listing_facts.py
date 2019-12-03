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
module: oci_app_catalog_listing_facts
short_description: Retrieve details about published App Catalog listings in OCI Compute Service
description:
    - This module retrieves information of a specified app catalog listing or lists all the app catalog listings
      in the tenancy.
version_added: "2.5"
options:
    listing_id:
        description: The OCID of the listing. Required to get information of a specific app catalog listing.
        required: false
        aliases: ["id"]
    publisher_name:
        description: A filter to return only the publisher that matches the given publisher name exactly.
        required: false
    publisher_type:
        description: A filter to return only publishers that match the given publisher type exactly.
        required: false
        choices: ["OCI", "ORACLE", "TRUSTED", "STANDARD"]
author: "Manoj Meda (@manojmeda)"
extends_documentation_fragment: [ oracle, oracle_display_name_option ]
"""

EXAMPLES = """
- name: Get all the published app catalog listings in the tenancy
  oci_app_catalog_listing_facts:

- name: Get a specific app catalog listing using its OCID
  oci_app_catalog_listing_facts:
    listing_id: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx

- name: Get app catalog listing having the specified display name
  oci_app_catalog_listing_facts:
    display_name: Test app catalog listing

- name: Get all app catalog listings from a specific publisher
  oci_app_catalog_listing_facts:
    publisher_name: Test Publisher
"""

RETURN = """
app_catalog_listings:
    description: List of app catalog listing details
    returned: always
    type: complex
    contains:
        contact_url:
            description: Listing's contact URL.
            returned: always
            type: string
            sample: "https://testpublisher/contact.html"
        description:
            description: Description of the listing.
            returned: always
            type: string
            sample: Test app catalog listing
        display_name:
            description: Name of the listing.
            returned: always
            type: string
            sample: Test app catalog listing
        listing_id:
            description: The OCID of the listing.
            returned: always
            type: string
            sample: ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx
        publisher_logo_url:
            description: Publisher's logo URL.
            returned: always
            type: string
            sample: "https://testpublisher/logo.png"
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
        time_published:
            description: Date and time the listing was published, in RFC3339 format.
            returned: always
            type: string
            sample: 2019-02-14T19:53:30.878000+00:00
    sample: [{
            "contact_url": "https://testpublisher/contact.html",
            "description": "Test app catalog listing.",
            "display_name": "Test app catalog listing",
            "listing_id": "ocid1.appcataloglisting.oc1..xxxxxEXAMPLExxxxx",
            "publisher_logo_url": "https://testpublisher/logo.png",
            "publisher_name": "Test Publisher",
            "summary": "Test app catalog listing",
            "time_published": "2019-02-14T19:53:30.878000+00:00"
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


def list_app_catalog_listings(compute_client, module):
    optional_list_method_params = ["display_name", "publisher_name", "publisher_type"]
    optional_kwargs = dict(
        (param, module.params[param])
        for param in optional_list_method_params
        if module.params.get(param) is not None
    )
    return to_dict(
        [
            oci_utils.call_with_backoff(
                compute_client.get_app_catalog_listing,
                listing_id=app_catalog_listing.listing_id,
            ).data
            for app_catalog_listing in oci_utils.list_all_resources(
                compute_client.list_app_catalog_listings, **optional_kwargs
            )
        ]
    )


def get_app_catalog_listing(compute_client, module):
    listing_id = module.params["listing_id"]
    return to_dict(
        [
            oci_utils.call_with_backoff(
                compute_client.get_app_catalog_listing, listing_id=listing_id
            ).data
        ]
    )


def main():
    module_args = oci_utils.get_facts_module_arg_spec()
    module_args.update(
        dict(
            listing_id=dict(type="str", required=False, aliases=["id"]),
            publisher_name=dict(type="str", required=False),
            publisher_type=dict(
                type="str",
                required=False,
                choices=["OCI", "ORACLE", "TRUSTED", "STANDARD"],
            ),
        )
    )
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=False)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    compute_client = oci_utils.create_service_client(module, ComputeClient)

    try:
        listing_id = module.params["listing_id"]
        if listing_id:
            result = get_app_catalog_listing(compute_client, module)
        else:
            result = list_app_catalog_listings(compute_client, module)
    except ServiceError as se:
        module.fail_json(msg=se.message)

    module.exit_json(app_catalog_listings=result)


if __name__ == "__main__":
    main()
