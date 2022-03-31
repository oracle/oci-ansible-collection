#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_service_catalog_facts
short_description: Fetches details about one or multiple ServiceCatalog resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ServiceCatalog resources in Oracle Cloud Infrastructure
    - Lists all the service catalogs in the given compartment.
    - If I(service_catalog_id) is specified, the details of a single ServiceCatalog will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The unique identifier for the compartment.
            - Required to list multiple service_catalogs.
        type: str
    service_catalog_id:
        description:
            - The unique identifier for the service catalog.
            - Required to get a specific service_catalog.
        type: str
        aliases: ["id"]
    sort_by:
        description:
            - Default is `TIMECREATED`
        type: str
        choices:
            - "TIMECREATED"
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
- name: Get a specific service_catalog
  oci_service_catalog_facts:
    # required
    service_catalog_id: "ocid1.servicecatalog.oc1..xxxxxxEXAMPLExxxxxx"

- name: List service_catalogs
  oci_service_catalog_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    service_catalog_id: "ocid1.servicecatalog.oc1..xxxxxxEXAMPLExxxxxx"
    sort_by: TIMECREATED
    sort_order: ASC
    display_name: display_name_example

"""

RETURN = """
service_catalogs:
    description:
        - List of ServiceCatalog resources
    returned: on success
    type: complex
    contains:
        time_updated:
            description:
                - The date and time the service catalog was last modified, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-12-10T05:10:29.721Z`"
                - Returned for get operation
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
                - Returned for get operation
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        id:
            description:
                - The unique identifier for the Service catalog.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        lifecycle_state:
            description:
                - The lifecycle state of the service catalog.
            returned: on success
            type: str
            sample: ACTIVE
        compartment_id:
            description:
                - The Compartment id where the service catalog exists
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The name of the service catalog.
            returned: on success
            type: str
            sample: display_name_example
        time_created:
            description:
                - The date and time the service catalog was created, expressed in L(RFC 3339,https://tools.ietf.org/html/rfc3339)
                  timestamp format.
                - "Example: `2021-05-26T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: [{
        "time_updated": "2013-10-20T19:20:30+01:00",
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "freeform_tags": {'Department': 'Finance'},
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "lifecycle_state": "ACTIVE",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "time_created": "2013-10-20T19:20:30+01:00"
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


class ServiceCatalogFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "service_catalog_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_service_catalog,
            service_catalog_id=self.module.params.get("service_catalog_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "service_catalog_id",
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
            self.client.list_service_catalogs,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


ServiceCatalogFactsHelperCustom = get_custom_class("ServiceCatalogFactsHelperCustom")


class ResourceFactsHelper(
    ServiceCatalogFactsHelperCustom, ServiceCatalogFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            service_catalog_id=dict(aliases=["id"], type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            display_name=dict(aliases=["name"], type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="service_catalog",
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

    module.exit_json(service_catalogs=result)


if __name__ == "__main__":
    main()
