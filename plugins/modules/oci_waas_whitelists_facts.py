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
module: oci_waas_whitelists_facts
short_description: Fetches details about one or multiple Whitelists resources in Oracle Cloud Infrastructure
description:
    - Fetches details about one or multiple Whitelists resources in Oracle Cloud Infrastructure
    - Gets the list of whitelists defined in the Web Application Firewall configuration for a WAAS policy.
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
- name: List whitelists
  oci_waas_whitelists_facts:
    waas_policy_id: "ocid1.waaspolicy.oc1..xxxxxxEXAMPLExxxxxx"

"""

RETURN = """
whitelists:
    description:
        - List of Whitelists resources
    returned: on success
    type: complex
    contains:
        name:
            description:
                - The unique name of the whitelist.
            returned: on success
            type: string
            sample: name_example
        addresses:
            description:
                - A set of IP addresses or CIDR notations to include in the whitelist.
            returned: on success
            type: list
            sample: []
        address_lists:
            description:
                - A list of L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of IP address lists to include in the whitelist.
            returned: on success
            type: list
            sample: []
    sample: [{
        "name": "name_example",
        "addresses": [],
        "address_lists": []
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


class WhitelistsFactsHelperGen(OCIResourceFactsHelperBase):
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
            self.client.list_whitelists,
            waas_policy_id=self.module.params.get("waas_policy_id"),
            **optional_kwargs
        )


WhitelistsFactsHelperCustom = get_custom_class("WhitelistsFactsHelperCustom")


class ResourceFactsHelper(WhitelistsFactsHelperCustom, WhitelistsFactsHelperGen):
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
        resource_type="whitelists",
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

    module.exit_json(whitelists=result)


if __name__ == "__main__":
    main()
