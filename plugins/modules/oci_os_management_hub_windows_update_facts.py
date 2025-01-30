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
module: oci_os_management_hub_windows_update_facts
short_description: Fetches details about one or multiple WindowsUpdate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple WindowsUpdate resources in Oracle Cloud Infrastructure
    - Lists Windows updates that have been reported to the service.
    - If I(windows_update_id) is specified, the details of a single WindowsUpdate will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    windows_update_id:
        description:
            - "The unique identifier for the Windows update. Note that this is not an OCID, but is a unique identifier assigned by Microsoft.
              Example: '6981d463-cd91-4a26-b7c4-ea4ded9183ed'"
            - Required to get a specific windows_update.
        type: str
        aliases: ["id"]
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment. This parameter is required and returns
              only resources contained within the specified compartment.
            - Required to list multiple windows_updates.
        type: str
    classification_type:
        description:
            - A filter to return only packages that match the given update classification type.
        type: list
        elements: str
        choices:
            - "SECURITY"
            - "BUGFIX"
            - "ENHANCEMENT"
            - "OTHER"
    name:
        description:
            - "A filter based on the unique identifier for the Windows update. Note that this is not an OCID, but is a unique identifier assigned by Microsoft.
              Example: '6981d463-cd91-4a26-b7c4-ea4ded9183ed'"
        type: list
        elements: str
    display_name_contains:
        description:
            - A filter to return resources that may partially match the given display name.
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
- name: Get a specific windows_update
  oci_os_management_hub_windows_update_facts:
    # required
    windows_update_id: "ocid1.windowsupdate.oc1..xxxxxxEXAMPLExxxxxx"

- name: List windows_updates
  oci_os_management_hub_windows_update_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    classification_type: [ "SECURITY" ]
    name: [ "name_example" ]
    display_name_contains: display_name_contains_example
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
windows_updates:
    description:
        - List of WindowsUpdate resources
    returned: on success
    type: complex
    contains:
        description:
            description:
                - Description of the update.
                - Returned for get operation
            returned: on success
            type: str
            sample: description_example
        size_in_bytes:
            description:
                - size of the package in bytes
                - Returned for get operation
            returned: on success
            type: int
            sample: 56
        installation_requirements:
            description:
                - List of requirements for installing the update on the managed instance.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
        kb_article_ids:
            description:
                - List of the Microsoft Knowledge Base Article Ids related to this Windows Update.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
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
        installable:
            description:
                - Indicates whether the update can be installed using the service.
            returned: on success
            type: str
            sample: INSTALLABLE
        is_reboot_required_for_installation:
            description:
                - Indicates whether a reboot is required to complete the installation of this update.
            returned: on success
            type: bool
            sample: true
    sample: [{
        "description": "description_example",
        "size_in_bytes": 56,
        "installation_requirements": [],
        "kb_article_ids": [],
        "name": "name_example",
        "update_id": "ocid1.update.oc1..xxxxxxEXAMPLExxxxxx",
        "update_type": "SECURITY",
        "installable": "INSTALLABLE",
        "is_reboot_required_for_installation": true
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


class OsManagementHubWindowsUpdateFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "windows_update_id",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_windows_update,
            windows_update_id=self.module.params.get("windows_update_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "classification_type",
            "name",
            "display_name_contains",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_windows_updates,
            compartment_id=self.module.params.get("compartment_id"),
            **optional_kwargs
        )


OsManagementHubWindowsUpdateFactsHelperCustom = get_custom_class(
    "OsManagementHubWindowsUpdateFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubWindowsUpdateFactsHelperCustom,
    OsManagementHubWindowsUpdateFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            windows_update_id=dict(aliases=["id"], type="str"),
            compartment_id=dict(type="str"),
            classification_type=dict(
                type="list",
                elements="str",
                choices=["SECURITY", "BUGFIX", "ENHANCEMENT", "OTHER"],
            ),
            name=dict(type="list", elements="str"),
            display_name_contains=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "name", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="windows_update",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
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
