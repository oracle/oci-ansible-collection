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
module: oci_os_management_hub_search_software_source_package_groups_facts
short_description: Fetches details about one or multiple SearchSoftwareSourcePackageGroups resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple SearchSoftwareSourcePackageGroups resources in Oracle Cloud Infrastructure
    - Searches the package groups from the specified list of software sources. Filter the list against a variety of criteria
      including but not limited to its name, and group type.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    software_source_ids:
        description:
            - List of software source L(OCIDs,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm).
        type: list
        elements: str
        required: true
    sort_order:
        description:
            - The sort order.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by.
        type: str
        choices:
            - "NAME"
    name_contains:
        description:
            - A filter that returns package groups with a name that contains the given string.
        type: str
    group_type:
        description:
            - Indicates if this is a group, category or environment.
        type: str
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List search_software_source_package_groups
  oci_os_management_hub_search_software_source_package_groups_facts:
    # required
    software_source_ids: [ "software_source_ids_example" ]

    # optional
    sort_order: ASC
    sort_by: NAME
    name_contains: name_contains_example
    group_type: group_type_example

"""

RETURN = """
search_software_source_package_groups:
    description:
        - List of SearchSoftwareSourcePackageGroups resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - Package group identifier.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        name:
            description:
                - Package group name.
            returned: on success
            type: str
            sample: name_example
        description:
            description:
                - Description of the package group.
            returned: on success
            type: str
            sample: description_example
        is_user_visible:
            description:
                - Indicates if this package group is visible to users.
            returned: on success
            type: bool
            sample: true
        is_default:
            description:
                - Indicates if this package group is the default.
            returned: on success
            type: bool
            sample: true
        repositories:
            description:
                - The repository IDs of the package group.
            returned: on success
            type: list
            sample: []
        group_type:
            description:
                - Indicates if this is a group, category or environment.
            returned: on success
            type: str
            sample: group_type_example
        display_order:
            description:
                - Indicates the order to display category or environment.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "is_user_visible": true,
        "is_default": true,
        "repositories": [],
        "group_type": "group_type_example",
        "display_order": 56
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
    from oci.os_management_hub.models import SearchSoftwareSourcePackageGroupsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubSearchSoftwareSourcePackageGroupsFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "software_source_ids",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.search_software_source_package_groups,
            search_software_source_package_groups_details=oci_common_utils.convert_input_data_to_model_class(
                self.module.params, SearchSoftwareSourcePackageGroupsDetails
            ),
            **optional_kwargs
        )


OsManagementHubSearchSoftwareSourcePackageGroupsFactsHelperCustom = get_custom_class(
    "OsManagementHubSearchSoftwareSourcePackageGroupsFactsHelperCustom"
)


class ResourceFactsHelper(
    OsManagementHubSearchSoftwareSourcePackageGroupsFactsHelperCustom,
    OsManagementHubSearchSoftwareSourcePackageGroupsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            software_source_ids=dict(type="list", elements="str", required=True),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["NAME"]),
            name_contains=dict(type="str"),
            group_type=dict(type="str"),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="search_software_source_package_groups",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(search_software_source_package_groups=result)


if __name__ == "__main__":
    main()
