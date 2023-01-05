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
module: oci_marketplace_publication_package_facts
short_description: Fetches details about one or multiple PublicationPackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PublicationPackage resources in Oracle Cloud Infrastructure
    - Lists the packages in the specified publication.
    - If I(package_version) is specified, the details of a single PublicationPackage will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    publication_id:
        description:
            - The unique identifier for the publication.
        type: str
        required: true
    package_version:
        description:
            - The version of the package. Package versions are unique within a listing.
            - Required to get a specific publication_package.
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific publication_package
  oci_marketplace_publication_package_facts:
    # required
    publication_id: "ocid1.publication.oc1..xxxxxxEXAMPLExxxxxx"
    package_version: package_version_example

- name: List publication_packages
  oci_marketplace_publication_package_facts:
    # required
    publication_id: "ocid1.publication.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    package_version: package_version_example
    package_type: package_type_example
    sort_by: TIMERELEASED
    sort_order: ASC

"""

RETURN = """
publication_packages:
    description:
        - List of PublicationPackage resources
    returned: on success
    type: complex
    contains:
        app_catalog_listing_id:
            description:
                - The ID of the listing resource associated with this publication package. For more information, see
                  L(AppCatalogListing,https://docs.cloud.oracle.com/en-us/iaas/api/#/en/iaas/latest/AppCatalogListing/) in the Core Services API.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.appcataloglisting.oc1..xxxxxxEXAMPLExxxxxx"
        app_catalog_listing_resource_version:
            description:
                - The resource version of the listing resource associated with this publication package.
                - Returned for get operation
            returned: on success
            type: str
            sample: app_catalog_listing_resource_version_example
        image_id:
            description:
                - The ID of the image that corresponds to the package.
                - Returned for get operation
            returned: on success
            type: str
            sample: "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx"
        description:
            description:
                - A description of the package.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        version:
            description:
                - The package version.
                - Returned for get operation
            returned: on success
            type: str
            sample: version_example
        operating_system:
            description:
                - ""
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the operating system.
                    returned: on success
                    type: str
                    sample: name_example
        resource_link:
            description:
                - A link to the stack resource.
                - Returned for get operation
            returned: on success
            type: str
            sample: resource_link_example
        variables:
            description:
                - A list of variables for the stack resource.
                - Returned for get operation
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - The name of the variable.
                    returned: on success
                    type: str
                    sample: name_example
                default_value:
                    description:
                        - The variable's default value.
                    returned: on success
                    type: str
                    sample: default_value_example
                description:
                    description:
                        - A description of the variable.
                    returned: on success
                    type: str
                    sample: description_example
                data_type:
                    description:
                        - The data type of the variable.
                    returned: on success
                    type: str
                    sample: STRING
                is_mandatory:
                    description:
                        - Whether the variable is mandatory.
                    returned: on success
                    type: bool
                    sample: true
                hint_message:
                    description:
                        - A brief textual description that helps to explain the variable.
                    returned: on success
                    type: str
                    sample: hint_message_example
        listing_id:
            description:
                - The ID of the listing that the specified package belongs to.
            returned: on success
            type: str
            sample: "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx"
        package_version:
            description:
                - The version of the specified package.
                - Returned for list operation
            returned: on success
            type: str
            sample: package_version_example
        package_type:
            description:
                - The specified package's type.
            returned: on success
            type: str
            sample: ORCHESTRATION
        resource_id:
            description:
                - The unique identifier for the package resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        time_created:
            description:
                - The date and time the publication package was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "app_catalog_listing_id": "ocid1.appcataloglisting.oc1..xxxxxxEXAMPLExxxxxx",
        "app_catalog_listing_resource_version": "app_catalog_listing_resource_version_example",
        "image_id": "ocid1.image.oc1..xxxxxxEXAMPLExxxxxx",
        "description": "description_example",
        "version": "version_example",
        "operating_system": {
            "name": "name_example"
        },
        "resource_link": "resource_link_example",
        "variables": [{
            "name": "name_example",
            "default_value": "default_value_example",
            "description": "description_example",
            "data_type": "STRING",
            "is_mandatory": true,
            "hint_message": "hint_message_example"
        }],
        "listing_id": "ocid1.listing.oc1..xxxxxxEXAMPLExxxxxx",
        "package_version": "package_version_example",
        "package_type": "ORCHESTRATION",
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
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
    from oci.marketplace import MarketplaceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicationPackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "publication_id",
            "package_version",
        ]

    def get_required_params_for_list(self):
        return [
            "publication_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_publication_package,
            publication_id=self.module.params.get("publication_id"),
            package_version=self.module.params.get("package_version"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "package_version",
            "package_type",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_publication_packages,
            publication_id=self.module.params.get("publication_id"),
            **optional_kwargs
        )


PublicationPackageFactsHelperCustom = get_custom_class(
    "PublicationPackageFactsHelperCustom"
)


class ResourceFactsHelper(
    PublicationPackageFactsHelperCustom, PublicationPackageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            publication_id=dict(type="str", required=True),
            package_version=dict(type="str"),
            package_type=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMERELEASED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="publication_package",
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

    module.exit_json(publication_packages=result)


if __name__ == "__main__":
    main()
