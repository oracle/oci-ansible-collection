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
module: oci_service_catalog_application_facts
short_description: Fetches details about one or multiple Application resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Application resources in Oracle Cloud Infrastructure
    - Lists all the applications in a service catalog or a tenancy.
      If no parameter is specified, all catalogs from all compartments in
      the tenancy will be scanned for any type of content.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier for the compartment.
        type: str
    service_catalog_id:
        description:
            - The unique identifier for the service catalog.
        type: str
    entity_type:
        description:
            - The type of the application in the service catalog.
        type: str
    display_name:
        description:
            - Exact match name filter.
        type: str
        aliases: ["name"]
    entity_id:
        description:
            - The unique identifier of the entity associated with service catalog.
        type: str
    publisher_id:
        description:
            - Limit results to just this publisher.
        type: list
        elements: str
    package_type:
        description:
            - Name of the package type. If multiple package types are provided, then any resource with
              one or more matching package types will be returned.
        type: list
        elements: str
        choices:
            - "STACK"
    pricing:
        description:
            - Name of the pricing type. If multiple pricing types are provided, then any resource with
              one or more matching pricing models will be returned.
        type: list
        elements: str
        choices:
            - "FREE"
            - "BYOL"
            - "PAYGO"
    is_featured:
        description:
            - Indicates whether to show only featured resources. If this is set to `false` or is omitted, then all resources will be returned.
        type: bool
    sort_order:
        description:
            - The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List applications
  oci_service_catalog_application_facts:

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    service_catalog_id: "ocid1.servicecatalog.oc1..xxxxxxEXAMPLExxxxxx"
    entity_type: entity_type_example
    display_name: display_name_example
    entity_id: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
    publisher_id: [ "ocid1.publisher.oc1..xxxxxxEXAMPLExxxxxx" ]
    package_type: [ "STACK" ]
    pricing: [ "FREE" ]
    is_featured: true
    sort_order: ASC

"""

RETURN = """
applications:
    description:
        - List of Application resources
    returned: on success
    type: complex
    contains:
        entity_id:
            description:
                - Identifier of the application from a service catalog.
            returned: on success
            type: str
            sample: "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx"
        entity_type:
            description:
                - The type of an application in the service catalog.
            returned: on success
            type: str
            sample: entity_type_example
        display_name:
            description:
                - The name that service catalog should use to display this application.
            returned: on success
            type: str
            sample: display_name_example
        is_featured:
            description:
                - Indicates whether the application is featured.
            returned: on success
            type: bool
            sample: true
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
                    type: str
                    sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
                display_name:
                    description:
                        - The name of the publisher.
                    returned: on success
                    type: str
                    sample: display_name_example
        short_description:
            description:
                - A short description of the application.
            returned: on success
            type: str
            sample: short_description_example
        logo:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                display_name:
                    description:
                        - The name used to refer to the uploaded data.
                    returned: on success
                    type: str
                    sample: display_name_example
                content_url:
                    description:
                        - The content URL of the uploaded data.
                    returned: on success
                    type: str
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the uploaded data.
                    returned: on success
                    type: str
                    sample: mime_type_example
        pricing_type:
            description:
                - Summary of the pricing types available across all packages in the application.
            returned: on success
            type: str
            sample: FREE
        package_type:
            description:
                - The type of the packages withing the application.
            returned: on success
            type: str
            sample: STACK
    sample: [{
        "entity_id": "ocid1.entity.oc1..xxxxxxEXAMPLExxxxxx",
        "entity_type": "entity_type_example",
        "display_name": "display_name_example",
        "is_featured": true,
        "publisher": {
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        },
        "short_description": "short_description_example",
        "logo": {
            "display_name": "display_name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example"
        },
        "pricing_type": "FREE",
        "package_type": "STACK"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.service_catalog import ServiceCatalogClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ApplicationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "service_catalog_id",
            "entity_type",
            "display_name",
            "entity_id",
            "publisher_id",
            "package_type",
            "pricing",
            "is_featured",
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_applications, **optional_kwargs
        )


ApplicationFactsHelperCustom = get_custom_class("ApplicationFactsHelperCustom")


class ResourceFactsHelper(ApplicationFactsHelperCustom, ApplicationFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            service_catalog_id=dict(type="str"),
            entity_type=dict(type="str"),
            display_name=dict(aliases=["name"], type="str"),
            entity_id=dict(type="str"),
            publisher_id=dict(type="list", elements="str"),
            package_type=dict(type="list", elements="str", choices=["STACK"]),
            pricing=dict(
                type="list", elements="str", choices=["FREE", "BYOL", "PAYGO"]
            ),
            is_featured=dict(type="bool"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="application",
        service_client_class=ServiceCatalogClient,
        namespace="service_catalog",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(applications=result)


if __name__ == "__main__":
    main()
