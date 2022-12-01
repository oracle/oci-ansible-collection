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
module: oci_threat_intelligence_indicator_count_facts
short_description: Fetches details about one or multiple IndicatorCount resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple IndicatorCount resources in Oracle Cloud Infrastructure
    - Get the current count of each threat indicator type. Indicator counts can be sorted in ascending or descending order.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the tenancy (root compartment) that is used to filter results.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List indicator_counts
  oci_threat_intelligence_indicator_count_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC

"""

RETURN = """
indicator_counts:
    description:
        - List of IndicatorCount resources
    returned: on success
    type: complex
    contains:
        dimensions:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                compartment_id:
                    description:
                        - The compartment OCID that contains the indicator type.
                    returned: on success
                    type: str
                    sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
                type:
                    description:
                        - The indicator type that was counted.
                    returned: on success
                    type: str
                    sample: DOMAIN_NAME
        count:
            description:
                - The count of indicators in the group.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "dimensions": {
            "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
            "type": "DOMAIN_NAME"
        },
        "count": 56
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.threat_intelligence import ThreatintelClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class IndicatorCountFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_indicator_counts,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


IndicatorCountFactsHelperCustom = get_custom_class("IndicatorCountFactsHelperCustom")


class ResourceFactsHelper(
    IndicatorCountFactsHelperCustom, IndicatorCountFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="indicator_count",
        service_client_class=ThreatintelClient,
        namespace="threat_intelligence",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(indicator_counts=result)


if __name__ == "__main__":
    main()
