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
module: oci_os_management_hub_entitlement_facts
short_description: Fetches details about one or multiple Entitlement resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Entitlement resources in Oracle Cloud Infrastructure
    - Lists entitlements in the specified tenancy L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Filter the list against a
      variety of criteria including but
      not limited to its Customer Support Identifier (CSI), and vendor name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This parameter is required and returns
              only resources contained within the specified compartment.
        type: str
        required: true
    csi:
        description:
            - A filter to return entitlements that match the given CSI.
        type: str
    vendor_name:
        description:
            - A filter to return only resources that match the given vendor name.
        type: str
        choices:
            - "ORACLE"
            - "MICROSOFT"
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort entitlements by. Only one sort order may be provided.
        type: str
        choices:
            - "csi"
            - "vendorName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List entitlements
  oci_os_management_hub_entitlement_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    csi: csi_example
    vendor_name: ORACLE
    sort_order: ASC
    sort_by: csi

"""

RETURN = """
entitlements:
    description:
        - List of Entitlement resources
    returned: on success
    type: complex
    contains:
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the tenancy containing the entitlement.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        csi:
            description:
                - The Customer Support Identifier (CSI) which unlocks the software sources. The CSI is is a unique key given to a customer and it uniquely
                  identifies the entitlement.
            returned: on success
            type: str
            sample: csi_example
        vendor_name:
            description:
                - The vendor for the entitlement.
            returned: on success
            type: str
            sample: vendor_name_example
    sample: [{
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "csi": "csi_example",
        "vendor_name": "vendor_name_example"
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


class OsManagementHubEntitlementFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "csi",
            "vendor_name",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_entitlements,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OsManagementHubEntitlementFactsHelperCustom = get_custom_class(
    "OsManagementHubEntitlementFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubEntitlementFactsHelperCustom,
    OsManagementHubEntitlementFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            csi=dict(type="str"),
            vendor_name=dict(type="str", choices=["ORACLE", "MICROSOFT"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["csi", "vendorName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="entitlement",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(entitlements=result)


if __name__ == "__main__":
    main()
