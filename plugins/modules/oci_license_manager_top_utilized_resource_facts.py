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
module: oci_license_manager_top_utilized_resource_facts
short_description: Fetches details about one or multiple TopUtilizedResource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple TopUtilizedResource resources in Oracle Cloud Infrastructure
    - Retrieves the top utilized resources for a given compartment.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) used for the license record, product license,
              and configuration.
        type: str
        required: true
    is_compartment_id_in_subtree:
        description:
            - Indicates if the given compartment is the root compartment.
        type: bool
    resource_unit_type:
        description:
            - A filter to return only resources whose unit matches the given resource unit.
        type: str
        choices:
            - "OCPU"
            - "ECPU"
    sort_order:
        description:
            - The sort order to use, whether `ASC` or `DESC`.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - Specifies the attribute with which to sort the rules.
            - "Default: `totalUnits`"
            - "* **totalUnits:** Sorts by totalUnits consumed by resource."
        type: str
        choices:
            - "totalUnits"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List top_utilized_resources
  oci_license_manager_top_utilized_resource_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    is_compartment_id_in_subtree: true
    resource_unit_type: OCPU
    sort_order: ASC
    sort_by: totalUnits

"""

RETURN = """
top_utilized_resources:
    description:
        - List of TopUtilizedResource resources
    returned: on success
    type: complex
    contains:
        resource_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the resource.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        resource_name:
            description:
                - Resource canonical name.
            returned: on success
            type: str
            sample: resource_name_example
        resource_compartment_id:
            description:
                - The compartment L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) that contains the resource.
            returned: on success
            type: str
            sample: "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx"
        resource_compartment_name:
            description:
                - The display name of the compartment that contains the resource.
            returned: on success
            type: str
            sample: resource_compartment_name_example
        total_units:
            description:
                - Number of license units consumed by the resource.
            returned: on success
            type: float
            sample: 1.2
        unit_type:
            description:
                - The resource unit.
            returned: on success
            type: str
            sample: OCPU
    sample: [{
        "resource_id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_name": "resource_name_example",
        "resource_compartment_id": "ocid1.resourcecompartment.oc1..xxxxxxEXAMPLExxxxxx",
        "resource_compartment_name": "resource_compartment_name_example",
        "total_units": 1.2,
        "unit_type": "OCPU"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.license_manager import LicenseManagerClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class TopUtilizedResourceFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "is_compartment_id_in_subtree",
            "resource_unit_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_top_utilized_resources,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


TopUtilizedResourceFactsHelperCustom = get_custom_class(
    "TopUtilizedResourceFactsHelperCustom"
)


class ResourceFactsHelper(
    TopUtilizedResourceFactsHelperCustom, TopUtilizedResourceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            is_compartment_id_in_subtree=dict(type="bool"),
            resource_unit_type=dict(type="str", choices=["OCPU", "ECPU"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["totalUnits"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="top_utilized_resource",
        service_client_class=LicenseManagerClient,
        namespace="license_manager",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(top_utilized_resources=result)


if __name__ == "__main__":
    main()
