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
module: oci_os_management_available_update_facts
short_description: Fetches details about one or multiple AvailableUpdate resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple AvailableUpdate resources in Oracle Cloud Infrastructure
    - Returns a list of available updates for a Managed Instance.
version_added: "2.9"
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
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List available_updates
  oci_os_management_available_update_facts:
    managed_instance_id: ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
available_updates:
    description:
        - List of AvailableUpdate resources
    returned: on success
    type: complex
    contains:
        display_name:
            description:
                - Package name
            returned: on success
            type: string
            sample: display_name_example
        name:
            description:
                - "Unique identifier for the package available for update. NOTE - This is not an OCID"
            returned: on success
            type: string
            sample: name_example
        update_type:
            description:
                - The purpose of this update.
            returned: on success
            type: string
            sample: SECURITY
        type:
            description:
                - Type of the package
            returned: on success
            type: string
            sample: type_example
        installed_version:
            description:
                - Version of the installed package
            returned: on success
            type: string
            sample: installed_version_example
        available_version:
            description:
                - Version of the package available for update
            returned: on success
            type: string
            sample: available_version_example
        architecture:
            description:
                - The architecture for which this package was built
            returned: on success
            type: string
            sample: architecture_example
        errata:
            description:
                - List of errata containing this update
            returned: on success
            type: complex
            contains:
                id:
                    description:
                        - unique identifier that is immutable on creation
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
                display_name:
                    description:
                        - User friendly name
                    returned: on success
                    type: string
                    sample: display_name_example
        related_cves:
            description:
                - List of CVEs applicable to this erratum
            returned: on success
            type: list
            sample: []
        software_sources:
            description:
                - list of software sources that provide the software package
            returned: on success
            type: complex
            contains:
                name:
                    description:
                        - software source name
                    returned: on success
                    type: string
                    sample: name_example
                id:
                    description:
                        - software source identifier
                    returned: on success
                    type: string
                    sample: ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx
    sample: [{
        "display_name": "display_name_example",
        "name": "name_example",
        "update_type": "SECURITY",
        "type": "type_example",
        "installed_version": "installed_version_example",
        "available_version": "available_version_example",
        "architecture": "architecture_example",
        "errata": [{
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
            "display_name": "display_name_example"
        }],
        "related_cves": [],
        "software_sources": [{
            "name": "name_example",
            "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        }]
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


class AvailableUpdateFactsHelperGen(OCIResourceFactsHelperBase):
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
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_available_updates_for_managed_instance,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


AvailableUpdateFactsHelperCustom = get_custom_class("AvailableUpdateFactsHelperCustom")


class ResourceFactsHelper(
    AvailableUpdateFactsHelperCustom, AvailableUpdateFactsHelperGen
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
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="available_update",
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

    module.exit_json(available_updates=result)


if __name__ == "__main__":
    main()
