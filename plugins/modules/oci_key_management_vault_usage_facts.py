#!/usr/bin/python
# Copyright (c) 2017, 2020 Oracle and/or its affiliates.
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
module: oci_key_management_vault_usage_facts
short_description: Fetches details about a VaultUsage resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a VaultUsage resource in Oracle Cloud Infrastructure
    - Gets the count of keys and key versions in the specified vault to calculate usage against service limits.
version_added: "2.9"
author: Oracle (@oracle)
options:
    vault_id:
        description:
            - The OCID of the vault.
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific vault_usage
  oci_key_management_vault_usage_facts:
    vault_id: ocid1.vault.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
vault_usage:
    description:
        - VaultUsage resource
    returned: on success
    type: complex
    contains:
        key_count:
            description:
                - The number of keys in this vault that persist on a hardware security module (HSM), across all compartments, excluding keys in a `DELETED`
                  state.
            returned: on success
            type: int
            sample: 56
        key_version_count:
            description:
                - The number of key versions in this vault that persist on a hardware security module (HSM), across all compartments, excluding key versions in
                  a `DELETED` state.
            returned: on success
            type: int
            sample: 56
        software_key_count:
            description:
                - The number of keys in this vault that persist on the server, across all compartments, excluding keys in a `DELETED` state.
            returned: on success
            type: int
            sample: 56
        software_key_version_count:
            description:
                - The number of key versions in this vault that persist on the server, across all compartments, excluding key versions in a `DELETED` state.
            returned: on success
            type: int
            sample: 56
    sample: {
        "key_count": 56,
        "key_version_count": 56,
        "software_key_count": 56,
        "software_key_version_count": 56
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.key_management import KmsVaultClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class VaultUsageFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "vault_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_vault_usage, vault_id=self.module.params.get("vault_id"),
        )


VaultUsageFactsHelperCustom = get_custom_class("VaultUsageFactsHelperCustom")


class ResourceFactsHelper(VaultUsageFactsHelperCustom, VaultUsageFactsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(dict(vault_id=dict(aliases=["id"], type="str", required=True),))

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="vault_usage",
        service_client_class=KmsVaultClient,
        namespace="key_management",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(vault_usage=result)


if __name__ == "__main__":
    main()
