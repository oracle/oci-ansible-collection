#!/usr/bin/python
# Copyright (c) 2020, 2022 Oracle and/or its affiliates.
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
module: oci_cloud_bridge_plugin_facts
short_description: Fetches details about a Plugin resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a Plugin resource in Oracle Cloud Infrastructure
    - Gets a plugin by identifier.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    agent_id:
        description:
            - Unique Agent identifier path parameter.
        type: str
        required: true
    plugin_name:
        description:
            - Unique plugin identifier path parameter.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific plugin
  oci_cloud_bridge_plugin_facts:
    # required
    agent_id: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
    plugin_name: plugin_name_example

"""

RETURN = """
plugin:
    description:
        - Plugin resource
    returned: on success
    type: complex
    contains:
        name:
            description:
                - Plugin identifier, which can be renamed.
            returned: on success
            type: str
            sample: name_example
        agent_id:
            description:
                - Agent identifier.
            returned: on success
            type: str
            sample: "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx"
        plugin_version:
            description:
                - Plugin version.
            returned: on success
            type: str
            sample: plugin_version_example
        desired_state:
            description:
                - State to which the customer wants the plugin to move to.
            returned: on success
            type: str
            sample: ENABLED
        time_created:
            description:
                - The time when the Agent was created. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        time_updated:
            description:
                - The time when the Agent was updated. An RFC3339 formatted datetime string.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
        lifecycle_state:
            description:
                - The current state of the plugin.
            returned: on success
            type: str
            sample: UPDATING
        lifecycle_details:
            description:
                - A message describing the current state in more detail. For example, it can be used to provide actionable information for a resource in Failed
                  state.
            returned: on success
            type: str
            sample: lifecycle_details_example
        freeform_tags:
            description:
                - "The freeform tags associated with this resource, if any. Each tag is a simple key-value pair with no
                  predefined name, type, or namespace/scope. For more information, see L(Resource
                  Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "The defined tags associated with this resource, if any. Each key is predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "The system tags associated with this resource, if any. The system tags are set by Oracle cloud infrastructure services. Each key is
                  predefined and scoped to namespaces.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{orcl-cloud: {free-tier-retain: true}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "name": "name_example",
        "agent_id": "ocid1.agent.oc1..xxxxxxEXAMPLExxxxxx",
        "plugin_version": "plugin_version_example",
        "desired_state": "ENABLED",
        "time_created": "2013-10-20T19:20:30+01:00",
        "time_updated": "2013-10-20T19:20:30+01:00",
        "lifecycle_state": "UPDATING",
        "lifecycle_details": "lifecycle_details_example",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
"""

from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
    OCIAnsibleModule,
)

try:
    from oci.cloud_bridge import OcbAgentSvcClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class PluginFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "agent_id",
            "plugin_name",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_plugin,
            agent_id=self.module.params.get("agent_id"),
            plugin_name=self.module.params.get("plugin_name"),
        )


PluginFactsHelperCustom = get_custom_class("PluginFactsHelperCustom")


class ResourceFactsHelper(PluginFactsHelperCustom, PluginFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(
            agent_id=dict(type="str", required=True),
            plugin_name=dict(type="str", required=True),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="plugin",
        service_client_class=OcbAgentSvcClient,
        namespace="cloud_bridge",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(plugin=result)


if __name__ == "__main__":
    main()
