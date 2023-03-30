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
module: oci_functions_pbf_listing_facts
short_description: Fetches details about one or multiple PbfListing resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PbfListing resources in Oracle Cloud Infrastructure
    - Fetches a wrapped list of all Pre-built Function(PBF) Listings. Returns a PbfListingCollection containing
      an array of PbfListingSummary response models.
    - If I(pbf_listing_id) is specified, the details of a single PbfListing will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    pbf_listing_id:
        description:
            - unique PbfListing identifier
            - Required to get a specific pbf_listing.
        type: str
        aliases: ["id"]
    name:
        description:
            - A filter to return only resources that match the entire PBF name given.
        type: str
    name_contains:
        description:
            - A filter to return only resources that contain the supplied filter text in the PBF name given.
        type: str
    name_starts_with:
        description:
            - A filter to return only resources that start with the supplied filter text in the PBF name given.
        type: str
    trigger:
        description:
            - A filter to return only resources that match the service trigger sources of a PBF.
        type: list
        elements: str
    lifecycle_state:
        description:
            - A filter to return only resources their lifecycleState matches the given lifecycleState.
        type: str
        choices:
            - "ACTIVE"
            - "INACTIVE"
            - "DELETED"
    sort_order:
        description:
            - Specifies sort order.
            - "* **ASC:** Ascending sort order.
              * **DESC:** Descending sort order."
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for name is ascending.
        type: str
        choices:
            - "timeCreated"
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific pbf_listing
  oci_functions_pbf_listing_facts:
    # required
    pbf_listing_id: "ocid1.pbflisting.oc1..xxxxxxEXAMPLExxxxxx"

- name: List pbf_listings
  oci_functions_pbf_listing_facts:

    # optional
    pbf_listing_id: "ocid1.pbflisting.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    name_contains: name_contains_example
    name_starts_with: name_starts_with_example
    trigger: [ "trigger_example" ]
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
pbf_listings:
    description:
        - List of PbfListing resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - A brief descriptive name for the PBF listing. The PBF listing name must be unique, and not match and existing
                  PBF.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - "A short overview of the PBF Listing: the purpose of the PBF and and associated information."
            returned: on success
            type: str
            sample: description_example
        publisher_details:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - Name of the Publisher
                    returned: on success
                    type: str
                    sample: name_example
        triggers:
            description:
                - An array of Trigger. A list of triggers that may activate the PBF.
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - A brief descriptive name for the PBF trigger.
                    returned: on success
                    type: str
                    sample: name_example
        time_created:
            description:
                - The time the PbfListing was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The last time the PbfListing was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the PBF resource.
            returned: on success
            type: str
            sample: ACTIVE
        freeform_tags:
            description:
                - "Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
                  Example: `{\\"bar-key\\": \\"value\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"foo-namespace\\": {\\"bar-key\\": \\"value\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "publisher_details": {
            "name": "name_example"
        },
        "triggers": [{
            "name": "name_example"
        }],
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "ACTIVE",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.functions import FunctionsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PbfListingFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "pbf_listing_id",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pbf_listing,
            pbf_listing_id=self.module.params.get("pbf_listing_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "pbf_listing_id",
            "name",
            "name_contains",
            "name_starts_with",
            "trigger",
            "lifecycle_state",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_pbf_listings, **optional_kwargs
        )


PbfListingFactsHelperCustom = get_custom_class("PbfListingFactsHelperCustom")


class ResourceFactsHelper(PbfListingFactsHelperCustom, PbfListingFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            pbf_listing_id=dict(aliases=["id"], type="str"),
            name=dict(type="str"),
            name_contains=dict(type="str"),
            name_starts_with=dict(type="str"),
            trigger=dict(type="list", elements="str"),
            lifecycle_state=dict(type="str", choices=["ACTIVE", "INACTIVE", "DELETED"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="pbf_listing",
        service_client_class=FunctionsManagementClient,
        namespace="functions",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(pbf_listings=result)


if __name__ == "__main__":
    main()
