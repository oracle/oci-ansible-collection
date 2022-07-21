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
module: oci_database_management_snapshot_actions
short_description: Perform actions on a Snapshot resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a Snapshot resource in Oracle Cloud Infrastructure
    - For I(action=generate_awr), creates an AWR snapshot for the target database.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    managed_database_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm) of the Managed Database.
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the Snapshot.
        type: str
        required: true
        choices:
            - "generate_awr"
extends_documentation_fragment: [ oracle.oci.oracle ]
"""

EXAMPLES = """
- name: Perform action generate_awr on snapshot
  oci_database_management_snapshot_actions:
    # required
    managed_database_id: "ocid1.manageddatabase.oc1..xxxxxxEXAMPLExxxxxx"
    action: generate_awr

"""

RETURN = """
snapshot_details:
    description:
        - Details of the Snapshot resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        snapshot_id:
            description:
                - The ID of the beginning AWR snapshot.
            returned: on success
            type: int
            sample: 56
    sample: {
        "snapshot_id": 56
    }
"""

from ansible.module_utils.basic import AnsibleModule
from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    get_custom_class,
)

try:
    from oci.database_management import DbManagementClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class SnapshotActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        generate_awr
    """

    @staticmethod
    def get_module_resource_id_param():
        return "managed_database_id"

    def get_module_resource_id(self):
        return self.module.params.get("managed_database_id")

    def generate_awr(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.generate_awr_snapshot,
            call_fn_args=(),
            call_fn_kwargs=dict(
                managed_database_id=self.module.params.get("managed_database_id"),
            ),
            waiter_type=oci_wait_utils.NONE_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=self.get_action_desired_states(
                self.module.params.get("action")
            ),
        )


SnapshotActionsHelperCustom = get_custom_class("SnapshotActionsHelperCustom")


class ResourceHelper(SnapshotActionsHelperCustom, SnapshotActionsHelperGen):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=False
    )
    module_args.update(
        dict(
            managed_database_id=dict(aliases=["id"], type="str", required=True),
            action=dict(type="str", required=True, choices=["generate_awr"]),
        )
    )

    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="snapshot",
        service_client_class=DbManagementClient,
        namespace="database_management",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
