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
module: oci_waas_good_bots_facts
short_description: Fetches details about one or multiple GoodBots resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple GoodBots resources in Oracle Cloud Infrastructure
    - Gets the list of good bots defined in the Web Application Firewall configuration for a WAAS policy.
    - The list is sorted by `key`, in ascending order.
version_added: "2.9"
author: Oracle (@oracle)
options:
    waas_policy_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the WAAS policy.
        type: str
        required: true
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_name_option ]
"""

EXAMPLES = """
- name: List good_bots
  oci_waas_good_bots_facts:
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
good_bots:
    description:
        - List of GoodBots resources
    returned: on success
    type: complex
    contains:
        key:
            description:
                - The unique key for the bot.
            returned: on success
            type: string
            sample: key_example
        name:
            description:
                - The bot name.
            returned: on success
            type: string
            sample: name_example
        is_enabled:
            description:
                - Enables or disables the bot.
            returned: on success
            type: bool
            sample: true
        description:
            description:
                - The description of the bot.
            returned: on success
            type: string
            sample: description_example
    sample: [{
        "key": "key_example",
        "name": "name_example",
        "is_enabled": true,
        "description": "description_example"
    }]
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.waas import WaasClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class GoodBotsFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: list"""

    def get_required_params_for_list(self):
        return [
            "waas_policy_id",
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
            self.client.list_good_bots,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


GoodBotsFactsHelperCustom = get_custom_class("GoodBotsFactsHelperCustom")


class ResourceFactsHelper(GoodBotsFactsHelperCustom, GoodBotsFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(waas_policy_id=dict(type="str", required=True), name=dict(type="str"),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="good_bots",
        service_client_class=WaasClient,
        namespace="waas",
    )

    result = []

    if resource_facts_helper.is_get():
        result = [resource_facts_helper.get()]
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(good_bots=result)


if __name__ == "__main__":
    main()
