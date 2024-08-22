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
module: oci_os_management_hub_package_group_facts
short_description: Fetches details about one or multiple PackageGroup resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple PackageGroup resources in Oracle Cloud Infrastructure
    - Lists package groups that are associated with the specified software source
      L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm). Filter the list against a
      variety of criteria including but not limited to its name, and package group type.
    - If I(package_group_id) is specified, the details of a single PackageGroup will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    package_group_id:
        description:
            - The unique package group identifier.
            - Required to get a specific package_group.
        type: str
        aliases: ["id"]
    software_source_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    name:
        description:
            - The name of the entity to be queried.
        type: str
    name_contains:
        description:
            - A filter to return resources that may partially match the name given.
        type: str
    group_type:
        description:
            - A filter to return only package groups of the specified type.
        type: list
        elements: str
    sort_order:
        description:
            - The sort order to use, either 'ASC' or 'DESC'.
        type: str
        choices:
            - "ASC"
            - "DESC"
    sort_by:
        description:
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific package_group
  oci_os_management_hub_package_group_facts:
    # required
    package_group_id: "ocid1.packagegroup.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

- name: List package_groups
  oci_os_management_hub_package_group_facts:
    # required
    software_source_id: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    name_contains: name_contains_example
    group_type: [ "group_type_example" ]
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
package_groups:
    description:
        - List of PackageGroup resources
    returned: on success
    type: complex
    contains:
        packages:
            description:
                - The list of packages in the package group.
                - Returned for get operation
            returned: on success
            type: list
            sample: []
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
                - The repository IDs of the package group's repositories.
            returned: on success
            type: list
            sample: []
        group_type:
            description:
                - Indicates if this is a group, category, or environment.
            returned: on success
            type: str
            sample: GROUP
        display_order:
            description:
                - Indicates the order to display category or environment.
            returned: on success
            type: int
            sample: 56
    sample: [{
        "packages": [],
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "name": "name_example",
        "description": "description_example",
        "is_user_visible": true,
        "is_default": true,
        "repositories": [],
        "group_type": "GROUP",
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

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PackageGroupFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "software_source_id",
            "package_group_id",
        ]

    def get_required_params_for_list(self):
        return [
            "software_source_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_package_group,
            software_source_id=self.module.params.get("software_source_id"),
            package_group_id=self.module.params.get("package_group_id"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
            "name_contains",
            "group_type",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_package_groups,
            software_source_id=self.module.params.get("software_source_id"),
            **optional_kwargs
        )


PackageGroupFactsHelperCustom = get_custom_class("PackageGroupFactsHelperCustom")


class ResourceFactsHelper(PackageGroupFactsHelperCustom, PackageGroupFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            package_group_id=dict(aliases=["id"], type="str"),
            software_source_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            name_contains=dict(type="str"),
            group_type=dict(type="list", elements="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="package_group",
        service_client_class=SoftwareSourceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(package_groups=result)


if __name__ == "__main__":
    main()
