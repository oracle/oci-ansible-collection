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
module: oci_os_management_hub_managed_instance_group_installed_package_facts
short_description: Fetches details about one or multiple ManagedInstanceGroupInstalledPackage resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedInstanceGroupInstalledPackage resources in Oracle Cloud Infrastructure
    - Lists installed packages on the specified managed instances group. Filter the list against a variety
      of criteria including but not limited to the package name.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_group_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance group.
        type: str
        required: true
    display_name:
        description:
            - A filter to return resources that match the given display names.
        type: list
        elements: str
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
        type: str
    time_install_date_start:
        description:
            - The install date after which to list all packages, in ISO 8601 format
            - "Example: 2017-07-14T02:40:00.000Z"
        type: str
    time_install_date_end:
        description:
            - A filter to return only packages that were installed on or before the date provided, in ISO 8601 format.
            - "Example: 2017-07-14T02:40:00.000Z"
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
            - The field to sort by. Only one sort order may be provided. Default order for timeInstalled is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeInstalled"
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List managed_instance_group_installed_packages
  oci_os_management_hub_managed_instance_group_installed_package_facts:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    time_install_date_start: 2013-10-20T19:20:30+01:00
    time_install_date_end: 2013-10-20T19:20:30+01:00
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeInstalled

"""

RETURN = """
managed_instance_group_installed_packages:
    description:
        - List of ManagedInstanceGroupInstalledPackage resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The name of the package that is installed on the managed instance group.
            returned: on success
            type: str
            sample: name_example
        architecture:
            description:
                - The architecture of the package that is installed on the managed instance group.
            returned: on success
            type: str
            sample: architecture_example
    sample: [{
        "name": "name_example",
        "architecture": "architecture_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management_hub import ManagedInstanceGroupClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class ManagedInstanceGroupInstalledPackageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_group_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "display_name_contains",
            "time_install_date_start",
            "time_install_date_end",
            "compartment_id",
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
            self.client.list_managed_instance_group_installed_packages,
            managed_instance_group_id=self.module.params.get(
                "managed_instance_group_id"
            ),
            **optional_kwargs
        )


ManagedInstanceGroupInstalledPackageFactsHelperCustom = get_custom_class(
    "ManagedInstanceGroupInstalledPackageFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagedInstanceGroupInstalledPackageFactsHelperCustom,
    ManagedInstanceGroupInstalledPackageFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_group_id=dict(type="str", required=True),
            display_name=dict(type="list", elements="str"),
            display_name_contains=dict(type="str"),
            time_install_date_start=dict(type="str"),
            time_install_date_end=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(
                type="str", choices=["timeInstalled", "timeCreated", "displayName"]
            ),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance_group_installed_package",
        service_client_class=ManagedInstanceGroupClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instance_group_installed_packages=result)


if __name__ == "__main__":
    main()
