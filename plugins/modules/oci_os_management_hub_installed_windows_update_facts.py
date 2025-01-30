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
module: oci_os_management_hub_installed_windows_update_facts
short_description: Fetches details about one or multiple InstalledWindowsUpdate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InstalledWindowsUpdate resources in Oracle Cloud Infrastructure
    - Returns a list of Windows updates that have been installed on the specified managed instance.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
        type: str
        required: true
    name:
        description:
            - "A filter based on the unique identifier for the Windows update. Note that this is not an OCID, but is a unique identifier assigned by Microsoft.
              Example: '6981d463-cd91-4a26-b7c4-ea4ded9183ed'"
        type: list
        elements: str
    display_name:
        description:
            - A filter to return resources that match the given user-friendly name.
        type: str
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeInstalled is descending. Default order for name or displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "name"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List installed_windows_updates
  oci_os_management_hub_installed_windows_update_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    name: [ "name_example" ]
    display_name: display_name_example
    display_name_contains: display_name_contains_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
installed_windows_updates:
    description:
        - List of InstalledWindowsUpdate resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Name of the Windows update.
            returned: on success
            type: str
            sample: name_example
        update_id:
            description:
                - "Unique identifier for the Windows update. Note that this is not an OCID, but is a unique identifier assigned by Microsoft.
                  Example: '6981d463-cd91-4a26-b7c4-ea4ded9183ed'"
            returned: on success
            type: str
            sample: "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx"
        update_type:
            description:
                - The type of Windows update.
            returned: on success
            type: str
            sample: SECURITY
    sample: [{
        "name": "name_example",
        "update_id": "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx",
        "update_type": "SECURITY"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import ManagedInstanceClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubInstalledWindowsUpdateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
            "display_name",
            "display_name_contains",
            "compartment_id",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_managed_instance_installed_windows_updates,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


OsManagementHubInstalledWindowsUpdateFactsHelperCustom = get_custom_class(
    "OsManagementHubInstalledWindowsUpdateFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubInstalledWindowsUpdateFactsHelperCustom,
    OsManagementHubInstalledWindowsUpdateFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            name=dict(type="list", elements="str"),
            display_name=dict(type="str"),
            display_name_contains=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "name", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="installed_windows_update",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(installed_windows_updates=result)


if __name__ == "__main__":
    main()
