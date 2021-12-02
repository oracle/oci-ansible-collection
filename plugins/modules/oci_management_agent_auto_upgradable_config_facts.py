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
module: oci_management_agent_auto_upgradable_config_facts
short_description: Fetches details about a AutoUpgradableConfig resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AutoUpgradableConfig resource in Oracle Cloud Infrastructure
    - Get the AutoUpgradable configuration for all agents in a tenancy.
      The supplied compartmentId must be a tenancy root.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The OCID of the compartment to which a request will be scoped.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific auto_upgradable_config
  oci_management_agent_auto_upgradable_config_facts:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
auto_upgradable_config:
    description:
        - AutoUpgradableConfig resource
    returned: on success
    type: complex
    contains:
        is_agent_auto_upgradable:
            description:
                - true if the agents can be upgraded automatically; false if they must be upgraded manually.
            returned: on success
            type: bool
            sample: true
    sample: {
        "is_agent_auto_upgradable": true
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.management_agent import ManagementAgentClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutoUpgradableConfigFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "compartment_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_auto_upgradable_config,
            compartment_id=self.module.params.get("compartment_id"),
        )


AutoUpgradableConfigFactsHelperCustom = get_custom_class(
    "AutoUpgradableConfigFactsHelperCustom"
)


class ResourceFactsHelper(
    AutoUpgradableConfigFactsHelperCustom, AutoUpgradableConfigFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(compartment_id=dict(type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="auto_upgradable_config",
        service_client_class=ManagementAgentClient,
        namespace="management_agent",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    else:
        resource_facts_helper.fail()

    module.exit_json(auto_upgradable_config=result)


if __name__ == "__main__":
    main()
