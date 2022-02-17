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
module: oci_database_autonomous_database_wallet
short_description: Manage an AutonomousDatabaseWallet resource in Oracle Cloud Infrastructure
description:
    - This module allows the user to update an AutonomousDatabaseWallet resource in Oracle Cloud Infrastructure
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    autonomous_database_id:
        description:
            - The database L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm).
        type: str
        aliases: ["id"]
        required: true
    should_rotate:
        description:
            - Indicates whether to rotate the wallet or not. If `false`, the wallet will not be rotated. The default is `false`.
            - This parameter is updatable.
        type: bool
    state:
        description:
            - The state of the AutonomousDatabaseWallet.
            - Use I(state=present) to update an existing an AutonomousDatabaseWallet.
        type: str
        required: false
        default: 'present'
        choices: ["present"]
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Update autonomous_database_wallet
  oci_database_autonomous_database_wallet:
    # required
    autonomous_database_id: "ocid1.autonomousdatabase.oc1..xxxxxxEXAMPLExxxxxx"

    # optional
    should_rotate: true

"""

RETURN = """
autonomous_database_wallet:
    description:
        - Details of the AutonomousDatabaseWallet resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        lifecycle_state:
            description:
                - The current lifecycle state of the Autonomous Database wallet.
            returned: on success
            type: str
            sample: ACTIVE
        time_rotated:
            description:
                - The date and time the wallet was last rotated.
            returned: on success
            type: str
            sample: "2013-10-20T19:20:30+01:00"
    sample: {
        "lifecycle_state": "ACTIVE",
        "time_rotated": "2013-10-20T19:20:30+01:00"
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIResourceHelperBase,
    get_custom_class,
)

try:
    from oci.work_requests import WorkRequestClient
    from oci.database import DatabaseClient
    from oci.database.models import UpdateAutonomousDatabaseWalletDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class AutonomousDatabaseWalletHelperGen(OCIResourceHelperBase):
    """Supported operations: update and get"""

    def __init__(self, *args, **kwargs):
        super(AutonomousDatabaseWalletHelperGen, self).__init__(*args, **kwargs)
        self.work_request_client = WorkRequestClient(
            self.client._config, **self.client._kwargs
        )

    def get_possible_entity_types(self):
        return super(
            AutonomousDatabaseWalletHelperGen, self
        ).get_possible_entity_types() + [
            "autonomousdatabasewallet",
            "autonomousdatabasewallets",
            "databaseautonomousdatabasewallet",
            "databaseautonomousdatabasewallets",
            "autonomousdatabasewalletresource",
            "autonomousdatabasewalletsresource",
            "wallet",
            "wallets",
            "databasewallet",
            "databasewallets",
            "walletresource",
            "walletsresource",
            "database",
        ]

    def get_module_resource_id_param(self):
        return "autonomous_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("autonomous_database_id")

    def get_get_fn(self):
        return self.client.get_autonomous_database_wallet

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_autonomous_database_wallet,
            autonomous_database_id=self.module.params.get("autonomous_database_id"),
        )

    def get_update_model_class(self):
        return UpdateAutonomousDatabaseWalletDetails

    def update_resource(self):
        update_details = self.get_update_model()
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.update_autonomous_database_wallet,
            call_fn_args=(),
            call_fn_kwargs=dict(
                autonomous_database_id=self.module.params.get("autonomous_database_id"),
                update_autonomous_database_wallet_details=update_details,
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation=oci_common_utils.UPDATE_OPERATION_KEY,
            waiter_client=self.work_request_client,
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


AutonomousDatabaseWalletHelperCustom = get_custom_class(
    "AutonomousDatabaseWalletHelperCustom"
)


class ResourceHelper(
    AutonomousDatabaseWalletHelperCustom, AutonomousDatabaseWalletHelperGen
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            autonomous_database_id=dict(aliases=["id"], type="str", required=True),
            should_rotate=dict(type="bool"),
            state=dict(type="str", default="present", choices=["present"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="autonomous_database_wallet",
        service_client_class=DatabaseClient,
        namespace="database",
    )

    result = dict(changed=False)

    if resource_helper.is_update():
        result = resource_helper.update()

    module.exit_json(**result)


if __name__ == "__main__":
    main()
