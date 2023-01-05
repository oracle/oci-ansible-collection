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
module: oci_compute_app_catalog_subscription_facts
short_description: Fetches details about one or multiple AppCatalogSubscription resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AppCatalogSubscription resources in Oracle Cloud Infrastructure
    - Lists subscriptions for a compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for DISPLAYNAME is ascending. The DISPLAYNAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The DISPLAYNAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    listing_id:
        description:
            - A filter to return only the listings that matches the given listing id.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_display_name_option ]
"""

EXAMPLES = """
- name: List app_catalog_subscriptions
  oci_compute_app_catalog_subscription_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
app_catalog_subscriptions:
    description:
        - List of AppCatalogSubscription resources
    returned: on success
    type: complex
    contains:
        publisher_name:
            description:
                - Name of the publisher who published this listing.
            returned: on success
            type: str
            sample: publisher_name_example
        listing_id:
            description:
                - The ocid of the listing resource.
            returned: on success
            type: str
            sample: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
        listing_resource_version:
            description:
                - Listing resource version.
            returned: on success
            type: str
            sample: listing_resource_version_example
        listing_resource_id:
            description:
                - Listing resource id.
            returned: on success
            type: str
            sample: "ocid1.listingresource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name. Does not have to be unique, and it's changeable.
                  Avoid entering confidential information.
            returned: on success
            type: str
            sample: display_name_example
        summary:
            description:
                - The short summary to the listing.
            returned: on success
            type: str
            sample: summary_example
        compartment_id:
            description:
                - The compartmentID of the subscription.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - "Date and time at which the subscription was created, in L(RFC3339,https://tools.ietf.org/html/rfc3339) format.
                  Example: `2018-03-20T12:32:53.532Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "publisher_name": "publisher_name_example",
        "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
        "listing_resource_version": "listing_resource_version_example",
        "listing_resource_id": "ocid1.listingresource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "summary": "summary_example",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "time_created": "2013-10-20T19:20:30+01:00"
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


class AppCatalogSubscriptionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "listing_id",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_app_catalog_subscriptions,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


AppCatalogSubscriptionFactsHelperCustom = get_custom_class(
    "AppCatalogSubscriptionFactsHelperCustom"
)


class ResourceFactsHelper(
    AppCatalogSubscriptionFactsHelperCustom, AppCatalogSubscriptionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            listing_id=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="app_catalog_subscription",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(app_catalog_subscriptions=result)


if __name__ == "__main__":
    main()
