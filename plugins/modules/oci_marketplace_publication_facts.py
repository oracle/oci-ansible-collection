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
module: oci_marketplace_publication_facts
short_description: Fetches details about one or multiple Publication resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Publication resources in Oracle Cloud Infrastructure
    - Lists the publications in the specified compartment.
    - If I(publication_id) is specified, the details of a single Publication will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier for the compartment.
            - Required to list multiple publications.
        type: str
    listing_type:
        description:
            - The type of the listing.
            - Required to list multiple publications.
        type: str
        choices:
            - "COMMUNITY"
            - "PARTNER"
            - "PRIVATE"
    name:
        description:
            - The name of the publication.
        type: list
        elements: str
    publication_id:
        description:
            - The unique identifier for the publication.
            - Required to get a specific publication.
        type: str
        aliases: ["id"]
    operating_systems:
        description:
            - The operating system of the listing.
        type: list
        elements: str
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
- name: Get a specific publication
  oci_marketplace_publication_facts:
    # required
    publication_id: "ocid1.publication.oc1..xxxxxxEXAMPLExxxxxx"

- name: List publications
  oci_marketplace_publication_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    listing_type: COMMUNITY

    # optional
    name: [ "name_example" ]
    publication_id: "ocid1.publication.oc1..xxxxxxEXAMPLExxxxxx"
    operating_systems: [ "operating_systems_example" ]
    sort_by: TIMERELEASED
    sort_order: ASC

"""

RETURN = """
publications:
    description:
        - List of Publication resources
    returned: on success
    type: complex
    contains:
        long_description:
            description:
                - A long description of the publication to use in the listing.
                - Returned for get operation
            returned: on success
            type: str
            sample: long_description_example
        support_contacts:
            description:
                - Contact information for getting support from the publisher for the listing.
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
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        lifecycle_state:
            description:
                - The lifecycle state of the publication.
            returned: on success
            type: str
            sample: CREATING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the publication exists.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The unique identifier for the publication in Marketplace.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - The name of the publication, which is also used in the listing.
            returned: on success
            type: str
            sample: name_example
        short_description:
            description:
                - A short description of the publication to use in the listing.
            returned: on success
            type: str
            sample: short_description_example
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
        supported_operating_systems:
            description:
                - The list of operating systems supprted by the listing.
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
                - The publisher category to which the publication belongs. The publisher category informs where the listing appears for use.
            returned: on success
            type: str
            sample: COMMUNITY
        time_created:
            description:
                - The date and time the publication was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "long_description": "long_description_example",
        "support_contacts": [{
            "name": "name_example",
            "phone": "phone_example",
            "email": "email_example",
            "subject": "subject_example"
        }],
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "lifecycle_state": "CREATING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "short_description": "short_description_example",
        "icon": {
            "name": "name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example",
            "file_extension": "file_extension_example"
        },
        "package_type": "ORCHESTRATION",
        "supported_operating_systems": [{
            "name": "name_example"
        }],
        "listing_type": "COMMUNITY",
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


class PublicationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "publication_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "listing_type",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_publication,
            publication_id=self.module.params.get("publication_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "publication_id",
            "operating_systems",
            "sort_by",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_publications,
            compartment_id=self.module.params.get("compartment_id"),
            listing_type=self.module.params.get("listing_type"),
            **optional_kwargs
        )


PublicationFactsHelperCustom = get_custom_class("PublicationFactsHelperCustom")


class ResourceFactsHelper(PublicationFactsHelperCustom, PublicationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            listing_type=dict(type="str", choices=["COMMUNITY", "PARTNER", "PRIVATE"]),
            name=dict(type="list", elements="str"),
            publication_id=dict(aliases=["id"], type="str"),
            operating_systems=dict(type="list", elements="str"),
            sort_by=dict(type="str", choices=["TIMERELEASED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="publication",
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

    module.exit_json(publications=result)


if __name__ == "__main__":
    main()
