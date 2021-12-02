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
module: oci_compute_instance_agent_plugin_facts
short_description: Fetches details about one or multiple Plugin resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Plugin resources in Oracle Cloud Infrastructure
    - The API to get one or more plugin information.
    - If I(plugin_name) is specified, the details of a single Plugin will be returned.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    instanceagent_id:
        description:
            - The OCID of the instance.
        type: str
        required: true
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the compartment.
        type: str
        required: true
    plugin_name:
        description:
            - The name of the plugin.
            - Required to get a specific plugin.
        type: str
    status:
        description:
            - The plugin status
        type: str
        choices:
            - "RUNNING"
            - "STOPPED"
            - "NOT_SUPPORTED"
            - "INVALID"
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
- name: Get a specific plugin
  oci_compute_instance_agent_plugin_facts:
    # required
    instanceagent_id: "ocid1.instanceagent.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    plugin_name: plugin_name_example

- name: List plugins
  oci_compute_instance_agent_plugin_facts:
    # required
    instanceagent_id: "ocid1.instanceagent.oc1..xxxxxxEXAMPLExxxxxx"
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    status: RUNNING
    sort_by: TIMECREATED
    sort_order: ASC
    name: name_example

"""

RETURN = """
plugins:
    description:
        - List of Plugin resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The plugin name
            returned: on success
            type: str
            sample: name_example
        status:
            description:
                - "The plugin status Specified the plugin state on the instance * `RUNNING` - The plugin is in running state * `STOPPED` - The plugin is in
                  stopped state * `NOT_SUPPORTED` - The plugin is not supported on this platform * `INVALID` - The plugin state is not recognizable by the
                  service"
            returned: on success
            type: str
            sample: RUNNING
        time_last_updated_utc:
            description:
                - The last update time of the plugin in UTC
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        message:
            description:
                - The optional message from the agent plugin
            returned: on success
            type: str
            sample: message_example
    sample: [{
        "name": "name_example",
        "status": "RUNNING",
        "time_last_updated_utc": "2013-10-20T19:20:30+01:00",
        "message": "message_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.compute_instance_agent import PluginClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PluginFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get, list"""

    def get_required_params_for_get(self):
        return [
            "instanceagent_id",
            "compartment_id",
            "plugin_name",
        ]

    def get_required_params_for_list(self):
        return [
            "compartment_id",
            "instanceagent_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_instance_agent_plugin,
            instanceagent_id=self.module.params.get("instanceagent_id"),
            compartment_id=self.module.params.get("compartment_id"),
            plugin_name=self.module.params.get("plugin_name"),
        )

    def list_resources(self):
        optional_list_method_params = [
            "status",
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
            self.client.list_instance_agent_plugins,
            compartment_id=self.module.params.get("compartment_id"),
            instanceagent_id=self.module.params.get("instanceagent_id"),
            **optional_kwargs
        )


PluginFactsHelperCustom = get_custom_class("PluginFactsHelperCustom")


class ResourceFactsHelper(PluginFactsHelperCustom, PluginFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            instanceagent_id=dict(type="str", required=True),
            compartment_id=dict(type="str", required=True),
            plugin_name=dict(type="str"),
            status=dict(
                type="str", choices=["RUNNING", "STOPPED", "NOT_SUPPORTED", "INVALID"]
            ),
            sort_by=dict(type="str", choices=["TIMECREATED", "DISPLAYNAME"]),
            sort_order=dict(type="str", choices=["ASC", "DESC"]),
            name=dict(type="str"),
        )
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="plugin",
        service_client_class=PluginClient,
        namespace="compute_instance_agent",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(plugins=result)


if __name__ == "__main__":
    main()
