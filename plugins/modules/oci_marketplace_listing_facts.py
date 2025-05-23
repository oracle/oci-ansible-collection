#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_marketplace_listing_facts
short_description: Fetches details about one or multiple Listing resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Listing resources in Oracle Cloud Infrastructure
    - Gets a list of listings from Oracle Cloud Infrastructure Marketplace by searching keywords and
      filtering according to listing attributes.
    - If you plan to launch an instance from an image listing, you must first subscribe to the listing. When
      you launch the instance, you also need to provide the image ID of the listing resource version that you want.
    - Subscribing to the listing requires you to first get a signature from the terms of use agreement for the
      listing resource version. To get the signature, issue a L(GetAppCatalogListingAgreements,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements/GetAppCatalogListingAgreements) API call.
      The L(AppCatalogListingResourceVersionAgreements,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersionAgreements)
      object, including
      its signature, is returned in the response. With the signature for the terms of use agreement for the desired
      listing resource version, create a subscription by issuing a
      L(CreateAppCatalogSubscription,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogSubscription/CreateAppCatalogSubscription) API
      call.
    - To get the image ID to launch an instance, issue a L(GetAppCatalogListingResourceVersion,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/iaas/latest/AppCatalogListingResourceVersion/GetAppCatalogListingResourceVersion) API call.
      Lastly, to launch the instance, use the image ID of the listing resource version to issue a L(LaunchInstance,https://docs.cloud.oracle.com/en-
      us/iaas/api/#/en/iaas/latest/Instance/LaunchInstance) API call.
    - If I(listing_id) is specified, the details of a single Listing will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    name:
        description:
            - The name of the listing.
        type: list
        elements: str
    listing_id:
        description:
            - The unique identifier for the listing.
            - Required to get a specific listing.
        type: str
        aliases: ["id"]
    image_id:
        description:
            - The image identifier of the listing.
        type: str
    publisher_id:
        description:
            - Limit results to just this publisher.
        type: str
    package_type:
        description:
            - A filter to return only packages that match the given package type exactly.
        type: str
    sort_by:
        description:
            - The field to use to sort listed results. You can only specify one field to sort by.
              `TIMERELEASED` displays results in descending order by default.
              You can change your preference by specifying a different sort order.
        type: str
        choices:
            - "TIMERELEASED"
    sort_order:
        description:
            - The sort order to use, either `ASC` or `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    category:
        description:
            - Name of the product category or categories. If you specify multiple categories, then Marketplace returns any listing with
              one or more matching categories.
        type: list
        elements: str
    pricing:
        description:
            - Name of the pricing type. If multiple pricing types are provided, then any listing with
              one or more matching pricing models will be returned.
        type: list
        elements: str
        choices:
            - "FREE"
            - "BYOL"
            - "PAYGO"
    is_featured:
        description:
            - Indicates whether to show only featured listings. If this is set to `false` or is omitted, then all listings will be returned.
        type: bool
    listing_types:
        description:
            - The type of the listing.
        type: list
        elements: str
        choices:
            - "COMMUNITY"
            - "PARTNER"
            - "PRIVATE"
    operating_systems:
        description:
            - The operating system of the listing.
        type: list
        elements: str
    compartment_id:
        description:
            - The unique identifier for the compartment.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific listing
  oci_marketplace_listing_facts:
    # required
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: List listings
  oci_marketplace_listing_facts:

    # optional
    name: [ "name_example" ]
    listing_id: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
    image_id: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
    publisher_id: "ocid1.publisher.oc1..xxxxxxEXAMPLExxxxxx"
    package_type: package_type_example
    sort_by: TIMERELEASED
    sort_order: ASC
    category: [ "category_example" ]
    pricing: [ "FREE" ]
    is_featured: true
    listing_types: [ "COMMUNITY" ]
    operating_systems: [ "operating_systems_example" ]
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
listings:
    description:
        - List of Listing resources
    returned: on success
    type: complex
    contains:
        version:
            description:
                - The version of the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: version_example
        keywords:
            description:
                - Keywords associated with the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: keywords_example
        usage_information:
            description:
                - Usage information for the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: usage_information_example
        long_description:
            description:
                - A long description of the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: long_description_example
        license_model_description:
            description:
                - A description of the publisher's licensing model for the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: license_model_description_example
        system_requirements:
            description:
                - System requirements for the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: system_requirements_example
        time_released:
            description:
                - The release date of the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        release_notes:
            description:
                - Release notes for the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: release_notes_example
        languages:
            description:
                - Languages supported by the listing.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the item.
                    returned: on success
                    type: str
                    sample: name_example
                code:
                    description:
                        - A code assigned to the item.
                    returned: on success
                    type: str
                    sample: code_example
        screenshots:
            description:
                - Screenshots of the listing.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the screenshot.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - A description of the screenshot.
                    returned: on success
                    type: str
                    sample: description_example
                content_url:
                    description:
                        - The content URL of the screenshot.
                    returned: on success
                    type: str
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the screenshot.
                    returned: on success
                    type: str
                    sample: mime_type_example
                file_extension:
                    description:
                        - The file extension of the screenshot.
                    returned: on success
                    type: str
                    sample: file_extension_example
        videos:
            description:
                - Videos of the listing.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Text that describes the resource.
                    returned: on success
                    type: str
                    sample: name_example
                url:
                    description:
                        - The URL of the resource.
                    returned: on success
                    type: str
                    sample: url_example
        support_contacts:
            description:
                - Contact information to use to get support from the publisher for the listing.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the contact.
                    returned: on success
                    type: str
                    sample: name_example
                phone:
                    description:
                        - The phone number of the contact.
                    returned: on success
                    type: str
                    sample: phone_example
                email:
                    description:
                        - The email of the contact.
                    returned: on success
                    type: str
                    sample: email_example
                subject:
                    description:
                        - The email subject line to use when contacting support.
                    returned: on success
                    type: str
                    sample: subject_example
        support_links:
            description:
                - Links to support resources for the listing.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Text that describes the resource.
                    returned: on success
                    type: str
                    sample: name_example
                url:
                    description:
                        - The URL of the resource.
                    returned: on success
                    type: str
                    sample: url_example
        documentation_links:
            description:
                - Links to additional documentation provided by the publisher specifically for the listing.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Text that describes the resource.
                    returned: on success
                    type: str
                    sample: name_example
                url:
                    description:
                        - The URL of the resource.
                    returned: on success
                    type: str
                    sample: url_example
                document_category:
                    description:
                        - The category that the document belongs to.
                    returned: on success
                    type: str
                    sample: document_category_example
        banner:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name used to refer to the upload data.
                    returned: on success
                    type: str
                    sample: name_example
                content_url:
                    description:
                        - The content URL of the upload data.
                    returned: on success
                    type: str
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the upload data.
                    returned: on success
                    type: str
                    sample: mime_type_example
                file_extension:
                    description:
                        - The file extension of the upload data.
                    returned: on success
                    type: str
                    sample: file_extension_example
        default_package_version:
            description:
                - The default package version.
                - Returned for get operation
            returned: on success
            type: str
            sample: default_package_version_example
        links:
            description:
                - Links to reference material.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                rel:
                    description:
                        - Reference links to the previous page, next page, and other pages.
                    returned: on success
                    type: str
                    sample: SELF
                href:
                    description:
                        - The anchor tag.
                    returned: on success
                    type: str
                    sample: href_example
        id:
            description:
                - The unique identifier for the listing in Marketplace.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the listing.
            returned: on success
            type: str
            sample: name_example
        short_description:
            description:
                - A short description of the listing.
            returned: on success
            type: str
            sample: short_description_example
        is_rover_exportable:
            description:
                - True if this application is Rover exportable
                - Returned for list operation
            returned: on success
            type: bool
            sample: true
        tagline:
            description:
                - The tagline of the listing.
            returned: on success
            type: str
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
                    type: str
                    sample: name_example
                content_url:
                    description:
                        - The content URL of the upload data.
                    returned: on success
                    type: str
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the upload data.
                    returned: on success
                    type: str
                    sample: mime_type_example
                file_extension:
                    description:
                        - The file extension of the upload data.
                    returned: on success
                    type: str
                    sample: file_extension_example
        package_type:
            description:
                - The listing's package type.
            returned: on success
            type: str
            sample: ORCHESTRATION
        pricing_types:
            description:
                - Summary of the pricing types available across all packages in the listing.
                - Returned for list operation
            returned: on success
            type: list
            sample: []
        compatible_architectures:
            description:
                - The list of compatible architectures supported by the listing
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
                    type: str
                    sample: name_example
                code:
                    description:
                        - The code of the region.
                    returned: on success
                    type: str
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
                            type: str
                            sample: name_example
                        code:
                            description:
                                - A code assigned to the item.
                            returned: on success
                            type: str
                            sample: code_example
        is_featured:
            description:
                - Indicates whether the listing is included in Featured Listings.
            returned: on success
            type: bool
            sample: true
        categories:
            description:
                - Categories that the listing belongs to.
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
                        - Unique identifier for the publisher.
                    returned: on success
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                name:
                    description:
                        - The name of the publisher.
                    returned: on success
                    type: str
                    sample: name_example
                description:
                    description:
                        - A description of the publisher.
                    returned: on success
                    type: str
                    sample: description_example
                year_founded:
                    description:
                        - The year the publisher's company or organization was founded.
                    returned: on success
                    type: int
                    sample: 56
                website_url:
                    description:
                        - The publisher's website.
                    returned: on success
                    type: str
                    sample: website_url_example
                contact_email:
                    description:
                        - The email address of the publisher.
                    returned: on success
                    type: str
                    sample: contact_email_example
                contact_phone:
                    description:
                        - The phone number of the publisher.
                    returned: on success
                    type: str
                    sample: contact_phone_example
                hq_address:
                    description:
                        - The address of the publisher's headquarters.
                    returned: on success
                    type: str
                    sample: hq_address_example
                logo:
                    description:
                        - ""
                    returned: on success
                    type: complex
                    contains:
                        name:
                            description:
                                - The name used to refer to the upload data.
                            returned: on success
                            type: str
                            sample: name_example
                        content_url:
                            description:
                                - The content URL of the upload data.
                            returned: on success
                            type: str
                            sample: content_url_example
                        mime_type:
                            description:
                                - The MIME type of the upload data.
                            returned: on success
                            type: str
                            sample: mime_type_example
                        file_extension:
                            description:
                                - The file extension of the upload data.
                            returned: on success
                            type: str
                            sample: file_extension_example
                links:
                    description:
                        - Reference links.
                    returned: on success
                    type: complex
                    contains:
                        rel:
                            description:
                                - Reference links to the previous page, next page, and other pages.
                            returned: on success
                            type: str
                            sample: SELF
                        href:
                            description:
                                - The anchor tag.
                            returned: on success
                            type: str
                            sample: href_example
        supported_operating_systems:
            description:
                - List of operating systems supported by the listing.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the operating system.
                    returned: on success
                    type: str
                    sample: name_example
        listing_type:
            description:
                - The publisher category to which the listing belongs. The publisher category informs where the listing appears for use.
            returned: on success
            type: str
            sample: COMMUNITY
    sample: [{
        "version": "version_example",
        "keywords": "keywords_example",
        "usage_information": "usage_information_example",
        "long_description": "long_description_example",
        "license_model_description": "license_model_description_example",
        "system_requirements": "system_requirements_example",
        "time_released": "2013-10-20T19:20:30+01:00",
        "release_notes": "release_notes_example",
        "languages": [{
            "name": "name_example",
            "code": "code_example"
        }],
        "screenshots": [{
            "name": "name_example",
            "description": "description_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example",
            "file_extension": "file_extension_example"
        }],
        "videos": [{
            "name": "name_example",
            "url": "url_example"
        }],
        "support_contacts": [{
            "name": "name_example",
            "phone": "phone_example",
            "email": "email_example",
            "subject": "subject_example"
        }],
        "support_links": [{
            "name": "name_example",
            "url": "url_example"
        }],
        "documentation_links": [{
            "name": "name_example",
            "url": "url_example",
            "document_category": "document_category_example"
        }],
        "banner": {
            "name": "name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example",
            "file_extension": "file_extension_example"
        },
        "default_package_version": "default_package_version_example",
        "links": [{
            "rel": "SELF",
            "href": "href_example"
        }],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "short_description": "short_description_example",
        "is_rover_exportable": true,
        "tagline": "tagline_example",
        "icon": {
            "name": "name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example",
            "file_extension": "file_extension_example"
        },
        "package_type": "ORCHESTRATION",
        "pricing_types": [],
        "compatible_architectures": [],
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
            "description": "description_example",
            "year_founded": 56,
            "website_url": "website_url_example",
            "contact_email": "contact_email_example",
            "contact_phone": "contact_phone_example",
            "hq_address": "hq_address_example",
            "logo": {
                "name": "name_example",
                "content_url": "content_url_example",
                "mime_type": "mime_type_example",
                "file_extension": "file_extension_example"
            },
            "links": [{
                "rel": "SELF",
                "href": "href_example"
            }]
        },
        "supported_operating_systems": [{
            "name": "name_example"
        }],
        "listing_type": "COMMUNITY"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.marketplace import MarketplaceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ListingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "listing_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        optional_get_method_params = [
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_get_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.call_with_backoff(
            self.client.get_listing,
            listing_id=self.module.params.get("listing_id"),
            **optional_kwargs
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "listing_id",
            "image_id",
            "publisher_id",
            "package_type",
            "sort_by",
            "sort_order",
            "category",
            "pricing",
            "is_featured",
            "listing_types",
            "operating_systems",
            "compartment_id",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_listings, **optional_kwargs
        )


ListingFactsHelperCustom = get_custom_class("ListingFactsHelperCustom")


class ResourceFactsHelper(ListingFactsHelperCustom, ListingFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            name=dict(type="list", elements="str"),
            listing_id=dict(aliases=["id"], type="str"),
            image_id=dict(type="str"),
            publisher_id=dict(type="str"),
            package_type=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMERELEASED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            category=dict(type="list", elements="str"),
            pricing=dict(
                type="list", elements="str", choices=["FREE", "BYOL", "PAYGO"]
            ),
            is_featured=dict(type="bool"),
            listing_types=dict(
                type="list", elements="str", choices=["COMMUNITY", "PARTNER", "PRIVATE"]
            ),
            operating_systems=dict(type="list", elements="str"),
            compartment_id=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="listing",
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

    module.exit_json(listings=result)


if __name__ == "__main__":
    main()
