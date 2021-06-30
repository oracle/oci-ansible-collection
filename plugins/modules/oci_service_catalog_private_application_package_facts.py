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
module: oci_service_catalog_private_application_package_facts
short_description: Fetches details about one or multiple PrivateApplicationPackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PrivateApplicationPackage resources in Oracle Cloud Infrastructure
    - Lists the packages in the specified private application.
    - If I(private_application_package_id) is specified, the details of a single PrivateApplicationPackage will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    private_application_package_id:
        description:
            - The unique identifier for the private application package.
            - Required to get a specific private_application_package.
        type: str
        aliases: ["id"]
    private_application_id:
        description:
            - The unique identifier for the private application.
            - Required to list multiple private_application_packages.
        type: str
    package_type:
        description:
            - Name of the package type. If multiple package types are provided, then any resource with
              one or more matching package types will be returned.
        type: list
        choices:
            - "STACK"
    sort_by:
        description:
            - The field to use to sort listed results. You can only specify one field to sort by.
              `TIMECREATED` displays results in descending order by default. You can change your
              preference by specifying a different sort order.
        type: str
        choices:
            - "TIMECREATED"
            - "VERSION"
    sort_order:
        description:
            - The sort order to apply, either `ASC` or `DESC`. Default is `ASC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    display_name:
        description:
            - Exact match name filter.
        type: str
        aliases: ["name"]
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List private_application_packages
  oci_service_catalog_private_application_package_facts:
    private_application_id: "ocid1.privateapplication.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific private_application_package
  oci_service_catalog_private_application_package_facts:
    private_application_package_id: "ocid1.privateapplicationpackage.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
private_application_packages:
    description:
        - List of PrivateApplicationPackage resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the private application package.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        private_application_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the private application where the package is hosted.
            returned: on success
            type: string
            sample: "ocid1.privateapplication.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The display name of the package.
            returned: on success
            type: string
            sample: display_name_example
        version:
            description:
                - The package version.
            returned: on success
            type: string
            sample: version_example
        package_type:
            description:
                - The specified package's type.
            returned: on success
            type: string
            sample: STACK
        time_created:
            description:
                - The date and time the private application package was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-05-27T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2021-05-27T21:10:29.600Z
        content_url:
            description:
                - The content URL of the terraform configuration.
            returned: on success
            type: string
            sample: content_url_example
        mime_type:
            description:
                - The MIME type of the terraform configuration.
            returned: on success
            type: string
            sample: mime_type_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "private_application_id": "ocid1.privateapplication.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "version": "version_example",
        "package_type": "STACK",
        "time_created": "2021-05-27T21:10:29.600Z",
        "content_url": "content_url_example",
        "mime_type": "mime_type_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.service_catalog import ServiceCatalogClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PrivateApplicationPackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "private_application_package_id",
        ]

    def get_required_params_for_list(self):
        return [
            "private_application_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_application_package,
            private_application_package_id=self.module.params.get(
                "private_application_package_id"
            ),
        )

    def list_resources(self):
        optional_list_method_params = [
            "private_application_package_id",
            "package_type",
            "sort_by",
            "sort_order",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_private_application_packages,
            private_application_id=self.module.params.get("private_application_id"),
            **optional_kwargs
        )


PrivateApplicationPackageFactsHelperCustom = get_custom_class(
    "PrivateApplicationPackageFactsHelperCustom"
)


class ResourceFactsHelper(
    PrivateApplicationPackageFactsHelperCustom, PrivateApplicationPackageFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            private_application_package_id=dict(aliases=["id"], type="str"),
            private_application_id=dict(type="str"),
            package_type=dict(type="list", choices=["STACK"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "VERSION"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="private_application_package",
        service_client_class=ServiceCatalogClient,
        namespace="service_catalog",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(private_application_packages=result)


if __name__ == "__main__":
    main()
