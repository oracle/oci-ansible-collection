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
module: oci_compute_instance_agent_instance_agent_available_plugins_facts
short_description: Fetches details about one or multiple InstanceAgentAvailablePlugins resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple InstanceAgentAvailablePlugins resources in Oracle Cloud Infrastructure
    - The API to get the list of plugins that are available.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    os_name:
        description:
            - "The OS for which the plugin is supported.
              Examples of OperatingSystemQueryParam:OperatingSystemVersionQueryParam are as follows:
              'CentOS' '6.10' , 'CentOS Linux' '7', 'CentOS Linux' '8',
              'Oracle Linux Server' '6.10', 'Oracle Linux Server' '8.0',
              'Red Hat Enterprise Linux Server' '7.8',
              'Windows' '10', 'Windows' '2008ServerR2', 'Windows' '2012ServerR2', 'Windows' '7', 'Windows' '8.1'"
        type: str
        required: true
    os_version:
        description:
            - The OS version for which the plugin is supported.
        type: str
        required: true
    sort_by:
        description:
            - The field to sort by. You can provide one sort order (`sortOrder`). Default order for
              `TIMECREATED` is descending.
            - "**Note:** In general, some \\"List\\" operations (for example, `ListInstances`) let you
              optionally filter by availability domain if the scope of the resource type is within a
              single availability domain. If you call one of these \\"List\\" operations without specifying
              an availability domain, the resources are grouped by availability domain, then sorted."
        type: str
        choices:
            - "TIMECREATED"
            - "DISPLAYNAME"
    sort_order:
        description:
            - The sort order to use, either ascending (`ASC`) or descending (`DESC`). The `DISPLAYNAME` sort order
              is case sensitive.
        type: str
        choices:
            - "ASC"
            - "DESC"
    name:
        description:
            - The plugin name
        type: str
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: List instance_agent_available_plugins
  oci_compute_instance_agent_instance_agent_available_plugins_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    os_name: os_name_example
    os_version: os_version_example

    # optional
    sort_by: TIMECREATED
    sort_order: ASC
    name: name_example

"""

RETURN = """
instance_agent_available_plugins:
    description:
        - List of InstanceAgentAvailablePlugins resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The plugin name
            returned: on success
            type: str
            sample: name_example
        summary:
            description:
                - A brief description of the plugin functionality
            returned: on success
            type: str
            sample: summary_example
        is_supported:
            description:
                - Is the plugin supported or not
            returned: on success
            type: bool
            sample: true
        is_enabled_by_default:
            description:
                - Is the plugin enabled or disabled by default
            returned: on success
            type: bool
            sample: true
    sample: [{
        "name": "name_example",
        "summary": "summary_example",
        "is_supported": true,
        "is_enabled_by_default": true
    }]
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.compute_instance_agent import PluginconfigClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class InstanceAgentAvailablePluginsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "os_name",
            "os_version",
        ]

    def list_resources(self):
        optional_list_method_params = [
            "sort_by",
            "sort_order",
            "name",
        ]
        optional_kwargs = dict(
            (param, self.module.params[param])
            for param in optional_list_method_params
            if self.module.params.get(param) is not None
        )
        return oci_common_utils.list_all_resources(
            self.client.list_instanceagent_available_plugins,
            compartment_id=self.module.params.get("compartment_id"),
            os_name=self.module.params.get("os_name"),
            os_version=self.module.params.get("os_version"),
            **optional_kwargs
        )


InstanceAgentAvailablePluginsFactsHelperCustom = get_custom_class(
    "InstanceAgentAvailablePluginsFactsHelperCustom"
)


class ResourceFactsHelper(
    InstanceAgentAvailablePluginsFactsHelperCustom,
    InstanceAgentAvailablePluginsFactsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            compartment_id=dict(type="str", required=True),
            os_name=dict(type="str", required=True),
            os_version=dict(type="str", required=True),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="instance_agent_available_plugins",
        service_client_class=PluginconfigClient,
        namespace="compute_instance_agent",
    )

    result = []

    if resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(instance_agent_available_plugins=result)


if __name__ == "__main__":
    main()
