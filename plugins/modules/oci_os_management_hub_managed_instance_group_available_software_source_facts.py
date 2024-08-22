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
module: oci_os_management_hub_managed_instance_group_available_software_source_facts
short_description: Fetches details about one or multiple ManagedInstanceGroupAvailableSoftwareSource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedInstanceGroupAvailableSoftwareSource resources in Oracle Cloud Infrastructure
    - Lists available software sources for a specified managed instance group. Filter the list against a variety of criteria including but not limited to the
      software source name. The results list only software sources that have not already been added to the group.
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
        aliases: ["name"]
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
            - The field to sort by. Only one sort order may be provided. Default order for timeCreated is descending. Default order for displayName is
              ascending.
        type: str
        choices:
            - "timeCreated"
            - "displayName"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List managed_instance_group_available_software_sources
  oci_os_management_hub_managed_instance_group_available_software_source_facts:
    # required
    managed_instance_group_id: "ocid1.managedinstancegroup.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: [ "display_name_example" ]
    display_name_contains: display_name_contains_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: timeCreated

"""

RETURN = """
managed_instance_group_available_software_sources:
    description:
        - List of ManagedInstanceGroupAvailableSoftwareSource resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the software source.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User-friendly name for the software source.
            returned: on success
            type: str
            sample: display_name_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example"
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


class ManagedInstanceGroupAvailableSoftwareSourceFactsHelperGen(
    OCIResourceFactsHelperBase
):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_group_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
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
            self.client.list_managed_instance_group_available_software_sources,
            managed_instance_group_id=self.module.params.get(
                "managed_instance_group_id"
            ),
            **optional_kwargs
        )


ManagedInstanceGroupAvailableSoftwareSourceFactsHelperCustom = get_custom_class(
    "ManagedInstanceGroupAvailableSoftwareSourceFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagedInstanceGroupAvailableSoftwareSourceFactsHelperCustom,
    ManagedInstanceGroupAvailableSoftwareSourceFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_group_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="list", elements="str"),
            display_name_contains=dict(type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["timeCreated", "displayName"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance_group_available_software_source",
        service_client_class=ManagedInstanceGroupClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instance_group_available_software_sources=result)


if __name__ == "__main__":
    main()
