#!/usr/bin/python
# Copyright (c) 2020, 2021 Oracle and/or its affiliates.
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
module: oci_healthchecks_health_checks_vantage_point_facts
short_description: Fetches details about one or multiple HealthChecksVantagePoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple HealthChecksVantagePoint resources in Oracle Cloud Infrastructure
    - Gets information about all vantage points available to the user.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    sort_by:
        description:
            - The field to sort by when listing vantage points.
        type: str
        choices:
            - "name"
            - "displayName"
    sort_order:
        description:
            - Controls the sort order of results.
        type: str
        choices:
            - "ASC"
            - "DESC"
    name:
        description:
            - Filters results that exactly match the `name` field.
        type: str
    display_name:
        description:
            - Filters results that exactly match the `displayName` field.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List health_checks_vantage_points
  oci_healthchecks_health_checks_vantage_point_facts:

"""

RETURN = """
health_checks_vantage_points:
    description:
        - List of HealthChecksVantagePoint resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - The display name for the vantage point. Display names are determined by
                  the best information available and may change over time.
            returned: on success
            type: str
            sample: display_name_example
        provider_name:
            description:
                - The organization on whose infrastructure this vantage point resides.
                  Provider names are not unique, as Oracle Cloud Infrastructure maintains
                  many vantage points in each major provider.
            returned: on success
            type: str
            sample: provider_name_example
        name:
            description:
                - The unique, permanent name for the vantage point.
            returned: on success
            type: str
            sample: name_example
        geo:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                geo_key:
                    description:
                        - An opaque identifier for the geographic location of the vantage point.
                    returned: on success
                    type: str
                    sample: geo_key_example
                admin_div_code:
                    description:
                        - The ISO 3166-2 code for this location's first-level administrative
                          division, either a US state or Canadian province. Only included for locations
                          in the US or Canada. For a list of codes, see
                          L(Country Codes,https://www.iso.org/obp/ui/#search).
                    returned: on success
                    type: str
                    sample: admin_div_code_example
                city_name:
                    description:
                        - Common English-language name for the city.
                    returned: on success
                    type: str
                    sample: city_name_example
                country_code:
                    description:
                        - The ISO 3166-1 alpha-2 country code. For a list of codes,
                          see L(Country Codes,https://www.iso.org/obp/ui/#search).
                    returned: on success
                    type: str
                    sample: country_code_example
                country_name:
                    description:
                        - The common English-language name for the country.
                    returned: on success
                    type: str
                    sample: country_name_example
                latitude:
                    description:
                        - Degrees north of the Equator.
                    returned: on success
                    type: float
                    sample: 3.4
                longitude:
                    description:
                        - Degrees east of the prime meridian.
                    returned: on success
                    type: float
                    sample: 3.4
        routing:
            description:
                - An array of objects that describe how traffic to this vantage point is
                  routed, including which prefixes and ASNs connect it to the internet.
                - The addresses are sorted from the most-specific to least-specific
                  prefix (the smallest network to largest network). When a prefix has
                  multiple origin ASNs (MOAS routing), they are sorted by weight
                  (highest to lowest). Weight is determined by the total percentage of
                  peers observing the prefix originating from an ASN. Only present if
                  `fields` includes `routing`. The field will be null if the address's
                  routing information is unknown.
            returned: on success
            type: complex
            contains:
                as_label:
                    description:
                        - The registry label for `asn`, usually the name of the organization that
                          owns the ASN. May be omitted or null.
                    returned: on success
                    type: str
                    sample: as_label_example
                asn:
                    description:
                        - The Autonomous System Number (ASN) identifying the organization
                          responsible for routing packets to `prefix`.
                    returned: on success
                    type: int
                    sample: 56
                prefix:
                    description:
                        - An IP prefix (CIDR syntax) that is less specific than
                          `address`, through which `address` is routed.
                    returned: on success
                    type: str
                    sample: prefix_example
                weight:
                    description:
                        - An integer between 0 and 100 used to select between multiple
                          origin ASNs when routing to `prefix`. Most prefixes have
                          exactly one origin ASN, in which case `weight` will be 100.
                    returned: on success
                    type: int
                    sample: 56
    sample: [{
        "display_name": "display_name_example",
        "provider_name": "provider_name_example",
        "name": "name_example",
        "geo": {
            "geo_key": "geo_key_example",
            "admin_div_code": "admin_div_code_example",
            "city_name": "city_name_example",
            "country_code": "country_code_example",
            "country_name": "country_name_example",
            "latitude": 3.4,
            "longitude": 3.4
        },
        "routing": [{
            "as_label": "as_label_example",
            "asn": 56,
            "prefix": "prefix_example",
            "weight": 56
        }]
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.healthchecks import HealthChecksClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class HealthChecksVantagePointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return []

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
            "display_name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_health_checks_vantage_points, **optional_kwargs
        )


HealthChecksVantagePointFactsHelperCustom = get_custom_class(
    "HealthChecksVantagePointFactsHelperCustom"
)


class ResourceFactsHelper(
    HealthChecksVantagePointFactsHelperCustom, HealthChecksVantagePointFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            sort_by=dict(type="str", choices=["name", "displayName"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
            display_name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="health_checks_vantage_point",
        service_client_class=HealthChecksClient,
        namespace="healthchecks",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(health_checks_vantage_points=result)


if __name__ == "__main__":
    main()
