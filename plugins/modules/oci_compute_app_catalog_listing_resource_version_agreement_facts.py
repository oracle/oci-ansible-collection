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
module: oci_compute_app_catalog_listing_resource_version_agreement_facts
short_description: Fetches details about a AppCatalogListingResourceVersionAgreement resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AppCatalogListingResourceVersionAgreement resource in Oracle Cloud Infrastructure
    - Retrieves the agreements for a particular resource version of a listing.
version_added: "2.5"
options:
    listing_id:
        description:
            - The OCID of the listing.
        type: str
        aliases: ["id"]
        required: true
    resource_version:
        description:
            - Listing Resource Version.
        type: str
        aliases: ["version"]
        required: true
author: Oracle (@oracle)
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific app_catalog_listing_resource_version_agreement
  oci_compute_app_catalog_listing_resource_version_agreement_facts:
    listing_id: ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx
    resource_version: resource_version_example

"""

RETURN = """
app_catalog_listing_resource_version_agreement:
    description:
        - AppCatalogListingResourceVersionAgreement resource
    returned: on success
    type: complex
    contains:
        listing_id:
            description:
                - The OCID of the listing associated with these agreements.
            returned: on success
            type: string
            sample: ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx
        listing_resource_version:
            description:
                - Listing resource version associated with these agreements.
            returned: on success
            type: string
            sample: listing_resource_version_example
        oracle_terms_of_use_link:
            description:
                - Oracle TOU link
            returned: on success
            type: string
            sample: oracle_terms_of_use_link_example
        eula_link:
            description:
                - EULA link
            returned: on success
            type: string
            sample: eula_link_example
        time_retrieved:
            description:
                - "Date and time the agreements were retrieved, in RFC3339 format.
                  Example: `2018-03-20T12:32:53.532Z`"
            returned: on success
            type: string
            sample: 2018-03-20T12:32:53.532Z
        signature:
            description:
                - A generated signature for this agreement retrieval operation which should be used in the create subscription call.
            returned: on success
            type: string
            sample: signature_example
    sample: {
        "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
        "listing_resource_version": "listing_resource_version_example",
        "oracle_terms_of_use_link": "oracle_terms_of_use_link_example",
        "eula_link": "eula_link_example",
        "time_retrieved": "2018-03-20T12:32:53.532Z",
        "signature": "signature_example"
    }
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


class AppCatalogListingResourceVersionAgreementFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "listing_id",
            "resource_version",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_app_catalog_listing_agreements,
            listing_id=self.module.params.get("listing_id"),
            resource_version=self.module.params.get("resource_version"),
        )


AppCatalogListingResourceVersionAgreementFactsHelperCustom = get_custom_class(
    "AppCatalogListingResourceVersionAgreementFactsHelperCustom"
)


class ResourceFactsHelper(
    AppCatalogListingResourceVersionAgreementFactsHelperCustom,
    AppCatalogListingResourceVersionAgreementFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            listing_id=dict(aliases=["id"], type="str", required=True),
            resource_version=dict(aliases=["version"], type="str", required=True),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="app_catalog_listing_resource_version_agreement",
        service_client_class=ComputeClient,
        namespace="core",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(app_catalog_listing_resource_version_agreement=result)


if __name__ == "__main__":
    main()
