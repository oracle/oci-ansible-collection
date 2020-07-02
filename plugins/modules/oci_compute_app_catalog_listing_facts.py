#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_compute_app_catalog_listing_facts
short_description: Fetches details about one or multiple AppCatalogListing resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AppCatalogListing resources in Oracle Cloud Infrastructure
    - Lists the published listings.
    - If I(listing_id) is specified, the details of a single AppCatalogListing will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    listing_id:
        description:
            - The OCID of the listing.
            - Required to get a specific app_catalog_listing.
        type: str
        aliases: ["id"]
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    publisher_name:
        description:
            - A filter to return only the publisher that matches the given publisher name exactly.
        type: str
    publisher_type:
        description:
            - A filter to return only publishers that match the given publisher type exactly. Valid types are OCI, ORACLE, TRUSTED, STANDARD.
        type: str
    display_name:
        description:
            - A filter to return only resources that match the given display name exactly.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List app_catalog_listings
  oci_compute_app_catalog_listing_facts:

- name: Get a specific app_catalog_listing
  oci_compute_app_catalog_listing_facts:
    listing_id: ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
app_catalog_listings:
    description:
        - List of AppCatalogListing resources
    returned: on success
    type: complex
    contains:
        contact_url:
            description:
                - Listing's contact URL.
            returned: on success
            type: string
            sample: contact_url_example
        description:
            description:
                - Description of the listing.
            returned: on success
            type: string
            sample: description_example
        listing_id:
            description:
                - The OCID of the listing.
            returned: on success
            type: string
            sample: ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx
        display_name:
            description:
                - Name of the listing.
            returned: on success
            type: string
            sample: display_name_example
        time_published:
            description:
                - "Date and time the listing was published, in RFC3339 format.
                  Example: `2018-03-20T12:32:53.532Z`"
            returned: on success
            type: string
            sample: 2018-03-20T12:32:53.532Z
        publisher_logo_url:
            description:
                - Publisher's logo URL.
            returned: on success
            type: string
            sample: publisher_logo_url_example
        publisher_name:
            description:
                - Name of the publisher who published this listing.
            returned: on success
            type: string
            sample: publisher_name_example
        summary:
            description:
                - Summary of the listing.
            returned: on success
            type: string
            sample: summary_example
    sample: [{
        "contact_url": "contact_url_example",
        "description": "description_example",
        "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_published": "2018-03-20T12:32:53.532Z",
        "publisher_logo_url": "publisher_logo_url_example",
        "publisher_name": "publisher_name_example",
        "summary": "summary_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AppCatalogListingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "listing_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_app_catalog_listing,
            listing_id=self.module.params.get("listing_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "publisher_name",
            "publisher_type",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_app_catalog_listings, **optional_kwargs
        )


AppCatalogListingFactsHelperCustom = get_custom_class(
    "AppCatalogListingFactsHelperCustom"
)


class ResourceFactsHelper(
    AppCatalogListingFactsHelperCustom, AppCatalogListingFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            listing_id=dict(aliases=["id"], type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            publisher_name=dict(type="str"),
            publisher_type=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="app_catalog_listing",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(app_catalog_listings=result)


if __name__ == "__main__":
    main()
