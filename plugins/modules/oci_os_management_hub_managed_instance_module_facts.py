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
module: oci_os_management_hub_managed_instance_module_facts
short_description: Fetches details about one or multiple ManagedInstanceModule resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple ManagedInstanceModule resources in Oracle Cloud Infrastructure
    - Retrieves a list of modules, along with streams of the modules, from a managed instance. Filters may be applied to select a subset of modules based on the
      filter criteria.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_instance_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the managed instance.
        type: str
        required: true
    compartment_id:
        description:
            - The OCID of the compartment that contains the resources to list. This filter returns only resources contained within the specified compartment.
        type: str
    name:
        description:
            - The resource name.
        type: str
    name_contains:
        description:
            - A filter to return resources that may partially match the name given.
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
            - The field to sort by. Only one sort order may be provided. Default order for name is ascending.
        type: str
        choices:
            - "name"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List managed_instance_modules
  oci_os_management_hub_managed_instance_module_facts:
    # required
    managed_instance_id: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    name: name_example
    name_contains: name_contains_example
    sort_order: ASC
    sort_by: name

"""

RETURN = """
managed_instance_modules:
    description:
        - List of ManagedInstanceModule resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The module name.
            returned: on success
            type: str
            sample: name_example
        enabled_stream:
            description:
                - The stream that is enabled in the module.
            returned: on success
            type: str
            sample: enabled_stream_example
        installed_profiles:
            description:
                - List of installed profiles in the enabled stream of the module.
            returned: on success
            type: list
            sample: []
        active_streams:
            description:
                - List of streams that are active in the module.
            returned: on success
            type: list
            sample: []
        disabled_streams:
            description:
                - List of streams that are disabled in the module.
            returned: on success
            type: list
            sample: []
        software_source_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the software source that provides this module and
                  the associated streams.
            returned: on success
            type: str
            sample: "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
    sample: [{
        "name": "name_example",
        "enabled_stream": "enabled_stream_example",
        "installed_profiles": [],
        "active_streams": [],
        "disabled_streams": [],
        "software_source_id": "ocid1.softwaresource.oc1..xxxxxxEXAMPLExxxxxx"
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


class ManagedInstanceModuleFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "managed_instance_id",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "compartment_id",
            "name",
            "name_contains",
            "sort_order",
            "sort_by",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_managed_instance_modules,
            managed_instance_id=self.module.params.get("managed_instance_id"),
            **optional_kwargs
        )


ManagedInstanceModuleFactsHelperCustom = get_custom_class(
    "ManagedInstanceModuleFactsHelperCustom"
)


class ResourceFactsHelper(
    ManagedInstanceModuleFactsHelperCustom, ManagedInstanceModuleFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            managed_instance_id=dict(type="str", required=True),
            compartment_id=dict(type="str"),
            name=dict(type="str"),
            name_contains=dict(type="str"),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            sort_by=dict(type="str", choices=["name"]),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="managed_instance_module",
        service_client_class=ManagedInstanceClient,
        namespace="os_management_hub",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(managed_instance_modules=result)


if __name__ == "__main__":
    main()
