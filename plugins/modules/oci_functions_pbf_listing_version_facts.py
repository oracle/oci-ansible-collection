#!/usr/bin/python
# Copyright (c) 2020, 2024 Oracle and/or its affiliates.
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
module: oci_functions_pbf_listing_version_facts
short_description: Fetches details about one or multiple PbfListingVersion resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PbfListingVersion resources in Oracle Cloud Infrastructure
    - Fetches a wrapped list of all Pre-built Function(PBF) Listing versions. Returns a PbfListingVersionCollection
      containing an array of PbfListingVersionSummary response models.
    - Note that the PbfListingIdentifier must be provided as a query parameter, otherwise an exception shall
      be thrown.
    - If I(pbf_listing_version_id) is specified, the details of a single PbfListingVersion will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    pbf_listing_id:
        description:
            - unique PbfListing identifier
            - Required to list multiple pbf_listing_versions.
        type: str
    pbf_listing_version_id:
        description:
            - unique PbfListingVersion identifier
            - Required to get a specific pbf_listing_version.
        type: str
        aliases: ["id"]
    name:
        description:
            - Matches a PbfListingVersion based on a provided semantic version name for a PbfListingVersion.
              Each PbfListingVersion name is unique with respect to its associated PbfListing.
        type: str
    is_current_version:
        description:
            - Matches the current version (the most recently added version with an Active
              lifecycleState) associated with a PbfListing.
        type: bool
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
- name: Get a specific pbf_listing_version
  oci_functions_pbf_listing_version_facts:
    # required
    pbf_listing_version_id: "ocid1.pbflistingversion.oc1..xxxxxxEXAMPLExxxxxx"

- name: List pbf_listing_versions
  oci_functions_pbf_listing_version_facts:
    # required
    pbf_listing_id: "ocid1.pbflisting.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    pbf_listing_version_id: "ocid1.pbflistingversion.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    is_current_version: true
    lifecycle_state: ACTIVE
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
pbf_listing_versions:
    description:
        - List of PbfListingVersion resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        pbf_listing_id:
            description:
                - The OCID of the PbfListing this resource version belongs to.
            returned: on success
            type: str
            sample: "ocid1.pbflisting.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Semantic version
            returned: on success
            type: str
            sample: name_example
        config:
            description:
                - Details about the required and optional Function configurations needed for proper performance of the PBF.
            returned: on success
            type: complex
            contains:
                key:
                    description:
                        - The key name of the config param.
                    returned: on success
                    type: str
                    sample: key_example
                description:
                    description:
                        - Details about why this config is required and what it will be used for.
                    returned: on success
                    type: str
                    sample: description_example
                is_optional:
                    description:
                        - Is this a required config or an optional one. Requests with required config params missing will be rejected.
                    returned: on success
                    type: bool
                    sample: true
        requirements:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                min_memory_required_in_mbs:
                    description:
                        - Minimum memory required by this PBF. The user should use memory greater than or equal to
                          this value while configuring the Function.
                    returned: on success
                    type: int
                    sample: 56
                policies:
                    description:
                        - List of policies required for this PBF execution.
                    returned: on success
                    type: complex
                    contains:
                        policy:
                            description:
                                - Policy required for PBF execution
                            returned: on success
                            type: str
                            sample: policy_example
                        description:
                            description:
                                - Details about why this policy is required and what it will be used for.
                            returned: on success
                            type: str
                            sample: description_example
        change_summary:
            description:
                - Details changes are included in this version.
            returned: on success
            type: str
            sample: change_summary_example
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
                - The time the PbfListingVersion was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The last time the PbfListingVersion was updated. An RFC3339 formatted datetime string.
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
        "pbf_listing_id": "ocid1.pbflisting.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "config": [{
            "key": "key_example",
            "description": "description_example",
            "is_optional": true
        }],
        "requirements": {
            "min_memory_required_in_mbs": 56,
            "policies": [{
                "policy": "policy_example",
                "description": "description_example"
            }]
        },
        "change_summary": "change_summary_example",
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


class PbfListingVersionFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "pbf_listing_version_id",
        ]

    def get_required_params_for_list(self):
        return [
            "pbf_listing_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_pbf_listing_version,
            pbf_listing_version_id=self.module.params.get("pbf_listing_version_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "pbf_listing_version_id",
            "name",
            "is_current_version",
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
            self.client.list_pbf_listing_versions,
            pbf_listing_id=self.module.params.get("pbf_listing_id"),
            **optional_kwargs
        )


PbfListingVersionFactsHelperCustom = get_custom_class(
    "PbfListingVersionFactsHelperCustom"
)


class ResourceFactsHelper(
    PbfListingVersionFactsHelperCustom, PbfListingVersionFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            pbf_listing_id=dict(type="str"),
            pbf_listing_version_id=dict(aliases=["id"], type="str"),
            name=dict(type="str"),
            is_current_version=dict(type="bool"),
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
        resource_type="pbf_listing_version",
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

    module.exit_json(pbf_listing_versions=result)


if __name__ == "__main__":
    main()
