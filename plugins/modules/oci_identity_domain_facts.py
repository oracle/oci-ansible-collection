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
module: oci_identity_domain_facts
short_description: Fetches details about one or multiple Domain resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Domain resources in Oracle Cloud Infrastructure
    - (For tenancies that support identity domains) Lists all identity domains within a tenancy.
    - If I(domain_id) is specified, the details of a single Domain will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    domain_id:
        description:
            - The OCID of the identity domain.
            - Required to get a specific domain.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The OCID of the compartment (remember that the tenancy is simply the root compartment).
            - Required to list multiple domains.
        type: str
    display_name:
        description:
            - The mutable display name of the identity domain.
        type: str
    url:
        description:
            - The region-agnostic identity domain URL.
        type: str
    home_region_url:
        description:
            - The region-specific identity domain URL.
        type: str
    type:
        description:
            - The identity domain type.
        type: str
    license_type:
        description:
            - The license type of the identity domain.
        type: str
    is_hidden_on_login:
        description:
            - Indicates whether or not the identity domain is visible at the sign-in screen.
        type: bool
    name:
        description:
            - A filter to only return resources that match the given name exactly.
        type: str
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              TIMECREATED is descending. Default order for NAME is ascending. The NAME
              sort order is case sensitive.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by Availability Domain if the scope of the resource type is within a
              single Availability Domain. If you call one of these \\"List\\" operations without specifying
              an Availability Domain, the resources are grouped by Availability Domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "NAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The NAME sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    lifecycle_state:
        description:
            - A filter to only return resources that match the given lifecycle state. The state value is case-insensitive.
        type: str
        choices:
            - "CREATING"
            - "ACTIVE"
            - "DELETING"
            - "INACTIVE"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific domain
  oci_identity_domain_facts:
    # required
    domain_id: "ocid1.domain.oc1..xxxxxxEXAMPLExxxxxx"

- name: List domains
  oci_identity_domain_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    url: url_example
    home_region_url: home_region_url_example
    type: type_example
    license_type: license_type_example
    is_hidden_on_login: true
    name: name_example
    sort_by: TIMECREATED
    sort_order: ASC
    lifecycle_state: CREATING

"""

RETURN = """
domains:
    description:
        - List of Domain resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The OCID of the identity domain.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The OCID of the compartment containing the identity domain.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - The mutable display name of the identity domain.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - The identity domain description. You can have an empty description.
            returned: on success
            type: str
            sample: description_example
        url:
            description:
                - Region-agnostic identity domain URL.
            returned: on success
            type: str
            sample: url_example
        home_region_url:
            description:
                - Region-specific identity domain URL.
            returned: on success
            type: str
            sample: home_region_url_example
        home_region:
            description:
                - The home region for the identity domain.
                  See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
                  for the full list of supported region names.
                - "Example: `us-phoenix-1`"
            returned: on success
            type: str
            sample: us-phoenix-1
        replica_regions:
            description:
                - The regions where replicas of the identity domain exist.
            returned: on success
            type: complex
            contains:
                region:
                    description:
                        - A REPLICATION_ENABLED region, e.g. us-ashburn-1.
                          See L(Regions and Availability Domains,https://docs.cloud.oracle.com/Content/General/Concepts/regions.htm)
                          for the full list of supported region names.
                    returned: on success
                    type: str
                    sample: us-phoenix-1
                url:
                    description:
                        - Region-agnostic identity domain URL.
                    returned: on success
                    type: str
                    sample: url_example
                regional_url:
                    description:
                        - Region-specific identity domain URL.
                    returned: on success
                    type: str
                    sample: regional_url_example
                state:
                    description:
                        - The IDCS-replicated region state.
                    returned: on success
                    type: str
                    sample: ENABLING_REPLICATION
        type:
            description:
                - The type of the domain.
            returned: on success
            type: str
            sample: DEFAULT
        license_type:
            description:
                - The license type of the identity domain.
            returned: on success
            type: str
            sample: license_type_example
        is_hidden_on_login:
            description:
                - Indicates whether the identity domain is hidden on the sign-in screen or not.
            returned: on success
            type: bool
            sample: true
        time_created:
            description:
                - Date and time the identity domain was created, in the format defined by RFC3339.
                - "Example: `2016-08-25T21:10:29.600Z`"
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state.
            returned: on success
            type: str
            sample: CREATING
        lifecycle_details:
            description:
                - Any additional details about the current state of the identity domain.
            returned: on success
            type: str
            sample: DEACTIVATING
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "url": "url_example",
        "home_region_url": "home_region_url_example",
        "home_region": "us-phoenix-1",
        "replica_regions": [{
            "region": "us-phoenix-1",
            "url": "url_example",
            "regional_url": "regional_url_example",
            "state": "ENABLING_REPLICATION"
        }],
        "type": "DEFAULT",
        "license_type": "license_type_example",
        "is_hidden_on_login": true,
        "time_created": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "CREATING",
        "lifecycle_details": "DEACTIVATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}}
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.identity import IdentityClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class DomainFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "domain_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_domain, domain_id=self.module.params.get("domain_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "url",
            "home_region_url",
            "type",
            "license_type",
            "is_hidden_on_login",
            "name",
            "sort_by",
            "sort_order",
            "lifecycle_state",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_domains,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


DomainFactsHelperCustom = get_custom_class("DomainFactsHelperCustom")


class ResourceFactsHelper(DomainFactsHelperCustom, DomainFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            domain_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(type="str"),
            url=dict(type="str"),
            home_region_url=dict(type="str"),
            type=dict(type="str"),
            license_type=dict(type="str"),
            is_hidden_on_login=dict(type="bool"),
            name=dict(type="str"),
            sort_by=dict(type="str", choices=["TIMECREATED", "NAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            lifecycle_state=dict(
                type="str", choices=["CREATING", "ACTIVE", "DELETING", "INACTIVE"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="domain",
        service_client_class=IdentityClient,
        namespace="identity",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(domains=result)


if __name__ == "__main__":
    main()
