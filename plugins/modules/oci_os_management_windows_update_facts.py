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
module: oci_os_management_windows_update_facts
short_description: Fetches details about one or multiple WindowsUpdate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WindowsUpdate resources in Oracle Cloud Infrastructure
    - Returns a list of Windows Updates.
    - If I(windows_update) is specified, the details of a single WindowsUpdate will be returned.
version_added: "2.9"
author: Oracle (@oracle)
options:
    windows_update:
        description:
            - The Windows Update
            - Required to get a specific windows_update.
        type: str
    compartment_id:
        description:
            - The ID of the compartment in which to list resources. This parameter is optional and in some cases may have no effect.
        type: str
    display_name:
        description:
            - A user-friendly name. Does not have to be unique, and it's changeable.
            - "Example: `My new resource`"
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List windows_updates
  oci_os_management_windows_update_facts:
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

- name: Get a specific windows_update
  oci_os_management_windows_update_facts:
    windows_update: windows_update_example

"""

RETURN = """
windows_updates:
    description:
        - List of WindowsUpdate resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Windows Update name.
            returned: on success
            type: string
            sample: display_name_example
        name:
            description:
                - "Unique identifier for the Windows update. NOTE - This is not an OCID,
                  but is a unique identifier assigned by Microsoft.
                  Example: `6981d463-cd91-4a26-b7c4-ea4ded9183ed`"
            returned: on success
            type: string
            sample: 6981d463-cd91-4a26-b7c4-ea4ded9183ed
        description:
            description:
                - Information about the Windows Update.
            returned: on success
            type: string
            sample: description_example
        update_type:
            description:
                - The purpose of this update.
            returned: on success
            type: string
            sample: SECURITY
        size_in_bytes:
            description:
                - size of the package in bytes
            returned: on success
            type: int
            sample: 56
        is_eligible_for_installation:
            description:
                - Indicates whether the update can be installed using OSMS.
            returned: on success
            type: string
            sample: INSTALLABLE
        installation_requirements:
            description:
                - List of requirements forinstalling on a managed instances
            returned: on success
            type: list
            sample: []
        is_reboot_required_for_installation:
            description:
                - Indicates whether a reboot may be required to complete installation of this update.
            returned: on success
            type: bool
            sample: true
        kb_article_ids:
            description:
                - List of the Microsoft Knowledge Base Article Ids related to this Windows Update.
            returned: on success
            type: list
            sample: []
        installable:
            description:
                - Indicates whether the update can be installed using OSMS.
            returned: on success
            type: string
            sample: INSTALLABLE
    sample: [{
        "display_name": "display_name_example",
        "name": "6981d463-cd91-4a26-b7c4-ea4ded9183ed",
        "description": "description_example",
        "update_type": "SECURITY",
        "size_in_bytes": 56,
        "is_eligible_for_installation": "INSTALLABLE",
        "installation_requirements": [],
        "is_reboot_required_for_installation": true,
        "kb_article_ids": [],
        "installable": "INSTALLABLE"
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


class WindowsUpdateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "windows_update",
        ]

    def get_required_params_for_list(self):
        return []

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_windows_update,
            windows_update=self.module.params.get("windows_update"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "display_name",
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
            self.client.list_windows_updates, **optional_kwargs
        )


WindowsUpdateFactsHelperCustom = get_custom_class("WindowsUpdateFactsHelperCustom")


class ResourceFactsHelper(WindowsUpdateFactsHelperCustom, WindowsUpdateFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            windows_update=dict(type="str"),
            compartment_id=dict(type="str"),
            display_name=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="windows_update",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(windows_updates=result)


if __name__ == "__main__":
    main()
