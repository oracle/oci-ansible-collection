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
module: oci_os_management_hub_management_station_actions
short_description: Perform actions on a ManagementStation resource in Oracle Cloud Infrastructure
description:
    - Perform actions on a ManagementStation resource in Oracle Cloud Infrastructure
    - For I(action=change_compartment), moves a managment station to a different compartment.
    - For I(action=refresh_management_station_config), refreshes the list of software sources mirrored by the management station to support the associated
      instances.
    - For I(action=synchronize_mirrors), synchronize the specified software sources mirrors on the management station.
version_added: "2.9.0"
author: Oracle (@oracle)
options:
    compartment_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment to move the management station to.
            - Required for I(action=change_compartment).
        type: str
    management_station_id:
        description:
            - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station.
        type: str
        aliases: ["id"]
        required: true
    software_source_list:
        description:
            - List of Software Source OCIDs to synchronize
            - Required for I(action=synchronize_mirrors).
        type: list
        elements: str
    action:
        description:
            - The action to perform on the ManagementStation.
        type: str
        required: true
        choices:
            - "change_compartment"
            - "refresh_management_station_config"
            - "synchronize_mirrors"
extends_documentation_fragment: [ oracle.oci.oracle, oracle.oci.oracle_wait_options ]
"""

EXAMPLES = """
- name: Perform action change_compartment on management_station
  oci_os_management_hub_management_station_actions:
    # required
    compartment_id: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    action: change_compartment

- name: Perform action refresh_management_station_config on management_station
  oci_os_management_hub_management_station_actions:
    # required
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    action: refresh_management_station_config

- name: Perform action synchronize_mirrors on management_station
  oci_os_management_hub_management_station_actions:
    # required
    management_station_id: "ocid1.managementstation.oc1..xxxxxxEXAMPLExxxxxx"
    software_source_list: [ "software_source_list_example" ]
    action: synchronize_mirrors

"""

RETURN = """
management_station:
    description:
        - Details of the ManagementStation resource acted upon by the current operation
    returned: on success
    type: complex
    contains:
        id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the management station.
            returned: on success
            type: str
            sample: "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx"
        managed_instance_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the instance that is acting as the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx"
        compartment_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the compartment that contains the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx"
        scheduled_job_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the scheduled job for the mirror sync.
            returned: on success
            type: str
            sample: "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx"
        profile_id:
            description:
                - The L(OCID,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm) of the registration profile used for the management
                  station.
            returned: on success
            type: str
            sample: "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx"
        display_name:
            description:
                - A user-friendly name for the management station.
            returned: on success
            type: str
            sample: display_name_example
        description:
            description:
                - User-specified description for the management station.
            returned: on success
            type: str
            sample: description_example
        hostname:
            description:
                - Hostname of the management station.
            returned: on success
            type: str
            sample: hostname_example
        overall_state:
            description:
                - Current state of the mirror sync for the management station.
            returned: on success
            type: str
            sample: NORMAL
        overall_percentage:
            description:
                - A decimal number representing the progress of the current mirror sync.
            returned: on success
            type: int
            sample: 56
        mirror_capacity:
            description:
                - A decimal number representing the amount of mirror capacity used by the sync.
            returned: on success
            type: int
            sample: 56
        total_mirrors:
            description:
                - The number of software sources that the station is mirroring.
            returned: on success
            type: int
            sample: 56
        mirror_sync_status:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                unsynced:
                    description:
                        - Total number of software sources that have not yet been synced.
                    returned: on success
                    type: int
                    sample: 56
                queued:
                    description:
                        - Total number of software sources that are queued for sync.
                    returned: on success
                    type: int
                    sample: 56
                syncing:
                    description:
                        - Total number of software sources currently syncing.
                    returned: on success
                    type: int
                    sample: 56
                synced:
                    description:
                        - Total number of software sources that successfully synced.
                    returned: on success
                    type: int
                    sample: 56
                failed:
                    description:
                        - Total number of software sources that failed to sync.
                    returned: on success
                    type: int
                    sample: 56
        proxy:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                is_enabled:
                    description:
                        - Indicates if the proxy should be enabled or disabled. Default is enabled.
                    returned: on success
                    type: bool
                    sample: true
                hosts:
                    description:
                        - List of hosts.
                    returned: on success
                    type: list
                    sample: []
                port:
                    description:
                        - Listening port used for the proxy.
                    returned: on success
                    type: str
                    sample: port_example
                forward:
                    description:
                        - The URL the proxy will forward to.
                    returned: on success
                    type: str
                    sample: forward_example
        mirror:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                directory:
                    description:
                        - Path to the data volume on the management station where software source mirrors are stored.
                    returned: on success
                    type: str
                    sample: directory_example
                port:
                    description:
                        - Default mirror listening port for http.
                    returned: on success
                    type: str
                    sample: port_example
                sslport:
                    description:
                        - Default mirror listening port for https.
                    returned: on success
                    type: str
                    sample: sslport_example
                sslcert:
                    description:
                        - Path to the SSL cerfificate.
                    returned: on success
                    type: str
                    sample: sslcert_example
        health:
            description:
                - ""
            returned: on success
            type: complex
            contains:
                state:
                    description:
                        - Overall health status of the management station.
                    returned: on success
                    type: str
                    sample: HEALTHY
                description:
                    description:
                        - Explanation of the health status.
                    returned: on success
                    type: str
                    sample: description_example
        lifecycle_state:
            description:
                - The current state of the management station.
            returned: on success
            type: str
            sample: CREATING
        freeform_tags:
            description:
                - "Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Department\\": \\"Finance\\"}`"
            returned: on success
            type: dict
            sample: {'Department': 'Finance'}
        defined_tags:
            description:
                - "Defined tags for this resource. Each key is predefined and scoped to a namespace.
                  For more information, see L(Resource Tags,https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm).
                  Example: `{\\"Operations\\": {\\"CostCenter\\": \\"42\\"}}`"
            returned: on success
            type: dict
            sample: {'Operations': {'CostCenter': 'US'}}
        system_tags:
            description:
                - "System tags for this resource. Each key is predefined and scoped to a namespace.
                  Example: `{\\"orcl-cloud\\": {\\"free-tier-retained\\": \\"true\\"}}`"
            returned: on success
            type: dict
            sample: {}
    sample: {
        "id": "ocid1.resource.oc1..xxxxxxEXAMPLExxxxxx",
        "managed_instance_id": "ocid1.managedinstance.oc1..xxxxxxEXAMPLExxxxxx",
        "compartment_id": "ocid1.compartment.oc1..xxxxxxEXAMPLExxxxxx",
        "scheduled_job_id": "ocid1.scheduledjob.oc1..xxxxxxEXAMPLExxxxxx",
        "profile_id": "ocid1.profile.oc1..xxxxxxEXAMPLExxxxxx",
        "display_name": "display_name_example",
        "description": "description_example",
        "hostname": "hostname_example",
        "overall_state": "NORMAL",
        "overall_percentage": 56,
        "mirror_capacity": 56,
        "total_mirrors": 56,
        "mirror_sync_status": {
            "unsynced": 56,
            "queued": 56,
            "syncing": 56,
            "synced": 56,
            "failed": 56
        },
        "proxy": {
            "is_enabled": true,
            "hosts": [],
            "port": "port_example",
            "forward": "forward_example"
        },
        "mirror": {
            "directory": "directory_example",
            "port": "port_example",
            "sslport": "sslport_example",
            "sslcert": "sslcert_example"
        },
        "health": {
            "state": "HEALTHY",
            "description": "description_example"
        },
        "lifecycle_state": "CREATING",
        "freeform_tags": {'Department': 'Finance'},
        "defined_tags": {'Operations': {'CostCenter': 'US'}},
        "system_tags": {}
    }
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
    from oci.os_management_hub.models import ChangeManagementStationCompartmentDetails
    from oci.os_management_hub.models import SynchronizeMirrorsDetails

    HAS_OCI_PY_SDK = True
except ImportError:
    HAS_OCI_PY_SDK = False


class OsManagementHubManagementStationActionsHelperGen(OCIActionsHelperBase):
    """
    Supported actions:
        change_compartment
        refresh_management_station_config
        synchronize_mirrors
    """

    def get_waiter_client(self):
        return oci_config_utils.create_service_client(self.module, WorkRequestClient)

    @staticmethod
    def get_module_resource_id_param():
        return "management_station_id"

    def get_module_resource_id(self):
        return self.module.params.get("management_station_id")

    def get_get_fn(self):
        return self.client.get_management_station

    def get_resource(self):
        return oci_common_utils.call_with_backoff(
            self.client.get_management_station,
            management_station_id=self.module.params.get("management_station_id"),
        )

    def change_compartment(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, ChangeManagementStationCompartmentDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.change_management_station_compartment,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_station_id=self.module.params.get("management_station_id"),
                change_management_station_compartment_details=action_details,
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

    def refresh_management_station_config(self):
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.refresh_management_station_config,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_station_id=self.module.params.get("management_station_id"),
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

    def synchronize_mirrors(self):
        action_details = oci_common_utils.convert_input_data_to_model_class(
            self.module.params, SynchronizeMirrorsDetails
        )
        return oci_wait_utils.call_and_wait(
            call_fn=self.client.synchronize_mirrors,
            call_fn_args=(),
            call_fn_kwargs=dict(
                management_station_id=self.module.params.get("management_station_id"),
                synchronize_mirrors_details=action_details,
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


OsManagementHubManagementStationActionsHelperCustom = get_custom_class(
    "OsManagementHubManagementStationActionsHelperCustom"
)


class ResourceHelper(
    OsManagementHubManagementStationActionsHelperCustom,
    OsManagementHubManagementStationActionsHelperGen,
):
    pass


def main():
    module_args = oci_common_utils.get_common_arg_spec(
        supports_create=False, supports_wait=True
    )
    module_args.update(
        dict(
            compartment_id=dict(type="str"),
            management_station_id=dict(aliases=["id"], type="str", required=True),
            software_source_list=dict(type="list", elements="str"),
            action=dict(
                type="str",
                required=True,
                choices=[
                    "change_compartment",
                    "refresh_management_station_config",
                    "synchronize_mirrors",
                ],
            ),
        )
    )

    module = OCIAnsibleModule(argument_spec=module_args, supports_check_mode=True)

    if not HAS_OCI_PY_SDK:
        module.fail_json(msg="oci python sdk required for this module.")

    resource_helper = ResourceHelper(
        module=module,
        resource_type="management_station",
        service_client_class=ManagementStationClient,
        namespace="os_management_hub",
    )

    result = resource_helper.perform_action(module.params.get("action"))

    module.exit_json(**result)


if __name__ == "__main__":
    main()
