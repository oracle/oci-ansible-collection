#!/usr/bin/python
# Copyright (c) 2020, 2025 Oracle and/or its affiliates.
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
module: oci_os_management_hub_management_stations_mirror_actions
short_description: Perform actions on a ManagementStationsMirror resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagementStationsMirror resource in Oracle Cloud Infrastructure
    - For I(action=synchronize_single_mirrors), synchronize the specified software source mirrors on the management station.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    management_station_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station.
        type: str
        required: true
    mirror_id:
        description:
            - Unique Software Source identifier
        type: str
        aliases: ["id"]
        required: true
    action:
        description:
            - The action to perform on the ManagementStationsMirror.
        type: str
        required: true
        choices:
            - "synchronize_single_mirrors"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action synchronize_single_mirrors on management_stations_mirror
  oci_os_management_hub_management_stations_mirror_actions:
    # required
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    mirror_id: "ocid1.mirror.oc1..xxxxxxEXAMPLExxxxxx"
    action: synchronize_single_mirrors

"""


from ansible_collections.oracle.oci.plugins.module_utils import (
    oci_common_utils,
    oci_wait_utils,
    oci_config_utils,
)
from ansible_collections.oracle.oci.plugins.module_utils.oci_resource_utils import (
    OCIActionsHelperBase,
    OCIAnsibleModule,
    get_custom_class,
)

try:
    from oci.os_management_hub import WorkRequestClient
    from oci.os_management_hub import ManagementStationClient

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubManagementStationsMirrorActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        synchronize_single_mirrors
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "mirror_id"

    def get_module_resource_id(self):
        return self.module.params.get("mirror_id")

    def synchronize_single_mirrors(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.synchronize_single_mirrors,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_station_id=self.module.params.get("management_station_id"),
                mirror_id=self.module.params.get("mirror_id"),
            ),
            waiter_type=oci_wait_utils.WORK_REQUEST_WAITER_KEY,
            operation="{0}_{1}".format(
                self.module.params.get("action").upper(),
                oci_common_utils.ACTION_OPERATION_KEY,
            ),
            waiter_client=self.get_waiter_client(),
            resource_helper=self,
            wait_for_states=oci_common_utils.get_work_request_completed_states(),
        )


OsManagementHubManagementStationsMirrorActionsHelperCustom = get_custom_class(
    "OsManagementHubManagementStationsMirrorActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubManagementStationsMirrorActionsHelperCustom,
    OsManagementHubManagementStationsMirrorActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            management_station_id=dict(type="str", required=True),
            mirror_id=dict(aliases=["id"], type="str", required=True),
            action=dict(
                type="str", required=True, choices=["synchronize_single_mirrors"]
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_stations_mirror",
        service_client_class=ManagementStationClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
