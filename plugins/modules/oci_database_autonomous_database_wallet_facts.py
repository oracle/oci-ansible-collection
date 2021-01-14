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
module: oci_database_autonomous_database_wallet_facts
short_description: Fetches details about a AutonomousDatabaseWallet resource in Oracle Cloud Infrastructure
description:
    - Fetches details about a AutonomousDatabaseWallet resource in Oracle Cloud Infrastructure
    - Gets the wallet details for the specified Autonomous Database.
version_added: "2.9"
author: Oracle (@oracle)
options:
    autonomous_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Get a specific autonomous_database_wallet
  oci_database_autonomous_database_wallet_facts:
    autonomous_database_id: ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx

"""

RETURN = """
autonomous_database_wallet:
    description:
        - AutonomousDatabaseWallet resource
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The current lifecycle state of the Autonomous Database wallet.
            returned: on success
            type: string
            sample: ACTIVE
        time_rotated:
            description:
                - The date and time the wallet was last rotated.
            returned: on success
            type: string
            sample: 2013-10-20T19:20:30+01:00
    sample: {
        "lifecycle_state": "ACTIVE",
        "time_rotated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import oci_common_utils
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceFactsHelperBase,
    get_custom_class,
)

try:
    from oci.database import DatabaseClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDatabaseWalletFactsHelperGen(OCIResourceFactsHelperBase):
    """Supported operations: get"""

    def get_required_params_for_get(self):
        return [
            "autonomous_database_id",
        ]

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database_wallet,
            autonomous_database_id=self.module.params.get("autonomous_database_id"),
        )


AutonomousDatabaseWalletFactsHelperCustom = get_custom_class(
    "AutonomousDatabaseWalletFactsHelperCustom"
)


class ResourceFactsHelper(
    AutonomousDatabaseWalletFactsHelperCustom, AutonomousDatabaseWalletFactsHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec()
    module_args.update(
        dict(autonomous_database_id=dict(aliases=["id"], type="str", required=True),)
    )

    module = AnsibleModule(argument_spec=module_args)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_facts_helper = ResourceFactsHelper(
        module=module,
        resource_type="autonomous_database_wallet",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = []

    if resource_facts_helper.is_get():
        result = resource_facts_helper.get()
    elif resource_facts_helper.is_list():
        result = resource_facts_helper.list()
    else:
        resource_facts_helper.fail()

    module.exit_json(autonomous_database_wallet=result)


if __name__ == "__main__":
    main()
