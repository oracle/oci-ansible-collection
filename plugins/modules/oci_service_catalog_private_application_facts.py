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
module: oci_service_catalog_private_application_facts
short_description: Fetches details about one or multiple PrivateApplication resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PrivateApplication resources in Oracle Cloud Infrastructure
    - Lists all the private applications in a given compartment.
    - If I(private_application_id) is specified, the details of a single PrivateApplication will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    private_application_id:
        description:
            - The unique identifier for the private application.
            - Required to get a specific private_application.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The unique identifier for the compartment.
            - Required to list multiple private_applications.
        type: str
    sort_by:
        description:
            - The field to use to sort listed results. You can only specify one field to sort by.
              Default is `TIMECREATED`.
        type: str
        choices:
            - "TIMECREATED"
            - "LIFECYCLESTATE"
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
- name: List private_applications
  oci_service_catalog_private_application_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific private_application
  oci_service_catalog_private_application_facts:
    private_application_id: "ocid1.privateapplication.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
private_applications:
    description:
        - List of PrivateApplication resources
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The lifecycle state of the private application.
            returned: on success
            type: string
            sample: CREATING
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment where the private application resides.
            returned: on success
            type: string
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        id:
            description:
                - The unique identifier for the private application in Marketplace.
            returned: on success
            type: string
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the private application.
            returned: on success
            type: string
            sample: display_name_example
        short_description:
            description:
                - A short description of the private application.
            returned: on success
            type: string
            sample: short_description_example
        long_description:
            description:
                - A long description of the private application.
            returned: on success
            type: string
            sample: long_description_example
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
                    type: string
                    sample: display_name_example
                content_url:
                    description:
                        - The content URL of the uploaded data.
                    returned: on success
                    type: string
                    sample: content_url_example
                mime_type:
                    description:
                        - The MIME type of the uploaded data.
                    returned: on success
                    type: string
                    sample: mime_type_example
        package_type:
            description:
                - Type of packages within this private application.
            returned: on success
            type: string
            sample: STACK
        time_created:
            description:
                - The date and time the private application was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-05-26T21:10:29.600Z`"
            returned: on success
            type: string
            sample: 2021-05-26T21:10:29.600Z
        time_updated:
            description:
                - The date and time the private application was last modified, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-12-10T05:10:29.721Z`"
            returned: on success
            type: string
            sample: 2021-12-10T05:10:29.721Z
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
    sample: [{
        "lifecycle_state": "CREATING",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "short_description": "short_description_example",
        "long_description": "long_description_example",
        "logo": {
            "display_name": "display_name_example",
            "content_url": "content_url_example",
            "mime_type": "mime_type_example"
        },
        "package_type": "STACK",
        "time_created": "2021-05-26T21:10:29.600Z",
        "time_updated": "2021-12-10T05:10:29.721Z",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'}
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


class PrivateApplicationFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "private_application_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_private_application,
            private_application_id=self.module.params.get("private_application_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "private_application_id",
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
            self.client.list_private_applications,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


PrivateApplicationFactsHelperCustom = get_custom_class(
    "PrivateApplicationFactsHelperCustom"
)


class ResourceFactsHelper(
    PrivateApplicationFactsHelperCustom, PrivateApplicationFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            private_application_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "LIFECYCLESTATE"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="private_application",
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

    module.exit_json(private_applications=result)


if __name__ == "__main__":
    main()
