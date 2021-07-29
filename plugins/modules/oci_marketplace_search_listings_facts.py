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
module: oci_marketplace_search_listings_facts
short_description: Fetches details about one or multiple SearchListings resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SearchListings resources in Oracle Cloud Infrastructure
    - Find listings that match the specified criteria. The search query could be free text
      or structured.
version_added: "2.9"
author: Oracle (@oracle)
options:
    type:
        description:
            - The type of SearchDetails, whether FreeText or Structured.
        type: str
        choices:
            - "Structured"
            - "FreeText"
        required: true
    matching_context_type:
        description:
            - The type of matching context returned in the response.
        type: str
        choices:
            - "NONE"
            - "HIGHLIGHTS"
    query:
        description:
            - The structured query describing which resources to search for.
            - Required when type is 'Structured'
        type: str
    text:
        description:
            - The text to search for.
            - Required when type is 'FreeText'
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List search_listings
  oci_marketplace_search_listings_facts:
    type: "FreeText"
    text: "Fortinet"

"""

RETURN = """
search_listings:
    description:
        - List of SearchListings resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The unique identifier for the listing in Marketplace.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the listing.
            returned: on success
            type: string
            sample: name_example
        short_description:
            description:
                - A short description of the listing.
            returned: on success
            type: string
            sample: short_description_example
        tagline:
            description:
                - The tagline of the listing.
            returned: on success
            type: string
            sample: tagline_example
        icon:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name used to refer to the upload data.
                    returned: on success
                    type: string
                    sample: name_example
                content_url:
                    description:
                        - The content URL of the upload data.
                    returned: on success
                    type: string
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the upload data.
                    returned: on success
                    type: string
                    sample: mime_type_example
                file_extension:
                    description:
                        - The file extension of the upload data.
                    returned: on success
                    type: string
                    sample: file_extension_example
        package_type:
            description:
                - The listing's package type.
            returned: on success
            type: string
            sample: ORCHESTRATION
        pricing_types:
            description:
                - Summary of the pricing types available across all packages in the listing.
            returned: on success
            type: list
            sample: []
        regions:
            description:
                - The regions where you can deploy the listing. (Some listings have restrictions that limit their deployment to United States regions only.)
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the region.
                    returned: on success
                    type: string
                    sample: name_example
                code:
                    description:
                        - The code of the region.
                    returned: on success
                    type: string
                    sample: code_example
                countries:
                    description:
                        - Countries in the region.
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name of the item.
                            returned: on success
                            type: string
                            sample: name_example
                        code:
                            description:
                                - A code assigned to the item.
                            returned: on success
                            type: string
                            sample: code_example
        is_featured:
            description:
                - Indicates whether the listing is featured.
            returned: on success
            type: bool
            sample: true
        categories:
            description:
                - Product categories that the listing belongs to.
            returned: on success
            type: list
            sample: []
        publisher:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - The unique identifier for the publisher.
                    returned: on success
                    type: string
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the publisher.
                    returned: on success
                    type: string
                    sample: name_example
                description:
                    description:
                        - A description of the publisher.
                    returned: on success
                    type: string
                    sample: description_example
        supported_operating_systems:
            description:
                - The list of operating systems supported by the listing.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the operating system.
                    returned: on success
                    type: string
                    sample: name_example
        listing_type:
            description:
                - The publisher category to which the listing belongs. The publisher category informs where the listing appears for use.
            returned: on success
            type: string
            sample: COMMUNITY
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "short_description": "short_description_example",
        "tagline": "tagline_example",
        "icon": {
            "name": "name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example",
            "file_extension": "file_extension_example"
        },
        "package_type": "ORCHESTRATION",
        "pricing_types": [],
        "regions": [{
            "name": "name_example",
            "code": "code_example",
            "countries": [{
                "name": "name_example",
                "code": "code_example"
            }]
        }],
        "is_featured": true,
        "categories": [],
        "publisher": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "name": "name_example",
            "description": "description_example"
        },
        "supported_operating_systems": [{
            "name": "name_example"
        }],
        "listing_type": "COMMUNITY"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.marketplace import MarketplaceClient
    from oci.marketplace.models import SearchListingsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SearchListingsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "type",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.search_listings,
            search_listings_details=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, SearchListingsDetails
            ),
            **optional_kwargs
        )


SearchListingsFactsHelperCustom = get_custom_class("SearchListingsFactsHelperCustom")


class ResourceFactsHelper(
    SearchListingsFactsHelperCustom, SearchListingsFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            type=dict(type="str", required=True, choices=["Structured", "FreeText"]),
            matching_context_type=dict(type="str", choices=["NONE", "HIGHLIGHTS"]),
            query=dict(type="str"),
            text=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="search_listings",
        service_client_class=MarketplaceClient,
        namespace="marketplace",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(search_listings=result)


if __name__ == "__main__":
    main()
