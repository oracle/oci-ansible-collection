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
module: oci_os_management_available_windows_update_facts
short_description: Fetches details about one or multiple AvailableWindowsUpdate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AvailableWindowsUpdate resources in Oracle Cloud Infrastructure
    - Returns a list of available Windows updates for a Managed Instance. This is only applicable to Windows instances.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - OCID for the managed instance
        type: str
        required: true
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
        type: str
    compartment_id:
        description:
            - The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
        type: str
    sort_order:
        description:
            - The sort order to use, either 'asc' or 'desc'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for TIMECREATED is descending. Default order for DISPLAYNAME is
              ascending. If no value is specified TIMECREATED is default.
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    is_eligible_for_installation:
        description:
            - Indicator of whether the update can be installed using OSMS.
        type: str
        choices:
            - "INSTALLABLE"
            - "NOT_INSTALLABLE"
            - "UNKNOWN"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List available_windows_updates
  oci_os_management_available_windows_update_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: My new resource
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: TIMECREATED
    is_eligible_for_installation: INSTALLABLE

"""

RETURN = """
available_windows_updates:
    description:
        - List of AvailableWindowsUpdate resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Windows Update name
            returned: on success
            type: str
            sample: display_name_example
        name:
            description:
                - "Unique identifier for the Windows update. NOTE - This is not an OCID,
                  but is a unique identifier assigned by Microsoft.
                  Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`"
            returned: on success
            type: str
            sample: 6981d463-cd91-4a26-b7c4-ea4ded9183ed
        update_type:
            description:
                - The purpose of this update.
            returned: on success
            type: str
            sample: SECURITY
        is_eligible_for_installation:
            description:
                - Indicates whether the update can be installed using OSMS.
            returned: on success
            type: str
            sample: INSTALLABLE
        is_reboot_required_for_installation:
            description:
                - Indicates whether a reboot may be required to complete installation of this update.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "display_name": "display_name_example",
        "name": "6981d463-cd91-4a26-b7c4-ea4ded9183ed",
        "update_type": "SECURITY",
        "is_eligible_for_installation": "INSTALLABLE",
        "is_reboot_required_for_installation": true
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AvailableWindowsUpdateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "display_name",
            "compartment_id",
            "sort_order",
            "sort_by",
            "is_eligible_for_installation",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_available_windows_updates_for_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


AvailableWindowsUpdateFactsHelperCustom = get_custom_class(
    "AvailableWindowsUpdateFactsHelperCustom"
)


class ResourceFactsHelper(
    AvailableWindowsUpdateFactsHelperCustom, AvailableWindowsUpdateFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            display_name=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            is_eligible_for_installation=dict(
                type="str", choices=["INSTALLABLE", "NOT_INSTALLABLE", "UNKNOWN"]
            ),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="available_windows_update",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(available_windows_updates=result)


if __name__ == "__main__":
    main()
