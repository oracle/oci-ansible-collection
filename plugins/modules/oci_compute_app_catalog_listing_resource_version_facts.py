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
module: oci_compute_app_catalog_listing_resource_version_facts
short_description: Fetches details about one or multiple AppCatalogListingResourceVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AppCatalogListingResourceVersion resources in Oracle Cloud Infrastructure
    - Gets all resource versions for a particular listing.
    - If I(resource_version) is specified, the details of a single AppCatalogListingResourceVersion will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    resource_version:
        description:
            - Listing Resource Version.
            - Required to get a specific app_catalog_listing_resource_version.
        type: str
    listing_id:
        description:
            - The OCID of the listing.
        type: str
        aliases: ["id"]
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific app_catalog_listing_resource_version
  oci_compute_app_catalog_listing_resource_version_facts:
    # required
    resource_version: resource_version_example
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"

- name: List app_catalog_listing_resource_versions
  oci_compute_app_catalog_listing_resource_version_facts:
    # required
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC

"""

RETURN = """
app_catalog_listing_resource_versions:
    description:
        - List of AppCatalogListingResourceVersion resources
    returned: on success
    type: complex
    contains:
        available_regions:
            description:
                - List of regions that this listing resource version is available.
                - For information about regions, see
                  L(Regions and Availability Domains,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/regions.htm).
                - "Example: `[\\"us-ashburn-1\\", \\"us-phoenix-1\\"]`"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        compatible_shapes:
            description:
                - Array of shapes compatible with this resource.
                - You can enumerate all available shapes by calling L(ListShapes,https://docs.cloud.oracle.com/en-
                  us/iaas/api/#/en/iaas/latest/Shape/ListShapes).
                - "Example: `[\\"VM.Standard1.1\\", \\"VM.Standard1.2\\"]`"
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        accessible_ports:
            description:
                - List of accessible ports for instances launched with this listing resource version.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        allowed_actions:
            description:
                - Allowed actions for the listing resource.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        listing_id:
            description:
                - The OCID of the listing this resource version belongs to.
            returned: on success
            type: str
            sample: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
        time_published:
            description:
                - "Date and time the listing resource version was published, in L(RFC3339,https://tools.ietf.org/html/rfc3339) format.
                  Example: `2018-03-20T12:32:53.532Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        listing_resource_id:
            description:
                - OCID of the listing resource.
            returned: on success
            type: str
            sample: "ocid1.listingresource.oc1..xxxxxxEXAMPLExxxxxx"
        listing_resource_version:
            description:
                - Resource Version.
            returned: on success
            type: str
            sample: listing_resource_version_example
    sample: [{
        "available_regions": [],
        "compatible_shapes": [],
        "accessible_ports": [],
        "allowed_actions": [],
        "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
        "time_published": "2013-10-20T19:20:30+01:00",
        "listing_resource_id": "ocid1.listingresource.oc1..xxxxxxEXAMPLExxxxxx",
        "listing_resource_version": "listing_resource_version_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.core import ComputeClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AppCatalogListingResourceVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "listing_id",
            "resource_version",
        ]

    def get_required_params_for_list(self):
        return [
            "listing_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_app_catalog_listing_resource_version,
            listing_id=self.module.params.get("listing_id"),
            resource_version=self.module.params.get("resource_version"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_app_catalog_listing_resource_versions,
            listing_id=self.module.params.get("listing_id"),
            **optional_kwargs
        )


AppCatalogListingResourceVersionFactsHelperCustom = get_custom_class(
    "AppCatalogListingResourceVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    AppCatalogListingResourceVersionFactsHelperCustom,
    AppCatalogListingResourceVersionFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            resource_version=dict(type="str"),
            listing_id=dict(aliases=["id"], type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="app_catalog_listing_resource_version",
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

    module.exit_json(app_catalog_listing_resource_versions=result)


if __name__ == "__main__":
    main()
