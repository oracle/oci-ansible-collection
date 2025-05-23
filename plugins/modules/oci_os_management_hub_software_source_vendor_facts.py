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
module: oci_os_management_hub_software_source_vendor_facts
short_description: Fetches details about one or multiple SoftwareSourceVendor resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SoftwareSourceVendor resources in Oracle Cloud Infrastructure
    - Lists available software source vendors. Filter the list against a variety of criteria including but not limited
      to its name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This parameter is required and returns
              only resources contained within the specified compartment.
        type: str
        required: true
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort software source vendors by. Only one sort order may be provided. Default order for name is ascending.
        type: str
        choices:
            - "name"
    name:
        description:
            - The name of the entity to be queried.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List software_source_vendors
  oci_os_management_hub_software_source_vendor_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    sort_order: ASC
    sort_by: name
    name: name_example

"""

RETURN = """
software_source_vendors:
    description:
        - List of SoftwareSourceVendor resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Name of the vendor providing the software source.
            returned: on success
            type: str
            sample: ORACLE
        os_families:
            description:
                - List of corresponding operating system families.
            returned: on success
            type: list
            sample: []
        arch_types:
            description:
                - List of corresponding architecture types.
            returned: on success
            type: list
            sample: []
    sample: [{
        "name": "ORACLE",
        "os_families": [],
        "arch_types": []
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import SoftwareSourceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubSoftwareSourceVendorFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_order",
            "sort_by",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_software_source_vendors,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OsManagementHubSoftwareSourceVendorFactsHelperCustom = get_custom_class(
    "OsManagementHubSoftwareSourceVendorFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubSoftwareSourceVendorFactsHelperCustom,
    OsManagementHubSoftwareSourceVendorFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="software_source_vendor",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(software_source_vendors=result)


if __name__ == "__main__":
    main()
