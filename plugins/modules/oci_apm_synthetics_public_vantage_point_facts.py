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
module: oci_apm_synthetics_public_vantage_point_facts
short_description: Fetches details about one or multiple PublicVantagePoint resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PublicVantagePoint resources in Oracle Cloud Infrastructure
    - Returns a list of public vantage points.
version_added: "2.9"
author: Oracle (@oracle)
options:
    apm_domain_id:
        description:
            - The APM domain ID the request is intended for.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). Default sort order is ascending.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. You can provide one sort by (`sortBy`). Default order for displayName or name is ascending. The displayName or name
              sort by is case insensitive.
        type: str
        choices:
            - "name"
            - "displayName"
    display_name:
        description:
            - A filter to return only resources that match the entire display name given.
        type: str
    name:
        description:
            - A filter to return only resources that match the entire name given.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List public_vantage_points
  oci_apm_synthetics_public_vantage_point_facts:
    apm_domain_id: "ocid1.apmdomain.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
public_vantage_points:
    description:
        - List of PublicVantagePoint resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Unique name that can be edited. The name should not contain any confidential information.
            returned: on success
            type: string
            sample: exampleName
        name:
            description:
                - Unique permanent name of the vantage point.
            returned: on success
            type: string
            sample: ap-seol
        geo:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                admin_div_code:
                    description:
                        - The ISO 3166-2 code for this location's first-level administrative division, either a US state or Canadian province.
                          Only included for locations in the US or Canada. For a list of codes, see Country Codes.
                    returned: on success
                    type: string
                    sample: kr
                city_name:
                    description:
                        - Common English-language name for the city.
                    returned: on success
                    type: string
                    sample: seoul
                country_code:
                    description:
                        - The ISO 3166-1 alpha-2 country code. For a list of codes, see Country Codes.
                    returned: on success
                    type: string
                    sample: kr
                country_name:
                    description:
                        - The common English-language name for the country.
                    returned: on success
                    type: string
                    sample: South Korea
                latitude:
                    description:
                        - Degrees north of the Equator.
                    returned: on success
                    type: float
                    sample: 37.5665
                longitude:
                    description:
                        - Degrees east of the prime meridian.
                    returned: on success
                    type: float
                    sample: 126.978
    sample: [{
        "display_name": "exampleName",
        "name": "ap-seol",
        "geo": {
            "admin_div_code": "kr",
            "city_name": "seoul",
            "country_code": "kr",
            "country_name": "South Korea",
            "latitude": 37.5665,
            "longitude": 126.978
        }
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.apm_synthetics import ApmSyntheticClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PublicVantagePointFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "apm_domain_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "display_name",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_public_vantage_points,
            apm_domain_id=self.module.params.get("apm_domain_id"),
            **optional_kwargs
        )


PublicVantagePointFactsHelperCustom = get_custom_class(
    "PublicVantagePointFactsHelperCustom"
)


class ResourceFactsHelper(
    PublicVantagePointFactsHelperCustom, PublicVantagePointFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            apm_domain_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name", "displayName"]),
            display_name=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="public_vantage_point",
        service_client_class=ApmSyntheticClient,
        namespace="apm_synthetics",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(public_vantage_points=result)


if __name__ == "__main__":
    main()
