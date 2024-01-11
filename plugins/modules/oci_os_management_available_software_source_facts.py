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
module: oci_os_management_available_software_source_facts
short_description: Fetches details about one or multiple AvailableSoftwareSource resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AvailableSoftwareSource resources in Oracle Cloud Infrastructure
    - Returns a list of available software sources for a Managed Instance.
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
        aliases: ["name"]
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
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List available_software_sources
  oci_os_management_available_software_source_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    display_name: display_name_example
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    sort_order: ASC
    sort_by: TIMECREATED

"""

RETURN = """
available_software_sources:
    description:
        - List of AvailableSoftwareSource resources
    returned: on success
    type: complex
    contains:
        id:
            description:
                - unique identifier that is immutable on creation
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - OCID for the Compartment
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - User friendly name for the software source
            returned: on success
            type: str
            sample: display_name_example
        parent_id:
            description:
                - OCID for the parent software source, if there is one
            returned: on success
            type: str
            sample: "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx"
        parent_name:
            description:
                - Display name of the parent software source, if there is one
            returned: on success
            type: str
            sample: parent_name_example
    sample: [{
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "parent_id": "ocid1.parent.oc1..xxxxxxEXAMPLExxxxxx",
        "parent_name": "parent_name_example"
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.os_management import OsManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AvailableSoftwareSourceFactsHelperGen(OCIResourceFactsHelperBase):
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
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_available_software_sources_for_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


AvailableSoftwareSourceFactsHelperCustom = get_custom_class(
    "AvailableSoftwareSourceFactsHelperCustom"
)


class ResourceFactsHelper(
    AvailableSoftwareSourceFactsHelperCustom, AvailableSoftwareSourceFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            display_name=dict(aliases=["name"], type="str"),
            compartment_id=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="available_software_source",
        service_client_class=OsManagementClient,
        namespace="os_management",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(available_software_sources=result)


if __name__ == "__main__":
    main()
